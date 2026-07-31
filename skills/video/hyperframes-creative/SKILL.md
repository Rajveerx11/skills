---
name: hyperframes-creative
description: Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narration, beat planning, audio-reactive visuals, composition patterns, and brand / style decisions. For atomic motion patterns and scene blueprints, use `hyperframes-animation`.
---

# HyperFrames Creative

Brand, pacing, style, narration, and composition direction. Use after the technical contract from `hyperframes-core` is in place.

For motion patterns, scene blueprints, transitions, and CSS marker effects, use `hyperframes-animation` — this skill is intentionally non-animation.

> **Read these two FIRST for any non-trivial composition — they override web instincts:**
>
> - `references/house-style.md` — "interpret the prompt, generate real content," the lazy-default list, and the background/foreground layer recipe. This is what turns a literal restyle into a _concept_.
> - `references/video-composition.md` — video-medium density, scale, foreground metadata (the "produced, not generated" detailing: data bars, registration marks, monospace readouts, 8-10 elements/scene).
>
> Skipping these is the single biggest cause of generic, web-page-looking output. They are not optional rows in the routing table below — for anything beyond a one-line edit, open both before you choose colors or write HTML.

## Workflow

1. If a project has a design spec, read it first — precedence `frame.md` → `design.md` → `DESIGN.md`. `frame.md` is the preferred spec for video/hyperframes projects and wins if more than one exists (same format as `design.md`); it is always lowercase, no `FRAME.md` variant, while `design.md` and `DESIGN.md` are different files on Linux. Treat it as brand truth: colors, fonts, spacing, tone, and constraints.
2. If no design spec exists and the user asks for visual direction, choose a route:
   - Named style or mood → `references/visual-styles.md`
   - Fast defaults → `references/house-style.md`
   - Interactive selection → `references/design-picker.md`
3. For multi-scene work, plan beats and rhythm before writing HTML → `references/beat-direction.md`. For scene transitions, jump to `hyperframes-animation/transitions/`.
4. For motion-heavy work, read `references/motion-principles.md` (high-level guardrails), then go to `hyperframes-animation` for atomic rules.

## Routing

| Topic                                                                    | Read                                 |
| ------------------------------------------------------------------------ | ------------------------------------ |
| Default palettes, motion, typography, lazy defaults to question          | `references/house-style.md`          |
| Named style presets, mood-to-style routing                               | `references/visual-styles.md`        |
| Palette-specific color tokens                                            | `palettes/*.md`                      |
| Composition patterns — PiP, text-behind-subject, title card, slide show  | `references/composition-patterns.md` |
| Stats / infographic presentation                                         | `references/data-in-motion.md`       |
| Structured expansion for open-ended prompts                              | `references/prompt-expansion.md`     |
| Video-medium density, scale, color, frame composition                    | `references/video-composition.md`    |
| Per-beat direction, rhythm planning, transition timing                   | `references/beat-direction.md`       |
| Post-authoring spec verification (colors, type, corners, spacing, depth) | `references/design-adherence.md`     |
| High-level motion guardrails and GSAP-quality rules                      | `references/motion-principles.md`    |
| Font selection, pairings, rendered-video type guardrails                 | `references/typography.md`           |
| Script pacing, tone, openings, number pronunciation                      | `references/narration.md`            |
| Precomputed audio bands mapped to motion                                 | `references/audio-reactive.md`       |

## Scripts

- `scripts/contrast-report.mjs` — inspect contrast warnings from rendered frames.
- `scripts/extract-audio-data.py` — pre-extract audio bands for audio-reactive compositions.
- `scripts/package-loader.mjs` — support script for bundled creative tooling.

Run from the repo root with explicit paths, for example:

```bash
python skills/hyperframes-creative/scripts/extract-audio-data.py <audio-file>
```

Animation analysis (`animation-map.mjs`) lives in `hyperframes-animation/scripts/`.

## Boundaries

- Do not override `hyperframes-core` technical rules.
- Do not require a design system for a minimal technical composition.
- Do not add extra scenes, narration, music, captions, or transitions unless the request calls for them or you first propose the expansion.
- Keep recipe references task-specific; do not read every reference for simple edits.

<!-- skill-evolver:adaptive-start -->
## Professional execution

- **Discover automatically:** read the strongest available design source in precedence order, inspect brand assets/fonts/content/audience/platform, and extract non-negotiables, reusable motifs, forbidden treatments, and accessibility needs before proposing a direction.
- **Default intelligently:** when no spec exists, generate 2-3 meaningfully different internal worlds, judge them against message, audience, distinctiveness, feasibility, and motion potential, then develop one. Use the house style and embeddable typography as constraints, not a template.
- **Produce a build contract:** define concept sentence, palette roles, type hierarchy, composition grid, foreground/detail system, imagery/material language, motion grammar, density, transition family, audio relationship, and negative list.
- **Reduce manual choices:** infer safe platform/design defaults, present only decisions that materially change identity or scope, and reuse the picker/package loader/contrast tooling where applicable.
- **Validate before build:** reject directions that imitate a named reference too closely, use arbitrary novelty, lack readable hierarchy, fail contrast, depend on unavailable assets/fonts, or cannot be expressed deterministically.
- **Finish the handoff:** deliver one coherent direction with rationale, tokens, asset needs, scene rules, validation criteria, and explicit assumptions; include alternatives only when the user requested a choice.
- **Learn only from evidence:** record accepted directions, explicit rejections, and audience feedback through `skill-evolver`; never convert personal model taste into a portfolio rule.
<!-- skill-evolver:adaptive-end -->
