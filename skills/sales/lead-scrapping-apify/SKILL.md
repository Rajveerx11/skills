---
name: lead-scrapping-apify
description: Build a compliant local lead-discovery pipeline using an authorized Apify Actor, commonly for public Google Maps business data. Use when the user asks to find businesses by service/location, run or resume an Apify prospecting job, export/deduplicate/score a business lead list, identify evidence-based digital-presence gaps, or draft unsent B2B outreach.
---

# Lead Scraping with Apify

Produce a deduplicated, source-backed business prospect list plus transparent scoring. Do not claim every business “needs AI,” assume a cloud plugin, or send outreach automatically.

## Scope the run

Derive:

- offered service and ideal customer profile;
- business categories and exact locations;
- desired count, required fields, exclusion/suppression list;
- jurisdiction, allowed contact channels, output format;
- Apify budget ceiling and outreach status.

Default outreach to drafts only. Ask before a paid run when price or maximum charge cannot be bounded from the Actor's current pricing and run controls.

## Select and verify an Actor

1. Confirm `APIFY_TOKEN` exists without printing it.
2. Find a maintained Actor in the Apify Store that supports the requested public source and geography.
3. Inspect the Actor's current input schema, pricing, limits, terms, last update, and sample output.
4. Record Actor ID/version, selected fields, maximum items/charge, and expected cost.
5. Run a small preview first and inspect quality before scaling.

Never invent Actor input keys. Prefer the official Apify client/CLI or API. Send tokens in the `Authorization` header, not query strings or logs.

## Run and resume

Start asynchronously for non-trivial jobs. Save the run ID immediately. Poll the canonical run endpoint until a terminal state:

```text
POST /v2/actors/{actorId}/runs
GET  /v2/actor-runs/{runId}
GET  /v2/datasets/{defaultDatasetId}/items
```

Persist Actor ID, input hash, run ID, dataset ID, status, started/finished time, item count, and finalized cost. On interruption, resume from run/dataset ID instead of starting a duplicate. Retry only transient platform failures.

Export JSON as the raw evidence source. Apify dataset exports may also return CSV/XLSX. Never treat a timed-out synchronous request as proof that the Actor failed; inspect the run.

## Normalize and qualify

Use the bundled normalizer:

```powershell
python "<skill-directory>\scripts\normalize_places.py" raw-dataset.json --output qualified-leads.csv
```

It maps common place fields, deduplicates by place ID/domain/phone/name+address, and scores only observable signals. Review unknown schemas and low-evidence rows before use.

Qualification must cite evidence:

- missing business website from the source;
- public rating/review-count opportunity;
- relevant category/location;
- verified contactability and source URL.

Do not infer budget, revenue, decision-maker identity, or automation need without evidence. Enrich promising rows separately with `$enrich-lead`.

## Outreach

Create short drafts grounded in a verified observation and the offered outcome. Keep email and WhatsApp/phone columns separate, include opt-out language where required, and honor suppression lists. Follow platform terms and applicable anti-spam/privacy law.

Do not send messages, upload contacts, create campaigns, or contact personal numbers without explicit authorization. For regulated or sensitive sectors, keep outreach about the business service and avoid personal/sensitive attributes.

## Quality gate

Report Actor/version, run and dataset IDs, actual cost, raw and normalized paths, raw/unique/duplicate counts, field coverage, score rubric, exclusions, compliance assumptions, and unsent outreach status. Spot-check a sample against source URLs before handoff.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for a compliant, deduplicated, scored lead list with evidence-based personalization and usable outreach drafts.
- Use medium freedom for segment discovery/messaging and low freedom for platform terms, privacy, anti-spam law, rate limits, facts, and sending authority.
- Require explicit targeting/jurisdiction, sourced deduped records, and truthful personalized drafts that remain unsent unless authorized. Revise once when weak.
- Learn only from verified field corrections, response outcomes, segment fit, and source-quality evidence.
<!-- skill-evolver:adaptive-end -->
