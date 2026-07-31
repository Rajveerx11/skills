---
name: obsidian-vault-tune-up
description: Audit, reorganize, repair, and improve an Obsidian vault for human navigation and reliable AI retrieval. Use when the user asks to clean up a vault, repair links, reduce duplicate or orphan notes, design maps of content, normalize metadata, improve searchability, or make an Obsidian knowledge base safer for model context.
---

# Obsidian Vault Tune-Up

Turn a working vault into a clearer, safer knowledge system without flattening the user's voice or destroying useful history.

## Modes

- **Audit**: inventory structure, links, metadata, duplicates, attachments, and retrieval friction. Default when change authority is unclear.
- **Plan**: propose a target structure, migration batches, naming rules, and rollback.
- **Apply**: make an approved reorganization, updating links and validating every batch.
- **Maintain**: add lightweight conventions, templates, maps of content, and repeatable checks.

## Autonomous workflow

1. Locate the vault from the user-provided path, current workspace, or an existing profile. A vault normally contains `.obsidian/`. If several candidates exist, present the ranked paths and ask once.
2. Read local instructions and inspect a representative sample before proposing taxonomy. Detect existing folder, filename, frontmatter, tag, attachment, and linking conventions.
3. Run the bundled read-only audit:

   ```powershell
   python scripts/audit_vault.py "C:\path\to\vault" --output "$env:TEMP\obsidian-vault-audit.md"
   ```

   Use `--json` when another tool will consume the report. The script rejects
   output inside the vault by default; use `--allow-inside-vault` only after the
   user explicitly requests an in-vault report. The report is evidence, not an
   automatic mandate to reorganize.
4. Rank findings by retrieval impact, breakage risk, confidence, and effort. Separate confirmed defects from subjective preferences.
5. Design the smallest useful change. Prefer navigation notes, maps of content, aliases, and consistent metadata before large folder moves.
6. Before bulk edits, establish recovery:
   - use the vault's clean Git history when available;
   - otherwise create a timestamped backup outside the vault;
   - show the exact files affected and migration rules.
7. Apply in bounded batches. Move notes with filesystem-safe operations, update Obsidian wikilinks and Markdown links, preserve frontmatter and aliases, and keep attachments with their references.
8. Rerun the audit after each material batch. Compare broken links, ambiguous links, orphans, duplicate names, missing metadata, and note counts against baseline.
9. Deliver changed paths, before/after metrics, remaining judgment calls, rollback location, and a maintenance command.

## Organization heuristics

- Preserve a user's working mental model unless measured retrieval problems justify change.
- Prefer shallow folders plus maps of content over deep taxonomies.
- Give durable concepts stable filenames; put changing display language in aliases.
- Use frontmatter only for fields that drive a real query, workflow, or retrieval filter.
- Treat tags as cross-cutting facets, not a second folder tree.
- Separate inbox, active work, reference, and archive only when those states are meaningful in this vault.
- Keep source notes and synthesized evergreen notes distinguishable.
- Flag near-duplicates for review; never merge solely from title similarity.

## Hard guardrails

1. Default to read-only audit. Never rename, move, merge, or delete notes without authorization covering that scope.
2. Never delete content as "duplicate." Quarantine or retain both versions until the user approves a merge.
3. Never expose private note contents in public reports. Use paths, counts, hashes, and short redacted excerpts.
4. Preserve `.obsidian/`, plugin state, hidden files, canvases, embeds, aliases, block references, and attachment relationships.
5. Do not turn every note into a rigid template. Optimize retrieval while preserving natural capture.
6. Validate links after changes; a visually tidy vault with broken references is a regression.
7. Keep generated audit reports outside the vault unless the user wants them stored there.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for: a safer, easier-to-navigate vault that remains understandable to humans and useful as model context
- Freedom: Medium. Adapt taxonomy, maps, links, and templates; preserve content, backlinks, user conventions, privacy, and recoverability.
- Autonomy: discover the vault and its conventions, run a read-only baseline, rank changes, and complete approved batches without repeated handoffs.
- Quality gate: inventory and broken-link baseline are captured; changes are previewed and reversible; navigation, orphan, duplicate, and retrieval checks improve. Revise once when any gate is weak.
- Learning: after explicit feedback or measurable results, record accepted organization choices and measured retrieval friction through `skill-evolver`. Never self-edit from silence, a single unverified outcome, or model self-rating.
<!-- skill-evolver:adaptive-end -->
