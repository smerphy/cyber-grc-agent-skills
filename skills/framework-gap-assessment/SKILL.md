---
name: framework-gap-assessment
description: >-
  Assesses an organization's current security posture against a chosen framework
  (NIST CSF 2.0, ISO/IEC 27001:2022, CIS Controls v8, SOC 2, NIST SP 800-53,
  PCI DSS v4) and produces maturity scores, a severity-rated gap register, and a
  prioritized remediation roadmap. Use when asked for a "gap assessment", "gap
  analysis", "maturity assessment", "current-state review", "benchmark against
  a framework", or "where do we stand against X".
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

# Framework Gap Assessment

## Purpose

Run a structured current-state assessment of an organization against one security framework, score each domain on a defined 5-level maturity scale, and convert the findings into a gap report and remediation roadmap that leadership can act on. The output is evidence-based: every score traces to an interview answer, a document, or an observed artifact — never to assumption.

## When to use

- The user asks how their organization measures up against NIST CSF 2.0, ISO/IEC 27001:2022, CIS Controls v8/v8.1, SOC 2 Trust Services Criteria, NIST SP 800-53 Rev. 5, or PCI DSS v4.x.
- The user wants a maturity baseline before a certification, audit, or board reporting cycle.
- The user has partial evidence (policies, interview notes, tool exports) and wants it turned into scored findings and a roadmap.

**Do NOT use this skill when:**
- The goal is certification-specific readiness with audit mechanics (Statement of Applicability, auditor evidence lists). Use [../iso27001-readiness/SKILL.md](../iso27001-readiness/SKILL.md) or [../soc2-readiness/SKILL.md](../soc2-readiness/SKILL.md).
- The goal is translating one framework's controls into another's. Use [../control-mapping/SKILL.md](../control-mapping/SKILL.md).
- The goal is testing whether individual controls operate effectively (sampling, test procedures). Use [../control-testing/SKILL.md](../control-testing/SKILL.md). A gap assessment evaluates *existence and maturity*; control testing evaluates *operating effectiveness*.
- The user needs to know which regulations apply at all. Use [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md) first.

## Inputs to gather

Ask for these before starting. Do not begin scoring until items 1–3 are answered.

1. **Framework and version.** Exact edition matters: ISO/IEC 27001:2022 (not 2013), CIS v8 vs v8.1, PCI DSS v4.0.1, CSF 2.0 (not 1.1 — CSF 2.0 added the Govern function). If the user says "NIST", disambiguate CSF vs SP 800-53.
2. **Organizational boundary.** Whole company, a business unit, a product line, or a defined system boundary? For PCI DSS, the cardholder data environment (CDE) scope; for SOC 2, the system description boundary.
3. **Systems and locations in scope.** Data centers, cloud tenants, SaaS estate, remote workforce, OT/ICS if any.
4. **Assessment driver.** Certification prep, customer demand, board request, M&A diligence, regulator. The driver shapes severity weighting and roadmap horizon.
5. **Available evidence.** Policies, prior audits/pen tests, risk register, asset inventory, tool inventories, org chart, incident history.
6. **Interview access.** Which roles can be interviewed (CISO/security lead, IT ops, HR, legal/privacy, engineering, facilities)? If none, declare the assessment document-review-only and lower confidence accordingly.
7. **Target maturity** (optional). If the organization has a target profile or target level per domain, capture it; otherwise default the gap threshold to Level 3 (Defined) and confirm with the user.

## Procedure

1. **Confirm scope and freeze it.** Write a one-paragraph scope statement (framework + version, org boundary, systems, exclusions with justification, assessment dates, evidence cutoff date). Get user confirmation. Scope creep mid-assessment invalidates comparability of scores.

