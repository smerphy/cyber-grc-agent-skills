# COSO Internal Control — Integrated Framework (2013) and COSO Enterprise Risk Management (2017)

## At a glance

| Attribute | Detail |
|---|---|
| Publisher | Committee of Sponsoring Organizations of the Treadway Commission (COSO) — a joint initiative of five sponsoring bodies: AAA, AICPA, FEI, IMA and The IIA |
| Internal control framework | *Internal Control — Integrated Framework* (ICIF): issued 1992, revised and reissued **May 2013**. The 1992 edition was superseded on **15 December 2014** |
| ERM framework | *Enterprise Risk Management — Integrated Framework* (2004), superseded by *Enterprise Risk Management — Integrating with Strategy and Performance* (**June 2017**) |
| Structure (ICIF-2013) | 3 objective categories (operations, reporting, compliance) × 5 components × 17 principles, each principle subdivided into points of focus (87 in total across the 17 principles) |
| Structure (ERM 2017) | 5 interrelated components × 20 principles, organised around mission/vision/core values → strategy development → business objective formulation → implementation and performance |
| Who uses it | Any entity; in practice the default internal-control framework for US public-company ICFR under SOX s404 and the backbone of the SOC 2 common criteria |
| Certifiable? | **No.** There is no COSO certification or attestation scheme for organisations. COSO licenses individual certificate programs (Internal Control, ERM, Fraud Risk Management) delivered through AICPA, IIA, FEI and IMA |
| Cost | Framework volumes are paid publications; the ICIF and ERM **Executive Summaries and the ICIF FAQ are free** from coso.org |
| Effectiveness test | All five components and all *relevant* principles **present and functioning**, and the five components **operating together** in an integrated manner. A major deficiency in any one defeats the conclusion |
| Status, September 2026 | ICIF-2013 and ERM-2017 both current; no refresh or exposure draft announced. Active supplemental output — GenAI guidance (Feb 2026), board-oversight principles (Mar 2026), practical-ERM paper (May 2026). A full Corporate Governance Framework remains in development after the July 2025 withdrawal of its draft |

## What it is

COSO was founded in 1985 by five accounting and auditing bodies, which together sponsored the National Commission on Fraudulent Financial Reporting — the Treadway Commission. The Commission's 1987 recommendations called for a workable internal-control framework, and COSO published the first ICIF in 1992 (with revisions through 1994). It publishes *thought leadership*, not regulation: its frameworks acquire force because regulators, standard setters and auditors adopt them by reference. ICIF-2013 defines internal control as "a process, effected by an entity's board of directors, management, and other personnel, designed to provide reasonable assurance regarding the achievement of objectives relating to operations, reporting, and compliance." Two words in that definition do the heavy lifting: *process* (a means, not an end) and *reasonable assurance* (never absolute).

The 2013 revision kept the 1992 definition and the five components intact. Its substantive change was to **formalise the 17 principles** that were previously implicit in the narrative, so that management can demonstrate coverage principle by principle rather than asserting effectiveness from prose. COSO's FAQ states the Framework *presumes* all 17 principles are relevant to all entities; a principle may be treated as not relevant only in a "rare industry, operating, or regulatory situation."

ERM-2017 is a separate framework with a different job. It is not a control framework: COSO's own guidance stresses that ERM "addresses more than internal control," extending to strategy-setting, governance, stakeholder communication and performance measurement, and that ERM "is not a function or department" but "the culture, capabilities, and practices that organizations integrate with strategy-setting." Security and GRC teams routinely need both: ICIF for the control-assertion machinery, ERM for how cyber risk enters strategic decision-making and board risk appetite.

## Who it covers / Scope

- **No statutory scope of its own.** COSO frameworks are voluntary. Obligation arises indirectly.
- **US public companies (ICFR).** Exchange Act Rule 13a-15(c) (17 CFR 240.13a-15(c)) requires management's annual ICFR evaluation to be based on "a suitable, recognized control framework that is established by a body or group that has followed due-process procedures, including the broad distribution of the framework for public comment." Regulation S-K Item 308 (17 CFR 229.308(a)(2)) requires the annual report to **name** the framework used. The SEC does not mandate COSO, but COSO is the framework almost universally named. See [../regulations/sox-itgc.md](../regulations/sox-itgc.md).
- **Service organisations (SOC 2).** The AICPA 2017 Trust Services Criteria are built on the 17 COSO principles, so any SOC 2 examination inherits COSO scope at the entity level. See [soc2-tsc.md](soc2-tsc.md).
- **Everyone else by choice.** Non-listed entities, government bodies, not-for-profits and non-US issuers adopt ICIF for internal assurance; ICIF-2013 is explicitly scalable (entity, division, operating unit, function levels).
- **No exemption mechanism and no extraterritorial reach** — the question is never "does COSO apply?" but "which regime is requiring me to name a framework?"

