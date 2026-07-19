# Vendor Security Questionnaire

**How to use:** Send the **Core section** to every vendor that will process organizational data or connect to organizational systems. Add the **Extended section** for high-tier vendors (critical service, sensitive/regulated data, or network/privileged access). Each question carries a *reviewer note* describing what a strong answer looks like — use it to grade responses, not just collect them. For tiering, scoring, and how questionnaire results feed a risk decision, use [../skills/third-party-risk-assessment/SKILL.md](../skills/third-party-risk-assessment/SKILL.md). Prefer evidence over assertions: request the artifact wherever the reviewer note names one.

Grade each answer: **Acceptable / Acceptable with follow-up / Deficient**. Deficient answers on questions marked ⚑ are candidate deal-breakers requiring a documented risk decision.

---

## Core section (all vendors)

### A. Organizational security

**C1.** Do you maintain a documented information security program? Who owns it, and how is it governed?
*Strong answer:* Named accountable executive (CISO or equivalent), a policy set reviewed at least annually, and governance cadence (steering committee, board reporting). Weak: "We take security seriously" with no structure.

**C2.** ⚑ Which independent certifications or attestations do you hold (e.g., ISO/IEC 27001, SOC 2 Type II, PCI DSS AOC)? Provide scope statements and issue dates.
*Strong answer:* Current report/certificate whose **scope covers the service you are buying** (check the system description and the ISO certificate scope wording, not just the logo). SOC 2 Type II preferred over Type I — see [../context/frameworks/soc2-tsc.md](../context/frameworks/soc2-tsc.md).

**C3.** Do you carry out background screening for employees with access to customer data, where legally permitted?
*Strong answer:* Screening proportional to role, performed pre-hire, with the legal-permissibility caveat acknowledged for relevant jurisdictions.

**C4.** Describe your security awareness training program, including frequency and coverage of phishing.
*Strong answer:* Mandatory at onboarding and at least annually, completion tracked with a stated rate (>95%), plus phishing simulation.

**C5.** Do you have a documented risk assessment process, and when was the last assessment?
*Strong answer:* Periodic (at least annual) assessment with a maintained register and treatment tracking; last run within 12 months.

### B. Access control

**C6.** ⚑ How is customer data logically segregated from other customers' data?
*Strong answer:* Named mechanism (per-tenant encryption keys, row-level security with tenant ID enforced in a shared access layer, or dedicated instances) and evidence it is tested (pen test coverage of cross-tenant access).

**C7.** ⚑ Is multi-factor authentication enforced for (a) your staff's access to production and (b) administrative access to the application?
*Strong answer:* MFA enforced (not "available") for both, with phishing-resistant factors for production/privileged access.

**C8.** How is privileged access to production granted, time-limited, and logged?
*Strong answer:* Just-in-time or ticket-gated elevation, session logging, no standing shared admin accounts, break-glass procedure with alerts.

**C9.** How quickly is access revoked when your staff leave or change roles, and how do you verify it?
*Strong answer:* Automated deprovisioning tied to HR events (same-day), plus periodic access recertification (quarterly for privileged).

**C10.** Does the service support SSO (SAML/OIDC) and SCIM provisioning for customers? At which pricing tier?
*Strong answer:* SSO and SCIM available on the tier being purchased. "SSO tax" (enterprise-tier-only SSO) is a negotiation item.

### C. Encryption and data protection

**C11.** ⚑ Is customer data encrypted in transit and at rest? State protocols/algorithms and where TLS terminates.
*Strong answer:* TLS 1.2+ for all external and internal service-to-service traffic; AES-256 (or equivalent) at rest; specifics rather than "military-grade encryption".

**C12.** How are encryption keys managed? Can customers hold or supply their own keys?
*Strong answer:* Managed KMS/HSM with rotation, role-separated key administration; BYOK/HYOK availability noted if the data classification demands it.

