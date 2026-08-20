# energy/harness/ — the fixed inference workload

**Step 3 (Part A) · Lead: Karl (with James)**

The workload `energy/measure.py` runs must be **fixed and reproducible** so watt-hour
numbers are comparable across models and hardware. This folder holds that definition: the
prompt set, the token targets, and the model/serving settings (context length, batch size,
quantisation) used for a run.

Keep it self-hosted only — the whole measurement is meaningless against a hosted API,
which has no knowable power draw or grid.

**Done** when a fixed prompt set + serving config lives here and `measure.py` consumes it,
so any two runs of the same harness are directly comparable.
