# CHANGELOG — remotion-video-prompt

Semver: patch = lesson/tweak, minor = new capability, major = workflow overhaul.
Updated as part of the Self-update protocol (see SKILL.md) after every iteration.

## v1.2.1 — 2026-06-17
Iteration on the flaky video (landscape recut for LinkedIn):
- Added **aspect-ratio swap recipe** (vertical ⇄ 16:9 = swap dims + one global `SceneWrap` scale; centered scenes + in-device cursor adapt with no per-scene edits).
- Added **CTA-VO-length check** (a "broader overview" line ballooned the end card to ~15s; tighten VO to ~9–10s and let the on-screen text carry the detail).

## v1.2.0 — 2026-06-17
Second real build (Tessera vertical "Catch Flaky Tests" Reel) fed its lessons back:
- Added **rules-of-hooks rule**: never call hooks in `.map()` — read frame/fps once, compute `spring()` inline per item.
- Added **`@remotion/google-fonts` `as const` pitfall**: inline `loadFont` options literals (mutable union arrays), don't share an `as const` object.
- Added **cursor-clicks-UI pattern**: animated cursor lives inside the same positioned+scaled "device" container as the UI, coords in unscaled local space → stays aligned under zoom.
- Added **vertical 9:16 strategy**: one large focal element per scene; background rendered once at `Main` level (only content crossfades); per-scene camera = scale + translateY.
- Added **faithful-UI-recreation** checklist (tonal token alpha rules, inline lucide SVG paths, tabular-nums, spring count-ups) and **node_modules robocopy reuse** (+ robocopy exit-1 = success) + **monitor/grep command-echo gotcha**.
- Confirmed the v1.1 core patterns (VO-driven timeline, readiness flags, pure-Node audio, Kokoro default) transfer cleanly to a new format/aspect ratio.

## v1.1.0 — 2026-06-14
First real build (Tessera intro) fed its lessons back into the skill:
- Voiceover default switched from Windows SAPI → **Kokoro** (natural); SAPI demoted to fallback.
- **SFX + music now synthesized in pure Node**, after discovering Remotion's bundled ffmpeg is a stripped `--disable-filters` build (no noise/fade filters).
- Added **synthesized music bed** guidance + raised duck level to ~0.22 (0.12–0.15 was inaudible).
- Added **readiness-flag gating** (`voReady/sfxReady/musicReady`) and **VO-driven timeline** as core patterns.
- Added: exact version-pinning rule, `still`-render validation, google-fonts weight/fallback note, **film-grain** finish, punchy-copy guidance.
- Established the **Self-update protocol** + `LEARNINGS.md` (this skill now improves itself each iteration).

## v1.0.0 — 2026-06-14
Initial skill: workflow (capture → 4–5 questions → storyboard → emit master prompt → handoff),
`reference.md` knowledge base (Remotion rules, motion/easing, camera/depth, color, typography,
sound design, story structure, style archetypes), and `template.md` master-prompt skeleton.
Built from research on Remotion's `llms.txt` + motion-design/color/audio best practices.
