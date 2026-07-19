---
name: third-party-risk-assessment
description: >-
  Assesses the security risk of a vendor or third party: tiers the vendor by data
  access and criticality, selects the right assessment method (questionnaire, SOC 2
  review, ISO certificate verification, pen test attestation), analyzes evidence,
  produces risk findings, and defines contract clauses and monitoring cadence. Use
  when asked to "assess a vendor", "review a SOC 2 report", "onboard a supplier",
  or "run TPRM/vendor due diligence".
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Produce a defensible, decision-ready security risk assessment of a third party before onboarding or at reassessment. The output is a tier assignment, an evidence-based findings list, a risk rating with a recommendation (approve / approve with conditions / reject), required contract terms, and an ongoing monitoring plan. Depth is proportional to tier — a Tier 4 SaaS tool with no sensitive data should take minutes, not a 300-question ordeal.

## When to use

- New vendor onboarding due diligence, or periodic reassessment of an existing vendor.
- A stakeholder shares a SOC 2 report, ISO 27001 certificate, or completed security questionnaire and asks "is this vendor OK?"
- A vendor's scope of service or data access is changing (e.g., now processing production PII).
- Post-incident review of a vendor's security posture.
- **Not for:** assessing your own organization's controls — use [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md) or [../control-testing/SKILL.md](../control-testing/SKILL.md). Not for negotiating a live vendor breach — use [../incident-regulatory-reporting/SKILL.md](../incident-regulatory-reporting/SKILL.md). Not for quantifying an accepted vendor risk into the register — hand findings to [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md). Deviations from your vendor standard that the business wants to accept go through [../exception-management/SKILL.md](../exception-management/SKILL.md).

## Inputs to gather

Ask for these before starting; proceed with assumptions flagged if unavailable:

1. **Service description** — what the vendor does, and whether it is in the critical path of revenue, operations, or safety.
2. **Data involved** — categories (PII, PHI, cardholder data, credentials, IP, employee data), volume (record counts), and direction (vendor stores, processes, transits, or merely views).
3. **Access model** — network connectivity, API keys, SSO integration, agents installed on endpoints, physical access, or none.
4. **Evidence available** — SOC 2 report (Type I or II, period, which Trust Services Criteria), ISO 27001 certificate + Statement of Applicability, pen test attestation or summary, completed questionnaire, security whitepaper, insurance certificate.
5. **Regulatory context** — does the engagement pull in GDPR processor obligations, HIPAA BAA, PCI DSS third-party requirements, DORA ICT third-party rules, or GLBA Safeguards oversight? See [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md) if unclear.
6. **Business context** — contract value, term, renewal date, existing alternatives, and who the internal owner is.

## Procedure

### 1. Tier the vendor

Assign a tier using two axes — **data sensitivity/access** and **operational criticality** — taking the *higher* of the two. Full rubric with worked examples: [references/vendor-tiering.md](references/vendor-tiering.md).

| Tier | Shorthand | Typical profile | Assessment depth |
|------|-----------|-----------------|------------------|
| 1 | Critical | Stores/processes regulated or highly sensitive data at scale, OR outage halts core business within hours; privileged access to production | Full questionnaire + SOC 2 Type II review + pen test attestation + architecture review; annual reassessment; contract security schedule mandatory |
| 2 | High | Sensitive data in meaningful volume, or important business function with days of outage tolerance; some production access | SOC 2 Type II or ISO 27001 cert + SoA, plus targeted questionnaire on gaps; reassess every 12-18 months |
| 3 | Moderate | Limited sensitive data (e.g., business contact info), replaceable service | Short-form questionnaire OR verified certification; reassess every 24 months or on trigger |
| 4 | Low | No sensitive data, no connectivity, easily replaced | Registration + terms review only; no proactive reassessment, trigger-based only |

Decision point: if data sensitivity and criticality diverge by 2+ tiers, document the driver — this shapes which findings matter (confidentiality vs. availability).

### 2. Select assessment method(s)

Match evidence to tier; prefer independent attestation over self-attestation:

