# Methodology — the non-negotiables

This project's credibility rests entirely on how the evidence is handled. These rules are
not style preferences; they are the standard the published report will be judged against.
Read them before you add a number, a source, or a conclusion.

## The rules

- **Every number gets a source or a calculation.** A figure you can't trace — back to a
  primary source with a URL and a retrieval date, or to a calculation that lives in this
  repo — is a figure we delete.

- **Negative results count.** If the electricity thesis doesn't hold, or the pipeline
  loses to a hosted API, that is a finding and we publish it. We are not here to defend a
  conclusion; we are here to find out.

- **Everything goes in the repo** — code, data, notebooks, half-finished analysis. Commit
  little and often. The history is the audit trail.

- **Primary sources only** for the Southland landscape: coverage, submissions, official
  statements. Not summaries of summaries. If a claim rests on someone else's paraphrase,
  chase it to the original before it earns a place in the corpus.

## ⚠ The protected held-out eval

**`model/eval/` is protected.** The 100-question held-out set is never used for training
and never tuned against. If Step 5 slips, cut the dataset size — never the eval set. A
small dataset with a rigorous eval is a result; a big one with a rushed eval measures
nothing. This warning is repeated in `model/eval/README.md`; treat any change under that
directory as requiring explicit sign-off.

## How this shows up in practice

- **Sources** live one-per-file in `research/sources/`, each with frontmatter
  (`id, title, publisher, date, url, retrieved, type, camp`). The register is
  `research/corpus.csv`.
- **Claims and numbers** become nodes in the knowledge graph (`graph/schema.cypher`),
  each linked back to the Source it came from — so an untraceable number is structurally
  impossible to represent.
- **Datasets** (EMI grid data, any scraped coverage) have their provenance recorded in
  `data/README.md`: source, licence, retrieval date, and what transformed them. The raw
  bytes stay out of git (`data/raw/` is gitignored); only derived, redistributable
  artefacts are committed.
- **Measurements** (energy per 1000 tokens, scheduling simulations) commit their raw
  output CSVs with a hardware fingerprint, so a reader can see the run, not just the
  headline.
