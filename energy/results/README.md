# energy/results/ — measured runs

**Step 3 (Part A) · Lead: Karl (with James)**

One CSV per run, written by `energy/measure.py`. Each row carries a hardware fingerprint,
the average power draw, the energy used, and the derived watt-hours per 1000 tokens. These
are committed to git (they are small and redistributable — unlike raw grid data).

Do not hand-edit these files; regenerate them by re-running the harness so the number
always traces to a run. A favourable and an unfavourable result are committed the same way.

**Done** when at least one real run's CSV is committed here, reproducible from the harness.
