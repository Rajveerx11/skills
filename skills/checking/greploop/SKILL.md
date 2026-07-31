---
name: greploop
description: Iterate on a GitHub pull request, GitLab merge request, or Perforce shelved changelist until current Greptile findings are resolved and its reported confidence target is met. Use when the user asks to run a Greptile review loop, clear Greptile comments, or bring a reviewed change set to 5/5 without hiding valid findings or weakening tests.
---

# Greploop

Run a real review/fix/review loop using the repository's configured Greptile integration. This skill does not assume a cloud plugin or fabricate a trigger command.

## Preflight

1. Detect provider and change identifier from the current branch, URL, or user input.
2. Read repository instructions, ticket/acceptance criteria, diff, related tests, branch policy, CI, and Git status.
3. Verify authenticated read/write tooling (`gh`, `glab`, or `p4`) and identify the existing Greptile surface: check, review, bot comments, command, webhook, or UI action.
4. Preserve unrelated and uncommitted user changes. Reuse the existing branch/worktree/changelist.
5. Record the starting commit/shelf, Greptile score/state, unresolved thread IDs, and required tests.

If no Greptile installation, trigger path, or score is observable, stop after available read-only discovery and report the exact missing connection. Do not substitute another reviewer while claiming Greptile completion.

## Ingest findings

Fetch all current Greptile checks, reviews, inline threads, and summary comments, including pagination. Normalize each finding:

- stable provider/thread ID and file/line;
- severity and requested change;
- commit or diff version reviewed;
- status: actionable, already fixed/outdated, duplicate, incorrect, or acceptance-scope conflict;
- evidence and planned verification.

Read the surrounding code and tests before classifying. Never dismiss a finding solely to reduce the unresolved count.

## Fix one coherent batch

1. Address root causes with the smallest complete changes.
2. Add or strengthen regression tests for behavioral findings.
3. Preserve public contracts and acceptance criteria; avoid unrelated cleanup.
4. Run focused tests, then required format/lint/typecheck/build checks.
5. Review the new diff for unintended changes.
6. Commit and push, or re-shelve, using repository conventions.
7. Reply to threads with concise evidence when provider policy expects it. Resolve a thread only after the fix is published or the evidence-backed rejection is documented.

Consequential changes that exceed the ticket, alter architecture, or conflict with reviewer advice require user direction.

## Re-trigger and repeat

Use only the trigger mechanism discovered in preflight. Record the reviewed commit SHA or shelf version, then wait for a fresh Greptile result. Confirm comments belong to the new version.

Repeat ingestion, fixes, tests, publish, and review until:

- Greptile explicitly reports 5/5 when that score exists;
- no actionable unresolved Greptile findings remain;
- relevant tests and required CI pass.

Do not translate another score into “5/5.” If the same finding returns twice unchanged, Greptile never reviews the new commit, CI is blocked externally, or the integration stops responding, investigate once and report a stalled-state blocker with evidence rather than looping forever.

## Completion

Return provider/change link, starting and final commit/shelf, score history, finding disposition summary, test/CI evidence, and unresolved blocker if any. Never merge unless separately requested.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for a reviewed change set with every actionable Greptile finding resolved or evidence-backed.
- Use medium freedom for fixes; preserve user changes, acceptance criteria, branch policy, tests, and reviewer independence.
- Require classified findings, passing tests/CI, and target review state without hiding or gaming feedback. Revise once when weak.
- Learn only from repeated review failure categories and accepted remediation evidence.
<!-- skill-evolver:adaptive-end -->
