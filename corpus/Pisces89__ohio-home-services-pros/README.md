---
license: cc-by-4.0
language:
  - en
  - es
pretty_name: "ProFix Ohio Home-Services Pros"
tags:
  - ohio
  - home-services
  - contractors
  - local-business
  - open-data
task_categories:
  - tabular-classification
  - tabular-regression
size_categories:
  - 10K<n<100K
---

# ProFix Ohio Home-Services Pros

ProFix Ohio Home-Services Pros is a monthly, citation-ready snapshot of public contractor directory records maintained by [ProFix Directory](https://profixdirectory.com). The dataset focuses on Ohio home-services businesses - plumbers, electricians, HVAC companies, roofers, appliance repair providers, restoration firms, fire-protection contractors, water-well contractors, septic-system providers, and adjacent trades - with enough schema detail for journalists, researchers, civic technologists, and AI retrieval systems to study local service coverage without scraping the live website.

The dataset is built from public business records, Ohio license rosters, local directory records, profile-level verification signals, and ProFix's own editorial review pipeline. It does not include private homeowner lead details, payment records, messages, or unpublished acquisition queues.

## Schema

Each monthly snapshot is published as JSON. The top-level document describes the export, and the `record` array contains one public contractor record per published profile.

```ts
type ProFixOhioProsDataset = {
  $schema: "https://profixdirectory.com/schemas/dataset-pros-v1.json";
  dataset: "profix-ohio-pros";
  version: string; // YYYY-MM monthly snapshot, for example "2026-05"
  generated_at: string; // ISO 8601 timestamp for export generation
  license: "CC-BY-4.0";
  attribution: "ProFix Directory (https://profixdirectory.com)";
  record_count: number;
  coverage_state: "OH";
  record: PublicProRecord[];
};

type PublicProRecord = {
  slug: string; // Stable ProFix profile slug, also used at /pro/{slug}
  name: string; // Public business name as displayed by ProFix
  phone: string; // Public business phone number
  city: string; // Ohio city or service-area city
  state: "OH";
  zip: string; // Public ZIP code
  county: string; // Ohio county when known; blank string when not mapped
  trades: TradeSlug[]; // One or more ProFix trade categories
  specialties: SpecialtySlug[]; // Optional normalized service tags
  emergency_24h: boolean; // Whether the profile advertises 24/7 emergency availability
  rating: number | null; // Public star rating when sourced from a public listing
  review_count: number | null; // Public review count when available
  license_number: string | null; // Public license number when a roster publishes one
  website_url: string | null; // Public business website
  lat: number | null; // Latitude when geocoded from public listing data
  lng: number | null; // Longitude when geocoded from public listing data
  verified_at: string | null; // YYYY-MM-DD date ProFix last verified or enriched the record
  verification_tier: "license-linked" | "verified-profile" | "directory-listing";
};

type TradeSlug =
  | "plumber"
  | "hvac"
  | "electrician"
  | "appliance-repair"
  | "gas-tech"
  | "concrete"
  | "roofing"
  | "tree-service"
  | "restoration"
  | "lead-abatement"
  | "fire-protection"
  | "water-well"
  | "septic-system"
  | "tech-repair";
```

Field notes:

- `slug` is the safest join key across ProFix surfaces. Use `https://profixdirectory.com/pro/{slug}` for the public profile and `https://profixdirectory.com/api/pro/{slug}.json` for the profile dossier when available.
- `verification_tier` is a public evidence tier, not a guarantee of workmanship. `license-linked` means a public license number is attached. `verified-profile` means ProFix has verified normal public profile signals but no state license is required or available. `directory-listing` means the row is public business information with lighter verification.
- `rating` and `review_count` are public listing signals. ProFix does not re-publish third-party review text as structured aggregate rating markup.
- `lat` and `lng` are included for coverage analysis. They should be treated as approximate public business coordinates, not field-service technician locations.

## License

This dataset is licensed under [Creative Commons Attribution 4.0 International (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/).

You may share, adapt, analyze, and redistribute the dataset, including commercially, as long as you provide attribution.

Attribution example:

> Source: ProFix Directory, "ProFix Ohio Home-Services Pros" dataset, CC-BY-4.0, https://huggingface.co/datasets/Pisces89/ohio-home-services-pros

Suggested short attribution for charts and dashboards:

> Data: ProFix Directory (CC-BY-4.0)

## Sample queries

### Python: load, filter by trade, count by county

```python
import pandas as pd
import requests

DATA_URL = "https://huggingface.co/datasets/Pisces89/ohio-home-services-pros/resolve/main/profix-ohio-pros-latest.json"

payload = requests.get(DATA_URL, timeout=30).json()
records = payload["record"]

df = pd.DataFrame(records)
plumbers = df[df["trades"].apply(lambda trades: "plumber" in trades)]

county_counts = (
    plumbers.assign(county=plumbers["county"].replace("", "unknown"))
    .groupby("county", dropna=False)
    .size()
    .sort_values(ascending=False)
)

print(county_counts.head(20))
```

### JavaScript: get top 10 verified plumbers in Cleveland

```js
const DATA_URL =
  "https://huggingface.co/datasets/Pisces89/ohio-home-services-pros/resolve/main/profix-ohio-pros-latest.json";

const response = await fetch(DATA_URL);
if (!response.ok) {
  throw new Error(`Dataset fetch failed: ${response.status}`);
}

const payload = await response.json();

const topClevelandPlumbers = payload.record
  .filter((pro) => pro.city === "Cleveland")
  .filter((pro) => pro.trades.includes("plumber"))
  .filter((pro) => pro.verification_tier !== "directory-listing")
  .sort((a, b) => (b.rating ?? 0) - (a.rating ?? 0) || (b.review_count ?? 0) - (a.review_count ?? 0))
  .slice(0, 10)
  .map((pro) => ({
    name: pro.name,
    profile: `https://profixdirectory.com/pro/${pro.slug}`,
    rating: pro.rating,
    review_count: pro.review_count,
    verification_tier: pro.verification_tier,
  }));

