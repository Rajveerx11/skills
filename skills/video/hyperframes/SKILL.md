---
name: hyperframes
description: >
  Create or edit deterministic HyperFrames HTML video compositions:
  animations, title cards, overlays, captions, voiceovers, audio-reactive
  visuals, variables, media, sub-compositions, and scene transitions. Use for
  HTML-based video authoring and when composition structure, timing, media
  playback, or rendering must follow the HyperFrames contract. Route specialist
  requests to their dedicated video skill; use hyperframes-cli for commands,
  hyperframes-media for preprocessing, hyperframes-core for contracts,
  hyperframes-creative for direction, and hyperframes-animation for motion.
---

# HyperFrames

HTML is video source of truth. Preserve deterministic composition, timeline, media, and render behavior while using broad creative freedom for concept, layout, scene grammar, and motion.

## Route first

Use a specialist when it clearly owns the complete workflow:

- product/SaaS launch or promo: `product-launch-video`
- general website tour/showcase: `website-to-video`
- topic/article explainer with generated narration: `faceless-explainer`
- pull request: `pr-to-video`
- captions embedded into talking-head footage: `embedded-captions`
- editorial cards over existing footage: `graphic-overlays`
- short design-led motion hit: `motion-graphics`
- explicit Remotion source migration: `remotion-to-hyperframes`
- custom fallback composition: `general-video`

For native authoring, combine only needed domain skills:

- composition/data/timeline contract: `hyperframes-core`
- design system and creative direction: `hyperframes-creative`
- motion rules, transitions, and runtimes: `hyperframes-animation`
- TTS, music, transcription, captions, background removal: `hyperframes-media`
- scaffold, lint, inspect, preview, render, diagnose: `hyperframes-cli`
- registry blocks/components: `hyperframes-registry`

## Binding contract

Read [references/authoring-contract.md](references/authoring-contract.md) before non-trivial authoring or structural edits. It preserves exact data attributes, layout rules, media semantics, timeline registration, transition ownership, animation guardrails, typography/assets, variables, quality checks, and reference routing.

Always load from that contract:

- composition structure and timeline contract for new compositions;
- editing section before changing existing compositions;
- transition section for multi-scene work;
- output and quality sections before handoff.

Load other linked references only when their intent applies. Do not reconstruct exact contracts from memory.

## Autonomous workflow

1. **Inspect:** locate project root, `hyperframes.json`, design specs, compositions, IDs, tracks/clips, variables, media, fonts, providers, prior diagnostics, previews, and renders.
2. **Route and scope:** choose the owning workflow; for edits, identify the smallest affected composition and preserve unaffected timing/structure.
3. **Resolve direction:** follow design-spec precedence. When no spec exists, use `hyperframes-creative`; choose one buildable world rather than generic UI styling.
4. **Plan:** state communication job, composition graph, dimensions/fps/duration, asset ledger, rhythm, static hero frames, runtime, and validation plan.
5. **Build layout first:** size every root explicitly, create title-safe static end-state layouts, then add deterministic animation and media.
6. **Checkpoint:** keep an input/design fingerprint, composition IDs, referenced assets, and last passing gate. Reuse only compatible artifacts; invalidate dependants after timing, media, variable, or design changes.
7. **Validate:** static frames, lint, validate, inspect, contrast, design adherence, animation map, boundary/peak snapshots, render playback, media sync, and final metadata.
8. **Handoff:** provide composition IDs, variable examples, asset ledger, preview/render paths, media metadata, exact gate results, supported edit points, and anything unverified.

## Defaults and freedom

- Default runtime: one paused registered GSAP timeline per composition.
- Default layout: explicit root pixels, full-frame container, title-safe padding, static hero frame before motion.
- Default assets: project-local, licensed, deterministic, embeddable fonts.
- Default architecture: simplest valid form; modularize at the contract's documented threshold.
- Ask only when a missing choice materially changes outcome, rights, cost, access, or irreversible scope.
- Never relax root sizing, clip/track semantics, sub-composition isolation, deterministic seek state, media preload, transition ownership, or CLI gates.

Creative freedom is high for story, visual world, typography, composition, scene grammar, and choreography. Generate meaningful alternatives internally when direction is subjective, then commit to one coherent system.

Learn only from explicit approval, reproduced defects, or measured render evidence through `skill-evolver`; never alter a contract from subjective output alone.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for a distinctive, deterministic HyperFrames composition that communicates clearly and renders correctly.
- Creative freedom is high for direction, layout, scene grammar, and animation; composition, timeline, media, and renderer contracts remain fixed.
- Inspect and reuse context first, choose strong defaults, validate every affected layer, and report exact artifacts and unverified behavior.
- Record learning only from explicit approval, reproduced defects, or measured render evidence through `skill-evolver`.
<!-- skill-evolver:adaptive-end -->
