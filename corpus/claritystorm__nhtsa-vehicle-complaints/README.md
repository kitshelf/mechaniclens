---
license: other
license_name: public-domain
task_categories:
- tabular-classification
- text-classification
- tabular-regression
tags:
- vehicles
- safety
- consumer
- automotive
- united-states
- nlp
pretty_name: NHTSA Vehicle Complaints 1995–March 2026
---

# NHTSA Vehicle Complaints 1995–March 2026

**One-time dated snapshot.**

Vehicle complaint records with narratives and component fields.

**Verified coverage:** Added dates: 1995-01-03 through 2026-03-26.

**Records:** 2,189,824 component rows; 1,582,110 complaints.

This repository contains a **1,000-row public sample**, not the full package. A sample does not establish complete historical coverage.

## Limitations

- Failure dates include implausible values through 2203 and model years include the 9999 sentinel. Validate these fields before analysis.
- Coverage is based on complaint-added dates, not incident dates. Consumer reports are allegations, not independently established defects.
- The 2,189,824 rows represent complaint/component records covering 1,582,110 distinct odino values. Count distinct odino values when estimating complaint totals.

Package upload: 2026-03-30. Listing reviewed: 2026-09-19. These dates do not extend source coverage. This review did not refresh the data.

## Existing package tables

| File | Rows | Fields |
|---|---:|---:|
| `nhtsa_complaints.parquet` | 2,189,824 | 53 |

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

The dated snapshot is available for a one-time **$79** purchase, subject to its documented limitations and license terms. Future updates are not included.

New annual update subscriptions and bundle purchases are paused. Existing customers retain their purchase download access and can contact support@claritystorm.com for assistance.

[Current dataset details and availability](https://www.claritystorm.com/datasets/nhtsa-complaints)

[Government source portal](https://www.nhtsa.gov/nhtsa-datasets-and-apis)
