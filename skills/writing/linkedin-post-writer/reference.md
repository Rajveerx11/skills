# LinkedIn Writing Reference

Loaded at Phase 4 (writing). The orchestration, memory, and learning logic live in `SKILL.md`.

## Hook patterns that work

The hook is the only thing most people read. Keep it 1–2 lines, ideally under ~10 words. Curiosity-gap and contrarian hooks out-engage everything else.

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
- **Listicle** — "5 things I learned shipping X." Skimmable, high saves.
- **Contrarian take** — "Everyone says X. They're wrong." High comments — only with a real opinion.
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

- **3–5 max.** In 2026 they're a topic signal for the algorithm and a discoverability aid — not a growth hack. More looks spammy and dilutes targeting.
- **Mix tiers:** 1 broad (#AI, #SoftwareEngineering) + 2–3 niche (#DeveloperTools, #TestAutomation) + optionally 1 branded (#Tessera).
- Real, searchable tags only. No invented multi-word tags nobody follows. Last line, after a blank line, never inline.

## Format & polish

- Plain text only — LinkedIn renders no markdown (no `**bold**`, no `#` headers, no `-` bullets). Use line breaks and Unicode bullets (•, →, ✅) sparingly.
- Emojis: 0–3, purposeful (section markers or tone), never decorative spam.
- Length: 150–300 words for most posts. Listicles can run longer. Hot takes can be 3 lines.
- Read the first line alone — does it earn the click? If not, rewrite it.
- If there's a link, suggest it as a **first comment** (LinkedIn suppresses reach on posts with outbound links), and supply that comment text.

## Anti-patterns — never do these

- ❌ "I'm thrilled/excited/humbled to announce…"
- ❌ Walls of text with no line breaks
- ❌ 10+ hashtags or hashtag stuffing
- ❌ "Comment 'X' and I'll DM you the link" bait — downranked and distrusted
- ❌ Vague corporate speak with no specifics
- ❌ Fabricated metrics, fake stories, invented quotes
- ❌ Multiple CTAs ("like AND comment AND share AND visit AND subscribe")
- ❌ Outbound link in the post body when reach is the goal

## Worked example

Input: "Wrote a post about Tessera, my local-first AI testing IDE, launched coverage in the sandbox runner."

```
We just taught our AI testing IDE to grade its own homework.

Tessera now runs the test cases it generates — in a locked-down
Docker sandbox, no network — and reports real pass/fail + line coverage.

Generating tests is easy. Trusting them is the hard part.

So we closed the loop:
→ Static analysis maps your code
→ AI drafts the test cases
→ The sandbox actually runs them
→ You see green/red + coverage, locally, no code leaves your machine

Most "AI writes your tests" tools stop at "here's some code, good luck."
The interesting problem was never generation. It was proof.

What would make you trust an AI-written test — coverage, or watching it catch a real bug?

#AI #DeveloperTools #SoftwareTesting #BuildInPublic
```

Link goes in the first comment: "Try it / see how it works → [link]"
