# Workflow: Quarterly Board Reporting Cycle

```yaml
name: board-reporting-cycle
description: >-
  Standing quarterly cycle producing the board/risk-committee security report:
  metric collection with quality checks, risk register refresh for movement,
  regulatory horizon items with a stated "so what", narrative drafting to the
  board template, pre-wire review, delivery, and minuted actions tracked forward.
skills_used:
  - grc-metrics-reporting
  - risk-assessment
  - regulatory-horizon-scanning
typical_duration: 3-4 weeks elapsed per quarter, working back from the committee date
roles:
  - grc-analyst
  - risk-manager
  - compliance-officer
```

## Trigger

- The standing quarterly board or risk-committee date — schedule backward from it: pre-wire a week out, draft two weeks out, data cut three weeks out.
- An off-cycle demand: a material incident, a regulator interaction, or a director request. Off-cycle reports reuse steps 4-6 on whatever data is current, clearly dated.

## Prerequisites

- A defined metric set with formulas, owners, and thresholds (build it first via [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md) if it does not exist — this workflow runs the cycle, it does not design the program).
- Prior quarter's report and the minuted decisions/actions from it.
- Current risk register and appetite statement; a maintained horizon register from [regulatory-horizon-scanning](../skills/regulatory-horizon-scanning/SKILL.md).
- The [board report template](../templates/grc-board-report.md) and the committee's slot length and page limits.

## Steps

### 1. Data collection and metric computation — grc-analyst

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md) (metric definitions and trend presentation)
- **Inputs:** metric definition sheet; extracts from source systems (vulnerability scanner, identity platform, ticketing, GRC tool, TPRM records, exception register).
- **Actions:** pull each metric per its exact formula — same population, same exclusions, same clock definitions as last quarter, so trends are real. Quality-check before anyone sees a number: reconcile counts against source systems, investigate implausible jumps (a metric that improved 40% usually changed definition, not reality), show n for small populations, and derive RAG strictly from the defined thresholds — never assigned by judgment on the day. Annotate known causes on trend lines. A red metric ships with its defined response, not an apology.
- **Outputs:** computed metric pack with 6-12 period trends and annotations; data-quality notes.
- **Decision gate:** a metric whose source data cannot be reconciled is reported as "not reliable this quarter" with a fix owner — never silently plugged with last quarter's number.

### 2. Risk register refresh for movement — risk-manager with risk owners

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (analyze and evaluate steps)
- **Inputs:** current register; quarter's incidents, [control testing](../skills/control-testing/SKILL.md) results, audit findings, treatment-plan status.
- **Actions:** this is a movement pass, not the annual re-assessment: re-score risks with new evidence, check treatment milestones against dates, and capture new risks the quarter surfaced. For each top risk, write the movement story — up, down, or flat, and why, in one or two sentences. Verify above-appetite risks still have a live treatment or a signed acceptance; a lapsed one is itself a reportable item.
- **Outputs:** refreshed register; top-risks-vs-appetite view with direction arrows and causes.

### 3. Regulatory and horizon items — compliance-officer

- **Skill:** [regulatory-horizon-scanning](../skills/regulatory-horizon-scanning/SKILL.md) (triage and briefing steps)
- **Inputs:** horizon register; quarter's regulatory developments and any regulator correspondence.
- **Actions:** select only items with a stated "so what" for this organization — a rule change with no applicability or no delta is noise, not board material. For each item carried forward: what changed, what it demands of us, the deadline band (act now / plan / watch), and what we are doing. Verify dates and status against primary sources before they go in front of directors; hedge anything not yet fixed in final text.
- **Outputs:** external-context section input: 2-5 items, each with organizational impact and response status.

