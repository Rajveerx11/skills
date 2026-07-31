---
name: task-to-pr
description: Take one scoped task, ticket, issue, bug, or existing pull request through implementation, testing, independent review, publication, and CI until the pull request is ready for human merge. Use when the user explicitly wants end-to-end delivery to a PR rather than code changes or advice only.
---

# Task to PR

Ship one smallest complete change to a green, reviewed pull request. Never merge without a separate explicit request.

## Resume before creating

1. Resolve repository, source task/ticket, linked pull request, current branch/worktree, remote default branch, and Git status.
2. Read all applicable repository instructions.
3. Reuse an existing PR and branch when they represent the task. Do not duplicate tickets, branches, worktrees, or PRs.
4. Preserve unrelated and uncommitted user changes. Create a dedicated branch/worktree only when repository policy and current state make it safer.
5. Verify authenticated remote tooling and required CI before changing code.

Record a compact checkpoint: acceptance criteria, current commit, PR/ticket IDs, required checks, test commands, and known blockers. Use it to resume after interruption.

## Define acceptance

Translate the source into:

- user-visible outcome;
- in-scope and explicitly out-of-scope behavior;
- compatibility/security/performance constraints;
- tests and evidence that will prove completion.

If the source conflicts with the codebase or is materially incomplete, update/comment on the source only when authorized; otherwise report the decision needed.

## Implement

Inspect the relevant code and history. Make the smallest cohesive change, following existing patterns. Add or update tests for behavior and failure paths. Avoid adjacent cleanup unless required for correctness.

Run focused checks early, then applicable format, lint, typecheck, unit/integration/end-to-end tests, and production build. Use a real browser for browser-rendered acceptance criteria. Fix product failures; distinguish unrelated baseline failures with evidence.

## Independent review

Use a fresh subagent or equivalent independent reviewer that did not implement the change. Give it the task, acceptance criteria, and raw diff/artifacts—not the intended conclusions. Ask for correctness, regressions, security, missing tests, and scope drift.

Classify each finding with evidence. Fix valid issues, rerun affected tests, and obtain fresh review after substantial changes. Do not suppress findings to reach completion.

## Publish

1. Review the final diff and confirm no secrets or unrelated files.
2. Create a repository-conforming Conventional Commit.
3. Push the task branch.
4. Open or update one ready pull request linked to the source.
5. Include concise outcome, risk/rollback, and exact test/review evidence.

Invocation of this skill for delivery to a PR authorizes ordinary branch push and PR create/update for the scoped repository. It does not authorize merge, force-push, deleting branches, changing repository settings, or publishing releases.

## CI and feedback loop

Wait for required checks to reach a terminal state. Inspect logs for relevant failures, fix, test, commit, push, and reassess. Address currently available important human/bot feedback and reply with evidence. Use bounded polling and report external blockers; do not wait indefinitely for future comments.

## Stop condition

Stop only when the PR is open, mergeable, required CI is green or no checks are configured, independent review has no important unresolved findings, and current feedback is addressed.

Return PR link, commit SHA, changed paths, tests and CI, review disposition, merge state, and any precise blocker. Leave merge to the user.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for an explicitly requested, tested, independently reviewed, green pull request ready for human merge.
- Use medium freedom for implementation/test design and low freedom for user changes, branch policy, remote writes, acceptance criteria, and merge authority.
- Require explicit acceptance, risk-based tests, independent review, green CI, and verified PR state without merging. Revise once when weak.
- Learn only from project-local CI and review failures with verified resolutions.
<!-- skill-evolver:adaptive-end -->
