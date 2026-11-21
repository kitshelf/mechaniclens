---
license: odbl
pretty_name: 'ApplianceDB: Home Appliance Error Codes & Ranked Repairs'
language:
- en
tags:
- appliance-repair
- error-codes
- home-appliances
- manufacturing
- engineering
size_categories:
- n<1K
configs:
- config_name: error_codes
  data_files: error_codes.csv
- config_name: repair_procedures
  data_files: repair_procedures.csv
- config_name: error_codes_fixes_joined
  data_files: error_codes_fixes_joined.csv
- config_name: replacement_parts
  data_files: replacement_parts.csv
- config_name: brand_recalls
  data_files: brand_recalls.csv
---

![ApplianceDB](cover.png)

# ApplianceDB: Home Appliance Error Codes & Ranked Repairs

> **Paid tier:** [appliancedb.dataengineered.io](https://appliancedb.dataengineered.io/) · **$99 one-time** (Repair Intelligence Snapshot: commercial licence + a SQLite build; the same rows, CSV and Parquet files as this sample) → [Buy on Stripe](https://buy.stripe.com/bJedRa7BegDA23p6Yo3840i) · the same sample on [Kaggle](https://www.kaggle.com/datasets/dataengineered/appliancedb-error-codes-repair-database)

Relational database of 438 home-appliance error codes across 13 brands and 26 (brand, market, appliance-type) groups; 247 of the codes are mapped to 288 ranked repair procedures with DIY difficulty tiers. Every code is identified by its composite (brand, market, appliance_type, code) key — Samsung washer 5C is a distinct record from Samsung dishwasher 5C.


## Files / configs

Each table is a separate config for the Datasets viewer:

- `error_codes` — 438 fault codes keyed by composite `(brand, market, appliance_type, code)`, with meaning, component, cause category, severity and source URL
- `repair_procedures` — 288 ranked repair procedures with DIY difficulty tiers
- `error_codes_fixes_joined` — denormalized join of every error code with its ranked fixes (where shipped), for quick analysis
- `replacement_parts` — OEM replacement parts linked to procedures
- `brand_recalls` — 56 home-appliance recalls (CPSC) affecting these brands, cross-referenced from the sibling RecallDB corpus, with the agency listing URL per row

## Quick start

```python
from datasets import load_dataset

codes = load_dataset("Ichlibitiche/appliancedb-error-codes-repair-database", "error_codes", split="train")
fixes = load_dataset("Ichlibitiche/appliancedb-error-codes-repair-database", "repair_procedures", split="train")
```

Or with pandas:

```python
import pandas as pd
codes = pd.read_csv("hf://datasets/Ichlibitiche/appliancedb-error-codes-repair-database/error_codes.csv")
```

## Coverage

- **13 brands:** Beko, Bosch, Candy, Frigidaire, GE, Hoover, Hotpoint, Indesit, LG, Maytag, Miele, Samsung, Whirlpool
- **5 appliance types:** dishwasher, dryer, oven/range, refrigerator, washer

## Portal & full documentation

Portal: https://appliancedb.dataengineered.io/ · Docs & data dictionary: https://github.com/ApplianceDB/ApplianceDB-public

## License

**ODbL-1.0** (Open Database License). Facts re-derived from fetched source listings — manufacturer support pages or independent appliance-repair reference sites, flagged per row in `source_type` — with per-row source URLs; meanings and repair steps paraphrased into original wording.

## Provenance & Methodology

Codes come from two kinds of fetched listing, flagged per row in source_type: 239 from official manufacturer support pages (manufacturer_listing) and 199 from independent appliance-repair reference sites (aggregator_listing: ApplianceAid, ApplianceCodeHub, Domex UK, Whitegoods Help), used where the manufacturer's own listing was unfetchable or too thin. The exact source URL is recorded per row; filter on source_type for manufacturer-only data. All meanings and repair steps are paraphrased into original wording (no verbatim source prose). Repair ranks carry an explicit basis (cost_ascending or manufacturer_first). Costs are left NULL where no verified price observation exists — never guessed. Each release is built by a deterministic, test-gated pipeline (composite-uniqueness, controlled-vocabulary, rank-contiguity, and >=10-codes-per-group coverage gates).

Full documentation and data dictionary: https://github.com/ApplianceDB/ApplianceDB-public