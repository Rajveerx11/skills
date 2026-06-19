# Templates

Copy-paste-ready shapes for the Obsidian note, the profile, the daily log, and the Calendar payload.

## Obsidian daily note — `<vault_path>/<DD-MM-YY(ddd)>.md`  (e.g. `15-06-26(Mon).md`)

> Filename uses the profile's `daily_note_format`. The `date:` frontmatter field stays ISO (`YYYY-MM-DD`) for sorting; only the filename uses the `DD-MM-YY(ddd)` form.

Frontmatter holds the machine state (ids + calendar links); the body is the human checklist.

```markdown
---
date: 2026-06-15
plan_generated: 2026-06-14
tasks:
  - id: sandbox-feature
    title: Sandbox feature
    start: "11:00"
    end: "13:00"
    type: event        # event (default) | task
    priority: top      # top | normal
    gcal_event_id: ""   # filled after Calendar sync
  - id: learn-rag
    title: Learn RAG
    start: "14:00"
    end: "15:00"
    type: event
    priority: normal
    gcal_event_id: ""
rolled_over: []        # ids carried from the previous day
---

# 2026-06-15

## Schedule
- 08:00–10:00 — Basketball _(anchor)_
- 10:00–10:45 — Breakfast + rituals _(anchor)_
- 11:00–13:00 — **Sandbox feature** ★ _(event)_
- 13:00–14:00 — Lunch _(anchor)_
- 14:00–15:00 — Learn RAG _(event)_
- 15:00–15:30 — Call with Aman _(event, fixed)_

## To-do
- [ ] Sandbox feature
- [ ] Learn RAG
- [ ] Call with Aman

## Notes
```

At Wrap, flip `- [ ]` → `- [x]` for completed items. Anchors/meals usually aren't to-do items unless the user wants them tracked.

## Profile — `data/profile.md` (written at Setup)

```markdown
---
timezone: Asia/Kolkata
working_hours: { start: "10:30", end: "19:00" }
vault_path: "C:/path/to/Vault"
daily_folder: "Daily"
calendar:
  name: "Tessera Schedule"
  id: ""                 # resolved via list_calendars at Setup
  default_reminder_min: 10
anchors:
  - { title: "Basketball", usual: "08:00-10:00", days: "Mon-Sat", tolerance_min: 30 }
  - { title: "Breakfast + rituals", usual: "10:00-10:45", days: "daily", tolerance_min: 45 }
  - { title: "Lunch", usual: "13:00-14:00", days: "daily", tolerance_min: 60 }
focus_areas:
  - "AI learning"
  - "Existing projects"
  - "New project ideas"
  - "LinkedIn personal branding"
  - "YouTube / Instagram channel (to start)"
---

# Profile
Set once at Setup. The skill reads this every run and never re-asks the anchors.
Edit by re-running `/plan-day setup` or by hand.
```

## Daily log — `data/logs/YYYY-MM-DD.json`

See the shape in `learning.md` §1. Created/updated at Wrap from the note's planned data.

## Google Calendar payload (per block)

When calling `mcp__claude_ai_Google_Calendar__create_event`:
- `calendar id` → from `profile.calendar.id`.
- `summary` → task title (prefix `[task]` only for the task fallback case).
- `start` / `end` → ISO datetime built from the block times + profile timezone.
- `reminders` → profile `default_reminder_min`.
- Capture the returned event id → write into the note frontmatter `gcal_event_id`.

For re-sync use `update_event` / `delete_event` keyed on the stored `gcal_event_id` (idempotency — see `scheduling.md`).
