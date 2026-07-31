---
name: shorts
description: >
  Turn a recent feature of the current project into a finished YouTube Short
  or long-form channel video plus publishing metadata. Use when the user
  explicitly asks for a YouTube Short, types "/shorts", or wants a video about
  something shipped in the current project. This route takes precedence for an
  explicit YouTube Short or current-project feature request even when the user
  also says launch, reveal, demo, or promo. For a general product/company/site
  marketing launch or promo not anchored to the current project or YouTube
  channel output, use product-launch-video.
---

# /shorts — Feature → Video

You are a senior creative director + motion engineer + research analyst. From a single feature shipped in **this session's project**, you produce a finished, on-brand video (Short or long-form) plus its title, description, and hashtags — without ever making facts up.

**Route boundary:** Explicit YouTube Short and current-project feature-video
requests stay in `/shorts`, including launch/reveal/demo/promo wording. A
general product, company, SaaS, app, or site marketing launch/promo without
that current-project or YouTube-channel anchor routes to
`/product-launch-video`.

**Pipeline strategy (decide FIRST — this saves the most time):** Not every video should be built in code. Route the request into ONE pipeline in **Phase 0** before loading any engine machinery, so you only pull in the heavy path you actually need:
- **FOOTAGE** — real app screen-capture (Cap) edited/graded in DaVinci Resolve. For demos, walkthroughs, "how it works" with live UI.
- **PROGRAMMATIC** — HyperFrames end-to-end. For concept/explainer with no real UI: kinetic type, diagrams, stat pops, abstract.
- **HYBRID (default for product-facing channel videos)** — real footage in Resolve + HyperFrames **transparent overlays** (titles, callouts, intro/outro, data-viz). Closest to industry-grade.

**Programmatic engine is standardized on HyperFrames** (TTS, captions, transitions, audio-reactive, `lint`/`inspect` QA built in). Remotion is a rare escape hatch only (see [reference.md](reference.md) §2); existing Remotion videos are kept as-is, not migrated. The storyboard / motion brain comes from the `remotion-video-prompt` skill for any pipeline that has motion graphics. Hybrid/footage guidance lives in [hybrid-pipeline.md](hybrid-pipeline.md).

**Before doing anything, resolve this skill's directory from host-provided skill metadata, then read:**
- [reference.md](reference.md) — engine routing, research grounding, copy, and hashtag rules.
- [style.md](style.md) — private preference-state schema and portable baseline.
- Private state when present: `%USERPROFILE%\.skill-data\shorts\preferences.md` on Windows or `~/.skill-data/shorts/preferences.md` on macOS/Linux. Never commit or echo private state.

If a legacy `LEARNINGS.md`, `history/`, or `memory/` exists beside an installed
copy and external state does not, offer one previewed, opt-in migration. Keep
the legacy files as backup and excluded runtime state.

Reviewed outcomes may improve future runs through the evidence-gated protocol below; runtime feedback does not authorize silent skill rewrites.

The current request may already name a feature or format. Use it; do not re-ask answered details.

---

## Phase 0 — Route the pipeline (do this before anything else)

Classify the requested video into ONE pipeline. This decides which skills you even load.

| If the video is mostly… | Pipeline | What carries it |
|---|---|---|
| Showing the REAL app working — demo, walkthrough, feature reveal, "how it works" with live UI | **FOOTAGE** | Cap screen-capture → DaVinci Resolve edit/grade/mix |
| Concept / explainer with NO real UI needed — kinetic type, diagrams, stat pops, abstract | **PROGRAMMATIC** | HyperFrames end-to-end |
| A product promo wanting credibility AND polish (most YouTube-channel videos) | **HYBRID** | Real footage in Resolve + HyperFrames transparent overlays |

- **Default to HYBRID** for product-facing channel content — it is the closest to industry-grade SaaS video.
- **Only load the chosen path's skills.** PROGRAMMATIC/HYBRID → `hyperframes*` skills. FOOTAGE → skip them; follow `hybrid-pipeline.md`. This is the time-saver — don't spin up the full HyperFrames build for a video that should be footage-led.
- State your pipeline choice; fold a confirm into GATE A only if it's genuinely ambiguous.
- Full router + footage/hybrid steps: [reference.md](reference.md) §0 and [hybrid-pipeline.md](hybrid-pipeline.md).

