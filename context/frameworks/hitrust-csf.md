# HITRUST CSF and the HITRUST assessment portfolio (e1, i1, r2)

## At a glance

| Attribute | Detail |
|---|---|
| Owner / publisher | HITRUST Services LLC (commonly "HITRUST", historically the HITRUST Alliance) — a private standards and certifying body, not a regulator |
| Current framework version | **HITRUST CSF v11.8.0**, available in MyCSF and downloadable as of **8 May 2026** (advisory HAA 2026-002). Immediate predecessor library version v11.7.1; earlier: v11.7.0 (18 Dec 2025), v11.6.0 (22 Aug 2025) |
| Structure | 14 control categories → 49 control objectives → 156 control specifications; each specification carries up to three progressive implementation levels plus segment-specific levels |
| Harmonization | v11.8.0 integrates **75** security and privacy standards, regulations and frameworks as "authoritative sources"; core structure is based on ISO/IEC 27001 and 27002 |
| Assessment portfolio | **e1** (43 requirement statements, 1 year) · **i1** (182, 1 year) · **r2** (tailored, 2 years with an interim at month 12) · targeted (non-certifiable self-assessment). Traversable: e1 ⊂ i1 ⊂ r2 baseline |
| Certifiable? | Yes — HITRUST issues the certification itself after a HITRUST Authorized External Assessor performs validated fieldwork and HITRUST performs centralized quality assurance |
| Scoring model | PRISMA-derived control maturity model: Policy, Procedure, Implemented, Measured, Managed. r2 scores all five (Measured/Managed optional); e1 and i1 score **Implemented only** |
| Certification thresholds | e1/i1: core requirement statements in **each** assessment domain must average ≥ **83**. r2: **each** domain must average ≥ **62** |
| Platform | MyCSF (assessment SaaS, CAP management, inheritance); reports shared through the HITRUST Report Center, live 10 Sep 2026 and mandatory for draft reports issued after that date, alongside the Assessment XChange and Results Distribution System |
| Sector | Originated in US healthcare but is sector-neutral in current releases; heaviest adoption remains healthcare and health-tech vendor assurance |

## What it is

The HITRUST CSF is a **prescriptive, harmonized control library plus a certification programme**. Its differentiator is not the control content — which borrows its skeleton from ISO/IEC 27001 and 27002 and pulls requirement text from dozens of other sources — but the **assurance machinery** wrapped around it: fixed requirement statements with published illustrative procedures, a defined maturity-scoring rubric, mandatory testing by an authorized external assessor, and a centralized quality-assurance review performed by HITRUST before any report is issued. That centralization is why a HITRUST certification travels between counterparties more readily than a self-attested framework score.

Requirements are selected by **risk factors** rather than picked by the assessed entity. Organizational factors (data volumes, transaction counts, geographic scope), compliance factors (the regulations the entity elects to cover, e.g. HIPAA, PCI DSS, GDPR), and system factors (internet accessibility, third-party access, mobile use, number of interfaces and users) drive which implementation level of each control applies in an r2. The e1 and i1 instead use **fixed baselines** — a curated set of requirement statements, identical for every assessed entity — which is what makes them fast and comparable.

HITRUST publishes a "cyber threat adaptive" claim: requirement selection is periodically re-evaluated against threat intelligence and breach data, and HITRUST states in its 2026 Trust Report that 99.62% of HITRUST-certified environments were breach-free in 2025 (99.41% in 2024). Treat that figure as the publisher's own marketing claim, not independently audited evidence.

## Who it covers / scope

HITRUST is **voluntary and contractual** — nothing legally compels certification. It is used where a counterparty, payer, health system, cyber insurer or procurement function demands it, and increasingly as an umbrella for multi-regulation assurance.

