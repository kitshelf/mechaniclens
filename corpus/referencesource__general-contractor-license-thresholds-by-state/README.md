---
pretty_name: "General contractor license requirements and dollar thresholds by US state"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/general-contractor-license-thresholds-by-state/
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
# General contractor license requirements and dollar thresholds by US state

**Canonical, always-current version: https://referencesource.org/general-contractor-license-thresholds-by-state/**
Machine-readable: https://referencesource.org/general-contractor-license-thresholds-by-state/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-10-05
- **Stale after:** 2027-10-05 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 11

Do I need a contractor license for this project in my state, and what does it take to get one? Every US state handles general contractor licensing differently: some require a state license for any construction work, others only above a dollar threshold ($1,000 in Arizona, $10,000 residential in Alabama, $100,000 commercial in Alabama), and some have no state-level license at all (municipal only). One record per license type per state, sourced from the state's licensing board. Answers 'do I need a contractor license in Florida', 'what is the minimum project size for a contractor license in Alabama', 'general contractor license requirements by state', and 'how much is a contractor license bond'. New Jersey added a formal licensing system effective February 2026; Montana transitioned from registration to licensing in 2026. The assembled versions on page one are all from insurance lead-gen sites (nextinsurance.com, insureon.com) selling general liability to contractors. Extends the electrician-licence-progression-by-state pattern to general contractors.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

Facts extracted from state licensing board websites, with attributed quote and link back. Licensing requirements are public regulatory facts. No source carries a restrictive notice.

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://lslbc.gov/types-of-licenses/
- https://www.oregon.gov/ccb/Pages/CCB%20License.aspx
- https://www.tn.gov/commerce/regboards/contractors/license/get/contractor.html
- https://genconbd.alabama.gov/about/law/
- https://llr.sc.gov/clb/faq.aspx
- https://lni.wa.gov/licensing-permits/contractors/register-as-a-contractor/
- https://www.tn.gov/commerce/regboards/contractors/license/get/home-improvement.html

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/general-contractor-license-thresholds-by-state/
