# /shorts — Reference

Combined knowledge for turning a project feature into a video. Read fully before a run.
This file holds the *decisions*; the heavy how-to lives in the skills it points to
(`remotion-video-prompt`, `hyperframes*`). Don't duplicate them — route to them.

---

## 0. Pipeline router — decide BEFORE touching an engine

The biggest quality lever for industry-grade SaaS video is **not which code engine you use** — it's
whether you show the **real product** at all. Recreating UI in HTML always reads as "made by a dev."
Route every request into one of three pipelines first; only load that path's tooling.

| Signal | Pipeline | Carrier |
|---|---|---|
| Shows the real app working (demo, walkthrough, feature reveal, live UI) | **FOOTAGE** | Cap capture → DaVinci Resolve |
| No real UI needed — pure concept, kinetic type, diagram, stat pop, abstract | **PROGRAMMATIC** | HyperFrames end-to-end |
| Product promo wanting credibility + polish (default for the channel) | **HYBRID** | Footage in Resolve + HyperFrames transparent overlays |

- **Default HYBRID** for product-facing content. Pure-programmatic caps below the cinematic SaaS look;
  footage + a grade + overlays gets a solo creator to ~one notch below a top studio.
- The motion-design brain (`remotion-video-prompt`) is pipeline-agnostic and still used for
  HYBRID/PROGRAMMATIC overlays/scenes.
- Footage + hybrid step-by-step (tools, capture settings, Resolve assembly, grade, mix, export):
  `hybrid-pipeline.md`.

## 1. The programmatic engine (standardized: HyperFrames)

- **HyperFrames (primary)** — HTML + GSAP + `data-*` timing, rendered headless. Native TTS,
  captions/karaoke, scene transitions, audio-reactive, variables, `lint`/`inspect` QA. Fast to
  iterate, deterministic, seek-safe. Default for ~everything: title cards, kinetic type, UI
  recreations, stat pops, multi-scene explainers, Shorts and long-form alike.
- **Remotion (rare escape hatch only)** — React + `useCurrentFrame`. New work is standardized on
  HyperFrames; reach for Remotion only by §2. Do not migrate an existing Remotion project unless
  the user asks. For real product footage, prefer the FOOTAGE/HYBRID pipeline over rebuilding the
  UI in either engine.

The **storyboard / motion-design thinking is engine-agnostic** and comes from the
`remotion-video-prompt` skill (3-act spine, easing language, color, depth, audio). We borrow its
brain and emit a HyperFrames composition; only the tagged shots fall back to Remotion.

## 2. When to fall back to Remotion (and how)

Default to HyperFrames. Reach for Remotion ONLY when the shot needs:
- A heavy React component ecosystem you'd otherwise rebuild from scratch, or an existing Remotion
  asset the user already has (then consider the `remotion-to-hyperframes` port instead).
- Frame-exact programmatic generative work that's far easier in React/`spring()` than GSAP.
- Output the user explicitly asked to keep in Remotion.

If HyperFrames has a native answer (transitions, captions, audio-reactive, Lottie/Three via its
adapters — see `hyperframes-animation`), it is NOT a fallback case. Prefer HyperFrames.

**How to composite a fallback shot:** build that single clip with the `remotion-video-prompt`
flow (its own isolated project when parent dependencies conflict, version-pinned), render it to MP4/transparent
WebM, then bring it into the HyperFrames timeline as a `<video muted playsinline>` clip (+ a
separate `<audio>` if it carries sound). Keep the seam on a transition so it reads as one piece.
Always tell the user when and why a shot used Remotion.

## 3. Research grounding — the anti-hallucination contract

The video's credibility is the whole point. Every on-screen claim about the feature must trace to
something real in THIS repo. Two layers:

**3a. Internal truth (the spine).** Before storyboarding, read the actual source for the chosen
feature:
- The commits/PR(s) that shipped it (`git log`, `gh pr view <n> --json title,body,files`).
- The real code surface — function/command names, the UI strings, the config flags, the data
  model. Recreate UI from real tokens, not invented ones.
