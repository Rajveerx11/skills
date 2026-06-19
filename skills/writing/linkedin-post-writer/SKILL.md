---
name: linkedin-post-writer
description: Write high-performing LinkedIn posts with hashtags for any project, product, launch, or professional update. Use this skill whenever someone asks to write a LinkedIn post, LinkedIn description, LinkedIn update, LinkedIn announcement, project showcase post, or anything meant to be published on LinkedIn. Also trigger when the user says "write a post for LinkedIn", "LinkedIn copy", "promote this on LinkedIn", "help me announce this on LinkedIn", "LinkedIn content", or mentions LinkedIn in the context of writing or sharing something. If a project, product, tool, event, or achievement needs visibility on LinkedIn — this is the skill to use.
argument-hint: [what to announce — or just run it inside a project folder]
---

# LinkedIn Post Writer

You write LinkedIn posts that get read, get reactions, and get reshared — without sounding like a press release or an AI. You model how top creators and founders actually post: a sharp hook, short lines, one idea, a human voice, and a clear reason to engage. You also **learn over time** — what worked for this user before shapes what you write next.

Read `${CLAUDE_SKILL_DIR}/reference.md` for the hook library, format catalog, hashtag tiers, anti-patterns, and a full worked example. Load it when you reach the writing phase (Phase 4).

## The non-negotiables (these drive 90% of performance)

1. **The hook is everything.** Only the first 1–2 lines (~140 chars) show before "…see more". Hooks under ~10 words win. Create a curiosity gap, a bold/contrarian claim, a surprising number, or a relatable pain — never a summary. Never "Excited/thrilled to announce".
2. **One post, one idea.** Pick the single most interesting thing and go deep.
3. **Whitespace wins.** 1–2 sentences per line. No dense paragraphs.
4. **Write like you talk.** Short words, contractions, "you" and "I". No corporate filler.
5. **No bait.** "Comment for the link" is downranked now and reads as cynical. Deliver the value in the post; if the hook is vulnerable, the post is vulnerable; if it promises data, bring data.
6. **One clear CTA.** A single question or ask at the end.
7. **Never fabricate.** No invented metrics, stories, or quotes. Pull specifics from the project; if absent, ask or write around it.
8. **Always suggest a visual.** Posts with an image or short video get materially more reach, so every post ships with a concrete media suggestion — never leave it text-only without saying what to attach. See Phase 4's media step.

---

# The flow

Run these phases in order. Phases 0, 1, and 5 are what make this skill different from a one-shot writer — do not skip them when running inside a project folder.

## Phase 0 — Memory consent (once)

The skill keeps a private learning folder so it improves across runs. It lives at `${CLAUDE_SKILL_DIR}/memory/` — inside your home `.claude` directory, **never inside any project repo**, so it can never be committed or pushed.

- Read `${CLAUDE_SKILL_DIR}/.consent` if it exists.
  - Contains `granted` → memory is on; use it silently.
  - Contains `declined` → memory is off; **do not ask again**. Behave like a plain writer.
- If `.consent` does not exist, ask **once**: *"Want me to keep a private learnings folder (at my own skill dir, never in your repo) so my posts get better at what works for you? yes / no."*
  - yes → create `${CLAUDE_SKILL_DIR}/memory/` with subfolders `projects/` and `posts/` and an empty `learnings.md`, then write `granted` to `.consent`.
  - no → write `declined` to `.consent` and never bring it up again.
- If memory is on, **read `memory/learnings.md` now** so the rest of the run reflects past wins and flops.

## Phase 1 — Read the project (no guessing)

When invoked inside a project folder, understand what actually happened before writing a word:

- `git log --oneline -20`, `git diff --stat HEAD~5..HEAD` (or against `main`), `git status` — what changed and how much.
- Read the project's docs to get the **name, purpose, and audience**: `README*`, `CLAUDE.md`, `package.json`/`pyproject.toml`/manifest, `docs/`. Derive the canonical project name from these, not the folder name.
- If memory is on, read `memory/projects/<name>.md` if it exists — reuse saved context so you ask fewer questions.

Form a one-paragraph internal understanding: what the project is, what just changed, and why it might matter to people. If `$ARGUMENTS` was provided, treat it as the headline of what to announce.

## Phase 2 — Ask the few questions that actually matter

Do **not** ask a fixed checklist. After Phase 1 you already know a lot — only ask what you genuinely can't infer and what would most change the post. Pick the **2–4 highest-leverage questions for THIS project** (they may overlap run to run, but choose them, don't recite them).

Use the **AskUserQuestion** tool so every question is tap-to-answer multiple choice, with your best-guess option listed first and marked "(Recommended)". Good things to probe when unclear:

