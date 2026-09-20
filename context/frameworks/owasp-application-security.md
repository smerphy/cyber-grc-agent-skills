# OWASP application security standards (ASVS, Top 10, SAMM, MASVS, GenAI)

## At a glance

| Attribute | Detail |
|---|---|
| Publisher | OWASP Foundation (Open Worldwide Application Security Project), a vendor-neutral nonprofit; GenAI/LLM work sits under the OWASP GenAI Security Project (genai.owasp.org) |
| Verification standard | **ASVS 5.0.0**, May 2025 — around **350 requirements** (**345** in the published 5.0.0 requirement list) across **17 chapters**, three levels (L1/L2/L3). Supersedes 4.0.3 (286 requirements); every identifier was renumbered |
| Awareness list | **OWASP Top 10:2025** — the 8th installment, issued as final and listed by the project as the most current released version; the publisher pages give no publication date, so treat the 2025 release date as (verify). Two new categories, SSRF folded into A01 |
| Maturity model | **SAMM v2** — 5 business functions, 3 security practices each (15 total), 2 activity streams per practice, 3 maturity levels |
| Mobile | **MASVS v2** (8 control groups, controls numbered `MASVS-GROUP-n`) with the **MASTG** (v2.0.0, June 2026) and **MASWE** (v1.0.0, 17 August 2026 — 78 weaknesses); the old L1/L2/R levels were replaced in the 2023 refactor by **MAS Testing Profiles** (MAS-L1, MAS-L2, MAS-R, MAS-P, plus the specialised MAS-EUDIW) |
| API and GenAI | **API Security Top 10 – 2023** (API1–API10); **Top 10 for LLM Applications 2026** (the document is dated 4 August 2026; the publisher resource page is dated 3 August 2026), superseding the 2025 edition (publisher resource page dated 17 November 2024) |
| Supply chain | **SCVS** (OWASP Lab project, supply-chain assurance controls); **CycloneDX** BOM specification **v1.7** (released 2025-10-21), standardized as **ECMA-424 2nd edition**, published 2025-12-10 by Ecma TC54 with OWASP (1st edition, June 2024, covered v1.6) |
| Certifiable? | **No.** OWASP certifies no vendor, verifier or software; any "ASVS certified" trust mark is not OWASP-endorsed. Organizations may sell assurance services but not official OWASP certification |
| Cost / licence | Free. ASVS 5.0.0 and the GenAI LLM Top 10 under CC BY-SA 4.0; Top 10:2025 under CC BY 3.0; SAMM under CC BY-SA 4.0 |
| Typical GRC use | Contractual secure-development baseline, pen-test scoping and reporting standard, secure-SDLC maturity roadmap, evidence source for PCI DSS Req. 6 and ISO 27001 secure-development controls |

## What it is

OWASP is not one framework but a family of free, community-maintained appsec artifacts that fill different roles. The **Top 10** is the project's self-described "standard awareness document" — a ranked list of risk categories, not a pass/fail requirement set. The **ASVS** is the *verifiable* standard: pass/fail requirements an application either meets or does not. **SAMM** measures the *organization's* software-assurance maturity rather than any one application. **MASVS/MASTG** do for mobile apps what ASVS/WSTG do for web. The GenAI project extends the model to LLM-backed and agentic systems.

The pieces are designed not to overlap. ASVS 5.0 states its scope deliberately excludes "how do I implement this in my stack" (Cheat Sheet Series) and "how do I test this" (Web Security Testing Guide, currently v4.2 with v5.0 in development). ASVS contains only requirements ("must"), never recommendations ("should"), and every requirement must be verifiable to a fail/pass decision and have demonstrable security impact.

For GRC purposes the practical division is: cite **ASVS** in contracts, security requirements and pen-test statements of work; use **Top 10** for developer awareness, training and board-level risk narrative; use **SAMM** for programme roadmaps and maturity reporting; use **MASVS/LLM Top 10** where the asset is a mobile app or a model-backed application.

## Who it covers / Scope

Nothing here is legally binding on its own. Scope is set by whoever adopts it:

