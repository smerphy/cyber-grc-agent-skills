# Security Exception Request and Approval Record

**How to use:** One form per exception. The requester completes Sections 1-4; the security/GRC function completes Section 5 (risk assessment); approvers complete Section 6. File the completed record in the exception register and link it from the affected risk register row (`linked_exceptions` in [risk-register.csv](risk-register.csv)). Process, tiering logic, and register design: [../skills/exception-management/SKILL.md](../skills/exception-management/SKILL.md). Ground rules: no retroactive exceptions, no permanent exceptions, no self-approval.

## 1. Request summary

| Field | Value |
|---|---|
| Exception ID | [EXC-YYYY-NNN — assigned by GRC] |
| Date submitted | [YYYY-MM-DD] |
| Requester | [Name, role] |
| Business unit / system | [What the exception applies to — be precise about scope: which systems, accounts, or processes. "The finance file server FS-FIN-02", not "some servers"] |
| Requested duration | [Start and end date. Maximum initial duration: 12 months; shorter for higher-risk exceptions (suggested: 90 days for High, 30 days for Critical). Renewals require a fresh request and fresh approval.] |

## 2. Control or policy reference

| Field | Value |
|---|---|
| Requirement deviated from | [Exact statement ID and text — e.g., "AC-03: MFA must be enforced for all administrative access"] |
| Source document | [Policy/standard ID and version] |
| Framework/regulatory impact | [Does the deviation affect certification or compliance scope — e.g., an ISO 27001 Annex A control asserted in the [SoA](statement-of-applicability.md), a PCI DSS requirement, a SOX ITGC? Name it. Regulatory requirements often cannot be excepted internally at all — flag for compliance review.] |

## 3. Business justification

*Why compliance is not currently achievable and what the business impact of enforcing the requirement would be. Quantify where possible (cost, delay, contractual penalty). "Legacy application does not support MFA and vendor end-of-life migration completes Q1 2027" is a justification; "inconvenient for the team" is not.*

## 4. Compensating controls

*Proposed by the requester, validated by security. Each compensating control must address the same risk the original requirement addresses, and must be verifiable.*

| # | Compensating control | Addresses which aspect of the risk | Verification method |
|---|---|---|---|
| 1 | [e.g., Admin access to FS-FIN-02 restricted to two named accounts, reachable only from the PAW VLAN] | Reduces exposure of the un-MFA'd interface | Firewall rule export; account list review |
| 2 | [e.g., All admin sessions logged to SIEM with real-time alert on new account use] | Detects misuse the control would have prevented | Alert test evidence |

## 5. Risk assessment (completed by security/GRC)

| Field | Value |
|---|---|
| Risk description | [What could go wrong because of this deviation — if/then/resulting-in form] |
| Likelihood / impact / rating | [Per the organizational scale — see [../context/risk-scoring.md](../context/risk-scoring.md)] |
| Rating **with** compensating controls | [The rating that drives the approval route below] |
| Linked risk register entry | [R-NNN, or "new entry created"] |
| Assessor and date | [Name, role, YYYY-MM-DD] |

## 6. Approval record

*Route by assessed risk (with compensating controls). Higher levels include, not replace, lower-level review. Adjust roles to your organization, but keep two properties: the approver must be senior enough to own the risk, and must not be the requester or in the requester's reporting line for High/Critical.*

| Risk level | Required approver(s) | Suggested max duration |
|---|---|---|
| Low | System owner + security manager | 12 months |
| Medium | Security manager + business unit head | 6 months |
| High | CISO + risk owner (business executive) | 90 days |
| Critical | CISO + CIO/COO; risk committee notified | 30 days |

| Approver | Role | Decision | Conditions attached | Date |
|---|---|---|---|---|
| | | [Approve / Reject / Approve with conditions] | | |
| | | | | |

## 7. Expiry and review

| Field | Value |
|---|---|
| Expiry date | [Hard date. On expiry the exception lapses automatically — the default state is compliance, and continued deviation past expiry is a policy violation, not a grace period.] |
| Review checkpoint(s) | [Mid-term check for exceptions > 90 days: are compensating controls still operating? Is the remediation on track?] |
| Remediation plan and owner | [The work that removes the need for this exception, with owner and target date. An exception without a remediation path is a risk acceptance and should be recorded as one.] |
| Closure record | [Completed at closure: date, how compliance was restored, evidence reference] |

---

**Worked example (abbreviated):** EXC-2025-014 — deviation from VULN-STD-01 14-day critical patch SLA for the VPN appliance HA pair, because the vendor's current firmware breaks HA clustering (vendor case #48213). Duration 30 days. Compensating controls: exploit-attempt alerting on perimeter logs routed to SOC; admin interface reachable only from management VLAN; daily check of vendor advisory for fixed firmware. Risk with compensating controls: High (4x5 inherent → 2x5 residual). Approved by CISO and CIO 2026-07-11; expires 2026-08-10; linked to risk R-003; remediation = apply fixed firmware within 72 hours of release.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