## Phase 1 — Find the feature

1. Confirm the project: it is the repo this Claude session is open in. Read its name (package.json / Cargo.toml / repo dir).
2. **If the user named a feature in the current request** → skip to Phase 2 and research only that.
3. **Otherwise, discover recent features** from the actual history — do NOT guess:
   - `git log --oneline -30` (lean on `feat(...)` / `fix(...)` Conventional Commit subjects).
   - Merged PRs: `gh pr list --state merged --limit 20` (title + number).
   - Roadmap / design docs if present (`plan/`, `docs/`, `ROADMAP.md`, `CHANGELOG`).
4. Group commits into 4–8 distinct **shippable features** (not raw commits). One line each: what the user gets.
5. **GATE A — ask which feature** through the host's normal user-input mechanism (offer the top features + "something else"). Wait for the pick.

## Phase 2 — Research the feature (grounded, zero hallucination)

Two layers, both required (full rules in `reference.md` §3):
1. **Internal truth** — read the actual code/PRs/design docs for THIS feature in THIS repo. Extract: what it does, the real UI/CLI surface, exact names, real numbers, the before→after. This is the spine of the video; everything on screen must trace to something real.
2. **External context** — use available official-documentation lookup for named libraries/tools and the host's current web-research capability for general concepts. Use it only to frame the feature for a general audience — never to invent project capabilities.

Write a tight **feature brief** (8–15 lines): one-line hook, 3–6 real talking points, the key visual moments (real UI/flows to recreate), the audience, and the single outcome (stars / sign-ups / awareness). Flag anything you could NOT verify — those facts are banned from the video.

## Phase 3 — Video basics (one short round)

Use the host's normal user-input mechanism for at most one round; skip anything the current request already answered:
1. **Format & ratio** — Short / Reel (9:16 vertical, ≤60s) vs long-form (16:9, 1–5 min).
2. **Tone** — energetic-snappy vs calm-premium.
3. **Length** — exact target seconds.
4. **Voiceover** — yes (TTS) / no (text + music only).

If the user says "you decide," pick strong defaults from `style.md` and state them.

## Phase 4 — Build the combined master prompt

1. **Storyboard brain:** invoke the `remotion-video-prompt` skill to design the 3-act spine (Hook 0–15% → Value/Demo 15–80% → CTA 80–100%), scene breakdown, timing, easing, color, depth, and audio beats. Feed it the feature brief + Phase-3 answers.
2. **Retarget to HyperFrames (primary):** translate that storyboard into the **HyperFrames-first master prompt** using [template.md](template.md). Honor the HyperFrames contract (data attributes, single paused GSAP timeline, `window.__timelines` registration, deterministic — no `Math.random()`/`Date.now()`, transitions between every scene). Resolve uncertainties from the `hyperframes`, `hyperframes-animation`, and `hyperframes-cli` skills plus available official documentation or `npx hyperframes docs`.
3. **Mark Remotion-fallback shots:** if a beat needs something HyperFrames can't do (per `reference.md` §2), tag it `[REMOTION FALLBACK]` in the storyboard with why + the exact Remotion approach, to be rendered separately and composited.
4. **Bake in real values:** exact hex from `style.md`/brand, real on-screen copy, real feature facts from the Phase-2 brief, exact scene durations, voice + music choices.
5. **GATE B — show the full master prompt** in one fenced block and STOP. Do not render until the user approves. Apply their edits first.

## Phase 5 — Render

**Branch by the Phase-0 pipeline:**
- **FOOTAGE / HYBRID** → follow [hybrid-pipeline.md](hybrid-pipeline.md) end-to-end (capture in Cap → author any HyperFrames **transparent** overlays with `render --format webm` → assemble + grade + mix in DaVinci Resolve → export). Overlay authoring still uses the HyperFrames steps below; footage, compositing, grade, and final export happen in Resolve.
- **PROGRAMMATIC** → the full in-engine path below.

