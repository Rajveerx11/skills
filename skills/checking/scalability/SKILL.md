---
name: scalability
description: Diagnose, design, implement, and verify software scalability and performance improvements. Use for database/query load, connection pools, caching, queues, background jobs, API throughput, concurrency, rate limiting, backpressure, autoscaling, CDNs, microservices, load tests, capacity planning, or performance bottlenecks under growth.
---

# Scalability

Improve measured capacity or reliability against a real workload and SLO. Do not introduce distributed complexity to solve an unmeasured problem.

## Model the workload

Inspect topology, code paths, data model, deployment, metrics, traces, queries, queue behavior, traffic shape, growth, failure history, and cost. Define:

- request/job mix, payload sizes, read/write ratio, burst and sustained rates;
- latency/error/availability SLOs and consistency requirements;
- current capacity, saturation point, and headroom;
- tenant hot spots, downstream limits, and recovery objectives.

If production telemetry is unavailable, create a representative fixture and label conclusions as test-environment evidence.

Read the relevant reference only:

- [database-scaling.md](database-scaling.md) for queries, indexes, pools, replicas, and partitioning.
- [caching-and-queues.md](caching-and-queues.md) for cache and async patterns.
- [api-and-services.md](api-and-services.md) for API resilience and backpressure.
- [infrastructure.md](infrastructure.md) for deployment, autoscaling, observability, and load tests.

Treat thresholds and sizing formulas as starting hypotheses; derive values from the actual system and provider limits.

## Find the bottleneck

Trace one representative request/job across CPU, memory, database, network, external dependencies, locks, pools, and queues. Rank constraints by evidence and user impact. Distinguish:

- latency from throughput;
- saturation from a leak;
- hot key/tenant from global load;
- downstream throttling from application compute;
- average performance from tail behavior.

## Change the smallest effective layer

Prefer, in order when evidence supports it:

1. remove wasted work or fix query/algorithm behavior;
2. bound work with pagination, streaming, batching, timeouts, and backpressure;
3. tune pools and concurrency against downstream capacity;
4. cache with explicit freshness/invalidation semantics;
5. move durable deferrable work to an idempotent queue;
6. scale compute/data topology;
7. partition or split services only when simpler limits are exhausted.

Preserve consistency, ordering, authorization, tenancy, and retry semantics. Add rollback and observability before production rollout.

## Prove the result

Run a reproducible load test in an authorized safe environment. Include warm-up, steady state, burst, soak when leaks matter, and dependency failure when resilience is in scope. Compare before/after:

- throughput and latency percentiles;
- error/timeout rate;
- CPU, memory, pool/connection saturation, queue depth/age;
- database plans/rows/buffer usage;
- consistency failures, retries, and cost per unit.

Avoid unsafe production load generation. Roll out gradually and stop when an agreed guardrail regresses.

## Completion

Return workload/SLO assumptions, bottleneck evidence, implemented change, test command and data, before/after results with confidence, capacity estimate, cost effect, rollback, and next saturation signal.

<!-- skill-evolver:adaptive-start -->
## Adaptive excellence

- Optimize for measured capacity and reliability improvement against explicit workload and SLOs.
- Use medium freedom for hypotheses and low freedom for thresholds, consistency, data safety, or unmeasured capacity claims.
- Require a workload/topology baseline, load test with rollback, and measured capacity/latency/error/consistency/cost deltas. Revise once when weak.
- Learn only from statistically meaningful project benchmark results.
<!-- skill-evolver:adaptive-end -->
