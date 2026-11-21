# Document types

The kit decodes documents the customer is asked to sign or pay. Each type has its own anatomy, but the labels, the no-prices rule, and the question discipline stay the same.

## Repair estimate — primary

The document a shop hands the customer before work begins. It may be called an estimate, a quote, or a work order. It lists parts, labor, fees, and sometimes a diagnosis charge.

The kit reads each line into the categories defined once in [`anatomy.md`](anatomy.md) — parts, labor, fees, taxes, and the total as written — plus what the document does not state.

What the kit does not do: price the job, diagnose the car, or judge the shop.

## Final invoice — after-repair branch

The document the customer receives after the work. It should match the approved estimate. The kit compares the two: what was authorized, what was billed, and what changed.

This is a branch, not a separate workflow. It runs only when the user says the work is done and provides both documents. See [`after-repair.md`](after-repair.md).

## Body-shop or insurance estimate — candidate

An estimate produced for an insurance claim, often by the insurer or a body shop. It has its own conventions: supplements, betterment, depreciation, and insurer-approved labor rates. The kit does not claim to decode this type yet. If a user brings one, say so and offer the general anatomy pass without pretending the insurance conventions are covered.

## Adding a document type

Follow `CONVENTIONS.md` §Building a new document type. Confirm the need is real, write the type's anatomy and question library, add fixtures with a near-miss clean document, and only then list it as supported.
