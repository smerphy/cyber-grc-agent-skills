# GRC Glossary

Working definitions for terms used throughout this repository. Definitions reflect common usage in security governance, risk, compliance, and audit practice; where a framework defines a term more narrowly, the framework's definition controls in that context.

**Assurance** — Confidence that controls or processes achieve their objectives, supported by evidence. Levels range from self-assessment through independent internal audit to external attestation or certification; the appropriate level depends on who needs to rely on the result.

**Attestation** — A practitioner's (typically a CPA firm's) formal report on subject matter against defined criteria — e.g., a SOC 2 report attests to controls against the Trust Services Criteria. Distinct from certification (e.g., ISO 27001, issued by an accredited certification body against a standard).

**Audit trail** — Chronological, tamper-evident records sufficient to reconstruct who did what, when, and with what result. Required for both security investigation and audit evidence; retention and protection requirements come from applicable frameworks and law.

**Baseline** — An approved reference configuration or minimum control set against which deviations are measured — e.g., a hardened OS build, or the 800-53 low/moderate/high control baselines.

**Bridge letter (gap letter)** — A letter from a service organization's management covering the period between a SOC report's end date and the user's reporting date, asserting whether controls materially changed. Management representation only — not auditor assurance.

**Business impact analysis (BIA)** — Analysis identifying critical business processes, the impact of their disruption over time, and recovery requirements (RTO/RPO). Feeds continuity planning and helps prioritize control investment.

**Carve-out vs. inclusive method** — SOC reporting treatment of subservice organizations. Carve-out excludes the subservice org's controls from the report (users must obtain its own SOC report); inclusive covers them within the examination.

**Compensating control** — An alternative control that mitigates the risk of a requirement that cannot be met as stated. Must meet the intent and rigor of the original requirement and be documented with a risk analysis; PCI DSS formalizes this, and v4 adds the distinct "customized approach."

**Complementary subservice organization control (CSOC)** — A control assumed, in a SOC report, to be operating at a carved-out subservice organization for the service organization's control objectives to be met.

**Complementary user entity control (CUEC)** — A control a SOC report assumes the *customer* operates (e.g., deprovisioning its own users) for the service organization's controls to achieve their objectives. Reviewing CUECs is a required step when relying on a vendor's SOC report.

**Continuous control monitoring (CCM)** — Automated, ongoing evaluation of control operation (e.g., daily checks that MFA is enforced) rather than point-in-time testing. Reduces sampling burden but requires assurance over the monitoring pipeline itself.

