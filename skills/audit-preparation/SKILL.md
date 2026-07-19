---
name: audit-preparation
description: >-
  Prepares an organization for internal or external audits: SOC 2, ISO 27001
  certification/surveillance, customer security audits, and regulator exams.
  Builds a control-mapped evidence request (PBC) list, runs evidence quality
  review, pre-tests weak controls, and briefs control owners for interviews.
  Use when a user says "audit is coming", "PBC list", "evidence request",
  "auditor fieldwork", "get ready for our SOC 2 / ISO audit", or "regulator exam prep".
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Turn an upcoming audit from a scramble into a managed project. This skill produces a scoped, control-mapped evidence request (PBC — "Prepared By Client") list, applies audit-grade quality standards to every evidence item before the auditor sees it, surfaces weak controls early enough to remediate or pre-disclose, and prepares control owners to give accurate, bounded answers in interviews.

## When to use

- An external audit is scheduled: SOC 2 Type I/II, ISO 27001 Stage 1/Stage 2 or surveillance, PCI DSS assessment, customer right-to-audit, or a regulator examination.
- An internal audit function has issued an engagement notice and the team must respond.
- The user asks to build or review a PBC/evidence list, run a "mock audit", or check whether evidence is "audit-ready".
- **Do NOT use** for:
  - Assessing overall readiness against a framework before an audit is even booked — use [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md), or the program-level [../soc2-readiness/SKILL.md](../soc2-readiness/SKILL.md) / [../iso27001-readiness/SKILL.md](../iso27001-readiness/SKILL.md).
  - Designing and executing formal tests of controls yourself — use [../control-testing/SKILL.md](../control-testing/SKILL.md). This skill *prepares* for someone else's testing; that skill *performs* testing.
  - Responding to audit findings after fieldwork — track those through [../exception-management/SKILL.md](../exception-management/SKILL.md).

## Inputs to gather

Ask for these before starting; do not guess:

1. **Audit type and criteria** — SOC 2 (which Trust Services Categories?), ISO 27001 (initial, surveillance, recertification?), customer audit (get their questionnaire/contract clause), regulator exam (which regulator, which rule?).
2. **Audit period** — Type II review period or ISO certification cycle dates. Evidence must cover this window, not "now".
3. **Scope** — in-scope systems, locations, business units, and the system description or Statement of Applicability if one exists.
4. **Control set** — the control matrix, SoA, or policy framework the audit will test against. If none exists, that is a readiness gap; route to the relevant readiness skill first.
5. **Auditor's request list**, if already received — otherwise this skill drafts one proactively.
6. **Timeline** — fieldwork dates, evidence due dates, interview windows.
7. **Known problem areas** — prior findings, open exceptions, controls the team already doubts.

## Procedure

1. **Confirm scope and criteria.** Restate in writing: audit type, criteria version, period, in-scope systems/entities, and exclusions. Get the audit sponsor to confirm. Scope drift mid-audit is the most expensive failure mode — an auditor testing a system the team thought was out of scope generates findings nobody prepared for.

2. **Build the evidence request (PBC) list mapped to controls.** For every in-scope control, list the evidence that demonstrates it operated during the period. Use the template at [../../templates/audit-evidence-request-list.md](../../templates/audit-evidence-request-list.md). Each row needs: request ID, control reference, evidence description, period covered, source system, owner, due date, status. Decision point:
   - If the auditor sent their own list, map each of their requests to your controls and owners — do not restructure their numbering; auditors track by their IDs.
   - If not, draft the list from the control matrix and typical requests for the audit type, and share it with the auditor for confirmation.
   Distinguish **one-time evidence** (policies, org charts, network diagrams, risk assessment) from **period evidence** (tickets, access reviews, logs) — period evidence is where deadlines slip.

3. **Run evidence quality review on every item before submission.** Apply the standards in [references/evidence-standards.md](references/evidence-standards.md). The five checks, in order:
   - **Completeness** — does the item answer the request fully, for all in-scope systems? A request for "access reviews" covering only the primary app when three are in scope will bounce.
   - **Period coverage** — evidence must be dated within (or demonstrably cover) the audit period. A policy approved after period end does not evidence the period. For recurring controls, verify every expected occurrence exists (12 monthly reviews for a 12-month period, not 9).
   - **System-generated vs. manual** — prefer system-generated exports (with visible query parameters and generation date) over manually assembled spreadsheets. Manually curated evidence invites completeness challenges; expect the auditor to ask "how do I know this list is complete?" and prepare the answer.
   - **Screenshots** — must show timestamp, URL/hostname or system identifier, and the logged-in context. A cropped screenshot with no date is rejectable on sight.
   - **Population-then-sample integrity** — where the auditor will sample, submit the *full population* first (with the extraction query and record count), and let sampling happen from that. Never pre-select "sample" items yourself: hand-picked samples are a scoping violation the auditor must reject, and it damages credibility.
   Reject-and-recollect internally now; every item the auditor bounces during fieldwork costs a request cycle and signals weak control operation.

