---
name: create-skill
description: Create, update, audit, migrate, and validate reusable skills for Codex, Claude Code, or a shared agent-skills repository. Use when the user asks to create a skill, custom command, slash command, reusable agent workflow, skill package, or to improve an existing SKILL.md and its scripts, references, assets, triggers, metadata, or tests.
---

# Create Skill

Build skills that give advanced models useful domain leverage without replacing judgment with boilerplate.

Read [references/platforms.md](references/platforms.md) when selecting runtime-specific metadata or install paths. Read [references/examples.md](references/examples.md) only when a concrete pattern is needed.

## Modes

- **Create**: build a new skill and reusable resources.
- **Update**: improve an existing skill while preserving its working contracts.
- **Audit**: diagnose trigger, portability, context, workflow, resource, and validation problems.
- **Migrate**: make a runtime-specific skill portable across Codex and Claude Code.

## End-to-end workflow

### 1. Discover context

Inspect repository instructions, target agent, skill roots, duplicate names, nearby conventions, expected artifacts, failure modes, and side effects before asking questions. Infer low-risk details. Ask one consolidated clarification only when scope, authority, cost, or irreversible behavior would materially change.

### 2. Model the skill

Write a compact internal contract:

- outcome the skill must produce;
- three realistic trigger examples and two near-miss examples;
- repeated human work to automate;
- required scripts, references, or assets;
- freedom class: high, medium, or low;
- hard safety, schema, platform, or tool constraints;
- three observable quality gates.

Use high freedom for writing, design, strategy, and synthesis. Use medium freedom for mixed workflows. Use low freedom for destructive operations, fragile APIs, exact formats, releases, and security invariants.

### 3. Choose scope and portability

Prefer a shared portable skill when both agents should use it:

```text
skill-name/
├── SKILL.md
├── agents/openai.yaml
├── scripts/
├── references/
└── assets/
```

For portable `SKILL.md` frontmatter, use only `name` and `description`. Add runtime-specific fields only when the user explicitly wants a single-runtime skill and the current runtime supports them.

Default to project scope for project-specific behavior, global scope for cross-project behavior, and an existing canonical skills repository when it already controls installed copies. Never edit managed system skills, plugin caches, or package-generated vendor files; create an owned fork.

### 4. Initialize and build resources

For a new Codex-compatible skill, locate the installed `skill-creator` helper and run:

```bash
python scripts/init_skill.py skill-name --path <target-root> --resources scripts,references --interface "display_name=Skill Name" --interface "short_description=Short useful description" --interface "default_prompt=Use $skill-name to complete the task."
```

Request only needed resource directories. Delete placeholders. For updates, patch the smallest complete surface.

- Put deterministic or repeatedly rewritten operations in `scripts/`.
- Put optional domain detail in `references/`.
- Put output templates, fonts, icons, and boilerplate in `assets/`.
- Keep core routing and workflow in `SKILL.md`.

Run every new script on a representative fixture.

### 5. Author `SKILL.md`

```yaml
---
name: concise-kebab-case
description: What it does. Use when the user asks for concrete trigger contexts.
---
```

1. Use imperative instructions for another capable agent.
2. Lead with outcome, modes, and routing.
3. Automate context discovery, batching, defaults, checkpoints, and verification.
4. Treat subjective workflows as adaptable defaults; protect exact contracts.
5. Ask only for decisions requiring user knowledge or authority.
6. Link resources relative to the skill directory and state when to read them.
7. Keep core file under 500 lines; move long variants and examples one level into `references/`.
8. Never embed secrets, personal runtime logs, temporary files, or generated caches.
9. Do not add README, changelog, install guide, or process diary inside the skill.

### 6. Add agent metadata

For Codex discovery, generate `agents/openai.yaml` with the official helper when available. Supply a clear display name, a 25–64 character short description, and a one-sentence default prompt explicitly mentioning `$skill-name`. Quote strings. Add no icon or brand fields without actual assets or values.

### 7. Validate behavior

Run the platform validator:

```bash
python scripts/quick_validate.py <skill-folder>
```

Then verify:

- name matches folder and description handles positive and negative triggers;
- every relative reference resolves;
- scripts pass representative success and failure fixtures;
- runtime metadata matches the body;
- a fresh agent can complete a realistic task without hidden context;
- safety and user authority remain intact.

For substantial changes, forward-test with a fresh agent receiving only the skill and a realistic request. Do not leak the intended solution. Compare artifacts against the quality gates and revise once.

### 8. Install and hand off

Sync approved canonical files only. Back up overwritten globals, exclude runtime learning and caches, verify copied hashes, then report changed paths, targets, test evidence, dependencies, and rollback source.

## Guardrails

- A skill cannot grant authority beyond the user's request.
- Never make deterministic protocols “creative.”
- Never copy managed vendor skills into a public repository without checking license and provenance.
- Never learn from silence, model self-rating, or one unverified result.
- Prefer one sharp skill over overlapping instructions that compete for context.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for: a concise, portable, tested skill with strong triggers and reusable resources
- Freedom: Medium. Tailor workflow and resources to task variability; preserve platform syntax, validation, safety, and context efficiency.
- Autonomy: inspect target runtimes and nearby conventions, generate reusable resources, validate, forward-test, install, and report without unnecessary handoffs.
- Quality gate: positive and negative trigger cases are clear; all referenced resources and commands resolve; representative forward tests improve results. Revise once when any gate is weak.
- Learning: after explicit feedback or measurable results, record versioned eval failures and explicit maintainer feedback through `skill-evolver`. Never self-edit from silence, a single unverified outcome, or model self-rating.
<!-- skill-evolver:adaptive-end -->
