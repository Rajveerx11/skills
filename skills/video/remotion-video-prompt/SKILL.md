---
name: remotion-video-prompt
description: Turn a raw video idea into a production-ready Remotion generation prompt. Use when the user wants to create a video with Remotion, make a SaaS intro, explainer, product demo, promo, motion-graphics video, or asks for a prompt an AI can use to build a video. Inspects available context, asks at most one concise round only for material unknowns, then emits one self-contained master prompt with storyboard, assets, timing, audio, implementation contracts, validation, and handoff.
---

# Remotion Video Prompt Builder

Your job: take the user's rough idea and turn it into a single, comprehensive **master prompt** that another AI coding agent (or you) can execute to produce a genuinely professional Remotion video — correct animation timing, on-brand color, depth, camera, kinetic typography, and synced audio.

Read [reference.md](reference.md) and [template.md](template.md). If present, read private preferences and outcome evidence from `%USERPROFILE%\.skill-data\remotion-video-prompt\` on Windows or `~/.skill-data/remotion-video-prompt/` on macOS/Linux. Never commit or echo that private state. Runtime feedback is evidence for `skill-evolver`; it does not authorize silently rewriting this skill.

If legacy `LEARNINGS.md`, `history/`, or `memory/` exists beside an installed
copy and external state does not, offer one previewed, opt-in migration. Keep
the legacy files as backup and excluded runtime state.

## Workflow

### 1. Capture the raw idea
Take whatever the user gave you. Don't critique it. Note what's already specified so you don't re-ask it.

### 2. Resolve unknowns (zero or one round)
Inspect the request and current project first. Ask only about dimensions whose answers materially change the result; zero questions is correct for a complete brief or delegated choices. If needed, use one concise round with at most five questions. Prefer discrete choices with a recommendation; use free text only when necessary. Never re-ask answered dimensions:

1. **Goal & destination** — What's the one outcome (sign-ups, GitHub stars, awareness)? Where does it play (X/LinkedIn 16:9, vertical Reel/Short 9:16, YouTube, site hero loop)? This fixes aspect ratio + length.
2. **Style archetype & tone** — Offer concrete references from `reference.md` §Style Archetypes (e.g. *Linear-premium*, *Apple-keynote*, *Vercel-dark*, *playful startup*, *cinematic/dramatic*, *retro-terminal*). Tone = energetic/snappy vs. calm/elegant.
3. **Brand system** — Exact hex colors (primary/accent/bg), font(s), logo. If they don't know, offer to derive a palette per `reference.md` §Color.
4. **Footage vs. pure motion** — Do they have screen recordings / screenshots of the product to splice in, or should it be 100% code-drawn motion graphics / recreated UI?
5. **Content beats & audio** — The 3-6 key messages/features in order + any must-say lines; and audio choices: voiceover (yes/no, write it or they supply), music mood, SFX intensity.

If the user said "just decide / surprise me," pick strong defaults from `reference.md` and tell them what you chose.

### 3. Design the storyboard
Using their answers + `reference.md`:
- Pick a **3-act spine**: Hook (0-15%) → Value/Demo (15-80%) → CTA (80-100%).
- Break into 5-9 scenes. For each, decide: duration, on-screen text, layout/focal point, animation technique, easing/spring values, camera move, transition in/out, VO line, SFX cue.
- Apply the timing, easing, color, depth/parallax, and audio rules from `reference.md`. Pacing must match the chosen tone.

### 4. Emit the master prompt
Fill `template.md` completely. Rules for a strong emit:
- Be concrete: real hex codes, real frame counts / seconds, exact font names, exact on-screen copy, exact VO lines, named SFX cues.
- Bake in the **Remotion technical contract** (see template + `reference.md` §Remotion Rules) so the agent writes valid, deterministic code on the first try.
- Include portable browser handling: if `REMOTION_BROWSER_EXECUTABLE` names a verified executable, call `Config.setBrowserExecutable(process.env.REMOTION_BROWSER_EXECUTABLE)`; otherwise omit the override and let Remotion resolve or install its browser. Never hardcode a user directory or platform-specific cache path.
- Run in an isolated project directory when a parent repository hoists conflicting React, Remotion, or Zod versions. Pin every `@remotion/*` package plus `react`/`react-dom` to one exact compatible release and use the Zod major required by that release; do not copy a machine-specific workaround blindly.
- End the prompt with explicit acceptance criteria + the exact render command.

### 5. Deliver + offer handoff
Output the finished master prompt in a single fenced block (so it's copy-pasteable). Then offer the user a choice:
- **Save** it to a file (e.g. `video-prompt.md`), and/or
- **Execute it now** — either you build the Remotion project directly, or spawn a fresh agent with the prompt as its task.

Do not start building the video until the user confirms the prompt.

## Guardrails
- One question round only — don't interrogate. 4-5 questions max.
- Never emit a vague prompt. If a critical detail is missing and the user didn't answer, choose a sensible default from `reference.md` and state the assumption inside the prompt.
- The emitted prompt is the product. Keep it self-contained: an agent with zero prior context should be able to produce the video from it alone.

## Evidence-gated improvement

After a reviewed render or explicit correction, treat the outcome as evidence rather than an automatic skill edit:

1. Record explicit preference, reproduced defect, or measured result privately through `skill-evolver`; do not write secrets, project-private facts, or ordinary completion.
2. Promote a correctness guardrail after one reproduced defect; promote a quality default only after two consistent outcomes or one strong measured result.
3. Make the smallest general change in `reference.md`, `template.md`, or `SKILL.md`; keep user-specific preferences private.
4. Validate any proposed portfolio revision on a realistic brief before release.
5. Keep private preferences/outcomes under the external state directory; de-duplicate or supersede stale evidence there and never append contradictory folklore to repository files.

<!-- skill-evolver:adaptive-start -->
## Professional execution

- **Discover automatically:** extract goal, audience, platform, format, duration, brand, assets, product facts, required beats, audio, and constraints from the request and current project before asking anything. Never re-ask known details.
- **Default intelligently:** when the user delegates choices, select a platform-appropriate format/duration, one specific style archetype, derived accessible palette, coherent font pair, 3-act spine, 5-9 scenes, restrained SFX, and buildable Remotion primitives.
- **Reduce human coordination:** ask zero to five questions in one round, only for choices whose answers materially change the result. State inferred defaults inside the master prompt so the build agent can proceed without another interview.
- **Make the prompt executable:** include project/context discovery, asset ledger, scene-level purpose/content/timing/motion/audio, composition IDs/props, implementation constraints, dependency policy, render commands, QA gates, fallback behavior, and completion artifacts.
- **Protect truth and feasibility:** label assumptions, never invent product behavior or assets, avoid inaccessible/local-only fonts without fallback, specify deterministic frame-based animation, and require source-grounded copy plus final render inspection.
- **Finish the handoff:** emit one complete master prompt, a compact assumptions list, required user-provided assets only, and suggested invocation. Do not leave placeholders the receiving agent must rediscover.
- **Learn only from evidence:** record reviewed render outcomes, explicit concept approval, and reproduced failures through `skill-evolver`; update portfolio files only after evidence meets its promotion rules.
<!-- skill-evolver:adaptive-end -->
