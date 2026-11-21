# Corpus manifest

Provenance, license, and counts for every vendored dataset. **US/Canada only.** One owner: this file. All data files are stored as-is from their source repositories (parquet converts to `.json` + `.md`, noted per row); every directory carries the source's own card as `README.md`. Vendored on 2026-11-21.

---

## Vendored — 54 datasets

Grouped by area. The 13 original datasets are listed first; the 41 added in the 2026-11-21 expansion follow.

| Directory | Hugging Face id | License | Rows | What it is / notes |
|---|---|---|---|---|
| `referencesource__oem-vehicle-maintenance-schedule-by-model/` | `referencesource/oem-vehicle-maintenance-schedule-by-model` | other (source-terms-cited) | 6,111 | US Toyota OEM maintenance schedules by make/model/year/interval, each quoted from the manufacturer's PDF. License position: facts + short attributed quotes; no page reproduced. Canonical source: referencesource.org |
| `Ichlibitiche__mechanicdb-obd2-repair-sample/` | `Ichlibitiche/mechanicdb-obd2-repair-sample` | ODbL | 865 | US-standard OBD-II DTCs (90 codes), authored repair procedures in consideration order (326), replacement parts (449), identity rows (865). Converted from parquet to `.json` + `.md` |
| `CodesList__obd2-codes/` | `CodesList/obd2-codes` | CC-BY-4.0 | 9,414 | US-standard OBD-II trouble codes with category and severity |
| `karsonmadden__us-vehicle-trouble-codes/` | `karsonmadden/us-vehicle-trouble-codes` | CC-BY-4.0 | 1,142 | US vehicle trouble codes with meaning, bulletins, owner-report counts |
| `aowens25__NHTSA/` | `aowens25/NHTSA` | Apache-2.0 | 216,141 | US NHTSA vehicle recalls (make, model, year, summary). Large file (67 MB) |
| `vic35get__nhtsa_complaints_dataset/` | `vic35get/nhtsa_complaints_dataset` | Apache-2.0 | 12,534 | US NHTSA owner complaints (components, summary text). Converted from parquet to `.json` + `.md` |
| `iqbaltaher__us-vehicle-owner-complaints-by-model-2010-2025/` | `iqbaltaher/us-vehicle-owner-complaints-by-model-2010-2025` | CC-BY-4.0 | 90,254 | US owner complaints aggregated by make/model/year/component |
| `ItsMayur__Vehicle_Complaints_NHSTA/` | `ItsMayur/Vehicle_Complaints_NHSTA` | MIT | 1,064 | US NHTSA complaint narratives |
| `sorbh-kd__us-auto-body-shops/` | `sorbh-kd/us-auto-body-shops` | CC-BY-4.0 | 81,141 | US auto body shop directory (services, location, hours) |
| `yandyman__us-consumer-recalls/` | `yandyman/us-consumer-recalls` | CC0-1.0 | 3,721 | US CPSC consumer recalls (autos and household products) |
| `dipenbhuva__home-diy-repair-qa/` | `dipenbhuva/home-diy-repair-qa` | Apache-2.0 | 5,000 | Synthetic English home-repair Q&A (inside/outside the house). 4,000 train + 1,000 eval |
| `ShingleGeek__roofing-cost-index/` | `ShingleGeek/roofing-cost-index` | CC-BY-4.0 | 655 | US residential roofing cost index (505 cities). Contains prices — reference only; the kit never quotes prices |
| `NextTerritory__us-exterior-home-improvement-market-size/` | `NextTerritory/us-exterior-home-improvement-market-size` | CC-BY-4.0 | 4,935 | US exterior home improvement market size (roofing, siding, gutters, windows, exterior walls by metro/state) |

### Expansion — 41 datasets added 2026-11-21

#### Auto repair — diagnostics, complaints, recalls, shops, liens

