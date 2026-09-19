# UK Financial Sector Operational Resilience (FCA SYSC 15A / PRA Operational Resilience Parts, SS2/21, PS26/2 & PS7/26, Critical Third Parties regime)

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | FCA Handbook SYSC 15A (operational resilience), SYSC 8 (outsourcing), SUP 15 (notifications); PRA Rulebook Operational Resilience Parts (CRR firms; Insurance – Operational Resilience), Notifications Part, with PRA SS1/21 and SS2/21; FSMA 2000 Part 18 Chapter 3C (ss. 312L–312V, inserted by FSMA 2023 s. 18) for critical third parties (CTPs); the Critical Third Parties (Designation) Regulations 2026 (SI 2026/777) |
| Regulators | FCA (conduct, all authorised firms), PRA (prudential: banks, building societies, PRA-designated investment firms, insurers), Bank of England (FMIs); the three jointly oversee CTPs; HM Treasury designates CTPs |
| Status and key dates | Operational resilience rules in force 31 March 2022; impact-tolerance compliance deadline 31 March 2025 (passed); SS2/21 current version effective 31 December 2024; CTP rules in force 1 January 2025; first four CTPs designated with effect from 13 July 2026; operational incident and material third-party (MTP) reporting rules (FCA PS26/2, PRA PS7/26) published 18 March 2026, in force 18 March 2027 |
| Who is covered | Operational resilience: banks, building societies, PRA-designated investment firms, Solvency II firms, enhanced-scope SM&CR firms, UK RIEs, e-money and payment institutions, RAISPs, consolidated tape providers. Incident reporting from 2027: all firms with Part 4A permission, PSPs, UK RIEs, trade repositories, credit rating agencies. CTPs: designated technology/service providers |
| Structure | Three layers: (1) firm-level operational resilience (important business services, impact tolerances, mapping, scenario testing, self-assessment); (2) outsourcing/third-party risk management and, from 2027, structured incident and MTP reporting; (3) direct regulatory oversight of designated CTPs |
| Incident clocks (from 18 March 2027) | Initial report as soon as practicable and at most 24 hours after determining a reporting threshold is met (PSPs keep the 4-hours-from-detection rule); enhanced-reporting firms update at the intermediate phase and finalise within 30 working days of resolution (60 working days absolute limit) |
| Penalties / enforcement | FSMA s. 206: financial penalty "of such amount as [the regulator] considers appropriate" (no statutory cap); own-initiative requirements (ss. 55J/55L); public censure. CTPs: censure (s. 312Q) and prohibition/conditions on providing or receiving services (s. 312R). Precedent: TSB fined £48.65m by FCA and PRA (December 2022) for IT-migration and outsourcing-risk failures |
| Certifiable? | No. Supervisory regime evidenced by a board-approved written self-assessment (retained 6 years under SYSC 15A.6.2R), regulatory returns and supervisory review; intelligence-led testing via CBEST / STAR-FS where requested |
| Relationship to neighbours | UK analogue of DORA but principles-based and spread across rulebooks; UK–EU regulators signed a CTP/CTPP oversight MoU on 14 January 2026; incident templates aligned with the FSB FIRE format |

## What it is

The UK has no single operational-resilience statute for financial services. The FCA, PRA and Bank of England instead built a shared policy framework in stages. The first stage (FCA PS21/3, PRA PS6/21 and SS1/21, both March 2021) requires firms to identify **important business services (IBS)**, set an **impact tolerance** for each, and prove through mapping and scenario testing that they can stay within tolerance in "severe but plausible" disruption. Rules took effect on 31 March 2022, with a hard deadline of 31 March 2025 to have completed the mapping, testing and investment needed to operate within tolerance. Since that date the PRA describes maintaining operational resilience as "a dynamic activity" rather than a project.

