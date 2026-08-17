# Inklusion Blog — English Editorial Export

This repository contains the complete English translation of Inklusion's Spanish-language blog archive as of **August 17, 2026**.

## Delivery status

- **Source articles identified:** 34
- **English translations:** 34
- **Coverage:** 100%
- **Format:** one review-ready Markdown file per article
- **Validation:** structural and coverage checks passed with no failures

## Repository structure

- `articles/` — complete English translations in Markdown
- `inventory.csv` — article-by-article manifest with title, publication date, original URL, file path, and word-count comparison
- `scripts/translate_articles.py` — reproducible translation workflow; existing files are skipped on reruns
- `scripts/validate_export.py` — coverage and structural-fidelity validator

## Editorial approach

The translations were prepared for professional English-language review and reuse. They preserve:

- all substantive paragraphs and their original order;
- headings, lists, checklists, FAQs, blockquotes, links, and calls to action;
- source citations and original URLs;
- Mexico-specific legal and operational context;
- distinctions between Mexican, U.S., European, Ukrainian, and international jurisdictions;
- WCAG, disability inclusion, accessibility, and HR terminology;
- Inklusion's direct, practical editorial tone.

The translations do not intentionally update, summarize, expand, or fact-check the Spanish originals. Any future publication should still receive final review from Inklusion for brand voice, legal context, and market-specific terminology.

## File naming

Files retain the original Spanish slug. This is intentional: it creates a one-to-one audit trail between every English translation and the currently published Spanish article. Each file also includes front matter with:

- English title and description
- publication date
- original source slug
- original public URL
- language code

## Validation

Run:

```bash
python3 scripts/validate_export.py
```

The validator confirms:

- all 34 source articles have one corresponding translation;
- required front matter is present;
- original source links and slugs match;
- H1/H2/H3 structure is preserved;
- lists have not been omitted;
- translated word counts remain within a reasonable fidelity range;
- no accidental code fences or malformed exports remain.

## Editorial ownership

The underlying article content belongs to Inklusion. This repository is an editorial handoff for review and authorized reuse; it is not an open-source content license.
