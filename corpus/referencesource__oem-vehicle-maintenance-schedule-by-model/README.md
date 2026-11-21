---
pretty_name: "OEM maintenance schedule by vehicle model and year, sourced from the manufacturer's own document"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/oem-vehicle-maintenance-schedule-by-model/
language:
- en
tags:
- reference-data
- provenance
- referencesource-org
configs:
- config_name: default
  data_files:
  - split: train
    path: data/records.jsonl
---
# OEM maintenance schedule by vehicle model and year, sourced from the manufacturer's own document

**Canonical, always-current version: https://referencesource.org/oem-vehicle-maintenance-schedule-by-model/**
Machine-readable: https://referencesource.org/oem-vehicle-maintenance-schedule-by-model/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-08-31
- **Stale after:** 2027-08-31 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 6111

What the manufacturer's own maintenance guide says to do at each mileage/time interval, one record per make, model, model year, interval and service item, each quoted from the manufacturer's own PDF. Toyota publishes a Warranty & Maintenance Guide per model and model year at assets.sia.toyota.com, and those documents are behind every record here — one make so far. Published today: the 2024 Camry, the 2026 Camry, the 2025 Corolla, RAV4, Tacoma, Tundra, Highlander, 4Runner and Sienna, and the 2026 Sequoia Hybrid, including the Special Operating Conditions schedule and the condition each of those items applies under. The 2025 Camry and 2025 Prius guides have been fetched and checked, and their records are deliberately not published here yet.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

Facts taken from Toyota's own published Maintenance Guide/Owner's Manual Supplement PDFs, one short verbatim quote per record with a link back to the PDF. No page, chart or table is reproduced in full; each record is one line item's own words, not the assembled chart. Facts are not copyrightable (Feist, 1991); what is taken here is a maintenance fact plus a short attributed quote linking back to Toyota's own document.

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-24Camry/pdf/T-MMS-24Camry.pdf
- https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-25Corolla/pdf/T-MMS-25Corolla.pdf
- https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-254Runner/pdf/T-MMS-254Runner.pdf
- https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-25Highlander/pdf/T-MMS-25Highlander.pdf
- https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-25Prius/pdf/T-MMS-25Prius.pdf
- https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-25RAV4/pdf/T-MMS-25RAV4.pdf
- https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-25Sienna/pdf/T-MMS-25Sienna.pdf
- https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-25Tacoma/pdf/T-MMS-25Tacoma.pdf
- https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-25Tundra/pdf/T-MMS-25Tundra.pdf
- https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-25Camry/pdf/T-MMS-25Camry.pdf
- https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-26Camry/pdf/T-MMS-26Camry.pdf
- https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-26SequoiaHV/pdf/T-MMS-26SequoiaHV.pdf

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/oem-vehicle-maintenance-schedule-by-model/
