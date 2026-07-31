---
name: ui-ux-pro-max
description: Query and apply the bundled UI/UX design-intelligence dataset for web, mobile, desktop, and cross-platform products. Use when the user asks for evidence-backed style, palette, typography, product-pattern, UX, accessibility, motion, chart, icon, landing-structure, or stack-specific recommendations, or when a design-system decision should be grounded in the local searchable dataset. Not a generic frontend builder or existing-UI polish suite.
---

# UI/UX Pro Max

Turn product context into an implementable, evidence-backed design system. Use the bundled dataset as decision support, not a slot machine: query several dimensions, reconcile results with the product, then verify the rendered artifact.

## Routing boundaries

Use this skill when **searching or applying the bundled dataset** is central.

Route near misses:

- Existing interface audit, critique, polish, hardening, accessibility repair, or live browser iteration: use `impeccable`.
- Anti-slop aesthetic direction for a landing page, portfolio, marketing site, or showcase surface: use `design-taste-frontend`.
- Complete premium animated marketing-site delivery through React + Vite + Tailwind + GSAP: use `build-premium-website`.
- General production frontend page/component/application implementation with no dataset requirement: use `frontend-design-skill`.

When another frontend skill owns implementation, return a compact recommendation packet—selected system, tokens, constraints, and source rows—for that owner. Do not co-own the build.

## Locate the tools

Resolve the absolute directory containing this `SKILL.md` as `<skill-dir>`. Keep the user's project as working directory.

```bash
python "<skill-dir>/scripts/search.py" --help
```

Try `python3` or `py -3` only when `python` is unavailable. Scripts use Python 3 and the standard library. Do not use stale `.claude`, plugin-cache, or repository-specific paths.

## Discover context

Inspect before asking:

- product type, industry, primary user, key task, usage setting, and desired feeling;
- existing tokens, typography, components, brand assets, screenshots, and neighboring surfaces;
- stack from manifests and source files;
- viewport, input method, platform conventions, accessibility target, and performance limits;
- whether task is new design, local refinement, review, or design-system persistence.

Infer low-risk details. Ask only when a missing brand, audience, or product decision would materially change the result.

Stack detection examples:

- `package.json`: React, Next.js, Vue, Nuxt, Svelte, Astro, Angular;
- `pubspec.yaml`: Flutter;
- `Package.swift` or Xcode project: SwiftUI;
- `composer.json`: Laravel;
- React Native markers: `react-native` dependency plus native/app config;
- desktop manifests/source: WPF, WinUI, Avalonia, Uno, UWP, JavaFX.

When stack remains unknown, use platform-neutral guidance. Do not silently label it `html-tailwind`.

<!-- skill-evolver:adaptive-start -->
## Generate candidates

For new surfaces and redesigns, run a broad system query:

```bash
python "<skill-dir>/scripts/search.py" "<product> <industry> <audience> <tone> <density>" --design-system -p "<project>"
```

Then create three meaningfully different internal candidates. Change style family, typography character, palette logic, spatial rhythm, and motion—not only accent color. Use dial variants when helpful:

```bash
python "<skill-dir>/scripts/search.py" "<query>" --design-system --variance 3 --motion 3 --density 4 -p "<project>"
python "<skill-dir>/scripts/search.py" "<query>" --design-system --variance 6 --motion 5 --density 6 -p "<project>"
python "<skill-dir>/scripts/search.py" "<query>" --design-system --variance 9 --motion 7 --density 7 -p "<project>"
```

Select one candidate using:

1. user task and audience;
2. platform and stack conventions;
3. incumbent brand compatibility;
4. accessibility and content density;
5. implementation cost and performance;
6. distinctiveness without novelty tax.

Keep alternatives internal unless requested. The database recommends; product evidence decides.

For narrow refinements, skip full candidate generation. Query only affected domains and preserve the existing system.
<!-- skill-evolver:adaptive-end -->

## Search targeted domains

```bash
python "<skill-dir>/scripts/search.py" "<keywords>" --domain <domain> -n 5
python "<skill-dir>/scripts/search.py" "<keywords>" --stack <stack> -n 5
```

| Need | Domain |
|---|---|
| Product conventions | `product` |
| Style families | `style` |
| Palette logic | `color` |
| Type pairings or fonts | `typography`, `google-fonts` |
| UX, forms, navigation, accessibility | `ux` |
| Landing-page structure | `landing` |
| Icons | `icons` |
| Charts | `chart` |
| Motion | `gsap` |
| React performance | `react` |
| App/native interface rules | `web` |

Use `--json` for programmatic synthesis and `--full` when truncated text hides needed fields. If a search returns zero results, broaden once, then use clearly labeled general guidance. Never invent a dataset match.

## Persist decisions safely

Persist only after selecting a direction:

```bash
python "<skill-dir>/scripts/search.py" "<query>" --design-system --persist -p "<project>" --output-dir "<project-root>"
```

This creates `design-system/<project-slug>/MASTER.md` and optional page overrides. Before writing:

1. inspect existing `MASTER.md` and page override;
2. preserve accepted decisions;
3. use `--force` only when replacement is intentional and authorized;
4. pass `--page "<page>"` for page-specific differences instead of mutating the master.

## Apply by risk priority

Resolve conflicts in this order:

1. accessibility and input usability;
2. task completion and feedback;
3. responsive layout and navigation;
4. performance and content stability;
5. product/brand consistency;
6. typography and color;
7. motion and decorative treatment;
8. charts and optional polish.

Read [references/quick-reference.md](references/quick-reference.md) for full rules. Read [references/pro-rules.md](references/pro-rules.md) before delivering native/mobile app UI.

## Execute and verify

When implementation is authorized:

1. translate the selected system into semantic tokens and reusable components;
2. implement representative states before duplicating patterns;
3. include loading, empty, error, focus, disabled, hover/pressed, and reduced-motion states relevant to scope;
4. render representative desktop/mobile or native-size views;
5. check contrast, keyboard/touch, overflow, content stress, safe areas, motion, and console/runtime errors;
6. fix findings in one batch and confirm once.

For review-only requests, return ranked findings with evidence, impact, and concrete fixes. Do not edit.

## Completion gate

- Recommendations trace to dataset results or are labeled general guidance.
- Chosen system fits product, audience, stack, and incumbent truth.
- Components use coherent tokens rather than isolated magic values.
- Critical accessibility and interaction failures are resolved first.
- Rendered states are coherent, distinctive, responsive, and usable.
- Persisted master and page overrides match the implemented decision.
