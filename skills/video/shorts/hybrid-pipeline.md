# Hybrid / Footage Pipeline — toward industry-grade SaaS video

The goal: SaaS marketing video that looks **one notch below a top studio**, built solo with AI +
free/open-source tools on Windows. The lever is **real product footage + a grade + motion-graphic
overlays** — not recreating the UI in code. Use this for the FOOTAGE and HYBRID pipelines from the
Phase-0 router.

Honest ceiling: this gets a dedicated solo creator to "very strong indie SaaS video." The last 20%
is **editorial taste + iteration** — it improves per video; AI assists, it doesn't replace it.

---

## The stack (all free / OSS, Windows-friendly)

| Layer | Tool | Notes |
|---|---|---|
| **Screen capture** (biggest lever) | **Cap** (cap.so) | Open-source, Windows. Screen-Studio-style auto-zoom on clicks + smoothed cursor. This single tool moves you ~40% toward the premium look. |
| **Edit / color grade / mix** | **DaVinci Resolve** (free) | Industry-grade, free (not OSS). Cut page for editing, **Fusion** for node motion-graphics, **Fairlight** for audio + ducking. Cross-platform. |
| **Motion-graphic overlays** (titles, lower-thirds, callouts, intro/outro, data-viz) | **HyperFrames → transparent WebM** | `npx hyperframes render --format webm` = VP9 alpha. Composite over footage in Resolve. This is where the code engine shines. |
| **Voiceover** | **ElevenLabs** (cheap, best) or **Kokoro** (OSS, `npx hyperframes tts`) | Human-grade VO is a big perceived-quality jump. Use ElevenLabs for hero videos. |
| **Music / SFX** | Licensed (Epidemic Sound / Artlist) or OSS-generated | Don't skip sound design — duck music under VO, SFX on cuts/clicks. |
| **(Advanced) 3D hero shots** | **Blender** (OSS) | Device mockups / abstract hero moments. Later. |

If the user lacks a tool, say so and offer the closest substitute (e.g. OBS for capture if Cap isn't
installed — but OBS has no auto-zoom, so flag the quality gap).

---

## Step-by-step

1. **Plan shots from the storyboard.** Take the 3-act spine (from `remotion-video-prompt`) and tag
   each beat: `LIVE UI` (film it) vs `OVERLAY` (HyperFrames alpha) vs `FULL-SCREEN GRAPHIC`
   (HyperFrames scene). Write the on-screen copy + which real flow each live beat shows. Keep the
   anti-hallucination contract (`reference.md` §3) — every claim traces to the real app.

2. **Prep the app for filming.** Clean demo data (no lorem/garbage, realistic names/numbers), hide
   desktop clutter, set a comfortable window size, increase UI font/zoom slightly so it reads on
   mobile. Rehearse the click path once.

3. **Capture with Cap.** Record at ≥ delivery resolution. Turn on auto-zoom (emphasis on clicks) and
   cursor smoothing. One clean take per beat — short, deliberate movements; pause briefly on key
   states so you have room to cut. Re-record rather than fix jank later.

4. **Author HyperFrames overlays on a TRANSPARENT background.** Build title cards / lower-thirds /
   callout chips / intro / outro / data-viz as a HyperFrames composition with **no opaque background
   layer** (the scene's bg stays transparent). Position elements where they'll sit over the footage.
   Render each with `npx hyperframes render --format webm` (VP9 alpha). Keep the brand system
   (`style.md`) identical to the footage's on-screen UI so overlays feel native.

5. **Assemble in DaVinci Resolve (Cut/Edit page).** Import footage + `.webm` overlays + VO + music.
   Cut to the VO/beat rhythm — hard hook in the first 1–2s (Short) / 5–10s (long-form). Overlays go
   on upper video tracks (Resolve alpha-composites WebM natively). Add speed ramps / punch-in zooms
   for emphasis if Cap didn't already.

6. **Grade for a unified film look (Color page).** Subtle, consistent: lift contrast, gentle
   saturation, a soft vignette, optional fine grain. Goal is cohesion between live UI and overlays —
   not a heavy LUT. One grade applied across all footage clips.

7. **Sound design (Fairlight).** VO on its own track at the front of the mix; music ducked under it
   (Fairlight has a ducking/normalize); SFX on cuts, clicks, and reveals. Target around -14 LUFS for
   social. This is where "fine" becomes "pro."

8. **Captions.** Burn in captions for silent autoplay (most social viewing is muted) — Resolve can
   auto-transcribe, or use `npx hyperframes transcribe` and style them as overlays.

9. **Export.** H.264 MP4, platform preset. Short/Reel = 1080×1920 (9:16); long-form = 1920×1080
   (16:9) or 4K. Verify with `ffprobe` (dims, duration, audio stream present) before delivering.

---

## Quality checklist — the "one notch below studio" bar

- [ ] Real app shown (not recreated), clean demo data, no UI jank
- [ ] Smooth auto-zoom / cursor; deliberate motion; nothing frantic
- [ ] Hard hook in first 1–2s (Short) / 5–10s (long-form)
- [ ] Overlays match the app's brand tokens exactly (feel native, not pasted on)
- [ ] One consistent grade across all footage
- [ ] VO mixed above ducked music; SFX land on events; ~-14 LUFS
- [ ] Burned-in captions for muted autoplay
- [ ] Correct ratio + resolution for the platform; ffprobe-verified

## When to stay PROGRAMMATIC (skip footage)

Pure HyperFrames is the right call — not a downgrade — when there's no real UI to show: concept
explainers, kinetic-typography hooks, animated diagrams, stat/number pops, brand stings, abstract
motion. Don't film those; build them in-engine per `reference.md` §5.
