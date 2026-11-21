---
pretty_name: "Minimum auto liability insurance limits by state"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/auto-insurance-minimums/
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
# Minimum auto liability insurance limits by state

**Canonical, always-current version: https://referencesource.org/auto-insurance-minimums/**
Machine-readable: https://referencesource.org/auto-insurance-minimums/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-08-10
- **Stale after:** 2027-02-06 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 51

The minimum auto liability insurance a driver must carry in each US state and DC, as bodily injury per person, bodily injury per accident, and property damage per accident (the '25/50/10' shorthand), sourced one state at a time from that state's own statute, insurance department or DMV — never from an aggregator. Answers 'what is the minimum auto liability insurance required in [state]', 'minimum auto liability limits by state 2026', 'which states changed their minimum auto liability limits in 2025 or 2026 and what were the limits before and after', 'is it true that California's minimum auto liability limits are 15/30/5' (no — California raised its minimums to 30/60/15 effective 1 January 2025, its first increase since 1967; separately, New Jersey raised its minimums to 35/70/25 effective 1 January 2026), and 'what would I use to get state minimum liability limits as data rather than reading comparison sites'. No federal agency and no single publisher states this for all 50 states — it is 50 statutes and 50 insurance departments, seven of which changed in 2025 or 2026 (NJ, CA, NC, MA, UT, VA and HI), which is why every page-one search result is a lead-generation or law-firm site quoting numbers with no citation. A handful of states (Tennessee, California, New Jersey) also let a driver satisfy the requirement with a bond or cash deposit instead of a policy, at a stated dollar amount — recorded where the source states it. Florida and Michigan run materially different systems (Florida requires PIP/PDL, not a bodily-injury minimum; Michigan lets drivers choose down to a floor after a 2020 no-fault reform) and New Hampshire does not mandate insurance at all — these are recorded as stated, not forced into the standard three-number shape.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

Facts and short attributed quotes taken from each state's own statute, insurance department or DMV page, linking back to the source. Facts are not copyrightable (Feist, 1991); no source page's compiled table is reproduced wholesale. No source in this list carries a restrictive reuse notice as of the date fetched.

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://aldoi.gov/consumers/AutoFAQ.aspx
- https://dmv.alaska.gov/driver-services-adjudication/mandatory-insurance/
- https://www.azleg.gov/ars/28/04009.htm
- https://insurance.arkansas.gov/documents/automobile-insurance-brochure/
- https://www.insurance.ca.gov/01-consumers/105-type/95-guides/01-auto/auto101.cfm
- https://doi.colorado.gov/types-of-insurance/auto-insurance
- https://portal.ct.gov/cid/consumer-information-center/auto-insurance
- https://dmv.de.gov/VehicleServices/registration/index.shtml?dc=ve_reg_insurance
- https://code.dccouncil.gov/us/dc/council/code/sections/31-2406
- https://www.flhsmv.gov/insurance/
- https://oci.georgia.gov/insurance-resources/auto
- https://cca.hawaii.gov/wp-content/uploads/2026/01/Auto-Minimum-Limits-FAQs.pdf
- https://doi.idaho.gov/consumers/auto-insurance/required-auto-coverage/
- https://idoi.illinois.gov/consumers/consumerinsurance/auto-insurance-shopping-guide.html
- https://www.in.gov/bmv/licenses-permits-ids/suspension-and-reinstatement/proof-of-financial-responsibility/
- https://iid.iowa.gov/consumers/insurance/auto
- https://insurance.ks.gov/documents/department/publications/auto-shoppers-guide.pdf
- https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=46758
- https://www.ldi.la.gov/docs/default-source/documents/publicaffairs/consumerpublications/consumer's-guide-to-auto-insurance.pdf?sfvrsn=c0907c52_83
- https://www.maine.gov/pfr/insurance/consumers/auto-insurance/insurance-required-by-law
- https://mva.maryland.gov/title-registration/auto-insurance-requirements
- https://malegislature.gov/Laws/SessionLaws/Acts/2024/Chapter275
- https://www.michigan.gov/autoinsurance/choosing-coverage/choosing-bodily-injury-coverage
- https://www.revisor.mn.gov/statutes/cite/65B.49/pdf
- https://www.mid.ms.gov/mississippi-insurance-department/consumers/auto-insurance/
- https://dor.mo.gov/driver-license/insurance/
- https://csimt.gov/your-insurance/auto/
- https://doi.nebraska.gov/important-auto-insurance-and-types-coverage
- https://doi.nv.gov/Consumers/Automobile-Insurance/
- https://gc.nh.gov/rsa/html/XXI/259/259-61.htm
- https://nj.gov/dobi/division_consumers/insurance/standardpolicy.html
- https://www.mvd.newmexico.gov/vehicles/insurance/
- https://newyork.public.law/laws/n.y._vehicle_and_traffic_law_section_311
- https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_20/GS_20-279.21.html
- https://www.insurance.nd.gov/consumers/insurance/auto
- https://codes.ohio.gov/ohio-revised-code/section-4509.51
- https://www.oid.ok.gov/auto-insurance-common-myths/
- https://www.oregonlegislature.gov/bills_laws/ors/ors806.html
- https://www.pa.gov/agencies/insurance/consumer-help-center/learn-about-insurance/auto-insurance
- https://webserver.rilegislature.gov/Statutes/TITLE31/31-32/31-32-2.htm
- https://doi.sc.gov/Faq.aspx?QID=352
- https://sdlegislature.gov/api/Statutes/32-35-70.html
- https://revenue.support.tn.gov/hc/en-us/articles/360060282311-DIFD-1-Insurance-Verification-Overview
- https://www.tdi.texas.gov/pubs/consumer/cb020.html
- https://le.utah.gov/xcode/Title31A/Chapter22/C31A-22-S304_2023050320230503.pdf
- https://dfr.vermont.gov/consumers/explore-insurance/auto
- https://law.lis.virginia.gov/vacode/title46.2/chapter4/section46.2-472/
- https://www.insurance.wa.gov/insurance-resources/auto-insurance/how-auto-insurance-works/washington-states-mandatory-automotorcycle-insurance-law
- https://www.wvinsurance.gov/Consumer_Services_mandatory_limits
- https://wisconsindot.gov/pages/dmv/license-drvs/rcd-crsh-rpt/auto-insurance.aspx
- https://wyoleg.gov/statutes/compress/title31.pdf

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/auto-insurance-minimums/
