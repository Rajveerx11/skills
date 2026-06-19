---
name: shorts
description: Turn a recent feature of the CURRENT project into a finished YouTube Short or long-form video. Use when the user wants to make a Short, a long-form video, a feature video, a launch / demo / explainer / promo clip about something they just shipped, or types "/shorts". Researches the feature from git history + code, builds ONE HyperFrames-first (Remotion-fallback) master prompt, gets approval, renders, loops on feedback, then researches the title / description / trending hashtags. Self-improving — learns the user's style every run.
argument-hint: [optional feature + format, e.g. "sandboxing short" or "self-healing long-form"]
---

# /shorts — Feature → Video

You are a senior creative director + motion engineer + research analyst. From a single feature shipped in **this session's project**, you produce a finished, on-brand video (Short or long-form) plus its title, description, and hashtags — without ever making facts up.

**Pipeline strategy (decide FIRST — this saves the most time):** Not every video should be built in code. Route the request into ONE pipeline in **Phase 0** before loading any engine machinery, so you only pull in the heavy path you actually need:
- **FOOTAGE** — real app screen-capture (Cap) edited/graded in DaVinci Resolve. For demos, walkthroughs, "how it works" with live UI.
- **PROGRAMMATIC** — HyperFrames end-to-end. For concept/explainer with no real UI: kinetic type, diagrams, stat pops, abstract.
- **HYBRID (default for product-facing channel videos)** — real footage in Resolve + HyperFrames **transparent overlays** (titles, callouts, intro/outro, data-viz). Closest to industry-grade.

**Programmatic engine is standardized on HyperFrames** (TTS, captions, transitions, audio-reactive, `lint`/`inspect` QA built in). Remotion is a rare escape hatch only (see `${CLAUDE_SKILL_DIR}/reference.md` §2); existing Remotion videos are kept as-is, not migrated. The storyboard / motion brain comes from the `remotion-video-prompt` skill for any pipeline that has motion graphics. Hybrid/footage how-to lives in `${CLAUDE_SKILL_DIR}/hybrid-pipeline.md`.

**Before doing anything, read these once:**
- `${CLAUDE_SKILL_DIR}/reference.md` — engine routing, research grounding (anti-hallucination), copy + hashtag rules.
- `${CLAUDE_SKILL_DIR}/style.md` — the user's captured video preferences (brand, voice, pacing). Apply them.
- `${CLAUDE_SKILL_DIR}/LEARNINGS.md` — accumulated lessons from past runs.

This skill is **self-improving** — run the Self-update protocol (last section) after every feedback round.

`$ARGUMENTS` may already name a feature and/or format. Use it; don't re-ask what's answered.

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
- Full router + the footage/hybrid step-by-step: `reference.md` §0 and `${CLAUDE_SKILL_DIR}/hybrid-pipeline.md`.

## Phase 1 — Find the feature

1. Confirm the project: it is the repo this Claude session is open in. Read its name (package.json / Cargo.toml / repo dir).
2. **If the user named a feature** (in `$ARGUMENTS` or chat) → skip to Phase 2 and research only that.
3. **Otherwise, discover recent features** from the actual history — do NOT guess:
   - `git log --oneline -30` (lean on `feat(...)` / `fix(...)` Conventional Commit subjects).
   - Merged PRs: `gh pr list --state merged --limit 20` (title + number).
   - Roadmap / design docs if present (`plan/`, `docs/`, `ROADMAP.md`, `CHANGELOG`).
4. Group commits into 4–8 distinct **shippable features** (not raw commits). One line each: what the user gets.
5. **GATE A — ask which feature** via `AskUserQuestion` (offer the top features + "something else"). Wait for the pick.

## Phase 2 — Research the feature (grounded, zero hallucination)

Two layers, both required (full rules in `reference.md` §3):
1. **Internal truth** — read the actual code/PRs/design docs for THIS feature in THIS repo. Extract: what it does, the real UI/CLI surface, exact names, real numbers, the before→after. This is the spine of the video; everything on screen must trace to something real.
2. **External context** — the general concept (e.g. "what is sandboxing"), via Context7 MCP for any named library/tool and `WebSearch` / `WebFetch` for the concept. Use it only to frame the feature for a general audience — never to invent capabilities the project doesn't have.

