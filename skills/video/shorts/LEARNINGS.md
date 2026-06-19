# LEARNINGS — /shorts

Dated lessons from real `/shorts` runs. Newest first. Durable rules get promoted into
`style.md` / `reference.md` / `template.md`; this file is the running log + the *why*.
Append a bullet after every feedback round. Keep it tight — edit stale entries, don't pile up.

## 2026-06-20 — First HyperFrames build + strategic pivot to hybrid (v2.0.0)

Shipped the Self-Heal video fully in HyperFrames (`C:\Tessera-Self-Heal-Video`, 1080×1350, 30s).
Lessons — env gotchas already promoted into the global hyperframes-* skills + `[[reference-hyperframes-toolchain]]` memory; workflow lessons here:

- **No code engine alone hits the premium SaaS look.** User correctly noticed the all-programmatic
  result is the same class as Remotion (both are HTML→Chrome→ffmpeg). Industry-grade SaaS videos are
  ~70% real footage + grade + sound design. → Added the **Phase 0 router** + `hybrid-pipeline.md`;
  default product-facing videos to HYBRID, not pure-programmatic.
- **Standardized programmatic on HyperFrames** (decision): for an AI-driven solo workflow its
  built-in `lint`/`inspect`/`validate`(contrast)/`tts`/`bgm` catch agent mistakes Remotion wouldn't.
  Remotion = rare escape hatch now.
- **HyperFrames toolchain quirks that cost time** (fixed once, see memory): ffmpeg not bundled (point
  PATH at the Remotion compositor build); Kokoro TTS needs a `python3.exe` shim because CLI runs
  `where python3` and misses the venv; no MusicGen → reuse + Node-trim a brand track.
- **`tl.fromTo()` re-animating an already-visible element needs `immediateRender:false`** or it
  vanishes from t=0 (a counter digit disappeared until its flip). Lint-clean; only shows in render.
  Promoted to `hyperframes/references/motion-principles.md`.
- **Always eyeball a hero frame per scene from the actual render** — automated lint/inspect/contrast
  all passed while the digit was invisible. Frame extraction caught it.

## 2026-06-19 — Skill created (v1.0.0), seeded from `remotion-video-prompt`

Built the combined HyperFrames-primary / Remotion-fallback skill. Carried over the transferable
lessons from two prior Remotion builds (Tessera intro + "Catch Flaky Tests" Reel) that are
engine-agnostic and worth not re-learning:

- **Drive the timeline from measured VO duration; gate audio behind readiness flags** so the
  project always renders even before audio exists. (Core pattern — Remotion side; the HyperFrames
  equivalent is letting `data-duration` + generated-then-synced audio drive layout.)
- **Punchy copy + faster pace beats long sentences** — rewriting VO short/energetic cut a video
  62s→52s and felt far more professional.
- **Natural voice is non-negotiable** — SAPI rejected as robotic. → `style.md`.
- **Recreate real UI from real tokens** (alpha rules, inline icon SVGs, tabular-nums, count-ups)
  → indistinguishable from the app. → `style.md`.
- **Duck music audibly (~0.22)** — 0.12–0.15 was inaudible. → `style.md`.
- **Run video projects OUTSIDE `C:\Testing IDE`** — inside the repo, toolchains resolve the repo's
  zod-3 and throw false mismatch warnings. → `reference.md` §5 + `template.md` §8.
- **Vertical ⇄ landscape recut is cheap** when scenes are centered columns (swap dims + one global
  scale). → `reference.md` §6.
- **Validate cheap before rendering expensive** — Remotion: `still` first; HyperFrames: `lint` +
  `inspect` first. → `reference.md` §5.

No `/shorts` end-to-end run yet. First real run will replace these seeds with lived lessons.
