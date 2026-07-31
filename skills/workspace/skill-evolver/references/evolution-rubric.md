# Evolution rubric

## Freedom classes

### High freedom

Use for design, writing, research synthesis, strategy, storytelling, and creative direction.

- Generate two or three meaningfully different internal directions when the choice matters.
- Select using audience, goal, context, distinctiveness, and feasibility.
- Preserve user voice and brand; avoid template convergence.
- Validate with an artifact-level critique and revise the weakest dimension once.

### Medium freedom

Use for planning, coaching, workflow assembly, integrations, migrations, and mixed creative/technical work.

- Follow required checkpoints and schemas.
- Adapt ordering, defaults, tools, and decomposition to context.
- Automate discovery and low-risk decisions.
- Validate both the artifact and the operational handoff.

### Low freedom

Use for security, destructive changes, exact file formats, deploy/release procedures, deterministic rendering, and fragile APIs.

- Follow exact contracts and commands.
- Fail closed when preconditions are unmet.
- Make risk, rollback, and evidence explicit.
- Use creativity only in diagnosis or optimization outside the protected protocol.

## Outcome profile

Each skill profile must answer:

1. What finished artifact or state should exist?
2. What must be true for the user to call it excellent?
3. Which steps can be inferred or automated?
4. Which decisions require user authority?
5. Which rules protect safety, correctness, or compatibility?
6. Which three checks can falsify a weak result?
7. Which feedback or metric can improve the next run?

## Human-work reduction

Prefer:

- automatic environment and context discovery;
- one consolidated clarification round;
- ranked defaults with reasons;
- batch processing;
- reusable scripts and templates;
- checkpoint/resume support;
- generated manifests and reports;
- direct verification;
- explicit final paths and next actions.

Avoid:

- asking for information already available locally;
- returning a plan when authorized execution is possible;
- making the user copy data between tools manually;
- repeating boilerplate code that belongs in a script;
- requiring subjective choices before offering concrete directions;
- writing runtime learning into a public repository.

## Learning evidence

| Signal | Strength | Promotion |
|---|---:|---|
| Explicit user preference | High for that user | User-specific default |
| Reproduced correctness defect | High | Immediate guardrail |
| Objective metric delta | High | General heuristic if causal link is plausible |
| Repeated similar feedback | Medium-high | General heuristic after two consistent signals |
| Single subjective outcome | Medium | Keep pending |
| Agent self-rating | Low | Never promote alone |
| No complaint or user silence | None | Do not record as success |

## Release gate

- Metadata triggers intended requests and avoids obvious false positives.
- Relative references resolve.
- Scripts pass representative tests.
- Skill preserves hard constraints.
- Output quality beats or matches baseline on realistic prompts.
- Runtime/personal data stays untracked.
- Canonical, Codex, and Claude copies match after sync.
