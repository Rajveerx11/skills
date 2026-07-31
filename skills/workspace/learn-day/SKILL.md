---
name: learn-day
description: Track daily learning and shipped work, write structured Obsidian notes, calculate weekly consistency, detect evidence-backed learning patterns, and coach the next action. Use when the user asks to log learning, record what they studied or shipped, review their learning week, measure a consume-to-create habit, maintain a learning streak, or improve a self-education plan.
---

# Learn Day

Capture learning with minimal friction, connect consumption to visible output, and turn weekly evidence into one or two useful behavior changes.

Read [templates.md](templates.md) for note and log schemas. Read [learning.md](learning.md) before updating durable learning patterns.

## Modes

- **Log**: capture today's study, practice, and shipped output.
- **Week**: calculate a seven-day scorecard and coach next week.
- **Setup**: create or update profile, vault, metrics, and learning tracks.
- **Repair**: reconcile missing or inconsistent notes and structured logs.

Infer mode from the request. Empty invocation means Log. Run Setup only when no usable profile exists.

## Runtime state

Never store personal state in a public or package-managed skill folder.

- Default state root: `%USERPROFILE%\.skill-data\learn-day` on Windows or `$HOME/.skill-data/learn-day` elsewhere.
- Profile: `profile.md`
- Durable patterns: `LEARNINGS.md`
- Structured logs: `logs/YYYY-MM-DD.json`
- Human notes: profile-selected Obsidian vault and folders.

If legacy `data/profile.md` exists beside this skill and external state does not, offer a one-time copy to the external state root. Preserve the legacy files as backup; never publish them.

## Autonomous workflow

### Log

1. Read profile and durable learnings. Resolve today's absolute date and timezone.
2. Extract everything already provided: sources studied, practice, duration, track, key insight, confusion, and shipped artifact.
3. Ask only for missing high-value fields, in one short batch. Never force all fields.
4. Map activity to configured tracks and curriculum steps. Do not invent completion or duration.
5. Upsert today's structured log by stable activity id and artifact id. Re-running must update, not duplicate. Count only unique artifacts explicitly marked `published`; drafts and scheduled items remain pipeline work.
6. Write or update today's Obsidian note from [templates.md](templates.md). Preserve user-authored text outside managed sections.
7. Update durable learnings only when evidence meets [learning.md](learning.md) thresholds.
8. End with one concrete action sized for the user's available time.

### Week

1. Read the requested date range; default to the last seven local calendar days.
2. Run the deterministic scorecard:

   ```powershell
   python scripts/weekly_score.py "<state-root>\logs" --end 2026-07-31
   ```

3. Read relevant notes for qualitative context, not to override structured facts.
4. Report specific wins, bottleneck evidence, track drift, consume-to-create ratio, and streak.
5. Recommend one to three changes with owner, trigger, size, and success measure.
6. Write a weekly Obsidian note only when profile enables it or the user asks.

### Setup

Resolve existing vaults and timezone before asking. Collect only:

- vault and learning-note folders;
- timezone and filename format;
- active learning tracks or curriculum source;
- target days and configured north-star behavior;
- what counts as a shipped artifact;
- optional weekly report folder.

Create external profile, learnings file, and log directory. Validate write access with a harmless temporary file, then remove it.

### Repair

- Compare daily notes with structured logs by date and stable activity id.
- Preview additions or corrections.
- Never overwrite freeform notes or infer shipped work.
- Recompute weekly metrics after repair and show the delta.

## Coaching rules

- Evidence over guilt. State the measured gap, likely cause, and next experiment.
- Output definition belongs in profile. A LinkedIn post, code commit, prototype, exercise, or teaching note can all count when configured.
- Use the shared artifact schema in [templates.md](templates.md). Stable published artifact IDs, not mutable titles or numeric counters, determine shipped totals and shipping streaks.
- Consumption is useful only when connected to recall, practice, synthesis, or shipping.
- Separate user preferences from patterns inferred across several days.
- Track estimates and streaks mechanically; use model judgment for synthesis and coaching.
- Treat missed days as missing data unless the user confirms no work occurred.

## Hard guardrails

1. Never fabricate activity, duration, streaks, shipped links, or outcomes.
2. Never publish vault paths, personal notes, logs, or learnings with the skill package.
3. Never rewrite an entire note when a managed section can be patched.
4. Never promote one weak observation into a durable rule.
5. Never create calendar items or public posts unless the request separately authorizes them.
6. Convert relative dates to absolute local dates before writes.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for: low-friction daily capture plus an evidence-backed weekly diagnosis that turns learning into shipped output
- Freedom: Medium. Personalize questions and coaching; preserve dates, user voice, source logs, privacy, and evidence thresholds.
- Autonomy: extract volunteered facts, upsert notes and logs, compute metrics, reconcile state, and offer the next experiment without repeated questions.
- Quality gate: note and JSON agree; weekly metrics are reproducible; coaching cites evidence and ends with a concrete next action. Revise once when any gate is weak.
- Learning: after explicit feedback or measurable results, record supported learning patterns, estimate errors, and confirmed preferences in private runtime state. Never learn from silence, a single unverified outcome, or model self-rating.
<!-- skill-evolver:adaptive-end -->
