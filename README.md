# Agent Skills Portfolio

Canonical source for 60 skills shared across Codex, Claude Code, and the common agent-skills root.

Each skill is outcome-driven: strong model judgment where work is subjective, exact guardrails where correctness or safety is fragile, reusable scripts for repeated operations, and observable quality gates.

## Portfolio workflow

```powershell
python skills/workspace/skill-evolver/scripts/run_release_checks.py .
python skills/workspace/skill-evolver/scripts/sync_portfolio.py . --prune --details
python skills/workspace/skill-evolver/scripts/sync_portfolio.py . --apply --prune
python skills/workspace/skill-evolver/scripts/sync_portfolio.py . --verify-only
```

`skills-manifest.json` controls install targets. Applied exact sync stages every change, backs up overwritten or pruned files under `~/.skill-evolver/backups`, writes a receipt, excludes runtime state, rolls back on failure, and verifies hashes. Personal profiles, logs, outcomes, caches, and temporary execution files are never canonical repository content.

## Categories

- **building** — applications, integrations, automation, and developer tooling
- **checking** — review, testing, safety, cost, scale, and release quality
- **design** — product, interface, visual-system, and presentation design
- **sales** — support, lead research, enrichment, and outreach
- **video** — video production, motion, captions, media, and HyperFrames
- **workspace** — skills, planning, learning, notes, and session operations
- **writing** — research, posts, proposals, resumes, slides, and communication

## building

- **[build-premium-website](skills/building/build-premium-website/SKILL.md)** — Build a complete premium marketing website, company site, product-marketing site, or campaign landing page from a business brief.
- **[code-structure](skills/building/code-structure/SKILL.md)** — Diagnose and refactor duplicated operational logic into appropriate shared services without changing behavior.
- **[composio](skills/building/composio/SKILL.md)** — Build or repair Composio integrations for AI agents, including scoped sessions, tool discovery and execution, connected-account authentication, MCP exposure, triggers, and multi-app workflo…
- **[frontend-design-skill](skills/building/frontend-design-skill/SKILL.md)** — Design and implement production-grade product frontend code, including application screens, dashboards, interactive flows, data-heavy pages, and reusable components.
- **[genmedia](skills/building/genmedia/SKILL.md)** — Use the genmedia CLI to discover, inspect, price, run, queue, download, and manage fal.ai media endpoints.
- **[local-coder](skills/building/local-coder/SKILL.md)** — Start, verify, reopen, or troubleshoot the user's local Qwen3-Coder model served by llama.cpp.
- **[n8n](skills/building/n8n/SKILL.md)** — Design, build, import, export, test, or repair n8n workflows, expressions, custom nodes, webhooks, credentials, and API/CLI automation.
- **[paper-mcp](skills/building/paper-mcp/SKILL.md)** — Inspect and edit the currently open Paper board through its local MCP server, including node reads, selection-aware HTML insertion, image placement, screenshots, and export/finalization.
- **[trigger-dev](skills/building/trigger-dev/SKILL.md)** — Build, test, deploy, or debug durable Trigger.dev background tasks and scheduled workflows in TypeScript.

## checking

- **[cost-reducer](skills/checking/cost-reducer/SKILL.md)** — Find, prioritize, implement, and verify software or infrastructure cost reductions without degrading required reliability, security, or performance.
- **[greploop](skills/checking/greploop/SKILL.md)** — Iterate on a GitHub pull request, GitLab merge request, or Perforce shelved changelist until current Greptile findings are resolved and its reported confidence target is met.
- **[playwright-skill](skills/checking/playwright-skill/SKILL.md)** — Automate and test websites with Playwright, including local dev-server discovery, browser flows, forms, authentication, screenshots, responsive and accessibility checks, network inspection,…
- **[roast](skills/checking/roast/SKILL.md)** — Pressure-test a business, product, feature, or go-to-market idea and return a decisive GO, RESHAPE, TEST, or KILL recommendation.
- **[scalability](skills/checking/scalability/SKILL.md)** — Diagnose, design, implement, and verify software scalability and performance improvements.
- **[security](skills/checking/security/SKILL.md)** — Design, review, harden, or repair web and desktop application security.
- **[task-to-pr](skills/checking/task-to-pr/SKILL.md)** — Take one scoped task, ticket, issue, bug, or existing pull request through implementation, testing, independent review, publication, and CI until the pull request is ready for human merge.

