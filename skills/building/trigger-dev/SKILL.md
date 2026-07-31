---
name: trigger-dev
description: Build, test, deploy, or debug durable Trigger.dev background tasks and scheduled workflows in TypeScript. Use for @trigger.dev/sdk or @trigger.dev/build code, queued/long-running jobs, cron tasks, retries, idempotency, concurrency, waits, realtime, Trigger.dev configuration, run inspection, or Trigger.dev deployment.
---

# Trigger.dev

Deliver a typed, durable task that behaves correctly across retries, duplicate triggers, long waits, and deployment boundaries.

## Detect and verify

1. Read repository instructions, package manager, lockfile, installed Trigger.dev packages, `trigger.config.*`, configured task directories, environment conventions, and existing task IDs/queues.
2. Use installed package types and current official Trigger.dev documentation for the detected version. Do not mix `latest` examples into a pinned project.
3. Read [core-reference.md](core-reference.md), [config-reference.md](config-reference.md), or [advanced-reference.md](advanced-reference.md) only for the feature in scope; verify version-sensitive APIs before use.
4. Search the codebase for task IDs, trigger call sites, idempotency keys, schedules, and consumers before adding anything.

## Define durability

State the task contract:

- validated JSON-serializable payload and output;
- caller and authorization boundary;
- expected volume, latency, machine needs, queue/concurrency policy;
- retryable versus permanent failures;
- idempotency scope and duplicate result;
- timeout, cancellation, wait/checkpoint behavior;
- logs, metadata, tags, alerting, and recovery path.

Use schema validation at task boundaries. Never put secrets or sensitive payloads into metadata, tags, or logs.

## Implement

- Use a stable unique task ID and export discoverable tasks.
- Reuse existing queues and conventions when they match.
- Add bounded retries with backoff for transient dependencies. Fail permanent validation/business errors without retry.
- Create idempotency keys from stable business identifiers before sends, charges, creates, or child triggers. Verify scope semantics against the installed SDK.
- Use Trigger.dev waits/checkpoints instead of process sleeps for durable delays.
- Pass tenant/user context explicitly and enforce it again inside consequential tasks.
- Design fan-out with bounded concurrency and partial-failure collection.
- Emit structured logs and enough metadata to locate the business object without exposing secrets.

## Test locally

Run format, lint, typecheck, and project tests. In Trigger.dev development mode or an isolated environment, test:

- valid and invalid payloads;
- success, retryable failure, permanent failure, cancellation, and timeout;
- duplicate trigger/idempotency behavior;
- concurrency saturation and child-task failure when relevant;
- schedule/timezone edge cases;
- resumed waits and output serialization.

Record task ID and run IDs. Inspect logs and final status rather than assuming a trigger succeeded.

## Deploy boundary

Do not deploy, create a schedule, trigger a production task, cancel runs, or alter environment variables unless requested. When deployment is authorized:

1. use the project's pinned CLI/tooling;
2. deploy the smallest environment;
3. verify the deployed task/version;
4. trigger a safe smoke run;
5. inspect status, output, logs, and retry count;
6. report rollback or disable steps.

Return changed paths, detected versions, task IDs, durability choices, test/run evidence, and any external configuration still required.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for a version-compatible, typed, durable task with safe retries, idempotency, observability, and verified execution.
- Use medium freedom for workflow design; use low freedom for detected SDK APIs, secrets, deployment, concurrency, retries, and public triggers.
- Require current schemas, passing compile/local/failure/retry paths, and explicit verified deployment authority. Revise once when weak.
- Learn only from versioned run failures and corrected project fixtures.
<!-- skill-evolver:adaptive-end -->
