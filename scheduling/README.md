# scheduling/ — can compute follow renewable generation?

**Plan Step:** Step 4 (Part A — evidence)
**Lead:** Karl (with James)
**Serves:** the second half of the energy thesis — not just *how much* energy inference
uses, but whether it can be shifted to *when* the grid is cleanest without breaking SLAs.

## What this is

A simulation that takes the EMI half-hourly generation mix (`grid/`) and the measured
energy per workload (`energy/`), and asks: if we defer flexible compute to trading periods
with a high renewable share, how much cleaner does the average token get, and what does it
cost in latency/SLA terms?

## Files

- `simulate.py` — reads a grid renewable-share series and a workload profile, applies a
  scheduling policy (e.g. "run when renewable share > X%"), and reports the clean-energy
  gain versus the SLA cost.
- `results/` — committed CSVs, one per simulation run, with the policy parameters recorded.

## The honest-conclusion clause

This is where the thesis is most falsifiable. If scheduling buys little because NZ's grid
is already highly renewable around the clock — or because the flexible fraction of
inference is small — that is a genuine finding and it gets published (docs/methodology.md).

## Definition of done (Step 4)

- A simulation that, given real EMI data and a workload, quantifies the clean-energy gain
  and SLA cost of renewable-following scheduling, across a range of policies.
- Results committed as CSVs in `results/`, each traceable to its policy parameters.
