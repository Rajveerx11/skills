# Scheduling Mechanics

How to turn vague tasks + soft anchors into a realistic, time-blocked day.

## Time-blocking algorithm

1. **Lay the anchors first.** Place each soft anchor from the profile at its usual time. These are pegs, not walls — you may slide each within its ± tolerance (default 30–60 min) to remove gaps/overlaps.
2. **Place hard-time items.** Anything the user gave a fixed clock time (meetings, calls) is immovable. Drop these in next.
3. **Fill the gaps with flexible tasks**, ordered by:
   - priority (the user's stated `★top` first),
   - deadline proximity,
   - learned energy windows (e.g. deep work in the user's peak block from `LEARNINGS.md`),
   - dependency/logical order.
4. **Apply learned durations.** Use `LEARNINGS.md` estimates over the user's optimistic guess. If a task historically runs short, block the realistic time and offer to fill the remainder.
5. **Add buffers.** Leave 10–15 min transitions around meetings and between heavy blocks. Don't pack the day wall-to-wall.
6. **Respect working hours.** Don't schedule focus work outside the profile's working hours unless the user asks.

## Soft-anchor rules

- Keep anchors near their usual time; prefer the smallest slide that makes the day fit.
- Never drop an anchor silently. If the day genuinely can't fit one, say so and ask.
- The user can override per day ("no basketball today", "lunch at 1:30") — honor it for that day only; don't change the profile.

## Draft format (what you show the user)

```
08:00–10:00  Basketball            (anchor)
10:00–10:45  Breakfast + rituals   (anchor)
11:00–13:00  Sandbox feature  ★top (event)
13:00–14:00  Lunch                 (anchor)
14:00–15:00  Learn RAG             (event)
15:00–15:30  Call with Aman        (event, fixed)
16:00–17:00  Record LinkedIn video (event)
```

- Mark each line `(anchor)` / `(event)` / `(task)`; add `, fixed` for hard-time items and `★top` for the priority.
- Below the table, surface **0–2 learning-based nudges** (see `learning.md`), phrased as questions.
- End with: "Look good, or want changes?"

## Handling tweaks

Accept plain language and redraft the whole table:
- "push X 30 min", "swap X and Y", "give X 3 hours", "make X a task", "drop Y", "add Z after lunch".
- After each tweak, re-show the full updated timeline so the user sees the knock-on effects.

## Writing on approval (Plan mode)

1. Generate a stable `id` per task (e.g. `kebab-slug` of the title; ensure uniqueness within the day).
2. Write the Obsidian daily note from the template in `templates.md` — checkbox
   list plus frontmatter holding `id`, canonical schedule fields, provider,
   calendar/event ids, synchronization fingerprint, and ownership state.
3. For each block, run `scripts/sync_fingerprint.py` on the provider-neutral
   canonical block, then call the connected calendar create tool (events by
   default). Store provider, calendar id, returned event id, and that
   synchronization fingerprint in managed note frontmatter for the task.
4. Report: `✅ Wrote <note path> → N items` and `✅ Calendar: X events, Y tasks`.

## Re-running Plan for the same day (idempotency)

- Read the existing note's frontmatter first.
- Match tasks by stable `id`. When canonical fingerprint is unchanged, do
  nothing. For changed times/titles, call the provider update tool with stored
  provider, calendar id, and event id. Delete removed events only when
  `sync_owned: true`. Create new tasks once, then persist returned ids.
- Never create a second provider event for a task with a verified event id.

## Wrap mode

1. Read today's note plus `<state-root>/logs/YYYY-MM-DD.json` (create the log if
   absent from the note's planned data).
2. Ask "what got done?" or accept the user's volunteered status. Map answers to tasks by `id`/title.
3. Tick `- [ ]` → `- [x]` in the note for completed items.
4. Fill the log's `actual` fields: completed bool, actual start/end or duration if known, skipped/rolled flags, a one-line note.
5. Stage unfinished tasks for tomorrow (carry title, priority, deadline). Tomorrow's Plan reads this staged list and pre-loads them.
6. Hand off to `learning.md` to update `LEARNINGS.md`. Close with one forward nudge.

## Review mode

- Read the last 7 (or `week`) daily logs.
- Compute: estimation accuracy per task type, completion rate, most-done vs most-skipped focus areas, energy/time-of-day patterns, overcommit days (≥3 rollovers).
- Produce a short growth read (5–8 lines) + **1–2 concrete push-forward suggestions**.
- Offer to fold any stable, confirmed pattern into `profile.md` or `LEARNINGS.md`.