The second stage covers dependencies. PRA SS2/21 (outsourcing and third-party risk management, implementing the EBA Outsourcing Guidelines in the UK) and FCA SYSC 8 govern outsourcing; from 18 March 2027 a single cross-regulator regime (FCA PS26/2, PRA PS7/26, plus the Bank's FMI equivalent) adds structured **operational incident reporting** and **material third-party notifications and an annual register**. The third stage reaches beyond the regulated perimeter: the Financial Services and Markets Act 2023 inserted ss. 312L–312V into FSMA 2000, letting HM Treasury designate **critical third parties** and giving the regulators rule-making, direction, information-gathering and disciplinary powers over them. Rules for CTPs took effect on 1 January 2025 and bit for the first time when four cloud providers were designated with effect from 13 July 2026.

The regime is outcomes-focused: no fixed recovery-time numbers, no prescribed incident taxonomy thresholds, and materiality left to firm judgement backed by supervisory challenge. That makes documented rationale — why a service is or is not an IBS, why a tolerance was set where it was, why an arrangement is or is not material — the core compliance artefact.

## Who it covers / Scope

| Layer | FCA scope | PRA scope | Notes |
|---|---|---|---|
| Operational resilience (SYSC 15A / Operational Resilience Parts) | Enhanced-scope SM&CR firms, banks, designated investment firms, building societies, Solvency II firms, UK RIEs, EMIs, PIs, RAISPs, consolidated tape providers (SYSC 15A.1.1R) | UK banks, building societies, PRA-designated investment firms, Solvency II firms, Society of Lloyd's and managing agents (SS1/21) | Not applicable to firms whose registered/head office is outside the UK (SYSC 15A.1.4R) or to temporary-permission firms (15A.1.3R); otherwise no territorial limitation (15A.1.9R). For PIs/EMIs it applies only to payment/e-money activity (15A.1.8R) |
| Outsourcing / third-party risk (SYSC 8; SS2/21) | Common-platform firms and others under SYSC 8.1 (critical or important operational functions defined in SYSC 8.1.4R/4AR) | Banks, building societies, PRA-designated investment firms, Solvency II insurers and groups, third-country branches; parts apply to credit unions and non-directive firms | SS2/21 treats "material outsourcing" as encompassing "critical or important" outsourcing |
| Operational incident reporting (from 18 March 2027) | All firms with Part 4A permission, PSPs, UK RIEs, registered trade repositories, registered credit rating agencies | PRA-regulated firms including credit unions | PSPs and CRAs are subsumed into the single regime; a dual-regulated firm makes one submission |
| MTP notifications and register (from 18 March 2027) | Enhanced-scope SM&CR firms, banks, designated investment firms, building societies, Solvency II firms, CASS large firms, UK RIEs, authorised EMIs/PIs, consolidated tape providers | Same prudential population; credit unions only if total assets are at least £50m | Third-country branches: register yes, notifications no (FCA shares branch registers with the PRA). Intragroup arrangements in scope only where there is an external third-party dependency (ring-fenced bodies excepted) |
| CTP regime (FSMA ss. 312L–312V) | Any person providing services to authorised persons, PSPs/EMIs or FMI entities, designated by HM Treasury where failure or disruption "could threaten the stability of, or confidence in, the UK financial system" (s. 312L(2)) | Same | HMT must weigh materiality of the services to essential activities and the number and type of firms served (s. 312L(3)), consult the regulators and give the provider a right to make representations (s. 312L(4)). The Bank of England cannot be designated (s. 312L(5)) |

## Core obligations

### 1. Operational resilience of important business services

FCA rules (SYSC 15A) and PRA rules (Operational Resilience Parts, rule numbers per SS1/21 footnotes) are deliberately parallel.

| Requirement | FCA rule | PRA rule | What it requires |
|---|---|---|---|
| Identify IBS | SYSC 15A.2.1R; factors 15A.2.4G | Operational Resilience 2.2 | Treat each distinct service separately; factors include client vulnerability, substitutability, time criticality, data sensitivity, potential to inhibit the UK financial system. Review on material change and at least every year (15A.2.2R) |
| Set impact tolerances | SYSC 15A.2.5R; factors 15A.2.7G | 2.3–2.4 | One tolerance per IBS, reflecting peak demand (15A.2.8G); dual-regulated firms set both an FCA (consumer/market harm) and a PRA (safety and soundness / financial stability) tolerance |
| Remain within tolerance | SYSC 15A.2.9R | 2.5–2.6 | Firm must be able to remain within tolerance in a severe but plausible disruption. Failure to meet a tolerance is expected to be notified under Principle 11 (15A.2.11G) |
| Strategies, processes, systems | SYSC 15A.3.1R–3.2R | — | Sound, effective, comprehensive and proportionate |
| Mapping | SYSC 15A.4.1R | 4.1 | Identify and document the people, processes, technology, facilities and information for each IBS, sufficient to find and remedy vulnerabilities; includes third-party-delivered components (15A.4.2G) |
| Scenario testing | SYSC 15A.5.1R–5.7R | 5.1 | Maintain a testing plan; test each IBS against adverse circumstances of varying nature, severity and duration; suggested scenarios include data corruption, loss of facilities or key people, loss of critical third-party services, disruption to other market participants and loss of technology (15A.5.6G). Retest after material change, after improvements and on a regular basis |
| Lessons learned | SYSC 15A.5.8R–5.9R | — | After every test and every operational disruption; remediate identified weaknesses |
| Self-assessment | SYSC 15A.6.1R–6.2R | 6.1 | Written record covering IBS and justification, tolerances and justification, mapping approach, testing plan and results, lessons learned, vulnerabilities with remediation timelines, communication strategy and methodologies. Retain each version for at least 6 years and provide on request |
| Governance | SYSC 15A.7.1R | 7 | Governing body / board approves and regularly reviews the self-assessment (PRA: board approves IBS, tolerances and self-assessment; SS1/21 ch. 7) |
| Communications | SYSC 15A.8.1R–8.3R | — | Internal and external communication strategy, including warnings to clients where no direct channel exists |

### 2. Outsourcing and third-party risk management (PRA SS2/21; FCA SYSC 8)

- **Definitions.** "Outsourcing" is an arrangement under which a service provider performs a process, service or activity the firm would otherwise undertake itself (SS2/21 para 2.1). "Material outsourcing" is outsourcing of services whose weakness or failure "would cast serious doubt upon the firm's continuing satisfaction of the threshold conditions or compliance with the Fundamental Rules" (para 5.2); the materiality criteria apply to non-outsourcing third-party arrangements too (para 5.6).
- **Notification.** Notifications 2.3(1)(e) requires PRA firms, including credit unions and non-directive firms, to notify the PRA when entering or significantly changing a material outsourcing arrangement; the PRA expects notification before entering the arrangement (para 5.14).
- **Chapters 6–10** set expectations for outsourcing agreements, data security, access/audit/information rights (including pooled audits and third-party certifications), sub-outsourcing, and business continuity and exit plans covering both stressed and non-stressed exit. Firms are expected to keep an **Outsourcing Register** of all arrangements distinguishing material from non-material (the earlier Cloud Register was subsumed by 31 December 2021).
- **Cloud.** SS2/21 adopts a shared-responsibility model (the firm is responsible for what is in the cloud; the provider for the cloud itself) and cross-refers to FCA FG16/5 on cloud and third-party IT outsourcing.
- **Versions.** Current SS2/21 published 15 November 2024 (effective 31 December 2024, after PS15/24 restating Solvency II law); a revised version published 18 March 2026 takes effect 18 March 2027 alongside the MTP reporting rules, recasting "material outsourcing" language around **material third-party arrangements**.

### 3. Operational incident and material third-party reporting (in force 18 March 2027)

Published 18 March 2026 as FCA PS26/2 (with FG26/3 incident guidance and FG26/4 MTP guidance) and PRA PS7/26 (with new SS1/26 on incident reporting and amended Notifications and Reporting Parts). One definition, one portal (FCA Connect for incidents and notifications; FCA RegData for the register) and one submission for dual-regulated firms.

| Element | Detail |
|---|---|
| Reporting thresholds | FCA (SUP 15.18.6R(1)): consumer harm (intolerable harm consumers cannot easily recover from), market integrity (risk to market stability, integrity or confidence), safety and soundness. PRA: safety and soundness, financial stability, and (insurers) policyholder protection. Near misses and uncrystallised events are not reportable; the assessment is made on information available at the time |
| Standard vs enhanced | Standard reporting (c. 90% of FCA firms): a single short report, no updates required. Enhanced reporting (firms listed in SUP 15.18.3R): one form updated through initial, intermediate and final phases |
| Initial phase | As soon as practicable, expected at most 24 hours after determining a threshold is met — but "firms should not wait 24 hours". PSPs retain the existing requirement to report within 4 hours of first detecting an incident |
| Intermediate phase | Material updates only (high bar), including a change that brings the incident within the other regulator's thresholds |
| Final phase | Within 30 working days of resolution; if impossible, as soon as practicable and no later than 60 working days |
| Data model | Fields aligned to the FSB FIRE format (final report April 2025); firms select which regulator's criteria were triggered |
| Governance (PRA) | SS1/26 expects the Chief Operations function (SMF24) to hold overall responsibility for incident-reporting outcomes, or another clearly allocated SMF |
| MTP definition (FCA) | A third-party arrangement whose disruption or failure could cause intolerable harm to clients, pose a risk to the UK financial system, or cast serious doubt on threshold conditions, Principles or SYSC 15A compliance. No monetary threshold; not limited to arrangements supporting an IBS |
| MTP notification | SUP 15.19 (FCA) / Notifications Part rule 2.3B (PRA): notify new MTP arrangements and significant changes (scope, data handling or location, ownership, key sub-contractor) at an early stage, before contractual or operational commitment. No prescribed lead time; the FCA does not approve notifications |
| MTP register | SUP 16.33 (FCA) / PRA Reporting Part: structured register of all MTP arrangements submitted annually via RegData in a common template; 90 calendar days to submit once the annual window opens. Replaces the PRA's BEEDS collection |
| Review | Regulators commit to review the policy two years after implementation |

### 4. Notification duties that apply today

- **SUP 15.3.1R** — notify the FCA immediately of any matter that could affect the firm's ability to continue to provide adequate services to customers with serious detriment, could have significant adverse reputational impact, or could have serious financial consequences for the UK financial system.
- **SUP 15.3.17R** — immediate notification of significant fraud, errors and irregularities.
- **Principle 11 / PRA Fundamental Rule 7** — open and cooperative dealing with regulators; the FCA expects to be told of any failure to meet an impact tolerance (SYSC 15A.2.11G).
- **PSPs** — existing major-incident reporting under the Payment Services Regulations 2017 (SUP 15.14), which the 2027 regime subsumes.

### 5. Critical third parties regime (FSMA 2000 ss. 312L–312V; regulators' CTP rules)

| Provision | Effect |
|---|---|
| s. 312L | HMT designation by regulations; test and factors as above; regulators consulted |
| s. 312M | FCA, PRA and Bank may make rules imposing duties on CTPs in connection with services to firms and FMIs |
| s. 312N–312O | Power of direction (with immunity from damages where the direction addresses a threat to financial stability); notice and Tribunal procedure |
| s. 312P | Information gathering, skilled-person reports (ss. 166/166A), investigations and entry under warrant applied to CTPs and connected persons |
| s. 312Q–312S | Public censure; disciplinary notices prohibiting or conditioning the CTP's provision of services or firms' receipt of them; warning/decision notices and Tribunal referral |
| s. 312T–312V | Statement of policy on discipline; duty of regulator coordination; published MoU reviewed annually |

The regulators' rules (PRA PS16/24; Bank FMI Rulebook CTP Instrument 2024; FCA instrument 2024/41; SS6/24 on compliance and SS7/24 on skilled persons) took effect on 1 January 2025 and apply once a provider is designated. Core content (rule references from the Bank's FMI Rulebook instrument; the PRA and FCA instruments were published jointly with it):

