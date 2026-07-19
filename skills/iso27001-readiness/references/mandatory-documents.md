# ISO/IEC 27001:2022 Mandatory Documented Information

The 2022 standard uses one term — "documented information" — for both documents (maintained: kept current) and records (retained: kept as evidence). This reference lists what the standard explicitly requires, with clause references, then the second tier auditors expect in practice via applicable Annex A controls. Verify wording against the official standard text; clause paraphrases below are summaries.

All documented information is subject to clause 7.5 control: identified and described (title, date, author/reference), format-controlled, reviewed and approved for suitability, available where needed, and protected (access, version control, retention, disposition). Missing 7.5 control over an otherwise-good document is itself a findable nonconformity.

## Tier 1 — Explicitly required by clauses 4-10

| # | Documented information | Clause | Maintain / Retain | Notes for auditors' eyes |
|---|---|---|---|---|
| 1 | Scope of the ISMS | 4.3 | Maintain | Must reflect consideration of internal/external issues (4.1), interested-party requirements (4.2), and interfaces/dependencies with other organizations. The certificate scope derives from this |
| 2 | Information security policy | 5.2 | Maintain | Approved by top management; includes commitment to satisfy applicable requirements and to continual improvement; communicated internally, available to interested parties as appropriate |
| 3 | Information security risk assessment process | 6.1.2 | Retain (about the process) | Must define risk acceptance criteria and criteria for performing assessments; produce consistent, valid, comparable results |
| 4 | Information security risk treatment process | 6.1.3 | Retain (about the process) | Includes how controls are determined and compared with Annex A |
| 5 | Statement of Applicability | 6.1.3 d) | Maintain | All 93 Annex A controls + any additional necessary controls; justification for inclusion; whether implemented; justification for every exclusion |
| 6 | Risk treatment plan | 6.1.3 e)-f) | Retain (as part of treatment process/results) | Requires risk owners' approval of the plan and acceptance of residual information security risks — capture both signatures/records |
| 7 | Information security objectives | 6.2 | Maintain | Measurable (if practicable), monitored, communicated, updated; the 2022 text expects plans: what, resources, who, when, how results evaluated |
| 8 | Evidence of competence | 7.2 | Retain | CVs, training records, certifications for people doing work affecting ISMS performance — including the internal auditor's competence |
| 9 | Operational planning and control | 8.1 | Retain (to extent necessary) | Enough to give confidence processes ran as planned — e.g., records of processes, outsourced-process control |
| 10 | Results of information security risk assessments | 8.2 | Retain | Dated results from planned intervals and from significant changes — one assessment three years ago fails 8.2 |
| 11 | Results of information security risk treatment | 8.3 | Retain | Implementation status of the treatment plan |
| 12 | Evidence of monitoring and measurement results | 9.1 | Retain | What is measured, methods, when, by whom, results — link to security objectives (6.2) |
| 13 | Internal audit programme(s) and audit results | 9.2 | Retain | Programme (frequency, methods, responsibilities, planning requirements, reporting) plus per-audit criteria, scope, findings |
| 14 | Results of management reviews | 9.3 | Retain | Minutes/records showing all required inputs considered and decisions on improvement opportunities and ISMS changes |
| 15 | Nature of nonconformities, actions taken, and results of corrective actions | 10.2 | Retain | The full loop: nonconformity → correction → root cause → corrective action → effectiveness review |

Clause 6.3 (planning of changes, new in 2022) requires changes to the ISMS be carried out in a planned manner but does not itself mandate a document; auditors nevertheless ask how change planning is evidenced — a change log or management review record usually serves.

## Tier 2 — Expected via applicable Annex A controls

Not listed as mandatory in clauses 4-10, but where the SoA marks these controls applicable (almost always), the control text or its 27002:2022 guidance implies documentation, and certification auditors treat absence as a nonconformity against the control:

| Documented information | Driving control(s) |
|---|---|
| Topic-specific policies (access control, information transfer, backup, secure development, etc.) | A.5.1 Policies for information security |
| Definition and allocation of security roles and responsibilities | A.5.2 |
| Inventory of information and other associated assets, with owners | A.5.9 |
| Acceptable use rules for information and assets | A.5.10 |
| Access control rules (topic-specific policy) | A.5.15 |
| Supplier security requirements and agreements | A.5.19-A.5.22 |
| Incident management planning: roles, procedures, response and reporting processes | A.5.24-A.5.28 |
| ICT continuity / readiness plans | A.5.29-A.5.30 |
| Legal, statutory, regulatory and contractual requirements register | A.5.31 |
| Documented operating procedures for operational facilities | A.5.37 |
| Confidentiality or non-disclosure agreements | A.6.6 |
| Configuration baselines/standards | A.8.9 |
| Backup policy/arrangements and test records | A.8.13 |
| Logging and monitoring arrangements | A.8.15-A.8.16 |
| Secure development rules/lifecycle documentation | A.8.25-A.8.28 |
| Change management procedure records | A.8.32 |

Scale tier 2 to the organization. The standard does not prescribe document count, length, or structure — a startup's two-page access control policy that matches reality beats a 40-page template that doesn't. Every process a document claims ("reviewed quarterly," "tested annually") becomes an audit test; write cadences the organization will actually keep.

## Operating records auditors sample at stage 2

Beyond the documents above, stage 2 auditors sample the records those documents promise. Ensure at least one cycle (ideally 3+ months) exists for:

- Access grants/revocations and periodic access review records
- Awareness training completion (7.3 evidence in practice)
- Risk register updates and treatment plan progress
- Incident and event records, including "no incidents" being credible against monitoring output
- Backup execution and restore-test results
- Vulnerability scan results and remediation records
- Change records
- Supplier review records
- Management review minutes and internal audit workpapers (tier 1, but the most commonly missing)

## Register format

Track readiness with a simple register:

| Doc | Clause/control | Owner | Version | Approved | Last review | Status |
|---|---|---|---|---|---|---|
| ISMS Scope | 4.3 | CISO | 1.2 | 2026-05-02 | 2026-05-02 | Current |
| SoA | 6.1.3 d) | CISO | 2.0 | 2026-06-10 | 2026-06-10 | Current |
| Internal audit results | 9.2 | Ext. auditor | — | — | — | Missing — scheduled Sep 2026 |

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
