---
name: frontend-slides
description: Create, reconstruct, or improve animated HTML slide decks that run in a browser and print cleanly to PDF. Use for talks, pitches, lessons, demos, web presentations, or PPT/PPTX-to-web reconstruction. Provides a reusable standalone HTML scaffold with keyboard navigation, fragments, progress, responsive scaling, reduced motion, and print styles. Use the dedicated slideshow/HyperFrames skill instead when the user explicitly wants HyperFrames manifests, branches, or presenter runtime.
---

# Frontend Slides

Build a story-first web presentation, not a webpage cut into rectangles. Deliver a portable deck, real assets, and verified navigation/print behavior.

## Resolve resources

Treat the directory containing this `SKILL.md` as `<skill-dir>`. Reuse:

- `<skill-dir>/assets/deck-template/index.html` for a dependency-free deck;
- `<skill-dir>/scripts/check_deck.py` for structural validation.

Keep the user's project as working directory. Copy the template into the requested output folder, then edit the copy.

## Discover context

Inspect before asking:

- source brief, existing deck, notes, product docs, brand tokens, and supplied assets;
- audience, room/device, presentation length, desired decision, and delivery format;
- whether the user wants a standalone HTML file, project integration, PDF export, or faithful reconstruction;
- factual claims, citations, screenshots, demos, logos, and confidentiality constraints.

Infer sensible defaults: 16:9, browser playback, keyboard navigation, and printable output. Ask only when audience/purpose, source access, brand identity, or output format materially changes the deck.

## Ingest source material

### From text or a brief

Create a fact ledger and a sequence of claim headlines. Separate verified facts, user-provided opinions, placeholders, and claims needing sources.

### From PPT/PPTX

Conversion means reconstruction into semantic HTML; do not promise pixel-perfect import or preserved PowerPoint animation.

Use capabilities in this order:

1. If a presentation-artifact skill is installed, use it to inspect text, notes, layout, and rendered slides.
2. Otherwise, check for `python-pptx` and use it only for text, shapes, images, and basic layout extraction.
3. Use LibreOffice only when installed and only to render/convert a reference PDF. It does not preserve web semantics or PowerPoint animation.
4. If none is available, ask for a PDF/image export or permission to install the needed dependency.

Preserve source facts and speaker notes. Replace unreadable slide screenshots with native HTML only when reconstruction is authorized.

<!-- skill-evolver:adaptive-start -->
## Shape the narrative

1. Define audience change: what they should understand, believe, or do after the deck.
2. Reduce content to one claim per slide. A title names the slide; a claim advances the argument.
3. Build a clear arc: hook, stakes, explanation/proof, resolution, action.
4. Choose an archetype for each slide: `statement`, `image`, `diagram`, `comparison`, `data`, `demo`, `quote`, `section`, or `close`.
5. Put detail in notes or appendix. Split overloaded slides; never solve density by shrinking type.

For subjective work, form three internal visual directions that differ in composition, typography, graphic device, and motion language. Select one using audience, brand, content, feasibility, and readability. Show options only when requested.
<!-- skill-evolver:adaptive-end -->

## Build

Start from the scaffold:

```powershell
Copy-Item -LiteralPath "<skill-dir>\assets\deck-template\index.html" -Destination "<output>\index.html"
```

Then:

- replace sample slides with semantic `<section class="slide" id="...">` elements;
- write complete-sentence headlines;
- set design tokens once in `:root`;
- use a small set of layout primitives rather than one-off positioning;
- use real diagrams, screenshots, and data; never fabricate UI, metrics, quotes, customers, or integrations;
- use `data-fragment` only when staged disclosure improves comprehension;
- animate transforms and opacity; respect `prefers-reduced-motion`;
- keep navigation, focus, hash state, progress, and print behavior from the scaffold;
- keep critical text as HTML, not baked into images.

Use local assets for reliable playback. If remote fonts/media are necessary, document network dependence and provide a system-font or static fallback.

## Motion

Motion must explain sequence, hierarchy, causality, or state change.

- Use one entrance grammar and one emphasis grammar across the deck.
- Default to short transitions; long cinematic motion belongs only at section boundaries.
- Avoid autoplay that prevents the presenter from controlling pace.
- Never hide essential meaning behind motion.
- Confirm reduced-motion mode exposes every final state.

## Validate

Run:

```bash
python "<skill-dir>/scripts/check_deck.py" "<output>/index.html"
```

Then open the deck in a browser and test:

- Arrow keys, Page Up/Down, Space, Home/End, buttons, and URL hash;
- fragment reveal order and backward navigation;
- first/last slide boundaries;
- 16:9 desktop plus one narrow viewport;
- fullscreen and browser zoom;
- reduced motion;
- print preview/PDF page breaks;
- missing assets, console errors, overflow, clipping, contrast, and focus visibility.

Render a contact sheet or capture representative slides. Fix findings in one batch; confirm once.

## Completion

Deliver:

- HTML entry path and asset paths;
- how to present and how to print/export;
- source/citation or placeholder notes;
- validation results and tested viewports;
- any known reconstruction differences from PPT/PPTX.