## Structure and requirements

### ICIF-2013: five components and seventeen principles

Points-of-focus counts below are as tabulated in COSO's 2023 ICSR publication (figure credited to Protiviti); they total 87.

| Component | # | Principle (abridged) | Points of focus |
|---|---|---|---|
| Control Environment | 1 | Demonstrates commitment to integrity and ethical values | 4 |
| | 2 | Board demonstrates independence from management and exercises oversight | 4 |
| | 3 | Establishes structures, reporting lines, authorities and responsibilities | 3 |
| | 4 | Demonstrates commitment to attract, develop and retain competent individuals | 4 |
| | 5 | Holds individuals accountable for internal control responsibilities | 5 |
| Risk Assessment | 6 | Specifies objectives with sufficient clarity to enable risk identification | 15 |
| | 7 | Identifies and analyses risks to achievement of objectives across the entity | 5 |
| | 8 | Considers the potential for **fraud** in assessing risks | 4 |
| | 9 | Identifies and assesses **changes** that could significantly impact internal control | 3 |
| Control Activities | 10 | Selects and develops control activities that mitigate risks to acceptable levels | 6 |
| | 11 | Selects and develops **general control activities over technology** | 4 |
| | 12 | Deploys control activities through **policies and procedures** | 6 |
| Information & Communication | 13 | Obtains, generates and uses relevant, quality information | 5 |
| | 14 | **Internally** communicates objectives and internal control responsibilities | 4 |
| | 15 | Communicates with **external parties** on matters affecting internal control | 5 |
| Monitoring Activities | 16 | Performs ongoing and/or separate evaluations of components | 7 |
| | 17 | **Evaluates and communicates deficiencies** timely to those responsible for corrective action | 3 |

Principle 11 is the hook for the entire IT general control population — access, change management, operations — and principle 12 is the policy-and-procedure anchor the SOC 2 control-activities criteria build on. Principle 8 is the anchor for fraud risk assessment and the reason the COSO/ACFE Fraud Risk Management Guide exists.

Points of focus are **not** a checklist: COSO's FAQ says the Framework "neither prescribes a process for assessing the effectiveness of a system of internal control nor requires that management assess separately whether points of focus are in place," and some may be neither suitable nor relevant to a given entity. The assessable unit is the principle.

### ICIF-2013: what "effective" means

| Requirement | Test |
|---|---|
| Present | The component/relevant principle exists in the **design and implementation** of the system |
| Functioning | The component/relevant principle **continues to exist in operation and conduct** |
| Operating together | All five components **collectively** reduce the risk of not achieving an objective to an acceptable level |
| Major deficiency | A deficiency (or aggregation of deficiencies) severe enough that a component or relevant principle is not present and functioning, or the components are not operating together — precludes a conclusion of effectiveness |

COSO deliberately does **not** define "material weakness" or "significant deficiency": the FAQ notes that entities subject to SEC rules use the SEC's classifications for external financial-reporting deficiencies, while others may use COSO's own severity terminology.

### ERM-2017: five components and twenty principles

| Component | Principles |
|---|---|
| Governance and Culture | 1 Exercises board risk oversight · 2 Establishes operating structures · 3 Defines desired culture · 4 Demonstrates commitment to core values · 5 Attracts, develops and retains capable individuals |
| Strategy and Objective-Setting | 6 Analyses business context · 7 Defines risk appetite · 8 Evaluates alternative strategies · 9 Formulates business objectives |
| Performance | 10 Identifies risk · 11 Assesses severity of risk · 12 Prioritises risks · 13 Implements risk responses · 14 Develops portfolio view |
| Review and Revision | 15 Assesses substantial change · 16 Reviews risk and performance · 17 Pursues improvement in enterprise risk management |
| Information, Communication and Reporting | 18 Leverages information systems · 19 Communicates risk information · 20 Reports on risk, culture and performance |

