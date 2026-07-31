---
name: paper-mcp
description: Inspect and edit the currently open Paper board through its local MCP server, including node reads, selection-aware HTML insertion, image placement, screenshots, and export/finalization. Use when the user asks to create, modify, or inspect a Paper canvas and the local Paper MCP connection at 127.0.0.1:29979 is available.
---

# Paper MCP

Edit the live Paper board through callable Paper MCP tools. Do not rely on a nonexistent local wrapper or expose internal node IDs to the user.

## Connect and inspect

1. Discover the Paper MCP toolset already connected to the agent. If it is unavailable, check whether the local Paper app/server is running at `http://127.0.0.1:29979/mcp`; report the connection blocker rather than inventing CLI commands.
2. Call `get_guide` with topic `paper-mcp-instructions` once per session.
3. Call `get_basic_info` and `get_selection`.
4. Inspect relevant nodes and take a baseline screenshot before meaningful edits.
5. Derive artboard size, selection scope, existing layout, typography, color, spacing, and layer naming from the board.

Ask only when the intended artboard/selection is ambiguous or an edit would replace/delete existing work.

## Edit efficiently

- Batch coherent insertions with `write_html`; use small follow-up patches for refinements.
- Target exact inspected node IDs and preserve unrelated layers.
- Use semantic layer names and existing board tokens.
- Place local images through the exact asset URL form documented by the live `get_guide`, using absolute validated paths.
- Keep text editable where possible. Use raster assets only when they add real value.
- Avoid deletion. Obtain explicit confirmation immediately before deleting or replacing material board content.

## Verify and finish

After each meaningful batch:

1. Take a screenshot and compare layout, clipping, alignment, hierarchy, and content against the request.
2. Inspect changed nodes when screenshot evidence is ambiguous.
3. Correct the weakest visible issue once.
4. Call `finish_working_on_nodes` even after a recoverable error.

Export only when requested and verify the returned artifact/path. Report the visible result and export, not raw node IDs or verbose MCP payloads.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for accurate Paper canvas edits through the live session with visual verification.
- Use medium freedom for batching and layout; use low freedom for board identity, node IDs, deletion, and write confirmation.
- Require inspected board/selection, exact write targets that preserve unrelated work, screenshot evidence, and successful finalization. Revise once when weak.
- Learn board style tokens only from explicit approval and persist them only when asked.
<!-- skill-evolver:adaptive-end -->
