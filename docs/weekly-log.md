# Weekly log

One row per week. Keep it terse — this is the "what actually happened" record that sits
alongside the commit history. Blocked items carry to the next week until resolved.

| Week | Who | Did | Found | Blocked |
|---|---|---|---|---|
| w/c 2026-08-17 | James | Scaffolded the repo: full Part A tree, Neo4j + schema, CI, methodology. Public from commit one. | Repo is the only blocking dependency in the plan; unblocked now. | Karl's GitHub handle needed before the collaborator invite can go out — collect on the 21 Aug sync. |
| w/c 2026-08-24 | James | Seeded `research/` with three real primary sources (Datagrid's own fast-track application, RNZ, 1News) and rewrote `corpus.csv` around them. Removed the `example-0001` template row from the register. | The template row was a live row: `load_corpus.py` upserts every row as a `:Source`, so the scaffold as shipped would have injected an "Example Publisher" source into the graph. Also: the applicant's own filing says "over 240MW of IT load" while coverage reports 280MW, and the capex is redacted under OIA, so no dollar figure traces to the application. | — |
