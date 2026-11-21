---
license: cc0-1.0
language:
- en
tags:
- real-estate
- housing
- building-permits
- urban-economics
- construction
- united-states
- time-series
pretty_name: PermitBase — U.S. Residential Building Permits 1980-2024
size_categories:
- 100K<n<1M
task_categories:
- time-series-forecasting
- tabular-regression
source_datasets:
- original
---

# PermitBase — U.S. Residential Building Permits 1980–2024

**The most comprehensive historical residential building permit dataset available at the place level.**

Place-level | Annual | 1980–2024 | SF/MF differentiated | 51 jurisdictions | 683,986 records

---

## Dataset Description

This dataset contains annual residential building permit data for permit-issuing places
(cities, towns, and unincorporated county areas) across the United States, covering
1980 through 2024. It is derived from the U.S. Census Bureau's Building Permits Survey (BPS)
and has been cleaned, normalized, and enriched with Census region labels, housing cycle
annotations, and multifamily share calculations.

**Source:** U.S. Census Bureau, Building Permits Survey (BPS)  
**License:** CC0 1.0 (source data is U.S. federal government, public domain)  
**API access:** [permitbase.org](https://permitbase.org) — query the live dataset via REST API or MCP

---

## What Makes This Dataset Unique

Most existing permit datasets start around 2000. This dataset begins in **1980** — capturing:
- The S&L crisis (1989–1991)
- The 1990s long expansion
- The housing bubble and crash (2001–2009)
- The post-crisis recovery
- The COVID-era surge
- The current rate correction

It also provides **clean SF/MF differentiation** at the place level:
- 1-unit (single family)
- 2-unit (duplex)
- 3–4 unit
- 5+ unit (multifamily)
- Pre-computed MF total and MF% per record

---

## Schema

| Column | Type | Description |
|--------|------|-------------|
| `Year` | int | Survey year (1980–2024) |
| `Region` | string | Census region (Northeast, Midwest, South, West) |
| `State_Code` | int | 2-digit FIPS state code |
| `State` | string | State name |
| `County_Code` | int | 3-digit FIPS county code |
| `Place` | string | City, town, or unincorporated area name |
| `Months_Reported` | int | Months of data reported (0–12; <12 = partial) |
| `SF_Units` | int | 1-unit (single family) units permitted |
| `MF_2Unit` | int | 2-unit (duplex) units permitted |
| `MF_34Unit` | int | 3–4 unit structures, total units |
| `MF_5Plus` | int | 5+ unit structures, total units |
| `MF_Total` | int | Sum of MF_2Unit + MF_34Unit + MF_5Plus |
| `Total_Units` | int | SF_Units + MF_Total |
| `MF_Pct` | float | MF_Total / Total_Units (0.0–1.0) |
| `Cycle` | string | Housing market cycle label (see below) |

### Housing Cycle Labels

| Cycle | Years |
|-------|-------|
| Early 80s Contraction | 1980–1981 |
| Mid-80s Expansion | 1982–1988 |
| S&L Crisis Downturn | 1989–1991 |
| 90s Long Expansion | 1992–2000 |
| Housing Bubble | 2001–2005 |
| Financial Crisis Bust | 2006–2009 |
| Post-Crisis Trough | 2010–2012 |
| Long Recovery | 2013–2019 |
| COVID Shock | 2020 |
| Post-COVID Boom | 2021–2022 |
| Rate Correction | 2023–present |

---

## Coverage Notes

| Region | Full Coverage | Partial / Missing |
|--------|--------------|-------------------|
| South (17 states) | 1980–2021, 2023 | 2022 (Feb only), 2024 (Mar only) |
| Midwest (12 states) | 1980–2020 | 2021–2024 not yet added |
| Northeast (9 states) | 1980–2018 | 2019 (Jan only), 2020–2024 not added |
| West (15 states) | 1980–2018 | 2019 (Jan only), 2020–2024 not added |

For live, fully updated national data, use the [PermitBase API](https://permitbase.org).

---

## Usage Examples

```python
import pandas as pd

df = pd.read_csv("national_permits_master.csv")

# National annual totals
nat = df.groupby('Year')[['SF_Units','MF_Total','Total_Units']].sum()
print(nat.loc[2005])  # Peak: 2.16M units

# Top 10 most active cities all-time
top = df.groupby(['State','Place'])['Total_Units'].sum().nlargest(10)
print(top)

# MF-heavy markets (min 5,000 units, ranked by MF share)
by_place = df.groupby(['State','Place']).agg(
    MF=('MF_Total','sum'), Tot=('Total_Units','sum')).reset_index()
by_place = by_place[by_place['Tot'] >= 5000]
by_place['MF_Pct'] = by_place['MF'] / by_place['Tot']
print(by_place.nlargest(10,'MF_Pct'))

# Texas post-GFC recovery
tx = df[(df['State']=='Texas') & (df['Year'].between(2009,2015))]
tx_yr = tx.groupby('Year')['Total_Units'].sum()
print(tx_yr.pct_change())
```

---

## API Access

The live, continuously updated dataset is available via the PermitBase REST API and MCP server:

```bash
# Annual trends for any state
curl https://api.permitbase.org/v1/permits/annual \
  -H "X-API-Key: your_key" \
  -d "state=California&year_from=2000"

# Top multifamily markets
curl https://api.permitbase.org/v1/permits/rankings \
  -H "X-API-Key: your_key" \
  -d "ranked_by=mf&limit=25"
```

Free tier: 50 calls/month, no credit card. Get your key at [permitbase.org](https://permitbase.org).

---

## Citation

If you use this dataset in research, please cite:

```bibtex
@dataset{permitbase2024,
  title     = {PermitBase: U.S. Residential Building Permits 1980--2024},
  author    = {PermitBase},
  year      = {2024},
  url       = {https://huggingface.co/datasets/thanna94/us-building-permits},
  note      = {Derived from U.S. Census Bureau Building Permits Survey (BPS)}
}
```

---

## Related Research

- LaPoint & Cortes (2024): "Housing Is the Financial Cycle: Evidence from 100 Years of Local Building Permits"
- U.S. Census Bureau Building Permits Survey: https://www.census.gov/construction/bps/