4. **Pre-audit readiness testing of weak controls.** Take the known problem areas from inputs plus anything flagged in step 3 (missing occurrences, manual workarounds) and run targeted tests using [../control-testing/SKILL.md](../control-testing/SKILL.md) at reduced sample sizes. Decision point per weak control:
   - **Remediable before fieldwork** — fix it, and document the fix date honestly; a control remediated mid-period is a partial-period exception in a Type II, not a clean pass.
   - **Not remediable in time** — prepare a pre-disclosure: what failed, period affected, compensating controls, remediation plan. Volunteering a known deficiency with a plan reads far better than the auditor discovering it. Log it via [../exception-management/SKILL.md](../exception-management/SKILL.md).

5. **Brief control owners on interview conduct.** Run a 30-minute prep per interviewee using [references/interview-prep.md](references/interview-prep.md). Core rules: answer only what is asked; describe what you actually do, not what the policy says; "I don't know, I'll follow up" beats guessing; never speculate about other teams' controls; know your own evidence before the interview. Run a mock interview for first-time interviewees and for any control with a pre-disclosed issue.

6. **Track requests to closure.** Maintain the PBC list as a live tracker through fieldwork: statuses (not started / in progress / submitted / auditor follow-up / accepted), owner, and age. Escalate any item unanswered 3+ business days before its due date. During fieldwork, log every auditor follow-up as a new tracked row — follow-ups that fall through become findings. After fieldwork, capture the preliminary findings list and hand off to [../exception-management/SKILL.md](../exception-management/SKILL.md) and, for recurring themes, feed [../grc-metrics-reporting/SKILL.md](../grc-metrics-reporting/SKILL.md).

## Output format

Primary deliverable: a populated PBC tracker per [../../templates/audit-evidence-request-list.md](../../templates/audit-evidence-request-list.md), plus a one-page readiness summary.

PBC tracker row example:

| Req ID | Control | Evidence requested | Period | Source | Owner | Due | Status | QA result |
|---|---|---|---|---|---|---|---|---|
| PBC-014 | AC-02: Quarterly user access review | All 4 quarterly access review records for prod ERP + AWS, incl. reviewer sign-off and remediation tickets | 2025-07-01 – 2026-06-30 | ERP admin console; Jira | J. Alvarez | 2026-08-04 | Submitted | FAIL — Q3 review missing for AWS; recollect or pre-disclose |

Readiness summary structure:

```
1. Scope confirmation (criteria, period, systems — confirmed by <sponsor>, <date>)
2. PBC status: <n> requests | <n> accepted | <n> in QA rework | <n> at risk
3. Weak controls pre-tested: <list with result: remediated / pre-disclose>
4. Pre-disclosures prepared: <list>
5. Interviews scheduled and prepped: <n>/<n>; mock interviews done for: <list>
6. Top 3 risks going into fieldwork, with owner and action
```

## Quality checklist

- [ ] Scope, criteria version, and audit period confirmed in writing by the audit sponsor.
- [ ] Every in-scope control has at least one PBC row; every PBC row maps to a control ID and a named owner with a due date.
- [ ] Every submitted evidence item passed all five quality checks (completeness, period coverage, generation method, screenshot standards, population integrity) — QA result recorded per item.
- [ ] Recurring-control evidence counted against expected occurrences; gaps either recollected or pre-disclosed, never left silent.
- [ ] No auditor sample was pre-selected by the client; populations were provided with extraction query and record count.
- [ ] Every weak control has a decision: remediated (with date) or pre-disclosure drafted.
- [ ] Every interviewee briefed; mock interview held for first-timers and owners of pre-disclosed controls.
- [ ] Tracker has zero unowned or undated open items; all auditor follow-ups logged as rows.

## References

- [references/evidence-standards.md](references/evidence-standards.md) — audit-grade evidence standards per evidence type; common rejection reasons.
- [references/interview-prep.md](references/interview-prep.md) — control-owner interview guidance and what auditors probe for.
- [../../templates/audit-evidence-request-list.md](../../templates/audit-evidence-request-list.md) — PBC tracker template.
- [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md) — SOC 2 TSC, Type I vs. Type II.
- [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md) — ISO/IEC 27001:2022 and Annex A.
- [../../context/frameworks/pci-dss-4.md](../../context/frameworks/pci-dss-4.md) — PCI DSS v4.0.1 assessment context.
- [../control-testing/SKILL.md](../control-testing/SKILL.md) — pre-audit readiness testing.
- [../soc2-readiness/SKILL.md](../soc2-readiness/SKILL.md) / [../iso27001-readiness/SKILL.md](../iso27001-readiness/SKILL.md) — program readiness before an audit is booked.
- [../exception-management/SKILL.md](../exception-management/SKILL.md) — pre-disclosures and post-audit findings.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
