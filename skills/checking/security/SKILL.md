---
name: security
description: Design, review, harden, or repair web and desktop application security. Use for authentication, authorization, tenancy, APIs, forms, databases, file uploads, SSRF, XSS, CSRF, injection, secrets, cryptography, dependencies, Electron/Tauri IPC, security headers, threat modeling, or evidence-backed vulnerability review and regression testing.
---

# Application Security

Reduce exploitable risk within the user's authorized scope. Do not perform broad exploitation, access unrelated data, or report speculative scanner output as a confirmed vulnerability.

## Establish scope and threat model

Inspect repository instructions, architecture, deployment, trust boundaries, identities, roles, tenant model, sensitive assets, entry points, dependencies, and existing controls. Define:

- attacker capabilities and protected assets;
- authentication, authorization, and ownership rules;
- external inputs and privileged sinks;
- production/test boundary and allowed verification.

Read the relevant reference:

- [web-security.md](web-security.md) for browser/API boundaries and injection.
- [auth-and-secrets.md](auth-and-secrets.md) for identity, tokens, and cryptography.
- [desktop-security.md](desktop-security.md) for Electron/Tauri, IPC, updates, and deep links.
- [database-and-deps.md](database-and-deps.md) for data access and supply chain.

Verify framework/version-sensitive guidance against current official documentation.

## Review systematically

Trace untrusted data from source to privileged sink. Check:

- authentication lifecycle, session fixation/revocation, account recovery, and MFA;
- authorization on every server/IPC boundary, tenant isolation, and object ownership;
- injection, output encoding, CSRF, CORS, SSRF, redirects, file/path handling;
- secret storage/logging, cryptographic purpose and key lifecycle;
- dependency provenance, install scripts, lockfiles, update/signing path;
- abuse controls, rate limits, audit events, and fail-closed behavior.

Use focused static analysis and dependency tooling where available. Never print discovered secrets; report file/location and redact the value.

## Findings

For each finding include:

- title, severity, confidence, CWE/category;
- affected path and trust boundary;
- attacker preconditions and impact;
- minimal reproducible evidence safe for the environment;
- root cause, smallest fix, defense in depth, and regression test;
- uncertainty or compensating control.

Rank severity by exploitability and impact in this system, not a generic label. Separate confirmed, likely, and hardening-only items. Do not recommend rotating a secret without noting that exposed credentials must be revoked/rotated through the owning provider.

## Fix when requested

Implement the smallest root-cause repair while preserving public behavior. Use established libraries and framework-native controls; do not design custom cryptography or authentication protocols. Add negative tests that prove unauthorized, cross-tenant, malformed, replayed, or hostile inputs fail closed.

Run format, lint, typecheck, tests, security checks, and safe reproduction. Re-scan the changed path and inspect the diff for secret leakage.

Consequential operations—credential rotation, account/permission changes, production configuration, destructive proof, or external scanning—require explicit authority.

## Completion

Return scope, threat model, findings by severity/confidence, changed paths, regression and tool evidence, residual risk, and exact operational follow-up. Never claim “secure” or “no vulnerabilities”; state tested coverage and limits.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for evidence-backed risk reduction with exploit path, calibrated severity, fix, and regression test.
- Use low freedom for security invariants/current framework guidance and high freedom for threat hypotheses within authorized scope.
- Require trust-boundary/authz/tenancy/abuse coverage, reproducible evidence with uncertainty, and current fixes plus negative tests. Revise once when weak.
- Learn only from reproduced defects and reviewed false-positive suppressions with owner and expiry.
<!-- skill-evolver:adaptive-end -->
