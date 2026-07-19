# SOC 2 Trust Services Criteria: Control Mapping Reference

Per-criterion breakdown of the 2017 Trust Services Criteria (with revised points of focus, 2022) as used in SOC 2 examinations. For each criterion: what it requires, typical controls a service organization implements, and the evidence an auditor typically requests. The criteria are the fixed grid; the controls below are common patterns, not requirements — substitute the organization's actual controls and test them against the criterion as written.

The Security category (Common Criteria, CC-series) applies to every SOC 2. The A, C, PI, and P series apply only when their category is in scope. CC1-CC5 mirror the 17 COSO internal control principles; CC6-CC9 are the supplemental criteria where most technical audit effort concentrates.

## CC1 — Control Environment

| Criterion | Requirement | Typical controls | Typical evidence |
|---|---|---|---|
| CC1.1 | Commitment to integrity and ethical values | Code of conduct signed at hire and annually; sanctions/disciplinary policy applied consistently | Signed acknowledgments; HR disciplinary records (redacted) |
| CC1.2 | Board/oversight body independence and oversight of internal control | Board or advisory committee with security on recurring agenda; charter defining oversight | Board minutes referencing security/risk topics; committee charter |
| CC1.3 | Structures, reporting lines, authorities and responsibilities | Org chart; documented security roles (CISO or equivalent); RACI for security processes | Current org chart; role descriptions; RACI |
| CC1.4 | Attract, develop, retain competent individuals | Job descriptions with security competencies; background checks; security training program | Background check records; training completion reports; job descriptions |
| CC1.5 | Hold individuals accountable for internal control responsibilities | Performance objectives including control duties; policy violation consequences enforced | Performance review templates; escalation records |

## CC2 — Communication and Information

| Criterion | Requirement | Typical controls | Typical evidence |
|---|---|---|---|
| CC2.1 | Relevant, quality information to support internal control | Defined security metrics and logging standards; data quality checks on control-relevant data | Metrics dashboards; logging standard |
| CC2.2 | Internal communication of objectives and responsibilities | Security policies published and acknowledged; onboarding security briefing; incident reporting channel communicated to staff | Policy portal + acknowledgment logs; onboarding checklist |
| CC2.3 | Communication with external parties | Publication of security commitments (trust page, DPA terms); customer incident notification process; responsible disclosure channel | Trust page; customer notification templates and sent notices; disclosure policy |

## CC3 — Risk Assessment

| Criterion | Requirement | Typical controls | Typical evidence |
|---|---|---|---|
| CC3.1 | Objectives specified with sufficient clarity to enable risk identification | Documented service commitments and system requirements; risk assessment methodology referencing them | Commitment inventory; risk methodology doc |
| CC3.2 | Risks identified and analyzed across the entity | Annual (minimum) formal risk assessment covering the in-scope system; risk register with likelihood/impact and owners | Dated risk assessment report in-period; risk register |
| CC3.3 | Potential for fraud considered | Fraud scenarios (incl. insider misuse of access) included in risk assessment; segregation of duties analysis | Risk register fraud entries; SoD matrix |
| CC3.4 | Changes that could significantly impact internal control identified and assessed | Risk review triggered by major changes (new products, M&A, architecture shifts); change-risk gate in project process | Change-triggered risk assessments; project security review records |

## CC4 — Monitoring Activities

| Criterion | Requirement | Typical controls | Typical evidence |
|---|---|---|---|
| CC4.1 | Ongoing and/or separate evaluations of internal control | Continuous control monitoring (GRC platform or scripts); internal audits; annual penetration test; readiness assessments | Monitoring reports; pen test report; internal audit reports |
| CC4.2 | Deficiencies evaluated and communicated for corrective action | Findings tracked to remediation with owners and due dates; management reporting of open deficiencies | Findings tracker; management/board reporting showing status |

## CC5 — Control Activities

| Criterion | Requirement | Typical controls | Typical evidence |
|---|---|---|---|
| CC5.1 | Control activities selected/developed to mitigate risks to acceptable levels | Controls in the control matrix explicitly linked to risk register entries | Control matrix with risk linkage |
| CC5.2 | General control activities over technology | ITGCs: access management, change management, operations controls (largely evidenced via CC6-CC8) | Cross-reference to CC6/CC8 evidence |
| CC5.3 | Control activities deployed through policies and procedures | Policy suite covering in-scope controls; procedures current and followed; annual policy review | Policy documents with approval dates; procedure runbooks |

