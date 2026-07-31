---
name: plan-day
description: Turn vague tasks into a realistic time-blocked day, reconcile calendar conflicts, write an approved Obsidian plan, mirror blocks idempotently to a connected calendar, wrap completed work, roll unfinished items forward, and improve estimates from evidence. Use when the user asks to plan today or tomorrow, time-block tasks, wrap or review a day, synchronize an Obsidian daily plan with a calendar, or improve scheduling habits.
---

# Plan Day

Create a realistic day the user can execute, keep Obsidian and calendar state consistent, then learn from planned-versus-actual evidence.

Read [scheduling.md](scheduling.md) for planning and synchronization mechanics, [templates.md](templates.md) for schemas, and [learning.md](learning.md) before promoting durable patterns.

## Modes

- **Plan**: draft, revise, approve, write, and synchronize a day.
- **Wrap**: record actuals, check off work, and stage unfinished items.
- **Review**: calculate weekly execution and estimation patterns.
- **Setup**: configure vault, timezone, working hours, anchors, and calendar.
- **Repair**: reconcile note, log, and calendar state without duplicating events.

Infer mode from the request. Empty invocation means plan tomorrow in the configured timezone.

## Private runtime state

Never store personal schedules or profiles in this repository or an installed skill folder.

- Default state root: `%USERPROFILE%\.skill-data\plan-day` on Windows or `$HOME/.skill-data/plan-day` elsewhere.
- Profile: `profile.md`
- Durable patterns: `LEARNINGS.md`
- Logs: `logs/YYYY-MM-DD.json`
- Staged rollovers: `staged-rollovers.json`
- Human daily plan: profile-selected Obsidian vault.

If legacy `data/` state exists and external state does not, offer a one-time copy. Preserve the legacy directory as backup and exclude it from publishing.

## Autonomous workflow

### Plan

1. Read profile, durable learnings, staged rollovers, existing target-date note, and stored calendar ids.
2. Extract tasks, deadlines, fixed commitments, priority, duration clues, and desired task/event types already present in the request or workspace.
3. When calendar read access exists, inspect target-date conflicts before drafting. Read-only discovery needs no confirmation.
4. Ask one compact batch only for missing decisions that materially affect the schedule.
5. Build the timeline using [scheduling.md](scheduling.md): fixed items, soft anchors, dependencies, learned durations, energy windows, working hours, transitions, and slack.
6. Show the complete draft with conflicts, assumptions, unscheduled overflow, and zero to two evidence-backed nudges.
7. Do not write the note or calendar until the user approves the draft.
8. On approval, upsert the Obsidian note first. Fingerprint each canonical block with `scripts/sync_fingerprint.py`. Synchronize calendar entries by stable task id and stored provider id: update changed items, create new items, delete only items removed from the approved plan.
9. Read back the note and calendar result. Report written path, created/updated/deleted counts, unscheduled work, and any provider failure.

### Wrap

1. Read today's note and structured log.
2. Map volunteered status to stable task ids; ask only about unresolved high-priority items.
3. Patch managed checkboxes and actual fields without overwriting freeform notes.
4. Stage unfinished items with priority, deadline, and rollover count. Never roll recurring anchors as tasks.
5. Update durable patterns only under [learning.md](learning.md) evidence thresholds.
6. End with the most useful next action, not a guilt summary.

### Review

Run:

```powershell
python scripts/review_schedule.py "<state-root>\logs" --end 2026-07-31
```

Use deterministic metrics for completion, rollovers, and estimate accuracy. Use model judgment to explain causes, uncertainty, and one or two experiments. Do not infer a preference from missed tasks without a confirmed reason.

### Setup

Discover timezone, candidate vaults, and available calendars before asking. Collect:

- vault and optional daily folder;
- timezone and working hours;
- target calendar and reminder default;
- hard commitments and soft anchors with tolerances;
- focus areas, energy constraints, and planning horizon.

Create external state only after confirmation. Resolve and store provider calendar id once.

### Repair

- Treat Obsidian note task ids as canonical.
- Compare note, log, and calendar provider ids.
- Preview create, update, unlink, and delete actions.
- Never delete calendar entries lacking a confirmed ownership id.
- Apply approved repairs, then rerun the comparison until idempotent.

## Scheduling contract

- Fixed commitments never move without explicit instruction.
- Soft anchors may move only within configured tolerance.
- Default timed blocks to calendar events. Create tasks only when the user requests tasks or the profile defines that category.
- Keep buffers and leave overflow unscheduled rather than hiding impossible capacity.
- Convert relative dates to absolute dates before any write.
- Handle cross-midnight blocks and timezone offsets explicitly.
- A retry must produce no duplicate note tasks or provider events.

## Calendar integration

Use whichever connected calendar tools are available. Resolve tool names from the live connector instead of hard-coding Claude-specific identifiers. Required capabilities are list calendars, list target-date events, create, update, and delete.

Store provider, calendar id, event id, and last synchronized fingerprint in managed note frontmatter. If calendar tools are unavailable, finish the Obsidian plan, provide a structured sync queue, and state that calendar synchronization remains pending.

Compute the fingerprint from canonical fields before provider mapping:

```powershell
python scripts/sync_fingerprint.py canonical-block.json
```

Identical Google and Outlook mappings must produce the same fingerprint. Provider response fields never enter the fingerprint.

## Hard guardrails

1. Calendar and note writes require approval of the displayed draft.
2. Deletion requires an event id previously created or adopted by this skill.
3. Preserve private runtime state outside the published skill.
4. Never fabricate completion, actual duration, provider ids, or conflict checks.
5. Never silently drop an anchor, deadline, or overflow task.
6. Keep note/calendar synchronization recoverable and idempotent.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for: a realistic, conflict-free day plan synchronized idempotently with the user's chosen systems
- Freedom: Medium. Optimize blocks and buffers; preserve commitments, timezone, calendar authority, private state, and rollback.
- Autonomy: discover profile and conflicts, construct one strong draft, patch approved state, synchronize, verify, wrap, and review without repeated handoffs.
- Quality gate: tasks, anchors, availability, and conflicts are resolved; cross-midnight and timezone behavior are explicit; sync IDs and rollback make retries safe. Revise once when any gate is weak.
- Learning: after explicit feedback or measurable results, record observed completion, causal miss reasons, preferences, and derived statistics in private runtime state. Never self-edit from silence, a single unverified outcome, or model self-rating.
<!-- skill-evolver:adaptive-end -->
