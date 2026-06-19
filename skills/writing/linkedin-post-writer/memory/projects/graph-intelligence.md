# Graph Intelligence (id: graph-intelligence)

Local-first Obsidian plugin that analyzes a vault as a knowledge graph — finds orphans,
clusters, knowledge gaps; suggests links; applies safe repair actions. React dashboard
inside an Obsidian ItemView. LLM + MCP layers optional/opt-in. Privacy-first, all local.

## Author / voice
- Rajveer Vadnal. Posts in **first person**, narrative, "I shipped X because Y bugged me."
- Headline persona: "AI/ML & Python · Real-world engineering · Focused builder."
- Repo link goes in **first comment**, not body.

## Audience
- Primary: devs + builders (Obsidian power users, PKM tool builders, indie hackers).
- Secondary: recruiters/peers (build-in-public credibility).

## What lands for THIS user (engagement evidence)
- Human/narrative post ("Most note-taking systems fail at one critical function...") = 485 impressions.
- Buzzword/architecture post ("Graph Intelligence 2.0 — knowledge infrastructure layer") = 232 impressions.
- => Lead with a real frustration or a single sharp idea. Avoid feature-dump lists and
  "infrastructure layer" abstraction. Narrow > comprehensive.

## Post history / what's been announced
- v1: the original graph-intelligence layer (graph analysis, embeddings, gap detection).
- v2.0: multimodal ingestion (PDF/OCR/YouTube), typed confidence edges, MCP query layer,
  context compression. (Buzzword-heavy — underperformed.)
- v2.1 (2026-06-12 post): **Vault Health Score** (0-100, 4 sub-scores: connectivity/
  cohesion/freshness/discoverability, sparkline trend, "+N since last") + **Note
  Rediscovery** (resurfaces old unlinked semantically-related notes, digest + live modes).
  Also under the hood: unified persistence layer refactor (not posted — invisible to readers).

## Stack (for reference)
Obsidian Plugin API, TypeScript, React 19, Transformers.js local embeddings
(Xenova/all-MiniLM-L6-v2), optional LLM (Ollama/OpenAI/OpenRouter/Anthropic), MCP layer,
GraphML/JSON export. No test suite — verification is `npm run lint` + manual.

## Good hashtags for this niche
#ObsidianMD #PKM #KnowledgeGraph #BuildInPublic #DeveloperTools #SecondBrain #GraphRAG
