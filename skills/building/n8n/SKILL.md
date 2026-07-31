---
name: n8n
description: Design, build, import, export, test, or repair n8n workflows, expressions, custom nodes, webhooks, credentials, and API/CLI automation. Use for n8n workflow JSON, n8n 2.x publish/unpublish flows, queue/error/idempotency design, n8n REST API work, or packages importing n8n-workflow.
---

# n8n

Deliver an importable, version-compatible workflow or node with safe credentials, deterministic data contracts, and failure handling.

## Detect the environment

Inspect the n8n version, deployment type (Cloud, npm, Docker, queue mode), available nodes, current workflow JSON/API state, credential names, project conventions, and whether production is in scope. Use installed node descriptions or current official docs for exact `typeVersion`, parameters, and CLI/API behavior.

Read references only as needed:

- [workflow-reference.md](workflow-reference.md) for flow patterns.
- [custom-nodes-reference.md](custom-nodes-reference.md) for package structure.
- [api-reference.md](api-reference.md) for API concepts.

Verify version-sensitive examples. In n8n 2.x, publication uses publish/unpublish semantics; do not rely on old active-toggle instructions.

## Define the contract

Before editing, state:

- trigger/input, expected item schema, and output/side effects;
- credential and permission requirements;
- volume, ordering, rate limits, duplicate policy, and retry behavior;
- partial-failure route, observability, and replay/resume mechanism.

Design for arrays of items. Preserve item linkage when downstream nodes depend on it.

## Build with the smallest reliable nodes

1. Prefer built-in nodes and expressions for clear mappings.
2. Use Code nodes only for logic that is materially clearer there.
3. Extract shared behavior into sub-workflows with explicit input/output contracts.
4. Add batching or Loop Over Items for rate-limited/high-volume APIs.
5. Add stable idempotency keys before external creates, sends, charges, or updates.
6. Configure bounded retries only for transient failures; route permanent errors with useful context.
7. Attach an Error Trigger workflow for operational failures when the deployment supports it.
8. Keep secrets in n8n credentials. Remove headers/tokens copied from cURL and anonymize credential names/IDs before sharing workflow JSON.

For custom nodes, detect the supported Node.js/n8n toolchain, scaffold from the current official starter, implement typed credentials and operations, then build and lint the package.

## Import, test, publish

- Save a sanitized workflow JSON artifact and a small fixture for representative input.
- Import into a non-production project or manual-test context first. Existing IDs can overwrite records; inspect and remove/change IDs when necessary.
- Test happy path, empty input, multiple items, invalid data, pagination, rate limit, timeout, retry, duplicate delivery, and partial failure.
- Confirm executions contain enough context to diagnose failures without logging secrets or sensitive payloads.
- Leave imported workflows unpublished/inactive by default. Publish, activate, replace credentials, or alter a production workflow only when the user explicitly requests it.

When using the self-hosted Server CLI, distinguish it from the remote n8n CLI: the Server CLI has direct database access and can bypass normal API permissions. Prefer scoped API/remote tooling for agent-driven management.

## Completion

Return workflow/node paths or IDs, detected n8n version, credentials still requiring manual connection, test evidence, publication state, and exact resume/replay instructions. Never claim a JSON file was imported or executed unless verified.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for an importable, version-compatible, observable workflow or node with safe credentials and failure handling.
- Use medium freedom for architecture; use low freedom for node schemas, type versions, credentials, idempotency, and platform limits.
- Require verified n8n schemas, explicit error/retry/rate-limit/idempotency paths, and a successful import or API dry-run. Revise once when weak.
- Learn only from versioned import failures, fixtures, and observed execution defects.
<!-- skill-evolver:adaptive-end -->
