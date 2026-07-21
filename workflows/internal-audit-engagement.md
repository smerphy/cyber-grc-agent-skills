# Workflow: Internal Audit Engagement

```yaml
name: internal-audit-engagement
description: >-
  A single internal audit engagement end to end: risk-based planning and
  scoping, announcement and evidence request, fieldwork testing design and
  operating effectiveness, finding development with management response,
  formal reporting, and follow-up verification — with auditor independence
  preserved at every step.
skills_used:
  - audit-preparation
  - control-testing
  - risk-assessment
  - grc-metrics-reporting
typical_duration: 6-10 weeks from planning to final report; follow-up runs until findings close
roles:
  - internal-auditor
  - grc-analyst
```

## Trigger

- The engagement comes up in the approved risk-based internal audit plan.
- The audit committee or executive sponsor requests an unscheduled engagement (post-incident, pre-transaction, whistleblower-driven) — same workflow, compressed planning.
- A prior engagement's follow-up found remediation stalled badly enough to warrant a re-audit.

## Prerequisites

- An approved audit plan or charter granting the engagement authority, access rights, and reporting line (functionally to the audit committee, not to the management being audited).
- The current risk register and any prior audit reports covering the area.
- An independence check completed: no assigned auditor designed, implemented, or operates the controls in scope, and none has within the last 12 months. Staff a substitute or narrow the scope before starting — not after fieldwork.
- A workpaper repository the audit function controls (auditees get read access to nothing in it).

## Steps

### 1. Engagement planning — internal-auditor

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (context and scoping); [control-testing](../skills/control-testing/SKILL.md) for feasibility
- **Inputs:** audit plan entry, risk register, prior reports and open findings, org charts and system inventory for the area.
- **Actions:** define the engagement objective as a question the report will answer ("are access controls over the ERP designed and operating effectively?"), not a topic. Select criteria explicitly — internal policy, a framework, a regulation — and cite the version. Scope by risk: use register scores and prior findings to decide which processes, systems, and locations are in and which are documented as out. Budget hours per phase; confirm the testing approach is feasible (populations extractable, owners available).
- **Outputs:** engagement plan: objective, scope, criteria, approach, team, timeline.
- **Decision gate:** the audit lead approves the plan. If management pressure has already narrowed scope away from the risk, escalate to the audit committee before fieldwork — scope negotiated under pressure is the engagement's first finding.

### 2. Announcement and evidence request — internal-auditor issues; grc-analyst coordinates the auditee side

