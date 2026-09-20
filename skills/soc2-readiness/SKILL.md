---
name: soc2-readiness
description: >-
  Guides an organization through SOC 2 Type I or Type II preparation: selecting Trust Services
  Criteria categories, defining the system boundary and system description, mapping controls to
  the Common Criteria (CC1-CC9), gap remediation, choosing Type I vs Type II and the observation
  window, auditor selection, and an evidence dry-run. Use when a user says "SOC 2 readiness",
  "prepare for SOC 2", "Type II audit prep", or "Trust Services Criteria gap".
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Take an organization from "customer asked for our SOC 2" to audit-ready: correct criteria scope, a defensible system description, controls mapped to the Trust Services Criteria, gaps closed, and evidence proven collectible before the auditor arrives. Output is a readiness package the organization can hand to a CPA firm, not the SOC 2 report itself — only a licensed CPA firm issues that.

## When to use

- Preparing for a first SOC 2 examination (Type I or Type II).
- Re-scoping before a renewal (adding Availability or Confidentiality, changing the boundary).
- A customer contract or security questionnaire demands a SOC 2 report and the organization has none.
- Mapping an existing control set (ISO 27001, CIS v8) onto the Common Criteria.
- **Not for:** general control-to-framework mapping outside SOC 2 — use [control-mapping](../control-mapping/SKILL.md). Broad maturity assessment against a framework — use [framework-gap-assessment](../framework-gap-assessment/SKILL.md). ISO 27001 certification prep — use [iso27001-readiness](../iso27001-readiness/SKILL.md) (many controls overlap; run this skill afterward for the SOC 2 delta). Designing evidence tests in depth — use [control-testing](../control-testing/SKILL.md).

## Inputs to gather

Ask for these before starting; proceed with stated assumptions if unavailable:

1. **The service in scope** — what product/service customers rely on, and which customer commitments (SLAs, DPAs, contract security exhibits) it carries.
2. **Driver and deadline** — which customer/deal needs the report and by when. This determines Type I vs Type II feasibility.
3. **Architecture summary** — cloud provider(s), production environments, data stores, CI/CD, identity provider, endpoint fleet.
4. **Existing control artifacts** — policies, prior audits (ISO 27001 SoA, pen tests), ticketing/change history, access review records.
5. **Subservice organizations** — cloud IaaS, payment processors, managed SOC, email/CRM handling in-scope data, and whether their SOC 2 reports are on file.
6. **Data sensitivity** — does the system process personal information for which the org makes privacy commitments in its own name?

## Procedure

### 1. Select Trust Services Criteria categories

Security (the Common Criteria) is mandatory in every SOC 2. Add other categories only when commitments justify them — each category adds criteria, controls, and evidence burden:

| Category | Add when | Skip when |
|---|---|---|
| Availability | Contractual SLAs/uptime commitments; customers depend on the service being up (SaaS platforms, hosting) | No uptime commitments beyond best effort |
| Confidentiality | Contracts designate customer data confidential with handling/retention/disposal commitments (most B2B SaaS) | Data handled is public or the org makes no confidentiality commitments |
| Processing Integrity | Customers rely on complete, accurate, timely processing — payments, payroll, billing, claims, data pipelines with correctness commitments | The service stores/transmits but customers own correctness |
| Privacy | The org makes privacy commitments about personal information in its own privacy notice as controller-like party | The org is a pure processor; customer privacy obligations flow through the customer (common case — Confidentiality usually suffices; check with counsel) |

Most first-time B2B SaaS reports scope Security + Availability + Confidentiality. Do not add Privacy casually — it imports the P-series criteria and notice/consent/retention evidence most processors cannot generate. Record the decision and rationale; the auditor will ask.

### 2. Define the system boundary and draft the system description

The "system" is the service, not the company. Define the boundary across the five components — infrastructure, software, people, procedures, data — and decide inclusive vs carve-out treatment for each subservice organization (carve-out is the norm for cloud IaaS). Draft the description sections and identify Complementary User Entity Controls (CUECs) and complementary subservice organization controls (CSOCs).

Full guidance, section-by-section: [references/system-description-guide.md](references/system-description-guide.md).

Decision point — boundary disputes: exclude a product line or environment only if it is operationally and logically separable and no in-scope customer commitment depends on it. A boundary that excludes the CI/CD pipeline or the identity provider that gates production access will not survive auditor scrutiny.

### 3. Map existing controls to the criteria

Build a control matrix: one row per criterion (CC1.1 through CC9.2, plus A/C/PI/P series if scoped), columns for control activity, owner, frequency, evidence source, automation status. The CC series structure:

- **CC1-CC5** — entity-level criteria aligned to the [COSO internal control framework](../../context/frameworks/coso-internal-control-erm.md): control environment (CC1), communication and information (CC2), risk assessment (CC3), monitoring activities (CC4), control activities (CC5).
- **CC6** — logical and physical access controls (provisioning, deprovisioning, authentication, encryption, physical security).
- **CC7** — system operations (vulnerability management, monitoring, incident detection and response, recovery).
- **CC8** — change management.
- **CC9** — risk mitigation (business disruption, vendor and business partner risk).

