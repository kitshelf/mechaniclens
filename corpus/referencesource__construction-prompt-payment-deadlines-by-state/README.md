---
pretty_name: "Construction prompt payment act deadlines by US state — owner-to-contractor and contractor-to-subcontractor payment windows, retention release deadlines, and late-payment interest rates"
license: other
license_name: source-terms-cited
license_link: https://referencesource.org/construction-prompt-payment-deadlines-by-state/
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
# Construction prompt payment act deadlines by US state — owner-to-contractor and contractor-to-subcontractor payment windows, retention release deadlines, and late-payment interest rates

**Canonical, always-current version: https://referencesource.org/construction-prompt-payment-deadlines-by-state/**
Machine-readable: https://referencesource.org/construction-prompt-payment-deadlines-by-state/data.json — this mirror is a point-in-time copy.

- **Last verified:** 2026-11-20
- **Stale after:** 2027-08-14 (past this date, prefer the canonical copy —
  it re-verifies on a cadence this snapshot does not)
- **Records:** 43

State-by-state comparison of the statutory deadlines that govern how quickly parties on a construction project must pay each other. Each record is one state with the owner-to-contractor payment deadline (days from invoice), contractor-to-subcontractor flow-down deadline (days from receipt of payment), retention release deadline (days from completion), late-payment interest rate (monthly or annual), whether the statute covers private projects, public projects, or both, and the statutory citation. Deadlines range from 7 days (some flow-down requirements) to 45+ days. Interest rates range from 1% to 2% per month. Answers 'how many days does an owner have to pay me in [state]', 'when must I pay my subs after I get paid', and 'what interest rate can I charge for late payment on a construction project'.

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

- https://www.levelset.com/prompt-payment/alabama-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/alaska-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/arizona-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/arkansas-prompt-payment-faqs/
- https://mechanicslien.com/california-prompt-payment-act/
- https://www.levelset.com/prompt-payment/colorado-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/connecticut-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/delaware-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/florida-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/georgia-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/hawaii-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/illinois-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/kansas-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/kentucky-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/louisiana-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/maine-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/maryland-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/massachusetts-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/michigan-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/minnesota-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/mississippi-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/missouri-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/montana-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/nebraska-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/nevada-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/new-jersey-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/new-mexico-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/new-york-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/north-carolina-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/ohio-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/oklahoma-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/oregon-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/pennsylvania-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/south-carolina-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/tennessee-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/texas-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/utah-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/vermont-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/virginia-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/washington-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/west-virginia-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/wisconsin-prompt-payment-faqs/
- https://www.levelset.com/prompt-payment/wyoming-prompt-payment-faqs/

## Fields

See any record in `data/records.jsonl` — field names are self-describing,
and the canonical page for each record renders them with labels:
https://referencesource.org/construction-prompt-payment-deadlines-by-state/
