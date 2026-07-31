---
name: design-taste-frontend
description: Establish strong aesthetic direction and remove generic AI or template-like design from landing pages, portfolios, marketing sites, and focused showcase surfaces. Use when the core problem is visual taste, a signature concept, anti-slop art direction, or translating a subjective brief into distinctive frontend implementation. Not for general app UI audits, dataset-backed pattern lookup, or full premium-site scaffolding.
---

# Design Taste Frontend

Ship a coherent visual point of view, working code, and bounded visual QA. Treat the brief and incumbent product truth as constraints; treat layout, typography, imagery, material, and motion as a creative field.

## Routing boundaries

Use this skill when **aesthetic direction and anti-slop differentiation** are the main job.

Route near misses:

- Existing product UI needing `audit`, `critique`, `polish`, `harden`, `adapt`, `clarify`, or live browser iteration: use `impeccable`.
- A request for searchable style, palette, typography, UX, chart, motion, product, or stack recommendations from the bundled dataset: use `ui-ux-pro-max`.
- A complete premium animated marketing website using the opinionated React + Vite + Tailwind + GSAP workflow: use `build-premium-website`.
- A general production frontend page, component, or application build without an anti-slop/art-direction mandate: use `frontend-design-skill`.

Do not co-trigger multiple frontend skills merely for extra rules. Choose one owner; load another only for a clearly separate subtask.

## Start from evidence

Inspect before asking:

- user brief, audience, desired action, brand cues, content, and supplied assets;
- current routes, framework, dependencies, tokens, fonts, theme, components, and screenshots;
- representative desktop and mobile states;
- existing behavior, accessibility needs, and performance limits.

Infer low-risk details. Ask one consolidated question only when missing information changes brand direction, factual content, scope, or irreversible implementation choices.

## Choose task mode

- **New surface:** establish a fresh visual world compatible with product truth.
- **Targeted evolution:** keep identity and behavior; improve weak dimensions.
- **Full redesign:** preserve content, function, and constraints; replace visual world.
- **Critique only:** diagnose and rank changes; do not edit unless asked.

State a one-line design read containing audience, mood, density, motion, and primary visual device. Do not make the user choose abstract style labels.

<!-- skill-evolver:adaptive-start -->
## Explore, then commit

For subjective work, form three meaningfully different internal directions. Vary composition, type character, imagery or material, and motion logic—not merely colors. Score them against:

1. brief fit and audience;
2. distinctiveness without gimmick;
3. content clarity and conversion or task success;
4. feasibility in the detected stack;
5. accessibility, responsive behavior, and performance.

Commit to the strongest direction. Show alternatives only when requested or two directions remain genuinely tied. Keep one visual thesis across the surface.
<!-- skill-evolver:adaptive-end -->

## Load the operational playbook

Read [references/frontend-craft-playbook.md](references/frontend-craft-playbook.md) before implementation. Load relevant sections:

- new page: sections 0–6, 9, and 14;
- redesign: sections 0–6, 9, 11, and 14;
- motion-heavy work: sections 5–6 plus the chosen motion recipe;
- design-system implementation: sections 2–4 and Appendix A/B;
- Apple-style glass request: Appendix C, including its platform limits;
- reusable block work: section 12.

The playbook's dependency, responsive, accessibility, reduced-motion, production-test, and source rules are hard constraints. Its aesthetic examples are starting points, not templates.

## Execute end to end

1. Build content hierarchy and page rhythm before decorative detail.
2. Reuse real assets and incumbent tokens when they support the direction. Source or generate assets when the brief needs them and available tools allow it.
3. Implement complete responsive states, interaction states, relevant loading/empty/error states, and reduced-motion behavior.
4. Preserve factual copy unless authorized to rewrite it. Never invent proof, customer quotes, metrics, or integrations.
5. Run existing project checks. Add no dependency before verifying it exists or installing it within authorized scope.
6. Render one representative desktop and mobile pass together. Check hierarchy, overflow, contrast, focus, hit targets, broken assets, motion, and console errors.
7. Fix findings in one batch. Confirm once. Stop after the bounded confirmation pass.

## Artifact-level critique

Judge the rendered artifact:

- Does first viewport communicate one clear promise or task?
- Could it belong to any competitor after swapping logo and color? If yes, strengthen the thesis.
- Does typography create hierarchy without relying on size alone?
- Do layout, imagery, and motion express the same idea?
- Are all states usable by keyboard, touch, narrow viewport, and reduced motion?
- Did any flourish reduce comprehension, speed, or trust?

Revise the weakest dimension once when any answer fails.

## Completion

Deliver working files, routes, or components; note checks and viewport coverage; identify missing user-owned assets or factual decisions. Do not return a moodboard when implementation was authorized.