- **Scoping is by environment, not entity.** The certified scope is the set of in-scope systems, facilities, business units and supporting infrastructure declared in MyCSF. Anything outside that boundary is not certified, and the certification letter is issued in two forms (with and without scope detail) so the scope can be withheld from relying parties.
- **Assessment domains** are the scoring unit. Certification is judged per domain, not on an overall average — a single weak domain blocks certification even with strong aggregate scores. (Commonly cited as 19 assessment domains — treat the count as unconfirmed **(verify)** against the current MyCSF domain list; the handbook names individual domains such as Endpoint Protection and Portable Media Security but does not enumerate a count.)
- **Carve-outs:** requirements performed by service providers on the entity's behalf (e.g. cloud providers) may be carved out of an **e1 or i1**, but **not** from an r2 — in an r2 the entity must cover them, typically via inheritance.
- **Version currency:** e1 and i1 assessments must be created on the most current CSF version available at creation; r2 assessments need not be. Effective 7 May 2026, new e1, i1 and rapid assessment objects must be created on v11.8.0 (HAA 2026-003).

## Structure and requirements

### Control categories (control objectives, control specifications)

| # | Category | (Obj., Spec.) | # | Category | (Obj., Spec.) |
|---|---|---|---|---|---|
| 0 | Information Security Management Program | (1, 1) | 7 | Asset Management | (2, 5) |
| 1 | Access Control | (7, 25) | 8 | Physical and Environmental Security | (2, 13) |
| 2 | Human Resources Security | (4, 9) | 9 | Communications and Operations Management | (10, 32) |
| 3 | Risk Management | (1, 4) | 10 | Information Systems Acquisition, Development, and Maintenance | (6, 13) |
| 4 | Security Policy | (1, 2) | 11 | Information Security Incident Management | (2, 5) |
| 5 | Organization of Information Security | (2, 11) | 12 | Business Continuity Management | (1, 5) |
| 6 | Compliance | (3, 10) | 13 | Privacy Practices | (7, 21) |

Ordering does not imply priority. Each control carries: a control objective, control reference, control specification, applicable risk factor types, topics, implementation requirements at up to three progressive levels (Level 1 is the minimum baseline; each level subsumes the one below), segment-specific levels where relevant (e.g. cloud service providers, FedRAMP, GDPR), and mapping to authoritative sources by level.

### Assessment types

| | e1 (Essentials, 1-year) | i1 (Implemented, 1-year) | r2 (Risk-based, 2-year) |
|---|---|---|---|
| Requirement statements | 43 fixed | 182 fixed | Tailored by risk factors (superset of i1 baseline) |
| Maturity levels scored | Implemented | Implemented | Policy, Procedure, Implemented (+ Measured, Managed optional) |
| Domain threshold | ≥ 83 (core statements) | ≥ 83 (core statements) | ≥ 62 (all statements in the domain) |
| Validity | 12 months | 12 months | 24 months + interim assessment at the 12-month anniversary |
| Max assessor fieldwork window | 90 days | 90 days | 90 days |
| Service-provider carve-out | Yes | Yes | No |
| Tailored to scope / privacy scope | No | No | Yes |
| Bridge certificate available | No | No | Yes |
| NIST CSF certification available | No | No | Yes (add-on) |

### Maturity model and scoring

| Level | What is evaluated |
|---|---|
| Policy | Documented policy/standard that mandates the requirement's evaluative elements, covering all in-scope facilities and systems |
| Procedure | Documented procedures derived from policy, detailed enough for a qualified person to execute, covering all in-scope scope items |
| Implemented | Actual operation across all in-scope systems; tested by the external assessor, sample-based where the illustrative procedure indicates |
| Measured | Separate or ongoing monitoring/metrics of the control's operation, reviewed by an operational or independent party |
| Managed | Corrective action or enhancement driven by the measurement results |

Each requirement statement is scored per maturity level on **strength** (rigour of implementation) × **coverage** (percentage of evaluative elements met), yielding Non-Compliant, Somewhat, Partially, Mostly or Fully Compliant. NC scores 0 and FC scores 100; partial scope coverage averages across scope items (a policy covering three of four in-scope business units scores 75). Weighting across scope components is permitted with documented rationale, which HITRUST QA can reject.

