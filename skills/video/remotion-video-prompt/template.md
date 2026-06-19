# Master-prompt skeleton

Fill EVERY `<...>` with concrete values. Delete bracket hints. The result must be self-contained — an agent with no prior context produces the video from this alone. Emit it inside one fenced code block so the user can copy it.

---

You are an expert **Remotion motion designer + creative director**. Build a complete, render-ready Remotion project for the video specified below. Aim for a professional, awe-factor result: precise timing, on-brand color, real depth, kinetic typography, and audio synced to motion. Write valid, deterministic Remotion code that renders on the first try.

## 1. Project
- **Title / subject:** <what the video is>
- **Goal / CTA:** <the one outcome + exact CTA text/URL>
- **Destination & format:** <platform> → **<W>×<H> @ 30fps**, target length **<N>s** (~<frames> frames).
- **Output:** `out/<filename>.mp4`, H.264.

## 2. Brand system
- **Colors (hex + role):** background `<#>`, surface `<#>`, text `<#>`, muted `<#>`, primary/accent `<#>`, secondary `<#>`. <gradient spec if any>.
- **Typography:** display `<font>`, body/mono `<font>` (load via `@remotion/google-fonts`; monospace/sans fallback).
- **Logo / wordmark:** <asset path in public/, or "render wordmark in <font> <color>">.
- **Visual motifs:** <dot-grid / grain / glow / shapes>.

## 3. Art direction
- **Style archetype:** <Linear-premium / Vercel-dark / Apple-keynote / playful / cinematic / retro-terminal>.
- **Mood & pacing:** <energetic-snappy | calm-elegant>.
- **Depth:** background/midground/foreground layers; parallax (bg slower than fg); <slow camera push 1.0→1.06 per scene | pan | 3D tilt on UI>.
- **Lighting/FX:** accent glow on focal elements; subtle **film grain** overlay (SVG `feTurbulence`, opacity ~0.045, `mix-blend-mode: soft-light`, drift position by frame) for a premium finish + anti-banding; <vignette/scanlines if archetype calls for it>.

## 4. Animation language (apply throughout)
- Entrances **ease-out** (~12–24f); exits ease-in; state changes ease-in-out; only loops are linear.
- Springs: smooth text/logos `config:{damping:200}`; lively pops `config:{damping:14,mass:0.7,stiffness:120}`. Stagger grouped items by 2–5f.
- Hold readable text ≥1.5s. One focal point per scene. Sync motion beats to the VO/music.

## 5. Storyboard (scene-by-scene)
For EACH scene give a row: **#, time range (s) & frames, on-screen text, layout/focal point, animation technique, camera move, transition in→out, VO line, SFX cue.**

| # | Time | On-screen text | Visual / layout | Animation | Camera | Transition | VO | SFX |
|---|------|----------------|-----------------|-----------|--------|-----------|----|-----|
| 1 | <0–Xs> | <copy> | <layout> | <technique> | <move> | <in→out> | "<line>" | <cue> |
| … | | | | | | | | |

Spine: Hook (0–15%) → Value/Demo (15–80%) → CTA (80–100%). 5–9 scenes.

## 6. Audio
- **Voiceover (default = Kokoro, natural):** generate locally with `kokoro-js` (voice `<af_bella | af_heart | am_michael>`, `speed: 1.1`); keep a Windows-SAPI script as offline fallback. Spell initialisms for TTS (`A.I.`, `I.D.E.`, `M.I.T.`). Script per scene is in the storyboard — keep lines short and punchy. The generator must **measure each clip's real duration and rewrite `public/timings.json`**, and the composition lays out scenes from that file so visuals always match narration. `padSeconds ~0.55`.
- **Music (synthesize it):** generate a royalty-free bed in pure Node (chord pad + arpeggio + sub bass + soft kick/hat; intro→build→full→outro). Duck to **~0.22** under VO via a `volume={(f)=>…}` fade keyed to the video length. Output `public/music.wav`. (Optional: user can drop a real `public/music.mp3`.)
- **SFX (synthesize in pure Node — NOT ffmpeg):** write 16-bit PCM WAVs directly (Remotion's bundled ffmpeg is a stripped build missing noise/fade filters). Place each in a `<Sequence from={eventFrame}>`: <whoosh on transitions, pops on text reveals, clicks on typewriter, success chime on ✓, riser into logo, boom + sparkle/ding on the CTA>.
- **Readiness flags:** `timings.json` carries `voReady` / `sfxReady` / `musicReady`, each set true by its generator; the composition only renders an `<Audio>` when its flag is true, so the project always renders (and `remotion studio` previews) even before audio exists.

## 7. Remotion technical contract (REQUIRED — do not violate)
- Frame-driven only: `useCurrentFrame()` + `interpolate(..., {extrapolateLeft:'clamp', extrapolateRight:'clamp'})` + `spring({frame, fps, config})`; `useVideoConfig()` for fps/size.
- **No** CSS `@keyframes`/`transition`, **no** `setTimeout`/`setInterval`/async-in-render, **no** `Math.random()`/`Date.now()` (use `random('seed')`).
- Structure: `src/index.ts` → `registerRoot`; `src/Root.tsx` → `<Composition>`; scenes via `<Sequence>`/`<Series>`/`<TransitionSeries>`; layers via `<AbsoluteFill>`.
- Assets in `public/`, via `staticFile`. Audio/Video from `@remotion/media` (`volume` 0–1). `<Img>` not `<img>`.
- `remotion.config.ts`: `setVideoImageFormat('jpeg')`, `setCodec('h264')`, `setOverwriteOutput(true)`, `setChromiumOpenGlRenderer('angle')`, and reuse the shared browser:
  `Config.setBrowserExecutable("C:/Users/rajve/.remotion/chrome-headless-shell/win64/chrome-headless-shell-win64/chrome-headless-shell.exe")`.
- **Pin all `@remotion/*` packages + `react`/`react-dom` to ONE exact version** (no `^`) and pin `zod@4.3.6`. Project lives **outside** `C:\Testing IDE` (avoids the repo's zod-3 mismatch warning). Node 24 OK.
- **Synthesize all SFX + music in pure Node** (write WAV PCM). Do NOT use `npx remotion ffmpeg` for synthesis — it's a stripped build missing `anoisesrc`/`afade`/`highpass`/etc.
- Load fonts with explicit weights + a CSS `monospace`/`sans-serif` fallback. Validate with a `still` render before the full render.

## 8. Deliverables
1. The full Remotion project (all files, `package.json`, `tsconfig.json`, `remotion.config.ts`).
2. Any audio-generation script(s) needed for the VO/SFX (free/local only).
3. Exact commands to install, generate audio, preview (`npx remotion studio`), and render.

## 9. Acceptance criteria
- Renders cleanly with `npx remotion render src/index.ts <CompId> out/<file>.mp4 --concurrency=2`.
- Text always readable (contrast + hold time); nothing clips off-frame or overlaps wrongly.
- Audio synced: VO matches on-screen content; SFX land on their visual events; music ducked under VO.
- Consistent brand color/type; deliberate, eased motion (no linear pops, no flicker); a clean, brandable final frame.
