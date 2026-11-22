# The catch — a decode where a pattern fires

A full report on a synthetic estimate, shown honestly. The document is [`../../tests/fixtures/01-scope-mismatch/message.txt`](../../tests/fixtures/01-scope-mismatch/message.txt); its answer key is [`../../tests/fixtures/01-scope-mismatch/expected.md`](../../tests/fixtures/01-scope-mismatch/expected.md). This is the shape of a report and the reasoning behind each label — not a recorded model run (those live in `tests/results/`).

The person is holding an estimate for front brake work and has told the shop about a rattle from the back. Nothing here says the shop is wrong. It says the paper does not connect the work to the complaint, and that the connection is worth one question.

---

## Reading

MechanicLens — repair estimate
Document: estimate
Reading: Standard 1 · Check 2 · Question this 3

## Anatomy

| Line | Plain-English name | What it claims to cover | Amount |
|---|---|---|---|
| 1 Front brake pad set, ceramic | Parts — front pads | Ceramic pads for the front brakes; quantity and part number not stated | 129.00 |
| 2 Front brake rotors, pair | Parts — front rotors | Both front rotors; no part number or tier stated | 218.00 |
| 3 Brake fluid flush | Service — fluid | A fluid flush, priced flat, with no reason on the line | 89.00 |
| 4 Labor — replace front pads and rotors, 1.5 hr @ 145.00/hr | Labor — operation | Removing and replacing front pads and rotors; book time and rate stated | 217.50 |
| 5 Shop supplies | Fee — supplies | Consumables; contents and cap not stated | 12.50 |
| 6 Sales tax 7.25% | Tax — rate | Tax at a stated rate; base not stated in words | 48.29 |

Total as written: 714.29.

## Scope check

Symptom, in the customer's words: "There's a rattle from the back of the car when I go over bumps."
Quoted work: front brake pads, front rotors, a brake fluid flush, and the labor to fit them.
Match: **mismatch** — the work is at the front of the car and on the brake system; the complaint is at the rear and about a rattle. No line explains the link.

## Labels

| Line (quoted) | Label | Pattern | Why |
|---|---|---|---|
| "Front brake pad set, ceramic" — 129.00 | **Question this** | S-1 | Front brake work does not answer a rear rattle, and no line says why it would. |
| "Front brake rotors, pair" — 218.00 | **Question this** | S-1 | Same gap as line 1; the rotors are part of the same unlinked job. |
| "Brake fluid flush" — 89.00 | **Check** | S-2 | Fluid service is maintenance, not a fix for a rattle; the line does not say it is optional. |
| "Labor — replace front pads and rotors, 1.5 hr @ 145.00/hr" — 217.50 | **Question this** | S-1 | The labor serves the mismatched parts. |
| "Shop supplies" — 12.50 | **Check** | F-2 | A flat charge with no statement of contents or cap. |
| "Sales tax 7.25%" — 48.29 | **Standard** | — | An ordinary tax line at a stated rate. |

## Questions to ask

1. "I came in about a rattle from the back over bumps. This estimate is for front brakes — can you tell me what connects them?" — a good answer sounds like a concrete link: a finding at the front that explains a noise heard at the rear, or an admission that the two are separate jobs.
2. "Was the rear end looked at at all, and is there a written note of what was found?" — a good answer sounds like a measurement or observation on paper, not "we'll check when it's up."
3. "The brake fluid flush — is that something this job needs, or is it maintenance I can decline?" — a good answer sounds like "maintenance, and you can decline it," with the price staying separate.
4. "What do the shop supplies cover, and is there a cap?" — a good answer sounds like a short list and a ceiling.
5. "How long is this estimate good for?" — a good answer sounds like a date or a number of days.

## Decision

- **Approve as written** — only if the answers connect the front brake work to the rattle in a way you can check against the paper.
- **Approve with questions answered first** — the likely path: hold the estimate, ask questions 1 and 2, and decide once the link is either shown or admitted to be absent.
- **Decline and get a second opinion** — if no line ever connects the work to the complaint. Take the paper, symptom included, to another shop and ask for a scope read.
- **Authorize diagnosis only** — if you want the rear noise investigated first, ask for that as its own written line before anything else is approved.

Documentation habit: photograph the estimate, write down what the counter says about the rattle, and keep the estimate and any later invoice together.

The decision is yours. This report asked two questions and quoted the paper; it did not judge the shop or diagnose the car.

## Needs confirmation

[CONFIRM: whether the rear of the car was inspected, and what was found]
[CONFIRM: what connects the front brake work to a rear rattle]
[CONFIRM: whether the brake fluid flush is required or optional]
[NOT SHOWN: part numbers or tier (OEM / aftermarket) for the pads and rotors]
[NOT SHOWN: validity date]
[NOT SHOWN: authorization line]

---

## Why it landed this way

- **Three lines at the ceiling, not six.** The mismatch is one finding spread across the parts and their labor. Lines 1, 2, and 4 are the same work, so they carry the same label; repeating it is the honest count, padding it further would not be.
- **The flush is a `Check`, not a `Question this`.** Maintenance sold inside a repair is a real question, but the document does name the service. The ceiling label is reserved for lines whose wording or placement leaves a specific question open.
- **The tax is `Standard`.** A stated rate on a stated amount is normal. Labeling it would be the over-labeling the near-miss examples exist to prevent — see [`02-the-not-catch.md`](02-the-not-catch.md).
- **Nothing was asserted.** The report asks whether the work matches the complaint; it does not say the work is unnecessary, that the shop is padding, or what is causing the rattle.