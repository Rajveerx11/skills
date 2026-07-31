# Reference: Making AI-generated Remotion videos look professional

Distilled from Remotion's official `llms.txt` system prompt + motion-design, color, camera, typography, and sound-design research. Use these as the rules you bake into every emitted prompt.

---

## 1. Remotion technical rules (HARD constraints — the agent MUST follow)

The #1 reason AI videos look broken is invalid Remotion code. Enforce these in the prompt:

**Animation is frame-driven, never time/CSS-driven:**
- Drive everything from `useCurrentFrame()`. Get `fps`, `durationInFrames`, `width`, `height` from `useVideoConfig()`.
- Use `interpolate(frame, [inStart, inEnd], [outStart, outEnd], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' })`. **Always clamp** or values overshoot off-screen.
- Use `spring({ frame, fps, config: { damping, mass, stiffness } })` for organic motion. Returns ~0→1.
- **NEVER** use CSS `@keyframes`, CSS `transition`, `setTimeout`, `setInterval`, or `async` work during render. They don't exist in a deterministic frame render.
- **NEVER** use `Math.random()` or `Date.now()` / `new Date()` — they break determinism (every frame re-randomizes → flicker). Use Remotion's `random('a-fixed-seed')` instead.

**Structure:**
- `src/index.ts` → `registerRoot(RemotionRoot)`.
- `src/Root.tsx` → one or more `<Composition id durationInFrames fps width height defaultProps component />`. Default 1920×1080 @ 30fps.
- Components are typed `React.FC`.
- Compute `durationInFrames` from real content (e.g. sum of scene lengths), or use `calculateMetadata` for data-driven length.

**Sequencing & layering:**
- `<Sequence from={f} durationInFrames={n}>` — child `useCurrentFrame()` resets to 0 at `from`. This is how you place scenes on the timeline.
- `<Series>` / `<Series.Sequence durationInFrames>` — back-to-back scenes without manual offsets.
- `<TransitionSeries>` + `<TransitionSeries.Transition presentation={fade()/slide()/wipe()} timing={linearTiming/springTiming}>` (from `@remotion/transitions`) — for cross-scene transitions.
- `<AbsoluteFill>` — full-frame layer; stack them for background / midground / foreground.

**Media & assets:**
- Assets live in `public/`, referenced with `staticFile('name.ext')`.
- `<Audio src={staticFile('vo.wav')} volume={0.9} />`, `<Video>` — import from `@remotion/media`. `volume` 0–1, `trimBefore`/`trimAfter` to clip. Place inside a `<Sequence>` to time it.
- `<Img>` / `<Gif>` (gif needs `@remotion/gif`) — for raster assets. Use `<Img>` not `<img>` so render waits for load.
- Fonts: `@remotion/google-fonts/<Family>` (`loadFont()` returns `fontFamily`), or `@remotion/fonts` `loadFont()` for local files. Always provide a `monospace`/`sans-serif` fallback.

**Render/setup conventions to include:**
- `remotion.config.ts`: `Config.setVideoImageFormat('jpeg')`, `Config.setCodec('h264')`, `Config.setOverwriteOutput(true)`, `Config.setChromiumOpenGlRenderer('angle')` (GPU for preview/glow).
- Reuse a verified browser only through `REMOTION_BROWSER_EXECUTABLE`; call `Config.setBrowserExecutable(process.env.REMOTION_BROWSER_EXECUTABLE)` when set. Otherwise let Remotion resolve or install its browser. Never hardcode a user directory or platform-specific cache path.
- Render: `npx remotion render src/index.ts <CompId> out/video.mp4 --concurrency=4` (4 is a good CPU balance on this machine; encode is CPU-only on Windows).

