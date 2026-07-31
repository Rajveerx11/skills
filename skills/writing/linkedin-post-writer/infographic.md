# Professional LinkedIn infographic workflow

Use this workflow only when user asks to create visual media, infographic, launch
graphic, or complete post package. Ordinary writing requests still receive a
specific media recommendation without automatic image generation.

## 1. Lock visual thesis

Turn chosen hook into one visual claim. Graphic must communicate that claim in
under three seconds.

- Keep one headline.
- Use at most three supporting pillars.
- Keep authored graphic copy below 45 words, excluding preserved UI screenshots.
- Prefer proof, architecture, before/after, or one strong number over feature
  collages.

## 2. Gather verified evidence

Read project docs, recent commits, theme tokens, existing assets, and product UI.
Do not guess.

When product has an interface, capture 2–3 fresh states:

1. Primary product surface.
2. Responsive, alternate, or interaction state.
3. Proof state: health, result, verification, success, or measurable output.

Remove desktop clutter. Do not expose secrets, private customer data, tokens,
personal notifications, or irrelevant applications. Keep raw captures.

## 3. Build design brief

Default LinkedIn feed format: 4:5 portrait, target 1080 × 1350.

Specify:

- Exact text, quoted verbatim.
- Brand palette from project tokens.
- Typography direction matching product.
- Composition with clear top, middle, and bottom hierarchy.
- Phone-size legibility.
- Screenshot roles and invariants.
- Explicit avoid list.

Professional floor:

- One accent system.
- Strong contrast.
- Generous negative space.
- No generic AI brains, robots, neon mesh, fake dashboards, decorative glass,
  fabricated charts, or tiny paragraph text.
- No more than one hero screenshot and one supporting screenshot unless carousel
  requested.

## 4. Generate

Use built-in `image_gen` for raster output. Pass real screenshot paths as
references. Require screenshot content and exact copy to remain faithful.

Recommended structure:

1. Hook or product name.
2. One-line thesis.
3. Real product proof.
4. Three-pillar map or one payoff.
5. Small factual footer.

Save output under:

`<project>/assets/linkedin/<slug>-infographic.png`

## 5. Inspect once, fix once

Inspect full-resolution image and a roughly 500-pixel-wide phone preview.

Check:

- Canvas close to 4:5.
- Every authored word spelled correctly.
- No invented claims.
- Main hook readable without zoom.
- Screenshot not distorted.
- No desktop clutter.
- Bottom copy not clipped.
- File size suitable for upload.

If defect exists, run one targeted edit that changes only the defect. Stop after
one confirmation pass.

## 6. Deliver package

Return:

- Copy-paste-ready post.
- First comment containing outbound link when applicable.
- Exactly one alternate hook.
- Primary infographic path.
- Supporting screenshot paths.
- Clear note if assets remain uncommitted.

When external runtime memory is enabled, upsert chosen hook, format, visual type,
and pending result under `~/.skill-data/linkedin-post-writer/` using the stable
artifact ID. Never write runtime state into the skill package.