**C13.** Where is customer data stored and processed (regions), and can location be contractually constrained?
*Strong answer:* Named regions, sub-region failover behavior explained, and contractual residency commitments available. Relevant to transfer analysis under [GDPR](../context/regulations/gdpr.md).

**C14.** What are your data retention and deletion practices on contract termination? Is deletion certified?
*Strong answer:* Defined deletion window (e.g., 30-90 days including backups aging out), deletion certificate on request, and a stated backup-expiry caveat.

### D. Secure development

**C15.** Describe your secure development lifecycle: code review, SAST/DAST/SCA, and how findings are triaged.
*Strong answer:* Mandatory peer review, automated scanning in CI with severity-based fix SLAs, dependency/SBOM management. Tool names are a plus; "developers are trained in OWASP" alone is weak.

**C16.** How are development, test, and production environments separated? Is production data used in non-production?
*Strong answer:* Separate accounts/projects and credentials; production data prohibited in lower environments or masked/synthesized with a documented exception path.

**C17.** ⚑ Do you commission independent penetration tests of the service? Frequency, scope, and will you share results?
*Strong answer:* At least annual, by a reputable third party, scope includes the service being purchased; willing to share summary/attestation letter and remediation status under NDA.

**C18.** Describe your vulnerability management: scanning cadence and remediation SLAs by severity.
*Strong answer:* Continuous or at least monthly scanning across infrastructure and images; SLAs like critical ≤ 7-14 days, high ≤ 30; tracking against SLAs, with special handling for known-exploited vulnerabilities.

### E. Incident management

**C19.** ⚑ Do you have a documented incident response plan, and within what timeframe do you notify customers of incidents affecting their data?
*Strong answer:* Tested IR plan; **contractual** notification commitment with a defined window (24-72 hours from confirmation is typical; shorter is needed if the customer has regulatory clocks — see [../context/crosswalks/breach-notification-timelines.md](../context/crosswalks/breach-notification-timelines.md)); named contact channel.

**C20.** Have you experienced a reportable security incident in the last 36 months? Describe impact and remediation.
*Strong answer:* Honest disclosure with lessons learned, or a credible "no". A vague non-answer is worse than a well-handled disclosed incident.

**C21.** What logging do you retain for the service, for how long, and can customers access logs relevant to their tenant?
*Strong answer:* Centralized security logging with ≥ 12-month retention; customer-facing audit logs (admin actions, auth events) exportable via UI/API.

### F. Business continuity and disaster recovery

**C22.** What are your RTO and RPO for the service, and when did you last test recovery?
*Strong answer:* Stated RTO/RPO consistent with the customer's tolerance, backed by a DR test within 12 months and willingness to share test summary.

**C23.** Describe backup arrangements: frequency, encryption, isolation from production, and restore testing.
*Strong answer:* Automated backups, encrypted, logically or physically isolated (protects against ransomware propagation), restores tested on a schedule — not just "backups exist".

### G. Subprocessors and supply chain

**C24.** ⚑ List subprocessors that access or store customer data, their roles and locations. How are customers notified of changes?
*Strong answer:* Published, current subprocessor list; advance notice of additions with objection rights in the DPA; flow-down of equivalent security obligations.

**C25.** How do you assess the security of your own critical suppliers?
*Strong answer:* Documented third-party risk process (tiering, assessment before onboarding, periodic reassessment) — vendors have vendors; fourth-party risk is real.

---

## Extended section (high-tier vendors only)

**E1.** Provide your most recent SOC 2 Type II report (or ISO 27001 certificate + Statement of Applicability) and bridge letter covering any gap period.
*Strong answer:* Report delivered under NDA, unqualified opinion or explained exceptions, gap between report period end and today covered by a bridge letter.

**E2.** Summarize findings from your last penetration test and the remediation status of high/critical findings.
*Strong answer:* Summary with severity counts, all criticals remediated and retested, dated within 12 months.