Principle 7 (risk appetite) and principle 14 (portfolio view) are the two most commonly missing in cyber programmes: an appetite statement that cannot be tested against an aggregated risk position is decorative. See [../risk-scoring.md](../risk-scoring.md) and [../../templates/risk-register-guide.md](../../templates/risk-register-guide.md).

### Supplemental and topic guidance (applies one of the two frameworks to a domain)

| Publication | Year | Base framework |
|---|---|---|
| Guidance on Monitoring Internal Control Systems | 2009 | ICIF |
| COSO in the Cyber Age (Governance and Internal Control) | Jan 2015 | ICIF |
| Fraud Risk Management Guide (with ACFE) | 2016; 2nd edition 2 May 2023 | ICIF (principle 8) |
| Managing Cyber Risk in a Digital Age (Governance and Enterprise Risk Management) | 2019 | ERM |
| Blockchain and Internal Control: The COSO Perspective | 2020 | ICIF |
| Compliance Risk Management: Applying the COSO ERM Framework | 2020 | ERM |
| Risk Appetite — Critical to Success | 2020 | ERM |
| Enterprise Risk Management for Cloud Computing | 2021 | ERM |
| Realize the Full Potential of Artificial Intelligence | Sept 2021 | ERM |
| Achieving Effective Internal Control Over Sustainability Reporting (ICSR) | Mar 2023 | ICIF |
| Alternative Data: The COSO Perspective | Mar 2024 | ERM |
| Achieving Effective Internal Control Over Robotic Process Automation | Dec 2024 | ICIF |
| Achieving Effective Internal Control Over Generative AI | Feb 2026 | ICIF |
| Corporate Governance: Guiding Principles for Board Oversight (with PwC) — twelve guiding principles | Mar 2026 | Governance |
| From Guidance to Action: Exploring Practical Enterprise Risk Management | May 2026 | ERM |

## Assessment, certification and evidence

- **There is no COSO certificate for an organisation.** Assurance comes through the regime that referenced COSO — a SOX s404(b) auditor attestation, a SOC 2 report, an internal-audit opinion — not from COSO.
- **Individual certificates** (Internal Control, ERM, Fraud Risk Management) are sold through AICPA, IIA, FEI and IMA; they evidence practitioner competence, not entity conformance.
- **Evidence model** is principle-by-principle: for each of the 17, a documented mapping to the controls that effect it, the evidence that each control operated, and a deficiency log rolled up to a component-level and entity-level conclusion. COSO's Illustrative Tools and the ICEFR Compendium support this. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md) and [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).
- **Entity-level vs process-level.** Components 1, 4 and 5 (control environment, information and communication, monitoring) are mostly entity-level and rarely carry sampled evidence; components 2 and 3 (risk assessment, control activities) carry the transactional and ITGC testing population.
- **Deficiency aggregation is the hard part.** Individually minor ITGC failures that together mean principle 11 is not functioning produce a major deficiency; track aggregation explicitly rather than closing findings one at a time. See [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).

## Timeline and status

| Date | Event |
|---|---|
| 1992 | ICIF first issued |
| 2004 | ERM — Integrated Framework issued |
| May 2013 | ICIF revised and reissued with 17 explicit principles; ICIF FAQ published |
| 15 Dec 2014 | 1992 ICIF (and the 2006 smaller-public-company guidance) formally superseded; entities using ICIF for external reporting during the transition had to disclose which edition they used |
| June 2017 | ERM — Integrating with Strategy and Performance replaces the 2004 ERM framework |
| 2 May 2023 | Fraud Risk Management Guide, 2nd edition (COSO/ACFE) |
| 31 Jan 2024 / 21 May 2024 | RFP, then award to PwC US (with NACD), for development of a Corporate Governance Framework |
| 15 July 2025 | Draft Corporate Governance Framework **withdrawn from public comment**, citing extensive feedback and a shifting US regulatory landscape |
| 23 Feb 2026 | *Achieving Effective Internal Control Over Generative AI* released |
| 31 Mar 2026 | *Corporate Governance: Guiding Principles for Board Oversight* released with PwC — twelve guiding principles, released after the July 2025 withdrawal of the draft Corporate Governance Framework |
| 4 May 2026 | *From Guidance to Action: Exploring Practical Enterprise Risk Management* released |
| 18 May 2026 | COSO opened the search for its next Board Chair; Lucia Wind steps down on 31 Dec 2026, successor's three-year term begins 1 Jan 2027 |
| As of Sept 2026 | ICIF-2013 and ERM-2017 remain the current editions; no successor edition or exposure draft appears on COSO's guidance or news pages. **Pending:** a revised Corporate Governance Framework — COSO's about page still lists it as an active workstream, with no reissued draft or comment period announced |