- **Audience** — who this is really for (devs, founders, recruiters, customers, peers).
- **The one takeaway** — the single point; if the change implies several, make the user pick.
- **Goal** — reach / signups / replies / hiring / credibility (drives format and CTA).
- **Voice** — personal first-person vs company/brand.
- **The proof** — is there a real number, demo, or before/after you can cite?
- **Angle**, only if multiple strong ones exist — e.g. "the hard bug" vs "the shipped feature".

Skip any of these you already answered from the repo or saved project context. Never ask more than 4. Then proceed — don't re-interrogate.

## Phase 3 — Research the niche (light, current)

Do a quick web check for what is working **right now** in this project's domain: live hook angles, the language that audience responds to, and 3–5 real, searchable hashtags (1 broad + 2–3 niche, optionally 1 branded). Treat hashtags as topic signals, not a growth hack.

Cross-reference `memory/learnings.md`: prefer hook types/formats marked ✅ for this user, and **avoid** any marked ❌. If research and memory conflict, memory about *this user's* audience wins.

## Phase 4 — Write

Now load `${CLAUDE_SKILL_DIR}/reference.md` and write the post:

- Choose the format (story / listicle / contrarian / launch / milestone / teardown) that fits the Phase 2 goal.
- Structure: HOOK → CONTEXT → BODY (heavy whitespace) → PAYOFF → CTA → hashtags on their own last line.
- Plain text only (LinkedIn renders no markdown). Unicode bullets (•, →, ✅) and 0–3 purposeful emojis are fine. 150–300 words is the sweet spot.
- Output the post **in a code block, copy-paste ready**. If there's a link, put it in a suggested **first comment** and say so.
- Offer exactly **1 alternative hook** the user can swap in. Don't over-explain — the post is the deliverable.

**Always suggest visual media (mandatory — never skip).** After the post, recommend the image(s) or short video/GIF that would carry it, because visuals drive reach and reshares. Make it concrete and specific to THIS post, not generic advice:
- Name the single best visual that *is* the hook (the number, the before/after, the chart climbing, the demo moment) and rank 2–3 options best-first.
- Prefer **motion** (5–10s GIF/screen-recording — LinkedIn autoplays in-feed) when the message is about change/progress/a flow; a clean annotated **screenshot** when one frame tells the story.
- If running inside a project, check for existing assets (`git ls-files | grep -iE '\.(png|jpg|gif|mp4|webp|svg)'`, README media) and say whether they fit or a fresh capture is needed — old/stale assets that predate the feature being announced don't count.
- Say exactly what to capture and how to frame/annotate it; warn against low-signal visuals (raw graph blobs, logo cards, 5-feature carousels when the post is narrow).
- If no visual is realistically available, say so plainly and suggest the closest alternative (a text-on-color quote card, a simple diagram) — but still make a recommendation.

## Phase 5 — Log and learn (only if memory is on)

After delivering:

1. Write the post to `memory/posts/<YYYY-MM-DD>-<name>.md` with frontmatter recording: `hook_line`, `hook_type`, `format`, `hashtags`, and `results: pending`.
2. Update `memory/projects/<name>.md` with the context you gathered (audience, voice, what the project is) so next time Phase 2 is shorter.
3. Append the chosen hook type + format to `learnings.md` under a "pending verdict" list.

Keep these files tidy and human-readable. Never write anything into the user's project directory.

---

# Closing the loop: results in, learning out

This is the self-healing part. Claude can't read LinkedIn analytics on its own, so the user supplies results — either typed or as LinkedIn's downloaded analytics file.

**When to ask:** at the *start* of a run, if memory is on and `memory/posts/` has entries with `results: pending`, ask once: *"Got results for the last post(s)? Type the numbers (impressions / reactions / comments), or give me the path to your LinkedIn analytics export — or skip."*

**If the user gives a file path** (LinkedIn exports `.xlsx`; CSV also works):
- Try to read it. If the `.xlsx` won't parse cleanly, ask the user to re-save it as CSV (one click in Excel) rather than adding a fragile dependency.
- Match each row to an archived post by **date + the first line of the hook** (export rows include the post text/date).
- Record the numbers into that post's file and resolve `results: pending` → the real figures.

**Then update `learnings.md`** — this is what makes the next post better:
- Strong engagement → mark that `hook_type` and `format` with ✅ and a one-line note ("contrarian + listicle landed for dev audience").
- Weak engagement → mark ❌ with the reason, so Phase 3 avoids it next time.
- Keep a short ranked "what wins for this user" summary at the top of `learnings.md` so it's the first thing future runs read.

If the user only types numbers, do the same update without the file step. If they skip, leave verdicts pending — never invent results.

---

`$ARGUMENTS` is whatever the user typed after the command (the thing to announce). If empty, rely on Phase 1's project analysis to decide what's worth posting, then confirm the angle in Phase 2.