## Assessment, certification and evidence

1. **Readiness (self) assessment** — optional, no HITRUST QA, produces a readiness report that cannot be certified but can feed a validated assessment.
2. **Validated assessment** — an Authorized External Assessor organization tests every in-scope requirement statement. The engagement's quality-assurance reviewer must hold both the CCSFP and CHQP credentials. In an r2 the assessed entity alone may enter control maturity scoring and scoping information (including the pre-assessment webforms and default scoring profile); in an e1 or i1 either the entity or the external assessor may.
3. **CAPs and representation letter** — requirements below threshold become corrective action plans; management signs a representation letter.
4. **HITRUST QA and reporting** — automated checks plus HITRUST's own review, then draft reports the entity has 30 days to approve or return for revision (scope, factors and scoring cannot be changed at this stage). Meeting the domain thresholds yields a **Certification Report**; failing them yields a **validated-only** report that states the thresholds were not met. Draft reports issued after 10 September 2026 must be shared with relying parties through the HITRUST Report Center.
5. **Maintenance** — r2: interim assessment submitted in the 90-day window before the one-year anniversary of certification issuance, testing one randomly selected requirement statement from each assessment domain plus every CAP'd statement, and confirming no significant scope change, no security events, no maturity degradation and sufficient CAP progress. Handbook v1.2 also permits using an e1 or i1 **in lieu of** the interim.
6. **Rapid assessments (e1/i1 year 2)** — a rapid sampling approach that rolls forward prior scores where sampling shows no material degradation. Eligibility requires an active certification from a full validated assessment on CSF v11 or later, identical scope, a signed representation letter on or before expiry, and a qualifying MyCSF subscription. e1 core statements are never eligible (the set holds 60 or fewer statements); i1 core and any compliance-factor set of more than 60 statements may be, with a sample of 60 drawn from each eligible set.
7. **Bridge certificate (r2 only)** — 90 days of limited assurance from the expiry of a prior r2 certification. 19 randomly selected requirement statements are tested; the object may be created and submitted no more than 60 days before and up to 30 days after expiry; the entity must not have missed recertification by more than 30 days. **It does not extend the certification expiry** — HITRUST does not extend expiry dates under any circumstances, and the interval between expiry and recertification is a "certification gap" during which the entity is not certified.

**Security-event clock.** An assessed entity must notify HITRUST of a security event (including any data breach) affecting the certified environment when it either confirms the event, or when the investigation has been open for **60 days** from the date the entity identified it as a potential security event or breach. HITRUST then opens an investigation **within 30 days** of notification, may require re-evaluation of the related requirement statements, and may **suspend or revoke** the certification where maturity scores dropped below the certification threshold. Wire this into incident playbooks alongside statutory clocks — see [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md) and [breach-notification-timelines](../crosswalks/breach-notification-timelines.md).

**Inheritance** lets an entity reuse previously validated maturity scores — internally (shared services to business unit) or externally (provider to tenant), and across CSF versions. Inheritance is allowed from active e1/i1/r2 validated assessments (r2 validated-only reports: only within one year of the report date), never from a readiness or incomplete assessment into a validated one.

