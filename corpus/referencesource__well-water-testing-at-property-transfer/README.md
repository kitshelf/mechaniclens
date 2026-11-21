---
pretty_name: "Private well water testing at property sale: which states require it"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/well-water-testing-at-property-transfer/
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
# Private well water testing at property sale: which states require it

**Canonical, always-current version: https://referencesource.org/well-water-testing-at-property-transfer/**
Machine-readable: https://referencesource.org/well-water-testing-at-property-transfer/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-08-18
- **Stale after:** 2027-08-18 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 13

For each US state whose statute or health department states a position: whether private well water must be tested when a home is sold, what must be tested for, and who is responsible. Four of the thirteen states here require it by law — New Jersey's Private Well Testing Act (seven named parameters, as a condition of sale), Oregon's ORS 448.271 (the seller tests for arsenic, nitrate and total coliform and reports the results), Rhode Island's RIGL 23-1-5.3 (eight analytes, prior to sale) and Maryland's Real Property 10-713 (since 2024, and the duty is the purchaser's, waivable in writing). The rest state that they do not: Virginia, Minnesota, Vermont, Wisconsin, Tennessee, Florida and Louisiana each say so in their own words, several while noting that the requirement a seller actually meets is the lender's or the county's — Minnesota names the lending institution and Dakota County in the same paragraph, and Washington's health department points at the county and the lender rather than at the state. Connecticut requires notice that testing material exists, not a test. Answers 'do I have to test the well water to sell my house in [state]', 'what does [state] require well water to be tested for at closing', and 'is a well test required for the buyer's loan or by law'. States whose authority states nothing get no record, and a duty to disclose a past test is not a duty to test.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

unknown

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://portal.ct.gov/dph/-/media/departments-and-agencies/dph/dph/environmental_health/private_wells/pdf/for-real-estate-professionals---educational-materials-concerning-private-well-testing.pdf
- https://www.floridahealth.gov/environmental-health/private-well-testing/index.html
- https://ldh.la.gov/page/real-estate-testing-requirements
- https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=grp&section=10-713&enactments=false
- https://www.health.state.mn.us/communities/environment/water/wells/disclosures/wellsatpropertytransfer.html
- https://pub.njleg.state.nj.us/Bills/2000/PL01/40_.PDF
- https://www.oregonlegislature.gov/bills_laws/ors/ors448.html
- https://webserver.rilegislature.gov/Statutes/TITLE23/23-1/23-1-5.3.htm
- https://www.tn.gov/environment/program-areas/wr-water-resources/water-quality/well-water.html
- https://www.healthvermont.gov/environment/drinking-water/new-drilled-well-testing-what-you-need-know
- https://www.vdh.virginia.gov/environmental-health/real-estate-transfer-faq/
- https://doh.wa.gov/community-and-environment/drinking-water/contaminants/testing-your-water
- https://dnr.wisconsin.gov/topic/Wells/RETransfer.html

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/well-water-testing-at-property-transfer/
