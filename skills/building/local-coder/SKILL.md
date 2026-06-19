---
name: local-coder
description: Launch the local Qwen3-Coder-30B-A3B coding model via llama.cpp and open its WebUI in the browser. Use when the user wants to run their local model, start llama.cpp, launch the local LLM, run Qwen coder locally, spin up the local AI chat, or open the local coding model UI. Trigger phrases include "run my local model", "start local coder", "launch llama.cpp", "fire up Qwen", "/local-coder".
argument-hint: [optional: ctx size, e.g. 16384, or n-cpu-moe override]
auto-activate: false
---

# Local Coder — launch Qwen3-Coder-30B-A3B + WebUI

You start the user's locally-installed llama.cpp server with the Qwen3-Coder-30B-A3B model (MoE-offload tuned for their RTX 4060 8 GB laptop) and open the built-in WebUI.

## What this runs

- llama.cpp: `C:\Users\rajve\llamacpp\llama-server.exe` (CUDA 13.3 build, on PATH)
- Model: `C:\Users\rajve\llamacpp\models\Qwen3-Coder-30B-A3B-Instruct-Q4_K_M.gguf`
- Tuning: `-ngl 99 --cpu-moe` (attention on the 8 GB GPU, experts in system RAM), 32K context, flash attention on, Q8_0 KV cache, jinja tool-calling template on.
- Serves the WebUI + OpenAI-compatible API at `http://127.0.0.1:8080`.

## How to run it

Run the launcher with the PowerShell tool. **Use a long timeout (300000 ms)** — first load reads ~18 GB from disk and can take 1–3 minutes:

```
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\Users\rajve\.claude\skills\local-coder\launch.ps1"
```

Optional overrides (only if the user asks):
- Smaller context (less VRAM / faster load): append `-Ctx 16384`
- More speed by keeping some experts on GPU (only if RAM/VRAM allows): append `-NCpuMoe 44` (lower N = more experts on GPU = faster but more VRAM; risk of OOM)
- Don't open a browser: append `-NoBrowser`

The script is idempotent: if the server is already listening on the port it just re-opens the WebUI instead of starting a second copy.

## After it launches

Tell the user:
- WebUI is open at `http://127.0.0.1:8080`
- Coding agents (Cline / Aider / OpenCode) point at `http://127.0.0.1:8080/v1` (OpenAI-compatible)
- Stop the server with: `Get-Process llama-server | Stop-Process`

## Critical rules

1. Always run `launch.ps1` — do NOT hand-type `llama-server` flags; the tuned, tested config lives in the script.
2. Always use a PowerShell tool timeout of at least 300000 ms so the model has time to load.
3. The model needs ~18 GB of free system RAM. If the script warns about low RAM, tell the user to close Chrome / heavy apps before retrying.
4. If the script reports the model file is missing, it is still downloading — check `C:\Users\rajve\llamacpp\models\download.log` and do not launch until the `.gguf` file is present.
5. If the server exits early, read the printed log tail (`...err.log`) and report the actual error (usually OOM → suggest `-Ctx 16384` or freeing RAM).
6. Do not change the model path or flags unless the user explicitly asks.

## Final note

This is a launch action with side effects (starts a long-running GPU/RAM-heavy server). It is slash-command only (`/local-coder`) and does not auto-activate. Just run the script and report the WebUI URL — keep output short.