- **ASVS defines "application"** as the software product itself — the security outcomes to be achieved *in the product*. It deliberately excludes what the application does not control: DNS, backups and other external processes. Components that serve, modify or validate HTTP traffic (WAFs, load balancers, proxies) may be treated as part of the application for specific requirements (cached responses, rate limiting, connection restrictions).
- **Tailoring is expected.** OWASP encourages organization-specific forks that drop irrelevant chapters (e.g. WebRTC, OAuth if unused) and add implementation guidance — provided traceability is kept, so that "requirement 4.1.1" means the same thing everywhere.
- **Regulatory pull-through** is where OWASP becomes binding in practice. PCI DSS v4.x Req. 6.2 ("Bespoke and custom software are developed securely") requires development "based on industry standards and/or best practices for secure development" (6.2.1), developer security training at least once every 12 months (6.2.2), and defined engineering techniques to prevent common attacks including injection flaws (6.2.4) — ASVS and the Top 10 are the usual evidence. See [pci-dss-4.md](pci-dss-4.md).
- **Not in scope for ASVS:** functional requirements, code style, policy-only requirements, and anything not verifiable.

## Structure and requirements

### ASVS 5.0.0 — 17 chapters

| Ch. | Chapter | Ch. | Chapter |
|---|---|---|---|
| V1 | Encoding and Sanitization | V10 | OAuth and OIDC |
| V2 | Validation and Business Logic | V11 | Cryptography |
| V3 | Web Frontend Security | V12 | Secure Communication |
| V4 | API and Web Service | V13 | Configuration |
| V5 | File Handling | V14 | Data Protection |
| V6 | Authentication | V15 | Secure Coding and Architecture |
| V7 | Session Management | V16 | Security Logging and Error Handling |
| V8 | Authorization | V17 | WebRTC |
| V9 | Self-contained Tokens | | |

Identifier format is the lowercase version tag, then chapter, section and requirement numbers — `v5.0.0-1.2.5`. Always cite the version — 5.0.0 renumbered everything.

**Levels are priority-based, not application-class-based** (a change in emphasis from 4.x):

| Level | Share of requirements | Character |
|---|---|---|
| L1 | ~20% (70 of 345) | Minimum starting point; critical first-layer defences against common attacks. Low barrier to entry. Not necessarily black-box testable |
| L2 | ~50% (183; ≈70% cumulative) | "Most applications should be striving to achieve this level." Less common attacks, or more complex protections against common ones |
| L3 | remaining ~30% (92; 100%) | Defence-in-depth and hard-to-implement controls; for applications demonstrating the highest assurance |