| Directory | Hugging Face id | License | Rows | What it is / notes |
|---|---|---|---|---|
| `claritystorm__nhtsa-vehicle-complaints/` | `claritystorm/nhtsa-vehicle-complaints` | other (public-domain) | 1,000 | US NHTSA vehicle complaints 1995–2026, 1,000-row public sample |
| `claritystorm__nhtsa-vehicle-recalls/` | `claritystorm/nhtsa-vehicle-recalls` | other (public-domain) | 1,000 | US NHTSA vehicle recalls 1966–2026, 1,000-row public sample |
| `CyberMax-tools__recallroll-vehicle-recalls/` | `CyberMax-tools/recallroll-vehicle-recalls` | other (us-government-work) | 6,712 | US vehicle safety recalls, last 12 months (NHTSA) |
| `earino__factory-nhtsa-pe-recall/` | `earino/factory-nhtsa-pe-recall` | other | 1,253 | NHTSA PE recall factory dataset |
| `referencesource__mechanics-lien-deadlines-by-state/` | `referencesource/mechanics-lien-deadlines-by-state` | other (source-terms-cited) | 51 | US mechanic lien deadlines by state |
| `referencesource__auto-insurance-minimums/` | `referencesource/auto-insurance-minimums` | other (source-terms-cited) | 51 | US auto insurance minimums by state |
| `referencesource__abandoned-vehicle-private-property-timelines-by-state/` | `referencesource/abandoned-vehicle-private-property-timelines-by-state` | other (source-terms-cited) | 44 | US abandoned-vehicle timelines by state |
| `referencesource__catalytic-converter-theft-laws-by-state/` | `referencesource/catalytic-converter-theft-laws-by-state` | other (source-terms-cited) | 7 | US catalytic converter theft laws by state |
| `referencesource__discontinued-part-replacement-mapping/` | `referencesource/discontinued-part-replacement-mapping` | other (source-terms-cited) | 28 | Discontinued part replacement mapping |

#### Home repair — inside the house

| Directory | Hugging Face id | License | Rows | What it is / notes |
|---|---|---|---|---|
| `Ichlibitiche__appliancedb-error-codes-repair-database/` | `Ichlibitiche/appliancedb-error-codes-repair-database` | ODbL | 1,281 | Appliance error codes and repair procedures |
| `chimneyrepairguide__thesepticguide-septic-licensing-statistics/` | `chimneyrepairguide/thesepticguide-septic-licensing-statistics` | CC-BY-4.0 | 2,345 | US septic contractor licensing statistics by state |
| `chimneyrepairguide__watersystemguide-hard-water-statistics/` | `chimneyrepairguide/watersystemguide-hard-water-statistics` | CC-BY-4.0 | 480 | US hard-water statistics |
| `referencesource__hvac-component-refrigerant-compatibility/` | `referencesource/hvac-component-refrigerant-compatibility` | other (source-terms-cited) | 109 | HVAC component refrigerant compatibility |
| `referencesource__appliance-fault-error-codes/` | `referencesource/appliance-fault-error-codes` | other (source-terms-cited) | 136 | Appliance fault/error codes |
| `referencesource__boiler-inspection-requirements-by-state/` | `referencesource/boiler-inspection-requirements-by-state` | other (source-terms-cited) | 55 | US boiler inspection requirements by state |
| `referencesource__well-water-testing-at-property-transfer/` | `referencesource/well-water-testing-at-property-transfer` | other (source-terms-cited) | 13 | US well-water testing requirements at property sale |

#### Home repair — outside the house

