# research/sources/ — one file per primary source

Each primary source is a single Markdown file with YAML frontmatter, then your notes and
relevant quotes below the frontmatter. The frontmatter is the machine-readable part that
`graph/loaders/load_corpus.py` and `corpus.csv` depend on, so the field names matter.

## Layout

Sources are filed in a subfolder named for their `camp`, so the shape of the evidence base
is visible from the directory listing alone:

```
sources/
  climate-first/   (empty - see its README, this gap is a finding)
  growth-first/    the applicant's own filings and announcements
  neutral/         news coverage carrying voices from more than one side
  official/        regulators and decision-makers speaking in their own documents
```

The folder must match the `camp` field in the file's frontmatter. `camp` stays the
authoritative value - `corpus.csv` and the graph loader read that, never the path - so if
you reclassify a source, change the frontmatter and move the file in the same commit.

`README.md` and `example-0001-template.md` stay at the top level: neither is a source.

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

## Evidence role: primary or secondary

Directly below the frontmatter, every source carries one line saying whether it is primary
or secondary evidence, and why:

```markdown
**Evidence role:** primary — Southland District Council's own decision on RMA/2025/53212.
```

- **primary** — the document itself, speaking in its own voice: an application, a consent, a
  decision, a commissioned report as lodged, an organisation's own release.
- **secondary** — an account of a document or an event: news coverage, a summary, a report
  of what someone else said.

This lives in the body rather than the frontmatter deliberately: the frontmatter is the
machine-readable contract that `corpus.csv` and `load_corpus.py` depend on, and it is not
changing. `tests/test_research_sources.py` checks the line is present and uses one of the
two values, so a new source cannot skip it.

Coverage is almost always `secondary`, but it can be the *only* record of an event it
witnessed — a public meeting, an interview. Say so on the same line ('Primary only for...')
rather than promoting the whole source to primary. A figure that originated in a consent
document should be cited to that document, never to the article that repeated it.

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