- **Skill:** [audit-preparation](../skills/audit-preparation/SKILL.md) (used from the auditor's side: the PBC list you issue is the one that skill teaches auditees to answer)
- **Inputs:** engagement plan; control documentation for the area.
- **Actions:** send the announcement memo (objective, scope, criteria, timeline, contacts) to the auditee executive. Issue a control-mapped evidence request list per [audit-evidence-request-list](../templates/audit-evidence-request-list.md) with request IDs, owners, and due dates; distinguish one-time from period evidence. Schedule walkthroughs and interviews. The auditee's coordinator (typically a grc-analyst) tracks delivery — but the auditor, not the auditee, judges evidence sufficiency.
- **Outputs:** announcement memo; issued PBC list; interview schedule.

### 3. Fieldwork: design effectiveness — internal-auditor

- **Skill:** [control-testing](../skills/control-testing/SKILL.md) (steps 1-3: restate, classify, walkthrough)
- **Inputs:** control descriptions, delivered evidence, walkthrough access to performers.
- **Actions:** restate each in-scope control as a testable assertion and walk one instance end-to-end with the performer, not the manager. Assess precision, timeliness, performer independence, and coverage against the stated risk. Classify each control (automated / manual / IT-dependent manual) to set the operating test approach.
- **Outputs:** design conclusions per control, documented in workpapers.
- **Decision gate:** a control with a design deficiency is not tested for operating effectiveness — write the finding now and move on. Operating a badly designed control consistently is not effectiveness.

### 4. Fieldwork: operating effectiveness — internal-auditor

- **Skill:** [control-testing](../skills/control-testing/SKILL.md) (sampling, population completeness, execution)
- **Inputs:** design-effective controls; population sources.
- **Actions:** pull populations system-generated with query, date, and count; validate completeness against an independent source before sampling. Sample per the frequency baselines, spread across the period, never letting the owner pick items. Test defined attributes per item and document in workpapers per [control-test-workpaper](../templates/control-test-workpaper.md) to the re-performance standard. Classify every exception honestly: isolated deviation (expand the sample) or deficiency. Communicate potential findings to owners as facts emerge — no surprises at the exit meeting.
- **Outputs:** completed, reviewed workpapers; validated exception list.

### 5. Finding development and management response — internal-auditor drafts; auditee management responds

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (rating findings on the org's matrix)
- **Inputs:** design deficiencies (step 3), operating exceptions (step 4).
- **Actions:** write each finding in the condition / criteria / cause / consequence structure: what is (condition), what should be per the cited criteria, why it happened (root cause, not "human error"), and what it exposes — rated on the organization's risk matrix with rationale. Confirm the condition's facts with the owner before drafting. Then negotiate the management response: agree facts, hear disputes on facts with evidence, but do not trade away ratings or delete findings to buy agreement — a disputed rating goes to the report with both positions. Every response needs an accountable owner and a committed date proportionate to the rating.
- **Outputs:** validated findings with ratings; management responses with owners and dates.
- **Decision gate:** management may accept a finding's risk instead of remediating — that acceptance is documented in the report and routed to the risk register, at the authority level the rating requires. Silence is not acceptance.

### 6. Reporting — internal-auditor; report to sponsor and audit committee

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md) (audience-calibrated narrative)
- **Inputs:** findings, responses, workpaper conclusions.
- **Actions:** hold the exit meeting on the draft — facts only, no new findings the auditee has not seen. Issue the report: objective, scope, overall conclusion (answer the step-1 question), findings with ratings and responses. Format in the assurance style per [assurance-formal](../branding/styles/assurance-formal.md) — measured, evidence-bound language; no adjectives the workpapers cannot carry. Issue within days of the exit meeting, not months: a stale report audits history.
- **Outputs:** final report distributed to auditee executive, sponsor, and audit committee; findings loaded into the findings register (see [finding-remediation](finding-remediation.md)).

### 7. Follow-up and closure verification — internal-auditor

- **Skill:** [control-testing](../skills/control-testing/SKILL.md) (remediation validation); [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md) (aging reporting)
- **Inputs:** findings register; management's remediation evidence.
- **Actions:** at each committed date, verify closure with evidence — inspect artifacts and, for higher-rated findings, retest with samples drawn from the post-remediation period only. An owner's assertion closes nothing. Report finding aging and overdue items to the audit committee each cycle; escalate items overdue past threshold. Feed engagement results into next year's audit plan risk assessment.
- **Outputs:** closure verifications in workpapers; aging report; engagement closed.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Engagement plan | 1 | Audit workpaper repository |
| Announcement memo + PBC list | 2 | Audit workpaper repository |
| Design and operating workpapers | 3-4 | Audit workpaper repository |
| Findings + management responses | 5 | Findings register |
| Final report | 6 | Audit committee records |
| Closure verifications + aging report | 7 | Findings register |

## Failure modes

- **Independence erosion.** The auditor advises on remediation design, then audits the result next year — auditing their own work. Advise on criteria, never on solutions; log any consulting-type help and rotate staffing.
- **Scope negotiated under pressure.** Management steers scope away from the sore spot during planning. The risk register, not management comfort, drives scope; escalate attempts to the audit committee.
- **Finding by anecdote.** One bad ticket becomes a rated finding without population or sample. Every operating-effectiveness finding must trace to a workpaper a reviewer could re-perform.
- **Rating horse-trading.** Findings downgraded at the exit meeting to get a signature. Facts are negotiable when evidence says so; ratings follow the matrix. Report disputes with both positions.
- **The stale report.** Fieldwork ends in March, the report lands in July, and half the findings are already moot or worse. Draft findings during fieldwork; issue within days of exit.
- **Closure by assertion.** "Done" emails close findings without evidence, and the next engagement finds the same condition. Step 7 requires artifacts, and retests the ones that matter.
- **Follow-up as a suggestion.** Overdue findings age silently because nobody reports them upward. The aging report to the audit committee is what makes committed dates real.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