**Gotchas learned the hard way:**
- **Pin every `@remotion/*` package plus `react`/`react-dom` to the SAME exact compatible version** (no `^`), and use the Zod major required by that release. Mixed versions cause version-mismatch failures.
- **Bundled ffmpeg is stripped** (`--disable-filters`) — see §6. Don't rely on it for audio synthesis; do SFX/music in pure Node.
- **`@remotion/google-fonts` loads many weights** → a "made N network requests" warning and needs network at render. Pass `loadFont('normal', { weights:['400','500','600','700'], subsets:['latin'], ignoreTooManyRequestsWarning:true })` and always keep a `monospace`/`sans-serif` CSS fallback so it renders even offline. **Inline that options object at each call** — a shared `as const` object makes `weights`/`subsets` `readonly` and fails the (mutable) `loadFont` type (TS2345).
- **Never call a hook inside `.map()`/loops/conditionals.** A per-item `usePop()`/`useCurrentFrame()` in a `.map()` violates rules-of-hooks and can break the render. Read `useCurrentFrame()` + `useVideoConfig()` **once at the top**, then compute `spring({ frame: frame - delay, fps, config })` inline per item.
- A `still` render is the fast way to validate the composition compiles before a full render: `npx remotion still src/index.ts <CompId> out/still.png --frame=<f>`. Render a still of **every cursor/interactive and dense-layout scene** to eyeball alignment before the multi-minute full render.
- **Reuse `node_modules` across video projects** with identical pinned deps via `robocopy <src> <dst>\node_modules /E /MT:16` — skips a fresh `npm install`. robocopy **exit code 1 = "files copied" = success** (its exit codes are a bitmask; 0–7 are non-error). Kokoro's model is cached after the first project, so later VO runs need no re-download.
- **Background-task monitor gotcha:** the task's output file first line echoes the launch command, so grepping for the output *filename* matches instantly and a "wait for done" watch ends before work starts. Match a completion-specific token (`Encoded N/N`, `time remaining: 0s`, `+ out/`) or just await the task's own completion notification.

---

## 2. Animation language (what makes motion feel pro)

**Easing — match the curve to the feeling:**
- **Entrances: ease-OUT** (fast start, settle slowly) — feels responsive. `Easing.out(Easing.cubic)` or a spring.
- **Exits: ease-IN** (accelerate away).
- **Moves between two states: ease-in-out.**
- **Linear only** for continuous/mechanical motion (scrolling marquees, conveyor, infinite loops).
- Refined/corporate = gentle curves; energetic/startup = snappier curves + slight overshoot.

**Spring config cheatsheet** (`config`):
- Smooth, no bounce (UI, text, logos): `{ damping: 200 }` (or 100–200).
- Lively pop with a touch of overshoot: `{ damping: 12–18, mass: 0.6–0.9, stiffness: 100–140 }`.
- Punchy snap: higher `stiffness` (180–260) + moderate damping.
- Stagger elements: offset each item's spring/interpolate by 2–5 frames for a cascade.

**Timing & pacing:**
- 30fps default. Entrance ≈ 0.4–0.8s (12–24f). Hold readable text ≥ 1.5–2s. Scene length 3–8s.
- Snappy cuts feel energetic; longer holds feel premium/elegant. Keep one clear focal point per scene.
- Sync motion beats to the audio (VO emphasis, music hits). The video timeline should be **driven by the VO length** when there's narration.

**12-principles that matter most here:** ease in/out, anticipation (tiny pre-move), follow-through/overlap (elements settle slightly after the main move), staging (one focal point), secondary action (subtle background motion).

---

## 3. Camera & depth (the "awe" factor)

