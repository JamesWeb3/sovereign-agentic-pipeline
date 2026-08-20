# energy/ — watt-hours per 1000 tokens

**Plan Step:** Step 3 (Part A — evidence)
**Lead:** Karl (with James)
**Serves:** the headline number of the whole project — what a token of inference actually
costs in energy — and, with `grid/`, on what electricity.

## What this is

A measurement harness that samples GPU/CPU power draw (`nvidia-smi` for GPU, RAPL for CPU)
around a **fixed inference workload** on a self-hosted open-weight model, and reports
watt-hours per 1000 tokens. The workload is fixed so runs are comparable across hardware.

## Files

- `measure.py` — runs a fixed workload, samples power at an interval, and writes a results
  CSV with a hardware fingerprint.
- `harness/` — the fixed workload definition (prompts, token targets, model settings) so a
  run is reproducible.
- `results/` — one committed CSV per run, each carrying the hardware fingerprint. These are
  small and redistributable, so they live in git (unlike raw data).

## The rule that governs this directory

**Negative results count.** If self-hosted inference turns out to be more energy-hungry
than the thesis predicts, that number gets committed and published exactly the same as a
favourable one (docs/methodology.md).

## Definition of done (Step 3)

- A reproducible harness producing watt-hours per 1000 tokens for at least one open-weight
  model on at least one real GPU, with the hardware fingerprint recorded.
- Results committed as CSVs in `results/`, each traceable to the harness config that
  produced it.
