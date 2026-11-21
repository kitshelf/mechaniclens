---
license: cc-by-4.0
language:
- en
pretty_name: US Vehicle Owner Complaints by Model 2010-2025
size_categories:
- 10K<n<100K
task_categories:
- tabular-classification
- tabular-regression
tags:
- nhtsa
- automotive
- vehicle-safety
- car-reliability
- complaints
- open-data
- united-states
configs:
- config_name: default
  data_files:
  - split: train
    path: nhtsa-complaints-by-model-2010-2025.csv
---

# US Vehicle Owner Complaints by Model, 2010-2025

Owner complaints filed with the US National Highway Traffic Safety Administration (NHTSA), rolled up to one row per make, model, model year and component. It covers model years 2010 to 2025 and 4,087 make, model and model year combinations from 84 makes.

Use it to compare how complaint counts differ between vehicles, which systems owners report most for a given model, and how a model year's complaint count grows as the cars age.

## Key findings

From the [most complained-about cars report](https://oilandmiles.com/reports/most-complained-cars), Q3 2026 edition (NHTSA file dated 2026-08-25, model years 2010-2025):

1. The 2010 Ford Fusion has the most complaints of any vehicle: 5,126, with steering named most (1,640 of them).
2. Ford holds 17 of the 25 most complained-about vehicles, and 45 of the top 100.
3. Ford accounts for 20.8% of all 625,987 complaints in the file; Chevrolet is next at 9.3%.
4. Power train is the component named most in 9 of the top 25 vehicles; steering in 6.
5. The only vehicle from model year 2023 or newer in the top 100 is the 2023 Tesla Model Y, with 1,134 complaints.

New to the data? [`quickstart.ipynb`](quickstart.ipynb) loads the CSV, lists the top 10 vehicles and charts the components for one model.

## Files

| File | What it holds |
|---|---|
| `nhtsa-complaints-by-model-2010-2025.csv` | 90,254 rows, one per make, model, model year and component, every component (loaded by `datasets`) |
| `most-complained-2026-q3.json` | The top 100 vehicles by complaint count, each with the component its owners named most |
| `CHANGELOG.md` | What changed between revisions |
| `build_dataset.py` | Rebuilds the CSV from NHTSA's flat complaint file |
| `latest.json` | The current edition, its dates, both DOIs and the file list |
| `quickstart.ipynb` | Load the CSV, list the top 10 vehicles, chart one vehicle's components (pandas, matplotlib) |

## Columns (CSV)

| Column | Type | Meaning |
|---|---|---|
| `make` | string | Vehicle make as NHTSA records it |
| `model` | string | Vehicle model |
| `model_year` | int | Model year, 2010 to 2025 |
| `component` | string | System named in the complaint, in NHTSA's wording (for example Engine, Air bags, Steering) |
| `complaints` | int | Complaints for this vehicle that name this component |
| `year_total` | int | All complaints for this make, model and model year |

```python
from datasets import load_dataset

ds = load_dataset("iqbaltaher/us-vehicle-owner-complaints-by-model-2010-2025", split="train")
df = ds.to_pandas()
top = df.drop_duplicates(["make", "model", "model_year"]).nlargest(10, "year_total")
```

## How the counts were made

- Source: NHTSA's public consumer complaint file, copy dated 2026-08-25.
- Each complaint number counts once per make, model and model year, and once under each component it names. Model names are kept exactly as NHTSA records them.
- Vehicles with fewer than 10 complaints are dropped.
- One complaint can name several components, so the `complaints` values for a vehicle can sum to more than its `year_total`.

## Limits

- Counts are not failure rates. The file has no sales figures, so models that sell well collect more complaints.
- NHTSA does not verify complaints, and owners file them voluntarily. Recalls and news coverage cause spikes.
- Older model years have had more years on the road to collect complaints than newer ones.

## Source, report and citation

The full edition, with charts, method notes and a per-vehicle lookup, is the [Oil & Miles most complained-about cars report](https://oilandmiles.com/reports/most-complained-cars). The same files are archived on Zenodo with a permanent DOI. Please cite that DOI (revision 2; all versions: [10.5281/zenodo.23662819](https://doi.org/10.5281/zenodo.23662819)):

> Taher, I. (2026). *Most Complained-About Vehicles: NHTSA Owner Complaints by Make, Model and Model Year, 2010-2025 (Q3 2026 Edition)* [Data set]. Oil & Miles. https://doi.org/10.5281/zenodo.23685716

```bibtex
@dataset{taher_2026_most_complained,
  author    = {Taher, Iqbal},
  title     = {Most Complained-About Vehicles: NHTSA Owner Complaints by Make, Model and Model Year, 2010-2025 (Q3 2026 Edition)},
  year      = {2026},
  publisher = {Oil \& Miles},
  version   = {2026-Q3-r2},
  doi       = {10.5281/zenodo.23685716},
  url       = {https://doi.org/10.5281/zenodo.23685716}
}
```

Author: Iqbal Taher, [Oil & Miles](https://oilandmiles.com) ([ORCID 0009-0000-5745-9451](https://orcid.org/0009-0000-5745-9451)). License: CC BY 4.0. The underlying complaint records are US government data from NHTSA.
