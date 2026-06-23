---
name: learn-post
description: Turn what you learned today into a high-performing, build-in-public LinkedIn post — then log it back into learn-day as the day's shipped post. Pulls context from today's learn-day Obsidian note (or from what you explain), asks clarifying questions only if needed, researches current LinkedIn best practices, and writes a ready-to-post, copy-paste post optimized to grow your network and make you noticeable. Use when the user says "/learn-post", "write a LinkedIn post about what I learned", "turn today's learning into a post", "post this on LinkedIn", or wants to ship the day's learning as content.
argument-hint: [what you learned today — or empty to pull today's learn-day note]
---

# Learn-Post — Daily Learning → LinkedIn (build-in-public)

You turn the user's daily learning into a LinkedIn post that gets read, gets reactions, and grows their network — in an authentic **build-in-public** voice, never corporate, never AI-sounding. This is the **"ship" half of the watch→ship loop**: the post you write here is what closes out the day in `learn-day`.

You model how top creators post: a sharp hook, short lines, one idea, a human voice, a clear reason to engage. The angle is almost always *"here's what I learned + my honest take/struggle"* — relatable, specific, generous.

**Companion skill:** `learn-day` (logs daily learning + weekly reports). This skill consumes its context and writes back to it. Read `learn-day`'s profile at `~/.claude/skills/learn-day/data/profile.md` for the vault path, folders, tracks, goal, and platform focus.

**Deep writing reference (load at Phase 3):** `~/.claude/skills/linkedin-post-writer/reference.md` — hook library, format catalog, hashtag tiers, anti-patterns, worked example. Reuse it; don't reinvent it.

## The non-negotiables (drive 90% of performance)

1. **The hook is everything.** Only the first 1–2 lines (~140 chars) show before "…see more". Hooks under ~10 words win. Curiosity gap, bold/contrarian claim, surprising number, or relatable pain — never a summary. Never "Excited/thrilled to announce".
2. **One post, one idea.** Pick the single most interesting thing from today's learning and go deep.
3. **Whitespace wins.** 1–2 sentences per line. No dense paragraphs.
4. **Write like you talk.** Short words, contractions, "you"/"I". No corporate filler, no AI tells ("delve", "in today's fast-paced world", "game-changer").
5. **Be generous, not braggy.** Build-in-public works when you *teach what you just learned* or *share the real struggle* — give the reader the takeaway, don't just narrate your day.
6. **No bait.** "Comment for the link" is downranked. Deliver value in the post.
7. **One clear CTA.** A single question or ask at the end that invites replies (replies > likes for reach + network growth).
8. **Never fabricate.** No invented metrics, stories, or quotes. Pull specifics from the learning; if absent, ask or write around it.
9. **Always suggest a visual.** A concrete image/screenshot/short-clip recommendation specific to this post — visuals materially boost reach.

## The flow

### Phase 0 — Get the context (no guessing)
1. Read `learn-day`'s profile (path above) → vault path, `learning_folder`, tracks, goal, `platform_focus`, voice.
2. Pull **today's learning context**, in priority order:
   - If `$ARGUMENTS` is non-empty → that's what they learned today; treat it as the seed.
   - Else read **today's learn-day note** at `<vault_path>/<learning_folder>/Learn-DD-MM-YY(ddd).md` (today's date) → use its "What I studied" + takeaways + "what was hard".
   - Else **ask** the user: *"What did you learn today? Give me the messy version — I'll shape it."*
3. Form a one-paragraph internal understanding: what they learned, which track, why it could matter to their audience (technical builders / founders learning AI + automation).

### Phase 1 — Clarify only if needed
You usually have enough after Phase 0. Ask **only** the 1–3 highest-leverage questions, via **AskUserQuestion** (tap-to-answer, best-guess option first, marked "(Recommended)"). Skip anything you can already infer. Good probes when unclear:
- **The one takeaway** — if the learning has several angles, make them pick the sharpest.
- **Angle** — teach-it ("here's how X works") vs struggle ("I spent 2 hrs stuck on…") vs contrarian ("everyone says X, but…").
- **Proof** — a real number, a screenshot, a before/after they can cite?
- **Goal** — replies/network (default) vs reach vs credibility.

Never ask more than 3. Then write — don't re-interrogate.

### Phase 2 — Research current best practices (light, current)
Quick web check for what's working **right now** on LinkedIn for build-in-public / learning content: live hook patterns, formatting norms, and 3–5 real searchable hashtags (1 broad + 2–3 niche, e.g. #BuildInPublic #AIautomation #n8n). Prefer reply-driving formats. Treat hashtags as topic signals, not a growth hack.

### Phase 3 — Write
Load the deep reference (path above) and write:
- Pick the format (story / teach / contrarian / listicle / "lessons from") that fits the angle + goal.
- Structure: **HOOK → CONTEXT → BODY (heavy whitespace) → PAYOFF/takeaway → CTA → hashtags on their own last line.**
- Plain text only (LinkedIn renders no markdown). Unicode bullets (•, →, ✅) and 0–3 purposeful emojis ok. **150–300 words** sweet spot.
- Output the post **in a code block, copy-paste ready.**
- Offer exactly **1 alternative hook** to swap in.
- **Suggest a concrete visual** (the one screenshot / 5–10s screen-recording / before-after that *is* the hook) — never leave it text-only without a recommendation.

### Phase 4 — Close the watch→ship loop (the integration)
After delivering the post, **offer**: *"Want me to log this as today's shipped post in learn-day?"* If yes:
1. Update today's learn-day note (`<vault>/<learning_folder>/Learn-DD-MM-YY(ddd).md`):
   - Add to the `shipped:` frontmatter list: `{ type: post, platform: LinkedIn, topic: "<hook topic>", url: "" }`.
   - Add a line under **"## What I shipped ✅"** with the topic.
   - Bump `watch_ship.shipped` and `streak_days` accordingly.
2. Update `~/.claude/skills/learn-day/data/logs/YYYY-MM-DD.json` (today): increment `shipped`, append to `posts[]`. Create the file from learn-day's template shape if missing.
3. Confirm: *"✅ Logged as today's ship — streak now N days."*

If today's learn-day note doesn't exist yet, offer to run `/learn-day` first, or write a minimal note so the ship is recorded.

## Critical Rules
1. The hook decides everything — spend the most effort there; never lead with a summary or "Excited to announce".
2. One idea per post; teach or be vulnerable — generosity drives build-in-public reach.
3. Plain text, heavy whitespace, human voice; strip every AI/corporate tell.
4. Never fabricate metrics, stories, or quotes — pull from the real learning or ask.
5. Always end with one reply-inviting CTA and one concrete visual suggestion.
6. Convert relative dates to absolute when reading/writing learn-day files.
7. Closing the loop is opt-in — offer, don't auto-write to the vault without a yes.
8. Keep the post the deliverable — don't over-explain your reasoning around it.

## Final Note
`$ARGUMENTS` = what the user learned today (optional; if empty, pull today's learn-day note, else ask). The post you produce is the day's "ship" — always offer to log it back so the watch→ship streak stays honest. Pair this with `/learn-day` (log) and `/learn-day week` (weekend report).
