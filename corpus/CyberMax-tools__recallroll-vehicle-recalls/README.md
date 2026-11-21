---
# LATEST: https://huggingface.co/datasets/CyberMax-tools/recallroll-vehicle-recalls/blob/main/latest.json (data date, refresh cadence, fresh API, licence links; also LATEST.md)
# API (fresh data): https://recallroll-api.cybermaxtools.com/?utm_source=huggingface&utm_medium=free-asset&utm_campaign=file-recallroll-vehicle-recalls&utm_content=recallroll-api#pricing
# Licence: other (open, unchanged); commercial licence + support: https://buy.stripe.com/5kQ9AT4A40oVfF7dlNbV61L?utm_source=huggingface&utm_medium=free-asset&utm_campaign=file-recallroll-vehicle-recalls&utm_content=st-dataset-license-small&client_reference_id=data_hf-file-recallroll-vehicle-recalls
license: other
license_name: us-government-work
license_link: https://www.usa.gov/government-works
pretty_name: US vehicle safety recalls, last 12 months (NHTSA) | Recallroll
language:
- en
tags:
- vehicle-recalls
- nhtsa
- auto-safety
- vin
- automotive
- fleet
- public-data
- government-data
- tabular
- cybermax
task_categories:
- tabular-classification
size_categories:
- 1K<n<10K
configs:
- config_name: recalls
  default: true
  data_files:
  - split: train
    path: recalls_recent.parquet
- config_name: vehicles
  data_files:
  - split: train
    path: vehicles_recent.parquet
---

# Recallroll: US vehicle safety recalls, last 12 months

