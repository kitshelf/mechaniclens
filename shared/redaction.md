# The redaction pass

Run this before the decode. A repair estimate carries the customer's name, address, phone number, VIN, plate, and sometimes an insurance policy or claim number. None of that is needed to read the lines.

## What to strip

| Strip | Replace with |
|---|---|
| Your name | `[NAME]` |
| Your address | `[ADDRESS]` |
| Your phone number | `[PHONE]` |
| Your email | `[EMAIL]` |
| VIN | `[VIN]` |
| License plate | `[PLATE]` |
| Insurance policy or claim number | `[POLICY]` |
| Payment card or bank digits | `[ACCOUNT]` |

## What to keep

Keep the document's substance:

- the shop's name and location, if shown
- every line item, quantity, and amount
- labor hours and the labor rate, if shown
- fees, supplies, taxes, and the total
- the symptom story you type alongside the estimate
- the date and any "verified as of" or estimate-validity date

The shop's name is the counterparty, not your personal data. Keep it so the question script can refer to the document.

## How to run it

1. Copy the estimate text into a plain document.
2. Replace the identifiers in the table above.
3. Paste the redacted text into the chat.
4. If the kit sees an identifier you missed, it will ask for a redacted paste. Do not paste the same document twice without redacting.

## If the document is a photo

The kit reads text. Type or transcribe the lines. Do not upload the photo unless the chat's privacy terms are acceptable to you; the kit itself never opens or transmits an image.