### 4. Narrative drafting — grc-analyst drafts; risk-manager owns content

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md) (board narrative step)
- **Inputs:** metric pack, risk movement view, horizon items, prior quarter's minuted actions.
- **Actions:** draft into the [board report template](../templates/grc-board-report.md), formatted per the [brand profile](../branding/brand-profile.md): posture vs appetite in plain language, movement with causes, external context, then asks. Every report either makes an explicit ask (budget, acceptance sign-off, priority trade-off) or states "no decision required" — a report with neither teaches the board to skim. Report status on every action minuted last quarter; dropped threads destroy credibility faster than bad news. Business language throughout (downtime, records, money, regulatory exposure); size the deck to the slot — 10 minutes is 5-7 slides, and the full metric table goes in the appendix.
- **Outputs:** draft report and appendix.

### 5. Pre-wire review — risk-manager with the CISO, then the committee chair

- **Inputs:** draft report.
- **Actions:** the CISO reviews for accuracy and message discipline; contested numbers get resolved against the step 1 data-quality notes, not softened. Then pre-wire the committee chair (and any director likely to lead questioning) a week out: walk the asks, surface surprises early — a board meeting is the wrong place for the chair to first see a red. Pre-wiring shapes delivery; it never changes the data. If a fact must change, it changes because it was wrong, with the correction noted.
- **Outputs:** final report, distributed per board-pack deadline (typically 5 business days ahead).
- **Decision gate:** the CISO signs off before distribution. An unresolved factual dispute holds that item out of the report, flagged as under review — it does not ship both versions.

### 6. Delivery and minuted decisions — risk-manager presents (or supports the CISO)

- **Inputs:** final report; committee agenda slot.
- **Actions:** present posture, movement, and asks — not a slide-by-slide read. Drive each ask to an outcome: approved, declined, or deferred with a date. Capture questions asked (they signal next quarter's concerns) and confirm decisions land in the minutes with owners — an unminuted decision did not happen, and directors' oversight records increasingly matter for disclosure obligations (verify specifics against the applicable regime's official text).
- **Outputs:** minuted decisions and actions; question log.

### 7. Action tracking to next cycle — grc-analyst

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md) (operate and prune step)
- **Inputs:** minutes; question log; cycle retrospective notes.
- **Actions:** log every minuted action with owner and due date; these are the opening status items of the next report. Feed the question log into next quarter's drafting. Once a year, prune the metric set: retire metrics that no longer drive decisions or sit permanently green, and annotate any formula change so the trend break is explained, not hidden.
- **Outputs:** action tracker seeded for next quarter; metric-set change log.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Computed metric pack + quality notes | 1 | GRC tool / metrics repository |
| Refreshed register + movement view | 2 | Risk register |
| Horizon items with "so what" | 3 | Horizon register |
| Draft report | 4 | Board reporting folder (versioned) |
| Final distributed report | 5 | Board portal (audit evidence) |
| Minuted decisions and actions | 6 | Committee minutes; action tracker |
| Seeded action tracker | 7 | Action tracker |

## Failure modes

- **The heroic quarterly scramble.** No standing calendar, so every quarter is a two-week fire drill and quality checks get skipped. Work backward from the committee date with fixed cut-off, draft, and pre-wire dates.
- **Judgment RAG.** Statuses assigned by feel on the day, so amber means "the CISO is worried" one quarter and "threshold breached" the next. RAG derives from defined thresholds or it means nothing.
- **The 40-metric tour.** Reporting everything measurable instead of the 8-12 metrics wired to decisions. Directors remember one number from a wall of forty, and it is rarely the right one.
- **No ask, ever.** Quarters of "all under control" until the year budget is refused for lack of groundwork. Every report makes an ask or explicitly states no decision is required.
- **Dropped actions.** Last quarter's minuted commitments never reported back. Step 7 exists so the next report opens with their status — boards forgive bad news, not amnesia.
- **Pre-wire drift.** "Softening" numbers after executive review until the report says nothing. Pre-wiring shapes framing and surfaces surprises; the data is the data.
- **Horizon noise.** Pasting a law-firm newsletter into the external section. If an item has no stated "so what" for this organization, it does not go to the board.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
