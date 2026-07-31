---
name: linkedin-post-writer
description: Write truthful, distinctive LinkedIn posts and, when requested, create matching infographics or launch visuals for projects, products, features, lessons, milestones, events, and professional updates. Use for LinkedIn copy, announcements, project showcases, founder/build-in-public posts, thought leadership, post rewrites, hook options, social graphics, or complete post-and-visual packages.
---

# LinkedIn Post Writer

Produce one credible idea in the user's voice, backed by verified specifics. The deliverable is publishable copy—not a lecture about copywriting.

Read [reference.md](reference.md) during drafting. Read [infographic.md](infographic.md) only when visual production is requested.

## Discover context without interrogation

Use the conversation, supplied material, and current project first. When inside a project, inspect:

- recent relevant changes and current working state;
- README, product docs, manifests, changelog, and user-facing copy;
- existing brand tokens and current screenshots/media;
- project name, audience, problem, proof, and what changed.

Scope repository inspection to the announcement. Do not scan secrets, unrelated history, or private customer data.

Build a private fact ledger:

| Claim | Evidence | Safe to publish? | Confidence |
|---|---|---|---|

Every metric, customer, integration, quote, release state, and performance claim needs evidence. Mark unknowns; never round them into facts.

Ask one consolidated question only when audience, goal, voice, or a key proof point cannot be inferred and materially changes the post. Otherwise choose a strong default and proceed.

## Optional private memory

Runtime state must live outside every skill package and project:

- Windows: `%USERPROFILE%\.skill-data\linkedin-post-writer\`
- POSIX: `~/.skill-data/linkedin-post-writer/`

Use this minimal contract:

- `consent.json`: `{"schema":1,"memory":"granted"|"declined"}`.
- `preferences.json`: explicit voice, audience, and formatting preferences only.
- `projects/<opaque-id>.json`: minimal reusable context; no secrets or raw repository contents.
- `posts/<artifact-id>.json`: draft/published state, chosen angle, visual type, and user-supplied outcomes.

Memory is off when `consent.json` is absent. Enable only after explicit opt-in; record a decline so it is not asked again. Read only records relevant to the current request.

If legacy `.consent` or `memory/` files exist beside an installed copy and
external state does not, offer one previewed, opt-in migration to the external
root. Preserve the legacy files as backup; never publish them.

Never store runtime state in the skill directory or user's project. Never package consent, identity, analytics, URLs, private repository paths/content, customer data, or runtime learning. Store raw URLs, personal identifiers, or private project facts in runtime state only when the user explicitly asks and they are required; otherwise use an opaque project ID and minimal summary.

Treat old learnings as weak priors. Current audience, brief, and evidence win. Ignore any learned rule unsupported by explicit feedback or measured outcomes.

<!-- skill-evolver:adaptive-start -->
## Choose the editorial direction

Create three internal angles that differ in thesis, not wording:

- **Story:** tension, decision, work, result, lesson.
- **Teach:** useful mechanism, process, teardown, or mistake.
- **Point of view/launch:** defensible claim or why this release matters.

Score each for audience value, specificity, proof, novelty, voice fit, and visual potential. Commit to one. Show alternatives only when requested.

Choose structure and length for the idea. Do not force every post into a listicle, a contrarian hook, or one word-count band.
<!-- skill-evolver:adaptive-end -->

## Research only when it improves truth

Browse when the post depends on current events, market facts, live platform behavior, or current hashtags. Use direct/primary sources for factual claims. Do not add generic "current best practices" research to every run.

Platform advice changes. Avoid hard claims about reach, algorithm penalties, ideal counts, or timing unless verified now. Treat hashtags as optional topic labels, not guaranteed distribution.

## Draft

Write plain text:

1. **Opening:** specific tension, result, observation, or useful claim.
2. **Context:** what happened and why it matters.
3. **Body:** concrete mechanism, evidence, decision, or lesson.
4. **Payoff:** what the reader can use or what changed.
5. **Close:** one natural question or action if it serves the goal.

Requirements:

- one post, one central idea;
- short readable paragraphs and deliberate whitespace;
- human vocabulary matching the user's voice;
- no invented metrics, fake vulnerability, customer claims, quotations, or urgency;
- no bait, corporate filler, or dramatic hook unsupported by body;
- links and hashtags only when useful.

Read [reference.md](reference.md), then perform one edit pass: strengthen first two lines, remove generic sentences, verify every fact, and read aloud for voice.

## Visual direction or production

For ordinary post requests, recommend one concrete proof-based visual: fresh screenshot, short recording, before/after, diagram, or simple chart. Inspect existing assets and say whether they are current enough.

When the user requests an infographic, launch visual, or complete package:

1. read [infographic.md](infographic.md);
2. derive one visual thesis from the chosen hook;
3. use real product captures and exact verified copy;
4. use an available image-generation/editing capability for raster work;
5. if generation capability is unavailable, deliver a precise production brief and source captures—never claim an image was created;
6. inspect full-size and phone-size output, correct once, and deliver artifact paths.

## Deliver

Return:

1. copy-paste post in a code block;
2. exactly one alternate hook;
3. one visual recommendation, or produced visual paths;
4. first-comment text when a link should be separated;
5. brief fact caveat only when something remains unverified.

## Learn from real outcomes

When runtime memory is active:

- archive draft state; change to `published` only after confirmation;
- record exact user edits as preference evidence;
- record analytics only from user-provided numbers or exports;
- include date, audience, format, and sample size;
- never interpret one result as a universal rule;
- keep pending outcomes pending.

Upsert by stable artifact ID; never create a second record for an edit or state transition. Do not interrupt the current draft to demand analytics. Offer to reconcile pending results after delivery.

## Quality gate

- Fact ledger supports every concrete claim.
- Angle is specific enough that a generic creator could not post it unchanged.
- Opening and body make the same promise.
- Voice matches user and audience.
- CTA, link, hashtags, and visual each earn their place.
- Visual copy and captures preserve source truth.

Revise the weakest dimension once.