| Rule area | Requirement |
|---|---|
| CTP Fundamental Rules 1–6 | Integrity; due skill, care and diligence; prudence; effective risk strategies and systems; organise and control affairs responsibly; open and cooperative dealing with each regulator |
| Requirements 1–8 (ch. 4) | Governance (named central points of contact); risk management; dependency and supply-chain risk; technology and cyber resilience; change management; mapping of resources supporting each systemic third-party service within 12 months of designation; incident management including a maximum tolerable level of disruption per service and an incident management playbook within 12 months; termination and exit of a systemic service |
| Assurance (ch. 5) | Regular scenario testing against severe but plausible disruption; playbook exercise with a representative sample of firms within 12 months of designation and at least biennially thereafter, with a report to the regulators |
| Self-assessment (ch. 6) | Interim self-assessment within 3 months of designation, then annually; retained for at least 3 years |
| Information sharing (ch. 7) | Provide firms with testing results, the redacted annual self-assessment and the maximum tolerable level of disruption for each service |
| Incident reporting (ch. 8) | Initial report as soon as practicable to regulators and affected firms; intermediate reports on significant change; final report within a reasonable time of resolution |
| Skilled persons (ch. 12) | CTP pays the fee where a regulator appoints a skilled person |

Designation is not authorisation, oversight is limited to the systemic services supplied to the UK financial sector, and — stated by HMT, the Bank and the FCA alike — it does not reduce firms' own third-party risk obligations.