## Key obligations for security/GRC teams

1. **Name your framework and mean it.** If the entity files a s404 management report, the framework named must be the one actually used; keep the principle-level mapping that substantiates the name. See [../regulations/sox-itgc.md](../regulations/sox-itgc.md).
2. **Map security controls to principle 11 (general technology controls) and principle 12 (policies)** before mapping anything else — that is where cyber evidence is consumed by the ICFR opinion. See [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).
3. **Treat all 17 principles as relevant by default.** Non-relevance is a documented, rare, defensible judgement — not a scoping convenience.
4. **Run the cyber risk register into the ERM portfolio view** (ERM principles 10–14) rather than maintaining a parallel taxonomy, so cyber risk is ranked against the risks the board already discusses. See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).
5. **Define and test a cyber risk appetite** against ERM principle 7 — expressed in measurable terms that a metric can breach, and reviewed with strategy, not annually in isolation.
6. **Wire fraud risk into the security risk assessment** (ICIF principle 8): insider misuse, payment-diversion and deepfake-enabled social engineering belong in the fraud risk assessment as well as the cyber register.
7. **Bring GenAI and automation under the existing control set.** COSO's Feb 2026 GenAI guidance and Dec 2024 RPA guidance both extend ICIF-2013 rather than replacing it; reuse the principle structure instead of building a standalone AI control framework. See [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md), [nist-ai-rmf.md](nist-ai-rmf.md) and [iso-42001-ai-management.md](iso-42001-ai-management.md).
8. **Report to the board against principles 2, 16 and 17** — oversight, monitoring, and timely deficiency communication. Deficiency ageing and aggregation are board content, not just audit content. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md) and [../../templates/grc-board-report.md](../../templates/grc-board-report.md).
9. **Keep policy architecture aligned to principle 12** — every policy traceable to the risk it addresses and the procedure that enacts it. See [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).

## Interplay

