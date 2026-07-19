# Test Procedures Library

Worked test procedures for twelve common security controls. Each entry gives the control as typically stated, its classification, the population and sample approach, the attributes to test per sampled item, the procedure, and the pitfalls that most often invalidate the test. Adapt frequencies and SLAs to the organization's documented control — test against *their* stated control, not this library's example values.

Sample sizes reference the baseline table in [sampling-guide.md](sampling-guide.md).

---

## 1. User access review

**Control (typical):** Quarterly, system owners review all user accounts and permissions in in-scope systems against business need; flagged access is removed within 10 business days.
**Type:** ITDM (human review of system-generated listing). **Frequency:** quarterly → sample 2 reviews, **plus** report-logic test.

**Population:** All review instances in the period (expect 4 per system per year). Completeness: count reviews per in-scope system against expected occurrences.

**Attributes per sampled review:**
- A1: Review performed within the required window, evidenced with reviewer identity and date.
- A2: Input listing was complete — generated from the live system at review time, covering all accounts including service and admin accounts.
- A3: Evidence of actual scrutiny: dispositions recorded per account or per group (not a blanket "all approved" with no exceptions ever).
- A4: Flagged items remediated within SLA, with removal evidence (ticket + system confirmation).
- A5: Reviewer had authority and was not reviewing their own access without a secondary check.

**Procedure:** Inspect the two sampled review packages end-to-end. For the report-logic test, independently extract the current account list from one system and reconcile against the most recent review's input listing (count and spot-check 5 accounts both directions). Reperform a slice: pick 10 accounts from a sampled review and form your own view of business need; compare with the reviewer's dispositions.

**Pitfalls:** Testing only that the review "happened" (A1) and skipping input completeness (A2) — a review of a stale or partial export is the most common silent failure. Reviews that have never once flagged anything warrant reperformance, not acceptance.

---

## 2. Change approval

**Control (typical):** Production changes require documented approval by an authorized, non-author approver before deployment; emergency changes follow a documented retro-approval path within 24 hours.
**Type:** Manual approval, often over an automated gate. **Frequency:** per-occurrence → sample 25 (stratify: standard vs. emergency; take all emergency changes if < 5).

**Population:** All production changes in the period from the deployment log (not the ticket system). Completeness: reconcile deploy log count to change tickets; unticketed deploys are findings in themselves.

**Attributes:** A1 approval recorded; A2 approver ≠ author/developer; A3 approver on the authorized-approver list at approval date; A4 approval timestamp ≤ deployment timestamp (or emergency path followed, with retro-approval inside its window); A5 evidence of testing/validation before approval where required.

**Procedure:** Inspection of tickets against deploy-log timestamps. If an automated merge/deploy gate exists, additionally test it as an automated control: inspect the branch-protection/pipeline config, verify one negative case (unapproved merge blocked), and confirm config change history for the period.

**Pitfalls:** Sampling from tickets instead of deployments (misses unticketed changes). Ignoring A4 timestamp ordering — "approved" tickets where approval postdates deploy. Not checking A3: approvals by people who left the approver group.

---

## 3. Backup and restore testing

**Control (typical):** In-scope systems are backed up per schedule; backup failures are alerted and resolved; restoration is tested at least annually per system.
**Type:** Automated (backup execution) + manual (failure handling, restore test). **Frequency:** backup jobs daily → automated: config + 1 instance, plus failure-handling sample; restore test annual → 1.

**Population:** Backup job catalog (all in-scope systems mapped to jobs — completeness against the system inventory); job failure alerts for the period; restore test records.

**Attributes:**
- Backup config: schedule, scope, and retention match policy per sampled system; encryption per policy.
- Failure handling: for 5 sampled failure alerts (or all, if fewer), alert generated, ticket raised, resolved, and a successful subsequent backup confirmed.
- Restore: annual test performed per in-scope system class, with date, performer, target, success criteria, result, and issues remediated.

**Procedure:** Inspect backup tool config against the system inventory (the completeness test *is* the point: find in-scope systems with no backup job). Inspect one successful job log. Sample failure alerts. Inspect restore-test evidence; strongest form is reperformance — observe a live restore of one sampled system.

