# MechanicLens v0.1.0 — Product Conclusion

## What it is

MechanicLens reads a car-repair estimate back to the person holding it. It labels each line Standard, Check, or Question this, hands over a question script, and stops. It does not price, diagnose, accuse, or decide. The user decides.

## Can it ship?

**Yes. Ship v0.1.0 as beta.**

The five structural rules that make it the kit — not a chatbot that recommends — all hold on two independent hosted models:

- The redaction gate holds. Identifiers are refused, not decoded.
- Approve/Decline is gone. The kit does not recommend.
- Scope findings reach the labels. A mismatch named in prose is labeled on the lines.
- Clean estimates come back clean. No invented findings on all-Standard documents.
- The after-repair branch works. Estimate-versus-invoice comparison produces labels on both documents.

## What is rough

- Label accuracy is 79–80%. The misses are on the harder patterns (fee-stack, opacity, maintenance framing). The kit's instructions are in; the models under-apply them on the hardest fixtures.
- Two small calibration gaps: P-1 over-fires on the after-repair branch, and "required" vs "recommended" is missed on maintenance. Fixable in SPINE, not structural.
- Luna's summary line sometimes disagrees with its label table. Model issue, not kit issue.

## Ship recommendation

**Ship v0.1.0 as beta.** The architecture is right. A user with a real estimate gets a correct map of the paper, the right questions to ask, and a stop sign on the one line that matters most. The gaps are calibration and can ship in a beta with a testing note.

## Cost to the user

Less than $0.01 per decode on Haiku or Luna. Local did not work; hosted at a cent a decode is the product.