- **SOX / ICFR** — COSO supplies the criteria; the SEC supplies the obligation to use *a* suitable, recognised framework and to identify it (17 CFR 229.308(a)(2)), and requires an external auditor's ICFR attestation for accelerated and large accelerated filers that are not emerging growth companies (17 CFR 229.308(a)(4) and (b)). See [../regulations/sox-itgc.md](../regulations/sox-itgc.md) and [../regulations/sec-cyber-disclosure.md](../regulations/sec-cyber-disclosure.md).
- **SOC 2** — the 2017 Trust Services Criteria carry the 17 COSO principles as common criteria CC1–CC5, then add supplemental criteria CC6–CC9 (logical and physical access, system operations, change management, risk mitigation) that the TSC treats as an extension of the control-activities component *(the AICPA criteria document sits behind a free-account gate and was not retrieved; verify the exact principle attribution against it) (verify)*. A clean COSO entity-level story materially shortens CC1–CC5 readiness. See [soc2-tsc.md](soc2-tsc.md) and [../../skills/soc2-readiness/SKILL.md](../../skills/soc2-readiness/SKILL.md).
- **ISO 31000** — a parallel, non-competing risk-management standard: ISO 31000 is principles/framework/process oriented and certification-free; COSO ERM is strategy-and-performance oriented and reporting-lineage. Running both is common; reconcile vocabulary once, in the glossary, rather than per assessment. See [iso-31000-27005-risk-management.md](iso-31000-27005-risk-management.md) and [../glossary.md](../glossary.md).
- **NIST CSF 2.0 / ISO 27001** — control frameworks that sit *inside* COSO principle 11, supplying the technical depth ICIF deliberately omits. Map CSF Govern-function outcomes to COSO components 1 and 5 to avoid duplicated governance evidence. See [nist-csf-2.md](nist-csf-2.md), [iso-27001-2022.md](iso-27001-2022.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
- **Three Lines Model** — The IIA replaced its 2013 "Three Lines of Defense" position paper with the **Three Lines Model** (position paper dated 8 September 2020, refreshed September 2024 to match the Global Internal Audit Standards glossary), dropping "defense" and reframing the six principles around value creation as well as protection. COSO's own thought paper *Leveraging COSO Across the Three Lines of Defense* still carries the older "defense" vocabulary in its title — align terminology deliberately when quoting either. See [iia-global-internal-audit-standards.md](iia-global-internal-audit-standards.md).
- **COBIT 2019** — the governance-and-management framework for enterprise IT that most directly operationalises COSO principle 11; COSO states the control objective, COBIT supplies the IT process model and maturity scale. See [cobit-2019.md](cobit-2019.md).
- **EU AI Act and AI management systems** — COSO's GenAI and AI papers are control-design guidance, not conformity evidence; they do not discharge AI Act obligations. See [../regulations/eu-ai-act.md](../regulations/eu-ai-act.md).

## Primary sources

- COSO, *Internal Control — Integrated Framework: Executive Summary* (May 2013) — definition, objective categories, five components, seventeen principles, effectiveness requirements: https://www.coso.org/_files/ugd/3059fc_1df7d5dd38074006bce8fdf621a942cf.pdf
- COSO, *Internal Control — Integrated Framework: Frequently Asked Questions* (May 2013) — relevance presumption for the 17 principles, role of points of focus, deficiency classification and the deferral to SEC criteria: https://www.coso.org/_files/ugd/3059fc_8fdac5b8011e4cd08d566bf40b1ac2a8.pdf
- COSO, *Enterprise Risk Management — Integrating with Strategy and Performance: Executive Summary* (June 2017) — five components, twenty principles, ERM misconceptions: https://www.coso.org/_files/ugd/3059fc_61ea5985b03c4293960642fdce408eaa.pdf
- COSO, *Achieving Effective Internal Control Over Sustainability Reporting (ICSR)* (2023) — Appendix B tabulation of principles and points-of-focus counts (Figure B-4, credited to Protiviti) and COSO's own founding history: https://www.coso.org/_files/ugd/3059fc_5949d4d5f3f74e2ea9ee11ce4b68b603.pdf
- COSO, *The 2013 COSO Framework & SOX Compliance: One Approach to an Effective Transition* (2013) — 15 December 2014 supersession and the transition-period disclosure expectation: https://www.coso.org/_files/ugd/3059fc_9e167c6fc9c745059baabee54670e1e8.pdf
- COSO, *COSO in the Cyber Age* (January 2015) — confirms the paper applies the 2013 ICIF, not the ERM framework: https://www.coso.org/_files/ugd/3059fc_9af90248e5a34ae3addd148d256107c0.pdf
- COSO, *Achieving Effective Internal Control Over Generative AI* (February 2026): https://www.coso.org/_files/ugd/719ba0_08f358f2c8f946fa9d26bd51d37b7117.pdf
- COSO guidance and programme indexes — publication inventory, dates and certificate providers: https://www.coso.org/guidance-on-ic , https://www.coso.org/guidance-erm , https://www.coso.org/governance , https://www.coso.org/fraud-deterrence , https://www.coso.org/about-us , https://www.coso.org/ic-certificate
- COSO news index (dated release list, checked September 2026): https://www.coso.org/news — with the individual releases at https://www.coso.org/generative-ai (23 Feb 2026), https://www.coso.org/corporate-governance-guiding-principles (31 Mar 2026), https://www.coso.org/new-erm-guidance (4 May 2026), https://www.coso.org/coso-announces-search-for-new-board-chair (18 May 2026) and https://www.coso.org/cgf-exposure-comment-period-end (15 July 2025)
- eCFR, 17 CFR 240.13a-15(c) — the "suitable, recognized control framework ... followed due-process procedures, including the broad distribution of the framework for public comment" requirement: https://www.ecfr.gov/current/title-17/section-240.13a-15
- eCFR, 17 CFR 229.308 (Item 308) — the obligation to identify the framework used, and the auditor attestation requirement for accelerated and large accelerated filers other than emerging growth companies: https://www.ecfr.gov/current/title-17/section-229.308
- The IIA, *The IIA's Three Lines Model: An update of the Three Lines of Defense*, position paper dated 8 September 2020, refreshed September 2024: https://www.theiia.org/en/content/position-papers/2020/the-iias-three-lines-model-an-update-of-the-three-lines-of-defense/
- AICPA & CIMA, *2017 Trust Services Criteria (with revised points of focus — 2022)* — alignment to the 17 COSO principles and the supplemental criteria. **Publisher page reachable, but the criteria document itself sits behind a free-account gate and was not retrieved:** https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
