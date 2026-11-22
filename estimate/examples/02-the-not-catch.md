# The not-catch — a near-miss that must stay clean

A full report on a synthetic estimate that looks, line for line, like several patterns — and earns none of them. The document is [`../../tests/fixtures/07-clean-estimate/message.txt`](../../tests/fixtures/07-clean-estimate/message.txt); its answer key is [`../../tests/fixtures/07-clean-estimate/expected.md`](../../tests/fixtures/07-clean-estimate/expected.md).

This is the calibration proof. A decoder that flags this estimate is not being careful; it is being wrong, and it will be wrong on every clean estimate the person brings it.

---

## Reading

MechanicLens — repair estimate
Document: estimate
Reading: Standard 5 · Check 0 · Question this 0

## Anatomy

| Line | Plain-English name | What it claims to cover | Amount |
|---|---|---|---|
| 1 Diagnostic scan, ABS — credited against the repair if approved | Fee — diagnostic | A scan charge with its credit condition written on the line | 145.00 |
| 2 Front wheel bearing, OEM, #WB-8821 | Parts — bearing | One OEM front wheel bearing, part number stated | 178.00 |
| 3 Labor — replace front wheel bearing, book time 1.8 hr @ 140.00/hr | Labor — operation | Removal and replacement, book time and rate stated | 252.00 |
| 4 Shop supplies — 5% of labor, capped at $25.00 | Fee — supplies | A percentage with its base and its cap stated | 12.60 |
| 5 Sales tax 7% on parts and labor | Tax — rate and base | Tax at a stated rate, applied to a named base | 41.13 |

Total as written: 628.73. Validity: 30 days. An authorization line is present at the foot.

## Scope check

Symptom, in the customer's words: "There's a humming noise from the front that gets louder when I turn left."
Quoted work: replace a front wheel bearing, with a diagnostic scan first.
Match: **match** — the work is on the front end, where the noise is described, and a bearing is consistent with a hum that changes with turning.

## Labels

| Line (quoted) | Label | Pattern | Why |
|---|---|---|---|
| "Diagnostic scan, ABS — credited against the repair if approved" — 145.00 | **Standard** | F-1 (not a pattern) | The fee states its credit condition on the line; the pattern's exemption applies. |
| "Front wheel bearing, OEM, #WB-8821" — 178.00 | **Standard** | P-1, P-5 (not a pattern) | Tier and part number are both stated. |
| "Labor — replace front wheel bearing, book time 1.8 hr @ 140.00/hr" — 252.00 | **Standard** | L-1, L-2 (not a pattern) | Basis, hours, and rate all appear; 1.8 × 140.00 is the stated 252.00. |
| "Shop supplies — 5% of labor, capped at $25.00" — 12.60 | **Standard** | F-2 (not a pattern) | Percentage, base, and cap are stated; 5% of labor is the printed 12.60, under the cap. |
| "Sales tax 7% on parts and labor" — 41.13 | **Standard** | D-4 (not a pattern) | The tax base is named on the line. |

Validity and authorization are both present, so D-1 and D-2 do not fire either.

## Questions to ask

A clean read still leaves the person something worth knowing. These are not findings; they are questions the paper cannot answer.

1. "Which side is the bearing — left or right?" — the line does not say; a good answer names it and writes it on the copy.
2. "What did the scan show?" — a good answer describes the reading in one sentence and how it points at the bearing.
3. "If I approve, how does the 145.00 credit appear on the final invoice?" — a good answer says it shows as its own line, taken off the total.

## Decision

- **Approve** — the document answers its own questions: a credited diagnostic, a named and numbered part, a stated labor basis and rate, a capped fee, and a stated tax base.
- **Keep the paper** — photograph it and keep the signed copy for comparison against the final invoice.

Standard is not a price verdict and not an approval recommendation. It means the lines are clear and normal. The decision remains the person's.

## Needs confirmation

[CONFIRM: which side the bearing is on]
[CONFIRM: the scan reading]
[NOT SHOWN: nothing material — this is the point of the fixture]

---

## Why nothing fired

Each of these was deliberately written to sit one step away from a pattern:

| Pattern that almost fired | What stopped it |
|---|---|
| **F-1 Diagnostic fee** | The line says "credited against the repair if approved." The pattern is the *uncredited* fee. |
| **F-2 Shop supplies** | A percentage with a stated base and a cap. The pattern is the unexplained or uncapped fee. |
| **P-1 Markup tier / P-6 OEM ambiguity** | "OEM" is written on the line. The pattern is the unnamed tier. |
| **P-5 Part number missing** | `#WB-8821` is written. |
| **L-1 Book time / L-2 Rate not shown** | "book time 1.8 hr @ 140.00/hr" is all three facts at once. |
| **D-1 No validity date / D-2 No authorization line** | "valid 30 days" and a signature field are both on the paper. |
| **D-4 Tax base unclear** | "on parts and labor" names the base. |

**The rule this example exists to enforce:** a pattern fires only when the document's own wording supports it. A line that answers the question is a **Standard**, and saying so plainly is the hard part of calibration. If this estimate came back with five flags, the kit would be unusable on the clean estimates that are most of what people actually hold.