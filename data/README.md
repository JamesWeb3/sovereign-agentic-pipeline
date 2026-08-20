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

Add a row per dataset as it enters the project. Keep the raw files out of git; commit only
derived, confirmed-redistributable tables.
