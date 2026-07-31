# Hosted connecting and publishing

This file governs hosted delivery only: finding the Plan MCP connector,
publishing one approved hosted artifact, and restoring the connector when its
tools are missing. Read it after hosted delivery has been explicitly selected.
Delivery selection remains governed by `SKILL.md`.

<!-- SHARED-CORE:connection START -->

**Once hosted delivery is approved, publish through the Plan MCP connector and
return its absolute URL.** Do not silently replace that selected deliverable
with an inline plan. If hosted delivery cannot complete, preserve the authored
source, report the connector problem, and offer local MDX or chat only as an
explicit delivery change.

**The connector is usually the `plan` server**, but older installed agents may
expose the same hosted connector as `agent-native-plans` — both names are valid,
so never report the connector as missing just because it is named
`agent-native-plans` instead of `plan`. Some clients also lazy-load connector
tools through a deferred tool registry instead of showing the namespace upfront.
Before declaring the connector missing, search/load tools with the host's
discovery surface (`tool_search` when available) for `create_visual_plan`,
`create_visual_recap`, or `get_plan_blocks`, then use the tools it exposes.

**If tools remain missing after discovery, do not claim hosted publication
succeeded.** The usual cause is a connector that did not finish connecting this
session, not necessarily an auth problem. Give the exact restore step for the
current client, retain local source, and offer the user the local/chat fallback:

- **Codex / Codex Desktop:** run
  `npx -y @agent-native/core@latest reconnect https://plan.agent-native.com --client codex`
  and start a new Codex session.
- **Claude Code:** run `/mcp` and choose Authenticate/Reconnect, or run the same
  reconnect command with `--client claude-code` and restart Claude.

The same applies when a Plan tool returns `needs auth`, `Unauthorized`, or
`Session terminated`: stop retrying the tool and give the reconnect step instead.

Auth is stored per client config/session, so one client's reconnect does not
make another running client load tools. `--client all` refreshes every local
client config that already has the Plan entry, but each running client still
has to reload its MCP tools afterward. Reconnect re-authenticates without
reinstalling and finds the entry by URL regardless of connector name.

<!-- SHARED-CORE:connection END -->
