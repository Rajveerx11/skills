# LinkedIn Writing Reference

Load during drafting. Orchestration and external runtime-state rules live in `SKILL.md`.

## Hook patterns

The opening is the first editorial promise. Keep it concise enough to scan, but prefer specificity and truth over a fixed word count. Use a pattern only when the body earns it.

- **Specific number** — "We cut test-gen time from 40 min to 90 seconds."
- **Curiosity gap** — "The bug took 3 days to find. The fix was one character."
- **Contrarian** — "Most AI coding tools solve the wrong problem."
- **Narrative mid-scene** — "I almost shipped a feature nobody asked for."
- **Stakes / pain** — "This nearly broke production at 2am."
- **Before/after** — "6 months ago this was a weekend hack. Today it's live."

**Never open with:** "Excited to share", "I'm thrilled", "Humbled to announce", "Check out my new". They signal "skip me".

**Match hook to body.** If the hook is vulnerable, the post is vulnerable. If it promises data, bring data. A dramatic hook over a generic tip-list reads as bait-and-switch.

## Formats — pick one, match it to the goal

- **Story / build-in-public** — "I spent 3 months on X. Here's what broke." Best for projects and lessons.
- **Listicle** — "5 things I learned shipping X." Useful when the points form a real set.
- **Contrarian take** — "Everyone says X. They're wrong." Use only with a defensible opinion and evidence.
- **Launch** — problem → what you built → who it's for → proof → CTA. For products/features.
- **Milestone / gratitude** — wins, hires, anniversaries. Specific, not humblebrag.
- **Teardown / how-to** — concrete tactical value. High saves and follows.

## Structure

```
[HOOK]      ← 1–2 lines. Stop the scroll. Above the fold.
[blank]
[CONTEXT]   ← Why this matters / the setup. 1–3 short lines.
[BODY]      ← The meat. Story beats or a list. Heavy whitespace.
[PAYOFF]    ← The insight, result, or takeaway.
[CTA]       ← One question or one ask.
[hashtags]  ← 3–5, own line, very bottom.
```

## Hashtags

- Hashtags are optional. Use a small set only when they help readers classify or find the topic.
- Prefer real, recognizable topic labels over invented multi-word tags.
- Put them on the last line when used. Verify current platform guidance before claiming algorithmic benefit.

## Format & polish

- Plain text only — LinkedIn renders no markdown (no `**bold**`, no `#` headers, no `-` bullets). Use line breaks and Unicode bullets (•, →, ✅) sparingly.
- Emojis: 0–3, purposeful (section markers or tone), never decorative spam.
- Length follows the idea. Remove lines that do not add evidence, tension, explanation, or payoff.
- Read the first line alone — does it earn the click? If not, rewrite it.
- If a link would distract from the post or the user's established practice favors a first comment, supply that comment text. Do not assert a reach penalty without current evidence.

## Anti-patterns — never do these

- ❌ "I'm thrilled/excited/humbled to announce…"
- ❌ Walls of text with no line breaks
- ❌ Hashtag stuffing
- ❌ "Comment 'X' and I'll DM you the link" bait — downranked and distrusted
- ❌ Vague corporate speak with no specifics
- ❌ Fabricated metrics, fake stories, invented quotes
- ❌ Multiple CTAs ("like AND comment AND share AND visit AND subscribe")
- ❌ Unnecessary outbound links that interrupt the post's main action

## Worked example

Synthetic input: "Our deployment tool now validates configuration before a release starts."

```
The cheapest failed deployment is the one that never starts.

This week we added a preflight step to our deployment workflow.

Before a release can run, it now checks:
→ required configuration
→ environment access
→ migration readiness
→ rollback instructions

If any check fails, the release stops before touching production.

The code was not the hard part.

The hard part was deciding which failures must block a deploy and which should
remain warnings.

What belongs in your deployment preflight?

#DevOps #DeveloperTools #SoftwareEngineering
```

If the user has a verified demo link, supply concise first-comment text.
