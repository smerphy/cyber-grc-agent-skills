# Quarterly Security & Risk Report — Board / Risk Committee

**How to use:** Target length when rendered: 4-6 pages plus appendices. Write for directors, not practitioners: business consequences, trends, and decisions — no tool names, no CVE lists, no acronym soup. Every metric shown must have a target and a trend; every red item must have an owner and a date. Metric selection and definitions: [../skills/grc-metrics-reporting/SKILL.md](../skills/grc-metrics-reporting/SKILL.md) and its [metric catalog](../skills/grc-metrics-reporting/references/metric-catalog.md). Delete guidance in *italics* before issuing.

**Reporting period:** [Qn YYYY] · **Prepared by:** [CISO] · **Date:** [YYYY-MM-DD] · **Classification:** [e.g., Board confidential]

## 1. Posture summary

*Half a page, three parts: (1) overall assessment in one sentence a director can repeat ("Security posture improved this quarter; one risk remains outside appetite"); (2) the 3-5 things that mattered this quarter; (3) the single most important thing the committee should take away. State posture against risk appetite explicitly — "improving" is meaningless without "relative to what we agreed to tolerate".*

> **Example opening:** "Posture improved: ransomware resilience work completed ahead of schedule and phishing-resistant MFA now covers 92% of staff. One risk (legacy VPN exposure, R-003) remains above appetite with remediation due August; we are requesting a decision on funding its permanent replacement (Section 7)."

## 2. Risk movement

*What changed in the risk profile since last quarter: new risks, escalations, de-escalations, closures — with the reason for each movement. Movement without explanation is noise.*

| Change | Risk | From → To | Why |
|---|---|---|---|
| [New / Up / Down / Closed] | [R-NNN title] | [e.g., 12 → 8] | [e.g., PAM rollout completed; residual re-scored at Q-review] |

## 3. Top risks

*Top 5-10 from the [risk register](risk-register.csv), residual view. "Within appetite" must reference the appetite statement the board approved.*

| Rank | Risk | Residual score / trend | Within appetite? | Treatment status | Owner | Target date |
|---|---|---|---|---|---|---|
| 1 | R-003 Unpatched internet-facing VPN appliance | 10 ▼ (was 15) | **No** | Emergency patching enrolled; ZTNA replacement decision requested (§7) | CIO | 2026-08-31 |
| 2 | [.] | | | | | |

## 4. Metrics dashboard

*8-12 metrics maximum, stable quarter to quarter so trends mean something. Each row: value, target, trend, and a one-line "so what" where off-target. Select from the [metric catalog](../skills/grc-metrics-reporting/references/metric-catalog.md); resist adding a metric you cannot act on.*

| Metric | This quarter | Target | Trend (4Q) | Commentary |
|---|---|---|---|---|
| [e.g., Phishing-resistant MFA coverage (workforce)] | 92% | 100% by Q3 | ▲ 71→84→89→92 | On track; remainder are field devices, plan in flight |
| [e.g., Critical vulnerabilities remediated within SLA (internet-facing)] | 87% | ≥ 95% | ▼ | Driven by one vendor-blocked appliance (EXC-2025-014, expires Aug) |
| [.] | | | | |

## 5. Incidents and regulatory update

*Incidents: count by severity, plus a short narrative for any significant incident — impact, response performance against plan, lessons, and any notification decisions made (reference the [notification log](incident-regulatory-notification-log.md), do not restate it). Regulatory: obligations that changed or will change, audits/certifications in flight and their results, regulator interactions. Horizon items: [../skills/regulatory-horizon-scanning/SKILL.md](../skills/regulatory-horizon-scanning/SKILL.md).*

- **Incidents this quarter:** [n significant / n moderate / n minor; comparison to prior quarter]
- **Significant incident narrative:** [If any]
- **Notifications made / declined:** [Regime, decision, status — one line each]
- **Audit and certification status:** [e.g., ISO 27001 surveillance audit passed, 2 minor NCs closed; SOC 2 Type II period ends Sep]
- **Regulatory horizon:** [2-3 items with expected impact and preparation status]

## 6. Program milestones

*Delivery against the security roadmap the board endorsed. Report slippage honestly with recovery plans — boards punish surprises, not delays.*

| Initiative | Milestone this quarter | Status | Note |
|---|---|---|---|
| [e.g., PAM rollout] | [Domain admin accounts migrated] | [Done / Slipped / At risk] | [.] |

## 7. Decisions requested

*The section the meeting exists for. Each item: the decision, the options with cost/risk trade-offs, the recommendation, and what happens if no decision is made. If this section is empty quarter after quarter, the report is informing, not governing.*

| # | Decision requested | Options and recommendation | Consequence of deferral |
|---|---|---|---|
| 1 | [e.g., Fund ZTNA replacement of legacy VPN (R-003): approve $480k FY27] | [A: replace (recommended); B: continue patch-and-monitor with risk accepted above appetite by the committee] | [Risk remains above appetite; acceptance would require committee sign-off per appetite statement] |

## Appendices

- A. Full risk register extract (residual ≥ [threshold])
- B. Metric definitions and data sources
- C. Exception summary: open exceptions by risk level, expirations next quarter ([exception-request.md](exception-request.md))
