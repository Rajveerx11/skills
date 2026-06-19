# ATS & Resume Rules Engine (2025–2026)

The verified rules behind the `resume-tailor` skill. Apply these literally. Confidence tags: **[PRIMARY]** vendor data/official docs/named study · **[REPORTED]** widely-repeated, vendor-blog grade · **[DIRECTIONAL]** rule-of-thumb.

## 0. Reality check (frame the user's expectations honestly)

- The "ATS auto-rejects 75% of resumes" line is a **myth** (traces to Preptel, a vendor that closed in 2013). Modern ATS mostly **parse, rank, and search** — they rarely auto-reject on resume *content*. [PRIMARY — Enhancv, The Interview Guys]
- **Real auto-rejection = knockout/screening questions** (work authorization, required certs/licenses, minimum years, location). 84% of recruiters use them. Independent of the resume. Always surface a knockout-readiness note. [PRIMARY — Enhancv, Greenhouse docs]
- Recruiters spend **~7.4 seconds** on the first skim. Optimize for two audiences at once: the **parser** (clean field extraction) and the **human** (fast skim + Boolean keyword search). [PRIMARY — Ladders]
- The "match rate" any tool shows is a **pre-flight visualization, not the ATS's real score** — say so. [PRIMARY — Jobscan]

## 1. ATS landscape & per-platform quirks

Adoption: **97.8% of Fortune 500** use a detectable ATS (2025); **99.7% of recruiters** use ATS filters. Enterprise leaders: Workday 39%+, SuccessFactors 13%. Mid-market: Greenhouse 19%, Lever 17%, Workday 16%, iCIMS 15%. Don't assume one ATS — build to the strictest. [PRIMARY — Jobscan]

| Platform | Auto-reject? | Key quirk | Strictness |
|---|---|---|---|
| **Taleo (Oracle)** | Yes (knockout/min-qual) | Literal keyword match, no semantics; weak PDF parser → prefer DOCX; needs exact headers | Strictest |
| **iCIMS** | Yes (knockout) | 85–95% accuracy single-column, drops to 70–80% multi-column; tables break | Very strict |
| **Workday** | Knockout only | Synonym-penalizing ("data viz tools" ≠ "Tableau"); current title highest-weight; "Mar. 2022" often fails, "March 2022" works | Strict |
| **Greenhouse** | No ("does not auto-reject") | Fails on graphics/headers/footers; rejects files > 2.5 MB | Lenient parser, human decides |
| **Lever** | No | Parsed profile IS the recruiter view; silently drops left-sidebar/column content; supports stemming | Lenient but parse-fragile |
| **Ashby** | No | AI returns "Meets / Does not Meet" per criterion as input, human decides | Lenient |
| **BambooHR** | No | Weak/no auto-parse; recruiters input manually (SMB) | N/A |

**Implication:** optimize for the literal-match floor (Taleo/iCIMS/Workday) and the semantic platforms are satisfied automatically.

## 2. Keyword extraction & scoring algorithm

Extract five classes from the JD: **hard skills, tools/tech, certifications/quals, job titles, domain terms** + years-of-experience phrases.

Scoring model (additive):
1. **Job title = highest weight.** Resumes containing the target title see **10.6× higher interview rates** (Jobscan, 2.5M apps). Mirror it when truthful. [PRIMARY for 10.6×]
2. **Frequency = priority.** A term repeated across sections (esp. first paragraph) is high-priority.
3. **Required > Preferred.** Required quals are hard filters; preferred are tiebreakers.
4. **Placement/recency.** Terms near the top and in the current title carry extra weight.

Algorithm: segment JD → extract term classes → score each (`+HIGH if in title region`, `+1 per occurrence`, `+BONUS if Required`, `+small if top region`) → normalize variants/acronyms into one ranked entity but surface **both surface forms** → cap at **top 10–15 terms** → cross-validate against ~10 postings for the same role to drop idiosyncratic terms.

**Exact-match vs semantic — do both:** use the **literal JD phrasing** (never hurts; required for Taleo/iCIMS) **plus** a paraphrased competency bullet (helps Greenhouse/Lever/Workday NLP). "Adobe Creative Cloud" ≠ "Adobe Creative Suite" to an ATS — copy the JD's exact wording when truthful.

