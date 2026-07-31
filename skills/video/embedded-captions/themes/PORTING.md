# Porting a demo into a first-class theme DNA

Port one theme at a time. The visual reference is the spec; the compiler contract is the law. Keep demos, source footage, mattes, and regression renders in the caller's workspace or a private test-data directory—never inside the skill.

## Inputs

- **Reference project** (`THEME_DEMO_DIR`): `index.html`, optional `rail.html`, `postfx.json`, a final render, and a comparison strip.
- **Regression fixture** (`THEME_FIXTURE_DIR`): a representative `source.mp4`, `frames_fg/`, `frames_bg/`, `matte.fps`, `transcript.json`, and `safe-zones.json`.
- **Engine**: `../scripts/make-theme.cjs`. Read its registries and existing theme files before changing code.

If either directory is absent, ask for that artifact or build a synthetic fixture that exercises the same behavior. Do not invent private machine paths.

## Process

1. **Decompose the reference.** Identify the body paradigm, layer, entrance/exit verbs, hero setpiece, front effects, plate budget, and linkages. Map each feature to an existing registry entry or mark it `NEW`.
2. **Extend only shared primitives.** Port genuinely new behavior into parameterized generator functions. Sizes, colors, counts, timing, and random seeds belong in DNA parameters. Preserve existing registry behavior.
3. **Write `themes/<name>.json`.** Follow the current schema and nearby theme examples for `voice`, `when`, `register`, `fonts`, `palette`, `body`, `hero`, `fx`, `plate`, and `linkages`.
4. **Compile and preview.**

   ```bash
   node scripts/make-theme.cjs "$THEME_FIXTURE_DIR"
   node scripts/preview-frames.cjs "$THEME_FIXTURE_DIR" <four-key-times>
   ```

   Compare the output against the reference strip. Iterate at most three focused rounds; record any deliberate deviations.
5. **Render and compare.**

   ```bash
   bash scripts/render-theme.sh "$THEME_FIXTURE_DIR"
   ```

   Extract a 12-frame strip around the apex. The new theme must read identically at a glance while preserving deterministic timing and layout.
6. **Regression-test.** Recompile at least one previously passing theme fixture plus the new fixture. Confirm the prior theme's two-frame preview remains visually unchanged.
7. **Register.** Add the identity to `CATALOG.md` and `themes/README.md`, including voice, fit, dependencies, and authoring compiler.

## Hard rules

- Preserve determinism, seeded randomness, equal-length keyframes, font constraints, stable body typography, apex ownership, and scheduling within clip duration.
- Never alter an existing setpiece or paradigm merely to fit one theme. A shared change needs a reproduced defect and regression evidence.
- Run `node --check scripts/make-theme.cjs` after compiler edits.
- Keep reference media, previews, renders, and private notes out of synchronized skill copies.
