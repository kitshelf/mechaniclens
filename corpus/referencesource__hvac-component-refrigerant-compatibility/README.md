---
pretty_name: "HVAC refrigerant replacements: retrofit compatibility, safety class, GWP and lubricant"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/hvac-component-refrigerant-compatibility/
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
# HVAC refrigerant replacements: retrofit compatibility, safety class, GWP and lubricant

**Canonical, always-current version: https://referencesource.org/hvac-component-refrigerant-compatibility/**
Machine-readable: https://referencesource.org/hvac-component-refrigerant-compatibility/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-10-10
- **Stale after:** 2027-10-10 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 109

Which refrigerant substitutes for which in air conditioning, heat pump and refrigeration equipment, drawn from the EPA SNAP substitutes list, compressor-manufacturer bulletins (Copeland) and refrigerant-manufacturer replacement guides (Chemours, Honeywell, Arkema). Each record carries the ASHRAE safety classification, GWP, whether the substitute is approved for retrofit or new equipment only, and the compatible lubricant. Answers 'can I put R-454B in an R-410A system', 'what replaces R-22 without changing the oil', and 'is this substitute EPA-acceptable' — questions where the wrong answer damages equipment or breaks federal rules.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

Factual compilation with source citations. EPA SNAP substitute listings are US government work (public domain). Manufacturer figures (Copeland, Chemours, Honeywell, Trane, Arkema) are facts taken with short attributed quotes linking back to the published guide.

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://epa.gov/snap/substitutes-residential-and-light-commercial-air-conditioning-and-heat-pumps
- https://webapps.copeland.com/online-product-information/Publication/LaunchPDF?Index=AEB&PDF=93-11
- https://www.federalregister.gov/documents/2025/11/10/2025-19812/protection-of-stratospheric-ozone-listing-of-substitutes-under-the-significant-new-alternatives
- https://www.epa.gov/sites/default/files/documents/Choosing_Right_R22_Retrofit.pdf
- https://www.chemours.com/en/-/media/files/freon/opteon-freon-general-replacement-guide.pdf
- https://forane.arkema.com/en/forane-refrigerants/forane-retrofits/the-drop-in-myth/
- https://www.freon.com/en/-/media/files/freon/freon-mo99-faq.pdf
- https://prod-edam.honeywell.com/content/dam/honeywell-edam/pmt/oneam/en-us/refrigerants/documents/pmt-am-solstice-454b-applications-guide.pdf
- https://www.shareddocs.com/hvac/docs/1006/Public/06/570-178.pdf
- https://www.trane.com/content/dam/Trane/Commercial/global/products-systems/equipment/unitary/split-systems/rauj-cauj-20-to-120-tons/SS-APG018A-EN_11102024.pdf

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/hvac-component-refrigerant-compatibility/