**Acronyms:** spell out + abbreviate on first use — "Search Engine Optimization (SEO)", "CI/CD (Continuous Integration/Continuous Deployment)" — captures exact-match + taxonomy credit.

**Density limits (anti-stuffing):** per high-priority term ≈ 1× Skills + 1–2× Experience + optional 1× Summary. Benefit plateaus at **3–4 contextual mentions**. Red flag: one keyword 10+ times on one page. Use a **coverage model** (% of top JD terms present), not a density target. Context matters, not raw count.

## 3. Match-rate targets

- **Target 80%**, floor 75%, practical floor ~65%. **Never push past ~90%** (forces stuffing; reads as spam). Cover **70–80% of required skills**. [PRIMARY — Jobscan]
- Hard skills weighted highest; **job title second**; education counted only when JD requires a degree. Measurable results don't move keyword-based match scores but strongly impress humans (58% of recruiters). [PRIMARY]

## 4. Formatting rules (parse-failure prevention)

Formatting causes ~23% of parse failures. Rules:

| Element | Rule |
|---|---|
| Layout | **Single column**, reverse-chronological. No tables, multi-column, text boxes, images, charts, skill-bar graphics, icons, or emoji. |
| Contact info | Plain text **in the body at top** — never in header/footer (dropped ~25% of the time). |
| Fonts | One web-safe font: Arial, Calibri, Cambria, Garamond, Georgia, Helvetica, Tahoma, Times New Roman, Verdana. Body 10–12 pt (11 sweet spot); headings 14–16 pt; name 16–20 pt. |
| Margins / spacing | 1 inch (0.5 in minimum); single line spacing (≤1.15). |
| Dates | `Month YYYY` (January 2022 / Jan 2022) **or** `MM/YYYY` — pick one, be consistent. Avoid year-only, apostrophe years ('21), single-digit months, em-dashes. Don't start a line with a date. |
| Characters | ASCII only: straight quotes, `•` or `-` bullets (not ★➤◆), hyphen/en-dash for ranges, spell out symbols ("Phone:", "50%"). Disable ligatures on export. |
| File | DOCX default (lowest failure rate) + text-based PDF option; never image/scanned PDF; keep < 2.5 MB. Name: `FirstName_LastName_JobTitle_Resume.pdf` (underscores/hyphens, no spaces). |
| Length | 1 page for ≤10 yrs; 1–2 pages mid-career; 2 pages senior. No ATS length penalty — only obey a stated one-page limit. Last ~15 years only. |

## 5. Section structure

Essential order — **experienced:** Contact → Professional Summary → Work Experience → Skills → Education → Certifications. **Entry-level:** Contact → Summary → Education → Skills → Experience. **Career changer:** Summary → Skills → reframed Experience → Certs → Projects.

**Standard headings ONLY** (ATS recognize these): "Professional Summary"/"Summary", "Work Experience"/"Professional Experience", "Skills"/"Technical Skills", "Education", "Certifications", "Awards", "Volunteer Experience". **Never** use creative headings ("My Journey", "Where I've Made an Impact", "Career Highlights", "Core Competencies") — they mis-bucket content. Make headings bold + (optionally) ALL CAPS.

Default to a **Professional Summary** (backward-looking, accomplishments); use an Objective only for very limited experience or a major career change.

## 6. Bullet writing

- **XYZ formula (Google/Laszlo Bock):** "Accomplished **[X]** as measured by **[Y]** by doing **[Z]**." Y is a number. e.g. "Increased sales 25% by launching a new product line in Q1."
- **PAR (MIT):** Project → Action → Result. Action verb first; 1–2 lines; quantify.
- **Quantify ~50–60%+ of bullets** (%, $, count, time).
- **Kill:** "Responsible for", "Duties included", "Worked on", "Helped", "Assisted with". And buzzwords: "hardworking", "team player", "detail-oriented", "results-driven", "dynamic".
- **Vary verbs** — a one-page resume uses ~20–30; don't repeat. Mix in some rarer verbs but keep it natural.

### Action-verb banks (Harvard / MIT / Berkeley)

- **Management/Leadership:** administered, chaired, consolidated, coordinated, delegated, directed, executed, orchestrated, organized, oversaw, prioritized, produced, spearheaded, strengthened, supervised, unified.
- **Communication:** authored, arbitrated, collaborated, convinced, corresponded, drafted, edited, influenced, mediated, moderated, negotiated, persuaded, promoted, publicized, reconciled, recruited.
- **Research/Analysis:** clarified, collected, critiqued, deciphered, diagnosed, evaluated, examined, extracted, identified, investigated, scrutinized, summarized, surveyed, systematized.
- **Technical:** assembled, built, computed, debugged, designed, devised, engineered, fabricated, maintained, operated, overhauled, programmed, rebuilt, restructured, upgraded.
- **Financial/Data:** administered, allocated, appraised, audited, balanced, budgeted, forecasted, projected, reduced.
- **Achievement/Improvement:** accelerated, achieved, amplified, boosted, doubled, eliminated, enhanced, expedited, ignited, improved, increased, lifted, pioneered, reduced, surpassed, sustained, transformed, trimmed.
- **Creative:** conceptualized, created, customized, established, founded, illustrated, initiated, instituted, integrated, introduced, invented, launched, originated, revitalized, shaped.
- **Helping:** advised, coached, counseled, demonstrated, educated, expedited, facilitated, guided, mentored, motivated, rehabilitated.

## 7. Honest reframing vs fabrication

Principle: *tailoring = selection and emphasis, not fabrication.* Every keyword must reflect real experience.

**Legitimate (do this):** reorder/re-emphasize real bullets so JD-relevant ones surface first; re-label the same real work in the employer's vocabulary (your "customer issue tracking" → JD's "ticket triage / case management" — only if genuinely that); confidently quantify true results; show a real growth trajectory.

