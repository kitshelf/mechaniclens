# Line anatomy — the vocabulary

The words the report uses for a line on a repair document, defined once. This is a glossary, not a rubric: it says what a term *is*, never whether a line carrying it should be flagged. Whether a line fires a pattern is [`../estimate/rubrics/patterns-estimate.md`](../estimate/rubrics/patterns-estimate.md); the label definitions are [`labels.md`](labels.md); which documents the kit decodes is [`document-types.md`](document-types.md).

**Why this file lives in `shared/`.** `document-types.md` names what each document contains and `after-repair.md` compares parts, labor, fees, taxes, and total across two documents — both need the same vocabulary. Housing it in `estimate/01-estimate/estimate.md` would have forced two `shared/` files to point up into one workflow. One owner, here; workflows point at this file and do not restate it.

**The rule for this file:** if a report uses a word for a line that is not defined here, that is a defect in this file — add the term, do not define it in a second place.

## How a document is built

- **Line item** — one row of the document: a part, an operation, a fee, or a tax. Labels attach to line items, never to the document as a whole.
- **Estimate** — the document handed over *before* work begins, stating intended work and amounts. It may be titled estimate, quote, quotation, or work order; the title does not change what it is.
- **Work order** — often the same paper as the estimate, sometimes the authorization form. When one sheet is both, say so.
- **Invoice** — the document given *after* the work, stating what was actually billed. It is a different document type; the kit compares it to the estimate on request and does not read it as an estimate.
- **Total as written** — the figure printed on the document, quoted exactly as it appears. The kit never computes a competing total.

## Parts

- **Part name** — the plain description on the line ("front brake pad set"). Not invented, and not expanded into a diagnosis.
- **Part number** — the identifier the shop or manufacturer uses. A line without one is a documentation gap, stated as `[NOT SHOWN]`.
- **Quantity** — how many units the line bills. Without a stated reason for the number, the quantity is not self-evident.
- **Unit price** — the amount for one unit; the line total is usually quantity × unit price. When only the line total appears, the unit price is not shown.
- **OEM (original equipment manufacturer)** — the part made to the vehicle maker's specification and sold under the maker's brand or part number.
- **Aftermarket** — a part made by a company other than the vehicle maker, sold as a replacement. It may be equal, better, or lesser quality; the term itself says nothing about which.
- **Remanufactured** — a used part rebuilt to a specification, then sold as a unit. Distinct from "used."
- **Salvage** — a part taken from another vehicle and sold as-is. Distinct from remanufactured.
- **Core charge** — a deposit billed on a remanufactured or rebuilt part, refunded when the old part is returned. It is conditional money, not a price.
- **Kit or assembly** — a set of parts sold and billed as one unit. The parts inside may or may not be listed individually.
- **Markup** — the difference between what the shop paid for a part and what it bills. The document rarely states it, and the kit never computes or judges it.

## Labor

- **Operation** — the named job a labor line covers ("replace front pads," "diagnose ABS light"). One line, one operation, or the line is unclear.
- **Labor hours** — the time billed for an operation.
- **Book time** — the published labor time for an operation (a flat-rate guide or the manufacturer's figure), not the clock time the technician spent.
- **Actual time** — the real clock time the technician spent on the vehicle.
- **Labor rate** — the charge per hour. The labor total is hours × rate when both are shown.
- **Flat rate** — a fixed price or fixed hours for an operation, independent of actual time. Not the same as a labor rate.
- **Diagnosis** — the separate step of finding out what is wrong: scan, test, road test, teardown to inspect. It is not a repair.
- **Diagnostic labor** — diagnosis billed as labor, as distinct from a diagnostic fee.
- **Remove-and-reinstall (R&R)** — taking a part off and putting it back, often to reach another part. It may be its own line or part of the main operation's hours.
- **Overlapping labor** — two labor lines whose hours appear to cover the same access, removal, or operation.
- **Add-on labor** — labor for work beyond the complaint the customer brought in, usually found during diagnosis.

## Fees

A fee is a charge that is neither a part nor an operation. The document's own word for it is quoted; the kit's job is to find out what it buys.

- **Diagnostic fee** — a charge for diagnosis as a separate line, sometimes credited toward the repair if approved.
- **Shop supplies** — a charge for consumables (cleaners, sealants, rags, gloves), often a percentage of labor.
- **Environmental fee** — a charge for handling or disposing of regulated material such as used oil or refrigerant.
- **Hazmat fee** — the same idea under a hazardous-materials name; the two are often used interchangeably on a document.
- **Disposal fee** — a charge to get rid of old parts or drained fluids.
- **Administrative fee** — a charge for paperwork, filing, or shop administration, with no work attached.
- **Document fee** — an administrative fee under a different name.
- **Storage fee** — a daily or flat charge for keeping the vehicle, usually starting after the work is done or after notice.
- **"Misc" or "other"** — a catch-all line whose contents are named nowhere on the document.

## Taxes and the base

- **Tax rate** — the percentage applied, when the document shows it.
- **Fee base** (or **tax base**) — *what* a tax or fee is applied to: parts, labor, both, or the whole total. Without it, the arithmetic cannot be checked from the paper.
- **Sales tax** — the jurisdiction's tax on the transaction, where the document charges one.

## Scope words

- **Symptom** — what the vehicle is doing, in the customer's own words. The kit checks the quoted work against it and never diagnoses from it.
- **Recommended** — suggested work, including manufacturer-scheduled maintenance, that the vehicle does not need in order to run or to fix the complaint.
- **Required** — work the document states must be done, and says why (safety, the repair, or a manufacturer requirement).
- **Deferred maintenance** — scheduled service that was put off earlier and is now due or overdue; on an estimate it may arrive bundled with a repair.
- **Safety inspection** — a check of safety-related systems, sometimes added to a repair, that should name what it found.
- **"While we're in there"** — work proposed because the vehicle is already partly apart, rather than because the complaint requires it.

## Paperwork words

- **Validity date** — how long the estimate's amounts stand ("valid until," "good through"). Absent means the number has no stated shelf life.
- **Authorization line** — the place on the document where the customer approves or declines work, usually a signature or initials field.
- **Written authorization** — approval recorded on paper or in writing, per line or per job.
- **Verbal authorization** — approval given by phone or in conversation. It is a real approval and a weak record; the kit asks for the written one.
- **Technical service bulletin (TSB)** — a manufacturer's published notice about a known condition and its remedy. It is a numbered document; "per TSB" without the number is an unnamed reference.

## Fields the document leaves out

`[NOT SHOWN]` and `[CONFIRM: ...]` are defined in [`labels.md`](labels.md) §The markers. They are not redefined here: a blank field is `[NOT SHOWN]`; a fact only the user or the shop can supply is `[CONFIRM: ...]`.