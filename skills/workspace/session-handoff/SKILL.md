---
name: session-handoff
description: Produce a verified, self-contained handoff so a fresh Codex or Claude session can resume without rediscovery. Use when the user says session handoff, wrap up, hand off, summarize before clearing context, continue this in a new session, or asks for current decisions, changed files, processes, tests, blockers, and the exact next action.
---

# Session Handoff

Produce a compact operational artifact for the next agent. This is not a retrospective or stakeholder status report.

## Evidence collection

Use conversation and active tool state first. Run narrow read-only checks only when needed to verify:

1. current user objective and latest scope changes;
2. active plan or goal status;
3. decisions the user approved and assumptions still provisional;
4. files actually created, modified, deleted, or generated this session;
5. branch, worktree, staged/unstaged state, and relevant commit or PR;
6. tests, validators, browser checks, deployments, and their exact outcomes;
7. active subprocesses, servers, monitoring cells, agents, ports, and stop commands;
8. external mutations such as messages, calendar events, deployments, PR comments, or connector writes;
9. blockers, deferred work, unresolved feedback, and unanswered questions.

Do not perform a broad filesystem audit. Use scoped `git status`, known plans, current process ids, tool results, and paths touched in this session. Mark facts as **confirmed**, **inferred**, or **unknown** when ambiguity matters.

## Output

Use this structure. Omit empty bullets, but never omit a section; write `none`.

```markdown
# Session Handoff — <outcome-focused title>

## Objective and scope
<original request, current definition of done, important constraints>

## Decisions and completed work
- <confirmed decision or change> — <reason and absolute path/resource id>

## Current state
- Workspace: <absolute path>
- Branch/worktree: <branch, path, dirty state>
- Active processes/agents: <ids, purpose, port, stop command> | none
- External state: <resource, mutation, verification> | none

## Key artifacts
- `<absolute path or resource URL/id>` — <why next agent needs it>

## Verification evidence
- `<command or check>` — <result, timestamp/commit when useful>

## Remaining work and blockers
- Next: <ordered unfinished work>
- Blocked: <exact dependency or authority needed> | none
- Open question: <decision and impact> | none

## Resume here
<single exact next action>

## Fresh-session prompt
<copy-ready prompt naming objective, workspace, key artifacts, constraints, and next action>
```

## Quality pass

Before returning:

- ensure the handoff alone can orient a fresh agent;
- replace relative paths with absolute paths;
- distinguish completed work from plans and unverified intent;
- include every live process or stateful external mutation;
- make verification reproducible;
- keep only the smallest set of key files;
- include one unambiguous next action;
- redact secrets, tokens, private note contents, and unnecessary personal data.

## Guardrails

1. Chat output only unless the user explicitly requests a file.
2. Never update memory, commit, stop processes, or mutate external state as part of handoff creation.
3. Never invent test success, Git cleanliness, remote state, process ids, or decisions.
4. Never claim a change is shipped when it is only local.
5. Never hide a dirty worktree, failed test, stale deployment, or unresolved review finding.
6. Preserve current user's tone, but prioritize technical clarity over compression when order matters.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for: a compact, evidence-tagged handoff that lets a fresh session resume without rediscovery
- Freedom: Medium. Adapt sections to task type; preserve confirmed state, scoped Git evidence, active processes, verification, and unresolved decisions.
- Autonomy: gather known state, run narrow verification, reconcile tool and Git evidence, then produce a copy-ready resumption prompt.
- Quality gate: confirmed, inferred, and unknown facts are separated; changed files and verification are scoped accurately; exact next action and resumption prompt are present. Revise once when any gate is weak.
- Learning: after explicit feedback or measurable results, record only explicit template preferences; task state is not durable skill learning. Never learn from silence, a single unverified outcome, or model self-rating.
<!-- skill-evolver:adaptive-end -->