## CC6 — Logical and Physical Access Controls

The most heavily tested criteria group in nearly every SOC 2.

| Criterion | Requirement | Typical controls | Typical evidence |
|---|---|---|---|
| CC6.1 | Logical access security over protected information assets: identification, authentication, authorization, encryption at rest | SSO/IdP with MFA enforced; asset inventory of in-scope systems; encryption at rest on all data stores; secrets management | IdP MFA policy config; asset inventory; encryption configuration (e.g., KMS settings); secrets vault policies |
| CC6.2 | Users registered/authorized before access; credentials removed when no longer valid | Access request workflow with owner approval before grant; deprovisioning tied to HRIS termination events | Sample of access tickets with approvals; termination reconciliation (HRIS list vs IdP deactivations, with timestamps) |
| CC6.3 | Access modified/removed based on roles; least privilege and segregation of duties; periodic review | RBAC role definitions; quarterly access reviews with documented revocations; SoD rules (e.g., no self-approval of own prod changes) | Access review workpapers per quarter: scope, reviewer, sign-off, resulting revocation tickets |
| CC6.4 | Physical access to facilities and assets restricted | Badge access to offices; visitor logs; for cloud-hosted infra, inherited from IaaS provider (carve-out — cite the provider's SOC 2) | Badge system reports; visitor logs; IaaS SOC 2 report review record |
| CC6.5 | Physical assets and data disposed of securely when no longer needed | Asset disposal procedure with wipe/destruction certificates; laptop return and sanitization at offboarding | Disposal certificates; offboarding checklists |
| CC6.6 | Protection against threats from outside the system boundary | Network segmentation; security groups/firewalls default-deny; WAF; no direct internet exposure of data stores; VPN or zero-trust access to admin planes | Firewall/security-group configs; network diagram; external attack surface scan |
| CC6.7 | Information transmission/movement restricted and protected | TLS enforced for all transmission; encryption of data in transit internally where feasible; removable media restrictions; DLP where applicable | TLS configuration/scan results; MDM removable-media policy |
| CC6.8 | Prevention/detection of unauthorized or malicious software | EDR/anti-malware on endpoints and servers; MDM enforcing baseline; allowlisting or application control where used; software installation restrictions | EDR deployment coverage report; MDM compliance report |

## CC7 — System Operations

| Criterion | Requirement | Typical controls | Typical evidence |
|---|---|---|---|
| CC7.1 | Detect/monitor configuration changes and new vulnerabilities | Vulnerability scanning on defined cadence; infrastructure-as-code drift detection; remediation SLAs by severity | Scan reports across the window; remediation tickets showing SLA adherence |
| CC7.2 | Monitor system components for anomalies indicating malicious acts, natural disasters, errors | Centralized logging; SIEM/alerting rules; alert triage process | Log pipeline architecture; alert rule inventory; triage records |
| CC7.3 | Evaluate security events to determine whether they are incidents | Documented event-to-incident classification criteria; on-call triage runbook | Triage decisions on sampled alerts; classification criteria doc |
| CC7.4 | Respond to identified incidents via a defined program | Incident response plan with roles, severity levels, communication (incl. customer/regulator notification); post-incident reviews; annual IR test/tabletop | IR plan; incident tickets with timeline; tabletop report. See [incident-regulatory-reporting](../../incident-regulatory-reporting/SKILL.md) for notification obligations |
| CC7.5 | Recover from identified incidents | Recovery procedures; root-cause analysis and corrective actions tracked | Post-incident review docs; corrective action tickets |

## CC8 — Change Management

| Criterion | Requirement | Typical controls | Typical evidence |
|---|---|---|---|
| CC8.1 | Changes authorized, designed, developed/acquired, configured, documented, tested, approved, implemented | PR-based workflow: peer review required, CI tests pass, branch protection blocks direct pushes; separate deploy approval for infra changes; emergency change procedure with retrospective approval; segregation between developer and deployer where feasible (or compensating pipeline controls) | Branch protection config; sample of merged PRs with review + CI status; deployment logs reconciled to PRs; emergency change records |

Population completeness matters most here: the auditor will ask for the full list of production changes in the window (from VCS/deploy tooling) and sample from it. Manual change logs that miss deployments are a common exception source.

## CC9 — Risk Mitigation

| Criterion | Requirement | Typical controls | Typical evidence |
|---|---|---|---|
| CC9.1 | Risk mitigation for business disruption | BCP/DR plan; documented RTO/RPO for in-scope services; consideration of insurance | BCP/DR plan; DR test results (ties to A1.3 if Availability in scope); cyber insurance policy summary |
| CC9.2 | Vendor and business partner risk management | Vendor inventory with criticality tiers; security assessment before onboarding; annual review of critical vendors incl. their SOC 2 reports and CUEC mapping; contractual security/notification clauses | Vendor register; assessment records; subservice SOC 2 review memos. See [third-party-risk-assessment](../../third-party-risk-assessment/SKILL.md) |

## Availability (A-series) — when in scope

| Criterion | Requirement | Typical controls | Typical evidence |
|---|---|---|---|
| A1.1 | Capacity monitored and managed to meet commitments | Capacity/utilization monitoring with alerts; autoscaling; capacity forecasting | Monitoring dashboards; scaling configuration |
| A1.2 | Environmental protections, software, backup and recovery infrastructure in place | Automated backups with defined schedule/retention; multi-AZ or equivalent resilience; environmental controls inherited from IaaS (carve-out) | Backup configuration and job logs; architecture diagram |
| A1.3 | Recovery plan procedures tested | Periodic restore tests; DR exercise at least annually with results and lessons | Restore test records; DR exercise report |

## Confidentiality (C-series) — when in scope

| Criterion | Requirement | Typical controls | Typical evidence |
|---|---|---|---|
| C1.1 | Confidential information identified and maintained per commitments | Data classification policy; identification of confidential data locations; handling requirements per class | Classification policy; data inventory/data-flow diagram |
| C1.2 | Confidential information disposed of per commitments | Retention schedule; deletion on customer offboarding/contract end with verification | Retention schedule; deletion job logs; offboarding deletion confirmations |

## Processing Integrity (PI-series) — when in scope

| Criterion | Requirement | Typical controls | Typical evidence |
|---|---|---|---|
| PI1.1 | Quality information about processing objectives, specifications | Documented processing specifications/data definitions available to users | Product/processing specification docs |
| PI1.2 | System inputs complete and accurate | Input validation; rejection/error queues with resolution workflow | Validation rules; error queue reports and resolution records |
| PI1.3 | Processing complete, accurate, timely, authorized | Reconciliations (record counts, control totals); job monitoring with failure alerting; processing authorization gates | Reconciliation reports; job failure/rerun logs |
| PI1.4 | Outputs complete, accurate, delivered timely to specified recipients | Output reconciliation to inputs; delivery confirmations | Output reconciliations; delivery logs |
| PI1.5 | Inputs, items in processing, and outputs stored completely/accurately | Data integrity checks on stores; backup of processing data | Integrity check results; backup records |

## Privacy (P-series) — when in scope

Scope Privacy only when the organization makes privacy commitments over personal information in its own name (see step 1 of the skill). The P-series is organized into eight areas: P1 notice; P2 choice and consent; P3 collection; P4 use, retention, and disposal; P5 access; P6 disclosure and notification; P7 quality; P8 monitoring and enforcement. P6 (disclosure to third parties, breach notification to data subjects) is the largest area. Controls here overlap heavily with privacy-law compliance work — coordinate with [dpia-privacy-assessment](../../dpia-privacy-assessment/SKILL.md) and the applicable regimes ([GDPR](../../../context/regulations/gdpr.md), [US state privacy](../../../context/regulations/us-state-privacy.md)) rather than building a parallel program.

Typical control themes: published privacy notice matching actual practice (P1); consent capture and preference management (P2); collection limited to notice (P3); retention schedule and disposal execution (P4); data subject access/correction workflow with SLA tracking (P5); processor agreements, disclosure logging, breach notification procedure (P6); data accuracy mechanisms (P7); privacy complaint handling and compliance monitoring (P8).

## Mapping from existing frameworks

If the organization already holds ISO 27001 or a CIS v8 assessment, seed the matrix from the domain-level crosswalk in [framework-crosswalk](../../../context/crosswalks/framework-crosswalk.md). High-yield equivalences: ISO/IEC 27002:2022 access control and identity controls → CC6; operations security, logging, vulnerability management → CC7; change management → CC8; supplier relationships → CC9.2; ISO clause 6 risk assessment → CC3. Two cautions: (1) SOC 2 criteria are commitment-anchored — a control satisfying an ISO control generically may still fail a criterion if it does not address the org's specific service commitments; (2) ISO certification evidence (audit once/3 years on samples) is thinner than Type II evidence (full-period operation), so mapped controls still need window-long evidence trails.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
