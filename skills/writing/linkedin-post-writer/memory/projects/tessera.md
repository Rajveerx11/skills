# Tessera (id: tessera)

Local-first AI testing IDE. Generates test artifacts (context, test plans, test cases,
defect/bug reports) from a codebase via tree-sitter static analysis + RAG over a local
vector index, then an LLM (Ollama default; OpenAI/Anthropic/Gemini/OpenRouter optional).
Opt-in local Docker sandbox runs the generated JS/TS + Python tests for real → pass/fail
+ line coverage. Code never leaves the machine on the default path. MIT, free.
Repo: https://github.com/neuratile/Tessera

## Author / voice
- Rajveer Vadnal. First person, narrative, "I shipped X because Y bugged me."
- Repo link goes in the FIRST COMMENT (LinkedIn) / REPLY (X), NEVER the body. Hard rule.

## Audience
- Primary: devs + builders (people who ship code and skip tests), indie hackers, QA/SDETs.
- Secondary: recruiters/peers — build-in-public credibility.

## Wedge / differentiation (lead with this)
- Local-first / privacy: code never leaves your machine (vs cloud AI-testing tools).
- Actually EXECUTES tests in a Docker sandbox (pass/fail + coverage), not just generates
  text. This "proof it runs" beat is the strongest separator. AI-testing is now a known
  category (TestZeus/Hercules), so the wedge must be local + execution, not "AI writes tests".

## Stack (reference)
React 19 + TS + Tailwind v4 (Vite) in Tauri 2, Rust backend, SQLite + sqlite-vec,
tree-sitter (JS/TS/Python), Docker sandbox runners (docker-js, docker-py).

## Assets
- 60s Remotion intro video at C:/Tessera-Intro-Video/out/tessera-intro.mp4 (1080p, ~16MB).
  Video hook = "Every team ships code fast. The tests never keep up." Upload native.

## Good hashtags
#OpenSource #DeveloperTools #AITesting #BuildInPublic #SoftwareTesting #TestAutomation