| Directory | Hugging Face id | License | Rows | What it is / notes |
|---|---|---|---|---|
| `thanna94__us-building-permits/` | `thanna94/us-building-permits` | CC0-1.0 | 780,525 | US residential building permits 1980–2026, place-level |
| `chimneyrepairguide__backupgeneratorguide-power-outages-by-state/` | `chimneyrepairguide/backupgeneratorguide-power-outages-by-state` | CC-BY-4.0 | 18,598 | US power outage burden by state (EIA/DOE) |
| `chimneyrepairguide__thefoundationrepairguide-foundation-repair-cost/` | `chimneyrepairguide/thefoundationrepairguide-foundation-repair-cost` | CC-BY-4.0 | 80 | US foundation repair cost register |
| `chimneyrepairguide__landclearingguide-land-clearing-cost/` | `chimneyrepairguide/landclearingguide-land-clearing-cost` | CC-BY-4.0 | 58 | US land clearing cost register |
| `chimneyrepairguide__retainingwallguide-retaining-wall-cost/` | `chimneyrepairguide/retainingwallguide-retaining-wall-cost` | CC-BY-4.0 | 53 | US retaining wall cost register |
| `chimneyrepairguide__sprayfoamguide-spray-foam-insulation-cost/` | `chimneyrepairguide/sprayfoamguide-spray-foam-insulation-cost` | CC-BY-4.0 | 44 | US spray foam insulation cost register |
| `chimneyrepairguide__bulkheadguide-bulkhead-seawall-cost/` | `chimneyrepairguide/bulkheadguide-bulkhead-seawall-cost` | CC-BY-4.0 | 50 | US bulkhead/seawall cost register |
| `referencesource__building-permit-validity-and-renewal/` | `referencesource/building-permit-validity-and-renewal` | other (source-terms-cited) | 7 | US building permit validity and renewal by jurisdiction |
| `referencesource__iecc-climate-zone-by-county/` | `referencesource/iecc-climate-zone-by-county` | other (source-terms-cited) | 3,134 | US IECC climate zones by county |
| `referencesource__construction-prompt-payment-deadlines-by-state/` | `referencesource/construction-prompt-payment-deadlines-by-state` | other (source-terms-cited) | 43 | US construction prompt-payment deadlines by state |
| `referencesource__construction-retainage-limits-by-state/` | `referencesource/construction-retainage-limits-by-state` | other (source-terms-cited) | 30 | US construction retainage limits by state |
| `referencesource__energy-code-adoption-by-state/` | `referencesource/energy-code-adoption-by-state` | other (source-terms-cited) | 9 | US energy code adoption by state |
| `referencesource__insurance-claim-handling-deadlines/` | `referencesource/insurance-claim-handling-deadlines` | other (source-terms-cited) | 42 | US insurance claim handling deadlines |
| `referencesource__home-energy-rebate-program-status-by-state/` | `referencesource/home-energy-rebate-program-status-by-state` | other (source-terms-cited) | 47 | US home energy rebate program status by state |

#### Home repair — contractor & licensing

| Directory | Hugging Face id | License | Rows | What it is / notes |
|---|---|---|---|---|
| `Pisces89__ohio-home-services-pros/` | `Pisces89/ohio-home-services-pros` | CC-BY-4.0 | 21,898 | Ohio home-services contractor directory (plumbers, electricians, HVAC, roofers, appliance repair, restoration, septic, etc.) |
| `nearbia__florida-contractor-license-types/` | `nearbia/florida-contractor-license-types` | CC-BY-4.0 | 27 | Florida contractor license types |
| `joeygambino__california-licensed-contractors/` | `joeygambino/california-licensed-contractors` | MIT | 101 | California licensed contractors registry sample |
| `joeygambino__phoenix-hvac-contractor-leads/` | `joeygambino/phoenix-hvac-contractor-leads` | MIT | 21 | Phoenix HVAC contractor leads |
| `referencesource__general-contractor-license-thresholds-by-state/` | `referencesource/general-contractor-license-thresholds-by-state` | other (source-terms-cited) | 11 | US general contractor license thresholds by state |
| `referencesource__electrician-licence-progression-by-state/` | `referencesource/electrician-licence-progression-by-state` | other (source-terms-cited) | 2 | US electrician licence progression by state |
| `referencesource__electrician-licence-reciprocity-by-state/` | `referencesource/electrician-licence-reciprocity-by-state` | other (source-terms-cited) | 16 | US electrician licence reciprocity by state |

