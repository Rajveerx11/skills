# Master-prompt skeleton (HyperFrames-first)

Fill EVERY `<...>` with concrete, verified values. Delete the bracket hints. The result must be
self-contained — an agent with zero prior context produces the video from this alone. Emit it in
ONE fenced code block at GATE B so the user can copy/approve it.

Every feature fact below must come from the Phase-2 verified brief. No unverifiable claims.

---

You are an expert **HyperFrames motion designer + creative director**. Build a complete,
render-ready **HyperFrames** composition for the video below. Primary engine is HyperFrames
(HTML + GSAP + `data-*` timing). Aim for a professional, awe-factor result: precise timing,
on-brand color, real depth, kinetic typography, and audio synced to motion. Deterministic and
seek-safe — it must pass `npx hyperframes lint` and `inspect` and render on the first try.

## 1. Project
- **Feature / subject:** <the real feature, one line>
- **Project:** <repo name> — <one-line what it is>
- **Goal / CTA:** <single outcome + exact CTA text/URL — real link only>
- **Format:** <Short 9:16 | long-form 16:9> → **<W>×<H>**, target length **<N>s**.
- **Output:** `renders/<filename>.mp4`, H.264.

## 2. Verified facts (the spine — nothing on screen outside this list)
- <fact 1 — traced to repo: file/PR/commit>
- <fact 2 …>
- Real names/strings/numbers to show exactly: <command names, UI labels, counts, limits, formula>.
- Before → after: <the pain it removed / what changed>.

## 3. Brand system
- **Colors (hex + role):** bg `<#>`, surface `<#>`, text `<#>`, muted `<#>`, primary/accent `<#>`,
  secondary `<#>`. <gradient/glow spec>. (Pull from `style.md` / the project's real tokens.)
- **Typography:** display `<font>`, body/mono `<font>` (built-in HyperFrames font if possible;
  else provide `.woff2` in `fonts/`).
- **Logo / wordmark:** <asset path, or "render wordmark in <font> <color>">.
- **Motifs:** <dot-grid / grain / glow / shapes>.

## 4. Art direction
- **Style archetype:** <Linear-premium / Vercel-dark / Apple-keynote / playful / cinematic / retro-terminal>.
- **Mood & pacing:** <energetic-snappy | calm-premium>.
- **Depth:** background rendered once at root level (continuous); only scene CONTENT crossfades on
  top. Per-scene "camera" = `scale()` + `translateY()` on content. Parallax bg slower than fg.
- **Finish:** accent glow on focal elements; subtle film grain (SVG `feTurbulence`, low opacity,
  `mix-blend-mode: soft-light`) for premium feel + anti-banding. Avoid full-screen linear
  gradients on dark bg (H.264 banding — use radial/solid + localized glow).

## 5. Animation language (HyperFrames contract — do not violate)
- One **paused** GSAP timeline per composition; register `window.__timelines["<comp-id>"] = tl`.
- Build **layout (end-state) first**, then `gsap.from()` entrances INTO that layout; exits only on
  the final scene.
- **Transitions between every scene** — no jump cuts. Entrance on every element. Vary ≥3 eases per
  scene. Offset first tween 0.1–0.3s.
- Deterministic: **no** `Math.random()` / `Date.now()` (seeded PRNG if needed); no `repeat: -1`
  (compute finite repeats); no async timeline construction; only animate visual props (never
  `visibility`/`display`, never call media `play()`).
- Duration comes from `data-duration`, not the GSAP length. 60px+ headlines, 20px+ body,
  `font-variant-numeric: tabular-nums` on number columns; count-ups via a tween on the integer.
- Recreate any real product UI faithfully: exact tonal tokens / pill alpha rules, inline real
  icon SVG paths, real labels and numbers from §2.

## 6. Storyboard (scene-by-scene)
Spine: **Hook (0–15%) → Value/Demo (15–80%) → CTA (80–100%)**, 5–9 scenes for long-form, 3–6 for
a Short. For EACH scene: **#, time range (s), on-screen text, layout/focal point, animation
technique, transition in→out, VO line, SFX/beat, engine.**

| # | Time | On-screen text | Visual / layout | Animation | Transition | VO line | Engine |
|---|------|----------------|-----------------|-----------|-----------|---------|--------|
| 1 | <0–Xs> | <copy> | <layout> | <technique> | <in→out> | "<line>" | HyperFrames |
| … | | | | | | | <HyperFrames \| [REMOTION FALLBACK: why + approach]> |

## 7. Audio (HyperFrames-native)
- **Voiceover:** `npx hyperframes tts` (see `hyperframes-media` for voice/provider). Natural voice,
  not robotic. Spell initialisms (A.I., I.D.E.). Lines are short and punchy (copy quality ≈ voice
  quality). Caption sync if captions are used.
- **Music:** BGM per `hyperframes-media`; duck audibly under VO (not inaudibly low). Keyed to video
  length so it fades at the real end.
- **SFX/beats:** land on visual events (text reveals, transitions, the ✓, the CTA). Sync motion
  beats to VO/music.

## 8. Remotion-fallback shots (only if any §6 row is tagged)
For each `[REMOTION FALLBACK]` shot: <why HyperFrames can't do it> + <the exact Remotion approach>.
Build it via the `remotion-video-prompt` flow as an isolated project when parent dependencies conflict; pin all
`@remotion/*` plus react/react-dom to one exact compatible version and use its required Zod major; render to MP4/transparent WebM,
then composite into the HyperFrames timeline as a `<video muted playsinline>` clip on a transition
seam. If no row is tagged, delete this section.

## 9. Deliverables
1. The full HyperFrames project (`index.html`, `compositions/`, assets, `fonts/` if custom).
2. Audio assets generated via `hyperframes-media`.
3. Any Remotion fallback clip(s) + the composite step.
4. Exact commands: init, generate audio, `lint` → `inspect` → `preview` → `render --quality high`.

## 10. Acceptance criteria
- `npx hyperframes lint` and `inspect` pass (overflow/contrast clean or intentionally marked).
- Renders cleanly to `renders/<file>.mp4`. Text always readable; nothing clips/overlaps wrongly.
- Every on-screen fact is in the §2 verified list. No invented claims, numbers, or links.
- Audio synced: VO matches on-screen content; SFX on their events; music ducked under VO.
- Consistent brand color/type; deliberate eased motion; transitions between all scenes; a clean,
  brandable final frame with the real CTA.
