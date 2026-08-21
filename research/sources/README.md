# research/sources/ — one file per primary source

Each primary source is a single Markdown file with YAML frontmatter, then your notes and
relevant quotes below the frontmatter. The frontmatter is the machine-readable part that
`graph/loaders/load_corpus.py` and `corpus.csv` depend on, so the field names matter.

## Frontmatter schema

```yaml
---
id: southland-es-submission-2025-04       # unique slug, also the source_id in corpus.csv
title: "Submission on the Makarewa data centre resource consent"
publisher: "Environment Southland"          # who published it
date: 2025-04-12                            # publication date (YYYY-MM-DD)
url: "https://example.org/the-actual-source"# where it lives (required — this is the trace)
retrieved: 2026-08-20                       # date YOU accessed it (YYYY-MM-DD)
type: submission                            # coverage | submission | official-statement | dataset | report | other
camp: climate-first                         # climate-first | growth-first | neutral | official
---
```

## Rules

- **`url` and `retrieved` are mandatory.** They are what make the source checkable. No URL,
  no source.
- **Primary sources only** for the Southland landscape (see the directory README).
- `type` and `camp` are controlled vocabularies — stick to the values above so the graph
  loader can filter cleanly. Extend the vocabulary here first if you genuinely need a new
  value.
- Below the frontmatter: capture the exact quotes and page/section references you rely on,
  not a paraphrase. Paraphrase belongs in `../notes/`.

See `example-0001-template.md` in this folder for a filled-in template.
