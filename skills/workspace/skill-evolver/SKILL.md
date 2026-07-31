---
name: skill-evolver
description: Audit, enhance, learn from, validate, and synchronize Codex and Claude skills. Use when creating or improving skills at scale, reducing repeated human work, adding advanced-model creative freedom, learning from explicit feedback or measurable outcomes, resolving drift between global skill copies and a Git repository, or preparing a tested skill release. Uses evidence-gated evolution; never silently rewrites skills from weak signals.
---

# Skill Evolver

Turn a skill collection into a maintained system: clear triggers, outcome-first autonomy, suitable creative freedom, deterministic checks, bounded learning, and reproducible synchronization.

## Modes

- **Audit**: inspect purpose, trigger quality, workflow friction, resources, portability, and validation.
- **Enhance**: revise one skill or a whole portfolio.
- **Learn**: record explicit feedback, preferences, failures, or metrics without editing a skill yet.
- **Evolve**: promote supported learning into a tested skill change.
- **Sync**: compare and copy an approved canonical portfolio to Codex and Claude roots.
- **Release**: validate, back up, synchronize, verify, commit, and publish an approved portfolio.

## Operating contract

1. Treat user-owned repository copies as canonical when a repository exists.
2. Treat system skills, plugin caches, package-manager files, and generated vendor bundles as read-only. Fork an owned copy instead of patching managed files.
3. Preserve hard safety rules, tool contracts, schemas, exact commands, and deterministic render/build requirements.
4. Treat the rest of a workflow as a strong default, not a ceiling. Let the model choose better tactics when context supports them.
5. Infer low-risk details from available context. Ask only when a missing choice materially changes outcome, risk, cost, or irreversible state.
6. Complete the authorized workflow end to end. Do not stop at advice when safe implementation and verification remain.
7. Never let a skill grant authority beyond the user request.
8. Keep private profiles, logs, outcomes, backups, caches, and execution scratch
   outside the canonical repository.

## Enhancement workflow

### 1. Discover

- Inventory direct global skill roots, the canonical repository, and duplicate names.
- Exclude `.git`, `node_modules`, caches, runtime logs, personal memory, and managed plugin/system directories unless explicitly requested.
- Read each target `SKILL.md`; inspect referenced scripts and only the resources relevant to its workflow.
- Run `scripts/validate_portfolio.py` for a structural baseline.
- Build or refresh target mapping from direct, non-junction installs with
  `scripts/build_manifest.py`; inspect the result before syncing.

### 2. Model each skill

For every skill, write a compact profile containing:

- intended outcome;
- repeated human work to automate;
- freedom class: high, medium, or low;
- hard constraints that cannot move;
- three observable quality gates;
- useful feedback or metrics.

Use [references/evolution-rubric.md](references/evolution-rubric.md) when classifying.

### 3. Improve

Prefer changes in this order:

1. Fix broken triggers, paths, commands, links, and portability.
2. Remove unnecessary questions and manual handoffs.
3. Add context discovery, sensible defaults, batch operations, reusable scripts, and artifact reuse.
4. Add an outcome contract and domain-specific quality gate.
5. Add multiple creative directions only when judgment is subjective.
6. Move long variants or examples into directly linked references.
7. Add deterministic scripts for repeated or fragile operations.
8. Add `agents/openai.yaml` when useful for Codex UI discovery.
9. Remove package runtime state from the repository and add explicit sync
   exclusions so upgrades cannot overwrite private learning.

Keep `SKILL.md` concise. Do not bury core steps in philosophy, duplicate the same rule across files, or make deterministic protocols “creative.”

### 4. Learn safely

Record only explicit feedback, stated preferences, observed failures, or measurable results:

```powershell
python scripts/record_outcome.py --skill example-skill --signal feedback --observation "User prefers concise executive summaries" --evidence "Explicit correction in run 2026-07-31"
python scripts/outcome_report.py --skill example-skill
```

Promotion rules:

- One explicit preference may update a user-specific default.
- One verified correctness or safety defect may update a hard guardrail.
- Quality heuristics need two consistent outcomes or one strong measured result.
- Silence, task completion, model self-rating, and unverified guesses are not learning evidence.
- Keep personal/runtime learning outside public skill repositories.

### 5. Evolve

- Convert supported evidence into the smallest general rule.
- State the hypothesis and expected improvement.
- Patch the canonical skill and reusable resources.
- Test scripts directly.
- Forward-test complex revisions on realistic tasks without leaking the expected answer.
- Compare output against the old version or a fixed rubric.
- Revert or revise when quality does not improve.

Never auto-commit, auto-push, or modify production systems unless the current user request authorizes it.

### 6. Validate and sync

```powershell
python scripts/build_manifest.py <repo-root>
python scripts/build_manifest.py <repo-root> --apply
python scripts/render_catalog.py <repo-root> --apply
python scripts/run_release_checks.py <repo-root>
python scripts/sync_portfolio.py <repo-root> --prune --details
python scripts/sync_portfolio.py <repo-root> --apply --prune
python scripts/sync_portfolio.py <repo-root> --verify-only
```

Dry-run manifest generation and exact sync first. Applied sync stages all
changes, creates a timestamped backup plus receipt for every overwritten or
pruned file, excludes runtime learning, uses atomic file replacement, rolls
back the transaction on failure, and verifies the full manifest afterward.

## Completion report

Report:

- skills audited, changed, added, skipped, and why;
- validation and forward-test results;
- backup location;
- repository commit/push state;
- any runtime learning intentionally excluded from version control.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for: a safer, more autonomous, validated skill portfolio that improves from evidence without silent drift
- Freedom: Medium. Adapt enhancements to each motive; preserve user authority, managed-file boundaries, safety contracts, validation, and rollback.
- Autonomy: inspect available context first, infer low-risk details, choose strong defaults, and finish the authorized workflow end to end. Ask only when a choice materially changes outcome, risk, cost, or irreversible state.
- Quality gate: every skill has a purpose-specific profile; structural and representative behavior tests pass; canonical and installed copies match with backups. Revise once when any gate is weak.
- Learning: after explicit feedback or measurable results, record explicit feedback, reproduced defects, and measured outcomes promoted through evidence gates through `skill-evolver`. Never self-edit from silence, a single unverified outcome, or model self-rating.
<!-- skill-evolver:adaptive-end -->
