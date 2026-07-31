# Self-Learning Loop

The skill gets smarter every week. Reality is logged daily, distilled into `LEARNINGS.md`, and fed back into both the daily questions and the weekly diagnosis. Goal: continuously sharpen the coaching and catch failure modes earlier — always pushing the user forward.

## The loop

```
Log daily (capture studied + shipped) → live the week → Weekly Report (diagnose)
       ▲                                                         │
       └──────────────── distill into LEARNINGS.md ◀─────────────┘
```

## 1. Log reality (every Log)

Upsert `<state-root>/logs/YYYY-MM-DD.json` using the shape in `templates.md`.
The configured consumption and creation metrics matter most; everything else is
context. Never store runtime logs in the installed skill directory.

## 2. Distill into LEARNINGS.md

Maintain a small set of durable, evidence-backed insights about *how this user learns and where they slip*. For each: the pattern, the evidence count, how to apply it.

Categories to maintain:
- **Consistency** — shipping cadence vs target. ("Ships ~2 posts/wk, target 3 — Mon/Tue strong, fades by Thu.")
- **Watch→ship gap** — the consumption-vs-action ratio over time. ("Watches 4–5/wk but only ships 1–2 — chronic over-consumption.")
- **Focus** — drift from the committed plan. ("Said LinkedIn-only; drifted to YouTube editing 2 weeks running.")
- **Friction points** — what consistently stalls them. ("Hook-writing takes 40+ min and kills momentum — needs a swipe-file shortcut.")
- **Energy/timing** — when learning + shipping actually happen. ("Posts that ship are written in the 13:00–18:00 window; evening study rarely converts.")
- **Product** — movement toward building/validating/selling. ("3 weeks of learning, 0 product steps — stuck in input mode.")

Update rules:
- Strengthen an insight when new evidence agrees (bump the count).
- Revise/soften when evidence contradicts; retire insights stale 2+ weeks.
- Require ≥3 supporting days before treating something as a firm rule; below that mark it `tentative`.

## 3. Weekly diagnosis — the failure-mode checklist

This is the heart of the "where you're going wrong" section. Run every item against the week's logs and call out the ones that fire, **with the numbers**:

1. **Consuming, not doing** — consumption materially exceeds the configured creation target. *"9 study units, 2 shipped artifacts — creation is not keeping pace this week."*
2. **Under the posting target** — posts_shipped < weekly_targets.posts. *"2 of 3 — the algorithm and the habit both need the 3rd."*
3. **Broken streak / front-loading** — ships early then fades. *"Shipped Mon–Wed, nothing Thu–Sun — consistency, not intensity, wins."*
4. **Focus drift / pivoting** — work logged outside the committed track/platform. *"You committed to LinkedIn + one niche — 3 days went elsewhere. Pivoting is the progress-killer."*
5. **No applied progress** — zero configured build, practice, validation, or shipping steps for the week.
6. **No validation-with-money** — building without a single pre-sell/demand test. *"Opinions aren't validation — test with a pre-order."*
7. **Avoiding the hard track** — one track (often Scaling SaaS or Copywriting reps) consistently untouched. *"Copywriting got 0 reps again — it's the skill under everything."*
8. **Passive logging** — days logged but thin (no takeaway, no ship). *"Showing up isn't the same as moving."*

Only fire what the evidence supports. Two or three sharp, true callouts beat a long list. Always pair each with the fix in the next section.

## 4. Suggest improvements (every Weekly Report)

Turn the fired failure modes into **1–3 concrete, measurable fixes** for next week. Small and specific beats ambitious and vague:
- *"Rule: ship the post BEFORE the next video. 1 post per video consumed."*
- *"Pre-write 3 hooks Sunday night from your swipe file so Mon–Wed posts are 10-min jobs."*
- *"This week: one product step — record the Loom and list the Gumroad draft, even unfinished."*
- *"Protect the 3rd post: put a Thu and Sat post slot in your work window."*

## 5. Reinforce the plan

Tie the report back to the profile's curriculum, north-star behavior, focus
constraints, and success measures. The weekly read should catch drift from the
user's chosen path without hard-coding a creator, platform, or business model.

## Tone guardrails

- **Honest, not harsh.** The user asked to be told where they're going wrong — deliver it, with evidence, framed as the fix.
- Push forward, never backward. Every slip becomes a next step.
- Be specific ("5 of 9 videos produced no post"), never preachy.
- The user owns the call — fixes are offers, not mandates. End with momentum.
