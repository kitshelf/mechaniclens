# Tuning log — what the US/Canada corpus teaches the pattern library

Every tuning pass is recorded here: the counts, the calibration findings, the candidate patterns, and the gaps. A pattern enters the rubric only with a source, a *not-a-pattern-when* line, and a fixture that exercises it. Nothing auto-enters.

---

## Pass 1 — 2026-11-21 — first US/Canada sweep

**Corpus:** 13 US/Canada datasets, ~505,000 records. See [`MANIFEST.md`](MANIFEST.md).

### What the corpus supports

| Pattern family | Source datasets | What to look for |
|---|---|---|
| **Fee language** | NHTSA complaints, CPSC recalls, body-shop directory | Diagnostic fee, shop supplies, hazmat, disposal, storage, admin fee, "misc" |
| **Labour language** | OEM maintenance schedules, mechanicdb procedures | Flat-rate vs hourly, "book time", labour operation, "per hour", "minimum 1 hour" |
| **Parts language** | mechanicdb replacement parts, body-shop directory | OEM vs aftermarket vs reman vs salvage, "like-kind", "LKQ", core charge |
| **Scope language** | NHTSA complaints, home-repair Q&A | "while we're in there", "recommended", "courtesy inspection", "related work" |
| **Documentation language** | OEM schedules, mechanicdb, home-repair Q&A | "per manufacturer", "per TSB", "per recall", "not shown", "see attached" |
| **Symptom-vs-scope** | NHTSA complaints (component vs summary), home-repair Q&A | Complaint names one component; the fix touches another |
| **Diagnostic language** | mechanicdb DTCs, CodesList, karsonmadden | DTC code, "diagnostic", "scan", "smoke test", "road test" |
| **Recall/campaign language** | aowens25 NHTSA, yandyman CPSC | "safety recall", "campaign", "remedy", "owner notification" |
| **Home-repair scope** | home-diy Q&A, NextTerritory market size | "inside the house" vs "outside the house", "per square", "per linear foot" |

### Candidate patterns surfaced

1. **F-31 "Shop supplies"** — a percentage line on the estimate. *Not a pattern when:* the estimate itemises the supplies (rags, solvent, gloves) at cost.
2. **L-12 "Book time"** — labour priced from a flat-rate guide, not the technician's actual time. *Not a pattern when:* the shop discloses the flat-rate source and the estimate matches it.
3. **P-09 "Core charge"** — a refundable deposit on a rebuilt part. *Not a pattern when:* the charge is refunded on return and the estimate says so.
4. **S-07 "While we're in there"** — related work added to the same job. *Not a pattern when:* the added work is safety-critical and the estimate says why.
5. **D-06 "Per TSB"** — a repair justified by a technical service bulletin. *Not a pattern when:* the TSB number is quoted and the repair matches it.
6. **R-03 "Safety recall"** — a line that may be covered by a campaign. *Not a pattern when:* the VIN is checked against the recall and the line is the remedy.
7. **H-04 "Per square"** — roofing priced by the square (100 sq ft). *Not a pattern when:* the estimate states the square count and the pitch.
8. **H-05 "Per linear foot"** — gutters, fencing, siding priced by the foot. *Not a pattern when:* the run length is measured and stated.

### Calibration findings

- **NHTSA complaint text is symptom-first.** Owners describe the symptom, not the part. The kit's symptom-vs-scope step is the right frame — the complaint names the noise, the estimate names the part.
- **Recall language is remedy-first.** "Remedy", "campaign", "owner notification" are the tells. The kit should flag "may be covered" without asserting coverage.
- **Body-shop directories list services, not prices.** "Collision repair", "paintless dent repair", "frame straightening" are service categories — useful for the anatomy glossary, not for price calibration.
- **Home-repair Q&A is synthetic and generic.** It teaches scope language ("inside/outside the house") but not US-specific fee structures. Treat it as a scope reference, not a fee reference.
- **OEM maintenance schedules are the strongest US source.** They give the manufacturer's own interval and wording — the calibration anchor for "per manufacturer" lines.

