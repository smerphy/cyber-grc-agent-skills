# SOC 2 and the Trust Services Criteria

## At a glance

| Attribute | Detail |
|---|---|
| Owner | AICPA (American Institute of Certified Public Accountants) |
| Criteria | Trust Services Criteria (TSC), TSP Section 100 — 2017 version, with revised points of focus issued 2022 |
| Attestation standard | AT-C Section 205 (examination engagements) under SSAE attestation standards |
| Categories | 5: Security (mandatory), Availability, Confidentiality, Processing Integrity, Privacy |
| Common Criteria | CC1–CC9 (Security category = the Common Criteria; always in scope) |
| COSO alignment | CC1–CC5 map directly to the 17 principles of the COSO 2013 Internal Control framework |
| Report types | Type I (design at a point in time) vs Type II (design + operating effectiveness over a period) |
| Who performs it | Licensed CPA firm; output is an attestation report with an auditor's opinion, not a certificate |
| Typical Type II period | 6–12 months (3-month minimum periods exist in practice for first reports) |
| Report distribution | SOC 2 is restricted-use; SOC 3 is the general-use summary |

## What SOC 2 is (and is not)

SOC 2 is an attestation engagement: a CPA firm examines a service organization's description of its system and its controls against the Trust Services Criteria and issues an opinion. Key consequences for GRC work:

- There is no "SOC 2 certification" and no pass/fail score. The deliverable is a report containing an opinion (unqualified, qualified, adverse, or disclaimer) plus detailed test results.
- The service organization chooses the scope: which system(s), which trust services categories, and (for Type II) the review period.
- Criteria are principles-based. The TSC defines *what* must be achieved; the organization defines *how* through its own controls. Two clean SOC 2 reports can rest on very different control sets.
- The 2022 revision updated the **points of focus** (illustrative considerations under each criterion) — the criteria themselves and their numbering did not change from the 2017 TSC.

## The five trust services categories

| Category | Criteria series | Mandatory? | Covers |
|---|---|---|---|
| Security | CC1–CC9 (Common Criteria) | Yes — every SOC 2 includes it | Protection against unauthorized access, disclosure, and damage to systems |
| Availability | A-series | Optional | System availability for operation and use per commitments/SLAs |
| Confidentiality | C-series | Optional | Protection of information designated confidential (broader than personal data) |
| Processing Integrity | PI-series | Optional | Complete, valid, accurate, timely, authorized processing |
| Privacy | P-series (P1–P8) | Optional | Personal information lifecycle: notice, choice/consent, collection, use/retention/disposal, access, disclosure, quality, monitoring |

Scoping guidance: Availability is the most commonly added category for SaaS. Confidentiality is often added when customer contracts reference confidential business data. Privacy is the heaviest lift and overlaps substantially with privacy-law obligations — if the driver is GDPR/CCPA compliance, a privacy-specific assessment (see [../regulations/gdpr.md](../regulations/gdpr.md) and [../regulations/us-state-privacy.md](../regulations/us-state-privacy.md)) is usually the better instrument; the P-series is driven by the organization's own privacy commitments.

## Common Criteria structure (CC1–CC9)

CC1–CC5 are drawn from COSO 2013; CC6–CC9 are supplemental criteria specific to the TSC.

| Series | Title | Typical control content |
|---|---|---|
| CC1 | Control Environment | Integrity/ethics, board oversight, org structure, competence, accountability (COSO principles 1–5) |
| CC2 | Communication and Information | Internal/external communication of objectives, responsibilities, system changes; quality of information |
| CC3 | Risk Assessment | Objective-setting, risk identification and analysis, fraud risk, assessing significant change |
| CC4 | Monitoring Activities | Ongoing/separate evaluations (e.g., internal audit, control self-assessment), deficiency communication |
| CC5 | Control Activities | Selection and deployment of control activities and technology controls; policies and procedures |
| CC6 | Logical and Physical Access Controls | Identity and access management, authentication, provisioning/deprovisioning, physical access, data protection at rest/in transit, disposal |
| CC7 | System Operations | Vulnerability management, security monitoring/detection, incident response and recovery |
| CC8 | Change Management | Authorization, design, development, testing, approval, and implementation of changes |
| CC9 | Risk Mitigation | Risk mitigation activities including business disruption and **vendor/business-partner risk management** |

Practitioner notes:

