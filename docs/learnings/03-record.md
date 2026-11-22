# 03 — Record-keeping learnings

What keeping an honest record taught: derived artifacts drift, counts must be re-derivable, a status row is a claim, and a ratio target changes meaning when its denominator moves.

Every entry cites its artifact — a file, a dataset, a count, a command. Nothing here is asserted from memory. The `L` numbers are global across this folder, in append order, and never renumber: other files in the kit cite them by number, so a learning moves between files without losing its id. Learnings are appended, never rewritten.

## Index

| # | Learning | Section |
|---|---|---|
| L8 | A compiled artifact drifts — keep the index, the manifest, and the spine in one breath | Keeping the record honest |
| L12 | A status row is a claim — check it against git, not against memory | Keeping the record honest |
| L13 | A ratio target silently re-defines itself when its denominator moves | Keeping the record honest |
| L23 | A record can be true when written and false an hour later — the falsifier is usually the next commit | Keeping the record honest |
| L24 | The file that defines a format can break it | Keeping the record honest |

## Keeping the record honest

### L8 · A compiled artifact drifts — keep the index, the manifest, and the spine in one breath

**Learning.** (Inherited from ScamCheck C5.) Any derived copy drifts from its source unless regenerated in the same change. Here the derived artifacts are `INDEX.md` (generated from `index.json`) and, in the kit proper, `estimate/SPINE.md` (compiled from the rubric and workflow). During the build, the first index pass and the manifest briefly disagreed on counts (898 vs. the vendored reality) because new fetches had not yet been re-indexed — the same class of defect.

**Evidence.** The index was rebuilt twice; the vendored-count mismatch is visible in the build log ([`../HOW-BUILT.md`](../HOW-BUILT.md) Steps 1 and 6).

**Change.** The rule from ScamCheck is carried into this kit's conventions: a rubric change requires a spine change in the same breath ([`../../CONTRIBUTING.md`](../../CONTRIBUTING.md) §Changing a rubric), and the corpus method ends with a verify step that recounts what is actually on disk.

### L12 · A status row is a claim — check it against git, not against memory

**Learning.** The WBS is a working checklist that people (and agents) trust to decide what is left. Its rows are claims, and they drift in both directions in the same way a compiled file does. In one session the record was wrong twice: WP-1 row 1.7 read "Commit + push the corpus batch — 🔶 awaiting your go" for a commit that `git branch -r --contains` shows sitting on `origin/main` (under-reporting finished work, which invites someone to re-do it); and WP-2 rows 2.3 and 2.4 still read "30/30" and "all 30 written" after the library had become 32 patterns (over-reporting stale work, which makes the row prove nothing). Neither error was caused by bad intent — both were caused by editing one file and not re-reading the row it governed. A status row is a measurement, and a measurement that is never re-taken is a guess wearing a checkmark.

**Evidence.** `git branch -r --contains 748c5c0` → `origin/main`, against [`../WBS.md`](../WBS.md) row 1.7 as written; the 30/30 residue in the same file rows 2.3–2.4 against [`../../estimate/rubrics/patterns-estimate.md`](../../estimate/rubrics/patterns-estimate.md), whose index holds 32 rows. The correction is L10's, applied to status instead of counts.

**Change.** Before flipping a WBS row, the claim is verified against the artifact it describes: `git branch -r --contains <sha>` for anything that says committed or pushed, and a count of the actual file (for this kit, `grep -c "^### " estimate/rubrics/patterns-estimate.md`) for anything that says *n* of *n*. Where a row cannot be verified by a command, it says so instead of carrying a checkmark.

### L13 · A ratio target silently re-defines itself when its denominator moves