**Pitfalls:** Accepting "backups are green" without mapping jobs to the full system inventory. Restore "tests" that only verify the backup file exists rather than restoring and validating data usability.

---

## 4. Vulnerability remediation SLA

**Control (typical):** Vulnerabilities are remediated within SLA by severity — e.g., critical 15 days, high 30, medium 90 — measured from detection; exceptions require documented risk acceptance.
**Type:** ITDM (scanner data + human triage/remediation). **Frequency:** continuous → sample 25 closed/aged findings, stratified by severity (weight toward critical/high).

**Population:** All findings detected or open during the period, from the scanner/VM platform with query and count. Completeness: verify scan coverage first — reconcile scanned assets to the asset inventory; unscanned assets make the finding population structurally incomplete.

**Attributes:** A1 severity assigned per the documented methodology (spot-check rescoring downgrades especially); A2 remediation date − detection date ≤ SLA for the severity; A3 remediation verified (rescan clean or validated fix), not just ticket-closed; A4 overdue/accepted items have a documented, authorized risk acceptance with expiry (cross-check against the exception register).

**Procedure:** Inspect the VM platform export; recompute aging yourself from raw detection/closure dates — do not trust the tool's SLA dashboard without checking its clock-start definition (first-detected vs. last-detected vs. ticket-created materially changes results). Sample per attributes.

**Pitfalls:** SLA measured from ticket creation while the control says detection. Findings "closed" by asset decommission or scanner scope change counted as remediated. Ignoring the scan-coverage precondition.

---

## 5. Leavers — access removal (JML: leaver)

**Control (typical):** Upon termination, all logical access is revoked within 1 business day (immediately for involuntary), per an HR-triggered offboarding workflow.
**Type:** Manual or partially automated workflow. **Frequency:** per-occurrence → sample 25 (or all, if fewer terminations in period).

