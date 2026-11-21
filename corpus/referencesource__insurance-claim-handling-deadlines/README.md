---
pretty_name: "How long an insurer has to acknowledge, decide and pay a claim, by state: statutory and regulatory claim-handling deadlines"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/insurance-claim-handling-deadlines/
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
# How long an insurer has to acknowledge, decide and pay a claim, by state: statutory and regulatory claim-handling deadlines

**Canonical, always-current version: https://referencesource.org/insurance-claim-handling-deadlines/**
Machine-readable: https://referencesource.org/insurance-claim-handling-deadlines/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-10-10
- **Stale after:** 2027-02-07 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 42

The deadlines each US state puts on an insurance company handling a claim: how many days to acknowledge that a claim was received, how many days to reply to a policyholder's communication, how many days to accept or deny the claim after receiving proof of loss, how many days to pay once it has accepted, and what interest or penalty runs if it misses. Each record is one deadline in one state, carrying the number of days exactly as the state writes it, whether they are calendar, business or working days, the event the clock starts from, the citation to the statute or administrative rule that sets it, and the verbatim sentence. Answers 'how long does an insurance company have to pay a claim in Texas', 'what is the deadline for an insurer to deny a claim', 'how many days does my insurer have to acknowledge my claim in Ohio', and 'my insurer has had my proof of loss for 46 days — has a deadline passed'. No single original exists: every state adopted its own version of the NAIC Unfair Claims Settlement Practices model, half of them in a statute and half in an administrative rule, and NAIC's own topic page for it is now a 404.

## Provenance — what every record carries

Every record carries `source` (the URL the value was read from) and
`source_quote` (a verbatim quote from that page stating it). A value you
cannot check against its page is indistinguishable from an invented one;
these can all be checked. Each record is also individually addressable on
the canonical site at its `url`.

## Licence position

Facts extracted from state statutes and administrative codes published free by state legislatures, secretaries of state and code publishers. Statutory text is not copyrightable in the United States. Each record quotes one sentence and links back to the state's own page for it. No compilation is reproduced.

Facts are not copyrightable; what this dataset takes from each source is a
fact plus a short attributed quote linking back to the page that states it.

## Sources

- https://www.flsenate.gov/Laws/Statutes/2025/627.70131
- https://www.revisor.mn.gov/statutes/cite/72A.201
- https://www.leg.state.nv.us/nac/nac-686a.html
- https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_58/GS_58-63-15.html
- https://codes.ohio.gov/ohio-administrative-code/rule-3901-1-54
- https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/031/chapter146/chap146toc.html
- https://law.lis.virginia.gov/admincode/title14/agency5/chapter400/section50/
- https://app.leg.wa.gov/WAC/default.aspx?cite=284-30-370
- https://docs.legis.wisconsin.gov/code/admin_code/ins/6/11

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/insurance-claim-handling-deadlines/
