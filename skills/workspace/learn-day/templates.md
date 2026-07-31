# Templates

Copy-paste-ready shapes for the daily note, weekly report, profile, and daily log.

## Daily note — `<learning_folder>/Learn-DD-MM-YY(ddd).md` (e.g. `Learn-23-06-26(Tue).md`)

> Filename uses the profile's `daily_note_format`. The `date:` frontmatter stays ISO for sorting.

```markdown
---
date: 2026-06-23
type: learn-day
tracks: [Personal Brand, Copywriting]      # which curriculum tracks today touched
studied:
  - { item: "Dan Koe — One-Person Business 2026", kind: video, track: Personal Brand }
  - { item: "Hook-Story-Offer framework", kind: article, track: Copywriting }
shipped:
  - { type: post, platform: LinkedIn, topic: "Why I'm building in public", url: "" }
watch_ship: { watched: 2, shipped: 1 }      # the headline ratio
product_progress: "Outlined the n8n template pack"
streak_days: 3                               # consecutive days a post shipped
---

# 📚 Learn-Day · 2026-06-23 (Tue)

## What I studied
- 🎥 **Dan Koe — One-Person Business 2026** — _Personal Brand_
  - Takeaway: validate as you go; idea → post → download → product.
- 📄 **Hook-Story-Offer** — _Copywriting_
  - Takeaway: lead with the hook, bury nothing.

## What I shipped ✅
- 📲 LinkedIn post — "Why I'm building in public" → [link]
- **Watch→ship: 2 watched / 1 shipped**

## Product / validation
- Outlined the n8n template pack (no pre-sale yet).

## What was hard
- Writing the hook took 40 min — felt slow.

## Tomorrow's intent
- Watch "Personal Brand From Scratch 2026" → ship a niche post.
```

At the end of the day this note is the human record; the JSON log is the machine record.

## Weekly report — `<weekly_folder>/Week-of-DD-MM-YY.md` (Monday of the week)

```markdown
---
type: learn-day-weekly
week_of: 2026-06-22
range: "2026-06-22 → 2026-06-28"
scorecard:
  days_logged: 6
  study_days: 5
  posts_shipped: 2          # target: 3
  watched_total: 9
  watch_ship_ratio: "9:2"   # ⚠️ consuming faster than shipping
  streak_best: 3
---

# 🗓️ Weekly Learning Report · Week of 2026-06-22

## 📊 Scorecard
| Metric | This week | Target | |
|--------|-----------|--------|---|
| Study days | 5 | 5 | ✅ |
| Posts shipped | 2 | 3 | ⚠️ |
| Watch→ship | 9 → 2 | ~1:1 | ❌ |
| Best streak | 3 days | — | — |

## 🧠 What you learned
- (synthesis across the week, in your own takeaways — themes, not a list dump)

## ✅ What's working
- (specific, evidence-backed wins — "you shipped 2 hook-led posts and both beat your baseline")

## ⚠️ Where you're going wrong
- (the honest section — cite numbers. e.g. "You watched 9 things and shipped 2 posts.
  You're consuming, not doing — the watch→ship loop is broken. 5 of the 9 videos
  produced no post.")
- (drift / focus / product / validation gaps — see learning.md §3)

## 🎯 Fix next week (1–3)
1. (small, measurable — "ship before you watch the next video: 1 post per video, no exceptions")
2. ...

## ▶️ The one thing
- (single highest-leverage move for next week)
```

## Profile — `<state-root>/profile.md` (written at Setup)

```markdown
---
configured: true
vault_path: "C:/path/to/your/Obsidian Vault"
learning_folder: "Learning Journal"        # daily notes go here (inside vault)
weekly_folder: "Learning Journal/Weekly"   # weekly reports go here
daily_note_format: "Learn-DD-MM-YY(ddd)"
report_day: "Saturday"
weekly_targets: { posts: 3, study_days: 5 }
tracks:
  - Personal Brand
  - Copywriting
  - Digital Product (n8n/AI automation)
  - Scaling SaaS
goal: "Build a personal brand + sell an n8n/AI automation digital product"
timeline: "first signals ~90 days, first sales ~6 months"
curriculum_doc: "Desktop/Learning-Hub/Personal-Brand-and-SaaS-Learning-Hub.md"
---

# Profile
Set once at Setup. The skill reads this every run. Edit by re-running `/learn-day setup` or by hand.
```

## Daily log — `<state-root>/logs/YYYY-MM-DD.json`

```json
{
  "date": "2026-06-23",
  "tracks": ["Personal Brand", "Copywriting"],
  "studied": [
    { "item": "Dan Koe — One-Person Business 2026", "kind": "video", "track": "Personal Brand" },
    { "item": "Hook-Story-Offer framework", "kind": "article", "track": "Copywriting" }
  ],
  "watched": 2,
  "shipped": [
    {
      "artifact_id": "post-linkedin-20260623-3a15c8c649d2",
      "type": "post",
      "platform": "LinkedIn",
      "status": "published",
      "topic": "Why I'm building in public",
      "hook": "I stopped hiding the unfinished version.",
      "url": null,
      "source_ref": "learn-day:2026-06-23:building-in-public",
      "created_at": "2026-06-23T10:00:00+05:30",
      "scheduled_at": null,
      "published_at": "2026-06-23T18:30:00+05:30",
      "updated_at": "2026-06-23T18:30:00+05:30"
    }
  ],
  "product_progress": "Outlined the n8n template pack",
  "hard": "Hook writing took 40 min",
  "streak_days": 3
}
```

Use the same artifact schema as `learn-post`. Allowed status values are
`draft`, `scheduled`, and `published`. Only unique `artifact_id` values with
`status: published` count as shipped or extend the shipping streak. Upsert by
`artifact_id`, then `source_ref`; never increment counters blindly.
