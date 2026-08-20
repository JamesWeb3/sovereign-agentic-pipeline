---
name: Plan Step
about: One issue mapping to a Step in the 18-week build plan
title: "Step N: <short description>"
labels: ["step"]
assignees: []
---

<!--
One issue = one Step from the build plan (see docs/ and the directory READMEs).
Keep it honest: negative results and dead ends are findings, so record them here too.
-->

**Step:** <!-- e.g. Step 2 — EMI half-hourly NZ generation data -->
**Part:** <!-- A (evidence, weeks 1-9) or B (pipeline, weeks 10-18) -->
**Owner / lead:** <!-- Karl or James -->
**Directory:** <!-- e.g. grid/ -->

## Deliverable — what "done" looks like

<!-- The concrete artefact this Step must produce, copied from the directory's README
     "done" line. Be specific: a committed CSV, a passing loader, a chart, a number. -->

## Definition of done

- [ ] Deliverable committed to the repo
- [ ] Every number traces to a primary source or a calculation (methodology.md)
- [ ] Provenance recorded (sources frontmatter / data/README.md) where data is involved
- [ ] `make lint` and `make test` pass
- [ ] Weekly log updated (docs/weekly-log.md)

## Notes / links

<!-- Primary sources, related issues, blockers. -->