## design

- **[design-taste-frontend](skills/design/design-taste-frontend/SKILL.md)** — Establish strong aesthetic direction and remove generic AI or template-like design from landing pages, portfolios, marketing sites, and focused showcase surfaces.
- **[impeccable](skills/design/impeccable/SKILL.md)** — Operate on an existing frontend interface through the Impeccable command suite.
- **[paper-deck-style](skills/design/paper-deck-style/SKILL.md)** — Create, extend, or restyle premium slide decks on Paper boards.
- **[ui-ux-pro-max](skills/design/ui-ux-pro-max/SKILL.md)** — Query and apply the bundled UI/UX design-intelligence dataset for web, mobile, desktop, and cross-platform products.

## sales

- **[customer-support](skills/sales/customer-support/SKILL.md)** — Draft, triage, analyze, and improve customer support work, including email/chat replies, ticket queues, escalations, macros, help-center articles, QA reviews, and support workflows.
- **[enrich-lead](skills/sales/enrich-lead/SKILL.md)** — Enrich one or many legitimate business leads from a name, company, domain, work email, or public professional profile into a sourced contact-and-company brief.
- **[lead-scrapping-apify](skills/sales/lead-scrapping-apify/SKILL.md)** — Build a compliant local lead-discovery pipeline using an authorized Apify Actor, commonly for public Google Maps business data.

## video

