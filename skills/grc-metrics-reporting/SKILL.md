---
name: grc-metrics-reporting
description: >-
  Designs GRC metrics programs (KPIs and KRIs) and board-level security reporting.
  Selects metrics tied to actual decisions, defines each with formula, data source,
  target, and thresholds, designs trend presentation, and drafts the board narrative
  covering risk posture, movement, and asks. Use when asked for "security KPIs",
  "risk metrics", "KRIs", "board deck for security", "CISO dashboard", or "how do we
  measure our security program".
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Build a metrics program that changes decisions, and reporting that gives a board what it needs for oversight: posture, movement, and what is being asked of them. The failure mode this skill prevents is the vanity dashboard — 40 counts nobody acts on ("12,438 attacks blocked") — replaced by a small set of metrics each wired to a threshold, an owner, and a defined response when the threshold breaks.

## When to use

- Standing up or overhauling a security/GRC metrics program.
- Preparing or improving a board or executive risk report.
- A regulator, auditor, or framework requires demonstrated measurement (e.g., ISO 27001 clause 9 performance evaluation; SOC 2 monitoring criteria; board oversight expectations under SEC 10-K Item 106 disclosure of board oversight — see [../../context/regulations/sec-cyber-disclosure.md](../../context/regulations/sec-cyber-disclosure.md)).
- Choosing KRIs to attach to risk appetite statements.
- **Not for:** performing the underlying risk analysis — [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md). Not for testing whether controls work (metrics consume those results) — [../control-testing/SKILL.md](../control-testing/SKILL.md). Not for one-off incident reporting to regulators — [../incident-regulatory-reporting/SKILL.md](../incident-regulatory-reporting/SKILL.md).

## Inputs to gather

1. **Audience(s)**: board, executive committee, CISO staff, control owners — each gets different altitude. Ask which report is being built first.
2. **Decisions in scope**: what has this audience actually decided in the last year (budget, risk acceptance, program priorities)? Metrics attach to these.
3. **Risk appetite statements** if they exist — KRIs operationalize them.
4. **Available data sources**: vulnerability scanner, identity platform, ticketing, GRC tool, HR system, phishing platform, TPRM records. A metric without an automatable source will silently die.
5. **Current reporting**: what is sent today, and which parts does the audience ignore or question?
6. **Reporting cadence and constraints**: board slot length (often 10-15 minutes), page/slide limits.

## Procedure

### 1. Anchor every metric to a decision

For each candidate metric, complete: *"If this crosses <threshold>, <who> will <do what>."* If no honest completion exists, drop the metric. Distinguish:

- **KPI** (performance): is the program doing what we said? (e.g., patching SLA attainment). Owner: operations.
- **KRI** (risk): is exposure moving toward/away from appetite? (e.g., open high risks past due, unmanaged asset percentage). Owner: risk function; breach of threshold escalates.
- **Vanity count**: raw volumes with no denominator or decision ("blocked attacks", "alerts triaged"). Exclude, or use once as context, never as a tracked metric.

Target 8-12 metrics for an executive/board view, 15-25 for the CISO operational view. More than that and nothing gets attention.

### 2. Define each metric precisely

Use this definition record for every metric (extended catalog with 25+ entries: [references/metric-catalog.md](references/metric-catalog.md)):

| Field | Content |
|-------|---------|
| Name | Short, unambiguous |
| Formula | Exact numerator/denominator, units, inclusion rules |
| Source | System of record + extraction method; manual sources flagged |
| Cadence | Measurement and reporting frequency |
| Target | Desired steady state |
| Threshold(s) | Amber/red trigger values and the defined response |
| Owner | Accountable for the number; distinct from who produces it |
| Gaming risk | How the metric can be made to look good without improving reality, and the counter-metric |

Definition rules: always ratio or time-based, never raw counts without denominators; define the population exactly ("critical vulns" = which severity source, which asset scope); pin the SLA clock start (detection date, not ticket-creation date); state exclusions explicitly (decommissioned assets, accepted risks) so the number is reproducible by someone else.

### 3. Starter metric catalog

Twelve defaults covering the major domains. Adjust populations and targets to context; targets below are common starting points, not standards.

| # | Metric | Formula | Type | Typical target |
|---|--------|---------|------|----------------|
| 1 | Critical vuln SLA attainment | % of critical-severity vulns on in-scope assets remediated within SLA (e.g., 15 days) in period | KPI | ≥90% |
| 2 | Control test pass rate | Controls passing / controls tested in period, by domain | KPI | ≥95%, no repeat fails |
| 3 | Mean time to revoke access | Mean hours from termination effective time to full access revocation (p95 alongside mean) | KPI | <24h mean, p95 <72h |
| 4 | Vendors assessed on schedule | Tier 1-2 vendors with current-cycle assessment / total Tier 1-2 vendors | KPI | ≥95% |
| 5 | Open high/critical risks past due | Count of register risks rated high+ whose treatment date has passed | KRI | 0; any is red |
| 6 | Policy attestation rate | Staff completing required attestation / staff in scope, 30 days post-launch | KPI | ≥97% |
| 7 | Phishing simulation failure trend | % clicking (and separately, % reporting) per campaign, trended over 4+ campaigns | KRI | Click declining; report rate rising |
| 8 | Audit finding aging | Open findings by age bucket (<30/30-90/>90 days past due), weighted by severity | KRI | 0 high findings >90 days past due |
| 9 | MFA/SSO coverage | Accounts with strong auth enforced / total accounts, split workforce vs. privileged | KPI | Privileged 100%; workforce ≥99% |
| 10 | Unmanaged asset rate | Assets seen on network not in inventory+management tooling / total observed | KRI | <2% and falling |
| 11 | Mean time to detect/contain incidents | Median (not mean) hours detection→containment for confirmed incidents, by severity | KPI | Trending down; small-n caveat stated |
| 12 | Exception load | Open security exceptions, count and % past review date | KRI | No exception past review date |

