---
name: greploop
description: Iteratively improves a PR (GitHub), MR (GitLab), or shelved changelist (Perforce) until Greptile gives it a 5/5 confidence score with zero unresolved comments. Triggers Greptile review, fixes all actionable comments, pushes/re-shelves, re-triggers review, and repeats. Use when the user wants to fully optimize a PR/MR/CL against Greptile's code review standards.
---

# greploop

Iteratively improve a PR / MR / changelist until Greptile gives a 5/5 confidence score with zero unresolved comments. Loop: trigger review → fix actionable comments → push → re-trigger.

**Source:** Greptile plugin (cloud-loaded). This is a catalog stub — full body content lives upstream.
