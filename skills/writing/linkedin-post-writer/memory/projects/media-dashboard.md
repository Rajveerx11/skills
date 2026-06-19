# Media Dashboard (id: media-dashboard)

Personal, PRIVATE, just-for-himself dashboard (NOT open source, NOT deployed —
runs locally). Aggregates everything Rajveer follows into one page so he doesn't
have to chase 20 tabs/apps to stay current on AI + world news.

What it does:
- 19 YouTube channels (10 AI builders + 9 podcasts) via free RSS — new uploads land automatically.
- Daily news digest across AI/ML, Politics, Geopolitics: Google News RSS (free) -> OpenRouter LLM
  summarizes the last 24h into a digest (not raw headlines).
- AI Tools & Launches feed: Show HN, GitHub trending (daily), Product Hunt — LLM filters to the
  genuinely AI-relevant ones. (Replaced an earlier Music section.)
- WebSub instant push + in-app notifications + NEW badges. Daily cron ingest + on-demand "Fetch latest".
- All free RSS, no paid APIs. "Audience of one."

## Author / voice
- Rajveer Vadnal. First person, narrative, longer origin-story arc ("a few months back I built...").
- Repo is PRIVATE (github.com/Rajveerx11/media-dashboard) and app not deployed.
  => For posts about this project: NO repo link, NO first-comment link, NO "fork it". It's personal.

## Audience
- Peers, devs/builders, recruiters. People who keep asking him "how do you keep up with AI?".

## Angle that works (the wedge)
- The recurring question people ask him IS the hook: "how do you stay updated on AI?".
- Reframe: he stopped trying to keep up; built a FILTER, not another feed. Consume less, on purpose.
- Goal for the first post = REPLIES (CTA flips the question back: "what's in your stack?").

## Stack (reference)
Next.js App Router · Supabase (Postgres) · Vercel (cron) · OpenRouter (nex-agi/nex-n2-pro:free)
for digests · free Google News + HN + GitHub-trending + Product Hunt RSS · WebSub push.

## Assets
- None in repo. App is local-only -> any visual must be a FRESH capture from localhost
  (screen recording of the one-page dashboard preferred).

## Good hashtags
#AI #BuildInPublic #LearningInPublic #DeveloperTools #AINews