### 6. Supervisory cyber testing

- **CBEST** (since 2014): intelligence-led penetration testing of live production systems supporting IBS, run by the PRA/FCA/Bank on regulator request as part of the supervisory cycle, at a firm's request with regulator agreement, or after an incident. Four phases — Initiation (~6 weeks), Threat Intelligence (~10 weeks), Penetration Testing (~14 weeks), Closure (~4 weeks) — averaging 9–12 months; providers must be CREST-accredited with certified threat-intelligence and red-team managers; findings feed a regulator-supervised remediation plan. An annual CBEST thematic is published (2023, 2024, 2025 editions).
- **STAR-FS**: a lighter threat-intelligence-led test for firms' IBS with reduced regulatory and firm effort; **CQUEST**: a further supervisory cyber-assessment tool listed by the Bank. These are supervisory tools, not standing obligations with a fixed frequency.

## Enforcement and penalties

- **Firms.** FSMA s. 206 allows the FCA or PRA to impose a penalty "of such amount as it considers appropriate" for contravening a relevant requirement; there is no statutory ceiling. The FCA may also use own-initiative powers (ss. 55J/55L) to require specific remedial steps where a firm disputes individual guidance on SYSC 15A (SYSC 15A.9.3G). Senior-manager accountability under SM&CR attaches to the SMF holding operational resilience responsibility (PRA: SMF24 for incident reporting outcomes).
- **Precedent.** TSB Bank (20 December 2022): FCA £29.75m and PRA £18.9m (total £48.65m after a 30% settlement discount; £69.5m otherwise) for failing to organise and control its 2018 IT migration and to manage outsourcing risk with its critical supplier; 5.2 million customers affected and £32.7m redress paid.
- **CTPs.** Censure (s. 312Q) and, if it would not itself threaten financial stability, prohibition or conditions on providing services to, or receipt by, UK firms and FMIs (s. 312R); breach of such a notice is itself a contravention. Skilled-person and investigation powers apply (s. 312P). Enforcement policy sits in the regulators' statements of policy.