**Population:** All terminations in the period **from HRIS** — never from the offboarding ticket queue (a termination with no ticket is precisely the failure you're hunting). Completeness: HRIS report with count; reconcile to ticket count and investigate differences.

**Attributes:** A1 offboarding ticket exists and was triggered by/linked to the HR record; A2 access disabled in each in-scope system with timestamp ≤ SLA from termination effective date/time; A3 involuntary terminations handled on the accelerated path; A4 physical access/tokens/MFA devices revoked where in scope.

**Procedure:** For each sampled leaver, inspect disable/revocation timestamps *in each in-scope system's own logs* (directory service, SaaS admin logs) — not just the ticket's "done" checkbox. Reperform a full sweep: take 5 sampled leavers and search all in-scope systems for any still-active account or session.

**Pitfalls:** Testing from the ticket population. Accepting ticket closure as proof of removal. Forgetting non-SSO systems, service accounts owned by the leaver, and shared credentials the leaver knew.

---

## 6. Joiners and movers — provisioning (JML: joiner/mover)

**Control (typical):** Access is granted only via approved request, per role-based profiles; transfers trigger review and removal of no-longer-needed access within 5 business days.
**Type:** Manual approval workflow, often with automated provisioning. **Frequency:** per-occurrence → sample 25 joiners; movers sampled separately (10, or all if fewer) because the failure mode differs.

**Population:** Joiners: HRIS hires for the period reconciled to account-creation logs (accounts created with no matching hire = finding). Movers: HRIS role/department changes.

**Attributes (joiner):** A1 documented request; A2 approval by the authorized approver *before* provisioning; A3 access granted matches the approved request/role profile (compare actual entitlements to request, not just "account exists"); A4 timeliness per policy.
**Attributes (mover):** A5 transfer triggered an access review; A6 access from the former role removed within SLA — accumulation is the mover failure mode.

**Procedure:** Inspection of requests vs. actual entitlements pulled from the system. For movers, reperform: for 5 sampled movers, list current entitlements and map each to current role; unmapped legacy entitlements fail A6.

**Pitfalls:** Testing that an approval exists without comparing granted-vs-approved entitlements. Skipping movers entirely (most programs do; auditors increasingly don't).

---

## 7. Security log / alert review

**Control (typical):** Security alerts from the SIEM are triaged within defined SLAs by severity; a documented review of key log sources/dashboards occurs daily; escalations follow the incident process.
**Type:** ITDM. **Frequency:** daily review → sample 25 days; alert triage per-occurrence → sample 25 alerts. Plus report-logic test on the SIEM pipeline.

**Population:** Alert export from the SIEM with query/count; review records (checklist, shift log, or tool audit trail) for the period. Completeness for the pipeline: verify in-scope log sources are actually feeding the SIEM (source health/ingestion status vs. the documented log-source list) — a diligent review of a SIEM missing half its feeds fails as a control.

**Attributes:** Per sampled day: review evidenced with reviewer and time. Per sampled alert: A1 triaged within SLA for its severity; A2 disposition recorded with rationale; A3 escalated alerts entered the incident process with linkage; A4 closed-as-benign alerts have a stated reason (not bulk-closed).

**Procedure:** Inspect ingestion/source health first. Inspect sampled reviews and alerts. Reperform triage on 5 sampled alerts: reach your own disposition from the alert data and compare. Check bulk-closure patterns in the alert audit trail (hundreds closed in one minute by one analyst = rubber stamp).

**Pitfalls:** Treating raw log existence as review evidence. Missing the log-source completeness precondition. Not probing bulk closures.

---

## 8. Endpoint hardening baseline

**Control (typical):** All endpoints are configured per the hardening baseline (disk encryption, EDR agent, screen lock, patch agent, local admin restricted), enforced via MDM/config management; drift is detected and remediated within SLA.
**Type:** Automated enforcement + ITDM drift handling. **Frequency:** automated: config + instance per platform; drift remediation per-occurrence → sample 10 drift/noncompliance records.

**Population:** Endpoint inventory from MDM reconciled against an independent source (directory join records, EDR console, procurement) — endpoints outside MDM are the population gap that matters most. Compliance/drift report with count.

**Attributes:** A1 baseline policy content matches the documented hardening standard (inspect each control in the profile: encryption on, EDR required, lock timeout value, admin rights); A2 policy assigned to all endpoint groups, no unexplained exclusions; A3 compliance rate report is system-generated; sampled "compliant" devices verified by direct inspection of 5 devices' actual state; A4 sampled noncompliant devices remediated or isolated within SLA.

**Procedure:** Inspect MDM policy configuration per platform (macOS/Windows profiles are separate configs — test each). Reconcile inventories. Reperform on 5 devices: pull device-level state from the MDM/EDR and compare each baseline item. Inspect drift-remediation records.

**Pitfalls:** Testing the policy document instead of the deployed profile. Ignoring exclusion groups ("executives", "developers") that swallow the riskiest machines. Trusting the compliance percentage without device-level verification.

---

## 9. MFA enforcement

**Control (typical):** MFA is required for all user access to in-scope systems (or at the SSO/IdP layer), including remote and administrative access; exceptions require documented approval.
**Type:** Fully automated. **Frequency:** config + 1 instance, per policy per IdP/tenant.

**Population:** The IdP authentication policies; the user population; the exception/exclusion list.

**Attributes:** A1 policy requires MFA for the in-scope population with no unexplained exclusions (inspect every exclusion group and named-user exception; each needs a documented, unexpired approval); A2 legacy/bypass protocols disabled (protocols that skip modern auth); A3 negative test: authentication attempt without a second factor is refused; A4 coverage: applications in scope actually route through the IdP — reconcile app inventory to SSO-integrated apps; direct-login paths bypass the control entirely; A5 config unchanged in the period (IdP audit log for the policy object).

**Procedure:** Inspect policy objects and exclusion lists in the IdP admin console. Observe/reperform one negative test with a test account. Inspect sign-in logs for a sample of 5 users across the period confirming MFA was performed. Inspect policy change history.

**Pitfalls:** Concluding on the policy while service accounts, API tokens, and non-SSO apps sit outside it. Exception lists with no expiry that only ever grow — cross-check against [exception-management](../../exception-management/SKILL.md) records.

---

## 10. Privileged access restriction and admin review

**Control (typical):** Administrative access is restricted to authorized personnel, granted via approval, reviewed monthly, and used via dedicated admin accounts (or just-in-time elevation) with logging.
**Type:** Manual grant + ITDM review. **Frequency:** monthly review → sample 2; grants per-occurrence → sample all grants if ≤ 25, else 25.

**Population:** Current privileged account listing pulled directly from each system/directory (not from the access tool's cached view); privileged-access grant tickets for the period; monthly review records. Completeness: enumerate privileged roles per system yourself (domain/tenant admin roles, root, DB admin, cloud org-level roles) — the documented "admin list" is frequently narrower than actual privileged role membership.

**Attributes:** A1 every current privileged account maps to an authorized, current employee with business need (full-population test, not a sample — privileged populations are small enough); A2 sampled grants have prior approval by the designated authority; A3 monthly reviews performed and evidenced with dispositions; A4 no standing shared admin credentials, or where they exist, vaulted with check-out logging; A5 admin activity logged and log sampled for 3 sessions tying activity to an individual.

**Procedure:** Independently enumerate privileged role membership (reperformance) and reconcile to the authorized list — differences are the finding. Inspect grants and reviews per sample.

**Pitfalls:** Sampling the privileged population instead of testing it 100%. Missing indirect privilege: group nesting, role-assumption paths, API keys with admin scopes.

---

## 11. Security awareness training

**Control (typical):** All personnel complete security awareness training within 30 days of hire and annually thereafter; completion is tracked and non-completion escalated.
**Type:** Manual/administrative with system tracking. **Frequency:** annual cycle + per-hire → sample 25 across both strata (weight toward new hires).

**Population:** The denominator is the point: all personnel *required* to train — HRIS headcount for the period including contractors if in scope — not the LMS enrollment list. Completeness: reconcile LMS assigned-user count to HRIS active headcount; people missing from the LMS are the primary failure.

**Attributes:** A1 sampled person was assigned the training; A2 completed within the deadline (hire + 30 days, or within the annual window); A3 completion record shows person, course/version, and date; A4 non-completers were escalated per the documented consequence (reminder → manager → access action), with evidence.

**Procedure:** Inspect the HRIS-to-LMS reconciliation (or perform it). Sample completions. Inspect escalation evidence for the period's non-completers — a control with 100% claimed completion and no escalation history for a 500-person org across a full year deserves skepticism; verify a handful of completion timestamps against the LMS audit log.

**Pitfalls:** Testing completion rate against LMS enrollees instead of HRIS headcount. Ignoring contractors when the policy includes them. New-hire deadline measured from LMS assignment date rather than hire date.

---

## 12. Incident response process

**Control (typical):** Security incidents are declared, categorized by severity, managed per the IR plan (containment, eradication, recovery), with defined internal escalation, regulatory-notification assessment, and post-incident review for high-severity incidents; the plan is tested at least annually.
**Type:** Manual process control. **Frequency:** per-occurrence → sample 5 incidents (or all if fewer), weighted to highest severity; plan test annual → 1.

**Population:** Incident register for the period. Completeness: reconcile against escalated SIEM alerts (control 7) and helpdesk security-tagged tickets — incidents handled "off register" are the completeness failure.

**Attributes:** A1 severity assigned per the documented matrix, and assessment for regulatory notification duties documented where facts could trigger them (see [../../incident-regulatory-reporting/SKILL.md](../../incident-regulatory-reporting/SKILL.md)); A2 escalation to the roles the plan names, within the plan's timeframes; A3 containment/eradication/recovery actions logged with timestamps; A4 post-incident review held for qualifying incidents, with tracked actions; A5 annual test (tabletop or functional) performed with scenario, participants, findings, and follow-ups.

**Procedure:** Inspect sampled incident records end-to-end against the IR plan's requirements. Inspect the annual test package. Inquiry with the IR lead to corroborate the walkthrough of the most recent high-severity incident.

**Pitfalls:** Testing only that tickets exist rather than that the *plan's* specific steps and timeframes were followed. Accepting a tabletop with no documented findings or follow-up actions as a "test". Missing the regulatory-assessment attribute on personal-data or reportable-sector incidents.

---

## Using this library

- Always rewrite the control statement to match the organization's documented control before deriving attributes; attributes test *their* commitments.
- Where a procedure says "reconcile X to Y", that reconciliation is a population-completeness test — document it per [sampling-guide.md](sampling-guide.md).
- Any attribute failure follows the exception workflow in [sampling-guide.md](sampling-guide.md): confirm it is real, root-cause, expand or classify.
