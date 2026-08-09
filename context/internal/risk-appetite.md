# Risk Appetite and Acceptance Authority

**Status: TEMPLATE — not filled in.**

*Consumed by [risk-assessment](../../skills/risk-assessment/SKILL.md) (is a residual risk within appetite?), [exception-management](../../skills/exception-management/SKILL.md) (who may accept what), and [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md) (posture vs. appetite is the board headline). Scoring method background: [../risk-scoring.md](../risk-scoring.md). Agents: while the status is TEMPLATE, nothing below is an organizational position.*

## Appetite statements

*One statement per risk category, in business language, each with the measurable boundary that makes it testable. "Low appetite" without a threshold is a mood, not an appetite.*

| Category | Statement | Measurable boundary |
|---|---|---|
| [example: Customer data confidentiality] | [example: No appetite for preventable exposure of customer personal data] | [example: any confirmed exposure = above appetite; encryption + access review controls mandatory] |
| [example: Service availability] | [example: Limited appetite for disruption to payment processing] | [example: ≤ 4h cumulative unplanned downtime/quarter on Tier 1 services] |
| [example: Regulatory compliance] | [example: No appetite for missing mandatory regulatory deadlines] | [example: any missed notification/filing deadline = above appetite] |

## Scoring and thresholds

| Field | Value |
|---|---|
| Method / matrix | [example: 5×5 likelihood × impact, per context/risk-scoring.md caveats] |
| Score bands | [example: 1–6 low · 8–12 moderate · 15–19 high · 20–25 critical] |
| "Within appetite" rule | [example: low/moderate within; high+ requires treatment or formal acceptance] |
| Review trigger | [example: any risk crossing a band; any new critical] |

## Risk-acceptance authority matrix

*The requester never approves. Acceptance above appetite is always time-bound and recorded in the risk register or exception register — silent acceptance is the failure mode this table exists to prevent.*

| Residual level | May accept | Maximum term | Recorded in |
|---|---|---|---|
| [example: Low] | [example: system owner] | [example: 12 months] | [example: risk register] |
| [example: Moderate] | [example: CISO] | [example: 12 months] | [example: risk register] |
| [example: High] | [example: risk committee] | [example: 6 months] | [example: exception register + register] |
| [example: Critical / above appetite] | [example: board risk committee only] | [example: 3 months, remediation funded] | [example: minuted committee decision] |

## Escalation

| Trigger | Escalate to | Timeframe |
|---|---|---|
| [example: KRI threshold breach] | [example: CISO, then risk committee if unresolved] | [example: 5 business days] |
| [example: Acceptance term expiry without remediation] | [example: original approver, one level up] | [example: at expiry, automatic] |

**Document owner:** [name/team] · **Approved by:** [example: board risk committee, YYYY-MM] · **Review cycle:** [example: annual]