#### Home repair — cost registers

| Directory | Hugging Face id | License | Rows | What it is / notes |
|---|---|---|---|---|
| `chimneyrepairguide__chimney-repair-cost-register/` | `chimneyrepairguide/chimney-repair-cost-register` | CC-BY-4.0 | 128 | US chimney repair cost register |
| `chimneyrepairguide__chimneyrepairguide-chimney-repair-cost/` | `chimneyrepairguide/chimneyrepairguide-chimney-repair-cost` | CC-BY-4.0 | 128 | US chimney repair cost register (second mirror) |
| `chimneyrepairguide__well-drilling-cost-register-us-2026/` | `chimneyrepairguide/well-drilling-cost-register-us-2026` | CC-BY-4.0 | 181 | US well drilling cost register |
| `chimneyrepairguide__thewelldrillingguide-well-drilling-cost/` | `chimneyrepairguide/thewelldrillingguide-well-drilling-cost` | CC-BY-4.0 | 181 | US well drilling cost register (second mirror) |

## Removed — non-US/Canada (2026-11-21)

| Removed | Reason |
|---|---|
| `svr99991__india-synthetic-property-maintenance-tickets/` | India — different fee structures and document formats; pollutes US/Canada calibration |
| `karthe05__maintenance-work-order-triage-data/` | Australia (MaintNorm/MaintIE, University of Western Australia) — mining heavy equipment, non-US/Canada |

## Considered and rejected (never vendored)

| Candidate | Why it did not come in |
|---|---|
| `PedroCuisinier2025/OBD2_panel_opel_2012` | Time-series telemetry (100k+ rows), not repair-document text |
| `hackermango/HyderabadUniversity_HVAC_Dataset` | India — non-US/Canada |
| `cs-uche/car_dealership` | Used-car sales listings (non-US market), not repair |
| `wushuang/vehicle_qa` | Chinese-language, non-US/Canada |
| `shubhamk1729/car-dealership-crm` | 130 MB+ CRM parquet (accounts, leads, tasks), not repair-document text |
| `HitmanH/Toronto_Collision_silver` | Traffic collision incident statistics, not repair estimates |
| `nus-yin/ex-repair` | Software code repair, not auto/home |
| `zookeeper/hvac-western-ny` | Gated (401) |
| `MechanicDB/MechanicDB-public` | Gated (401) |

## Totals

| Measure | Value |
|---|---|
| **Indexed (whole HF surface)** | 930 datasets — [`INDEX.md`](INDEX.md) / [`index.json`](index.json) |
| Vendored datasets | 54 |
| Vendored records | 1,272,956 — the sum of the `Rows` column above, counted 2026-11-21 |
| Vendored on-disk size | ~205 MB — `du -sh corpus`, 2026-11-21 |
| File types vendored | text only: `.csv`, `.json`, `.jsonl`, `.md` (+ converted parquet) |
| Vendored license range | Apache-2.0, MIT, CC-BY-4.0, CC0-1.0, ODbL, source-terms-cited — all redistributable with attribution |

## Surface reality (per category)

The HF surface for **US/Canada repair documents** is thin on actual repair *estimates* and *invoices*. The richest material is complaints (NHTSA), recalls (NHTSA/CPSC), trouble codes (OBD-II), maintenance schedules (OEM), directories (body shops, home-services contractors), licensing and permit data, and cost indices. The 2026-11-21 expansion added 41 datasets: US building permits, contractor directories and licensing, home-repair cost registers, appliance/HVAC/plumbing references, and more NHTSA complaint/recall samples. Even so, the surface still has **no US/Canada dataset of real repair estimates or invoices at scale** — the 41 additions deepen the symptom, cost, and licensing side, not the document side. That gap is why the kit's own fixtures are synthetic — and why the corpus is a calibration reference, not a training set.
