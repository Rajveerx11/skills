---
name: playwright-skill
description: Automate and test websites with Playwright, including local dev-server discovery, browser flows, forms, authentication, screenshots, responsive and accessibility checks, network inspection, link validation, and reproducible regression scripts. Use when browser-rendered behavior or visual evidence must be exercised rather than inferred from source.
---

# Playwright Browser Automation

Create deterministic browser evidence and leave no generated files in the skill directory.

## Resolve the target

1. Resolve this skill's directory from the loaded `SKILL.md`.
2. Read the target repository instructions, scripts, routes, auth fixtures, and current server configuration.
3. Use a URL supplied by the user or project first. For localhost with no URL, run:

```powershell
node -e "require('<skill-directory>/lib/helpers').detectDevServers().then(x => console.log(JSON.stringify(x)))"
```

Use one unambiguous server. If several remain plausible after repository inspection, ask once. Do not start, stop, or restart a server without checking project instructions and current processes.

## Prepare a focused script

Write the source script under the operating system temp directory, never inside the skill or project. Parameterize the URL and output directory. Execute through the bundled runner:

```powershell
node "<skill-directory>\run.js" "<temporary-script.js>"
```

The runner copies code to a transient executable beside its dependencies, waits for completion, and deletes that copy. If Playwright is missing, run `npm run setup` in the skill directory only after dependency installation is authorized.

Default to headless execution for repeatability. Use headed mode for user-visible debugging or when the task explicitly needs it.

## Write resilient automation

- Prefer role, label, placeholder, text, and test-ID locators over CSS structure.
- Assert the expected state after each meaningful action.
- Wait on locators, URLs, responses, or load state; avoid fixed sleeps except for intentional animation sampling.
- Create isolated browser contexts. Use project-provided test accounts or storage state; never hardcode credentials or print secrets.
- Capture console errors, page errors, failed requests, and the final URL.
- Save screenshots/traces only to a task output/temp directory and report exact paths.
- Close browser/context in `finally`.

Use [API_REFERENCE.md](API_REFERENCE.md) for specialized patterns. Inspect [lib/helpers.js](lib/helpers.js) before relying on helper behavior.

## Test the requested risk

Choose the smallest relevant matrix:

- critical happy path plus validation/error path;
- mobile, tablet, and desktop for responsive work;
- keyboard/focus and accessible names for interactive UI;
- authenticated and unauthorized states for access control;
- duplicate submit, retry, back/forward, refresh, and slow/failing network for stateful flows.

For external sites, stay within the user's authorized account and intended actions. Do not bypass login, CAPTCHA, access controls, rate limits, or site terms. Treat submits, messages, purchases, deletions, and account changes as consequential external actions requiring current authority.

## Report

Distinguish assertion failures, product defects, environment failures, and automation defects. Include target URL, tested scenarios/viewports, pass/fail counts, shortest decisive evidence, artifact paths, and a reproducible command. Do not claim visual quality from a screenshot that was not inspected.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for a reliable browser run with resilient locators, assertions, diagnostics, and cleanup.
- Use high freedom for exploration/test design and low freedom for credentials, isolation, external actions, and success claims.
- Require correct target/browser discovery, user-visible assertions, useful failure artifacts, and verified process/temp cleanup. Revise once when weak.
- Learn only from reproduced failures and accepted project-local selectors/page objects.
<!-- skill-evolver:adaptive-end -->