## Timeline and status

| Date | Event |
|---|---|
| 29 March 2021 | FCA PS21/3, PRA PS6/21 (SS1/21) and PS7/21 (SS2/21) published |
| 31 March 2022 | SYSC 15A and the PRA Operational Resilience Parts in force; IBS and tolerances identified; SS1/21 March 2022 version effective (after PS2/22) |
| 29 August 2023 | FSMA 2000 Part 18 Ch. 3C (CTP powers) in force (FSMA 2023 s. 18) |
| 5 April 2024 | SYSC 15A extended to consolidated tape providers |
| November 2024 | PS16/24: CTP rules, SS6/24, SS7/24 and oversight approach published; SS2/21 updated (effective 31 December 2024) |
| 1 January 2025 | CTP rules in force (apply on designation) |
| 31 March 2025 | Deadline to be able to remain within impact tolerances; regime now steady-state |
| 14 January 2026 | UK regulators sign MoU with the European Supervisory Authorities on CTP/CTPP oversight |
| 18 March 2026 | FCA PS26/2 and PRA PS7/26 final incident and MTP reporting rules published; 12-month implementation period |
| 10–13 July 2026 | SI 2026/777 designates Amazon Web Services EMEA SARL, Google Cloud EMEA Limited, Microsoft Ireland Operations Limited and Oracle Corporation UK Limited as CTPs from 13 July 2026; interim self-assessments due within 3 months and playbook exercises within 12 months |
| 18 March 2027 | Incident reporting, MTP notification and annual register rules in force; SS2/21 March 2026 version effective |
| Pending | Further CTP designations possible on a rolling basis (no statutory limit); FCA Handbook lists a further SYSC 15A version dated 25 October 2027 (content not reviewed — verify); regulators' two-year post-implementation review of the reporting regime (2029) |