<!-- cybermax-bridge:start -->
> **Need it fresh, filtered or via API?** **Check your own VINs for open recalls, live, by API: $5 for 400 calls of up to 10 VINs.** **[Buy now →](https://data.cybermaxtools.com/buy/recallroll-api-pack?s=hf-recallroll-vehicle-recalls-top)** · API key on screen the moment checkout ends · no subscription · [14-day refund](https://cybermaxtools.com/terms#payments) if it doesn't work as described · help: cybermax.tools@gmail.com Updated daily. Filters, alerts and API: [Recallroll VIN + recall API](https://recallroll-api.cybermaxtools.com/?utm_source=huggingface&utm_medium=free-asset&utm_campaign=recallroll-vehicle-recalls&utm_content=recallroll-api#pricing).
> 
> This free file is a snapshot (NHTSA recalls of the last 12 months), last updated **2026-11-21**.
> - **[Recallroll VIN + recall API](https://recallroll-api.cybermaxtools.com/?utm_source=huggingface&utm_medium=free-asset&utm_campaign=recallroll-vehicle-recalls&utm_content=recallroll-api#pricing)** (50 free calls a day, $5 for 400 calls (no expiry), or $19/month for 2,000): decodes up to 10 VINs per call and lists every NHTSA recall for each vehicle, Do Not Drive first, by API or MCP.
> - **[US Vehicle Recall Brief: Weekly Edition](https://buy.polar.sh/polar_cl_NK5PtAstfiHC8hKL3itnliyWYppYvB4vKFuiR36KglE?utm_source=huggingface&utm_medium=free-asset&utm_campaign=recallroll-vehicle-recalls&utm_content=recall-brief)** ($9/month): a fresh NHTSA recall brief every Monday (PDF + 5 CSVs): every new campaign ranked, stop-use advisories first, 90-day trends and a script that checks your own vehicle list.
> - **[All Three Monday Briefs: Rates, Recalls + Exploited Vulns](https://buy.polar.sh/polar_cl_k7zU5TjNPK3lFhEnKjkmIiFMxcSFKBmVVp0IS3PUNZE?utm_source=huggingface&utm_medium=free-asset&utm_campaign=recallroll-vehicle-recalls&utm_content=monday-briefs-3)** ($25/month): all three weekly briefs (Treasury/BLS rates & macro, NHTSA recalls, CISA KEV/EPSS) for $25/month instead of $37.
> - Using it at work? **[CyberMax Dataset Commercial License: Small (up to 10 people)](https://buy.stripe.com/5kQ9AT4A40oVfF7dlNbV61L?utm_source=huggingface&utm_medium=free-asset&utm_campaign=recallroll-vehicle-recalls&utm_content=st-dataset-license-small&client_reference_id=data_hf-recallroll-vehicle-recalls)** ($49/year, direct checkout; bigger teams: [Business and Enterprise](https://cybermaxtools.com/store/dataset-license/)): Commercial licence and support for one company or organisation with up to 10 people, for one year; first support reply within 2 business days.
> - **[Get an email when this dataset updates](https://data.cybermaxtools.com/notify?ds=recallroll-vehicle-recalls&s=hf-recallroll-vehicle-recalls)**: free, double opt-in, unsubscribe any time.
> - **[CyberMax Store](https://cybermaxtools.com/store/?utm_source=huggingface&utm_medium=dataset&utm_campaign=recallroll-vehicle-recalls)**: every CyberMax data product, API plan and weekly brief in one place.
<!-- cybermax-bridge:end -->

Every US safety recall campaign NHTSA received in the last 365 days (2025-11-12 to 2026-11-06): **943 campaigns** with **38,725,138 vehicles and items potentially affected** (manufacturer estimates), 66 of them in the last 30 days. **25** carry a *Do Not Drive* advisory and **24** a *Park Outside* (fire risk) advisory. Rebuilt from NHTSA's daily recall file; built 2026-11-12 20:39 UTC.

Free lookup page (decode a VIN, see its recalls, bulk-check 50 VINs, CSV): **https://cybermax-tools-cybermax.static.hf.space/recallroll/index.html**

## Configs

| Config | One row per | Rows | Use it for |
|---|---|---|---|
| `recalls` (default) | recall campaign | 943 | what was recalled, why, the risk, the fix, units affected, advisories |
| `vehicles` | campaign × make × model × model year | 5,732 | joining to your own inventory or fleet list by make/model/year |

### `recalls` columns
`campaign` (NHTSA recall number, e.g. 26V601000), `report_received`, `owners_notified`, `manufacturer`, `type` (vehicle / equipment / tire / child seat), `component`, `units_affected`, `initiated_by` (MFR = manufacturer, ODI/OVSC = NHTSA), `mfr_campaign`, `do_not_drive`, `park_outside`, `summary`, `consequence`, `remedy`, `nhtsa_url`, `makes`, `vehicles` (e.g. "FORD F-150 (2021-2023)"), `vehicle_count`.

### `vehicles` columns
`campaign`, `make`, `model`, `model_year` (null when NHTSA lists no year), `report_received`, `component`, `type`, `do_not_drive`, `park_outside`.

## Quick start

```python
from datasets import load_dataset
recalls = load_dataset("CyberMax-tools/recallroll-vehicle-recalls", "recalls", split="train").to_pandas()
print(recalls[recalls.do_not_drive][["campaign", "vehicles", "component"]])
```

Or without downloading: `https://datasets-server.huggingface.co/search?dataset=CyberMax-tools/recallroll-vehicle-recalls&config=vehicles&split=train&query=F-150`

## Limits

- A recall listed for a model year does not mean every vehicle of that year is affected (it may cover a build-date range or one plant), and it may already be repaired. Confirm a specific VIN at https://www.nhtsa.gov/recalls.
- Model names are NHTSA's recall spellings (e.g. "MUSTANG MACH E"), which can differ from VIN-decoder names.
- Information only: not safety, legal or purchase advice. Not affiliated with NHTSA or any manufacturer.

## Source and licence

NHTSA recall flat file `FLAT_RCL_POST_2010.zip` (https://static.nhtsa.gov/odi/ffdd/rcl/), field definitions in `RCL.txt` there. U.S. Government work, no copyright in the U.S. Compiled by CyberMax.