**E3.** Describe your security monitoring capability: SOC coverage hours, detection tooling, and mean time to detect/respond targets.
*Strong answer:* 24x7 coverage (in-house or MDR), EDR + log correlation, stated MTTD/MTTR targets and measurement.

**E4.** How do you manage secrets (API keys, service credentials) in your environment?
*Strong answer:* Central secrets manager, no secrets in code (enforced by scanning), rotation on schedule and on personnel departure.

**E5.** Detail your change management process for production, including emergency change handling.
*Strong answer:* Approval and testing gates proportionate to risk, segregation between developer and deployer for sensitive systems or compensating pipeline controls, emergency changes ratified retrospectively.

**E6.** What is your patch currency for internet-facing systems? How do you handle actively exploited vulnerabilities?
*Strong answer:* Inventory-driven exposure management, expedited out-of-band process for known-exploited vulnerabilities with a ≤ 48-72 hour target.

**E7.** Describe physical security of facilities where customer data is processed (or identify the IaaS provider and your shared-responsibility split).
*Strong answer:* For cloud-hosted vendors: named IaaS provider, clear articulation of which controls the vendor owns vs. inherits.

**E8.** Do you maintain cyber insurance? State coverage limits and whether customers can be named or notified.
*Strong answer:* Current policy with limits proportionate to the engagement; understands insurance is not a control.

**E9.** How would you support us in meeting our regulatory obligations (e.g., audit rights, DORA register-of-information data points for financial-sector customers, breach notification detail)?
*Strong answer:* Contractual audit/assurance rights, familiarity with sector regimes ([DORA](../context/regulations/dora.md), [HIPAA](../context/regulations/hipaa.md), [GLBA](../context/regulations/glba-ftc-safeguards.md)) and willingness to provide required contract clauses and data points.

**E10.** Do you use AI/ML on customer data (including for product improvement or model training)? Under what controls and opt-outs?
*Strong answer:* Explicit statement of whether customer data trains models, default opt-out or contractual prohibition, human-oversight and data-isolation controls. See [../skills/ai-governance/SKILL.md](../skills/ai-governance/SKILL.md).

**E11.** Describe your personnel security for privileged roles: screening depth, insider-threat monitoring, and joiner/mover/leaver control for production access.
*Strong answer:* Enhanced screening for privileged roles where lawful, activity monitoring on production access, mover reviews that actually remove prior entitlements.

**E12.** What is your software supply chain security posture: dependency provenance, build integrity, SBOM availability?
*Strong answer:* Locked/verified dependencies, hardened build pipeline with artifact signing, SBOM available on request per release.

**E13.** How do you test and assure your BC/DR at the organizational level (not just data restore)? Include results of the last exercise.
*Strong answer:* Scenario-based exercises (region loss, ransomware) at least annually, documented findings and fixes.

**E14.** What tenant-level security configuration do customers control, and what is the secure-by-default baseline?
*Strong answer:* Documented hardening guide, secure defaults (MFA on, public sharing off), configuration API for continuous monitoring by the customer.

**E15.** Provide your data flow diagram for the service showing where our data enters, is stored, is processed, and exits (including subprocessors).
*Strong answer:* Current, legible diagram consistent with the subprocessor list and DPA — inconsistencies between C24, the DPA, and this diagram are a red flag.

---

## Reviewer summary block

| Item | Value |
|---|---|
| Vendor / service | |
| Tier | [Tier 1 (critical) / Tier 2 (high) / Tier 3 (medium) / Tier 4 (low)] |
| Questions deficient | [n of N; list ⚑ deficiencies] |
| Evidence received | [SOC 2, ISO cert + SoA, pen test summary, DPA, subprocessor list...] |
| Overall assessment | [Approve / Approve with conditions / Reject] |
| Conditions and follow-ups | [With owners and due dates; feed material residual risks into the risk register — see [risk-register.csv](risk-register.csv)] |

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