2D scenes look flat; depth makes them cinematic. All achievable in Remotion with transforms:
- **Parallax:** background layers move/scale **slower** than foreground. Put bg/mid/fg in separate `<AbsoluteFill>`s and drive `translate`/`scale` from frame at different rates.
- **Camera push / slow zoom (Ken Burns):** continuously `scale` 1.0→1.06 across a scene for subtle life; never static for long.
- **Camera pan:** translate the whole scene group while content animates in.
- **Depth cues:** blur + lower opacity + smaller scale on far layers; sharp + full opacity on the focal layer. Animate focus shifts by changing which layer is blurred.
- **3D tilt:** `transform: perspective(1200px) rotateY(...) rotateZ(...)` on cards/UI mockups for a dimensional product shot.
- Keep camera moves **subtle and slow** — big fast moves read as amateur unless intentionally kinetic.

**Vertical (9:16 Reel/Short) strategy:** do NOT shrink a wide UI to fit the narrow frame. Show **one focal element per scene, large and centered**; render the **background once at the top (`Main`) level** so it's continuous (only the scene *content* crossfades on top); per-scene "camera" = `scale()` + `translateY()` on the content group. Reads as scrolling/zooming through a phone-sized panel.

**Aspect-ratio swap is cheap when scenes are centered columns.** To repurpose the same project across 9:16 (Reel) and 16:9 (LinkedIn/YouTube): swap `width`/`height` in `timings.json`, then add ONE global `transform: scale()` in the shared `SceneWrap` (about frame center) so the centered ~900px column fills the wider/narrower frame. Centered content + a cursor that lives inside the scaled device container both adapt with zero per-scene edits. Validate the tallest scene doesn't clip at the chosen scale.

**Self-operating cursor (the "it clicks the buttons itself" shot):** draw a code SVG pointer that glides between waypoints (ease-in-out) and pops a ring + scale-down on click frames. To keep clicks pixel-aligned **under a scene zoom, put the cursor INSIDE the same positioned + `scale()`d container as the UI**, with cursor coords in that container's *unscaled local* space — the scale then carries the cursor with the UI. Validate with stills.

---

## 4. Color & art direction

**Dark-mode tech default (most SaaS intros):**
- Background: near-black, **not** pure `#000` — e.g. `#0B0B0D`–`#15161A`, or cool neutrals (zinc/slate `#0E1116`).
- Text: off-white (`#E5E7EB`/`#E5E2E1`), secondary text muted gray.
- 1 primary accent + optionally 1 secondary accent. Use accent sparingly for emphasis/CTA.
- **Gradients are structural in 2026**, not decoration: a violet→blue (Linear-style), teal→cyan, or accent-tinted radial glow behind the hero element. Animate gradient angle/position slowly.
- Glow: `box-shadow`/`filter: drop-shadow` in the accent color around focal elements = premium tech look.
- Subtle dot-grid or noise/grain overlay (low opacity) adds texture and stops flat banding.

**Rules:** maintain strong contrast (WCAG-ish) for text legibility; limit palette to ~2–4 colors + neutrals; keep accent usage consistent (same color = same meaning).

**Light mode:** elevated neutrals (soft grey/sand/stone), not harsh pure white; one confident accent.

---

## 5. Typography / kinetic type

- **Fonts:** clean, legible. Mono (JetBrains Mono, Geist Mono) for dev-tool/technical identity; geometric sans (Inter, Geist, Satoshi) for display. Limit to 1–2 families.
- **Hierarchy:** vary size/weight/color to rank importance; one dominant line per scene.
- **Reveal techniques:** per-word or per-line staggered fade+rise (translateY 20–30px → 0, ease-out); mask/clip-path wipe; typewriter for terminal/code vibe; number count-ups for stats.
- **Readability:** never animate text so fast it can't be read; hold ≥1.5s. High contrast vs background. Avoid more than ~7 words on screen at once.
- Sync text appearance to the VO word/phrase it represents.

---

## 6. Sound design & audio (a synced video, not a silent one)

