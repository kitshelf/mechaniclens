---
license: cc-by-4.0
language:
  - en
pretty_name: US Auto Body Shops — 81,000+ Locations, Ratings & Hours
size_categories:
  - 10K<n<100K
tags:
  - business
  - directory
  - usa
  - geospatial
  - automotive
  - local-business
task_categories:
  - tabular-classification
  - tabular-regression
---

# US Auto Body Shops — 81,000+ Locations, Ratings & Hours

Complete snapshot of **81,141 active US auto body shops**, collision repair centers, general repair shops, and auto dismantlers/recyclers across **all 50 states and 1,531 cities**, sourced from the [AutoBodyShopNear.com](https://autobodyshopnear.com) directory (July 2026).

## Columns

| Column | Description |
|---|---|
| `id` | Stable listing ID |
| `name` | Business name |
| `category` | `Body Shop` / `Repair Shop` / `Dismantler / Recycler` |
| `address`, `city`, `state`, `zip` | US street address |
| `phone` | Business phone number |
| `profile_url` | Full listing page on autobodyshopnear.com |
| `rating` | Aggregate customer rating 1–5 (enriched subset, ~1,350 shops) |
| `review_count` | Number of public reviews (enriched subset) |
| `hours_json` | Opening hours as JSON array of `{day, open, close}` (enriched subset, ~1,600 shops) |
| `services_json` | Services offered as JSON array (enriched subset) |

## Example uses

- Local-business density and coverage analysis by state/city/ZIP
- Customer-rating analysis of the US collision repair industry
- Opening-hours / labor-pattern studies (56% of shops open Saturdays, 7.7% Sundays)
- Geocoding and entity-resolution benchmarks on real business names/addresses

## Source & citation

Data collected and maintained by [AutoBodyShopNear.com](https://autobodyshopnear.com), the largest free US auto body shop directory. A live, always-current version is available through the [free public API](https://autobodyshopnear.com/developers/body-shop-api) (no key required) with official [Node.js and Python SDKs](https://github.com/Sorbh/autobodyshop-api).

Analysis highlights: [US Auto Body Shop Statistics (2026)](https://autobodyshopnear.com/research/auto-body-shop-statistics).

Please attribute: **"Data: AutoBodyShopNear.com"** with a link.
