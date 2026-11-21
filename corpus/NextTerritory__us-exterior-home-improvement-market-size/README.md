---
license: cc-by-4.0
pretty_name: US Residential Exterior Home Improvement Market Size by Metro and State
language:
- en
tags:
- market-size
- roofing
- siding
- windows
- home-improvement
- construction
- united-states
- economics
size_categories:
- n<1K
configs:
- config_name: exterior_wall_systems_by_metro
  data_files: exterior_wall_systems_by_metro.csv
- config_name: exterior_wall_systems_by_state
  data_files: exterior_wall_systems_by_state.csv
- config_name: siding_by_metro
  data_files: siding_by_metro.csv
- config_name: siding_by_state
  data_files: siding_by_state.csv
- config_name: roofing_by_metro
  data_files: roofing_by_metro.csv
- config_name: roofing_by_state
  data_files: roofing_by_state.csv
- config_name: windows_doors_by_metro
  data_files: windows_doors_by_metro.csv
- config_name: windows_doors_by_state
  data_files: windows_doors_by_state.csv
- config_name: gutters_by_metro
  data_files: gutters_by_metro.csv
- config_name: gutters_by_state
  data_files: gutters_by_state.csv
---

# US Residential Exterior Market Size — by Metro and State (2026)

Annual installed-value market size for US residential roofing, siding, windows & doors and gutters — all 935 US metro and micropolitan areas (CBSAs) and every state, built bottom-up from Census, BLS and NOAA data.

Source and live, browsable version: **[nextterritory.com](https://nextterritory.com)**. Each figure
has its own page — national (e.g. [https://nextterritory.com/us-roofing-market](https://nextterritory.com/us-roofing-market)),
state (e.g. [https://nextterritory.com/us-roofing-market/texas](https://nextterritory.com/us-roofing-market/texas)) and
metro (e.g. [https://nextterritory.com/markets/atlanta/roofing](https://nextterritory.com/markets/atlanta/roofing)).

## Headline figures (annual, installed value)

| Line | Total | Replacement | New construction | Page |
|---|---|---|---|---|
| Exterior Wall Systems | $81.53B | $66.79B | $14.74B | [https://nextterritory.com/us-exterior-wall-systems-market](https://nextterritory.com/us-exterior-wall-systems-market) |
| Siding | $42.50B | $33.97B | $8.53B | [https://nextterritory.com/us-siding-market](https://nextterritory.com/us-siding-market) |
| Roofing | $67.68B | $58.58B | $9.10B | [https://nextterritory.com/us-roofing-market](https://nextterritory.com/us-roofing-market) |
| Window & Door Replacement | $39.03B | $32.82B | $6.20B | [https://nextterritory.com/us-window-door-replacement-market](https://nextterritory.com/us-window-door-replacement-market) |
| Gutter | $8.76B | $7.41B | $1.35B | [https://nextterritory.com/us-gutter-market](https://nextterritory.com/us-gutter-market) |

## Files

`<line>_by_metro.csv` — one row per CBSA: population, owner-occupied homes,
demand (total, replacement, new construction), annual jobs, specialty-contractor
establishments (BLS QCEW, by NAICS), demand per firm, saturation band, a 0-100
opportunity score, share of US demand and a link to the metro's report.

`<line>_by_state.csv` — one row per state (incl. DC and Puerto Rico):
demand, share of US, annual jobs, largest contributing metro.

Lines: `roofing`, `siding`, `windows_doors`, `gutters`, and
`exterior_wall_systems` (siding + windows & doors combined).

## Definitions

- **Installed value**: what homeowners and builders pay contractors, labor and
  materials together. Not manufacturer shipments — so larger than, and not
  directly comparable with, most industry reports.
- **Residential only**: replacement on existing homes plus new single-family
  construction. Commercial and multifamily excluded.
- **Coverage**: the 935 CBSAs. Rural counties outside a metro are not
  modeled or extrapolated.
- **States**: metro demand apportioned to counties by single-family detached
  housing, so metros crossing a state line are split.
- **Firm counts**: siding and gutters share NAICS 238170 — never sum firms across lines.
- **No growth rate**: housing inputs are one ACS vintage; see the site for measured
  drivers over time (permits, establishments, hail).

## Method (short)

Per metro: eligible owner-occupied single-family homes ÷ the line's service life,
adjusted for housing age and hail exposure, priced at the model's average ticket,
plus single-family permits at a builder price. Full methodology:
[https://nextterritory.com/methodology](https://nextterritory.com/methodology).

Sources: US Census Bureau (American Community Survey 5-year, Building Permits
Survey), Bureau of Labor Statistics (QCEW), NOAA (Storm Events, Climate Normals).

## License and citation

CC BY 4.0 — free to use, including commercially, with attribution.

> NextTerritory (2026). US Residential Exterior Market Size by Metro and State.
> https://nextterritory.com. Licensed CC BY 4.0.

Updated figures are always at [nextterritory.com](https://nextterritory.com).
