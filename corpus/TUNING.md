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
