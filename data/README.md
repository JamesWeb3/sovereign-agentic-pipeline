# data/ — datasets and their provenance

The raw bytes of any dataset live in `data/raw/`, which is **gitignored**. This file is the
provenance register: for every dataset we use, record where it came from, under what
licence, when it was retrieved, and what transformed it. A dataset with no entry here does
not belong in the project.

This matters doubly because the repo is public: nothing under a licence that forbids
redistribution may be committed. When in doubt, keep the raw file in `data/raw/` and link
to the source here instead of copying it in.

## Provenance register

| Dataset | Source | Licence | Retrieved | Transformed by | Notes |
|---|---|---|---|---|---|
| EMI half-hourly generation | Electricity Authority — EMI, <https://www.emi.ea.govt.nz/Wholesale/Datasets/Generation/Generation_MD> | © Electricity Authority; explicit reuse terms **to be confirmed** (info@ea.govt.nz) before committing any derived artefact | 2026-08-20 (dataset page verified) | `grid/ingest_emi.py` | By trading period (48/day, half-hourly), kWh. Raw CSVs stay in `data/raw/`. |

| MBIE electricity data tables | MBIE — Electricity statistics, <https://www.mbie.govt.nz/building-and-energy/energy-and-natural-resources/energy-statistics-and-modelling/energy-statistics/electricity-statistics> | Not stated in the workbook; reuse terms **to be confirmed** (energyinfo@mbie.govt.nz) before committing any derived table | 2026-09-04 (downloaded by hand) | read with pandas; see `research/sources/official/mbie-electricity-tables-2026` | `electricity-quarterly-webtable.xlsx`. Annual and quarterly generation, fuel mix, renewable share and consumption by sector, 1974–2025 (latest quarter March 2026). MBIE's site is behind Imperva and refuses automated fetches — a browser is required. |
| MBIE renewables data tables | MBIE — Renewables statistics, <https://www.mbie.govt.nz/building-and-energy/energy-and-natural-resources/energy-statistics-and-modelling/energy-statistics/renewables-statistics> | Not stated in the workbook; reuse terms **to be confirmed** (energyinfo@mbie.govt.nz) | 2026-09-04 (downloaded by hand) | not yet used | `renewables.xlsx`. Renewable energy supply, transformation and demand (PJ) — whole-of-energy, broader than electricity. Held for later; nothing in the corpus cites it yet. |
Add a row per dataset as it enters the project. Keep the raw files out of git; commit only
derived, confirmed-redistributable tables.
