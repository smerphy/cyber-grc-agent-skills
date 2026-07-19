# Audit Evidence Standards

What makes a piece of evidence audit-grade, by evidence type, plus the rejection reasons auditors cite most often. Apply these standards during internal QA (Procedure step 3 of the audit-preparation skill) so items never bounce during fieldwork.

## Universal requirements (every evidence type)

Every evidence item must let a skeptical third party answer four questions without asking you anything:

1. **What is this?** — labeled with the system, control, and request ID it supports.
2. **When was it created / what period does it cover?** — visible date or timestamp on the artifact itself, not just in the filename.
3. **Where did it come from?** — source system identifiable on the artifact (URL, hostname, console banner, report header, query text).
4. **Is it complete?** — record counts, page X-of-Y, "no results filtered" — something that shows nothing was omitted.

An item failing any of these is not evidence; it is a claim.

### The evidence hierarchy

Auditors weight evidence by how hard it is to fabricate or curate:

| Strength | Type | Example |
|---|---|---|
| Strongest | Auditor-observed / auditor-extracted | Auditor watches you run the query; screen-share of live config |
| Strong | System-generated, parameters visible | Export with query string, run date, and row count in the header |
| Moderate | System-generated, parameters not visible | CSV with no indication of the filter used |
| Weak | Manually assembled | Spreadsheet a human compiled "from the system" |
| Weakest | Assertion | Email saying "we do this quarterly" |

Aim for "Strong" on everything sampled. Manually assembled evidence is acceptable only for inherently manual artifacts (meeting minutes, sign-off memos) — and even those need dates and named participants.

## Standards by evidence type

### Configuration evidence (system settings, hardening, security parameters)

- Capture from the authoritative admin interface or via export/API — not from documentation describing the intended config.
- Show: the setting value, the system identifier (hostname/tenant/account ID), and a timestamp.
- For Type II / period audits, configuration screenshots taken today only evidence today. Pair with change history for the setting (audit log, IaC commit history) to demonstrate the config held through the period, or state that the auditor will rely on the change-management control.
- Infrastructure-as-code: the repo file alone is not enough — pair with evidence the code is what's deployed (pipeline run, drift detection output).
- Redact secrets (keys, hashes) before submission, and note the redaction; never redact the setting under test.

### Ticket evidence (change tickets, incident tickets, access requests, vulnerability remediation)

- Provide the ticket **population export first** (all tickets of the type in the period, with query and count), then individual tickets as sampled.
- Each sampled ticket must show, on-screen or in export: ticket ID, opened/closed dates, requester, approver (a *different* named person where segregation is required), the approval action with its timestamp, and links to the work performed.
- Approval must precede the action it authorizes. A change approved after deployment is an exception even if the ticket is "complete".
- Free-text fields saying "approved per Slack" without the Slack artifact will bounce — attach the referenced artifact or get the approval recorded in-system going forward.

### HR records (onboarding, termination, background checks, training)

- Source: the HRIS, not a tracking spreadsheet. Provide the HRIS-generated roster of hires/terminations for the period (population), then per-person records as sampled.
- Termination evidence must connect two systems: HRIS termination date **and** access-removal timestamp in each in-scope system, so the auditor can compute the gap against the control's SLA.
- Training: completion records with employee name, course, completion date, and the assignment population (who was *required* to complete it) — completion lists without the required-population denominator cannot evidence completeness.
- Background checks: evidence of completion and date, not the check contents. Redact personal data beyond name/date/result per privacy obligations.

### Log evidence (security logs, alerts, monitoring)

- Export must show: source system, query/filter used, time range, generation timestamp, and record count.
- For "review of logs/alerts" controls, the log itself is not the evidence — the evidence is the **review**: who looked, when, what was flagged, and what happened to flagged items. A pile of raw logs evidences logging, not reviewing.
- Retention: if the control claims 12-month retention, be able to produce a log from ~12 months ago on request.
- For alert-response controls, provide the alert population from the SIEM/monitoring tool and closed-loop tickets for sampled alerts.

### Approval evidence (policy approvals, access approvals, risk acceptances, exceptions)

- Must show the approver's identity, their authority (role at time of approval), the date, and exactly what was approved (version, scope).
- Policy approvals: the approved version with version number and date; the approval artifact (workflow record, signed minutes, tracked e-sign) tied to that version. "Reviewed annually" requires an approval dated within the period even if nothing changed.
- Verbal or chat approvals: acceptable only if the control is defined that way and the chat artifact is produced with timestamps and identities; treat as weak and migrate to workflow.
- Self-approval where the control requires independent approval is a deficiency, not an evidence-quality issue — flag it as such.

### Screenshots (any type)

Minimum bar, all four required:
1. Full-window capture including the URL bar / console host identifier — not a cropped panel.
2. Visible system date/time (OS clock in frame, or in-app timestamp).
3. The logged-in user context visible where relevant.
4. Filename or annotation tying it to request ID and system.

Prefer exports over screenshots wherever the system supports them. Screenshots of spreadsheets are never acceptable — provide the spreadsheet.

## Common evidence rejections

The recurring reasons auditors bounce evidence, with the fix:

| # | Rejection | Why it fails | Fix |
|---|---|---|---|
| 1 | No date/timestamp on artifact | Cannot tie to audit period | Recapture with visible date; use export headers |
| 2 | Evidence outside the audit period | Doesn't cover the review window | Pull period-dated artifact; for configs add change history |
| 3 | Population completeness not demonstrable | Manual list; no query/count | Re-extract system-generated with parameters shown |
| 4 | Client pre-selected the "sample" | Sampling integrity broken | Provide full population; auditor selects |
| 5 | Missing occurrences of a recurring control | 10 of 12 monthly reviews | Recollect if they exist; otherwise pre-disclose the gap |
| 6 | Cropped screenshot, no system identifier | Unverifiable source | Recapture full window with URL/hostname |
| 7 | Wrong scope — one system of several | Incomplete against request | Cover every in-scope system per request |
| 8 | Approval postdates the action | Control did not operate as designed | Cannot fix retroactively — classify as exception |
| 9 | Policy document as evidence of operation | Design ≠ operation | Provide operational artifacts (tickets, records, logs) |
| 10 | Aggregated/summary data where detail was requested | Cannot re-perform | Provide record-level export |
| 11 | Evidence references another artifact not provided | Chain broken ("per attached" with nothing attached) | Bundle the full chain under one request ID |
| 12 | Over-redaction | Tested attribute redacted away | Redact secrets/personal data only; never the attribute under test |

Items 4, 5, and 8 are not really evidence problems — they are control problems wearing an evidence costume. Route them to the weak-control path (remediate or pre-disclose), not to recollection.

## Internal QA workflow

For each PBC item before submission:

1. Check universal four questions (what/when/where/complete).
2. Check the type-specific standard above.
3. Check against the rejection table.
4. Record QA result on the tracker: PASS / FAIL-recollect / FAIL-control-issue.
5. FAIL-control-issue items go to the weak-control decision (remediate vs. pre-disclose) — never quietly submit and hope.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
