---
name: remotion-video-prompt
description: Turn a raw video idea into a production-ready Remotion generation prompt. Use when the user wants to create a video with Remotion, make a SaaS intro / explainer / product demo / promo / motion-graphics video, or "write a prompt for an AI to build my video." Asks 4-5 clarifying questions, then outputs one comprehensive master prompt engineered to make any AI coding agent generate an awe-factor, professional video.
---

# Remotion Video Prompt Builder

Your job: take the user's rough idea and turn it into a single, comprehensive **master prompt** that another AI coding agent (or you) can execute to produce a genuinely professional Remotion video — correct animation timing, on-brand color, depth, camera, kinetic typography, and synced audio.

Read `reference.md` (the motion-design + Remotion knowledge base) **and `LEARNINGS.md` (accumulated lessons from past builds)** before assembling the prompt. Emit using the skeleton in `template.md`. This skill is **self-improving** — see "Self-update protocol" below; apply it after every iteration so the skill gets better each time it's used.

## Workflow

### 1. Capture the raw idea
Take whatever the user gave you. Don't critique it. Note what's already specified so you don't re-ask it.

### 2. Ask 4-5 clarifying questions (one round)
Use the **AskUserQuestion** tool. Prefer multiple-choice for discrete decisions; ask open free-text only when needed. Skip any question the user already answered. Cover these dimensions (merge/trim to land at 4-5 total):

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
- Include the **global setup line** (reuse the machine's shared headless browser) so renders don't re-download Chrome:
  `Config.setBrowserExecutable("C:/Users/rajve/.remotion/chrome-headless-shell/win64/chrome-headless-shell-win64/chrome-headless-shell.exe")`
- Note: run the project from a directory **outside** `C:\Testing IDE` and pin `zod@4.3.6`, to avoid the repo's zod-3 version-mismatch warning.
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

## Self-update protocol (run after EVERY iteration)

This skill must improve itself continuously. **An "iteration" = any render produced + any round of user feedback on a video.** After each iteration — whether the skill built the video or a downstream agent did — do this before considering the turn done:

1. **Reflect.** What did we learn this iteration? Look for: a bug/gotcha hit and fixed; a tool/version quirk; a user preference or correction ("voice too robotic", "make it punchier", "music inaudible"); a technique that worked well; a default worth changing.
2. **Record (always).** Append a dated bullet to `LEARNINGS.md` for every non-trivial lesson — concise, with the *why* and the *fix*.
3. **Promote (when durable).** If a lesson should change future prompts, fold it into the right place:
   - a hard technical rule or gotcha → `reference.md` (§1 or §6 etc.)
   - a new default / phrasing for the emitted prompt → `template.md`
   - a workflow change → this `SKILL.md`
4. **Version + changelog.** Bump the version in `CHANGELOG.md` (semver: patch = lesson/tweak, minor = new capability, major = workflow overhaul) with a one-line summary of what changed and why.
5. **De-dupe.** If a new lesson supersedes an old one, edit the old entry rather than contradicting it. Keep the files tight — this is a living memory, not an append-only dump.

Trigger points: right after a render the user reviews, and right after the user gives feedback/asks for a change. Keep updates small and frequent. The goal: the next person who runs `/remotion-video-prompt` benefits from everything we already learned, without re-deriving it.