**Add-on outputs.** *Insights Reports* translate results for an eligible authoritative-source compliance factor selected in the assessment (e.g. HIPAA, AI risk management); availability depends on the CSF version used, and HITRUST does not publish the eligible list. *NIST CSF certification* is r2-only: for CSF v11.4.0 and later a NIST CSF v2.0 report is a purchased add-on requiring the NIST CSF 2.0 compliance factor, and is certified when the NIST-mapped HITRUST requirements average **70 or higher on every Core Function and Category**; CSF v11.3.2 and earlier produced a complimentary NIST CSF v1.1 report. *AI Security certification* — **ai1** (added to an e1 or i1) and **ai2** (added to an r2) — is available on CSF v11.4.0 and later via the "Cybersecurity for AI Systems" compliance factor, introduced by advisory HAA 2024-008 (6 December 2024). It is awarded when the AI requirement statements tailored into the assessment average at least **83** (ai1) or **62** (ai2), and it is contingent on achieving the underlying e1, i1 or r2 certification.

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| 12 Jan 2023 | HITRUST CSF v11 released (HAA 2023-001) — introduces the fully traversable, threat-adaptive e1/i1/r2 portfolio; e1 baseline of 44 requirement statements at launch, i1 182 |
| 6 Dec 2024 | CSF v11.4.0 (HAA 2024-006); HITRUST AI Security Assessment introduced (HAA 2024-008); HITRUST-issued NIST CSF v2.0 certification report introduced (HAA 2024-009); Assessment Handbook v1.1 (HAA 2024-005) |
| 22 Aug 2025 | CSF v11.6.0 — requirement consolidation; CMS ARC-AMPE added and GovRAMP CORE compliance factor added; CMMC Level 1 mapping refreshed; MARS-E v2.2 mapping removed; no change to the r2 baseline since v11.5.0 |
| 18 Dec 2025 | CSF v11.7.0 — 72 authoritative sources; adds BSI C5, APRA CPS 230, FedRAMP 20x Key Security Indicators, India DPDP Act, UK Cyber Assessment Framework, UK Data Security and Protection Toolkit; NIST SP 800-53 r5 mappings updated to Release 5.2.0; NIST IR 8374 ransomware compliance factor; e1 baseline confirmed at 43 statements |
| 13 Jan 2026 | Assessment Handbook **v1.2** (HAA 2026-001) — evidence from intermediate software platforms, expanded testing/evidence criteria, inheritance eligibility clarifications, e1/i1 usable in lieu of an interim assessment |
| 15 Apr 2026 | HITRUST QA begins enforcing Handbook v1.2 criteria on assessments submitted from this date |
| 7–8 May 2026 | CSF **v11.8.0** released (HAA 2026-002): adds Commonwealth of Virginia SEC530, NIST SP 800-137, ISO/IEC 29100:2024 and OWASP Top 10 for LLM Applications 2025; refreshes Texas Medical Records Privacy Act, PCI DSS v4.0.1 and AICPA SOC 2 TSC mappings; two e1/i1 baseline requirement statements amended, baseline sizes unchanged at 43 and 182. New e1/i1/rapid objects must use v11.8.0 from 7 May 2026 (HAA 2026-003) |
| 9 Jul 2026 | HAA 2026-004 announces the HITRUST Report Center |
| 10 Sep 2026 | Report Center goes live: assessments whose draft reports are issued after this date must share reports through it; earlier assessments may keep the existing sharing process. Assessment requirements, scoring, testing, certification criteria and QA are unchanged |

As of September 2026 **v11.8.0 is the current CSF version** and the Assessment Handbook stands at **v1.2**; no advisory after HAA 2026-004 has been published. New e1 and i1 objects can no longer be created on v11.7.0, but existing v11.7.0 e1/i1 assessments may still be submitted — HITRUST has not yet announced that submission deadline and must give at least 90 days' notice. **Re-check the advisories page before dating any requirement count, baseline or threshold** — baselines change at the requirement-statement level with almost every minor release.

## Key obligations for security/GRC teams