- **Voiceover — DEFAULT to Kokoro, not SAPI.** Windows SAPI sounds robotic, slow, and emotionless — usable only as an offline fallback. **Kokoro** (`kokoro-js`, MIT, runs locally; ~300MB model download on first run) sounds natural. Good voices: `af_bella` (warm female), `af_heart`, `am_michael`/`am_puck` (confident male). Pass `speed: 1.1` for a livelier pace. Generate per-line, **measure each clip's real duration, and rewrite scene timing from it** so visuals always match narration.
- **Copy matters as much as the voice:** short, punchy, energetic lines beat long sentences — they sound less draggy and read better. Use `padSeconds ~0.55` between lines for a tighter feel. Spell initialisms for TTS (`A.I.`, `I.D.E.`, `M.I.T.`) so they aren't mangled.
- **SFX — synthesize in PURE NODE, not ffmpeg.** ⚠️ Remotion's bundled ffmpeg (`npx remotion ffmpeg`) is a **stripped `--disable-filters` build**: only a few filters compiled in (`sine`, `volume`, `amix`, `atrim`, `aformat`…). `anoisesrc`, `afade`, `highpass`, `lowpass` etc. are **absent**, so ffmpeg-based SFX synthesis fails. Instead write 16-bit PCM WAVs directly in Node (oscillators + envelopes + a seeded PRNG for noise). Reliable, offline, deterministic, no filter limits. Cues: whoosh on transitions, pop/tick on reveals, keyboard clicks on typewriter, success chime on ✓, riser into logo/climax, low boom on final lockup, sparkle/ding on the CTA.
- **Music bed — synthesize it too.** There's no reliable free *download* path, so generate a royalty-free bed in pure Node: chord pad + plucky arpeggio + sub bass + soft kick/hat, with an intro→build→full→outro arrangement (add the bass+perc only under the demo section). **Duck to ~0.20–0.24** under the VO (0.12–0.15 reads too quiet to hear). Fade in/out via a `volume={(f)=>…}` function keyed to the *video* length (so it fades at video end regardless of the music file's length). Output `.wav` (the final mux re-encodes to AAC anyway). Optional: let the user drop a real track at `public/music.mp3`.
- **Gate audio with readiness flags** in `timings.json` (`voReady`, `sfxReady`, `musicReady`), each flipped true by its generator. The composition only renders an `<Audio>` when its flag is true — so the project always renders even before audio is generated (and `remotion studio` preview never breaks).
- Place every audio clip in a `<Sequence from={eventFrame}>` at the exact frame of its visual event.

---

## 7. Story structure (SaaS / product video)

**3-act spine, ~30–90s:**
1. **Hook (0–15%)** — a sharp problem statement, bold claim, or intriguing visual. Earn the next 5 seconds.
2. **Value / How-it-works / Demo (15–80%)** — 3–5 beats: the product, its key differentiators, real UI or recreated UI. One idea per scene. This is where footage (if any) goes.
3. **CTA (80–100%)** — logo lockup + the single action (URL, "star on GitHub", "download"). Memorable end frame.

Keep it to **one message per scene**, escalate energy toward the CTA, and land on a clean, brandable final frame.

---

## 8. Style archetypes (offer these as quick presets)

- **Linear-premium** — deep near-black, violet→blue structural gradients, restrained motion, generous spacing, glow accents, elegant pacing.
- **Vercel / Geist-dark** — pure-feeling black, high-contrast white type, minimal, sharp geometric, fast confident cuts, monochrome + one accent.
- **Apple-keynote** — lots of negative space, slow confident camera pushes, big type, soft depth-of-field, cinematic holds, subtle premium SFX.
- **Playful startup** — bright accent on dark, bouncy springs (low damping), rounded shapes, snappy energetic pacing, fun SFX.
- **Cinematic/dramatic** — film grain, vignette, slow parallax, swelling music, dramatic reveals, anamorphic-ish glow.
- **Retro-terminal / dev** — mono font, scanlines/CRT glow, typewriter text, command-line aesthetics, glitch transitions — great for developer tools.

Pick the archetype, then apply the matching color (§4), easing/pacing (§2), and SFX (§6).
