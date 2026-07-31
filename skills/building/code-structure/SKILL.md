---
name: code-structure
description: Diagnose and refactor duplicated operational logic into appropriate shared services without changing behavior. Use when workflows repeat provider, filesystem, process, networking, or infrastructure mechanics; when deciding what belongs in actions/controllers versus services; or when adding a feature that shares mechanics with existing flows.
---

# Code Structure

Reduce duplication and ownership confusion while preserving observable behavior. Prefer a small extraction over a new architecture.

## Map the behavior

1. Read repository instructions, dependency boundaries, public APIs, tests, and Git status.
2. Use code search to find every caller, near-duplicate, provider edge, state transition, transaction, retry, error mapping, and side effect.
3. Build a compact comparison:
   - behavior shared exactly;
   - behavior similar but intentionally different;
   - domain policy owned by each caller;
   - operational mechanics suitable for reuse.
4. Add or identify characterization tests before moving logic whose behavior is unclear.

Do not extract a one-off block solely to make a file shorter. Extract when multiple callers share a stable capability or a new caller would otherwise copy it.

## Choose the boundary

Keep in orchestration/actions:

- authorization, ownership, business policy, state transitions, transactions;
- user-facing error classification, workflow ordering, and product-specific retries;
- decisions about whether and when an operation occurs.

Move into a shared service:

- provider/SDK calls, command execution, sandbox setup, file mechanics;
- readiness checks, protocol normalization, and reusable low-level retries;
- operations that can accept explicit inputs and return structured results without reaching into domain state.

Design capability-sized functions. Avoid a god service that hides the original flow.

## Refactor safely

1. Define explicit parameters, return type, error contract, cancellation/timeout behavior, and observability.
2. Extract the smallest shared unit without opportunistic cleanup.
3. Migrate one representative caller and run its focused tests.
4. Migrate remaining callers in a mechanical batch, preserving their policy differences.
5. Remove dead copies only after search confirms no caller remains.
6. Add tests for shared mechanics plus caller-specific semantics and failure paths.

Prefer dependency injection at external boundaries. Do not introduce global mutable state, hidden database access, swallowed errors, or a generic abstraction with provider-specific conditionals everywhere.

## Quality gate

Run formatting, lint, typecheck, focused tests, and the relevant broader suite. Search again for duplicate blocks and old symbols. Confirm:

- public contracts, errors, ordering, transactions, and telemetry remain compatible;
- service API is smaller than the duplication it replaces;
- semantic differences remain visible at call sites;
- no unrelated user changes were overwritten.

Report the ownership boundary, migrated callers, tests run, and any duplication intentionally retained.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for simpler ownership and less duplication without semantic drift.
- Use medium freedom to choose boundaries and transaction ownership. Preserve public contracts, errors, behavior, and observability.
- Require mapped callers/differences, passing characterization/regression tests, and evidence that coupling decreased rather than moved. Revise once when weak.
- Learn only from accepted architecture decisions, reproduced defects, or measured complexity changes.
<!-- skill-evolver:adaptive-end -->
