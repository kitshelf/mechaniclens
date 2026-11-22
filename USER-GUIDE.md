# User guide

MechanicLens reads a repair estimate back to you before you approve the work. It explains each line in plain English, labels the lines **Standard / Check / Question this**, and gives you a short question script for the counter. It never tells you what the job should cost.

## The ninety-second walkthrough

1. **Open any AI chat.** A hosted chat or a local model both work. A local model keeps the whole run on your machine.
2. **Paste the kit.** Use [`estimate/SPINE.md`](estimate/SPINE.md) — the whole kit in one file.
3. **Redact first.** Remove your name, address, phone, VIN or plate, and any policy numbers. Keep the line items, the amounts, and the symptom story, because those are what the decode needs.
4. **Paste the estimate and the symptom.** Type or paste the estimate's lines, then one or two sentences about what the car is doing.
5. **Read the report.** You get the anatomy, a label per line, the question script, and a decision checklist.

## What the labels mean

| Label | What it means for you |
|---|---|
| **Standard** | The line is a normal part of an estimate and the wording is clear. It is not a price judgment. |
| **Check** | The line is common but worth confirming: the amount, the scope, or the assumption is not visible. |
| **Question this** | The wording or placement is worth a specific question before you approve. |

The report counts lines, not risk: **Reading: Standard N · Check N · Question this N**. It never gives a score or a percentage.

## The questions are for understanding, not haggling

Each question in the script is polite and specific. A good answer tells you something you can verify against the paper in your hand. For example:

- "Is the diagnostic fee credited toward the repair if I approve it?"
- "Is this labor billed at book time or actual time?"
- "What does 'shop supplies' cover on this job?"
- "Is this the same part as the one on the line above?"

If the answer does not match the paper, ask again or get a second opinion. The kit does not negotiate for you.

## What it will not do

- It will not quote, estimate, or compare prices. Your region, parts tier, and labor rate are unknowable from the document.
- It will not diagnose the car or recommend a repair.
- It will not say a shop is cheating. "Question this" is the ceiling.
- It will not click links, call the shop, or approve anything.
- It will not replace your judgment. The decision is yours.

## If the final invoice differs from the estimate

Keep the estimate you signed, the final invoice, and any texts or emails about the work. Compare them line by line: what was authorized, what was added, what was billed. The kit's after-repair branch walks through the comparison and names the channels to contact if the numbers do not match. It does not give legal advice and does not file anything for you.

## Privacy

The kit runs offline. It never fetches, clicks, opens, or transmits anything. Your document stays in the chat you chose. If you use a hosted model, the provider's terms apply; a local model avoids that entirely. See [`shared/local-models.md`](shared/local-models.md) for the honest note on small-model limits.

### Redact before you paste

The kit will not decode a document that carries personal data. It stops, names the **types** of identifier it saw, and asks you to paste again with them removed. It never repeats a value back to you.

**Before** — the kit refuses this:

```
Customer: Marisol Delgado-Ruiz
Address: 4412 Kestrel Lane, Austin, TX
Phone: 555-0134
VIN: 1SYNTHETICVIN0001
Plate: FIXTURE-1

Wren & Sons Auto
 1  Rear brake pads ............ 96.00
 2  Labor, 1.2 hr @ 140.00/hr .. 168.00
```

**After** — the kit decodes this:

```
Wren & Sons Auto
 1  Rear brake pads ............ 96.00
 2  Labor, 1.2 hr @ 140.00/hr .. 168.00
 3  Shop supplies .............. 10.00
 4  Sales tax 7.25% ............ 19.87
    TOTAL ..................... 293.87
```

What to remove: your name, street address, phone, email, account or card digits, VIN, and plate. What to keep: the shop name, every line item with its amount, the hours and rate, the fees, and the total. The shop name and the numbers are what the decode reads; the identifiers are not.

If you paste the unredacted version anyway, the kit will refuse and ask again. That is the kit working as designed — the refusal is the privacy promise, not an error.

## Related

- [The charter](WHAT-THIS-IS.md) — what the kit is and is not
- [The workflow](estimate/README.md) — how the decode runs
- [The labels](shared/labels.md) — the full label definitions
- [The line vocabulary](shared/anatomy.md) — every term the report uses for a line, defined once