- **SOC 2 Type II report** — strongest common evidence for SaaS. Type I only proves design at a point in time; treat it as a partial answer and ask when the Type II period ends. See [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md).
- **ISO/IEC 27001:2022 certificate** — verify: issuing certification body is accredited (check the accreditation mark), certificate is current (3-year cycle with surveillance audits), and the **scope statement covers the service you buy** — a certificate scoped to "corporate IT of HQ office" says nothing about the SaaS platform. Request the Statement of Applicability to see excluded controls. See [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md).
- **Penetration test attestation** — accept a summary letter stating scope, date (within 12 months), methodology, tester independence, and confirmation that critical/high findings are remediated or risk-accepted. A "clean" report with no findings and no scope statement is a yellow flag, not reassurance.
- **Security questionnaire** — use [../../templates/vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md), trimmed to tier. Send the full set only to Tier 1-2. Never send a questionnaire to a vendor whose SOC 2 already answers 80% of it — extract answers from the report first, then ask only the residual questions.

### 3. Analyze the evidence

**SOC 2 report** — read in this order (full walkthrough with red flags: [references/soc2-report-review.md](references/soc2-report-review.md)):
1. **Opinion** (Section 1): unqualified, qualified, adverse, or disclaimer. Qualified = read the basis-for-qualification paragraph; adverse or disclaimer = treat as no attestation.
2. **Scope**: which TSC categories (Security is mandatory; Availability, Confidentiality, Processing Integrity, Privacy are optional), which system/product, which period. Confirm the product *you* buy is the system described. A 3-month period or a gap since the last report period warrants questions.
3. **Exceptions** (Section 4 test results): list every exception, the control it hit, management's response, and whether it touches a control you depend on (access revocation, change management, backup restoration are the usual painful ones).
4. **Complementary User Entity Controls (CUECs)**: these are *your* obligations (e.g., "customer is responsible for configuring MFA"). Extract them into your findings — an unimplemented CUEC is your gap, not the vendor's.
5. **Carve-outs / subservice organizations**: note carved-out providers (usually the cloud IaaS). Carve-out means their controls were NOT tested — check the subservice org has its own SOC 2, and review the Complementary Subservice Organization Controls list.

**Questionnaire responses** — score each answer as Adequate / Partial / Inadequate / Non-answer. Detect boilerplate ("we take security seriously", policy quotes with no operational detail) and non-answers (answering a different question, "N/A" without justification, "available under NDA" for things already under NDA). Techniques and examples: [references/questionnaire-analysis.md](references/questionnaire-analysis.md).

**Cross-check** claims against observable signals where feasible: breach history (public reporting), TLS configuration of their endpoints, published subprocessor list, status page history, security.txt / vulnerability disclosure policy.

### 4. Identify and rate findings

For each gap, write a finding: **observation → why it matters for this engagement → risk rating → required remediation or compensating control**. Rate findings in the context of the actual data and access — a missing BCP matters for a Tier 1 payments processor, not for a Tier 4 swag vendor. Use your standard risk matrix ([../../context/risk-scoring.md](../../context/risk-scoring.md)).

Decision point — overall recommendation:
- **Approve**: no high findings, or highs have credible remediation dates.
- **Approve with conditions**: highs exist but are contractually mitigated (remediation SLA in contract, compensating controls on your side, restricted data scope). Conditions must be specific and dated.
- **Reject / escalate**: critical findings with no remediation path, refusal to provide evidence commensurate with tier, or adverse/disclaimed SOC 2 opinion for a Tier 1-2 vendor. Business override of a reject goes through [../exception-management/SKILL.md](../exception-management/SKILL.md).

### 5. Set contractual requirements

Specify the security schedule clauses required for the tier before signature — retrofitting after signature rarely works. Minimum set for Tier 1-2: breach notification SLA (define the clock trigger and hours), audit/assessment rights, subprocessor approval and flow-down, data return and deletion with certification, encryption requirements, cyber insurance minimums, and annual evidence refresh (current SOC 2 / cert). Full clause checklist with negotiation fallbacks: [references/contract-clauses.md](references/contract-clauses.md).

If personal data is processed, a DPA with GDPR Art. 28 processor terms is required — coordinate with [../dpia-privacy-assessment/SKILL.md](../dpia-privacy-assessment/SKILL.md) and [../../context/regulations/gdpr.md](../../context/regulations/gdpr.md). Financial-sector engagements may trigger DORA ICT third-party contractual requirements: [../../context/regulations/dora.md](../../context/regulations/dora.md).

