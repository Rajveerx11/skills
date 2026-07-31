# Evidence-Gated Learning Loop

Keep runtime learning outside the installed skill. Reality is logged at Wrap,
distilled into `<state-root>/LEARNINGS.md`, and fed back into Plan. Resolve
`<state-root>` from the private location defined in `SKILL.md` before reading or
writing anything. Goal: improve estimates, slotting, and growth nudges from
evidence without publishing personal routines.

## The loop

```
Plan (apply private learnings) → live the day → Wrap (log planned-vs-actual)
       ▲                                                  │
       └──── distill into <state-root>/LEARNINGS.md ◀──────┘
```

## 1. Log reality (at Wrap)

Upsert `<state-root>/logs/YYYY-MM-DD.json`. One record per task plus a day
summary. Never store runtime logs in the installed skill directory:

```json
{
  "date": "2026-06-15",
  "tasks": [
    { "id": "sandbox-feature", "type": "focus", "planned_min": 120,
      "actual_min": 45, "completed": true, "rolled": false, "note": "finished early" },
    { "id": "linkedin-video", "type": "content", "planned_min": 60,
      "actual_min": 0, "completed": false, "rolled": true, "note": "skipped again" }
  ],
  "summary": { "completed": 5, "skipped": 1, "rollovers": 1, "peak_energy_block": "11:00-13:00" }
}
```

## 2. Distill into private LEARNINGS.md (at Wrap)

After logging, update `<state-root>/LEARNINGS.md`. Never create `data/`,
`LEARNINGS.md`, logs, profiles, or other runtime state inside the installed
skill or canonical repository. Do not append raw noise—maintain a small set of
durable, evidence-backed insights. For each, keep the pattern, evidence count,
and how to apply it.

Categories to maintain:
- **Estimation** — typical actual duration per task type vs what the user blocks. ("Sandbox/focus features: ~45 min median over 6 days, user blocks ~2 hrs.")
- **Preferences** — what consistently gets done vs skipped. ("LinkedIn video skipped 4/6 days — protect it, shorten it, or rethink format.")
- **Energy** — when deep work actually lands. ("Deep work best 11:00–13:00; post-lunch drifts.")
- **Patterns** — recurring structural issues. ("Fridays overcommit: ≥3 rollovers 3 weeks running — auto-cap Friday load.")

Update rules:
- Strengthen an existing insight when new evidence agrees (bump the count).
- Revise/soften when evidence contradicts. Retire insights that haven't held for 2+ weeks.
- Require ≥3 supporting days before treating something as a firm rule; below that, mark it `tentative`.

## 3. Feed back into Plan

Before showing a draft, apply current learnings:
- Use **learned durations** instead of the user's optimistic guess; if a task runs short historically, block the realistic time and offer a filler.
- Slot deep work into the **learned peak window**.
- Surface **0–2 nudges** as questions in the draft, e.g.:
  - *"Sandbox usually takes you ~45 min, not 2 hrs — want me to add a second task after?"*
  - *"You've skipped the LinkedIn video 4 of 6 days — make it a 15-min task and put it in your peak block?"*
  - *"It's Friday — you tend to overcommit. Cap at 4 focus items?"*

## 4. Growth read (Review mode)

Weekly, turn the trend data into a short, motivating read: what they're doing more of (celebrate), what's slipping (reframe as opportunity), and **1–2 concrete next steps**. Never a guilt list. The frame is always: *here's how to grow from here.*

## Tone guardrails

- Push forward, never backward. Slips become next steps.
- Be specific and evidence-backed ("4 of 6 days"), not preachy.
- The user owns the call — nudges are questions/offers, not mandates.