- **[embedded-captions](skills/video/embedded-captions/SKILL.md)** — Add captions to a single-subject talking-head video through one identity catalog backed by Standard, Cinematic, and Theme engines.
- **[faceless-explainer](skills/video/faceless-explainer/SKILL.md)** — faceless-explainer video workflow - arbitrary text (article / notes / topic / brief) becomes narrator_scripts.json, audio (voice + BGM), section_plan.md, and a typography / abstract-graphic…
- **[general-video](skills/video/general-video/SKILL.md)** — Use as the fallback for custom HyperFrames HTML video composition authoring when no specialized workflow fits.
- **[graphic-overlays](skills/video/graphic-overlays/SKILL.md)** — Package an existing talking-head, interview, podcast, or demo video by layering timed graphic overlay cards onto the playing footage: titles, lower-thirds, data callouts, quotes, lists, cha…
- **[hyperframes](skills/video/hyperframes/SKILL.md)** — Create or edit deterministic HyperFrames HTML video compositions: animations, title cards, overlays, captions, voiceovers, audio-reactive visuals, variables, media, sub-compositions, and sc…
- **[hyperframes-animation](skills/video/hyperframes-animation/SKILL.md)** — All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven runtime adapters (GSAP defaul…
- **[hyperframes-cli](skills/video/hyperframes-cli/SKILL.md)** — HyperFrames CLI dev loop — `npx hyperframes` for scaffolding (init), validation (lint, inspect), preview, render, and environment troubleshooting (doctor, browser, info, upgrade).
- **[hyperframes-core](skills/video/hyperframes-core/SKILL.md)** — HyperFrames HTML composition contract.
- **[hyperframes-creative](skills/video/hyperframes-creative/SKILL.md)** — Non-animation creative direction for HyperFrames videos.
- **[hyperframes-media](skills/video/hyperframes-media/SKILL.md)** — Asset preprocessing for HyperFrames compositions — multi-provider TTS (HeyGen / ElevenLabs / Kokoro local), multi-provider BGM (Google Lyria / local MusicGen), Whisper transcription, backgr…
- **[hyperframes-registry](skills/video/hyperframes-registry/SKILL.md)** — Install and wire registry blocks and components into HyperFrames compositions.
- **[motion-graphics](skills/video/motion-graphics/SKILL.md)** — Use when the user wants a short, design-led motion graphic where motion is the message: kinetic typography, stat or number count-up, chart/data-viz hit, logo sting, brand lockup, lower-thir…
- **[pr-to-video](skills/video/pr-to-video/SKILL.md)** — pr-to-video workflow - a GitHub pull request URL, owner/repo pull number, or current checked-out PR becomes verified PR facts, narrator_scripts.json, audio, section_plan.md, and a code-diff…
- **[product-launch-video](skills/video/product-launch-video/SKILL.md)** — Create a product, company, SaaS, app, or site marketing launch video, promo, feature reveal, or product-focused video from a URL, brief, or script.
- **[remotion-to-hyperframes](skills/video/remotion-to-hyperframes/SKILL.md)** — Translate an existing Remotion (React-based) video composition into a HyperFrames HTML composition.
- **[remotion-video-prompt](skills/video/remotion-video-prompt/SKILL.md)** — Turn a raw video idea into a production-ready Remotion generation prompt.
- **[shorts](skills/video/shorts/SKILL.md)** — Turn a recent feature of the current project into a finished YouTube Short or long-form channel video plus publishing metadata.
- **[website-to-video](skills/video/website-to-video/SKILL.md)** — Capture a general website/URL and turn it into a HyperFrames video (site tour, showcase, or social clip from the site's own visuals).

## workspace

- **[create-skill](skills/workspace/create-skill/SKILL.md)** — Create, update, audit, migrate, and validate reusable skills for Codex, Claude Code, or a shared agent-skills repository.
- **[find-skills](skills/workspace/find-skills/SKILL.md)** — Discover, compare, inspect, and optionally install agent skills from the open skills ecosystem.
- **[learn-day](skills/workspace/learn-day/SKILL.md)** — Track daily learning and shipped work, write structured Obsidian notes, calculate weekly consistency, detect evidence-backed learning patterns, and coach the next action.
- **[obsidian-vault-tune-up](skills/workspace/obsidian-vault-tune-up/SKILL.md)** — Audit, reorganize, repair, and improve an Obsidian vault for human navigation and reliable AI retrieval.
- **[plan-day](skills/workspace/plan-day/SKILL.md)** — Turn vague tasks into a realistic time-blocked day, reconcile calendar conflicts, write an approved Obsidian plan, mirror blocks idempotently to a connected calendar, wrap completed work, r…
- **[session-handoff](skills/workspace/session-handoff/SKILL.md)** — Produce a verified, self-contained handoff so a fresh Codex or Claude session can resume without rediscovery.
- **[skill-evolver](skills/workspace/skill-evolver/SKILL.md)** — Audit, enhance, learn from, validate, and synchronize Codex and Claude skills.
- **[visual-plan](skills/workspace/visual-plan/SKILL.md)** — Create structured Agent-Native Plans with diagrams, file maps, annotated code, decision blocks, UI wireframes, and interactive prototypes.

## writing

- **[agent-reach](skills/writing/agent-reach/SKILL.md)** — Retrieve current public content from web pages and supported internet platforms through Agent Reach's multi-backend router.
- **[caveman](skills/writing/caveman/SKILL.md)** — Ultra-compressed communication mode.
- **[frontend-slides](skills/writing/frontend-slides/SKILL.md)** — Create, reconstruct, or improve animated HTML slide decks that run in a browser and print cleanly to PDF.
- **[learn-post](skills/writing/learn-post/SKILL.md)** — Turn today's real learning or shipped work into an authentic build-in-public LinkedIn post, then optionally log the confirmed draft or publication into the user's learn-day system.
- **[linkedin-post-writer](skills/writing/linkedin-post-writer/SKILL.md)** — Write truthful, distinctive LinkedIn posts and, when requested, create matching infographics or launch visuals for projects, products, features, lessons, milestones, events, and professiona…
- **[researcher](skills/writing/researcher/SKILL.md)** — Conduct current, multi-source research and produce decision-ready synthesis with direct citations, uncertainty, contradictions, and actionable recommendations.
- **[resume-tailor](skills/writing/resume-tailor/SKILL.md)** — Tailor a master resume or CV to a specific job description and produce an honest, ATS-readable, recruiter-ready application package.
- **[slideshow](skills/writing/slideshow/SKILL.md)** — Author a HyperFrames slideshow composition — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching sequences, and hotspot navigation.
- **[upwork](skills/writing/upwork/SKILL.md)** — Audit, position, and rewrite truthful Upwork freelancer profiles, headlines, overviews, specialized profiles, skills, project catalog offers, consultations, employment history, portfolios,…
- **[upwork-proposal](skills/writing/upwork-proposal/SKILL.md)** — Evaluate an Upwork job and write one tailored, truthful proposal using the freelancer's verified proof.
- **[youtube-researcher](skills/writing/youtube-researcher/SKILL.md)** — Research YouTube topics, niches, creators, channels, competitors, videos, titles, and transcripts using the bundled SerpApi/Supadata helper.
