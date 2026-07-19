# Audit Evidence Request List (PBC List)

**How to use:** The "provided by client" list that structures evidence collection for an audit or assessment. Issue it at kickoff, track it weekly, and keep it as the single status source — auditors and control owners work from the same table. Replace the example rows with your audit's actual requests, keeping the level of specificity shown: every request names the **system**, the **period**, and the **format** so the first submission is usable. Preparation strategy, evidence quality criteria, and interview readiness: [../skills/audit-preparation/SKILL.md](../skills/audit-preparation/SKILL.md).

## Conventions

- **Ref:** `PBC-NN`, grouped by domain. Stable once issued — auditors cite these refs in workpapers.
- **Period:** the audit period the evidence must cover. For samples, provide the full population first; the auditor selects — see [control-test-workpaper.md](control-test-workpaper.md) for why population completeness comes before sampling.
- **Format:** system-generated exports beat screenshots; screenshots must show URL/system name and timestamp; include generation parameters (filters, date run) with every export.
- **Status values:** Not started / In progress / Submitted / Accepted / Rejected - resubmit (with reason in Notes).
- Deliver via the agreed secure channel only. Redact credentials and personal data not needed for the test before submission.

## Request list

| Ref | Control | Evidence requested | Period | Format | Owner | Due | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| PBC-01 | User access provisioning | Complete listing of all access requests granted for ERP and AWS production, exported from the ticketing system with ticket ID, requester, approver, grant date | 2025-07-01 to 2026-06-30 | CSV export incl. query parameters | IT Service Desk Lead | 2026-08-01 | Submitted | Auditor will sample 25 for approval evidence |
| PBC-02 | Access termination | HR leaver listing (all terminations with last working day) and corresponding account-disable evidence for the same population | 2025-07-01 to 2026-06-30 | HR CSV + IdM audit log export | HR Ops + IAM Manager | 2026-08-01 | In progress | Two sources deliberately — auditor reconciles HR vs. IdM |
| PBC-03 | Quarterly access review | Completed access review certifications for ERP, AWS prod, and payroll SaaS: review packages, reviewer sign-offs, and revocation tickets for access not reaffirmed | Q3 2025 - Q2 2026 (4 quarters) | Review tool export + tickets | IAM Manager | 2026-08-05 | Not started | Q4 2025 review was late — prepare explanation and remediation evidence |
| PBC-04 | Privileged access | Current listing of all accounts in privileged groups (domain admin, AWS admin roles) with owner mapping and MFA status | As at fieldwork date | System-generated export | IAM Manager | 2026-08-05 | Not started | |
| PBC-05 | Change management | Full population of production changes to ERP (change tickets) with ticket ID, type, approver, implementer, deploy date | 2025-07-01 to 2026-06-30 | Change tool CSV | Change Manager | 2026-08-01 | Submitted | Sample of 25 standard + all 6 emergency changes |
| PBC-06 | Segregation: dev vs. deploy | Listing of personnel with production deployment rights for ERP, reconciled against developer role listing | As at fieldwork date | Two system exports + reconciliation | DevOps Lead | 2026-08-08 | Not started | If overlap exists, provide compensating pipeline-control evidence |
| PBC-07 | Backup execution | Backup job success/failure logs for Tier-1 systems and failure-handling tickets for any failed jobs | 2025-07-01 to 2026-06-30 | Backup console report | Infrastructure Manager | 2026-08-08 | Not started | |
| PBC-08 | Backup restoration testing | Evidence of completed restore tests per the quarterly schedule: test plan, execution record, result, sign-off | Q3 2025 - Q2 2026 | Test records (PDF) | Infrastructure Manager | 2026-08-08 | Not started | |
| PBC-09 | Vendor management | Vendor inventory with tiering; for the 5 critical vendors: latest assessment, SOC 2/ISO evidence review record, and signed contract security clauses/DPA | Current + assessments in period | Register export + assessment records | Vendor Risk Manager | 2026-08-12 | Not started | See [vendor-security-questionnaire.md](vendor-security-questionnaire.md) outputs |
| PBC-10 | Vulnerability management | Monthly vulnerability scan reports for external ranges and SLA compliance report (criticals vs. 14-day SLA), including exception records for any misses | 2025-07-01 to 2026-06-30 | Scanner reports + SLA tracking export | Security Operations Lead | 2026-08-12 | Not started | Link any misses to approved exceptions ([exception-request.md](exception-request.md)) |

## Tracking summary

| Metric | Value |
|---|---|
| Total requests | [N] |
| Accepted / Submitted / In progress / Not started / Rejected | [n / n / n / n / n] |
| Overdue | [n — list refs] |
| Next status call | [Date] |
