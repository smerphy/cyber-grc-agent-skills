# Workflow: Finding Remediation and Closure

```yaml
name: finding-remediation
description: >-
  Universal intake-to-closure pipeline for findings from any source — internal
  and external audits, penetration tests, vendor assessments, incident
  post-mortems, self-assessments: normalize into one register, risk-rate on a
  common scale, assign owners and dates by severity, escalate on aging, govern
  the won't-fix path, and verify closure with evidence.
skills_used:
  - risk-assessment
  - exception-management
  - control-testing
  - grc-metrics-reporting
typical_duration: standing pipeline; intake to rated-and-owned within 10 business days per finding
roles:
  - grc-analyst
  - risk-manager
  - internal-auditor
```

## Trigger

- Any source produces a finding: internal audit report, external audit or certification, penetration test, vendor security assessment, incident post-mortem, regulator feedback, framework self-assessment, or a control failure from the [control assurance cycle](control-assurance-cycle.md).
- Quarterly: register-wide aging and escalation review runs on the calendar regardless of new intake.

## Prerequisites

- A single findings register as system of record (a disciplined spreadsheet qualifies; five source-specific trackers do not).
- The organization's risk matrix and severity-to-SLA table — remediation timeframes per severity, defined in advance, not negotiated per finding (see [risk-scoring](../context/risk-scoring.md)).
- Escalation thresholds agreed with leadership: at what age and severity an overdue finding reaches the risk committee.
- An exception process for the won't-fix path ([exception-management](../skills/exception-management/SKILL.md) operational).

## Steps

### 1. Intake and normalization — grc-analyst

- **Skill:** none specific — register discipline
- **Inputs:** source reports in whatever format they arrive.
- **Actions:** register every finding within 5 business days of report receipt with: unique ID, source and source reference, description, affected assets/controls, date identified, and the source's own severity kept for traceability. Deduplicate against open entries — the pentest's "no MFA on VPN" and the audit's "remote access authentication deficiency" are one finding with two sources, not two findings; link sources to the surviving entry rather than deleting anything. Reject "findings" that are observations without a condition (a raw tool export is input, not a finding).
- **Outputs:** normalized register entries; dedupe links.

### 2. Risk rating — grc-analyst rates; risk-manager confirms high and critical

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (scoring on the org matrix)
- **Inputs:** normalized entries; risk matrix; asset criticality.
- **Actions:** re-rate every finding on the organization's own matrix regardless of source scale — a pentest "critical" on a sandboxed test box and an auditor "moderate" on the payment platform must land where this organization's likelihood and impact anchors put them, with the source rating retained alongside. Record one or two sentences of rationale; unrationalized ratings get re-litigated at every escalation. Findings revealing a risk not on the risk register feed a register entry, cross-referenced.
- **Outputs:** rated findings with rationale; risk register cross-references.
- **Decision gate:** critical-rated findings do not wait for the pipeline — immediate escalation to the risk-manager and affected executive, with interim risk reduction (compensating measure, service restriction) decided within days.

### 3. Ownership and remediation plan — grc-analyst brokers; business owner commits

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (treatment definition)
- **Inputs:** rated findings; severity-to-SLA table.
- **Actions:** assign each finding an accountable owner in the business or team that operates the deficient control — the security team tracking a finding does not own fixing it. The owner commits to a remediation plan naming specific actions (not "improve process") and a date within the severity SLA; a date beyond SLA requires risk-manager approval with reason recorded. Root cause goes on the entry — fixing the instance without the cause manufactures repeat findings.
- **Outputs:** every open finding has owner, plan, root cause, and committed date.
- **Decision gate:** if the owner declines to remediate — cost, feasibility, business conflict — that is not a stalemate to age silently: route to step 5 within the SLA window.

### 4. Tracking, aging, and escalation — grc-analyst runs; risk-manager escalates

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md) (aging thresholds and defined responses)
- **Inputs:** the register; committed dates.
- **Actions:** review the register monthly: status per finding, age against committed date, buckets (<30 / 30-90 / >90 days past due) weighted by severity. Escalate mechanically per the agreed thresholds — e.g., any high past due goes to the risk committee; a second missed date on the same finding escalates one management level — not by whether anyone remembered. Date changes are re-commitments requiring the same approval as an over-SLA date, logged with reason; a silently slipped date is an unmanaged violation, not a plan.
- **Outputs:** monthly aging report; escalation log.