**Never (hard lines):** invent titles, employers, dates, degrees, certs, or metrics; claim tools never used. These unravel in interviews/take-homes and fail background checks; credential-gated fields carry legal risk. For genuine gaps, present honest options — earn it via a quick project, list as "familiar", or omit — and let the user decide.

## 8. Cover letters & short answers (on request)

- Including a cover letter raised interview rates **3.4×** (Jobscan). Mirror the JD's exact skill terms; 3–4 short paragraphs; open with a specific company/role hook, not a template; ~90% of cover letters fail for lack of customization.
- **Short-answer "describe a time" questions → STAR** (Situation, Task, Action, Result). Spend the most words on **Action**; use "I" not "we"; quantify the Result. STAR is wrong for motivational questions ("Why us?"/"5 years?") — those need researched, specific company facts.

## 9. 2025–2026 AI-screening reality

- Skills are the #1 ATS filter (76.4%), then Education (59.7%), Job titles (55.3%), Years of experience (44%). [PRIMARY — Jobscan]
- Application flood: ~11,000 LinkedIn apps/minute (+45% YoY); 45% of applicants use AI. Differentiation matters more, not less.
- **AI-authorship is not auto-detected for rejection**, but **62% of employers reject generic, un-personalized AI output**, and ~33% of managers say they spot an AI resume in <20s. The penalty is *detectably generic voice + hallucinated, indefensible detail* — not AI use itself. Force real metrics, specific tactile verbs, varied structure.
- **Hidden white-font keywords / prompt injection: never.** ATS strip formatting and render the text visible to recruiters; ManpowerGroup detects hidden text in ~10% of AI-scanned resumes; many treat it as automatic rejection. The tool must never emit hidden text or injected prompts.

## 10. Pre-flight checklist (run before delivering)

1. Single column, standard headings, contact in body, web-safe font 10–12 pt, consistent `Month YYYY` dates, ASCII only, < 2.5 MB. ☐
2. Exact target job title mirrored in headline (if truthful). ☐
3. 15–30 hard-skill-led skills; 70–80% of required skills covered; acronyms dual-encoded. ☐
4. Each rewritten bullet = action verb + XYZ/PAR + metric; ~50–60%+ quantified; verbs varied; no "responsible for"/buzzwords. ☐
5. Match estimate ~80% (not > 90%); no keyword stuffing; no hidden text. ☐
6. Nothing fabricated; every claim defensible; gaps listed with honest options. ☐
7. Report includes coverage estimate, reframes made, gap list, and knockout-readiness note (auth/location/certs/years). ☐