Per-criterion control examples and evidence: [references/tsc-control-mapping.md](references/tsc-control-mapping.md). If the org has an ISO 27001 SoA or CIS v8 assessment, seed the matrix from [../../context/crosswalks/framework-crosswalk.md](../../context/crosswalks/framework-crosswalk.md) rather than starting blank — then verify each mapped control actually addresses the criterion as written, not just the same topic.

Every criterion needs at least one control; most need several. Criteria are the fixed grid; controls are the org's own — the auditor tests the org's controls against the criteria.

### 4. Gap-remediate

For each criterion with no control, a design-deficient control, or a control with no evidence trail:

1. Classify: missing control / control exists but undocumented / control documented but not operating / evidence not retained.
2. Prioritize by (a) criteria auditors test hardest first — access management (CC6), change management (CC8), risk assessment (CC3.1-CC3.2) — and (b) remediation lead time. Quarterly-cadence controls (access reviews, DR tests) need a full cycle of history before a Type II window closes, so start them first.
3. Fix policy gaps via [policy-authoring](../policy-authoring/SKILL.md); run formal risk assessment via [risk-assessment](../risk-assessment/SKILL.md); document any accepted gaps via [exception-management](../exception-management/SKILL.md).
4. Set a "controls operating" date — the earliest date every in-scope control is designed, documented, and producing evidence. The Type II window cannot start before this date.

### 5. Decide Type I vs Type II and the observation window

- **Type I**: design and implementation as of a point in time. Fast (achievable weeks after controls operate), but many enterprise customers discount or reject it.
- **Type II**: design plus operating effectiveness over a period — the market expectation. Window is typically 3-12 months; 12 months is the steady-state norm.

Decision rule for first audits: if the deal deadline allows ≥3 months of stable control operation, go straight to a 3- or 6-month Type II. Use Type I only as a bridge when a customer needs paper now — and tell the customer the Type II window has already started. Do not start the Type II window until step 4's "controls operating" date; every control must operate for the entire period or the auditor flags it. Plan the steady-state cycle: consecutive 12-month windows with no coverage gap between report periods, since customers scrutinize gaps.

### 6. Select the auditor

Criteria that matter: CPA firm licensed for attestation work; SOC 2 practice depth in the org's stack (cloud-native vs on-prem); willingness to do a readiness/pre-assessment phase distinct from the examination (same firm may do both, but the readiness output must not amount to the firm auditing its own remediation design); auditor's stance on the org's GRC automation platform (some firms accept platform-collected evidence wholesale, others re-pull); fee structure covering the readiness phase, the exam, and the bridge letter, if needed. Get the proposed report timeline in writing: fieldwork start relative to window end, and draft-to-final duration — customers waiting on the report care about the gap between window close and report issuance.

### 7. Run an evidence dry-run

4-6 weeks before fieldwork (Type II) or the as-of date (Type I), simulate the auditor's request list:

1. For every control in the matrix, pull the actual evidence for a sample: 2-3 months of access reviews, 5-10 change tickets, 3-5 onboarding/offboarding cases, incident records, backup/restore test results, vulnerability scan cadence.
2. Test population completeness — can the org produce the full list of hires, terminations, and changes for the window from a system of record (HRIS, VCS, ticketing), not from memory? Auditors sample from populations; an incomplete population is itself a finding.
3. Check evidence quality: timestamped, attributable to a person, showing the review actually happened (comments, approvals) — not a screenshot taken yesterday of a setting that says the right thing.
4. Log every failure in a punch list with owner and date; re-verify before fieldwork. Use [control-testing](../control-testing/SKILL.md) for test design and [audit-preparation](../audit-preparation/SKILL.md) for request-list logistics.

### 8. Pre-empt common first-audit exceptions

| Common exception | Avoidance |
|---|---|
| Terminated user access not removed within policy SLA | Automate deprovisioning from HRIS trigger; weekly reconciliation of IdP vs HRIS |
| Access reviews missing, late, or rubber-stamped | Calendar-driven quarterly reviews with documented scoping, reviewer sign-off, and remediation tickets for revocations |
| Changes deployed without documented approval/testing | Enforce PR review + CI checks in the pipeline (technical control beats procedural); no direct-to-prod pushes |
| Risk assessment stale or not performed in-period | Annual formal risk assessment dated inside the window ([risk-assessment](../risk-assessment/SKILL.md)) |
| Vendor reviews not performed for critical subservice orgs | Annual review of subservice SOC 2 reports incl. CUEC mapping ([third-party-risk-assessment](../third-party-risk-assessment/SKILL.md)) |
| Policy approvals expired mid-window | Annual policy review cycle with tracked approvals ([policy-review](../policy-review/SKILL.md)) |
| Backup restores never tested | Scheduled restore tests with recorded results, at least quarterly for critical data |
| Employee security training incomplete | Training assigned at onboarding + annually, completion tracked with escalation |

An exception does not automatically mean a qualified opinion — but a clean first report is a sales asset, and each item above is cheap to prevent and expensive to explain in the report's Section 4.