## Key obligations for security/GRC teams

1. **Confirm which layers apply** — SYSC 15A / PRA Operational Resilience Parts, SYSC 8 / SS2/21, 2027 incident reporting (standard or enhanced), MTP notification/register, and whether any supplier is a designated CTP. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Keep the IBS inventory and impact tolerances current** — annual review, re-justification on material change, board approval; tie each IBS to the mapped people, process, technology, facilities and information and to the third parties in the chain.
3. **Run and evidence scenario testing** against the SYSC 15A.5.6G scenario set (data corruption, loss of key people or sites, third-party outage, market-participant disruption, technology loss) and close lessons-learned actions. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
4. **Maintain the written self-assessment** with all nine SYSC 15A.6.1R elements, versioned and retained for 6 years, as the primary audit artefact. See [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).
5. **Build the 2027 incident pipeline now**: embed the three FCA and three PRA thresholds in severity triage, pre-map Connect submission ownership, rehearse the 24-hour initial report and 30-working-day final report, and keep SUP 15.3 immediate notifications and PSP 4-hour reporting running in parallel. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
6. **Reconcile the Outsourcing Register into the MTP register** (RegData template, annual, 90-day window) and route new or significantly changed material arrangements through pre-commitment notification. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../workflows/vendor-onboarding.md](../../workflows/vendor-onboarding.md).
7. **Remediate contracts** for material arrangements against SS2/21 chapters 6–10 (audit and access rights, sub-outsourcing controls, data security, stressed and non-stressed exit plans); log gaps as exceptions. See [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
8. **Consume CTP outputs**: for AWS, Google Cloud, Microsoft and Oracle, obtain the maximum tolerable level of disruption per systemic service, redacted annual self-assessments and test results, and use them in mapping and scenario tests — without treating designation as substitute diligence.
9. **Report to the board** on tolerance breaches, test outcomes, concentration in MTPs and CTPs, and remediation ageing. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md) and [../../templates/grc-board-report.md](../../templates/grc-board-report.md).
10. **Track the pipeline** — further CTP designations, the 2027 SYSC 15A change, and post-implementation review. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

- **DORA (EU 2022/2554).** Groups active in both markets face two regimes with the same architecture but different mechanics: DORA prescribes RTS-level incident thresholds and deadlines, a register of information in a fixed ITS format and Lead-Overseer supervision of CTPPs; the UK relies on judgement-based thresholds, a lighter MTP register and HMT designation of CTPs. The January 2026 UK–EU MoU coordinates oversight of providers that are both CTPs and CTPPs. Design one incident taxonomy (both are FIRE-aligned) and one register that can be cut both ways. See [dora.md](dora.md).
- **UK GDPR / Data Protection Act 2018.** A cyber incident involving personal data also triggers notification to the ICO on its own clock; see [other-jurisdictions.md](other-jurisdictions.md) and, for the EU text, [gdpr.md](gdpr.md). The 2027 regime reports data-loss incidents only where the financial-sector thresholds are met.
- **NIS2 / UK NIS.** NIS2 does not apply in the UK; UK NIS Regulations 2018 cover digital infrastructure and essential services, not financial firms as such — see [nis2.md](nis2.md) and [other-jurisdictions.md](other-jurisdictions.md).
- **EBA Guidelines.** SS2/21 implements the EBA Outsourcing Guidelines and relevant parts of the EBA ICT and security risk management Guidelines; SYSC 15A.2.12G–2.13G tell PSPs to read impact tolerances together with those Guidelines.
- **Frameworks.** IBS mapping and scenario testing map naturally onto NIST CSF 2.0 Identify/Respond/Recover and ISO 27001 Annex A continuity controls; see [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md), [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) and the [breach-notification crosswalk](../crosswalks/breach-notification-timelines.md).