### 5. The won't-fix path — risk-manager routes; approval per authority matrix

- **Skill:** [exception-management](../skills/exception-management/SKILL.md)
- **Inputs:** findings the owner declines or cannot remediate.
- **Actions:** convert to a formal, time-bound risk acceptance: residual risk scored, compensating controls evidenced where the level demands them, approval at the authority the residual risk requires — never the requester, never the analyst. Expiry and review dates are mandatory; at review, re-approval is a full decision, not a rubber stamp. The finding stays in the register as "risk accepted" with the exception ID — it does not vanish. Findings tracing to an external legal or regulatory obligation cannot be internally waived; escalate those to legal.
- **Outputs:** approved exception cross-referenced to the finding; or a declined acceptance, which sends the finding back to step 3 with executive weight behind it.

### 6. Closure verification — internal-auditor or independent tester verifies

- **Skill:** [control-testing](../skills/control-testing/SKILL.md) (remediation validation)
- **Inputs:** findings reported remediated, with the owner's evidence.
- **Actions:** closure by assertion is the classic failure — an owner's "done" closes nothing. Verify proportionate to severity: low findings close on inspected evidence (config export, ticket trail, updated document); medium and above get verification by someone other than the remediator; high and critical are retested with samples drawn from the post-remediation period only. Findings from external sources (auditor, regulator) close internally only with evidence that would satisfy the originating party at their next visit. Failed verification reopens the finding as a repeat, at escalated visibility.
- **Outputs:** closure record with evidence reference and verifier; reopened entries where verification failed.
- **Decision gate:** no finding moves to closed without a named verifier distinct from the owner and an evidence reference. No reference, no closure.

### 7. Metrics and feedback — grc-analyst produces; risk-manager presents

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md)
- **Inputs:** register history.
- **Actions:** report quarterly: open findings by severity and age bucket, SLA attainment, repeat-finding rate, won't-fix volume, and mean time to close by severity — each with threshold and defined response. Watch the gaming vectors: severity downgrades to dodge SLAs and close-reopen churn both get counter-checked. Feed repeat findings and root-cause clusters back into the risk register and the [control assurance cycle](control-assurance-cycle.md) test plan — a control producing findings from three sources is mis-designed, not unlucky.
- **Outputs:** findings metrics pack; inputs to risk register and test planning.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Normalized entries + dedupe links | 1 | Findings register |
| Ratings with rationale | 2 | Findings register / risk register |
| Owner, plan, committed date | 3 | Findings register |
| Aging report + escalation log | 4 | Findings register |
| Risk acceptances | 5 | Exception register |
| Closure records with evidence | 6 | Findings register |
| Metrics pack | 7 | Metrics program |

## Failure modes

- **Register sprawl.** Audit findings in one tracker, pentest findings in another, vendor findings in email. Nobody sees aggregate exposure, and the same weakness lives three lives. One register, all sources — step 1 is non-negotiable.
- **Source-severity worship.** Ratings imported unadjusted, so a scanner "critical" on a dev box outranks an auditor "moderate" on the crown jewels. Step 2 re-rates everything on the organization's matrix.
- **Ownerless findings.** Findings assigned to "IT" or to the security team that found them. No named accountable owner in the operating team means no remediation, just tracking.
- **The quiet slip.** Committed dates moved repeatedly without approval or log until the finding is eighteen months old and nobody remembers why. Date changes are governed re-commitments; aging escalates mechanically.
- **Closure by assertion.** The pipeline's classic failure: "done" emails close findings, and the next audit reopens them all — now as repeat findings with a management-credibility problem attached. Step 6 exists for exactly this.
- **Won't-fix limbo.** Findings neither remediated nor formally accepted, aging forever as "in discussion". The step-3 gate forces the fork: plan with a date, or exception with an approver.
- **Repeat-finding blindness.** Each recurrence handled as new, root cause never addressed. The repeat-finding rate in step 7 is the metric that catches a program treating symptoms.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
