---
license: cc0-1.0
pretty_name: U.S. Consumer Product Recalls (CPSC), normalized
configs:
- config_name: default
  data_files: data/recalls.csv
tags: [recalls, consumer-safety, cpsc, public-data, government]
size_categories: [1K<n<10K]
---

# U.S. Consumer Product Recalls (CPSC), normalized

Every consumer product recall published by the U.S. Consumer Product Safety Commission since 2015, flattened
to one row per recall: date, title, products, hazards, remedies, manufacturers, retailers, countries and a link
to the official notice. Rebuilt monthly by Agent Harbor.

- **Source:** CPSC Recalls REST service (saferproducts.gov). U.S. government work, public domain. We release our
  normalized version under CC0 as well.
- **No personal data:** company names only; consumer contact details are not included.
- **Need it live, or vehicles, food, drugs and devices too?** The same normalization across CPSC, NHTSA and FDA is
  available as an always-current API: Agent Harbor's recalls Actor on Apify, or the Rapid API Hub listing.

Not affiliated with or endorsed by CPSC. Always confirm recall details on the official notice.
