---
name: local-coder
description: Start, verify, reopen, or troubleshoot the user's local Qwen3-Coder model served by llama.cpp. Use when the user asks to launch the local coding model, start llama-server, open its WebUI, expose its OpenAI-compatible local endpoint, change the local context/port profile, or diagnose startup and resource failures.
---

# Local Coder

Use the bundled `launch.ps1`; it owns the tested model path and hardware profile. Starting it consumes substantial RAM/GPU and is authorized only by an explicit launch request.

## Run

Resolve this skill's directory from the loaded `SKILL.md`, then execute:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "<skill-directory>\launch.ps1"
```

Use a command timeout of at least 300 seconds. The launcher is idempotent: it reuses a healthy server and refuses a port owned by a different process.

Supported overrides:

```powershell
# Lower memory profile
powershell -NoProfile -ExecutionPolicy Bypass -File "<skill-directory>\launch.ps1" -Ctx 16384

# Alternate port without opening a browser
powershell -NoProfile -ExecutionPolicy Bypass -File "<skill-directory>\launch.ps1" -Port 8081 -NoBrowser
```

The launcher also accepts `-LlamaDir`, `-ServerPath`, and `-ModelPath`, or the `LLAMA_CPP_DIR`, `LLAMA_SERVER_PATH`, and `LLAMA_MODEL_PATH` environment variables. Prefer these overrides over editing the script.

Do not change `-NCpuMoe`, model, binary, or hardware flags unless the user requests tuning and understands the VRAM risk.

## Verify

After launch:

1. Require a successful launcher exit.
2. Confirm the listener's Win32 process uses the exact server executable and normalized exact `-m`/`--model` path.
3. Query `http://127.0.0.1:<port>/health`.
4. Query `/v1/models` and confirm the intended model is exposed.
5. When the user needs API proof, run one tiny non-destructive completion request and report latency; otherwise avoid consuming extra compute.
6. Record the URL, port, process ID when available, model identity, selected context, and log path printed by the launcher.

- WebUI: `http://127.0.0.1:<port>`
- OpenAI-compatible base URL: `http://127.0.0.1:<port>/v1`

## Diagnose

- Missing binary/model: report the exact checked path. Inspect `models\download.log` when present.
- Low RAM or early exit: read only the relevant tail of the printed error log. Suggest closing heavy apps or `-Ctx 16384` before changing offload flags.
- Port conflict: identify the owning process; do not stop it. Offer another port.
- Timeout: check process state, `/health`, and logs before retrying. Do not start a duplicate.

Never kill all `llama-server` processes by name. To stop the launched server, identify its exact PID/port first and obtain explicit stop authorization.

Return the verified URLs and profile, or the shortest decisive error plus a safe next action.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for the intended local server running with verified model identity, safe resources, and exact process control.
- Use low freedom for model, binary, port, process, and hardware checks; use medium freedom only among proven profiles.
- Require binary/model/resource/port preflight, exact PID and model identity, plus health and inference evidence. Revise once when weak.
- Learn only from explicit benchmark results tied to this model and hardware.
<!-- skill-evolver:adaptive-end -->
