# SOX for IT and Security Teams: Sections 302/404, ICFR, and IT General Controls

## At a glance

| Item | Detail |
|---|---|
| Law | Sarbanes-Oxley Act of 2002 (US federal), enforced by the SEC |
| Applies to | US public companies (SEC registrants), including foreign private issuers; their in-scope subsidiaries and outsourced processes |
| Core sections for IT | s302 (officer certification of disclosure controls), s404 (internal control over financial reporting) |
| s404(a) | Management's annual assessment of ICFR effectiveness — all registrants |
| s404(b) | External auditor attestation on ICFR — accelerated and large accelerated filers |
| Audit standard | PCAOB AS 2201 (audit of ICFR integrated with the financial statement audit) |
| Control framework | COSO Internal Control — Integrated Framework (2013) is the near-universal choice |
| IT relevance | ITGCs underpin reliance on automated controls, application controls, and system-generated reports |
| Failure taxonomy | Control deficiency → significant deficiency → material weakness (publicly disclosed) |

## Why SOX matters to security teams

SOX is a financial reporting law, not a security law — but modern financial reporting runs on systems. Management and auditors can only rely on automated controls (three-way match, posting logic, interfaces, calculations) and system-generated reports if the IT environment that hosts them is controlled. That is the job of IT General Controls (ITGCs). When ITGCs fail, auditors lose reliance on everything downstream: automated controls must be retested substantively, sample sizes balloon, audit fees rise, and unremediated failures can aggregate into a disclosed material weakness. Security teams typically own most ITGC evidence: access management, change management, and operations.

## s302 and s404 essentials

- **s302 — Disclosure controls certification.** The CEO and CFO personally certify each quarterly and annual report: that it is accurate, that disclosure controls and procedures are effective, and that they have disclosed to the auditor and audit committee all significant deficiencies, material weaknesses, and any fraud involving personnel with a significant role in internal control. This certification is why executives care about your control failures.
- **s404(a) — Management assessment.** Management must assess and report annually on the effectiveness of internal control over financial reporting (ICFR), using a recognized framework (COSO in practice). This drives the internal SOX program: scoping, control documentation, testing, deficiency evaluation.
- **s404(b) — Auditor attestation.** The external auditor independently opines on ICFR for accelerated and large accelerated filers, under PCAOB AS 2201. The auditor performs their own walkthroughs and tests; they may use management's or internal audit's work only within strict limits.
- **ICFR vs. disclosure controls.** ICFR covers the reliability of financial reporting and financial statement preparation. Disclosure controls (s302) are broader — they cover everything a registrant must disclose, including cybersecurity incidents (see [sec-cyber-disclosure.md](sec-cyber-disclosure.md)).

## Scoping: which systems are in SOX scope

Scope flows top-down from the financial statements, not from an asset inventory:

1. Identify material financial statement line items and disclosures.
2. Map each to the significant business processes that produce them (revenue, procure-to-pay, payroll, treasury, inventory, financial close and consolidation, tax).
3. Identify the applications, databases, operating systems, and infrastructure supporting those processes — including ERP, sub-ledgers, billing platforms, consolidation and close tools, and interfaces between them.
4. Include the spreadsheets and end-user computing tools that materially feed reporting (EUC controls), and the SOC 1 reports for outsourced processing (payroll providers, cloud-hosted ERP, claims processors).
5. Document the "layers" per application: application, database, OS, and supporting infrastructure — ITGCs are tested at each relevant layer.

A system with no path to a material financial statement assertion is out of SOX scope regardless of its security importance. Conversely, an obscure interface job that feeds the general ledger is in scope.

## The four classic ITGC domains

### 1. Access to programs and data

- **Provisioning:** new access and access changes are requested and approved by an appropriate owner before grant; approval is evidenced and retained.
- **Deprovisioning:** access is removed timely on termination or transfer. "Timely" must be defined (commonly within 1–3 business days for terminations); auditors test the population of leavers against removal dates.
- **Privileged access:** administrative access to in-scope applications, databases, and OS is restricted to authorized personnel, individually attributable (no shared generic admin accounts without compensating controls), and monitored. Direct database update access is a perennial finding.
- **Periodic access review:** user and privileged access is recertified on a defined cadence (typically quarterly for privileged, at least annually for standard), with evidence that flagged access was actually removed — a review that identifies issues but never remediates them fails.
- **Segregation of duties (SoD):** conflicting duties (e.g., create vendor + approve payment; maintain user access + approve journal entries; develop code + deploy to production) are separated, or a documented compensating/monitoring control exists. ERP SoD rulesets and mitigating-control mappings are commonly tested.
- **Authentication:** password/MFA configurations meeting policy at each layer.

### 2. Program changes (change management)

- Changes to in-scope applications and their supporting infrastructure are authorized, tested, and approved before deployment to production.
- **Segregated deployment:** developers do not migrate their own changes to production; deployment is performed by a separate person/team or a controlled pipeline. If developers hold production access, a compensating monitoring control (e.g., independent review of production changes) is required.
- Emergency changes follow an expedited path but still get retrospective approval and documentation.
- Auditors typically test a sample of changes from a system-generated population of production deployments — completeness of that population matters (see IPE below). DevOps and CI/CD pipelines are acceptable when pipeline configurations enforce approvals and the pipeline configuration itself is change-controlled and access-restricted.

