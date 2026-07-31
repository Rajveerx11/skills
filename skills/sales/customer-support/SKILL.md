---
name: customer-support
description: Draft, triage, analyze, and improve customer support work, including email/chat replies, ticket queues, escalations, macros, help-center articles, QA reviews, and support workflows. Use when a customer message or support conversation needs an accurate response, internal routing, policy-aware resolution, or reusable support content.
---

# Customer Support

Resolve the customer's actual goal while keeping external claims, account actions, policy, and timelines truthful.

## Gather the case

Extract from the prompt and authorized systems:

- customer request, impact, sentiment, urgency, and desired outcome;
- product/account facts, chronology, prior troubleshooting, and commitments;
- applicable policy, entitlement, SLA, incident status, and ownership;
- missing facts that block a correct resolution.

Do not ask for information already in the ticket or workspace. Ask one consolidated question only when a policy/account fact changes the answer. Never request passwords, full payment data, recovery codes, or unnecessary personal information.

Use [response-templates.md](response-templates.md) for structure and [escalation-guide.md](escalation-guide.md) for general routing patterns. Treat their policies, tiers, and SLA values as examples unless confirmed by the user's organization.

## Triage

Assign:

- concise issue and customer goal;
- category, severity, sentiment, duplicate/incident link;
- owner and next action;
- SLA or follow-up time based on confirmed policy;
- escalation reason and safe internal context.

Escalate security/privacy, account takeover, payment disputes, legal threats, widespread outages, data loss, vulnerable customers, and repeated unresolved failures through the organization's actual process. Do not promise that an escalation, refund, cancellation, restoration, or engineering fix occurred unless the tool result confirms it.

## Draft the response

Use natural language suited to the channel and customer:

1. acknowledge the specific impact without exaggerated apology;
2. answer the question or give the verified resolution;
3. provide the smallest clear steps, including expected result;
4. state ownership and confirmed timing;
5. close with the next checkpoint or exact information needed.

Use the customer's name only when known. Match formality and language, not anger. Avoid blame, jargon, canned enthusiasm, repeated apologies, internal tool details, and impossible guarantees.

Separate:

- **Customer reply:** safe to send externally.
- **Internal note:** diagnosis, evidence, tags, risk, owner, and escalation context.

Drafting does not authorize sending or changing an account.

## Batch queues and reusable content

For multiple tickets, process in stable order, preserve ticket IDs, deduplicate incidents, and output a table/CSV containing triage, draft status, owner, and blockers. Do not merge customer data across tickets.

For macros, parameterize only facts agents can verify and mark policy-dependent fields. For help articles, verify current product UI/behavior, write task-based steps, add troubleshooting and accessibility-friendly image descriptions, then test the steps on the supported version.

## Quality gate

Check:

- every factual claim and action has evidence;
- the actual customer question is answered;
- steps are safe, ordered, and channel-appropriate;
- no private/internal data leaks;
- next owner, action, and time are unambiguous;
- tone is human without being performative.

Return the send-ready draft, internal note/triage, and any action awaiting authorization. When reviewing support quality, cite examples and recommend a concrete coaching change.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for an accurate customer reply plus useful internal triage without inventing company actions.
- Use high freedom for empathy, tone, localization, and structure; use low freedom for policy, account facts, refunds, security, and promises.
- Require separated facts/uncertainty, a reply that answers the real goal, and explicit ownership/escalation/next action. Revise once when weak.
- Learn only from anonymized, explicit CSAT, reopen, escalation, and resolution outcomes.
<!-- skill-evolver:adaptive-end -->
