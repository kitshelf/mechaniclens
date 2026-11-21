# 04 — Fixture learnings

What building the synthetic gauntlet taught: how an answer key is derived, what the label table cannot carry, and why a behavior fixture is not a document fixture with the labels removed.

Every entry cites its artifact — a file, a count, a command. Nothing here is asserted from memory. The `L` numbers are global across this folder, in append order, and never renumber: other files in the kit cite them by number, so a learning moves between files without losing its id. Learnings are appended, never rewritten.

## Index

| # | Learning | Section |
|---|---|---|
| L17 | An answer key's reading is derived, not authored | Building the fixture gauntlet |
| L18 | A line-label table cannot carry the document-level patterns | Building the fixture gauntlet |
| L19 | A behavior fixture is not a document fixture with the labels taken out | Building the fixture gauntlet |

## Building the fixture gauntlet

### L17 · An answer key's reading is derived, not authored

**Learning.** In an answer key the reading is not a judgment — it is the sum of the labels written in the table directly above it. Typing it from the intent ("this should be about half Standard") produces a second, independent number, and the two disagree in ways no reader notices because both look equally authoritative. On the first pass six of fifteen keys disagreed with themselves: fixtures 02, 04, 05, and 10 each undercounted Standard by one; fixture 07 declared six line items for a five-line document; fixture 08's reading summed to four against five labeled rows. Every one was found by a command, none by re-reading.

**Evidence.** [`../../tests/fixtures/02-folded-diagnostic/expected.md`](../../tests/fixtures/02-folded-diagnostic/expected.md), `04`, `05`, `10` — reading corrected upward after the table was recounted; `07` — the sixth row was a validity/authorization finding sitting in a line-label table where it had no number in the document; `08` — the reading omitted a Standard row. The check is [`../../tests/verify_fixtures.py`](../../tests/verify_fixtures.py), which recomputes the count from the numbered lines and the labeled rows and fails on any mismatch.

**Change.** The count is computed from the table, and a script enforces it. `tests/README.md` states the counting rule so the derivation is unambiguous: numbered line items only — parts, labor, fees, tax, and the total when the total itself is labeled; headers, footers, and signature fields are not counted.

### L18 · A line-label table cannot carry the document-level patterns

**Learning.** The rubric holds two kinds of pattern and only one of them fits a row. A line pattern says "this line is unclear" and attaches to a line. A document-level pattern says "this document has no validity date" or "no authorization field" or "the total does not add up" — and there is no line to attach it to. A key built purely as line → label therefore **silently drops D-1 and D-2**, and a run that misses them still passes every rule, because nothing in the key asks about them. Writing fixture 11 is what forced the gap into view: its D-1 and D-2 findings had nowhere to go. Fixture 07 needed the mirror case — an explicit declaration that validity and authorization *are* present, so their absence is not inferred.

**Evidence.** [`../../tests/fixtures/11-documentation-holes/expected.md`](../../tests/fixtures/11-documentation-holes/expected.md) §Required findings (document level) — D-1 no validity date, D-2 no authorization line; [`../../tests/fixtures/07-clean-estimate/expected.md`](../../tests/fixtures/07-clean-estimate/expected.md) §Required findings — validity and authorization present, D-1 and D-2 do not fire. WBS item 4.1 originally described a key as "required labels, forbidden labels, the reading count" — no slot existed for a document-level finding.

**Change.** Every key now carries four sections: the reading, the required label per line, **the required findings at document level**, and the forbidden set, followed by the pass rules. `tests/README.md` documents the format, so a key that omits the findings section is visibly incomplete rather than quietly smaller.

### L19 · A behavior fixture is not a document fixture with the labels taken out

**Learning.** The six pass rules were written for documents that produce a reading: expected label present, forbidden label absent, count matches, no price invented, no accusation, type guard holds. A behavior fixture breaks that shape. The redaction fixture produces **no reading at all** — so "the reading count matches" has nothing to match, and a run that outputs nothing whatsoever could be scored as passing. The out-of-scope fixture produces a reading only if the user asks for one, after refusing three questions the charter bans. Neither can be judged by a label table; both need required behavior stated as ordered steps, plus an explicit statement of what "no reading" means.

**Evidence.** [`../../tests/fixtures/09-redaction-enforcement/expected.md`](../../tests/fixtures/09-redaction-enforcement/expected.md) — "No reading is produced" and five required steps, with "a count appearing is a failure"; [`../../tests/fixtures/10-out-of-scope-refusal/expected.md`](../../tests/fixtures/10-out-of-scope-refusal/expected.md) — three refusals stated as required behavior, reading conditional on a decode request. Both against the six pass rules in [`../../tests/README.md`](../../tests/README.md), which assume a labeled document.

**Change.** The pass rules are read as per-type, and `tests/README.md` names the four fixture types with what each one's key must answer. A behavior key states required steps and says plainly whether a reading exists; "no output" is never a pass.