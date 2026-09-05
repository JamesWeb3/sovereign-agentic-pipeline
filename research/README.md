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
  supports.
- `claims.csv` — the claim register: one row per claim, its topic, and what it is about.
  A claim id used in `corpus.csv` must exist here.
- `numbers.csv` — the number register: one row per figure, tied to the claim it evidences
  and the source it came from. `source_id` is mandatory, and `basis` says what the figure
  actually measures.
- `entities.csv` — the things a claim can be about: facilities, organisations, policies.
  A claim's `about_id` must exist here, or the graph holds a node with an id and no name.
- `notes/` — working notes, synthesis, reading summaries. Not sources; thinking.

A source's `camp` and `type` are deliberately **not** in `corpus.csv`. They live in the
source file's own frontmatter, which `tests/test_research_sources.py` already checks
against the folder it sits in, and the loader reads them from there. A second copy in the
register would be a value that can disagree with itself.

All three registers are read by `graph/loaders/load_corpus.py`, which refuses to write
anything if a reference does not resolve.

### Why numbers live in their own register

**A claim carrying two numbers is the normal case, not an error.** The Makarewa consent
allows 220,752,000 L/yr; Datagrid says it expects to use 66,000,000. Neither is wrong —
one is a consent limit and the other an operator expectation — so both are stored, each
with its `basis`, and `graph/queries/contested_numbers.cypher` shows them side by side.
Picking a winner would delete the finding, which is the failure mode a spreadsheet forces
and a graph does not.

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