1. Scaffold in an isolated project directory when the current parent repository hoists conflicting video-tool dependencies: `npx hyperframes init <name>`.
2. Build the composition per the approved prompt. Generate audio via the `hyperframes-media` skill (`npx hyperframes tts` for VO; BGM as specified).
3. Verify before serving: `npx hyperframes lint` → `npx hyperframes inspect` → fix findings. Preview, then `npx hyperframes render --quality high`.
4. For any `[REMOTION FALLBACK]` shot, build that clip with the `remotion-video-prompt` flow and composite it in (ffmpeg) — see `reference.md` §2.
5. Hand back the actual MP4 path + open it for the user.

## Phase 6 — Feedback loop

Show the video. The user reviews. For every change requested:
1. Apply it, re-lint/inspect/render, deliver again.
2. **Run the Self-update protocol** (below) on what the change taught you about their taste.
3. Repeat until the user says "final."

## Phase 7 — Title, description, hashtags (researched, no hallucination)

Only after "final" (rules in `reference.md` §4):
1. **Research** current high-performing titles and tags for the topic and platform using the host's web-research capability. Note real, current tags; do not invent vanity numbers.
2. Draft, grounded only in the verified feature brief:
   - **Title** — platform-appropriate, accurate, hooky (no clickbait the video doesn't deliver).
   - **Description** — what it is, the real value, real links (repo, site), then tags.
   - **Hashtags** — a researched mix of broad + niche tags actually used in this space now.
3. **GATE D — show all three** for approval. Apply edits. Then run the Self-update protocol on any copy corrections.

## Phase 8 — Deliver

Final MP4 path + approved title/description/hashtags in one copy-paste block. Confirm self-learning files were updated this run.

---

## Guardrails
- **Never state a feature fact you didn't verify in the repo.** Unverifiable → cut it. (`reference.md` §3.)
- Two hard stops: GATE B (prompt) before any render, GATE D (copy) before final. Plus GATE A if the feature is ambiguous.
- One question per round-trip batch; don't interrogate.
- HyperFrames is primary; reach for Remotion only by the §2 criteria, and say why when you do.
- Use an isolated project directory when a parent repository's hoisted dependencies conflict with the selected video toolchain.

## Evidence-gated improvement

1. Record only explicit preference, reproduced failure, reviewer correction, or measured publishing result through `skill-evolver`; ordinary completion and silence are not evidence.
2. Keep user-specific style preferences private. Promote a correctness guardrail after one reproduced defect; promote a quality default after two consistent outcomes or one strong measured result.
3. Apply the smallest supported change to `style.md`, `reference.md`, `template.md`, or `SKILL.md`, then forward-test a realistic feature brief.
4. Keep runtime evidence under `%USERPROFILE%\.skill-data\shorts\` or `~/.skill-data/shorts/`; never write it into the skill repository.
5. De-duplicate or supersede stale private guidance; never append contradictory folklore.

<!-- skill-evolver:adaptive-start -->
## Professional execution

- **Discover automatically:** inspect current branch/diff/log, relevant code/tests/docs, existing captures/renders, brand/style memory, platform hints, and available editing/render tools. Build a feature fact ledger before choosing the story.
- **Default intelligently:** route once; use HYBRID for product-facing demos when real UI is available, PROGRAMMATIC for concepts, FOOTAGE for walkthroughs. Default to vertical 9:16 and concise Short pacing only when the destination is unspecified and the request clearly implies short-form.
- **Reduce human coordination:** ask one compact round only for material feature, destination, audience, access, voice, or CTA choices. Infer engine mechanics, shot count, and safe stylistic defaults from evidence.
- **Resume safely:** checkpoint feature ledger, route, prompt/storyboard, captures/assets, project/render state, review notes, and publishing package. Reuse only artifacts tied to the current source commit and approved style.
- **Protect contracts:** do not invent features, metrics, quotes, UI, trends, or hashtags; preserve rights, brand, source truth, seekable footage, audio sync, and engine-specific validation. Research publishing metadata only after content is locked.
- **Finish the handoff:** deliver final video and metadata, source commit/feature evidence, route and asset ledger, title/description/hashtags with sources where searched, validation results, and remaining manual publishing action.
- **Learn only from evidence:** record controlled retention results, explicit style approval, and reproduced render corrections through `skill-evolver`; never append generic lessons after every run.
<!-- skill-evolver:adaptive-end -->
