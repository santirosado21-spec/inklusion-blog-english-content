#!/usr/bin/env python3
"""Translate Inklusion's Spanish HTML articles into review-ready English Markdown.

Requires OPENROUTER_API_KEY in the environment. Existing output files are skipped,
so interrupted runs can be resumed safely.
"""

from __future__ import annotations

import concurrent.futures
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

SOURCE_ROOT = Path(os.environ.get("INKLUSION_SOURCE", "/opt/data/repos/inklusion-blog/public/blog"))
OUTPUT_ROOT = Path(__file__).resolve().parents[1] / "articles"
MODEL = os.environ.get("TRANSLATION_MODEL", "anthropic/claude-sonnet-4.6")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
WORKERS = int(os.environ.get("TRANSLATION_WORKERS", "4"))

SYSTEM_PROMPT = """You are a senior English-language editor specializing in disability inclusion, accessibility, HR, WCAG, and responsible business communication. Translate faithfully from Mexican Spanish into clear, natural, professional English. Do not summarize, omit, embellish, update, or fact-check the source. Preserve every substantive claim, caveat, example, checklist item, FAQ, source link, and call to action. Preserve Mexico-specific and jurisdiction-specific distinctions exactly. Use respectful disability language (generally 'people with disabilities' unless context calls for another established term). Keep Inklusion as a brand name. Return only the requested Markdown, without code fences or commentary."""


def extract(html_text: str, slug: str) -> tuple[str, str, str, str]:
    title_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html_text, re.I)
    description = html.unescape(title_match.group(1)) if title_match else ""
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_text, re.I | re.S)
    title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip() if h1_match else slug
    title = html.unescape(title)
    date_match = re.search(r'"datePublished"\s*:\s*"([^"]+)"', html_text)
    date = date_match.group(1) if date_match else ""
    article_match = re.search(r'<article\s+class="article"[^>]*>(.*?)</article>', html_text, re.I | re.S)
    if not article_match:
        raise ValueError("article body not found")
    body = article_match.group(1).strip()
    return title, description, date, body


def build_prompt(slug: str, title: str, description: str, date: str, body: str) -> str:
    source_url = f"https://inklusion-blog.vercel.app/blog/{slug}/"
    return f"""Translate the complete article below into English Markdown.

Required output format:
---
title: "English title"
description: "English meta description"
datePublished: "{date}"
sourceSlug: "{slug}"
sourceUrl: "{source_url}"
language: "en"
---

Then include the FULL translated article body. Start the body with the translated H1 title as `# ...`. Convert the supplied HTML faithfully to Markdown:
- Preserve all paragraphs and their order.
- Preserve H2/H3 hierarchy, lists, blockquotes, bold emphasis, and links.
- Translate link text but keep external URLs unchanged.
- For internal `/blog/.../` links, convert the URL to the absolute original Spanish URL at `https://inklusion-blog.vercel.app/blog/.../`.
- Include the CTA panel content at the end as a `##` section.
- Do not include navigation, footer, table of contents, reading-time pills, or schema markup.
- Do not add translator notes or commentary.
- YAML values must be valid and double-quoted; escape embedded double quotes.

Source title: {title}
Source description: {description}

ARTICLE HTML:
{body}
"""


def request_translation(prompt: str, attempts: int = 5) -> str:
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY is not set")
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.1,
        "max_tokens": 16000,
    }
    data = json.dumps(payload).encode("utf-8")
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        req = urllib.request.Request(
            API_URL,
            data=data,
            method="POST",
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/santirosado21-spec",
                "X-Title": "Inklusion English Editorial Export",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=300) as response:
                result = json.load(response)
            text = result["choices"][0]["message"]["content"].strip()
            text = re.sub(r'^```(?:markdown)?\s*', '', text)
            text = re.sub(r'\s*```$', '', text)
            if not text.startswith("---") or "sourceSlug:" not in text or len(text) < 1500:
                raise ValueError("model returned incomplete or malformed Markdown")
            return text.rstrip() + "\n"
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, KeyError, ValueError) as exc:
            last_error = exc
            if attempt == attempts:
                break
            time.sleep(min(30, 2 ** attempt))
    raise RuntimeError(f"translation failed after {attempts} attempts: {last_error}")


def translate_one(path: Path) -> tuple[str, str]:
    slug = path.parent.name
    output = OUTPUT_ROOT / f"{slug}.md"
    if output.exists() and output.stat().st_size > 1500:
        return slug, "skipped"
    source = path.read_text(encoding="utf-8")
    title, description, date, body = extract(source, slug)
    translated = request_translation(build_prompt(slug, title, description, date, body))
    output.write_text(translated, encoding="utf-8")
    return slug, "translated"


def main() -> int:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in SOURCE_ROOT.glob("*/index.html") if p.parent.name != "blog")
    print(f"source_articles={len(files)} model={MODEL} workers={WORKERS}", flush=True)
    failures: list[tuple[str, str]] = []
    completed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        future_map = {pool.submit(translate_one, path): path for path in files}
        for future in concurrent.futures.as_completed(future_map):
            path = future_map[future]
            try:
                slug, status = future.result()
                completed += 1
                print(f"[{completed}/{len(files)}] {status}: {slug}", flush=True)
            except Exception as exc:
                failures.append((path.parent.name, str(exc)))
                print(f"ERROR {path.parent.name}: {exc}", file=sys.stderr, flush=True)
    print(f"completed={completed} failures={len(failures)}", flush=True)
    for slug, error in failures:
        print(f"failure: {slug}: {error}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