1. **Pick the tier against the buyer's actual demand.** e1 answers "are the basics validated?", i1 answers "is a modern control set operating?", r2 answers "is a tailored, multi-regulation programme documented, operating, measured and managed?" Do not start at r2 to satisfy an i1-level contract clause. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).
2. **Fix scope before anything else.** Systems, facilities, business units, endpoints and portable media in scope drive cost, testing volume and what the certification letter actually says. Re-scoping mid-assessment is the most common schedule killer.
3. **Budget for the maturity levels you must score.** An r2 requires policy and procedure text that *mandates every evaluative element* of each requirement statement — a documentation exercise far larger than the technical work. Use [policy-authoring](../../skills/policy-authoring/SKILL.md) and the [policy template](../../templates/policy-template.md).
4. **Score by domain, remediate by domain.** Certification is decided per domain; direct remediation at the weakest domains, not at the lowest individual scores. See [control-testing](../../skills/control-testing/SKILL.md).
5. **Plan the maintenance calendar at kickoff** — r2 interim in the 90-day window before month 12, e1/i1 renewal with no possibility of extension, bridge eligibility windows for r2. Track every date in the compliance calendar, not in an assessor's inbox.
6. **Add the HITRUST notification trigger to incident response** — confirmed event, or 60 days of open investigation, then notify HITRUST; expect a 30-day investigation and possible suspension. See [incident-regulatory-response](../../workflows/incident-regulatory-response.md).
7. **Exploit inheritance deliberately.** Map which in-scope requirements are delivered by certified providers and inherit them; for an r2 this is the only route, since carve-outs are not permitted. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
8. **Select compliance factors from a real applicability analysis**, not aspirationally — each factor adds requirement statements and testing, and only some sources are eligible for an Insights Report. See [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md).
9. **Track sub-threshold requirements as formal CAPs and exceptions**, with owners and dates; interim and rapid assessments test CAP progress directly. See [exception-management](../../skills/exception-management/SKILL.md) and the [exception request template](../../templates/exception-request.md).
10. **Report domain scores, CAP burn-down and certification dates to the board** rather than a single pass/fail. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md) and the [GRC board report template](../../templates/grc-board-report.md).

## Interplay

- **HIPAA:** HITRUST's healthcare origin means the HIPAA Security and Privacy Rules are authoritative sources, and a HIPAA Insights Report translates HITRUST results into HIPAA terms. A certification is **not** a regulatory safe harbour — it is evidence of reasonable and appropriate safeguards, not a defence in itself. See [hipaa.md](../regulations/hipaa.md).
- **SOC 2:** the AICPA Trust Services Criteria are a mapped authoritative source (mapping refreshed in v11.8.0), and both examine a defined environment — but SOC 2 is an attestation by a CPA firm against flexible criteria, while HITRUST is a certification against a fixed requirement set with centralized issuer QA. Combined or "joint" SOC 2 + HITRUST reporting is offered by assessor firms as a delivery model (confirm the terms with the firm **(verify)**; it is not a HITRUST-issued report type). See [soc2-tsc.md](soc2-tsc.md).
- **ISO/IEC 27001:** the CSF's structure derives from 27001/27002, so an existing ISMS maps well — but ISO certifies a management system with a scoped Statement of Applicability, while HITRUST scores individual requirement statements for maturity. See [iso-27001-2022.md](iso-27001-2022.md) and the [statement of applicability template](../../templates/statement-of-applicability.md).
- **NIST CSF 2.0 and SP 800-53:** r2 results can be reported as a NIST CSF scorecard and certified at ≥70 per Function and Category; 800-53 Rev. 5 mappings track Release 5.2.0 as of v11.7.0. See [nist-csf-2.md](nist-csf-2.md) and [nist-800-53.md](nist-800-53.md).
- **PCI DSS:** PCI DSS v4.0.1 is a selectable compliance factor with mappings refreshed in v11.8.0 — useful for coverage analysis, but it does not replace a PCI assessment by a QSA. See [pci-dss-4.md](pci-dss-4.md).
- **AI regimes:** ai1/ai2 certify the *security* of deployed AI systems; they are not a governance management system and do not substitute for an AI management system or risk framework. v11.8.0 adds OWASP Top 10 for LLM Applications 2025 as a source. See [ai-governance](../../skills/ai-governance/SKILL.md) and [eu-ai-act.md](../regulations/eu-ai-act.md).
- **Other mapped regimes** now selectable as compliance factors include the FTC Safeguards Rule at 16 CFR 314 (see [glba-ftc-safeguards.md](../regulations/glba-ftc-safeguards.md)) and the GDPR (see [gdpr.md](../regulations/gdpr.md)). Mappings are directional and lossy — use them for coverage analysis, never as equivalence claims. See [control-mapping](../../skills/control-mapping/SKILL.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).