**Learning.** The fixture manifest set "at least one near-miss for every two pattern fixtures." Written against six pattern fixtures and a 30-pattern library, that meant three near-misses. The library then grew to 32 patterns and the fixture set grew to cover them, which moved the denominator without touching the ratio text — so the same sentence now demanded more near-misses than existed, and the WBS carried the gap as an open decision instead of a number. A ratio is a promise about proportion; when the thing it is a proportion of changes, the promise changes quietly and no one notices, because the sentence reads the same. Targets that stay honest are counted in the units the work is actually planned in.

**Evidence.** [`../../tests/MANIFEST.md`](../../tests/MANIFEST.md) §Coverage targets ("At least one near-miss for every two pattern fixtures") against its golden list (6 pattern fixtures, 1 near-miss); [`../WBS.md`](../WBS.md) item 4.6, which records the arithmetic (6 pattern ⇒ 3 near-misses, only 07 exists) as an unresolved decision after the library reached 32 patterns.

**Change.** The rule: a near-miss target is written as a count derived from the pattern fixture count in the same file, so the two move together or the discrepancy is visible on the page; and coverage is recorded as an explicit pattern-to-fixture map, so "which pattern still has no fixture" is answered by reading the manifest rather than by trusting the ratio. The correction itself is carried by WP-4 item 4.6, which is open.

### L23 · A record can be true when written and false an hour later — the falsifier is usually the next commit

**Learning.** WP-0 through WP-4 each passed their own acceptance when written. An end-of-session review still found seven statements in checked-in files that had since become false, and none came from carelessness at authoring time: the WP-1 note "two commits are local and **not pushed**" was accurate until the push twenty minutes later; the glossary's "seven sections" was an eyeballed count against a file with eight; WBS 8.5's "L1–L16" was right before L17–L22 existed; the changelog's "8 planned fixtures. No fixture or run exists yet" was true at scaffold time and never revisited when fifteen fixtures and five runs landed; and WBS 6.3 listed "Ollama / LM Studio" because that phrasing was copied from habit rather than read out of `shared/local-models.md`, which also names oMLX. Every one was a true-at-the-time claim. Records do not decay on their own — the next commit decays them, and the next commit is written by the same person who is sure the record is fine.

**Evidence.** `docs/WBS.md` WP-1 open note against the pushed commits; [`../../shared/anatomy.md`](../../shared/anatomy.md) — eight `##` sections against the WBS's "seven"; `docs/WBS.md` 8.5 "L1–L16" against the learnings reaching L24; [`../../CHANGELOG.md`](../../CHANGELOG.md) Unreleased — "8 planned fixtures. No fixture or run exists yet"; WBS 6.3 against [`../../shared/local-models.md`](../../shared/local-models.md).

**Change.** After any change, the kit is searched for statements that describe the changed artifact — counts, section counts, "not yet", "no *X* exists", "Open:", and tool lists — and they are fixed in the same commit. A record review runs at each WP boundary, not only at release.

### L24 · The file that defines a format can break it

**Learning.** `tests/README.md` is the authority for what a fixture contains, how an answer key is shaped, how the reading is counted, and what the six pass rules are. On the same pass it carried the same path table twice — once headed "What a fixture contains", once headed "Structure" — said "The kit has no code to run" while the repository shipped `tests/verify_fixtures.py` and `corpus/verify.py`, and described the key format without the document-level findings section the keys actually carry. A spec file is read as the authority, so its errors are inherited as expectations rather than discovered as bugs. L14 established the one-owner rule and L16 said a rule does not travel to its neighbour; this is the third sighting, and the first inside the document that states the rule.

**Evidence.** [`../../tests/README.md`](../../tests/README.md) — duplicated path tables, the "no code to run" line, and the key-format paragraph; the scripts at [`../../tests/verify_fixtures.py`](../../tests/verify_fixtures.py) and [`../../corpus/verify.py`](../../corpus/verify.py).

**Change.** A spec file is reviewed against the artifacts it describes in the same pass that changes them — the duplication check applies to the spec itself, and a "the kit has no code" style absolute is checked against the repository before it is written.