- The bulk of technical evidence requests in a SOC 2 audit land in CC6 (access), CC7 (operations/monitoring/incidents), and CC8 (change).
- CC9.2 is the anchor for third-party risk management controls — cross-reference [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
- CC3 and CC4 expect a functioning risk assessment and monitoring cadence, not just documents — see [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).

## Type I vs Type II

| Dimension | Type I | Type II |
|---|---|---|
| Question answered | Were controls suitably designed and implemented **as of a date**? | Were controls suitably designed **and operating effectively over a period**? |
| Testing | Design and implementation only | Design + operating effectiveness (sampling across the period) |
| Section on tests of controls | Not included | Included ("Tests of Controls and Results" — the longest section) |
| Market acceptance | Weak — a stepping stone at best | The de facto expectation for vendor due diligence |
| Typical use | First-time report while building operating history | Annual recurring report, often with back-to-back periods to avoid coverage gaps |

When reviewing a vendor's Type II, check for **coverage gaps** between consecutive report periods and for a **bridge letter** (gap letter) covering the interval between period end and the review date. A bridge letter is a management representation, not auditor-attested.

## Anatomy of a SOC 2 report

1. **Independent Service Auditor's Report (opinion)** — the auditor's opinion on (a) fairness of the system description, (b) suitability of control design, and (c) for Type II, operating effectiveness. Read this first; note whether the opinion is qualified and why.
2. **Management's Assertion** — management asserts the description is fair and controls were suitably designed/operating.
3. **System Description** (management-authored) — services, system boundaries, components (infrastructure, software, people, procedures, data), relevant aspects of the control environment, complementary controls, and significant changes during the period.
4. **Tests of Controls and Results** (Type II) — each control, the auditor's test procedure, and the result. Exceptions are listed here; an exception does not automatically qualify the opinion — the auditor judges whether criteria are still met by other controls.
5. **Other Information** (optional, unaudited) — commonly management's responses to exceptions.

### CUECs and subservice organizations

- **Complementary User Entity Controls (CUECs):** controls the *customer* must operate for the system's criteria to be met (e.g., "customers are responsible for managing their own user accounts"). When reviewing a vendor report on your organization's behalf, extract the CUEC list and verify your side implements each one — this is a frequently missed step.
- **Complementary Subservice Organization Controls (CSOCs):** controls expected of the vendor's own subservice providers.
- **Carve-out vs inclusive method:** carve-out excludes the subservice organization's controls from the report (the norm — e.g., a SaaS provider carves out AWS and lists CSOCs); inclusive brings the subservice organization's controls inside scope and testing (rare, requires cooperation). For carve-outs, obtain and review the subservice organization's own SOC report.

## SOC 1 vs SOC 2 vs SOC 3

| | SOC 1 | SOC 2 | SOC 3 |
|---|---|---|---|
| Subject matter | Controls relevant to user entities' **internal control over financial reporting (ICFR)** | Controls relevant to security, availability, confidentiality, processing integrity, privacy | Same as SOC 2 |
| Criteria | Control objectives defined by the service organization | Trust Services Criteria | Trust Services Criteria |
| Standard | AT-C 320 | AT-C 205 | AT-C 205 |
| Audience | Restricted: user entities and their financial auditors | Restricted: management, customers, prospects under NDA, regulators | General use — public marketing |
| Detail level | Full tests and results | Full tests and results | Summary only, no test detail |
| Typical driver | Customer's SOX / financial audit (see [../regulations/sox-itgc.md](../regulations/sox-itgc.md)) | Security due diligence | Public trust signal |

Payroll processors, fund administrators, and claims processors typically need SOC 1; SaaS/cloud providers typically need SOC 2; many need both.

## Using this in assessments

- **Readiness work:** map existing controls to each in-scope criterion, identify gaps, remediate, then consider a readiness assessment before the audit period starts. Full procedure: [../../skills/soc2-readiness/SKILL.md](../../skills/soc2-readiness/SKILL.md).
- **Reviewing a third party's report:** check (1) opinion type and any qualifications, (2) report period freshness and gaps, (3) scope — right system, right categories, right locations, (4) exceptions in the tests section and management responses, (5) CUECs assigned to your organization, (6) carved-out subservice organizations and whether you need their reports. Feed results into [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
- **Mapping to other frameworks:** the TSC maps well to ISO/IEC 27001 Annex A, CIS Controls v8, and NIST CSF 2.0 at the domain level — see [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md) and [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md). Because TSC criteria are principles-based, map at the control-activity level, not criterion-to-control one-to-one.
- **Evidence realism:** for a Type II, controls must operate for the whole period. A control implemented mid-period will show as an exception or be excluded. Plan remediation to complete *before* the period starts.
- **Common pitfalls:** treating points of focus as mandatory requirements (they are illustrative); scoping only "Security" when customer contracts promise uptime (add Availability); ignoring CUECs; accepting a Type I or an expired report in vendor due diligence without compensating inquiry.

## References

- Related frameworks: [iso-27001-2022.md](iso-27001-2022.md), [nist-csf-2.md](nist-csf-2.md), [cis-controls-v8.md](cis-controls-v8.md)
- Crosswalk: [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md)
- Skills: [../../skills/soc2-readiness/SKILL.md](../../skills/soc2-readiness/SKILL.md), [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md), [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md)

## Primary sources

- [AICPA Audit & Assurance topic hub (Trust Services Criteria, SOC suite guidance)](https://www.aicpa-cima.com/topic/audit-assurance)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