## Output format

Deliver a **SOC 2 Readiness Package** with these sections:

1. **Scope decision memo** — criteria categories with rationale, system boundary, subservice orgs and inclusive/carve-out treatment, Type and window recommendation.
2. **Control matrix** — per criterion: control(s), owner, frequency, evidence source, status (Operating / Gap / Remediation-in-progress).
3. **Gap remediation plan** — gap, criterion, severity, owner, due date, dependency on window start.
4. **Draft system description** — per the structure in [references/system-description-guide.md](references/system-description-guide.md).
5. **Evidence dry-run results** — punch list of evidence failures.
6. **Timeline** — controls-operating date, window start/end, fieldwork, report issuance.

Worked example (matrix excerpt):

| Criterion | Control | Owner | Freq | Evidence | Status |
|---|---|---|---|---|---|
| CC6.2 | Access provisioned via role-based request in Jira, approved by resource owner before IdP grant | IT Ops | Per event | Jira tickets + Okta grant logs | Operating |
| CC6.3 | Termination triggers same-day IdP suspension from HRIS webhook | IT Ops | Per event | HRIS event log + Okta deactivation log | Gap: manual, SLA misses in March |
| CC8.1 | Prod changes require approved PR + passing CI; branch protection enforced | Eng Lead | Per change | GitHub PR history, branch protection config | Operating |

## Quality checklist

- [ ] Security criteria in scope; every added category is tied to a named customer commitment.
- [ ] System boundary covers all five components; no in-scope commitment depends on an excluded system.
- [ ] Every subservice org classified inclusive or carve-out; carve-out CSOCs identified.
- [ ] Every in-scope criterion (CC1.1-CC9.2 + category series) has ≥1 mapped control with named owner and evidence source.
- [ ] Type II window starts no earlier than the controls-operating date; periodic controls complete ≥1 full cycle in-window.
- [ ] Evidence dry-run performed with population-completeness checks; punch list closed before fieldwork.
- [ ] CUECs drafted for every customer-side dependency (e.g., customer manages its own user access).
- [ ] All eight common-exception areas verified against current practice.
- [ ] Deliverable states that the examination itself requires a licensed CPA firm.

## References

- [references/tsc-control-mapping.md](references/tsc-control-mapping.md) — CC1-CC9 and category criteria with typical controls and evidence per criterion.
- [references/system-description-guide.md](references/system-description-guide.md) — five system components, description structure, CUECs, inclusive vs carve-out.
- [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md) — Trust Services Criteria overview, Type I vs Type II.
- [../../context/frameworks/soc1-isae3402-soc-reports.md](../../context/frameworks/soc1-isae3402-soc-reports.md) — SOC 1 / ISAE 3402 and the rest of the SOC family, for choosing the right report.
- [../../context/frameworks/coso-internal-control-erm.md](../../context/frameworks/coso-internal-control-erm.md) — the components and principles the CC1-CC5 entity-level criteria are built on.
- [../../context/crosswalks/framework-crosswalk.md](../../context/crosswalks/framework-crosswalk.md) — seed mappings from ISO 27001 / CIS v8 / CSF 2.0.
- Assurance products customers ask for alongside or instead of SOC 2: [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md), [../../context/frameworks/iso-27017-27018-cloud.md](../../context/frameworks/iso-27017-27018-cloud.md), [../../context/frameworks/iso-27701-privacy-management.md](../../context/frameworks/iso-27701-privacy-management.md), [../../context/frameworks/csa-ccm-star.md](../../context/frameworks/csa-ccm-star.md) (STAR Attestation rides on a SOC 2 engagement), [../../context/frameworks/hitrust-csf.md](../../context/frameworks/hitrust-csf.md), [../../context/frameworks/fedramp.md](../../context/frameworks/fedramp.md), [../../context/frameworks/nist-csf-2.md](../../context/frameworks/nist-csf-2.md)
- Technical baselines behind common logical-access, change and incident controls: [../../context/frameworks/nist-800-63-digital-identity.md](../../context/frameworks/nist-800-63-digital-identity.md), [../../context/frameworks/nist-800-207-zero-trust.md](../../context/frameworks/nist-800-207-zero-trust.md), [../../context/frameworks/nist-ssdf-800-218.md](../../context/frameworks/nist-ssdf-800-218.md), [../../context/frameworks/owasp-application-security.md](../../context/frameworks/owasp-application-security.md), [../../context/frameworks/nist-800-61-incident-handling.md](../../context/frameworks/nist-800-61-incident-handling.md), [../../context/frameworks/cis-controls-v8.md](../../context/frameworks/cis-controls-v8.md)
- [../control-testing/SKILL.md](../control-testing/SKILL.md) — designing and executing evidence tests.
- [../audit-preparation/SKILL.md](../audit-preparation/SKILL.md) — fieldwork logistics and request-list management.
- [../iso27001-readiness/SKILL.md](../iso27001-readiness/SKILL.md) — overlapping certification track.
- [../third-party-risk-assessment/SKILL.md](../third-party-risk-assessment/SKILL.md) — subservice organization reviews.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