## Primary sources

- FCA Handbook SYSC 15A Operational resilience (rules and guidance): https://www.handbook.fca.org.uk/handbook/SYSC/15A/
- FCA Handbook SYSC 8.1 General outsourcing requirements: https://www.handbook.fca.org.uk/handbook/SYSC/8/1.html
- FCA Handbook SUP 15.3 General notification requirements: https://www.handbook.fca.org.uk/handbook/SUP/15/3.html
- FCA PS21/3 Building operational resilience (policy statement page): https://www.fca.org.uk/publications/policy-statements/ps21-3-building-operational-resilience
- FCA PS26/2 Operational incident and third party reporting (page and PDF), FG26/3 and FG26/4: https://www.fca.org.uk/publications/policy-statements/ps26-2-operational-incident-third-party-reporting
- PRA SS1/21 Operational resilience: Impact tolerances for important business services (March 2022 version, PDF): https://www.bankofengland.co.uk/prudential-regulation/publication/2021/march/operational-resilience-impact-tolerances-for-important-business-services-ss
- PRA SS2/21 Outsourcing and third party risk management (November 2024 and March 2026 versions, PDF): https://www.bankofengland.co.uk/prudential-regulation/publication/2021/march/outsourcing-and-third-party-risk-management-ss
- PRA PS7/26 Operational incident and third-party reporting (policy statement, includes SS1/26): https://www.bankofengland.co.uk/prudential-regulation/publication/2026/march/operational-incident-and-third-party-reporting-policy-statement
- FSMA 2000 ss. 312L–312V (legal text, legislation.gov.uk): https://www.legislation.gov.uk/ukpga/2000/8/section/312L (and following sections); FSMA s. 206: https://www.legislation.gov.uk/ukpga/2000/8/section/206
- The Critical Third Parties (Designation) Regulations 2026, SI 2026/777 (legal text): https://www.legislation.gov.uk/uksi/2026/777/made
- Bank of England FMI Rulebook: Critical Third Parties Instrument 2024 (rule text): https://www.bankofengland.co.uk/-/media/boe/files/financial-stability/financial-market-infrastructure-supervision/critical-third-parties/final-ctp-rule-instrument.pdf
- Bank of England Critical Third Parties page (links to PS16/24, SS6/24, SS7/24, oversight approach, MoUs): https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/critical-third-parties
- Bank of England news, 10 July 2026, regulators to begin overseeing CTPs: https://www.bankofengland.co.uk/news/2026/july/uk-financial-regulators-to-begin-overseeing-critical-third-parties-announced-by-hmt
- HM Treasury press release, 10 July 2026, CTP designations: https://www.gov.uk/government/news/uk-financial-system-strengthened-with-new-safeguards-for-major-technology-providers
- Bank of England statement, 14 January 2026, UK–EU MoU on CTP oversight: https://www.bankofengland.co.uk/news/2026/january/uk-and-eu-regulators-sign-mou-to-strengthen-oversight-of-critical-third-parties
- Bank of England CBEST Implementation Guide and operational resilience landing page (CBEST, STAR-FS, CQUEST): https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector
- FCA press release, TSB fined £48.65m (20 December 2022): https://www.fca.org.uk/news/press-releases/tsb-fined-48m-operational-resilience-failings
- Not fetched (page not reachable during review): PRA PS16/24 and SS6/24 landing pages and PDFs; PRA PS6/21 and PS7/21 pages; the PRA Rulebook Operational Resilience Part online text (rule numbers taken from SS1/21 footnotes). Verify against the PRA Rulebook before citing rule numbers.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