### 4. Design the trend presentation

- **Trend beats snapshot.** Show 6-12 periods; a single number without history is uninterpretable. Annotate known causes on the line ("dip = acquisition onboarding").
- One metric per chart; target and threshold drawn as reference lines so breach is visible without explanation.
- Direction convention fixed across the whole report (up = good, or explicitly marked otherwise). Mixed conventions cause misreadings in board settings.
- Use RAG status *derived from the defined thresholds*, never assigned by judgment on the day. If a metric is red, the response defined in step 2 must appear next to it.
- Small populations: show n. "Control pass rate 50%" from 2 tests is noise; say so.
- Resist the single "security score" composite. Aggregation hides the one red that matters — see [../../context/risk-scoring.md](../../context/risk-scoring.md) on aggregation pitfalls.

### 5. Draft the board narrative

Structure (full guidance and anti-patterns: [references/board-reporting.md](references/board-reporting.md); template: [../../templates/grc-board-report.md](../../templates/grc-board-report.md)):

1. **Posture** (1 slide/half-page): overall risk position against appetite in plain language; top 3-5 risks with direction arrows. No technology tour.
2. **Movement**: what changed since last report — risks up/down and why, incidents above threshold and lessons, program milestones hit/missed, metric threshold breaches and responses underway.
3. **External context**: threat and regulatory changes that alter the organization's position (feed from [../regulatory-horizon-scanning/SKILL.md](../regulatory-horizon-scanning/SKILL.md)) — only items with a stated "so what" for this organization.
4. **Asks and decisions**: what you need — budget, risk acceptance sign-off, policy approval, priority trade-off. Every board report should either make an ask or state explicitly that no decision is required. A report with no ask and no decision teaches the board to skim.
5. **Appendix**: full metric table with definitions, for the director who digs.

Write for a financially literate non-specialist: express impact in business terms (downtime, records, money, regulatory exposure), define any unavoidable acronym once, and never let the deck exceed the slot (10 minutes ≈ 5-7 slides).

### 6. Operate and prune

- Review the metric set every 6-12 months: retire metrics that stopped driving decisions or sit permanently green at target (declare victory, move to spot-check), replace them with metrics for the current program frontier.
- When a metric is gamed (SLA met by reclassifying severities; attestation rate via auto-acknowledge), fix the incentive, add the counter-metric from the definition record, and disclose the correction rather than silently restating history.
- Version metric definitions; a formula change breaks the trend line and must be annotated.

## Output format

Two deliverables:

**A. Metric definition sheet** — one record per metric using the step-2 table. Worked example:

```
Metric: Mean time to revoke access (MTTR-A)
Formula: mean and p95 of (last access-revocation completion timestamp −
  termination effective timestamp) in hours, all workforce terminations in period.
  Population: all systems in Tier 1 app inventory + IdP. Excludes: contractor
  conversions (no gap in employment).
Source: IdP audit log joined to HR termination feed; automated weekly extract.
Cadence: measured continuously, reported monthly.
Target: mean <24h. Thresholds: amber ≥24h → IAM lead root-causes within 2 weeks;
  red ≥72h or any single case >7 days → escalate to CISO, item in next exec report.
Owner: Head of IAM (accountable); GRC analyst (produces).
Gaming risk: revoking only IdP/SSO while local accounts persist → counter-metric:
  quarterly recertification residual-access find rate.
```

**B. Board report draft** — following the step-5 structure, populated with current numbers, trends, and explicit asks. Example ask phrasing: "We request approval to accept residual risk R-014 (legacy plant network segmentation, high) until Q2 FY27 remediation completes, per the attached exception; alternative is a $1.4M accelerated project."

## Quality checklist

- [ ] Every metric has a completed "if threshold, then who does what" statement — no orphan numbers.
- [ ] Every formula has explicit numerator, denominator, population, exclusions, and clock definitions; reproducible by a second analyst.
- [ ] No raw counts without denominators in the executive view; no composite "security score".
- [ ] Each metric names an accountable owner distinct from the data producer.
- [ ] Gaming risk and counter-metric documented for each metric.
- [ ] Trends span ≥6 periods where history exists; n shown for small populations; RAG derived from thresholds, not judgment.
- [ ] Board narrative leads with posture vs. appetite, states movement with causes, and contains an explicit ask or "no decision required".
- [ ] Impact expressed in business terms; deck fits the allotted slot.
- [ ] Metric set reviewed within the last 12 months; retired metrics documented.

## References

- [references/metric-catalog.md](references/metric-catalog.md) — extended 25+ metric catalog with formulas, sources, cadence, targets, gaming risks
- [references/board-reporting.md](references/board-reporting.md) — board report structure and anti-patterns
- [../../templates/grc-board-report.md](../../templates/grc-board-report.md) — board report template
- [../../context/risk-scoring.md](../../context/risk-scoring.md) — aggregation pitfalls, matrix caveats
- [../../context/regulations/sec-cyber-disclosure.md](../../context/regulations/sec-cyber-disclosure.md) — board oversight disclosure context
- [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md) — source of risk register data
- [../control-testing/SKILL.md](../control-testing/SKILL.md) — source of control pass-rate data
- [../third-party-risk-assessment/SKILL.md](../third-party-risk-assessment/SKILL.md) — source of vendor metrics
- [../exception-management/SKILL.md](../exception-management/SKILL.md) — source of exception-load metrics

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
