#!/usr/bin/env python3
"""Validate coverage and structural fidelity of the English Markdown export."""

from __future__ import annotations

import csv
import html
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SOURCE = Path("/opt/data/repos/inklusion-blog/public/blog")
ARTICLES = REPO / "articles"
REPORT = REPO / "inventory.csv"


def visible_text(source: str) -> str:
    source = re.sub(r'<script\b.*?</script>', ' ', source, flags=re.I | re.S)
    source = re.sub(r'<style\b.*?</style>', ' ', source, flags=re.I | re.S)
    source = re.sub(r'<[^>]+>', ' ', source)
    return re.sub(r'\s+', ' ', html.unescape(source)).strip()


def frontmatter_value(markdown: str, key: str) -> str:
    match = re.search(rf'^{re.escape(key)}:\s*"(.*)"\s*$', markdown, re.M)
    return match.group(1).replace('\\"', '"') if match else ""


def main() -> int:
    source_files = sorted(SOURCE.glob("*/index.html"))
    output_files = sorted(ARTICLES.glob("*.md"))
    failures: list[str] = []
    rows: list[dict[str, str | int]] = []

    source_slugs = {p.parent.name for p in source_files}
    output_slugs = {p.stem for p in output_files}
    if source_slugs != output_slugs:
        for slug in sorted(source_slugs - output_slugs):
            failures.append(f"missing translation: {slug}")
        for slug in sorted(output_slugs - source_slugs):
            failures.append(f"unexpected translation: {slug}")

    for source_path in source_files:
        slug = source_path.parent.name
        output_path = ARTICLES / f"{slug}.md"
        if not output_path.exists():
            continue
        source = source_path.read_text(encoding="utf-8")
        markdown = output_path.read_text(encoding="utf-8")
        article_match = re.search(r'<article\s+class="article"[^>]*>(.*?)</article>', source, re.I | re.S)
        article = article_match.group(1) if article_match else source
        source_words = len(visible_text(article).split())
        markdown_body = re.sub(r'^---.*?---\s*', '', markdown, flags=re.S)
        output_words = len(re.sub(r'[#*_>`\[\]()]', ' ', markdown_body).split())
        ratio = output_words / max(source_words, 1)
        source_h2 = len(re.findall(r'<h2\b', article, re.I))
        source_h3 = len(re.findall(r'<h3\b', article, re.I))
        output_h2 = len(re.findall(r'^## ', markdown, re.M))
        output_h3 = len(re.findall(r'^### ', markdown, re.M))
        source_li = len(re.findall(r'<li\b', article, re.I))
        output_li = len(re.findall(r'^\s*(?:[-*]|\d+\.)\s+', markdown, re.M))
        title = frontmatter_value(markdown, "title")
        description = frontmatter_value(markdown, "description")
        fm_slug = frontmatter_value(markdown, "sourceSlug")
        fm_url = frontmatter_value(markdown, "sourceUrl")

        if not markdown.startswith("---\n"):
            failures.append(f"{slug}: missing YAML front matter")
        if fm_slug != slug:
            failures.append(f"{slug}: sourceSlug mismatch")
        if not title or not description:
            failures.append(f"{slug}: missing translated title or description")
        if fm_url != f"https://inklusion-blog.vercel.app/blog/{slug}/":
            failures.append(f"{slug}: sourceUrl mismatch")
        if not re.search(r'^# ', markdown, re.M):
            failures.append(f"{slug}: missing H1")
        if output_h2 < source_h2:
            failures.append(f"{slug}: H2 omission ({output_h2} < {source_h2})")
        if output_h3 < source_h3:
            failures.append(f"{slug}: H3 omission ({output_h3} < {source_h3})")
        if output_li < source_li:
            failures.append(f"{slug}: list-item omission ({output_li} < {source_li})")
        if ratio < 0.65 or ratio > 1.45:
            failures.append(f"{slug}: suspicious word-count ratio {ratio:.2f}")
        if "```" in markdown:
            failures.append(f"{slug}: unexpected code fence")

        rows.append({
            "source_slug": slug,
            "english_title": title,
            "date_published": frontmatter_value(markdown, "datePublished"),
            "source_url": fm_url,
            "file": f"articles/{slug}.md",
            "source_words": source_words,
            "english_words": output_words,
            "word_ratio": f"{ratio:.2f}",
            "status": "translated",
        })

    with REPORT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "source_slug", "english_title", "date_published", "source_url", "file",
            "source_words", "english_words", "word_ratio", "status",
        ], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"source={len(source_files)} translated={len(output_files)} inventoried={len(rows)}")
    print(f"validation_failures={len(failures)}")
    for failure in failures:
        print(f"- {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