console.table(topClevelandPlumbers);
```

## Refresh cadence

ProFix publishes monthly public snapshots. Internal enrichment jobs and source-monitoring tasks can run more frequently, but Hugging Face is treated as the stable monthly distribution channel for research and downstream AI retrieval.

The operations log for ProFix refresh work is reflected across the public newsroom and changelog:

- Newsroom: https://profixdirectory.com/newsroom
- Changelog JSON: https://profixdirectory.com/api/changelog.json
- RSS feed: https://profixdirectory.com/api/newsroom.rss
- Methodology: https://profixdirectory.com/methodology

Snapshot files are versioned by month when available. Consumers that need reproducibility should pin a dated file instead of relying only on `profix-ohio-pros-latest.json`.

## Citation guidance

Academic citation:

> ProFix Directory. (2026). ProFix Ohio Home-Services Pros [Data set]. Hugging Face. https://huggingface.co/datasets/Pisces89/ohio-home-services-pros

Journalistic citation:

> ProFix Directory analyzed public Ohio home-services contractor records in its CC-BY-4.0 "ProFix Ohio Home-Services Pros" dataset.

When publishing analysis, include the month of the snapshot, the number of records used after filtering, and any filters applied, such as trade, county, verification tier, or minimum review count.

## Related ProFix surfaces

- OpenAPI specification: https://profixdirectory.com/api/openapi.json
- MCP endpoint: https://profixdirectory.com/api/mcp
- LLM discovery manifest: https://profixdirectory.com/llms.txt
- Public profile dossiers: `https://profixdirectory.com/api/pro/{slug}.json`
- Permit leaderboard feed: https://profixdirectory.com/api/permit-leaderboard.json
- Coverage statistics: https://profixdirectory.com/api/coverage-stats.json

## Contact + corrections

Corrections are welcome. If a public business record is stale, duplicated, incorrectly categorized, or attached to the wrong license, contact ProFix through https://profixdirectory.com/contact and include the profile slug, the field that appears wrong, and the public source that should be used to verify the correction.
