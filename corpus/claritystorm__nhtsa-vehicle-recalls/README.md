---
license: other
license_name: public-domain
task_categories:
- tabular-classification
- tabular-regression
tags:
- vehicles
- safety
- recalls
- automotive
- united-states
pretty_name: NHTSA Vehicle Recalls 1966–March 2026
---

# NHTSA Vehicle Recalls 1966–March 2026

**One-time dated snapshot.**

Recall campaign and affected-product records with defect and remedy text.

**Verified coverage:** Recall dates: 1966-01-19 through 2026-03-26.

**Records:** 176,073 product rows; 29,865 distinct campaign IDs.

This repository contains a **1,000-row public sample**, not the full package. A sample does not establish complete historical coverage.

## Limitations

- Multiple product/model rows can belong to the same campaign. Count distinct campno values for campaign totals.
- do_not_drive and park_outside are missing throughout this snapshot. Missing values do not mean that no warning exists.
- This historical snapshot cannot establish current recall status for a particular VIN.
- Current official files contain additions and revisions to historical records; this dated snapshot is not a complete copy of today's affected-product listings.

Package upload: 2026-03-31. Listing reviewed: 2026-09-19. These dates do not extend source coverage. This review did not refresh the data.

## Existing package tables

| File | Rows | Fields |
|---|---:|---:|
| `nhtsa_recalls.parquet` | 176,073 | 32 |

Counts are per table, not independent events. Full field names and types are on the dataset page.

## Inspect the public CSV

```python
import pandas as pd
df = pd.read_csv("sample_1000.csv")
print(df.shape)
print(df.columns.tolist())
print(df.head())
```

## Availability

The dated snapshot is available for a one-time **$59** purchase, subject to its documented limitations and license terms. Future updates are not included.

New annual update subscriptions and bundle purchases are paused. Existing customers retain their purchase download access and can contact support@claritystorm.com for assistance.

[Current dataset details and availability](https://www.claritystorm.com/datasets/nhtsa-recalls)

[Government source portal](https://www.nhtsa.gov/vehicle-safety/recalls)