- Real numbers only (durations, limits, counts, score formulas) — copy them, don't estimate.
- The before→after story (what was painful, what the feature changes).

**3b. External context (the frame).** To explain the concept to a general audience:
- Named library/tool/framework → **Context7 MCP** (`resolve-library-id` → `query-docs`) for
  current, accurate docs. Prefer it over memory.
- The general concept ("what is X, why it matters") → the host's current web-research capability.
- External context FRAMES the feature; it must never add capabilities the project lacks.

**The contract:** if you cannot verify a fact in the repo (or a named, citable source), it does
not go on screen or in the copy. When unsure, cut it or ask. Maintain a short "verified facts"
list in the feature brief; everything in the video maps to it.

## 4. Title / description / hashtags — researched, honest

Run only after the video is final. Order: research → draft → GATE D approval.

- **Research current trends** with the host's web-research capability: how do high-performing videos in THIS topic +
  THIS platform title themselves right now? Which hashtags actually circulate? Shorts and
  long-form differ — Shorts reward a punchy front-loaded hook + 3–8 tight tags; long-form rewards
  a searchable, descriptive title + a fuller description.
- **Title:** accurate to what the video actually shows. Hooky, not clickbait — never promise what
  the video doesn't deliver.
- **Description:** 1–3 line value summary → real links (repo, site, docs) → tags. Only verified
  facts and real URLs. No invented metrics ("10x faster") unless the repo proves it.
- **Hashtags:** a researched mix of broad reach + niche/topical tags genuinely used in this space
  now. No spammy walls; quality over count.

## 5. Production checklist (HyperFrames primary path)

Detail lives in `hyperframes-cli` / `hyperframes` / `hyperframes-media`. The spine:
1. `npx hyperframes init <name>` in an isolated project directory when parent dependencies conflict. Node ≥ 22, FFmpeg present
   (`npx hyperframes doctor` if render fails).
2. Author the composition from the approved prompt. Build layout (end-state) before animation.
   Transitions between every scene; entrance on every element; no exit tweens except the last
   scene. Deterministic only.
3. Audio via `hyperframes-media`: `npx hyperframes tts` for VO; BGM per spec; captions synced if
   used. Spell initialisms for TTS (A.I., I.D.E.).
4. QA: `npx hyperframes lint` → `npx hyperframes inspect` (fix overflow/contrast) → `preview`.
5. `npx hyperframes render --quality high` (use `--quality draft` while iterating).
6. Composite any `[REMOTION FALLBACK]` clips (§2). Deliver the real MP4 path; open it.

## 6. Format defaults

| | Short / Reel | Long-form |
|---|---|---|
| Ratio | 1080×1920 (9:16) | 1920×1080 (16:9) |
| Length | ≤ 60s (sweet spot 20–45s) | 1–5 min |
| Hook | first 1–2s, hard | first 5–10s |
| Pace | fast, one focal element/scene | room to breathe, demo depth |
| Copy | minimal on-screen, punchy VO | fuller VO + on-screen support |

When recutting a Short ⇄ long-form: keep scenes as centered columns and swap dims; a single
global scale on the scene wrapper adapts most shots without per-scene edits (proven pattern).

## 7. Pointers (load on demand)
- `hybrid-pipeline.md` — FOOTAGE + HYBRID how-to: Cap capture, HyperFrames alpha overlays, DaVinci Resolve assembly/grade/mix, export. The path to industry-grade.
- `remotion-video-prompt` skill — storyboard brain, motion-design knowledge, Remotion contract.
- `hyperframes` skill — composition contract, layout-before-animation, transition rules.
- `hyperframes-animation` — motion rules, blueprints, runtime adapters (GSAP/Lottie/Three/etc.).
- `hyperframes-cli` — init / lint / inspect / preview / render commands + flags.
- `hyperframes-media` — TTS, BGM, transcribe, background removal, captions.
- `remotion-to-hyperframes` — only if porting an existing Remotion project.
- Context7 MCP — current docs for any named library/tool.
