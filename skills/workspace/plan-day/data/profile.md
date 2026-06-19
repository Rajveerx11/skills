---
configured: true
timezone: Asia/Kolkata
# Primary focus window — where new tasks get time-blocked.
working_hours: { start: "13:00", end: "00:00" }
focus_window: { start: "13:00", end: "18:00" }   # main work session (4-5 hrs)
overflow_window: { start: "22:30", end: "00:00" } # optional late project work
vault_path: "C:/Users/rajve/OneDrive/Documents/Obsidian Vault/Daily Tasks Update"
daily_folder: ""            # notes go directly in vault_path
daily_note_format: "DD-MM-YY(ddd)"   # e.g. 15-06-26(Mon).md
calendar:
  name: "Rajveer Vadnal (primary)"
  id: "rajveer11vadnal@gmail.com"
  default_reminder_min: 10
anchors:
  - { title: "Basketball (morning)", usual: "08:00-10:00", days: "Mon-Sat", tolerance_min: 30 }
  - { title: "Work session", usual: "13:00-18:00", days: "daily", tolerance_min: 60, fills_tasks: true }
  - { title: "Basketball (evening)", usual: "19:00-22:00", days: "daily", tolerance_min: 30 }
  - { title: "Late project work (optional)", usual: "22:30-00:00", days: "daily", tolerance_min: 30, optional: true }
focus_areas:
  - "Existing projects"
  - "AI learning (podcasts, new concepts)"
  - "New project ideas"
  - "LinkedIn personal branding"
  - "YouTube / Instagram channel (to start)"
---

# Profile

Fully configured. The skill reads this every run and never re-asks anchors.

**How the day is shaped:**
- **Basketball morning** (08:00–10:00, Mon–Sat) and **evening** (19:00–22:00) are soft
  anchors — kept near time, flex ±30 min.
- **Work session** (13:00–18:00) is the primary focus window: new tasks for the day are
  time-blocked here (`fills_tasks: true`). Projects, AI learning, and podcasts live here.
- **Late project work** (22:30–00:00) is optional overflow — only used when there's more
  to do or a task spills past the work session.

Daily notes → written directly in `vault_path`, named `DD-MM-YY(ddd).md`.
Calendar → primary calendar, events by default, 10-min reminders.
Edit by re-running `/plan-day setup` or by hand.