## Primary sources

- HITRUST, *Introduction to the HITRUST CSF, Version 11.8.0* — publisher document: control categories, objectives and specifications, control architecture, implementation levels, authoritative-source count and list. https://hitrustalliance.net/hubfs/CSF%20v11.8/Introduction%20to%20HITRUST%20CSF%20v11.8.0.pdf
- HITRUST, *CSF v11.8.0 Summary of Changes (v11.7.1 to v11.8.0)* — publisher document: library version and requirement-level differences. https://hitrustalliance.net/hubfs/CSF%20v11.8/CSF%20Comparison%20Between%20v11.7.1%20to%20v11.8.0.pdf
- HITRUST, *Assessment Handbook* landing page — the current edition (v1.2, January 2026) is published online here. https://hitrustalliance.net/hitrust-assessment-handbook
- HITRUST, *The HITRUST Assessment Handbook, Version 1.1* (PDF, 2024) — assessment types, maturity levels, scoring rubric, certification thresholds, interim/bridge/rapid assessments, inheritance, carve-outs, security-event process, reporting. Still the downloadable edition; **re-check procedural detail against the online v1.2**. https://hitrustalliance.net/hubfs/HITRUST-Assessment-Handbook.pdf
- HITRUST advisory HAA 2023-001, *CSF Version 11 Release* (12 January 2023). https://hitrustalliance.net/advisories/haa-2023-001-csf-version-11-release
- HITRUST advisory HAA 2025-003, *HITRUST CSF Version 11.6.0 Release* (22 August 2025). https://hitrustalliance.net/advisories/haa-2025-003
- HITRUST advisory HAA 2025-005, *HITRUST CSF Version 11.7.0 Release* (18 December 2025). https://hitrustalliance.net/advisories/haa-2025-005
- HITRUST advisory HAA 2026-001, *Assessment Handbook v1.2 Release* (13 January 2026). https://hitrustalliance.net/advisories/haa-2026-001
- HITRUST advisory HAA 2026-002, *CSF Version 11.8.0 Release* (7 May 2026). https://hitrustalliance.net/advisories/haa-2026-002-csf-version-11.8.0-release
- HITRUST advisory HAA 2026-003, *CSF v11.7 Creation Deadline for e1 and i1 Assessments* (7 May 2026). https://hitrustalliance.net/advisories/haa-2026-003-csf-v11.7-creation-deadline-for-e1-and-i1-assessments
- HITRUST advisory HAA 2026-004, *HITRUST Report Center Release* (9 July 2026). https://hitrustalliance.net/advisories/haa-2026-004-hitrust-report-center-release
- HITRUST advisories index (CSF tag) — check here first for releases later than v11.8.0. https://hitrustalliance.net/advisories/tag/hitrust-framework-csf
- HITRUST product pages for e1, i1 and r2 (requirement counts, validity, rapid recertification, FAQs). https://hitrustalliance.net/assessments-and-certifications/e1 · https://hitrustalliance.net/assessments-and-certifications/i1 · https://hitrustalliance.net/assessments-and-certifications/r2
- HITRUST framework overview page. https://hitrustalliance.net/hitrust-framework
- HITRUST Trust Report (source of the breach-free percentages). https://hitrustalliance.net/trust-report
- Not confirmed in any fetched HITRUST document: the count of **19 assessment domains**, widely cited by assessor firms. Confirm against the domain list in the current MyCSF assessment object.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
