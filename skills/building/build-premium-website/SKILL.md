---
name: build-premium-website
description: Build a complete premium marketing website, company site, product-marketing site, or campaign landing page from a business brief. Use only when the primary deliverable is an end-to-end conversion-focused marketing site with copy, responsive implementation, imagery, and purposeful motion. Route product/app UI and components to frontend-design-skill, portfolios or visual-first redesign direction to design-taste-frontend, targeted critique/polish to impeccable, and UX research or design-system selection to ui-ux-pro-max.
---

# Build Premium Website

Deliver a production-ready marketing site, not a concept or code dump. Preserve the user's stack, brand, content truth, repository conventions, and deployment boundary.

## Route near matches

- Use this skill for a complete marketing/company/campaign site whose job is persuasion and conversion.
- Use `frontend-design-skill` for product interfaces, dashboards, application screens, flows, or standalone components.
- Use `design-taste-frontend` for portfolio work or a visual-first anti-generic redesign where art direction is the main task.
- Use `impeccable` for critique, audit, polish, clarification, adaptation, or targeted improvement of an existing interface.
- Use `ui-ux-pro-max` for UX research, product-pattern selection, design-system guidance, mobile UX, or guideline-driven analysis.

Choose the skill matching the dominant deliverable. Combine skills only when the user explicitly requests multiple distinct outcomes.

## Discover before deciding

Inspect the workspace first:

- Read repository instructions, package files, routes, existing components, design tokens, copy, assets, and Git status.
- Reuse the current framework and component system. For a new standalone site, default to React + Vite only when the user gave no stack preference.
- If `.openai/hosting.json` exists, follow the Sites workflow and reuse its project identity.
- Extract company name, offer, audience, proof, CTA, contact details, brand colors, and language from available files or the prompt.
- Separate supplied facts from assumptions. Never invent testimonials, certifications, clients, metrics, addresses, or legal claims.

Ask one consolidated question only when missing information changes the offer, audience, primary CTA, required pages, or irreversible project location. Otherwise choose documented defaults and proceed.

## Shape the site

1. Write a compact internal brief: audience, promise, proof, primary CTA, tone, constraints.
2. Explore two or three meaningfully different art directions internally. Select the strongest by brand fit, memorability, accessibility, implementation cost, and content density.
3. Define one signature visual or interaction. Do not decorate every section equally.
4. Choose the smallest section set that tells a complete conversion story. Typical order: navigation, hero, proof, problem/benefit, offer, process, trust, CTA/contact, footer.
5. Write concrete, audience-specific copy. Make headings informative; avoid generic AI slogans and unsupported superlatives.

Use bundled references selectively:

- [structure.md](reference/structure.md) for section mechanics and the reference implementation map.
- [design-system.md](reference/design-system.md) and [visual-examples.md](reference/visual-examples.md) for visual decisions.
- [animations.md](reference/animations.md) for GSAP and reduced-motion patterns.
- [industry-themes.md](reference/industry-themes.md) and [logo.md](reference/logo.md) for domain-specific motifs.
- [tech-setup.md](reference/tech-setup.md) and [code-snippets.md](reference/code-snippets.md) only for a compatible React/Vite build.
- Treat `full-reference-*` files as pattern sources, never as copy or mandatory architecture.

## Implement end to end

- Modify the existing site in place unless the user asked for a separate project.
- Build real navigation, routes, forms, buttons, and responsive states. A mock submission must be visibly labeled; do not imply data was sent.
- Reuse local brand assets. When sourcing or generating imagery is authorized, save durable local files, record provenance when relevant, and provide useful alt text.
- Centralize color, type, spacing, radius, shadow, and motion tokens. Keep dependencies minimal.
- Adapt motion to the content. Honor `prefers-reduced-motion`; avoid scroll hijacking and effects that block reading or input.
- Preserve SEO basics: meaningful title, description, heading order, semantic landmarks, share image when available.
- Do not publish, deploy, buy assets, or create external accounts unless requested.

## Verify and improve

Run the repository's install, format, lint, typecheck, test, and production-build commands that apply. Then inspect the rendered site:

- 375px, 768px, and a desktop width;
- keyboard navigation, focus visibility, labels, contrast, and reduced motion;
- primary CTA, navigation, forms, overlays, and error/success states;
- console errors, failed requests, overflow, clipped text, layout shift, and image loading;
- page hierarchy and visual specificity in screenshots.

Fix failures. Critique the weakest of concept, copy, responsiveness, accessibility, performance, or interaction, then revise once.

## Completion

Return the finished path or URL, major design decision, verification commands and results, any intentionally mocked integration, and remaining launch inputs. Do not create extra documentation unless requested.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for a distinctive production site that fits the brand, converts its audience, and works across devices.
- Use high creative freedom for art direction, narrative, layout, and motion. Preserve truthful claims, stack compatibility, accessibility, performance, and functional interactions.
- Require a brief-specific design, passing build/interactions, and responsive keyboard/contrast/reduced-motion evidence. Revise the weakest dimension once.
- Learn only from explicit visual decisions, screenshot deltas, or measured conversion evidence; never self-edit from silence or self-rating.
<!-- skill-evolver:adaptive-end -->
