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
    provider: "google"       # google | outlook | other connector id
    calendar_id: ""
    event_id: ""
    sync_fingerprint: ""
    sync_owned: false        # true only after this skill creates/adopts event
  - id: learn-rag
    title: Learn RAG
    start: "14:00"
    end: "15:00"
    type: event
    priority: normal
    provider: "google"
    calendar_id: ""
    event_id: ""
    sync_fingerprint: ""
    sync_owned: false
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

## Profile — `<state-root>/profile.md` (written at Setup)

```markdown
---
timezone: Asia/Kolkata
working_hours: { start: "10:30", end: "19:00" }
vault_path: "C:/path/to/Vault"
daily_folder: "Daily"
calendar:
  provider: "google"
  name: "Planning Schedule"
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

## Daily log — `<state-root>/logs/YYYY-MM-DD.json`

See the shape in `learning.md` §1. Created/updated at Wrap from the note's planned data.

## Provider-neutral calendar state

Build a canonical block first:

```json
{
  "id": "sandbox-feature",
  "title": "Sandbox feature",
  "start": "2026-06-15T11:00:00+05:30",
  "end": "2026-06-15T13:00:00+05:30",
  "timezone": "Asia/Kolkata",
  "type": "event",
  "reminder_min": 10
}
```

Map it to the connected provider:

- Google: `summary`, `start.dateTime`, `end.dateTime`, `timeZone`, reminders.
- Outlook: `subject`, `start.dateTime`, `end.dateTime`, `timeZone`, reminder.

After create/read-back, store `provider`, `calendar_id`, `event_id`,
`sync_fingerprint`, and `sync_owned: true`. Re-sync only when the canonical
fingerprint changes. Update/delete by provider plus calendar/event id. Never
delete when `sync_owned` is false.

Compute `sync_fingerprint` by passing this canonical block to
`scripts/sync_fingerprint.py` before mapping it to Google, Outlook, or another
provider. Do not hash provider response fields.
