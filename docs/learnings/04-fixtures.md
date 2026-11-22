# 04 — Fixture learnings

What building the synthetic gauntlet taught: how an answer key is derived, what the label table cannot carry, and why a behavior fixture is not a document fixture with the labels removed.

Every entry cites its artifact — a file, a count, a command. Nothing here is asserted from memory. The `L` numbers are global across this folder, in append order, and never renumber: other files in the kit cite them by number, so a learning moves between files without losing its id. Learnings are appended, never rewritten.

## Index

| # | Learning | Section |
|---|---|---|
| L17 | An answer key's reading is derived, not authored | Building the fixture gauntlet |
| L18 | A line-label table cannot carry the document-level patterns | Building the fixture gauntlet |
| L19 | A behavior fixture is not a document fixture with the labels taken out | Building the fixture gauntlet |
| L20 | A green consistency check says the fixture agrees with its key, not that the key is right | Building the fixture gauntlet |
| L21 | A fixture plants every pattern its wording supports, not only the one intended | Building the fixture gauntlet |
| L22 | A run by the key's author is a satisfiability check, not a validation | Recording the runs |

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

### L20 · A green consistency check says the fixture agrees with its key, not that the key is right

**Learning.** `tests/verify_fixtures.py` went green while three fixtures were still wrong. It checks that the count equals the numbered lines, that the key labels exactly those lines, and that the arithmetic holds — all statements about a fixture agreeing with its own key. None of them can tell whether the key is *right*, because the key is the only source of truth the checker has. Three defects survived a clean run: fixture 12 carried two lines naming the same part while the key forbade the label its wording earned; fixture 13 bundled a "required" service line above the items it contained; fixture 02 offered two overlapping diagnostic charges and asked for **Check** on both. Each would have failed a correct decode. Consistency is automatable; correctness needs the document read the way a decoder reads it — pattern by pattern, on the wording.

**Evidence.** [`../../tests/verify_fixtures.py`](../../tests/verify_fixtures.py) output "all 15 fixtures consistent" against the three fixtures as then written; the corrections are in commit `386bcfd` — `12` line 2/3 renamed to idler kit and tensioner, `13` restructured to eight independent lines, `02` line 2 changed from harness verification to a road test so it no longer overlaps the diagnostic fee.

**Change.** The checker keeps its job (counts, labeled lines, arithmetic) and the audit is added beside it: read every document against the rubric and ask what a decoder would actually label, then compare with the key. A green checker is the floor, never the sign-off.

### L21 · A fixture plants every pattern its wording supports, not only the one intended

**Learning.** A fixture is designed around one target pattern, but a decoder applies the whole library to whatever is on the page. Wording written for one pattern routinely satisfies another: in fixture 12 the second "timing belt" line was written to plant **P-3** (quantity) and simultaneously planted **P-2** (duplicate parts), so the key forbade **Question this** on a line where it was the correct label. In fixture 13 a "30,000-mile service — required" line was written for **S-2** and, sitting above the oil and filter items it contained, planted **S-3** (deferred maintenance bundled) on both. The key then failed any run that read the document correctly — a fixture that punishes accuracy teaches the model to be wrong.

**Evidence.** [`../../tests/fixtures/12-labor-and-parts-opacity/message.txt`](../../tests/fixtures/12-labor-and-parts-opacity/message.txt) — line 3 was "Timing belt, qty 2" under line 1 "Timing belt, #TB-9912"; [`../../tests/fixtures/13-maintenance-and-advice/message.txt`](../../tests/fixtures/13-maintenance-and-advice/message.txt) — line 1 was "30,000-mile service — required" above separate oil and cabin-filter lines. Both corrected in `386bcfd`.

**Change.** Before a key is written, every line is walked against the rubric to list **all** the patterns its wording supports. Each is then either intended and keyed, or the wording is changed until it is not supported — a forbidden label is only legitimate when the document's own words do not earn it.

## Recording the runs

### L22 · A run by the key's author is a satisfiability check, not a validation

**Learning.** The first WP-6 runs were recorded by the same agent that wrote the fixtures and the keys. All five passed — and that result is worth almost nothing, because it was almost guaranteed. The author knows which label each line was written to earn, so the run shows the key is legible and the fixture decodable as designed: a satisfiability check. What it cannot show is whether the key is *right*, because a shared blind spot sits on both sides of the comparison — the same misreading that wrote the key grades the run. A tester who wrote the question sheet can catch a broken question; they cannot catch a wrong answer key that matches their own misreading. Validation needs a reader that did not write the kit: another model in a fresh session, or a local model, run against the key as written.

**Evidence.** [`../../tests/results/`](../../tests/results/) — `2026-11-22-hosted.md` for fixtures 01–05, every one carrying the line "Run by the same agent that authored this key (WP-4)"; all five PASS. [`../WBS.md`](../WBS.md) items 6.2 and 6.3 still open; [`../../tests/README.md`](../../tests/README.md) state line counts 5 of 15 hosted author runs.

**Change.** Every run record states who ran it and whether the runner wrote the key. WP-6 stays open until each fixture has a hosted run and a local-model run, and at least one run comes from a model that did not author the kit. The `tests/README.md` state line counts runs by type instead of flipping to "tested" on author passes.