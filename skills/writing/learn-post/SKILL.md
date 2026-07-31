---
name: learn-post
description: Turn today's real learning or shipped work into an authentic build-in-public LinkedIn post, then optionally log the confirmed draft or publication into the user's learn-day system. Use for "/learn-post", "write a LinkedIn post about what I learned", "turn today's learning into a post", or "ship today's learning". Produces grounded copy, one alternate hook, and a specific visual direction without inventing results.
---

# Learn Post

Turn one real learning into one useful, human post. Reduce ceremony: discover today's context, choose the strongest angle, write the post, then offer an idempotent log update.

## Resolve companion context

Use the current conversation and explicit arguments first. If needed, discover the installed `learn-day` and `linkedin-post-writer` skills from the active skill catalog or user-owned global skill roots. Do not hardcode `.claude` paths when a loaded skill directory or catalog entry is available.

Read:

- `learn-day` profile/config only to locate the vault, learning folder, tracks, goal, and voice;
- today's note using the current local date and the configured naming pattern;
- the LinkedIn writing reference during drafting, if installed.

Never search unrelated vault notes or private files. If no companion skill/profile exists, continue from user-provided context rather than blocking.

## Build a fact ledger

Extract:

- what was studied, built, tested, or changed;
- the moment of confusion, surprise, failure, or breakthrough;
- concrete proof: code, screenshot, result, before/after, or source;
- why it matters to the user's actual audience;
- facts safe to publish versus private details.

Mark uncertain facts and omit them. Never invent metrics, duration, quotes, customers, or emotional stakes.

If neither arguments nor today's note contains enough substance, ask one question: what did you learn or ship today, in messy form?

<!-- skill-evolver:adaptive-start -->
## Choose the angle

Create three internal angles:

- **Teach:** explain one useful mechanism or practice.
- **Build in public:** show the real attempt, friction, and result.
- **Point of view:** make a defensible claim learned from the work.

Score them for specificity, audience value, proof, novelty, and authenticity. Choose one. Do not make the user select unless two angles remain tied or they explicitly ask for variants.
<!-- skill-evolver:adaptive-end -->

## Write

Use a structure that fits the chosen angle rather than a fixed template:

1. first one or two lines earn attention with a specific tension, result, or insight;
2. context establishes why this mattered;
3. body teaches or reveals the concrete mechanism;
4. payoff states what changed in the user's thinking or practice;
5. one natural closing question or action, only when it adds value.

Keep plain text suitable for LinkedIn. Use whitespace for rhythm. Avoid corporate filler, fake vulnerability, generic motivational lessons, bait, and inflated claims. Length follows the idea; remove any line that does not advance it.

Current platform tactics change. Research them only when the user asks for current optimization or when making time-sensitive claims about LinkedIn behavior. Prefer official/platform sources and label uncertainty.

## Deliver

Return:

1. copy-paste post in a code block;
2. exactly one alternate hook;
3. one specific visual recommendation tied to the hook;
4. optional first-comment text if an outbound link belongs there.

Use an existing screenshot, diagram, or short screen recording when it proves the learning. Do not recommend generic quote cards when real evidence exists.

## Log safely

Logging is a separate write action. Offer it after delivering; never make posting or publication implicit.

Use one shared artifact record in the learn-day note and daily JSON:

```yaml
artifact_id: post-linkedin-YYYYMMDD-<12-char-hash>
type: post
platform: LinkedIn
status: draft
topic: "short stable topic"
hook: "current first line"
url: null
source_ref: "learn-day:YYYY-MM-DD:<stable-topic-seed>"
created_at: "ISO-8601 timestamp"
scheduled_at: null
published_at: null
updated_at: "ISO-8601 timestamp"
```

Allowed `status`: `draft`, `scheduled`, `published`. Unknown timestamps and URL stay `null`, never empty strings or fabricated values.

Generate `artifact_id` once from SHA-256 of `lowercase platform + "\n" + YYYY-MM-DD + "\n" + source_ref`, using the first 12 lowercase hexadecimal characters. Prefer the source note's durable learning/topic ID in `source_ref`; otherwise normalize the original topic seed once. Hook edits, scheduling, publication, URL updates, and metric updates must reuse the existing `artifact_id`.

Only `published` counts toward `watch_ship.shipped` and streaks by default. Draft and scheduled records remain visible pipeline artifacts but do not count as shipped. Changing an existing published record back to a non-published state requires explicit confirmation because counts may decrease.

If the user confirms:

1. re-read today's note before editing;
2. find an existing record by `artifact_id`, then `source_ref`; never use mutable hook text as primary identity;
3. upsert one schema-identical record in note frontmatter and daily JSON;
4. preserve `created_at`; update only changed fields and `updated_at`;
5. add a human-readable line under "What I shipped" only when status becomes `published`; keep draft/scheduled items in the template's content-pipeline section;
6. recompute counts from unique published artifact IDs rather than incrementing blindly;
7. preserve unknown URL and metrics as `null`/pending, never zero;
8. verify both stores contain one matching record and counts agree.

If today's note does not exist, use `learn-day` to create the normal note or ask permission before creating a minimal one. Report exact files changed and final state.

## Quality gate

- Every concrete claim traces to today's note, supplied context, artifact, or source.
- Post contains one idea and at least one detail only this user could credibly say.
- Hook and body make the same promise.
- Voice sounds like the user, not a creator template.
- Visual proves or explains the idea.
- Draft, scheduled, and published states remain distinct.
- Re-running logging upserts one stable artifact record; only published records count.

Revise the weakest dimension once before delivery.