**Control** — A measure that modifies risk. Classify by function: *preventive* (stops the event: MFA), *detective* (identifies it: log review), *corrective* (limits/repairs impact: restore from backup). Classify by execution: *automated* (system-enforced), *manual* (human-performed), *IT-dependent manual* (human decision on system-produced data — test both the human step and the report's accuracy/completeness).

**Control environment** — The tone, structures, and accountability set by governance and management that underpin all other controls; the foundation component in COSO and the substance of SOC 2 CC1.

**Control objective** — The outcome a control (or set of controls) is intended to achieve, stated in testable terms — e.g., "access to production is restricted to authorized personnel and reviewed quarterly." Findings are assessed against objectives, not control mechanics.

**Control owner** — The individual accountable for a control's design, operation, and remediation of its deficiencies. Distinct from the risk owner and from operators who execute the control.

**Criteria** — The benchmark against which subject matter is evaluated in an assessment or attestation (e.g., Trust Services Criteria, ISO 27001 clauses, internal policy). No criteria, no audit — every finding must trace to one.

**Deficiency** — A shortfall in control design (control couldn't achieve its objective even if operated as designed) or operation (control doesn't operate as designed, or operator lacks competence/authority). In ICFR, escalates by severity to *significant deficiency* and *material weakness*.

**Design vs. operating effectiveness** — Design effectiveness: the control, as designed, would achieve its objective (tested by walkthrough/inspection; SOC 2 Type I stops here). Operating effectiveness: the control actually operated as designed over a period (tested via sampling/reperformance; SOC 2 Type II, SOX testing).

**DPIA (Data Protection Impact Assessment)** — Structured assessment of a processing activity's risks to individuals, required under GDPR Art. 35 for processing likely to result in high risk. See [regulations/gdpr.md](regulations/gdpr.md) and the dpia-privacy-assessment skill.

**Entity-level control** — A control operating across the organization rather than at a process/transaction level — e.g., code of conduct, risk assessment process, security governance committee. Strong entity-level controls can reduce (not eliminate) reliance on process-level testing.

**Evidence** — Records demonstrating a control's design or operation: configurations, tickets, logs, screenshots, reports, signed approvals. Quality attributes: relevant, reliable (system-generated beats self-attested), complete for the period, and traceable to the population tested.

**Exception (audit)** — A sampled instance where the control did not operate as prescribed. One exception does not automatically equal a failed control — evaluate cause, frequency, and impact — but it must be recorded and dispositioned, never silently dropped.

**Exception (policy/control)** — A formally approved, time-bound deviation from a policy or standard, with documented compensating measures, risk acceptance by an authorized owner, and an expiry/review date. Untracked exceptions are unmanaged risk.

**FAIR (Factor Analysis of Information Risk)** — A quantitative risk-analysis model decomposing risk into loss event frequency and loss magnitude, estimated as calibrated ranges and combined via simulation. See [risk-scoring.md](risk-scoring.md).

**Finding** — A documented gap between criteria and condition, typically structured as condition, criteria, cause, consequence (risk), and recommendation, with a severity rating and an owner.

**Gap assessment** — Comparison of current-state controls against a target framework or regulation to identify missing or partial coverage. Produces a remediation roadmap; distinct from an audit (no opinion, usually no operating-effectiveness testing).

**GRC (Governance, Risk & Compliance)** — The integrated discipline of directing an organization (governance), understanding and treating uncertainty (risk management), and meeting obligations (compliance) — ideally on shared processes, taxonomy, and tooling rather than in silos.

**Heat map** — A matrix visualization of risks by likelihood and impact rating. Useful for communication; unreliable for prioritization arithmetic — see [risk-scoring.md](risk-scoring.md) for the pitfalls.

**ICFR (Internal Control over Financial Reporting)** — Controls providing reasonable assurance about the reliability of financial reporting; the subject of SOX §302/§404. IT general controls are in scope where systems support financial reporting.

**Independence** — Freedom from conditions that compromise (or appear to compromise) an assessor's unbiased judgment — organizationally (reporting lines) and individually (self-review, familiarity). A control owner cannot audit their own control.

**Inherent risk** — Risk level before considering the effect of controls. Pairs with residual risk; the delta indicates how much you depend on your controls continuing to operate.

**ISMS (Information Security Management System)** — The governed system of policies, processes, roles, and improvement cycles for managing information security — the certifiable subject of ISO 27001, spanning its clauses 4–10 plus applicable Annex A controls.

**ITGC (IT General Controls)** — Controls over the IT environment on which application and reporting controls depend: access management, change management, IT operations (jobs/backup/incident), and program development. The backbone of SOX IT scope.

**Key control** — A control whose failure would create a reasonable possibility that a material error or significant risk would not be prevented or detected. Testing effort concentrates on key controls.

**KPI (Key Performance Indicator)** — A metric of how well a process performs against its goal (e.g., patch SLA attainment). Compare KRI.

**KRI (Key Risk Indicator)** — A metric that provides early signal of rising risk exposure (e.g., growth in unremediated critical vulnerabilities, privileged accounts without MFA), ideally with thresholds that trigger defined responses.

**Management assertion** — Management's written claim that an assessor then examines — e.g., the system description and control effectiveness assertion in a SOC 2 report, or SOX §302 certifications.

**Material weakness** — An ICFR deficiency (or combination) such that there is a reasonable possibility a material misstatement will not be prevented or detected timely. Publicly disclosed; the most severe deficiency class.

**Materiality** — The threshold at which information would influence a reasonable decision-maker. Context-specific: financial-statement materiality (SOX), disclosure materiality (SEC cyber incidents — quantitative and qualitative), and audit-scoping materiality differ.

**Maturity model** — A scale describing progressive capability levels for a process, typically from ad hoc through defined to optimizing (e.g., CMMI-style 1–5). Measures process institutionalization, not risk reduction — a mature process can still target the wrong risks.

**POA&M (Plan of Action & Milestones)** — A structured remediation register for known weaknesses: weakness, source, responsible party, resources, milestones with dates, and status. Standard in US federal practice (FISMA, FedRAMP) and a useful pattern anywhere.

**Policy / standard / procedure / guideline** — Policy: mandatory management intent ("what and why"). Standard: mandatory specific requirements ("how much/which"). Procedure: step-by-step instructions ("how"). Guideline: recommended, non-mandatory practice. Keep the layers separate so each can change at its own cadence.

**Population** — The complete set of items subject to a control during the test period (all changes, all new hires, all terminations). Sampling is only valid if the population is demonstrably complete — auditors test population completeness first.

**Qualified opinion** — An auditor's opinion that the subject matter is fairly presented *except for* specified matters. In SOC reports, qualification usually means one or more control objectives/criteria were not met.

**RACI** — Responsibility-assignment scheme: Responsible (does the work), Accountable (answers for the outcome — exactly one), Consulted, Informed. Used to pin control and process ownership.

**Residual risk** — Risk remaining after controls and other treatments are applied. This is what gets compared against risk appetite and either accepted or further treated.

**Risk acceptance** — A documented, authorized decision to take no further treatment of a specific risk, made by an owner with authority commensurate to the exposure, with an expiry or review date. Silence is not acceptance.

**Risk appetite** — The amount and type of risk an organization is willing to pursue or retain in aggregate, set by governing bodies and expressed in statements measurable enough to steer decisions.

**Risk assessment** — The process of identifying, analyzing, and evaluating risk against criteria. Output feeds treatment decisions and the risk register. See the risk-assessment skill and [risk-scoring.md](risk-scoring.md).

**Risk owner** — The person or entity with the accountability and authority to manage a specific risk, including choosing and resourcing its treatment. Should sit in the business, not default to the security team.

**Risk register** — The living inventory of identified risks with their analysis (inherent/residual ratings), owners, treatments, and review dates. Useful only if actively maintained and tied to decisions.

**Risk tolerance** — The acceptable variation around specific objectives or risk levels — operational thresholds (e.g., "no more than X hours unplanned downtime per quarter") that make appetite actionable.

**Risk transfer (sharing)** — Shifting part of a risk's financial consequence to another party, e.g., via insurance or contract. Liability and reputational impact are rarely fully transferable; regulatory accountability generally is not.

**Risk treatment** — The chosen response to a risk: mitigate (apply controls), transfer/share, avoid (stop the activity), or accept. ISO 27001 requires a risk treatment plan linking treatments to selected controls.

**RoPA (Record of Processing Activities)** — The GDPR Art. 30 inventory of processing activities: purposes, data categories, recipients, transfers, retention, and security measures. Foundational input to DPIAs and breach response.

**Root cause analysis** — Structured determination of why a failure occurred (not just what failed), so remediation addresses cause rather than symptom. Expected for repeat findings and significant incidents.

**Sampling** — Testing a subset of a population to conclude about the whole. Methods: statistical or judgmental (haphazard/targeted); sample sizes scale with control frequency and risk. Invalid without a complete population and a defined selection method.

**Scope** — The defined boundary of a system, assessment, or certification: locations, systems, services, data, and organizational units included. Most compliance disputes trace back to scope ambiguity; PCI segmentation and ISO 27001 ISMS boundaries are scope exercises.

**Significant deficiency** — An ICFR deficiency less severe than a material weakness but important enough to merit attention by those charged with governance (e.g., the audit committee).

**SoA (Statement of Applicability)** — The ISO 27001 document listing every Annex A control with its applicability, justification for inclusion or exclusion, and implementation status. The certification auditor's map of your control landscape.

**SoD (Segregation of Duties)** — Dividing conflicting duties (e.g., request vs. approve access; develop vs. deploy code) among different people or systems so no individual can both commit and conceal an error or fraud. Where headcount prevents it, apply compensating controls such as enhanced review.

**Subservice organization** — A vendor used by a service organization to perform services relevant to the service organization's own SOC-reported system (e.g., the cloud provider under a SaaS vendor). See carve-out vs. inclusive.

**Threat** — A potential cause of an unwanted incident — an actor, event, or condition capable of exploiting a vulnerability. Pairs with vulnerability and impact in most risk models.

**TPRM (Third-Party Risk Management)** — The lifecycle discipline of managing risk from vendors and other third parties: inherent-risk tiering, due diligence, contractual controls, ongoing monitoring, and termination/exit. See the third-party-risk-assessment skill.

**Vulnerability** — A weakness in an asset or control that a threat can exploit. Broader than software CVEs: includes misconfigurations, process gaps, and people-related weaknesses.

**Walkthrough** — Tracing a single transaction or control instance end-to-end with the people who perform it, to confirm understanding of design and identify where controls could fail. The standard method for testing design effectiveness.

**Workpaper** — The documented record of assessment work: what was tested, how, the evidence obtained, results, and conclusions — sufficient for an experienced reviewer with no prior connection to reperform the reasoning. If it isn't in the workpapers, it didn't happen.

## Related

- [risk-scoring.md](risk-scoring.md) — risk analysis methods behind the risk terms
- [crosswalks/framework-crosswalk.md](crosswalks/framework-crosswalk.md) — where these concepts appear across frameworks

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
