# Style preference schema

Keep repository guidance generic. User-specific brands, voices, rejected treatments, project
profiles, and feedback history belong in private runtime state:

- Windows: `%USERPROFILE%\.skill-data\shorts\preferences.md`
- macOS/Linux: `~/.skill-data/shorts/preferences.md`

Read that file when present. Do not create it from silence, copy it into this skill, or commit its
contents. When absent, infer a one-run style from current project evidence and state assumptions.

Recommended private headings:

- `## Brand`: palette, fonts, logo handling, forbidden treatments
- `## Voice`: approved voices, speed, pronunciation, rejected voices
- `## Pacing`: hook density, scene length, CTA preference
- `## Look`: approved motifs, UI fidelity, grain/glow/transition preferences
- `## Audio`: music mood, ducking range, SFX density
- `## Format`: platform/aspect defaults
- `## Evidence`: dated explicit feedback or measured outcomes supporting each preference

Portable baseline when no private state or brand evidence exists:

- grounded product copy; no invented claims;
- natural, intelligible narration;
- one focal communication job per scene;
- 3-act hook/value/CTA structure;
- project-native colors, fonts, and real UI assets;
- audible but subordinate music;
- platform-implied aspect ratio and duration;
- lint, inspect, render, playback, and publishing-package verification.
