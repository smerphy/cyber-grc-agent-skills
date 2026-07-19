# Workflow: Annual Risk Assessment

```yaml
name: annual-risk-assessment
description: >-
  Annual refresh of the enterprise cyber risk assessment: update context and
  asset understanding, run scenario workshops, analyze and score risks, update
  the register, plan treatments, sweep open exceptions, and report to governance
  bodies against risk appetite.
skills_used:
  - risk-assessment
  - exception-management
  - grc-metrics-reporting
typical_duration: 6-10 weeks elapsed, anchored to the annual governance calendar
roles:
  - risk-manager
  - grc-analyst
  - compliance-officer
```

## Trigger

- The annual risk assessment date on the governance calendar (commonly aligned to budget planning or an ISO 27001 management review).
- A material change forcing an off-cycle run: major acquisition, new business line, significant incident, or a large shift in the threat landscape. An off-cycle run may scope down to affected areas only.

## Prerequisites

- Last year's risk register, risk assessment report, and treatment plan status.
- Current risk appetite statement and scoring methodology (see [risk scoring](../context/risk-scoring.md)); if none exists, establish the methodology first via [risk-assessment](../skills/risk-assessment/SKILL.md) before workshops begin.
- Asset, system, and data inventories at whatever maturity exists; incident history for the period; recent audit, penetration test, and [control testing](../skills/control-testing/SKILL.md) results.
- Executive sponsorship and workshop time committed by business and technology leaders — book calendars before starting step 1.

## Steps

### 1. Context refresh — risk-manager

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (context establishment step)
- **Inputs:** prior-year register; org changes (M&A, new products, new geographies, restructures); threat intelligence summaries; regulatory changes from [horizon scanning](../skills/regulatory-horizon-scanning/SKILL.md).
- **Actions:** document what changed since last year in business context, technology estate, threat landscape, and obligations. Refresh the crown-jewels list. Confirm the scoring methodology and appetite statement are still endorsed by leadership — do not change scales mid-cycle without recalibrating prior scores.
- **Outputs:** context memo (2-4 pages); confirmed methodology; workshop scope list.

### 2. Scenario workshop preparation — grc-analyst

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (scenario development step)
- **Inputs:** context memo; prior-year risks; incident history; industry loss events.
- **Actions:** draft candidate risk scenarios per workshop (8-15 each is workable), pre-populated with last year's scores and any evidence gathered since. Write scenarios as event chains (threat actor + method + asset + consequence), not control-failure statements. Prepare a facilitation pack: scales, appetite thresholds, prior scores, and prompts for what is missing.
- **Outputs:** per-workshop scenario packs; workshop schedule with named attendees.

### 3. Risk identification and analysis workshops — risk-manager (facilitates), business/technology owners (assess)

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md)
- **Inputs:** scenario packs.
- **Actions:** run workshops per business unit or domain. For each scenario: confirm relevance, assess inherent likelihood and impact, identify existing controls and their observed effectiveness (use control testing results, not owner optimism), assess residual risk. Capture new risks the pack missed. Record disagreements and their resolution, not just final scores.
- **Outputs:** raw scored scenarios with rationale; new-risk candidates; controls-effectiveness observations.
- **Decision gate:** a workshop's output is accepted only when every scenario has documented likelihood/impact rationale. Scores without rationale go back to the owner.

### 4. Register consolidation and calibration — risk-manager

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (analysis and aggregation)
- **Inputs:** all workshop outputs; prior register.
- **Actions:** deduplicate and merge scenarios across workshops. Calibrate scores across workshops (different groups anchor differently — normalize against reference scenarios). Update the register: carry forward, re-score, close, or add each entry with a change reason. Beware aggregation pitfalls described in [risk scoring](../context/risk-scoring.md) — do not average ordinal scores.
- **Outputs:** updated risk register with year-over-year movement flagged; top-risk shortlist (typically 10-20 above appetite).

### 5. Treatment planning — risk-manager with risk owners

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (treatment step)
- **Inputs:** top-risk shortlist; appetite thresholds; budget envelope.
- **Actions:** for each above-appetite risk, select treat / transfer / avoid / accept with the risk owner. Treatments get an owner, cost estimate, target date, and expected residual score. Acceptances above appetite require sign-off at the level the appetite statement mandates and are recorded via [exception-management](../skills/exception-management/SKILL.md).
- **Outputs:** treatment plan; formally recorded acceptances.
- **Decision gate:** no above-appetite risk may be left with neither a treatment nor a signed acceptance.

### 6. Exceptions sweep — grc-analyst

- **Skill:** [exception-management](../skills/exception-management/SKILL.md)
- **Inputs:** exception register; updated risk register.
- **Actions:** reconcile all open policy/control exceptions against the refreshed risks: expire what is stale, re-approve what is still justified at current scores, and escalate exceptions whose underlying risk has grown. Link every exception to a register entry — unlinked exceptions are hidden risk acceptances.
- **Outputs:** cleaned exception register; escalation list for step 7.

### 7. Reporting — risk-manager, presented with compliance-officer

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md)
- **Inputs:** register, treatment plan, exception sweep results, year-over-year movement.
- **Actions:** produce the annual risk report for the risk committee/board: top risks vs appetite, movement since last year and why, treatment plan with cost, acceptances made and by whom, and asks (funding, decisions). Keep the board view to risk-and-decision language, not control minutiae. File the full pack as the audit-ready record.
- **Outputs:** board/committee risk report; approved treatment plan; minuted decisions.

## Outputs summary

| Output | Produced in | Consumed by |
|--------|-------------|-------------|
| Context memo + confirmed methodology | Step 1 | Workshops; audit evidence |
| Scenario packs | Step 2 | Step 3 |
| Scored scenarios with rationale | Step 3 | Step 4 |
| Updated risk register | Step 4 | Treatment, reporting, [audit preparation](../skills/audit-preparation/SKILL.md) |
| Treatment plan + acceptances | Step 5 | Budget cycle; quarterly tracking |
| Reconciled exception register | Step 6 | Ongoing exception management |
| Annual risk report | Step 7 | Board; ISO 27001 management review |

## Failure modes

- **Register archaeology.** Rolling last year's register forward with cosmetic re-scores instead of genuinely re-examining scenarios. The year-over-year "why did this move" question in step 7 exposes this — if nothing moved, the assessment probably did not happen.
- **Control-owner optimism.** Scoring residual risk on claimed control effectiveness rather than tested effectiveness. Feed [control testing](../skills/control-testing/SKILL.md) results into step 3 deliberately.
- **Scale drift.** Changing the scoring scale or appetite mid-cycle, making trend reporting meaningless. Lock methodology in step 1.
- **Workshop capture.** One loud voice sets every score. Facilitator collects independent scores before group discussion, then reconciles.
- **Treatment plans that are wish lists.** Unfunded, unowned treatments. The step 5 gate requires owner + cost + date; the budget conversation happens in step 7, not never.
- **Exception blind spot.** Skipping step 6, leaving years-old exceptions silently accepting risks the register says are being treated.
- **Calendar collision.** Running the assessment after budget season closes, so treatments wait a full year for funding. Anchor the schedule so step 7 lands before budget decisions.
