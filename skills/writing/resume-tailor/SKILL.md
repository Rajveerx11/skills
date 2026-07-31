---
name: resume-tailor
description: Tailor a master resume or CV to a specific job description and produce an honest, ATS-readable, recruiter-ready application package. Use for resume tailoring, CV customization, ATS optimization, job applications, role matching, gap analysis, recruiter-facing rewrites, cover letters, and application short answers. Supports pasted text, local files, and job URLs without inventing experience.
---

# Resume Tailor

Maximize credible fit, not keyword score. Preserve a defensible evidence trail from the master resume to every tailored claim.

Read [ats-reference.md](ats-reference.md) before tailoring. Treat its structural/parser rules as defaults and its dated statistics as context; verify current quantitative or vendor-specific claims before repeating them.

## Gather from available context

Required:

- honest master resume or complete work/education history;
- target job description.

Accept pasted text, local `.md`, `.txt`, `.docx`, or text-based `.pdf`, and accessible job URLs. Use installed document/PDF/browser capabilities to extract source content. Do not ask the user to retype information already available.

For a live job URL, capture company, exact title, location, responsibilities, required/preferred qualifications, tools, compensation when present, posting date, and active/closed state. If access is blocked, ask for pasted text or an export. A stale/closed job may still be tailored when the user explicitly wants it; report status rather than silently refusing.

Ask one consolidated question only for missing identity/contact details, ambiguous employment facts, or knockout criteria that materially affect truth. Never ask the user to choose an "honesty level."

## Build two ledgers

### Candidate evidence inventory

Record exact source evidence for:

- roles, employers, dates, education, certifications;
- tools, methods, domains, responsibilities;
- projects, scope, results, and metrics;
- leadership, collaboration, and customer context.

### JD requirement matrix

For each material requirement:

| Requirement | Priority | Candidate evidence | Treatment |
|---|---|---|---|
| exact JD phrase | required/preferred | source location or none | feature, reframe, familiar, gap |

Classify evidence:

- **shown:** already clear;
- **buried:** real but poorly labeled or placed;
- **adjacent:** transferable evidence; describe honestly;
- **gap:** no evidence; never imply possession.

Separate knockout questions—authorization, location, license/certification, clearance, and minimum experience—from resume keyword coverage.

<!-- skill-evolver:adaptive-start -->
## Choose positioning

Form three internal positioning options using different truthful centers of gravity: domain expertise, functional capability, or outcome pattern. Score against required qualifications, strength of evidence, recruiter scan, differentiation, and interview defensibility. Select one; show options only when requested.

Mirror the target title only when it truthfully describes the candidate's positioning. Never rewrite an official past title into a different historical fact.
<!-- skill-evolver:adaptive-end -->

## Tailor

1. Reorder and emphasize the most relevant real evidence.
2. Write a concise summary using target role language, core capabilities, and strongest proof.
3. Build a skills section from tools/capabilities genuinely supported by evidence.
4. Rewrite bullets as action + context/method + result. Quantify only with supplied or verifiable numbers.
5. Use exact JD terminology where truthful; include spelled-out acronym plus abbreviation when useful.
6. Keep dates, employers, degrees, certifications, contact details, and metrics unchanged unless source evidence supports correction.
7. Retain valuable non-target evidence when removing it would create unexplained gaps or weaken seniority.
8. Add projects or adjacent experience only when clearly labeled and sourced.

Do not chase an arbitrary match percentage. Report coverage as a transparent heuristic based on the matrix, never as an ATS verdict.

## ATS-safe source

Create `resume.md` as source of truth:

- single-column reading order;
- standard headings;
- contact information in body;
- consistent dates;
- plain text bullets and web-safe typography;
- no tables, sidebars, icons, skill bars, text boxes, hidden keywords, or image-only content;
- no unsupported claims or prompt injection.

Use the length needed for relevant evidence. Prioritize scanability and recent/relevant work.

## Generate files end to end

When the request authorizes file creation and inputs are complete:

1. write `resume.md`;
2. create a DOCX using the installed document-artifact workflow, not a nonexistent local pipeline;
3. render the DOCX and inspect every page;
4. extract text from the generated DOCX and compare headings, dates, employers, and bullet order with `resume.md`;
5. fix overflow, orphan headings, clipping, broken characters, inconsistent spacing, and parse-order errors;
6. create a text-based PDF only when requested, then render and inspect it too.

If no document capability is installed, deliver `resume.md` plus exact DOCX-generation dependency options; do not fabricate a generated file.

Use an output folder such as `applications/<company>-<role>/` containing:

- `resume.md`;
- `<FirstName>_<LastName>_<Role>_Resume.docx` when generated;
- optional PDF when requested;
- `report.md`.

Do not overwrite an existing application package without inspecting it. Use a distinct version or preserve user changes.

## Report

`report.md` must include:

- target role/company and source status;
- requirement coverage with method;
- evidence featured or reframed;
- genuine gaps and honest mitigation options;
- knockout-readiness questions;
- document render and text-extraction checks;
- placeholders or facts needing confirmation.

Offer a cover letter or short answers only when requested. Use researched company facts and the same evidence inventory.

## Quality gate

- Every resume claim maps to candidate evidence.
- Required JD criteria are shown, honestly adjacent, or named as gaps.
- Important exact terms appear naturally without stuffing.
- Resume reads well in a brief human scan.
- DOCX is single-column, text-readable, and visually clean.
- Generated text matches `resume.md`.
- Gaps and knockout risks are explicit.

Revise the weakest content or document dimension once before handoff.