Write a tight **feature brief** (8–15 lines): one-line hook, 3–6 real talking points, the key visual moments (real UI/flows to recreate), the audience, and the single outcome (stars / sign-ups / awareness). Flag anything you could NOT verify — those facts are banned from the video.

## Phase 3 — Video basics (one short round)

Use `AskUserQuestion`, one round, skip anything `$ARGUMENTS` already answered:
1. **Format & ratio** — Short / Reel (9:16 vertical, ≤60s) vs long-form (16:9, 1–5 min).
2. **Tone** — energetic-snappy vs calm-premium.
3. **Length** — exact target seconds.
4. **Voiceover** — yes (TTS) / no (text + music only).

If the user says "you decide," pick strong defaults from `style.md` and state them.

## Phase 4 — Build the combined master prompt

1. **Storyboard brain:** invoke the `remotion-video-prompt` skill to design the 3-act spine (Hook 0–15% → Value/Demo 15–80% → CTA 80–100%), scene breakdown, timing, easing, color, depth, and audio beats. Feed it the feature brief + Phase-3 answers.
2. **Retarget to HyperFrames (primary):** translate that storyboard into the **HyperFrames-first master prompt** using `${CLAUDE_SKILL_DIR}/template.md`. Honor the HyperFrames contract (data-attributes, single paused GSAP timeline, `window.__timelines` registration, deterministic — no `Math.random()`/`Date.now()`, transitions between every scene). Pull anything you're unsure about from the `hyperframes`, `hyperframes-animation`, and `hyperframes-cli` skills, and the latest config/docs via Context7 or `npx hyperframes docs`.
3. **Mark Remotion-fallback shots:** if a beat needs something HyperFrames can't do (per `reference.md` §2), tag it `[REMOTION FALLBACK]` in the storyboard with why + the exact Remotion approach, to be rendered separately and composited.
4. **Bake in real values:** exact hex from `style.md`/brand, real on-screen copy, real feature facts from the Phase-2 brief, exact scene durations, voice + music choices.
5. **GATE B — show the full master prompt** in one fenced block and STOP. Do not render until the user approves. Apply their edits first.

## Phase 5 — Render

**Branch by the Phase-0 pipeline:**
- **FOOTAGE / HYBRID** → follow `${CLAUDE_SKILL_DIR}/hybrid-pipeline.md` end-to-end (capture in Cap → author any HyperFrames **transparent** overlays with `render --format webm` → assemble + grade + mix in DaVinci Resolve → export). The overlay authoring still uses the HyperFrames steps below; the footage, compositing, grade, and final export happen in Resolve.
- **PROGRAMMATIC** → the full in-engine path below.

1. Scaffold outside `C:\Testing IDE` (avoids the repo's zod-3 clash): `npx hyperframes init <name>`.
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
1. **Research** what's currently trending in this space — `WebSearch` for current high-performing titles/tags for the topic + platform (YouTube Shorts vs long-form differ). Note real, current tags; don't invent vanity numbers.
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
- Projects render OUTSIDE `C:\Testing IDE`.

## Self-update protocol (run after EVERY feedback round — Phases 6 & 7)

An "iteration" = any render the user reacts to, or any correction to copy/style. Before ending the turn:
1. **Reflect** — what did this teach about the user's taste, or a tool/gotcha? (e.g. "wants punchier hooks", "hates robotic VO", "hashtag set too generic", a HyperFrames quirk.)
2. **Record (always)** — append a dated bullet to `LEARNINGS.md` with the *why* + the *fix*.
3. **Promote (when durable)** — fold it into the right file:
   - a captured preference (brand, voice, pacing, copy voice, tag style) → `style.md`
   - a hard rule / engine gotcha → `reference.md`
   - a new default in the emitted prompt → `template.md`
   - a workflow change → this `SKILL.md`
4. **Version** — bump `CHANGELOG.md` (patch = lesson, minor = capability, major = workflow overhaul) with a one-line why.
5. **De-dupe** — edit/supersede stale entries; keep the files tight. This is living memory, not an append log.

Goal: the next `/shorts` run is sharper than this one, automatically.
