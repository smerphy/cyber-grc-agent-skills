# Risk Register — Field Guide

**How to use:** This guide explains every column in [risk-register.csv](risk-register.csv). Copy the CSV, delete the three example rows once you understand the pattern, and populate one row per risk. Keep the register as the single source of truth; export views for reporting rather than maintaining parallel copies. For the assessment method behind the scores, use [../skills/risk-assessment/SKILL.md](../skills/risk-assessment/SKILL.md). Scale definitions and aggregation pitfalls: [../context/risk-scoring.md](../context/risk-scoring.md).

## Conventions

- One risk per row. If a "risk" needs two treatment plans with different owners, it is probably two risks.
- Dates in ISO format (`YYYY-MM-DD`). Scores are integers.
- Quote any CSV field containing commas.
- Never delete rows. Closed and accepted risks stay in the register with `status` updated; history is part of the point.

## Field-by-field instructions

| Field | Instructions |
|---|---|
| `risk_id` | Stable unique ID (`R-001`, `R-002`...). Never reuse an ID, even after closure. |
| `title` | Under 10 words, specific enough to distinguish from neighbors. "Ransomware outage of production systems", not "Ransomware". |
| `risk_statement` | One sentence in if/then/resulting-in form: *If <threat exploits condition>, then <event>, resulting in <business consequence>*. The consequence must be a business outcome (outage, fine, lost revenue, safety), not a technical state. |
| `category` | Pick from a fixed taxonomy you define once (e.g., cyber, third party, compliance, availability, privacy, physical). Consistency here is what makes aggregation and reporting possible. |
| `assets_affected` | Named systems, data sets, or processes — specific enough that a control owner knows whether their asset is in scope. |
| `threat_source` | Who or what initiates: external attacker (specify sophistication if known), insider, partner, accident, natural event. |
| `inherent_likelihood` / `inherent_impact` | 1-5 rating **assuming existing controls fail or are absent**. Use the organization's defined scale anchors — see [../context/risk-scoring.md](../context/risk-scoring.md). Do not invent per-row interpretations of "4". |
| `inherent_score` | Likelihood x impact (max 25 on a 5x5). A convenience product, not a precise quantity — do not average scores across risks. |
| `existing_controls` | Controls **currently operating**, semicolon-separated. List only controls that actually reduce this risk; padding this field is the most common register failure. |
| `control_refs` | Pointers that make the controls auditable: internal policy/standard IDs plus framework references (ISO 27001 Annex A, CIS v8, NIST CSF 2.0, SOC 2 CC-series). See [../context/crosswalks/framework-crosswalk.md](../context/crosswalks/framework-crosswalk.md). |
| `residual_likelihood` / `residual_impact` / `residual_score` | Same scales, **with existing controls operating as designed**. Residual must never exceed inherent. If residual equals inherent, the listed controls are decorative — say so or remove them. |
| `treatment_decision` | One of: **Mitigate** (reduce via new/improved controls), **Accept** (within appetite; requires sign-off by `risk_owner`), **Transfer** (insurance/contract — note it rarely transfers the whole consequence), **Avoid** (stop the activity). |
| `treatment_plan` | Concrete actions with implicit deliverables. Required when decision is Mitigate; write "N/A - accepted <date> by <role>" for Accept. |
| `treatment_owner` | Role (not name) accountable for delivering the plan. Distinct from `risk_owner`. |
| `due_date` | Date the treatment plan completes. Slipped dates get re-baselined explicitly in `notes`, not silently edited. |
| `risk_owner` | Role accountable for the risk itself — senior enough to accept it or fund treatment. Usually a business role, not security. |
| `review_date` | Next scheduled re-review. Suggested cadence: quarterly for residual score ≥ 12, semi-annually for 6-11, annually below 6. |
| `status` | One of: Open - treatment in progress, Open - awaiting decision, Accepted, Transferred, Closed - mitigated, Closed - no longer applicable. |
| `linked_exceptions` | Exception IDs from the exception register that touch this risk. Process: [../skills/exception-management/SKILL.md](../skills/exception-management/SKILL.md) and [exception-request.md](exception-request.md). |
| `notes` | Insurance references, tabletop dates, re-baselining history, regulatory hooks. Anything a successor would need. |

## Common failure modes

- **Score inflation/deflation drift:** two assessors rate the same scenario differently. Fix with written scale anchors and periodic calibration sessions, not by arguing per row.
- **Control wish-listing:** listing planned controls under `existing_controls`. Planned controls belong in `treatment_plan`.
- **Orphan risks:** `risk_owner` set to "Security team". Security facilitates; the business owns.
- **Stale registers:** if more than 20% of rows have a `review_date` in the past, report that as a metric — see [../skills/grc-metrics-reporting/SKILL.md](../skills/grc-metrics-reporting/SKILL.md).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
