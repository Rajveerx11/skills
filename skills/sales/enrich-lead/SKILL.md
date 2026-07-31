---
name: enrich-lead
description: Enrich one or many legitimate business leads from a name, company, domain, work email, or public professional profile into a sourced contact-and-company brief. Use for lead research, CRM enrichment, duplicate cleanup, account intelligence, provenance/confidence checks, or sales next-action planning. Never guess contact details or bypass platform access controls.
---

# Enrich Lead

Return useful professional facts with provenance, freshness, confidence, and conflicts. This skill works with available connected data providers or public sources; it does not assume an Apollo plugin exists.

## Define the job

Parse one lead or a batch file. Determine:

- legitimate business purpose and target role/company;
- fields needed, jurisdiction, and output format;
- whether the user has an authorized provider connection;
- maximum research depth and whether outreach drafting is requested.

Default to public business/professional data needed for B2B evaluation. Do not collect sensitive personal data, private profiles, personal contact details unrelated to work, or data obtained by bypassing login, CAPTCHA, paywalls, robots controls, or platform terms.

## Research in source order

1. Normalize the input identity: name, company, domain, supplied URL/email.
2. Use an authorized connected enrichment provider when available. Discover its exact tool/schema; never invent provider fields.
3. Verify identity against the company site and other first-party pages.
4. Use reputable public professional/business sources for missing fields.
5. Cross-check high-impact facts such as current employer, title, domain, and company status.
6. Record source URL/provider, retrieval date, and whether each value is direct, derived, or unverified.

Never generate an email address from a naming pattern and present it as found. Label email verification method and result. Flag stale or contradictory facts instead of silently choosing one.

## Confidence

- **High:** current first-party record or two independent current sources agree.
- **Medium:** one credible current source or multiple older sources agree.
- **Low:** ambiguous identity, stale source, indirect inference, or unresolved conflict.

Do not assign a single high confidence when critical fields conflict.

## Output

Return:

- input and resolved identity;
- name, current title, company, domain/site, public professional URL;
- work email/phone only when directly sourced and permitted;
- company industry, location, size range, offer, and relevant current signals;
- field-level sources, checked date, confidence, conflicts, and missing fields;
- two or three ethical next actions based on verified facts.

For batches, retain raw evidence and use `scripts/merge_leads.py` to normalize and deduplicate provider/public exports:

```powershell
python "<skill-directory>\scripts\merge_leads.py" input-a.csv input-b.json --output enriched-leads.csv
```

Process in resumable batches with stable input IDs. Review conflicts and low-confidence matches manually before CRM import.

## Outreach boundary

Draft truthful personalization from verified professional facts. Do not imply familiarity, scrape personal trivia, or manufacture pain. Respect consent, opt-out, suppression lists, anti-spam rules, and company policy. Never send, import to a CRM, or update records unless explicitly requested and authorized.

Report source coverage, dedup count, conflicts, low-confidence rows, output path, and research limits.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for a verified contact/company brief with provenance, confidence, and ethical next actions.
- Use medium freedom for research depth and sales framing; preserve privacy, source terms, consent boundaries, and uncertainty.
- Require field-level sources/confidence, surfaced conflicts/staleness, and jurisdiction-appropriate next actions. Revise once when weak.
- Learn only from verified field corrections, source reliability evidence, and explicit outreach outcomes.
<!-- skill-evolver:adaptive-end -->
