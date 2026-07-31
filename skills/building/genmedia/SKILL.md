---
name: genmedia
description: Use the genmedia CLI to discover, inspect, price, run, queue, download, and manage fal.ai media endpoints. Trigger for genmedia or fal CLI requests, model search, endpoint schema inspection, image/video/audio/3D generation through fal.ai, async request tracking, fal uploads, or importing downloaded results into a compatible local media app.
---

# genmedia CLI

Produce an inspected media artifact plus a reproducible receipt. Use the CLI rather than hand-written fal HTTP calls.

Read [full-reference.md](references/full-reference.md) when a command or flag is uncertain. Trust `genmedia --help`, the installed CLI version, and live endpoint schema over remembered examples.

## Preflight

1. Locate `genmedia`, record `genmedia version`, and inspect the requested output directory.
2. Confirm credentials exist without printing them. Keep keys in `genmedia setup`, `FAL_KEY`, or a private environment file.
3. Derive media type, purpose, aspect/duration, quality bar, budget/latency preference, source assets, privacy sensitivity, and destination from the request.
4. Ask only when cost, rights, a private upload, or the intended edit target cannot be inferred safely.

Do not run a paid endpoint before its price and schema are known.
If the CLI is absent, inspect the current official installer and obtain approval before executing downloaded installation code; record the installed version afterward.

## Discover and select

- Search with `genmedia models "<capability>" --json`.
- Verify candidate endpoint IDs; never invent one.
- Inspect each candidate with `genmedia schema <endpoint_id> --json` and `genmedia pricing <endpoint_id>`.
- Select by task fit, modality, input limits, quality, latency, price, license, and privacy—not popularity alone.
- For a consequential choice, compare up to three candidates and state the selected tradeoff.

## Execute reproducibly

- Create an output folder outside the skill directory.
- Save structured command output as a JSON receipt and media with `--download`.
- Upload source files with `genmedia upload`; do not substitute `curl`.
- Use async submission for long jobs. Persist endpoint ID and request ID immediately so polling can resume after interruption.
- For batches, use stable item names, bounded concurrency, and a manifest containing prompt/input, endpoint, parameters, request ID, output path, cost evidence, and status.
- Retry only transient failures. Fix schema or policy errors instead of resubmitting unchanged.

Example pattern:

```bash
genmedia models "product image background removal" --json
genmedia schema <endpoint_id> --json
genmedia pricing <endpoint_id>
genmedia run <endpoint_id> --<schema_field> "<value>" --download "./outputs/{request_id}_{index}.{ext}" --json
```

Use `genmedia status <endpoint_id> <request_id> --json` to resume. Add `--result` or `--download` only as supported by the installed CLI.

## Inspect and integrate

Open every generated image or representative frames/audio from every batch. Check prompt fidelity, artifacts, identity/content preservation for edits, duration/dimensions, and file integrity. Revise prompt or parameters once when the result misses the brief.

Use `scripts/import-to-mini-app.mjs` only when a compatible local app already exists and its directory/API are known. Treat import as a transaction: validate inputs, import, verify returned IDs and visible assets, then report. Never write placeholder app paths.

## Boundaries

- Do not upload private or biometric material without user authorization.
- Do not claim commercial rights; report the model/provider terms available at run time.
- Do not install or update the CLI, spend beyond the understood call cost, cancel another run, or delete remote/local assets unless authorized.
- Redact keys, signed URLs, and sensitive source data from receipts and logs.

Return selected endpoint and rationale, exact output paths, request IDs, cost evidence, inspection result, and any queued work still running.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for the best-fit media artifact downloaded, inspected, and integrated with cost and license understood.
- Use high freedom for prompts and variants; use low freedom for schemas, pricing, licensing, privacy, downloads, and destructive imports.
- Require fit across quality/latency/cost/rights, direct artifact inspection, and a transactional verified handoff. Revise once when weak.
- Learn only from explicit user ratings, model receipts, and successful parameter ranges.
<!-- skill-evolver:adaptive-end -->
