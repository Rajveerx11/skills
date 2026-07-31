---
name: find-skills
description: Discover, compare, inspect, and optionally install agent skills from the open skills ecosystem. Use when the user asks how to add a capability, wants a skill for a task, asks what reusable workflows exist, wants alternatives to an installed skill, or needs help installing or updating skills across Codex, Claude Code, or another supported agent.
---

# Find Skills

Find the smallest trustworthy skill set that fits the user's actual task and agent environment. Discovery is read-only; installation or updating requires authority from the current request.

## Workflow

### 1. Resolve the need

Infer from available context:

- concrete job to be done and desired artifact;
- target agent and global versus project scope;
- required tools, operating system, framework, and privacy constraints;
- whether an installed skill already covers the need.

List installed skills before searching when duplicate installation is plausible:

```bash
npx skills list --json
npx skills list -g --json
```

Do not ask for facts already visible in the workspace or agent configuration.

### 2. Search broadly, then narrow

Create two to four short query variants: task noun, action verb, ecosystem term, and common synonym. Run the useful searches, deduplicate package/skill pairs, then rank results.

```bash
npx skills find "react performance"
npx skills find "pull request review"
npx skills find react --owner vercel
```

If CLI search is unavailable, use the connected skill marketplace or search `skills.sh`; label that fallback.

### 3. Inspect candidates

Before recommending installation:

1. inspect available skills in the package:

   ```bash
   npx skills add owner/repository --list
   ```

2. inspect the selected `SKILL.md`, referenced scripts, requested permissions, external tools, and install scope;
3. prefer maintained, source-visible packages with precise triggers and reusable assets;
4. flag destructive commands, opaque downloads, broad permissions, secret handling, telemetry, or stale dependencies;
5. distinguish verified facts from repository claims.

Never treat popularity as proof of quality.

### 4. Present a decision-ready shortlist

Return at most three strong matches unless the user asks for a catalog. For each include:

- `owner/repository@skill`;
- what it automates;
- why it fits this environment;
- important dependency, permission, or maintenance tradeoff;
- exact install command.

Name a clear recommendation. If the installed skill already fits, recommend using or updating it instead of adding another.

### 5. Install only when authorized

Use explicit scope and agent selection. Avoid `--all` unless the user truly wants every skill installed for every supported agent.

```bash
npx skills add owner/repository --skill skill-name --agent codex claude-code -g
```

Use `-y` only when the user has already approved the exact package, skills, agents, and scope. After installation:

```bash
npx skills list -g --json
```

Verify the skill appears for each intended agent and report its resolved path. Never claim installation from command intent alone.

### 6. Update or remove

```bash
npx skills update skill-name -g
npx skills remove skill-name -g
```

Removal is destructive configuration change; require explicit request and verify the exact target first.

## No-match behavior

When no candidate clears the quality bar:

1. state which queries and sources were checked;
2. offer to solve the task directly;
3. if the need repeats, offer to create a focused owned skill with `npx skills init <name>`;
4. do not recommend a weak near-match to avoid returning empty results.

## Guardrails

- Never install, update, remove, trust, or grant permissions based only on inferred intent.
- Never execute scripts from an uninspected package.
- Keep credentials and private repository content out of search queries.
- Prefer one capable skill over overlapping packages that compete for context.
- Verify current CLI help before relying on experimental commands.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for: a small ranked set of trustworthy skills that genuinely match the user's task and environment
- Freedom: Medium. Expand queries and compare options; never install, trust, or grant permissions without current authority.
- Autonomy: inventory installed skills, search query variants, inspect candidates, rank tradeoffs, and verify authorized installation end to end.
- Quality gate: requirements and platform are captured; recommendations include provenance and tradeoffs; installation status is verified rather than assumed. Revise once when any gate is weak.
- Learning: after explicit feedback or measurable results, record selected results, rejected matches, and ecosystem compatibility through `skill-evolver`. Never self-edit from silence, a single unverified outcome, or model self-rating.
<!-- skill-evolver:adaptive-end -->
