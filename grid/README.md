# grid/ — NZ half-hourly generation data (EMI)

**Plan Step:** Step 2 (Part A — evidence)
**Lead:** Karl (with James)
**Serves:** the renewable-scheduling simulation (Step 4) and the "what grid did the
compute run on" claim at the heart of the sovereignty/energy thesis.

## What this is

Ingestion of New Zealand's electricity generation data from **EMI (Electricity Market
Information)**, the Electricity Authority's public data portal. This gives us, per trading
period, how much was generated and by what fuel — the denominator for every "clean" claim
the project makes.

## Dataset provenance & licence

*Verified by fetching the EMI generation dataset page on 2026-08-20.*

- **Source:** Electricity Authority — Electricity Market Information (EMI),
  <https://www.emi.ea.govt.nz/>. Generation dataset:
  <https://www.emi.ea.govt.nz/Wholesale/Datasets/Generation/Generation_MD>.
- **Granularity:** by **trading period** — 48 per day (TP1–TP48), i.e. half-hourly.
- **Measure:** generation in kilowatt-hours (kWh), estimated by mapping metered grid
  injections to the generating plant at each injection point.
- **Coverage:** monthly CSV files, 1997 to present.
- **Licence:** the EMI site carries "© Copyright material on this site is protected by
  copyright owned by the Electricity Authority or its licensors." The page does not link an
  explicit open-data licence. **Before committing any derived EMI artefact, confirm the
  reuse terms** (info@ea.govt.nz / the site's copyright & disclaimer page) and record the
  outcome in `data/README.md`. Raw downloads stay in `data/raw/` (gitignored) regardless.

## Files

- `ingest_emi.py` — downloads a monthly generation CSV to `data/raw/` and writes a tidy,
  derived table. Takes the month and (optionally) the file URL as arguments; the exact
  file-URL pattern should be confirmed against the EMI portal (see the script's docstring).

## Definition of done (Step 2)

- A reproducible ingest that pulls EMI half-hourly generation into `data/raw/` and
  produces a tidy per-trading-period table (timestamp, fuel/plant, kWh).
- Provenance and confirmed licence recorded in `data/README.md`.
- Enough history loaded to feed the Step 4 scheduling simulation.