### 6. Define ongoing monitoring

Set cadence by tier and record triggers that force out-of-cycle reassessment:

- **Tier 1**: annual full reassessment; new SOC 2 report reviewed within 30 days of issuance; quarterly check of subprocessor list, breach news, and SLA/incident reports.
- **Tier 2**: reassessment every 12-18 months; annual evidence refresh.
- **Tier 3**: every 24 months, evidence refresh only.
- **Tier 4**: no cycle; trigger-based only.
- **Triggers (all tiers)**: vendor breach or public security incident, material scope/data change, M&A of the vendor, SOC 2 opinion downgrade or lapsed certificate, missed remediation date, contract renewal.

Feed "% vendors assessed on schedule" and "vendor findings past due" into your metrics program — see [../grc-metrics-reporting/SKILL.md](../grc-metrics-reporting/SKILL.md).

## Output format

Deliver a **Vendor Security Assessment Report**:

```
# Vendor Security Assessment: <Vendor> — <Service>
Date | Assessor | Internal owner | Tier: <1-4> (drivers: data=<x>, criticality=<y>)

## 1. Engagement summary
Service, data categories & volume, access model, regulatory context.

## 2. Evidence reviewed
| Evidence | Date/Period | Result |
e.g. SOC 2 Type II (Security, Availability), 2025-04-01 to 2026-03-31, unqualified, 2 exceptions

## 3. Findings
| # | Finding | Severity | Source | Required action | Owner | Due |
| F1 | SOC 2 exception: 3 of 25 sampled terminations exceeded 24h access-revocation SLA | Medium | SOC 2 §4 | Confirm remediation in next report; interim: quarterly access recert on our tenant | Vendor | next report |
| F2 | CUEC: customer must enforce SSO/MFA — not yet configured in our tenant | High | SOC 2 CUEC list | Enable SSO enforcement before go-live | IT Ops | pre-launch |

## 4. Recommendation
Approve with conditions: (a) F2 closed pre-launch; (b) contract includes 24h breach
notification and annual SOC 2 delivery.

## 5. Contract requirements
Checklist of required clauses with status (agreed / negotiating / rejected).

## 6. Monitoring plan
Cadence, next reassessment date, triggers, metric feed.
```

## Quality checklist

- [ ] Tier assigned with both axes documented; assessment depth matches tier (no 200-question forms to Tier 4 vendors).
- [ ] SOC 2 opinion type, period, TSC scope, and system boundary explicitly recorded — not just "SOC 2: yes".
- [ ] Every SOC 2 exception and every CUEC dispositioned (relevant or not, and why).
- [ ] Carved-out subservice organizations identified and their attestation status checked.
- [ ] ISO certificate scope statement verified against the purchased service; SoA requested for Tier 1-2.
- [ ] Every finding states engagement-specific impact, not a generic control gap.
- [ ] Recommendation is one of the three defined outcomes with dated conditions.
- [ ] Required contract clauses listed with negotiation status; DPA flagged if personal data is processed.
- [ ] Monitoring cadence and out-of-cycle triggers recorded with a named internal owner.
- [ ] Residual accepted risks routed to the risk register or exception process.

## References

- [references/vendor-tiering.md](references/vendor-tiering.md) — tiering rubric with scoring examples
- [references/soc2-report-review.md](references/soc2-report-review.md) — step-by-step SOC 2 report analysis and red flags
- [references/questionnaire-analysis.md](references/questionnaire-analysis.md) — evaluating answers, detecting non-answers and boilerplate
- [references/contract-clauses.md](references/contract-clauses.md) — security/privacy contract clause checklist
- [../../templates/vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md) — questionnaire template
- [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md) — SOC 2 Trust Services Criteria background
- [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md) — ISO 27001 certification background
- [../../context/regulations/gdpr.md](../../context/regulations/gdpr.md) — processor obligations, transfers
- [../../context/regulations/dora.md](../../context/regulations/dora.md) — ICT third-party requirements
- [../../context/risk-scoring.md](../../context/risk-scoring.md) — rating findings
- [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md) — registering residual vendor risk
- [../exception-management/SKILL.md](../exception-management/SKILL.md) — accepting deviations
- [../grc-metrics-reporting/SKILL.md](../grc-metrics-reporting/SKILL.md) — TPRM metrics

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
