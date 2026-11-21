---
license: odbl
language:
- en
tags:
- automotive
- obd2
- diagnostics
- car-repair
- dtc-codes
- tabular
pretty_name: MechanicDB — OBD-II Diagnostic & Repair Sample
size_categories:
- n<1K
configs:
- config_name: dtc_codes
  data_files: dtc_codes.parquet
- config_name: diagnostic_fixes
  data_files: diagnostic_fixes.parquet
- config_name: replacement_parts
  data_files: replacement_parts.parquet
- config_name: dtc_fixes_joined
  data_files: dtc_fixes_joined.parquet
---

# 🔧 MechanicDB — OBD-II Diagnostic & Repair Database (Free Sample)

> **Full dataset:** [mechanicdb.dataengineered.io](https://mechanicdb.dataengineered.io/) · **$49 Standard (SAE) · $149 OEM Complete**, one-time → [Buy Standard](https://buy.stripe.com/5kQ3cw7Be9b88rNfuU38403) · [Buy OEM Complete](https://buy.stripe.com/28EfZicVy0ECdM796w38404) · the same sample on [Kaggle](https://www.kaggle.com/datasets/dataengineered/mechanicdb-automotive-obd2-repair-database)

The **free developer sample** of MechanicDB: an automotive dataset mapping OBD-II
Diagnostic Trouble Codes (DTCs) to **authored repair procedures in consideration order** with DIY
difficulty ratings, parts-cost ranges (USD), labor-hour estimates where known,
and step-by-step instructions.

**90 curated codes** (75 SAE-universal + 15 manufacturer-specific across makes
like Ford, Toyota, BMW, Audi) with the same tables and columns as the full commercial
dataset (the Parquet files here also carry a pandas index column, `__index_level_0__`) —
the most-searched codes (P0420, P0171, P0300, …) so you can prototype
joins, pipelines, and apps before licensing.

## Tables

| Config | Rows | Description |
| :--- | ---: | :--- |
| `dtc_codes` | 90 | Code registry: DTC, system category, OEM flag/make, fault family, short description, detailed technical explanation |
| `diagnostic_fixes` | 326 | Repair procedures in authored consideration order, with difficulty, parts-cost range and labor hours where estimated, action type, cost and labor status, cost basis, rationale, and step-by-step instructions |
| `replacement_parts` | 449 | Part mappings per fix with catalog search URLs; a row can also name a tool, a scan or programming session, or a rental |
| `dtc_fixes_joined` | 326 | Pre-joined analytical view (codes × fixes) for one-file ingestion |

Row identity: SAE rows are unique by `dtc_code`; OEM rows by `(oem_make, dtc_code)` —
the same manufacturer-range number legitimately means different things on
different brands.

Companion files: [`ordering_metadata.json`](ordering_metadata.json) (procedure order),
[`cost_metadata.json`](cost_metadata.json) (cost basis behind each `cost_basis_id`, and the
`parts_cost_status` / `labor_status` vocabularies), and `identity_metadata.json` with the filtered
`identity_map.csv` / `identity_map.parquet` and `identity_events.csv` (stable references; see
[IDENTITY.md](https://github.com/MechanicDB/MechanicDB-public/blob/main/IDENTITY.md)).

## Procedure ordering

The supported legacy-named `probability_rank` is the authored order for considering
diagnostic inspection or repair procedures within a code. Execution depends on each
procedure's prerequisites and findings. It does **not** represent measured cause
likelihood, repair success, severity, urgency, or minimum cost. The accompanying
[`ordering_metadata.json`](ordering_metadata.json) records the OBD-II ranking basis as
`authored_family_order`.

## Quickstart

```python
from datasets import load_dataset

joined = load_dataset("Ichlibitiche/mechanicdb-obd2-repair-sample", "dtc_fixes_joined", split="train")
p0420 = joined.filter(lambda r: r["dtc_code"] == "P0420")
for fix in sorted(p0420, key=lambda r: r["probability_rank"]):
    print(fix["probability_rank"], fix["fix_title"], fix["difficulty_level"])
```

## The full dataset

| | Full dataset | This sample |
| :--- | ---: | ---: |
| DTC codes | **15,886** (9,249 SAE + 6,637 OEM / 32 makes) | 90 |
| Repair procedures | **56,729** | 326 |
| Parts mappings | **75,055** | 449 |
| Fault families | **647** | (linked) |

Self-serve commercial licensing with instant download:
**[mechanicdb.dataengineered.io](https://mechanicdb.dataengineered.io/)** ·
also on [GitHub](https://github.com/MechanicDB/MechanicDB-public) and
[Kaggle](https://www.kaggle.com/datasets/dataengineered/mechanicdb-automotive-obd2-repair-database).

## Provenance & license

- Code-to-definition mappings compiled from an MIT-licensed SAE J2012-derived
  public compilation (attribution preserved in the source repos); repair
  procedures, difficulty ratings, and cost ranges are original editorial content
  from a deterministic, test-gated pipeline. Cost and labor values are editorial
  (parts in US dollars assuming aftermarket parts, labor in hours), not quotes;
  unknown values are empty.
- **License:** ODbL v1.0 (attribution + share-alike).

⚠️ Repair steps are educational reference material, not a substitute for the
vehicle manufacturer's service manual. High-voltage (hybrid/EV) and SRS/airbag
work calls for the manufacturer's safety procedure whatever the difficulty rating;
if you cannot follow it, leave the work to a qualified technician.