2. **Build the assessment workbook.** Enumerate the framework's domains at the level you will score:
   - NIST CSF 2.0: score at category level (22 categories across the 6 functions: Govern, Identify, Protect, Detect, Respond, Recover); record notes at subcategory level. See [../../context/frameworks/nist-csf-2.md](../../context/frameworks/nist-csf-2.md).
   - ISO/IEC 27001:2022: score clauses 4–10 (the management system) *and* the Annex A controls grouped by the four ISO/IEC 27002:2022 themes (Organizational, People, Physical, Technological — 93 controls total). See [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md).
   - CIS v8: score at control level (18 controls); note safeguard-level findings and the applicable Implementation Group (IG1/IG2/IG3). See [../../context/frameworks/cis-controls-v8.md](../../context/frameworks/cis-controls-v8.md).
   - SOC 2: score at common-criteria series level (CC1–CC9) plus any additional categories in scope (availability, confidentiality, processing integrity, privacy). See [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md).
   - NIST SP 800-53 Rev. 5: score at control-family level against the selected baseline (Low/Moderate/High). See [../../context/frameworks/nist-800-53.md](../../context/frameworks/nist-800-53.md).
   - PCI DSS v4.x: score at requirement level (12 requirements); PCI is ultimately pass/fail per requirement, so maturity scores are diagnostic, not compliance conclusions. See [../../context/frameworks/pci-dss-4.md](../../context/frameworks/pci-dss-4.md).
   - Other frameworks: the same procedure works for any pack in [../../context/frameworks/](../../context/frameworks/) — NIST SP 800-171/CMMC, FedRAMP, HITRUST CSF, CSA CCM, COBIT 2019, NERC CIP, ISO 22301, ISO 27701, ISO 42001, NIST AI RMF, Essential Eight, Cyber Essentials, TISAX. Score at the unit the framework itself defines (requirement family, domain, control objective, maturity level); each pack's "Using this in assessments" section states the right granularity and any pass/fail semantics that override maturity scoring.

3. **Gather evidence per domain.** For each domain, work through three evidence channels in order:
   a. **Document review** — policies, standards, procedures, diagrams, reports. Record document name, version, date, owner. A policy older than its stated review cycle is evidence of a governance gap, not just a stale document.
   b. **Structured interviews** — use the per-domain question banks in [references/interview-question-banks.md](references/interview-question-banks.md). Ask open questions first ("walk me through how a new laptop gets provisioned"), then close with specifics. Record who said what.
   c. **Artifact sampling** — where feasible, request one concrete artifact per claim (a ticket, a scan report, a log excerpt, a training completion export). "Show me" beats "tell me".
   **Decision point:** if interviews and documents conflict, the *observed practice* governs the score; note the discrepancy as a finding in itself.

4. **Score maturity per domain** on the 5-level scale (full anchors in [references/maturity-scale.md](references/maturity-scale.md)):

   | Level | Name | One-line semantic |
   |---|---|---|
   | 1 | Not Performed | Activity does not happen; no awareness or intent |
   | 2 | Ad Hoc | Happens inconsistently, person-dependent, undocumented |
   | 3 | Defined | Documented, approved, communicated; performed as written |
   | 4 | Managed | Measured with metrics; deviations detected and corrected |
   | 5 | Optimized | Continuously improved; metrics drive investment; automated where sensible |

   Scoring rules:
   - Score the *weakest credible evidence*, not the best anecdote. A domain with a great policy but no evidence of execution caps at Level 2.
   - Half-levels are not allowed. When torn between two levels, take the lower and record why.
   - Record a confidence tag per score: High (artifact-backed), Medium (interview-backed), Low (single source or document-only).
   - Not Applicable is permitted only with a written justification tied to the scope statement (e.g., no physical offices → parts of physical controls N/A). N/A without justification is a scoping error.

5. **Identify gaps and rate severity.** A gap exists wherever current level < target level, or a mandatory framework element is absent regardless of maturity. Rate severity on two axes and combine:
   - **Exposure**: what can go wrong because of this gap (tie to threats and to the risk register — cross-reference [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md)).
   - **Obligation**: does the gap block a certification, contract, or legal requirement the user named as a driver?
   - Severity = Critical / High / Medium / Low. Reserve Critical for gaps that are both high-exposure and obligation-blocking (e.g., no MFA on internet-facing admin access; no incident response capability at all).

6. **Draft the gap report** using the skeleton in [references/gap-report-structure.md](references/gap-report-structure.md): executive summary, scorecard, gap register, evidence appendix. Every gap row must carry: domain reference, current level, target level, finding statement, evidence pointer, severity, recommended remediation, suggested owner, effort estimate (S/M/L).

