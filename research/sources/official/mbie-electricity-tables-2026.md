---
id: mbie-electricity-tables-2026
title: "Electricity data tables (New Zealand Energy Quarterly, March 2026 quarter)"
publisher: "Ministry of Business, Innovation and Employment"
date: 2026-06-01
url: "https://www.mbie.govt.nz/building-and-energy/energy-and-natural-resources/energy-statistics-and-modelling/energy-statistics/electricity-statistics"
retrieved: 2026-09-04
type: dataset
camp: official
---

**Evidence role:** primary — MBIE's own statistical series, the numbers themselves rather than a publication describing them.

⚠ **Verification status:** figures below were read programmatically from the workbook with
pandas. The cell references are given so they can be re-checked, but a human has not opened
the spreadsheet and confirmed them.

**On the `date` field:** the workbook carries no release date. Its latest data point is the
**March 2026 quarter**, and tables 1–4 are "updated every quarter along with the latest New
Zealand Energy Quarterly publication", so 2026-06-01 is an *inferred* release date, not a
stated one. Treat it as approximate.

**On retrieval:** MBIE's HTML sits behind Imperva bot protection and refuses automated
requests, so the `url` above cannot be fetched by a script — it must be opened in a browser.
The file was downloaded by hand on 2026-09-04 and kept at
`data/raw/electricity-quarterly-webtable.xlsx`, which is gitignored. Provenance is registered
in `data/README.md`. Licence terms are **unconfirmed** — the workbook states none.

## Summary

The first `type: dataset` source in the corpus, and the authoritative version of figures that
until now came from PDFs describing them. Sheet "2 - Annual GWh" carries net generation,
generation by fuel, renewable share and consumption by sector for every calendar year from
1974 to 2025. It settles the application's 82% figure exactly, resolves a rounding discrepancy
between two MBIE publications, and shows that a published figure this corpus already cites has
since been revised.

## The series that matters

Sheet **"2 - Annual GWh"**, row 8 = calendar year, row 10 = Net Generation (GWh),
row 21 = Renewable Share (%), rows 41–54 = consumption by sector (estimated sales basis;
row 43 "Industrial:" is a subtotal and must not be added to its own components).

| Calendar year | Net generation (GWh) | Renewable share | Consumption (GWh) |
| --- | --- | --- | --- |
| 2021 | 43,361.8 | **82.15%** | — |
| 2022 | 43,637.0 | 87.14% | 39,951.2 |
| 2023 | 43,592.0 | **88.13%** | 40,004.1 |
| 2024 | 43,976.7 | 85.50% | 40,093.4 |
| 2025 | 44,140.5 | **88.46%** | 40,589.8 |

Earlier years, for the fast-track application's context: 2020 was 81.21%, 2019 82.77%,
2018 84.33%.

## What it settles

**The application's "82% renewable" is the 2021 calendar year, 82.15%.** Confirmed to two
decimal places from MBIE's own series rather than inferred from a publication's prose.

**The 2023 renewable share is 88.1%, not 88.0%.** `mbie-energy-in-nz-2024` gives 88.0 in its
summary and 88.1 in its body. The table gives 88.13, so the body is right and the summary
rounds down.

**A figure already cited in this corpus has been revised.** `mbie-energy-in-nz-2024` states
2023 national consumption as 39,130 GWh. The current table puts 2023 consumption at
40,004 GWh on the estimated-sales basis and 40,067.6 GWh on the actual-sales basis — roughly
870–940 GWh higher. The workbook's "Revisions" sheet records, against ENZ 2023, "Improvements
to consumption estimate methodology and revisions to data" for residential and transport,
March 2017 – December 2022. Total generation for 2023 has also moved, from 43,488 GWh in the
publication to 43,592 GWh here.

**Makarewa's share of national electricity is about 6%, and stable.** 280 MW at full load is
2,453 GWh a year. Against consumption that is 6.14% (2022), 6.13% (2023), 6.12% (2024),
6.04% (2025); against net generation it is about 5.6%.

## Claims this supports

- `claim-nz-renewable-share` — annual series 1974–2025; 82.15% (2021), 88.13% (2023), 85.50% (2024), 88.46% (2025)
- `claim-nz-total-electricity` — net generation and consumption by calendar year, 1974–2025
- `claim-makarewa-power-draw` — the denominator: 280 MW at full load is ~6% of national consumption
