# research/ — Southland landscape from primary sources

**Plan Step:** Step 1 (Part A — evidence)
**Lead:** Karl
**Serves:** the knowledge graph in `graph/`, and ultimately the report's landscape section.

## What this is

The primary-source corpus for the Southland data-centre controversy and NZ's electricity
system. Every source that any claim in the report leans on lives here — one Markdown file
per source in `sources/`, registered in `corpus.csv`.

## Layout

- `sources/` — one `.md` per primary source, with the frontmatter schema documented in
  [`sources/README.md`](sources/README.md).
- `corpus.csv` — the source register: a flat index of every source with the claim IDs it
  supports. This is what `graph/loaders/load_corpus.py` reads.
- `notes/` — working notes, synthesis, reading summaries. Not sources; thinking.

## The rule that governs this directory

**Primary sources only** for the Southland landscape — coverage, submissions, official
statements — not summaries of summaries. Every source carries a `url` and a `retrieved`
date so a reader can check it. See [`docs/methodology.md`](../docs/methodology.md).

## Definition of done (Step 1)

- The Southland controversy is mapped from primary sources: who is proposing what, who is
  objecting, and on what specific grounds.
- Each source is a file in `sources/` with complete frontmatter and a row in `corpus.csv`.
- The claims and numbers drawn from them are loaded into the Neo4j graph (`graph/`), each
  linked back to its Source — so no number in the graph is untraceable.
