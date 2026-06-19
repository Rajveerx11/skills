# CHANGELOG — /shorts

Semver: patch = lesson/tweak, minor = new capability, major = workflow overhaul.
Updated as part of the Self-update protocol (see SKILL.md) after every feedback round.

## v2.0.0 — 2026-06-20 (workflow overhaul)
Added **Phase 0 pipeline router**: every request is classified FOOTAGE / PROGRAMMATIC / HYBRID
*before* any engine machinery loads — only the chosen path's skills are pulled (saves time; stops
the full HyperFrames build for footage-led videos). **Default HYBRID** for product-facing channel
content. Programmatic engine **standardized on HyperFrames** (Remotion demoted to a rare escape
hatch; existing Remotion videos kept as-is, not migrated). New `hybrid-pipeline.md` — the
footage/hybrid how-to toward industry-grade SaaS video: Cap capture → HyperFrames transparent-WebM
overlays (`render --format webm`) → DaVinci Resolve assemble/grade/mix → export, plus a quality
checklist. Driven by the goal of a YouTube channel with industry-grade SaaS videos built solo with
AI + free/OSS tools; honest framing that no code engine alone reaches the premium SaaS look — real
footage + grade + overlays does.

## v1.0.0 — 2026-06-19
Initial skill. Workflow: find feature (git/PR history or user-named) → research it (internal repo
truth + external Context7/web context, anti-hallucination contract) → video basics (1 round) →
build ONE HyperFrames-first master prompt using the `remotion-video-prompt` storyboard brain
(Remotion tagged only as fallback) → GATE B approval → render via HyperFrames CLI → feedback loop
→ researched title/description/hashtags (GATE D) → deliver. Self-improving via LEARNINGS/style/
reference/template updates.

Files: `SKILL.md` (orchestration + gates + self-update protocol), `reference.md` (engine routing,
research grounding, copy/hashtag rules, production checklist), `template.md` (HyperFrames-first
master-prompt skeleton with Remotion-fallback block), `style.md` (seeded preferences),
`LEARNINGS.md` (seeded from prior Remotion builds), this changelog.

Built after confirming: HyperFrames installed (v0.6.114, `npx hyperframes`), CLI flow
init→lint→inspect→preview→render, and the existing `remotion-video-prompt` skill's proven
self-learning pattern.
