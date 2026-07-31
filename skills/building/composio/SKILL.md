---
name: composio
description: Build or repair Composio integrations for AI agents, including scoped sessions, tool discovery and execution, connected-account authentication, MCP exposure, triggers, and multi-app workflows. Use for Composio SDK code, @composio packages, Composio API/MCP setup, OAuth connection flows, or agent actions across services such as Gmail, GitHub, Slack, Notion, and Salesforce.
---

# Composio Integration

Deliver a least-privilege integration that runs for the correct user and account, handles authentication, and proves both read and write paths safely.

## Verify the installed surface

Composio changes quickly. Before coding:

1. Inspect the language, framework, lockfile, installed `composio` or `@composio/*` versions, environment conventions, and existing user/session persistence.
2. Read types and documentation shipped with the installed package.
3. Use current official Composio docs for APIs absent from the package. Pin the dependency version used by the implementation.
4. Treat [sdk-reference.md](sdk-reference.md) and [auth-and-triggers.md](auth-and-triggers.md) as conceptual examples; verify every version-sensitive method, option, tool slug, trigger slug, and response field.

Never invent an action name or infer its arguments. Discover the tool and inspect its schema.

## Model authority first

Write a compact integration contract:

- stable application `user_id` and tenant boundary;
- allowed toolkits and required scopes;
- read actions, reversible writes, sensitive writes, and destructive actions;
- account-selection behavior when a user has multiple accounts;
- session storage, trigger delivery, idempotency key, and audit fields.

Restrict sessions to needed toolkits. Require explicit account selection when ambiguity could send data from or to the wrong account. Never use email address or another mutable identifier as the primary user key.

## Implement the session

- Prefer current session-based APIs for agentic discovery and authentication.
- Create a fresh session for a new task context; persist and reuse the session ID for the same multi-turn context.
- Expose only the provider format the agent framework needs. Use MCP when the client supports it and dynamic discovery reduces context.
- Disable optional remote execution/sandbox features when the workflow does not need them.
- Keep `COMPOSIO_API_KEY` and provider credentials in the project's secret mechanism. Never log keys, OAuth codes, connection links after use, or raw tool responses containing sensitive data.

## Authenticate and execute

1. Check connection state for the target user, toolkit, and account.
2. If authentication is needed, generate the supported connection flow and give the user the consent link. Resume only after active status is verified.
3. Discover the exact tool and input schema.
4. Execute a harmless read or sandbox action first.
5. Normalize large responses outside the model context; retain source IDs and pagination state.
6. Require current user authority before sends, publishes, payments, permission changes, deletes, or other consequential external writes.
7. Record tool name, account alias/ID, request correlation ID, result status, and retry count without sensitive payloads.

## Triggers and multi-app flows

- Verify current trigger availability and payload schema for each toolkit.
- Validate webhook authenticity where supported, deduplicate delivery IDs, make handlers idempotent, and support replay.
- Separate event intake from downstream work with a queue when retries or bursts matter.
- Propagate a correlation ID across apps. Define compensation or human review for partial success.
- Never silently fan out a single event into external messages or updates.

## Test

Test with isolated users/accounts or vendor test environments:

- no connection, active connection, expired/revoked connection, and multiple accounts;
- schema validation, pagination, rate limit, timeout, retry, and partial failure;
- duplicate trigger delivery and replay;
- an approved write to a non-production target;
- tenant isolation and secret redaction.

Run compile/typecheck and relevant tests. Report pinned versions, toolkits/scopes, auth state, verified actions, trigger behavior, and any step awaiting user consent.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for a working least-privilege integration with verified actions, auth lifecycle, retries, and tests.
- Use medium freedom for framework and architecture; obey detected SDK schemas, provider scopes, webhook security, and user authorization.
- Require current action names, auth/idempotency/replay defenses, and a real or sandbox integration test. Revise once when weak.
- Learn only from versioned schemas, corrected fixtures, and observed failure modes.
<!-- skill-evolver:adaptive-end -->