### Gaps

- **No US/Canada repair *estimate* or *invoice* corpus at scale.** The surface has complaints, recalls, codes, schedules, and directories — not the documents themselves. The kit's fixtures must be synthetic.
- **No US/Canada household repair *invoice* corpus.** The home side is thinner than the auto side.
- **No Canada-specific repair documents.** The Canada sets found were collision statistics and aviation occurrences, not repair estimates.

### Patterns that did NOT survive calibration

- **"Diagnostic fee is always a marker"** — dropped. Many US shops charge a diagnostic fee that is credited toward the repair. The marker is the *non-creditable* fee, not the fee itself.
- **"Dealer markup is always a marker"** — dropped. Dealer labour rates are higher by design; the marker is the *undisclosed* markup, not the rate.
- **"Aftermarket part is always a marker"** — dropped. Aftermarket parts are legitimate; the marker is the *undisclosed* substitution, not the part type.

---

## Pass 2 — 2026-11-21 — rubric revisit (citation re-measure)

**Tool:** [`verify.py`](verify.py) — the citation check, added this pass (commit `66ad28b`). Section A re-measures the rubric's published counts; Section B hunts estimate vocabulary across all 54 vendored datasets. Every number below is the tool's output.

**Corpus:** 54 US/Canada datasets, ~1.45M records.

### Grading changes

| Pattern | Change | Evidence (tool output) |
|---|---|---|
| F-3, F-4 | brief → adjacent | `yandyman` recall remedies: 105 hazardous-waste rows, 52 waste-disposal references — the regulated practice each fee names. No fee line exists anywhere in the corpus. |
| L-2 | brief → adjacent | `mechanicdb` `cost_metadata.json`: "hours only, no labor rate" — the data models the exact shape |
| P-4 | brief → adjacent | 80 of 449 `mechanicdb` part rows name a kit ("Automotive wiring repair kit (solder + heat-shrink)") |
| P-7 core charge | entered (adjacent) | `vic35get`: one narrative of 12,534 — "core charges for the old part" on a remanufactured unit |
| D-6 per TSB | entered (adjacent) | `ItsMayur`: 3 narratives name a TSB as the basis for work; `karsonmadden` counts bulletins per code (P0300: 4,070) |
| S-1 | count corrected | 163 of 1,000 symptom rows (five families), not the previously published 176 |
| P-2 | precision fix | 449 rows across 320 procedures, max 3 per procedure — multiple distinct parts are normal; a repeated identical line is the deviation |

### Verified negative checks (patterns that stay brief)

- Administrative/document/filing-fee vocabulary: 0 matches corpus-wide (F-5).
- "While we're in there" and variants: 0 matches (S-5).
- Verbal/oral authorization: 0 matches; the only "verbal" text is recall correspondence (D-5).
- Repair authorization: the only "unauthorized" text is recall hazard language (D-2).
- Add-on/unauthorized billing narratives: none survive the hunt (L-5).
- Injection text: 0 matches (M-1 — awaits fixture 08).
- "Misc": home cost-register materials shorthand only (F-7).
- Quantity fields: absent from all parts data (P-3).
- OEM/aftermarket vocabulary: 0 of 28 discontinued-part records (P-1, P-6).

### Counts after the pass

**32 patterns: 4 direct · 16 adjacent · 12 brief.** Brief list: F-5, F-7, L-3, L-5, P-1, P-3, P-6, S-5, D-2, D-3, D-5, M-1.

### Gaps

- Still no US/Canada estimate/invoice corpus (L2 unchanged) — the 12 brief patterns must earn fixtures (WP-4).
- L-3 (overlapping labor) is ungroundable from current data: per-operation hours exist; shared access between operations is not modeled.
- P-7 and D-6 rest on 1 and 3 narrative rows respectively — honest but thin; fixtures must carry them.