### 3. Program development

- New systems and major implementations affecting financial reporting follow a controlled methodology: requirements, testing (including UAT with business sign-off), data conversion validation, and go-live approval.
- Data migration controls: completeness and accuracy of converted balances and master data are reconciled and approved.
- Applies only in years with relevant implementations; still document the control's design.

### 4. Computer operations

- **Job scheduling and monitoring:** critical batch jobs and interfaces (sub-ledger to GL feeds, revenue jobs) are monitored; failures are identified, resolved, and evidence of resolution retained.
- **Backup and recovery:** in-scope financial data is backed up per schedule; failures are remediated; restoration capability is periodically verified.
- **Incident and problem management:** incidents affecting in-scope systems are logged, resolved, and — critically — assessed for financial reporting impact (e.g., data corruption, unprocessed transactions, unauthorized changes).

## Key reports and IPE integrity

Information Produced by the Entity (IPE) — system-generated reports and query outputs used either in performing a control (a "key report") or as audit evidence — must be shown complete and accurate. For each key report, be able to evidence:

- **Source and logic:** where the data comes from and what parameters/filters were applied.
- **Report logic integrity:** standard reports rely on ITGCs over the application; custom reports and queries need validation (logic inspection, benchmarking, or re-performance) and change control over the report definition.
- **Parameter evidence:** screenshots or system logs showing the parameters used for the specific run.

Population completeness for testing (all terminations, all changes, all users) is IPE too — an incomplete change population undermines the entire change-management test.

## Deficiency evaluation and aggregation

| Level | Definition (paraphrased) | Consequence |
|---|---|---|
| Control deficiency | Control design or operation does not allow timely prevention/detection of misstatements | Tracked and remediated; evaluated for aggregation |
| Significant deficiency | Less severe than a material weakness but important enough to merit attention of those responsible for financial reporting oversight | Reported to the audit committee and external auditor |
| Material weakness | Reasonable possibility that a material misstatement will not be prevented or detected timely | Publicly disclosed in the 10-K; management cannot conclude ICFR is effective |

Key dynamics for IT:

- Severity is judged on **potential** misstatement (magnitude × likelihood), not whether a misstatement actually occurred.
- ITGC deficiencies are evaluated **through their effect on dependent controls**: a failed change-management control means every automated control and key report on that system is potentially unreliable for the exposure period.
- Deficiencies **aggregate**: several individually minor deficiencies affecting the same process, account, or assertion can combine into a significant deficiency or material weakness.
- **Compensating controls** (e.g., a precise business reconciliation that would catch the error an ITGC failure could introduce) can reduce severity — but must operate at a level of precision that would actually detect a material misstatement, and must be tested.
- Remediation must operate for a sufficient period before year-end to be credited; a control fixed in December rarely rescues the year.

## PCAOB and external-auditor reliance dynamics

- The external auditor's ITGC scope is driven by their planned **reliance strategy**: heavy reliance on automated controls and reports means deep ITGC testing; a fully substantive audit reduces ITGC emphasis but massively increases substantive work.
- Auditors may use the work of internal audit or management's testers, subject to competence/objectivity assessment and re-performance — higher-risk controls (privileged access, SoD over journal entries) are usually retested directly by the auditor.
- Expect walkthroughs of each ITGC process, sample-based operating-effectiveness testing across the period, and roll-forward testing between interim and year-end.
- For outsourced systems, the auditor relies on **SOC 1 Type II** reports — review them for qualified opinions, testing exceptions, sub-service organizations, and Complementary User Entity Controls (CUECs) that your organization must itself perform and evidence. See [../frameworks/soc2-tsc.md](../frameworks/soc2-tsc.md) for SOC report mechanics.
- PCAOB inspection pressure on audit firms flows downhill: inspection findings about ITGC and IPE testing translate into deeper, less flexible auditor requests the following year.

## Key obligations for security/GRC teams

1. Maintain the in-scope system inventory jointly with finance; re-scope annually and on M&A, ERP migrations, or new revenue streams.
2. Own and evidence the ITGC control set: provisioning/deprovisioning, privileged access, periodic access reviews, SoD, change management, job monitoring, backup — with retained, dated evidence for the full fiscal year.
3. Define "timely" SLAs (termination removal, access review remediation) in policy and meet them — auditors test to your own stated standard.
4. Control IPE: inventory key reports, validate custom report logic, capture run parameters, and prove population completeness for every testing population you hand over.
5. Evaluate every ITGC failure for downstream effect on automated controls and reports; escalate potential significant deficiencies to the controller/SOX PMO immediately, not at year-end.
6. Assess security incidents on in-scope systems for ICFR impact and s302 disclosure impact; route material cyber incidents into the disclosure process (see [sec-cyber-disclosure.md](sec-cyber-disclosure.md)).
7. Collect and review SOC 1 reports for in-scope service providers; map and operate CUECs (see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md)).
8. Test controls before the auditor does (see [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md)) and prepare evidence packages proactively (see [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md)).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
