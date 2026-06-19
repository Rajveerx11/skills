# style.md — captured video preferences

The user's evolving taste for `/shorts` videos. The skill READS this every run and UPDATES it
after feedback (Self-update protocol). Seeded below from prior video work; refine as you learn.
When the user corrects something, change the rule here — don't just remember it for one run.

## Voice & narration
- **Natural voice, never robotic.** Windows SAPI was rejected as "too much AI, slow, no emotion."
  Use a natural TTS (HyperFrames `tts`; a warm voice ~1.1x speed reads well).
- Lines **short and punchy** — copy quality ≈ voice quality. Tighten before adding length.
- Spell initialisms for TTS: A.I., I.D.E., M.I.T.

## Pacing & structure
- 3-act spine: Hook (front-loaded, hard) → Value/Demo → CTA.
- One focal element per scene, especially for Shorts. Don't shrink whole panels — go large + centered.
- CTA / end card ≤ ~9–10s; let on-screen text carry detail the VO drops. No long dead holds.

## Look
- Default brand seen so far: **emerald accent on dark** (premium dev-tool aesthetic).
- Recreate real product UI faithfully from real tokens (exact pill alpha rules, real icon SVGs,
  tabular-nums, spring count-ups) — looks indistinguishable from the app.
- Premium finish: subtle film grain (soft-light), localized glow, no full-screen linear gradients
  on dark (banding).

## Audio mix
- Duck music **audibly** under VO (~0.22), not inaudibly low. Fade keyed to real video length.

## Format
- Shorts → 9:16 vertical, tight. Long-form → 16:9. Centered-column scenes recut cheaply between
  the two with a single global scale.

## Known project profiles
- **Tessera** (this repo) — local-first AI testing IDE. Brand: emerald + dark, pulled from the
  app's real CSS tokens. Audience: developers. Confirm exact hex against the live app each run.

> Everything above is a SEED from past Remotion builds. Treat it as defaults, not gospel — the
> user's reactions in THIS skill override and extend it.