OWASP does not prescribe a level — the organization picks one from its own risk analysis (the standard's own illustration: an early-stage startup may target L1; a bank would struggle to justify below L3 for online banking).

**Documentation requirements** are an ASVS 5.0 design feature: where a rule is inherently application-specific (allowed file types, permission model, session-timeout rules, sensitive-data handling), the standard requires the organization's *decision* to be documented, with a paired implementation requirement. Verifying the documentation and verifying the implementation are two separate activities — a useful distinction when building audit evidence.

**Release semantics** matter for contracts: major (4.0.3 → 5.0.0) = full reorganization, re-assessment required; minor (5.0.0 → 5.1.0) = requirements added/removed, numbering stable, re-assessment easier; patch (5.0.0 → 5.0.1) = only removals or relaxations, so prior compliance still holds.

### OWASP Top 10:2025

| # | Category | Change from 2021 |
|---|---|---|
| A01 | Broken Access Control | Holds #1; 40 CWEs; SSRF rolled into this category |
| A02 | Security Misconfiguration | Up from #5; 16 CWEs |
| A03 | Software Supply Chain Failures | **New** — expands A06:2021 Vulnerable and Outdated Components to build systems and distribution infrastructure; 5 CWEs; fewest data occurrences but highest average CVE exploit/impact scores |
| A04 | Cryptographic Failures | Down from #2; 32 CWEs |
| A05 | Injection | Down from #3; 38 CWEs; most CVEs |
| A06 | Insecure Design | Down from #4 |
| A07 | Authentication Failures | Holds #7; renamed from "Identification and Authentication Failures"; 36 CWEs |
| A08 | Software or Data Integrity Failures | Holds #8; trust-boundary and artifact integrity below the supply-chain level |
| A09 | Security Logging & Alerting Failures | Holds #9; renamed from "…and Monitoring"; 5 CWEs; survey-promoted |
| A10 | Mishandling of Exceptional Conditions | **New** — 24 CWEs: improper error handling, logical errors, failing open |

Methodology: data-informed, not data-driven. Eight categories are selected from contributed data, two from the community survey. Contributors donated data on **over 2.8 million applications**; **589 CWEs** were analysed, of which **248** sit inside the ten categories; ~175k CVE-to-CWE records were used for exploit/impact scoring (CVSS v2/v3 — v4.0 was not usable for this cycle). Categories are capped at 40 CWEs and favour root cause over symptom.

### SAMM v2, MASVS and the GenAI lists

- **SAMM v2** business functions: Governance (Strategy & Metrics, Policy & Compliance, Education & Guidance), Design (Threat Assessment, Security Requirements, Secure Architecture), Implementation (Secure Build, Secure Deployment, Defect Management), Verification (Architecture Assessment, Requirements-driven Testing, Security Testing), Operations (Incident Management, Environment Management, Operational Management). Each practice has two streams and three maturity levels: 1 = initial implementation, 2 = structured realization, 3 = optimized operation. Assessment measures maturity from both a coverage and a quality perspective.
- **MASVS** control groups: STORAGE, CRYPTO, AUTH, NETWORK, PLATFORM, CODE, RESILIENCE, PRIVACY. Weaknesses are catalogued as MASWE-nnnn (v1.0.0, August 2026: 78 weaknesses) and tests in the MASTG, giving a traceability chain of MASVS control to MASWE weakness to MASTG test.
- **OWASP Top 10 for LLM Applications 2026**: LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Excessive Agency, LLM04 Supply Chain, LLM05 Data and Model Poisoning, LLM06 Unbounded Consumption, LLM07 Misinformation, LLM08 Hidden Context Exposure, LLM09 Vector and Embedding Weaknesses, LLM10 Improper Output Handling. Ranking weights the community vote at three-quarters and an incident corpus (7,714 collected, 6,639 classifiable) at one quarter. The edition draws an explicit boundary: it covers the model *as a component inside an application*; once the model acts — tools, cross-session memory, downstream consequences — the risk moves to the OWASP Top 10 for Agentic Applications (ASI). See [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).
- **API Security Top 10 – 2023**: API1 Broken Object Level Authorization, API2 Broken Authentication, API3 Broken Object Property Level Authorization, API4 Unrestricted Resource Consumption, API5 Broken Function Level Authorization, API6 Unrestricted Access to Sensitive Business Flows, API7 Server Side Request Forgery, API8 Security Misconfiguration, API9 Improper Inventory Management, API10 Unsafe Consumption of APIs.

## Assessment, certification and evidence

- **There is no OWASP certification.** OWASP does not certify vendors, verifiers or software. Treat any supplier claim of "OWASP/ASVS certification" as a self-assertion and ask for the underlying report.
- **ASVS reporting differs from a normal pen-test report.** A pen test reports by exception (failures only). An ASVS verification report must state the scope, the level attempted, a summary of **all** requirements checked, the exceptions found, requirements marked not applicable (with rationale), and remediation guidance — framed as what was included rather than what was excluded.
- **Verification is not black-box.** ASVS 5.0 is explicit that testing without documentation, source and access to the development team is inefficient and ineffective, especially for L2/L3. Verifying ASVS generally needs documentation, source code, configuration and people. Evidence expectations: work papers, screenshots, scripts, testing logs. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md) and [../../templates/control-test-workpaper.md](../../templates/control-test-workpaper.md).
- **"Testable using automation" ≠ "running an off-the-shelf tool."** DAST/SAST in the pipeline can cover some straightforward requirements (encoding, sanitization) but cannot verify business logic or access control; application-specific automated verifications, written like unit/integration tests, are the sustainable route.
- **SAMM evidence** is activity- and artifact-based per practice and stream, scored for coverage and quality, producing a maturity score and a roadmap — pair it with [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| 2008 | ASVS first launched |
| 2019 | ASVS 4.0 |
| 2021 | ASVS 4.0.3 — the final 4.x release (286 requirements) |
| 2023 | MASVS v2.0.0 refactor: 8 control groups; the L1/L2/R verification levels replaced by MAS Testing Profiles |
| 2023 | API Security Top 10 – 2023 edition; first LLM Top 10 (the 2023–24 list) |
| Nov 2024 | LLM Top 10 "Version 2025" release (publisher resource page dated 17 November 2024) |
| May 2025 | **ASVS 5.0.0** — current stable release; still current in September 2026, with a patch release (5.0.1) named as the next target. The repository's master branch is a "bleeding edge" build, explicitly not stable |
| 21 Oct 2025 | CycloneDX v1.7 released |
| 2025 (date not stated by the publisher) | **OWASP Top 10:2025** published, then issued as final — the 8th installment; the project page lists 2025 as the latest version |
| 26 Nov 2025 | OWASP AI Testing Guide v1 published |
| 9 Dec 2025 | OWASP Top 10 for Agentic Applications (ASI) 2026 announced |
| 10 Dec 2025 | ECMA-424 2nd edition adopts CycloneDX v1.7 |
| Jun–Aug 2026 | MASTG v2.0.0 (June 2026); MASWE v1.0.0 (17 August 2026) |
| 4 Aug 2026 | **OWASP Top 10 for LLM Applications 2026** published (the PDF's own revision history still shows the release date as a placeholder) |
| In progress | WSTG v5.0 under development; v4.2 remains the versioned release. ASVS 5.0.1 pending |

## Key obligations for security/GRC teams

1. **Pick and pin a version.** Write "ASVS 5.0.0, Level 2" into policies, contracts and SOWs — never "OWASP compliant". Record the level decision and its risk rationale; ASVS deliberately does not choose for you.
2. **Build the organization-specific ASVS fork** early: drop inapplicable chapters, add stack-specific implementation guidance, preserve requirement identifiers for traceability. Manage deviations through [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
3. **Satisfy the documentation requirements first.** Permission models, input-validation rules, allowed file types, session-timeout policy and sensitive-data handling must exist as documented decisions before implementation can be verified. See [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).
4. **Re-specify pen tests as ASVS verifications**: level, chapter scope, full requirement coverage summary, documented not-applicable rationale, and source/documentation access granted up front.
5. **Do not conflate the lists.** Top 10 coverage is an awareness and training metric, not an assurance statement; A03:2025 Software Supply Chain Failures in particular is under-represented in test data and needs SBOM/build-integrity evidence instead.
6. **Wire supply-chain evidence in**: CycloneDX v1.7 / ECMA-424 SBOMs from the build pipeline, SCVS controls for supplier and component assurance, feeding [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../templates/vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md).
7. **Run SAMM annually as the programme metric** — maturity by practice and stream, with coverage and quality separated — and report trend, not absolute score, to the board ([../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md)).
8. **Extend to the asset type**: MASVS/MASTG profiles for mobile apps, API Security Top 10 for machine-to-machine surfaces, LLM Top 10 2026 for model-backed applications, and the Agentic (ASI) list once a model gains tools, memory or downstream authority.
9. **Map OWASP evidence to the regimes that consume it** — PCI DSS Req. 6.2 (secure development, 12-monthly developer training, defined anti-injection techniques), ISO 27001 Annex A secure-development controls, SOC 2 change-management criteria — using [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).

## Interplay

- **PCI DSS v4.x** — [pci-dss-4.md](pci-dss-4.md). Req. 6.2.1's "industry standards and/or best practices for secure development" is where ASVS and the Top 10 are usually cited; 6.2.2 forces 12-monthly developer security training; 6.2.4 names injection classes explicitly. An ASVS-based SDLC produces most of the Req. 6 evidence set as a by-product.
- **ISO/IEC 27001:2022** — [iso-27001-2022.md](iso-27001-2022.md). Annex A's secure-development controls (A.8.25–A.8.29 — verify numbering against the current Annex A) are outcome statements; ASVS supplies the testable requirement text and SAMM supplies the maturity evidence behind them.
- **CIS Controls v8/v8.1** — [cis-controls-v8.md](cis-controls-v8.md). Control 16 (Application Software Security) starts at IG2; ASVS is the natural depth layer beneath its safeguards.
- **NIST CSF 2.0** — [nist-csf-2.md](nist-csf-2.md). CSF frames the programme, SAMM measures the software-assurance slice of it, ASVS provides application-level verification evidence. See also [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
- **SOC 2** — [soc2-tsc.md](soc2-tsc.md). ASVS verification reports and SAMM assessments are strong supporting evidence for change-management and system-development criteria, but are not themselves an attestation.
- **NIST SSDF (SP 800-218)** — [nist-ssdf-800-218.md](nist-ssdf-800-218.md) — and the **EU Cyber Resilience Act** — [../regulations/eu-cyber-resilience-act.md](../regulations/eu-cyber-resilience-act.md) — run in parallel on the same ground: SSDF describes secure-development *practices*, the CRA imposes legal *product* requirements and vulnerability-handling duties on manufacturers. ASVS/SAMM evidence feeds both but satisfies neither by itself.
- **Conflict to watch:** OWASP artifacts move faster than the regimes that cite them. A contract that says "current OWASP Top 10" silently re-scoped when 2021 became 2025, and an ASVS 4.x-based requirements library does not map cleanly onto 5.0.0 identifiers. Pin versions and schedule a review each time an edition lands — see [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Primary sources

- OWASP ASVS 5.0.0 source text — `https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x02-Preface.md`, `https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x03-What-is-the-ASVS.md`, `https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/en/0x04-Assessment_and_Certification.md` — publisher text (scope, levels, documentation requirements, release semantics, certification stance)
- OWASP ASVS published requirement lists — `https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv` (345 rows; 70 L1 / 183 L2 / 92 L3) and the 4.0.3 list at `https://raw.githubusercontent.com/OWASP/ASVS/v4.0.3/4.0/docs_en/OWASP%20Application%20Security%20Verification%20Standard%204.0.3-en.csv` (286 rows) — publisher data
- OWASP ASVS repository README (current release status, 4.0/4.0.3 dating, next target 5.0.1) — `https://raw.githubusercontent.com/OWASP/ASVS/master/README.md` — publisher text
- OWASP ASVS project page — `https://owasp.org/www-project-asvs/` (also served at `https://asvs.owasp.org/`) — publisher page confirming 5.0.0 as the latest stable version
- OWASP Top 10:2025 home and Introduction — `https://owasp.org/Top10/2025/` and `https://owasp.org/Top10/2025/0x00_2025-Introduction/` — publisher text
- OWASP Top Ten project page — `https://owasp.org/www-project-top-ten/` — publisher page (confirms 2025 as latest version)
- OWASP SAMM model, structure and version 2 release notes (maturity level names, coverage and quality scoring) — `https://owaspsamm.org/model/`, `https://owaspsamm.org/about/`, `https://owaspsamm.org/release-notes-v2/` — publisher pages
- OWASP MASVS control groups, MAS Testing Profiles and MAS news archive (MASVS v2.0.0 and the profile change, 2023; MASWE v1.0.0 and MASTG v2.0.0, 2026) — `https://mas.owasp.org/MASVS/`, `https://mas.owasp.org/Profiles/`, `https://mas.owasp.org/news/archive/2023/`, `https://mas.owasp.org/news/archive/2026/` — publisher pages
- OWASP API Security Top 10 – 2023 — `https://owasp.org/API-Security/editions/2023/en/0x11-t10/` — publisher text
- OWASP Top 10 for LLM Applications 2026 (PDF), the 2025 edition resource page and the LLM Top 10 index — `https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/`, `https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/`, `https://genai.owasp.org/llm-top-10/` — publisher documents
- OWASP SCVS — `https://owasp.org/www-project-software-component-verification-standard/` and the project README — publisher pages (control-family detail not retrievable)
- CycloneDX specification overview (v1.7, released 2025-10-21; ECMA-424 published 2025-12-10) — `https://cyclonedx.org/specification/overview/` — publisher page
- ECMA-424 standard page (1st edition June 2024; 2nd edition December 2025, defining CycloneDX v1.7) — `https://ecma-international.org/publications-and-standards/standards/ecma-424/` — standards-body page
- OWASP AI Testing Guide — `https://owasp.org/www-project-ai-testing-guide/` — publisher page
- OWASP Web Security Testing Guide — `https://owasp.org/www-project-web-security-testing-guide/` — publisher page
- PCI DSS v4.0 SAQ A-EP (Requirement 6.2 text) — `https://listings.pcisecuritystandards.org/documents/PCI-DSS-v4-0-SAQ-A-EP.pdf` — standards-body document

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
