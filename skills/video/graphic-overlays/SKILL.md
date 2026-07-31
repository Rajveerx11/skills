---
name: graphic-overlays
description: >
  Package an existing talking-head, interview, podcast, or demo video by
  layering timed graphic overlay cards onto the playing footage: titles,
  lower-thirds, data callouts, quotes, lists, chapter cards, diagrams, or
  picture-in-picture. Uses transcription with mandatory correction, bundled
  editorial layouts/styles/frames, dense-keyframe source preparation, and one
  faithful full-duration HyperFrames composition. Use for requests to add
  graphic overlays, package a video, add callouts or lower thirds, or make
  existing footage clearer and more engaging. Do not use for captions or
  word-synced text, generative scene editing, recoloring/background
  replacement, or a video built from scratch.
---

# Graphic Overlays

Add only graphics that clarify, prove, label, compare, or pace existing footage. Preserve the source video and audio as ground truth.

## Required runbook

Read [references/full-runbook.md](references/full-runbook.md) before execution. It contains binding commands, dense-keyframe preparation, transcription and correction rules, storyboard patterns, render strategies, bundled design primitives, HTML assembly, validation, and final render steps. Do not reconstruct those contracts from memory.

Load design resources only after the storyboard identifies a need:

- Browse [references/DESIGN_INDEX.md](references/DESIGN_INDEX.md) to select a shipped layout, style, and frame.
- Open only the selected HTML files under `references/layouts/`, `references/styles/`, and `references/frames/`.
- Use bundled `assets/vendor/gsap.min.js`; do not replace it with a network dependency.

## Outcome contract

Deliver one full-duration composition and final video in which:

- footage and audio remain continuous and synchronized;
- overlays map to corrected transcript facts and useful editorial beats;
- faces, captions, demonstrations, and critical UI remain unobscured;
- every card is readable at playback speed and has clean entry, hold, and exit;
- source seeking is frame-correct after dense-keyframe preparation;
- all documented HyperFrames and visual checks pass.

## Autonomous workflow

1. **Inspect:** locate source footage, prior transcript/storyboard, brand assets, bundled primitives, and previous outputs. Probe codec, dimensions, fps, duration, audio, keyframe interval, shot changes, and persistent safe zones.
2. **Resume:** fingerprint the source and relevant settings. Reuse valid metadata, seekable intermediate, audio, transcript, corrected transcript, storyboard, cards, composition, or render. Invalidate dependants after source, transcript timing, fps, or storyboard changes.
3. **Transcribe and correct:** run the exact runbook path. Flag low-confidence names, numbers, brands, and technical terms; never silently invent corrections.
4. **Storyboard:** choose sparse beats with explicit communication jobs. Default to the quietest shipped layout that works; remove decorative cards.
5. **Build cards:** customize shipped patterns instead of recreating equivalent CSS/animation. Inspect each card independently at entry, hold, and exit.
6. **Assemble and render:** follow the runbook's seekable-video and full-duration composition contracts exactly.
7. **Validate:** inspect sync, seek behavior, safe placement, contrast, overflow, cadence, audio continuity, final cleanup, and representative frames from every overlay.

## Decision policy

- Infer low-risk design and pipeline details from footage, transcript, brand, and platform.
- Ask only when a missing choice changes message, identity, rights, access, or irreversible scope.
- Preserve transcript truth, source continuity, safe zones, dense-keyframe media, absolute timing, overlay isolation, and render commands.
- Explore card type, composition, typography, transitions, and rhythm internally; commit to one coherent editorial system.

## Handoff

Report source and seekable-intermediate metadata, corrected transcript and storyboard paths, chosen shipped primitives, card/composition paths, final video path and media metadata, validation evidence, assumptions, and anything not verified.

Learn only from explicit approval, reproduced failures, or measured readability/timing evidence through `skill-evolver`. Never self-edit from silence or model self-rating.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for timed editorial overlays that clarify existing footage without obscuring speaker, captions, demonstrations, or critical UI.
- Creative freedom is high for card selection, composition, typography, and rhythm; transcript truth, source continuity, safe zones, seekable media, timing, and render contracts remain fixed.
- Inspect and reuse context first, finish the authorized pipeline, validate the assembled video, and report exact artifacts and unresolved checks.
- Record learning only from explicit approval, reproduced failures, or measurable readability and timing outcomes through `skill-evolver`.
<!-- skill-evolver:adaptive-end -->