7. **Build the remediation roadmap.** Sequence gaps into waves:
   - **Wave 1 (0–90 days):** Critical gaps and cheap/fast High gaps ("quick wins").
   - **Wave 2 (90–180 days):** Remaining High, plus foundational dependencies (asset inventory, logging) that later work relies on.
   - **Wave 3 (180–365 days):** Medium gaps and maturity uplift from Level 3 to 4 where the target demands it.
   - Sequence by dependency, not only severity: you cannot do meaningful detection engineering (CSF DE) before asset and log coverage exist (CSF ID/PR; CIS Controls 1, 2, 8).
   - Gaps accepted rather than remediated must go through [../exception-management/SKILL.md](../exception-management/SKILL.md) — say so in the roadmap.

8. **Review with the user.** Walk through Critical/High findings first, confirm factual accuracy of evidence citations, adjust scores only when *new evidence* is produced — never to negotiation. Then finalize.

## Output format

Deliver three artifacts (structures detailed in [references/gap-report-structure.md](references/gap-report-structure.md)):

1. **Scorecard** — one row per scored domain: `Domain | Current level | Target level | Confidence | Gap? (Y/N)`.
2. **Gap register** — one row per gap:

   | ID | Framework ref | Finding | Evidence | Current → Target | Severity | Recommendation | Owner | Effort |
   |---|---|---|---|---|---|---|---|---|
   | GAP-07 | CSF 2.0 PR.AA-02 / CIS 6.5 | MFA enforced for VPN but not for the three break-glass domain admin accounts | Interview: IT Ops lead, 2026-07-02; Entra ID CA policy export | 2 → 3 | Critical | Enroll break-glass accounts in phishing-resistant MFA with monitored exclusion procedure | Head of IT | S |

3. **Remediation roadmap** — waves with target dates, dependencies, and effort totals per wave.

Executive summary rules: one page maximum; lead with the three most consequential gaps and overall maturity distribution (e.g., "14 of 22 CSF categories at Level 2 or below"); no framework jargon without a plain-language gloss.

## Quality checklist

Pass/fail before delivery:

- [ ] Scope statement names framework **and version**, boundary, exclusions with justification, and evidence cutoff date.
- [ ] Every score has at least one cited evidence item; artifact-backed scores marked High confidence, document-only marked Low.
- [ ] No score exceeds Level 2 without evidence of documented *and executed* practice.
- [ ] Every N/A has a written justification traceable to the scope statement.
- [ ] Every gap register row has framework reference, evidence pointer, severity, recommendation, owner, and effort.
- [ ] No Critical severity assigned to a gap that is neither high-exposure nor obligation-blocking.
- [ ] Roadmap waves respect dependencies (inventory/logging before detection/response uplift).
- [ ] PCI DSS assessments state explicitly that maturity scores are diagnostic and do not constitute a compliance determination.
- [ ] Executive summary fits one page and states the maturity distribution numerically.
- [ ] Interview-vs-document conflicts are recorded as findings, not silently resolved.

## References

- [references/interview-question-banks.md](references/interview-question-banks.md) — per-domain question banks (CSF 2.0 functions; ISO 27001 clauses 4–10 and Annex A themes)
- [references/maturity-scale.md](references/maturity-scale.md) — detailed scoring anchors per level with edge-case rulings
- [references/gap-report-structure.md](references/gap-report-structure.md) — full report skeleton with example rows
- [../../context/frameworks/nist-csf-2.md](../../context/frameworks/nist-csf-2.md)
- [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md)
- [../../context/frameworks/cis-controls-v8.md](../../context/frameworks/cis-controls-v8.md)
- [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md)
- [../../context/frameworks/nist-800-53.md](../../context/frameworks/nist-800-53.md)
- [../../context/frameworks/pci-dss-4.md](../../context/frameworks/pci-dss-4.md)
- [../../context/crosswalks/framework-crosswalk.md](../../context/crosswalks/framework-crosswalk.md)
- [../../context/risk-scoring.md](../../context/risk-scoring.md)
- [../../branding/brand-profile.md](../../branding/brand-profile.md) — apply the brand profile and its report style (default: consulting-classic) when formatting the gap report for stakeholders
- Related skills: [../control-mapping/SKILL.md](../control-mapping/SKILL.md), [../control-testing/SKILL.md](../control-testing/SKILL.md), [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md), [../iso27001-readiness/SKILL.md](../iso27001-readiness/SKILL.md), [../soc2-readiness/SKILL.md](../soc2-readiness/SKILL.md), [../grc-metrics-reporting/SKILL.md](../grc-metrics-reporting/SKILL.md), [../exception-management/SKILL.md](../exception-management/SKILL.md)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
