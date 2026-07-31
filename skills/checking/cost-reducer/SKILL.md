---
name: cost-reducer
description: Find, prioritize, implement, and verify software or infrastructure cost reductions without degrading required reliability, security, or performance. Use for cloud bills, database/query cost, compute sizing, storage and egress, observability spend, CI usage, bundles/images, managed-service comparisons, unit economics, budgets, or FinOps reviews.
---

# Cost Reducer

Produce measured savings, not a list of generic tips. Preserve SLOs, security, compliance, data retention, and operational capacity.

## Establish the baseline

Inspect architecture, provider/region, billing exports or dashboards, utilization, traffic, data growth, commitments, contracts, and existing cost tags. Define:

- comparable billing window and currency;
- total spend and top line items;
- cost per business unit such as request, active user, job, or transaction;
- peak/average workload and required SLOs;
- known seasonality, credits, taxes, one-time charges, and shared costs.

If billing data is unavailable, return a hypothesis-ranked audit with explicit unknowns; do not present guessed savings as fact.

Read only the relevant reference:

- [code-level-savings.md](code-level-savings.md) for queries, bundles, images, caching, and memory.
- [cloud-and-infra.md](cloud-and-infra.md) for compute, storage, networking, serverless, and CI.
- [services-and-finops.md](services-and-finops.md) for vendors, observability, and unit economics.

Treat all prices and percentage examples in references as illustrative. Verify current official pricing for the exact provider, region, tier, and date.

## Build the opportunity register

For each candidate, record:

- evidence and affected resource;
- current monthly cost and usage driver;
- proposed change;
- monthly/annual gross savings range;
- migration and ongoing cost;
- net savings, confidence, effort, risk, SLO effect, and rollback;
- measurement window and owner.

Rank by annual net savings × confidence, then effort and risk. Prioritize idle resources, waste, and obvious routing mistakes before architecture changes.

## Implement safely

When the user asked for changes:

1. Take a configuration/code snapshot and identify rollback.
2. Apply the smallest reversible change to one workload or environment.
3. Preserve retention/legal requirements and redundancy.
4. Add or retain performance, error-rate, saturation, and cost telemetry.
5. Run functional and performance tests.
6. Roll out gradually where production impact exists.

Do not purchase commitments, resize/delete production resources, change retention, move regions, downgrade support, or alter redundancy without explicit authority. Never trade hidden reliability or engineer time for superficial cloud savings.

## Measure

Compare normalized before/after windows:

```text
net monthly savings =
  avoided provider cost
  - new provider cost
  - amortized migration cost
  - added operating cost
```

Check throughput, latency percentiles, errors, availability, capacity headroom, and business unit volume. Mark savings as projected until an invoice or reliable usage measurement confirms them.

## Completion

Return a ranked register, implemented changes, exact evidence sources/dates, validation results, realized versus projected savings, rollback, and next measurement date. Do not claim precision unsupported by the input.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for measurable savings ranked by annual impact, confidence, effort, risk, and SLO effect.
- Use medium freedom for hypotheses and low freedom for prices or savings claims. Use current billing evidence, reversible experiments, and rollback.
- Require an explicit baseline, current provider evidence, and normalized post-change cost/performance measurements. Revise once when weak.
- Learn only from comparable billing windows and verified cost-per-unit deltas.
<!-- skill-evolver:adaptive-end -->
