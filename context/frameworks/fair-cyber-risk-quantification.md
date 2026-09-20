# FAIR — Factor Analysis of Information Risk (Open FAIR Body of Knowledge: O-RT and O-RA)

## At a glance

| Attribute | Detail |
|---|---|
| What it is | An analytic, probabilistic model for expressing information and operational risk as a financial loss-exposure distribution. Not a control catalogue, not a maturity model |
| Publisher / owner | The Open Group (Security Forum) publishes the **Open FAIR** standards; the FAIR Institute (non-profit) holds the FAIR trademark and develops the ancillary models |
| Core documents | Risk Taxonomy (**O-RT**) — the factor model; Risk Analysis (**O-RA**) — the analysis method. Together they are the Open FAIR Body of Knowledge |
| Current editions | **O-RT Version 3.1 (C251)** and **O-RA Version 2.1 (C250)**, both published **22 May 2025**; they supersede O-RT 3.0.1 (C20B) and O-RA 2.0.1 (C20A), both published 15 Nov 2021 |
| Ancillary models | FAIR-CAM (controls analytics, launched 20 Oct 2021), FAIR-MAM (materiality assessment, released 15 Aug 2023), FAIR-AIR (AI-risk playbook), FAIR-TAM (third-party assessment model, still in development) — FAIR Institute publications, **not** Open Group standards |
| Certifiable? | People certification only — Open FAIR Foundation and Open FAIR 2 Foundation. There is **no organizational certification, audit scheme or attestation** |
| Access and licence | Open Group standards are free PDF downloads from The Open Group Library but require a (free) account; FAIR, FAIR-CAM and FAIR-MAM materials are licensed CC BY-NC-ND 4.0 — non-commercial use only, commercial use needs written FAIR Institute approval |
| Typical use | Sizing named risk scenarios in currency; prioritizing control spend; pricing audit findings, pen-test results and policy exceptions; securities materiality analysis; board reporting; cyber-insurance sizing |
| Relationship to control frameworks | Complementary. Catalogues (NIST CSF, ISO 27001, CIS, PCI DSS) say *what good practice looks like*; FAIR says *how much loss exposure exists* and *which gap matters most* |

## What it is

FAIR is the quantitative layer that most security programs lack. Control frameworks are, in the words of FAIR's author, "lists of good practices": complying with them is assumed to reduce risk, but they do not measure how much risk exists, so they cannot tell you which of your open gaps to fix first. FAIR supplies an explicit factor model — an ontology of the things that drive loss — plus a method for estimating those factors as calibrated ranges and running them through simulation to produce a loss-exposure distribution in currency.

Two bodies maintain it. **The Open Group** standardized FAIR through its Security Forum and publishes the two normative documents (O-RT, O-RA) plus a supporting library of guides, cookbooks and a spreadsheet analysis tool. The **FAIR Institute** is the practitioner community and research body: it develops the extensions that sit outside the Open Group standards, runs training and the Certified Cyber Risk Professional (CCRP) credential, and publishes the model diagrams. The Institute is explicit that the Open Group standards "provide an introduction to the concepts and methods within FAIR, but do not fully cover the body of knowledge" — deeper taxonomy levels, Monte Carlo simulation, calibrated estimation, sensitivity analysis and risk aggregation sit in Institute material and the FAIR book rather than in the two standards.

The practical claim FAIR makes is narrow and defensible: ordinal scales (1–5, red/amber/green) cannot legitimately be added or multiplied, cannot answer "how much more risk if…", and cannot be compared against a budget. Frequencies, probabilities and monetary ranges can.

## Who it covers / Scope

- **No mandatory applicability.** FAIR is a voluntary analytic model; nothing obliges an organization to adopt it. It is pulled in by regulatory and governance pressure to express cyber risk financially rather than by any rule that names it.
- **Sector- and size-agnostic.** The FAIR Institute reports use across banking, insurance, retail, manufacturing, high tech, health care, energy, education, consultancies and government, in organizations of every size — its own phrase is "from SMB to Fortune 1".
- **Scenario-scoped, not enterprise-scoped.** A FAIR analysis always applies to a defined scenario — a named asset, threat community and effect ("ransomware encrypts the ERP via a compromised administrator workstation"). It is not applied to a category such as "malware risk". Enterprise exposure is built by aggregating scenarios.
- **Where it fits badly:** where management wants only compliance confirmation, where no decision depends on the number, or where a scenario is so poorly scoped that decomposition has not been done. The learning curve is in scoping, not arithmetic.
- **Licensing is a real scope constraint.** Non-commercial use only under CC BY-NC-ND 4.0; you may not distribute modified versions of the model. Consultancies and product vendors embedding FAIR need written permission from the FAIR Institute.

## Structure and requirements

### The risk taxonomy (O-RT)

Factor names and units below are taken from the free HTML edition of **O-RT 3.0.1** (the 3.1 text is not publicly retrievable) and cross-checked against the FAIR Institute model diagram of June 2025:

| Factor | Decomposes into | Unit |
|---|---|---|
| **Risk** | Loss Event Frequency and Loss Magnitude — O-RT defines risk as "the probable frequency and probable magnitude of future loss" | Loss exposure in currency over a stated period |
| **Loss Event Frequency (LEF)** | Threat Event Frequency, Susceptibility | Events per unit time (usually per year) |
| **Threat Event Frequency (TEF)** | Contact Frequency (CF), Probability of Action (PoA) | Events per unit time |
| **Susceptibility** | Threat Capability (TCap) versus Resistance Strength (RS), each a percentile 0–100. O-RT 3.0.1 names this factor **Vulnerability (Vuln)** and gives Susceptibility as its synonym; the FAIR Institute's 2025 diagram uses Susceptibility | Probability (0–1 or %) |
| **Loss Magnitude (LM)** | Primary Loss, Secondary Loss | Currency |
| **Primary Loss** | Loss falling directly on the organization from the event | Currency |
| **Secondary Loss** | Reaction of secondary stakeholders (customers, regulators, partners); splits into Secondary Loss Event Frequency (SLEF — a conditional probability that a primary loss triggers a secondary one) and Secondary Loss Magnitude (SLM) | Currency |

O-RT 3.0.1 §4.4.1 defines **six forms of loss**: productivity, response, replacement, fines and judgments, competitive advantage, and reputation. Productivity, response and replacement are normally primary losses; the other three usually surface as secondary losses. Re-check the list against O-RT 3.1 before quoting it in a deliverable *(verify)*.

### The analysis method (O-RA)

O-RA standardizes the risk analysis process itself. The FAIR Institute states plainly that the two Open Group standards do not cover the whole body of knowledge; the rows marked below as "beyond the standards" are the ones it lists as sitting outside them.

| Element | What it does | Where it sits |
|---|---|---|
| Scenario scoping | Defines asset at risk, threat community, threat type and effect. Most analyst error lives here | O-RA / Process Guide *(verify)* |
| Deeper taxonomy levels | Decomposition below the factors tabulated above | Beyond the standards |
| Distributions instead of scales and matrices | Factors are estimated as ranges, not point values or ordinal scores | Beyond the standards |
| Calibrated estimation | Improves the quality and utility of estimates where data are sparse | Beyond the standards |
| Monte Carlo simulation | Propagates highly uncertain inputs into an output loss distribution | Beyond the standards |
| Sensitivity analysis | Identifies the factors that actually drive the result, so measurement effort goes where it pays | Beyond the standards |
| Risk aggregation | Combines scenario results into portfolio-level exposure | Beyond the standards |

Supporting Open Group publications: Open FAIR Risk Analysis Process Guide v1.1 (G180, 5 Sep 2022, aligned to Body of Knowledge v2.0); Risk Analysis Example Guide (G21A, July 2021); Mathematics for the Open FAIR Methodology (G224, September 2022); Open FAIR – NIST Cybersecurity Framework Cookbook (G167, October 2016); Open FAIR – ISO/IEC 27005 Cookbook (C103, November 2010); Open FAIR Risk Analysis Tool Beta spreadsheet (I181, January 2018) with its theory-of-operation guide (G181, January 2018).

### FAIR-CAM — controls analytics

FAIR-CAM, created by FAIR's author, describes control "physiology": how controls affect the frequency or magnitude of loss, individually and as a system, in real units (%, time, currency) rather than ordinal scores. Structure per the FAIR Institute model diagram (June 2025):

| Control function group | Sub-functions |
|---|---|
| Loss Event Controls (direct effect) | Loss Event Prevention, Loss Event Detection, Loss Event Response |
| Variance Management Controls (indirect) | Keep other controls operating as intended |
| Decision Support Controls (indirect) | Inform which controls exist and how they are tuned |

Institute workgroups have mapped, or are mapping, FAIR-CAM to NIST SP 800-53, the CIS Controls, the ISO 27000 series and HITRUST. The detailed white paper is gated behind contributing membership.

### FAIR-MAM — materiality assessment

FAIR-MAM, released **15 August 2023**, expands the Loss Magnitude branch into an open cyber loss-cost model built for securities materiality determinations. It is composed of **10 primary cost modules**, customizable to an organization's own cost structure, and supports aggregating the materiality of multiple events over time. The modules named in the FAIR Institute model diagram (June 2025):

| Module | Typically appears as |
|---|---|
| Information Privacy | Primary and secondary loss |
| Business Interruption | Primary and secondary loss |
| Network Security | Primary and secondary loss |
| Financial Fraud | Primary and secondary loss |
| Hardware Bricking | Primary and secondary loss |
| Cyber Extortion | Primary loss |
| Proprietary Data Loss | Secondary loss |
| Media Liability | Secondary loss |
| Post-Breach Security Improvements | Secondary loss |
| Reputational Damage | Secondary loss |

The Institute states FAIR-MAM loss categories can be mapped to MITRE ATT&CK "actions on objective" tactics and techniques — e.g. ransomware losses to T1486 / T1490, data-compromise losses to the Exfiltration tactic TA0010, business email compromise to T1566.

### FAIR-TAM — third-party assessment

FAIR-TAM is a FAIR-based third-party risk assessment model **still under development** by the Institute's Third-Party Risk Management Workgroup; there is no published standard document. Its three stated foundational concepts are risk-based tiering of vendors (assessing the vendor as a first-party scenario, with FAIR-MAM applied to data, server or revenue access), continuous inside-out telemetry rather than questionnaires or outside-in scans (with FAIR-CAM used to gauge breach likelihood), and treating third parties as part of the attack surface. Treat it as work in progress, not as a citable standard.

## Assessment, certification and evidence

There is **no FAIR certification of an organization or of a risk analysis**. Certification is individual and knowledge-based:

| Credential | Exam | Items / time | Pass mark | Body of Knowledge |
|---|---|---|---|---|
| Open FAIR Foundation | OG0-041 (English) | 80 questions / 120 min | 70% (56/80) | O-RA v1.0 + O-RT v2.0 |
| Open FAIR 2 Foundation | OGOF-101 (English) | 40 questions / 60 min | 60% (24/40) | O-RA v2.0.1 + O-RT v3.0.1 |

Both exams are supervised, closed-book, multiple-choice, with no prerequisites, delivered at test centres or by remote proctoring. Certification is **to a version of the Body of Knowledge and does not expire** — there is no recertification requirement. The FAIR Institute separately runs the Certified Cyber Risk Professional (CCRP) credential and a free five-course executive/board programme; it reports having trained more than 10,000 professionals since 2017.

Evidence practice for a defensible analysis (this is assurance convention, not a certification requirement): record the scenario definition, the estimator names and their calibration status, the source and vintage of every input, the distribution and simulation settings, the sensitivity output, and the decision the number supported. An unrecorded assumption is an unreviewable number — the same rule that applies to qualitative scoring in [../risk-scoring.md](../risk-scoring.md).

## Timeline and status

| Date | Event |
|---|---|
| November 2010 | Open FAIR – ISO/IEC 27005 Cookbook (C103) published |
| October 2016 | Open FAIR – NIST Cybersecurity Framework Cookbook (G167) published |
| January 2018 | Open FAIR Risk Analysis Tool Beta (I181) and its theory-of-operation guide (G181) published |
| 20 October 2021 | FAIR Institute launches FAIR-CAM |
| 15 November 2021 | O-RT v3.0.1 (C20B, 42 pp., supersedes C13K) and O-RA v2.0.1 (C20A, 47 pp., supersedes C13G) published; together they form Open FAIR Body of Knowledge v2.0 |
| September 2022 | Open FAIR Risk Analysis Process Guide v1.1 (G180) and Mathematics for the Open FAIR Methodology (G224) published |
| 15 August 2023 | FAIR-MAM released as an ancillary standard, the Institute tying it directly to the SEC cybersecurity disclosure rules approved earlier that year |
| February 2024 | FAIR Institute joins the NIST-convened US AI Safety Institute Consortium; the FAIR-AIR Approach Playbook and a GenAI work group are in place by this point |
| **22 May 2025** | **O-RT v3.1 (C251, 42 pp.) and O-RA v2.1 (C250, 48 pp.) published**, superseding C20B and C20A. The Open Group product pages carry no change list — obtain both PDFs and diff them before updating internal method documentation |
| As of September 2026 | O-RT 3.1 / O-RA 2.1 remain the current editions (Latin American Spanish translations have since been added); no further Open FAIR standard or guide has been published. The certification Bodies of Knowledge still reference O-RA 2.0.1 / O-RT 3.0.1 and no exam aligned to the 3.1/2.1 editions is announced. The Open Group's own Open FAIR overview page also still describes the 2021 editions. FAIR Institute reports 18,000+ members worldwide and 10,000+ people trained |

Pending as of September 2026: an exam and Body of Knowledge aligned to O-RT 3.1 / O-RA 2.1; publication of FAIR-TAM as a finished model. No Open FAIR standard has been withdrawn.

## Key obligations for security/GRC teams

1. **Decide what the number is for before running an analysis.** FAIR earns its cost on decisions — budget allocation, treat/accept, insurance limits, exception approval. See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).
2. **Scope scenarios properly.** Asset, threat community, threat type, effect. Most FAIR failures are scoping failures, not maths failures. Pair with the register discipline in [../../templates/risk-register-guide.md](../../templates/risk-register-guide.md).
3. **Choose the method deliberately.** Not every scenario justifies quantification; keep calibrated qualitative scoring for the long tail and reserve FAIR for material decisions — see [../risk-scoring.md](../risk-scoring.md).
4. **Calibrate your estimators and record the ranges.** Uncalibrated subject-matter estimates propagate straight into the output distribution.
5. **Quantify audit findings, pen-test results and policy exceptions** rather than rating them by severity label — this is where FAIR pays back fastest. See [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md) and [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
6. **Use FAIR-CAM to price control changes**, mapping it onto whichever control catalogue you already run ([nist-800-53.md](nist-800-53.md), [cis-controls-v8.md](cis-controls-v8.md), [iso-27001-2022.md](iso-27001-2022.md)) instead of replacing it.
7. **Pre-build the materiality model, not the materiality answer.** A loss model populated before an incident is what makes a four-business-day determination possible; see [../regulations/sec-cyber-disclosure.md](../regulations/sec-cyber-disclosure.md).
8. **Report distributions, not single numbers, to the board** — annualized loss exposure with a range and the top sensitivity drivers. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md) and [../../templates/grc-board-report.md](../../templates/grc-board-report.md).
9. **Apply the same model to vendors and to AI use cases**; scenarios differ, the taxonomy does not. FAIR-TAM is not finished, so build vendor scenarios from the base taxonomy rather than waiting on it. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).
10. **Re-baseline annually** and keep model versions under change control alongside the annual assessment cycle ([../../workflows/annual-risk-assessment.md](../../workflows/annual-risk-assessment.md)).

## Interplay

- **Securities disclosure:** the SEC's 2023 final rule (88 FR 51896, 4 August 2023; effective 5 September 2023) requires a Form 8-K **Item 1.05** filing within **four business days of determining** that a cybersecurity incident is material, with that determination to be made **"without unreasonable delay"** (the adopting release changed this from the proposal's "as soon as reasonably practicable"), plus annual risk-management and governance disclosure under Regulation S-K **Item 106** (17 CFR 229.106, still in force on the September 2026 eCFR). FAIR-MAM exists to make that determination fast, financial and comparable. Detail in [../regulations/sec-cyber-disclosure.md](../regulations/sec-cyber-disclosure.md); clocks across regimes in [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
- **Control catalogues:** FAIR does not replace [nist-csf-2.md](nist-csf-2.md), [iso-27001-2022.md](iso-27001-2022.md), [cis-controls-v8.md](cis-controls-v8.md) or [nist-800-53.md](nist-800-53.md); it prioritizes their gaps. The Open Group publishes cookbooks bridging FAIR to the NIST CSF and to ISO/IEC 27005. Coverage mapping belongs in [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
- **Risk-management standards:** ISO 31000 / ISO 27005 and NIST SP 800-30 define the *process* of risk management and leave the measurement method open; FAIR supplies a measurement model that can be slotted into either. (Companion packs on the ISO 31000/27005 and NIST 800-37/800-30 families cover those processes.)
- **Financial-sector resilience:** DORA-style ICT risk-management frameworks require documented risk assessment and board-level ownership without prescribing quantification; FAIR outputs are a defensible way to evidence the "assessed" part and to justify concentration and exit decisions. See [../regulations/dora.md](../regulations/dora.md) and [../regulations/nis2.md](../regulations/nis2.md).
- **AI risk:** the FAIR Institute publishes the FAIR-AIR Approach Playbook, a five-step method for identifying AI-related loss exposure (recognize the five vectors of generative-AI risk, identify scenarios, quantify frequency and magnitude, prioritize and treat, compare treatment options), and is a member of the US AI Safety Institute Consortium. Governance obligations sit in [../regulations/eu-ai-act.md](../regulations/eu-ai-act.md).
- **Terminology conflicts are real.** "Vulnerability", "threat" and "risk" carry FAIR-specific definitions that differ from common vulnerability-management usage; fix definitions in one place ([../glossary.md](../glossary.md)) before mixing FAIR outputs into an enterprise risk register.

## Primary sources

- The Open Group, *The Open FAIR Body of Knowledge* overview — https://www.opengroup.org/open-fair (publisher page; fetched — lists the O-RT/O-RA standards and the supporting guides with document numbers and dates)
- The Open Group Library, *Risk Taxonomy (O-RT), Version 3.1* (C251) — https://publications.opengroup.org/c251 (publisher product page; fetched — publication date, ISBN, supersession)
- The Open Group Library, *Risk Analysis (O-RA), Version 2.1* (C250) — https://publications.opengroup.org/c250 (publisher product page; fetched)
- The Open Group Library, *Risk Taxonomy (O-RT), Version 3.0.1* (C20B) — https://publications.opengroup.org/c20b and *Risk Analysis (O-RA), Version 2.0.1* (C20A) — https://publications.opengroup.org/c20a (publisher product pages; fetched)
- The Open Group Library, Open FAIR standards catalogue — https://publications.opengroup.org/standards/open-fair-standards (publisher listing; fetched — confirms 3.1/2.1 are the current editions and that nothing newer has been issued)
- The Open Group Standard, *Risk Taxonomy (O-RT), Version 3.0.1*, full HTML edition (C20B, November 2021), read from the Internet Archive capture of https://pubs.opengroup.org/security/o-rt/ (normative text; the live copy now sits behind sign-in — source of the factor definitions, units and the six forms of loss)
- The Open Group Library, *Open FAIR Risk Analysis Process Guide, Version 1.1* (G180) — https://publications.opengroup.org/g180 (publisher product page; fetched)
- The Open Group, *Open FAIR Certification Program* — https://www.opengroup.org/certifications/openfair (publisher page; fetched)
- The Open Group, *Open FAIR Examinations* datasheet — https://certification.opengroup.org/docs/datasheets/openfair-exams.pdf (publisher document; fetched — exam numbers, item counts, pass marks)
- The Open Group, *Open FAIR 2 Foundation Certification* datasheet — https://www.opengroup.org/sites/default/files/images/Accreditation/Open-FAIR-Certification-datasheet.pdf (publisher document; fetched)
- FAIR Institute, *FAIR Cyber Risk Management Framework — FAIR CRM on a Page*, June 2025 — https://www.fairinstitute.org/hubfs/FAIR%20CRM%20on%20a%20Page_June%202025.pdf (publisher document; fetched — factor names, FAIR-CAM control groups, FAIR-MAM modules)
- FAIR Institute, *What is FAIR?*, *FAIR Risk Management*, *FAIR-CAM*, *FAIR-MAM*, *AI Risk*, *Training and Certification*, *FAQ* — https://www.fairinstitute.org/what-is-fair, /fair-risk-management, /fair-cam, /fair-materiality-assessment-model, /ai-risk, /fair-training-and-certification, /frequently-asked-questions (publisher pages; all fetched)
- FAIR Institute, *Measure and Manage Third Party Risk with FAIR-TAM* — https://www.fairinstitute.org/fair-third-party-assessment-model (publisher page; fetched — confirms FAIR-TAM exists and is still in development)
- FAIR Institute home page — https://www.fairinstitute.org/ (publisher page; fetched — membership and training figures)
- FAIR Institute, *A New Extension of the FAIR Standard: Introducing FAIR-MAM*, 15 August 2023 — https://www.fairinstitute.org/blog/new-fair-standard-fair-materiality-assessment-model-fair-mam, and *FAIR Institute Introduces FAIR-CAM*, 20 October 2021 — https://www.fairinstitute.org/fair-newsroom/fair-institute-introduces-fair-cam-to-help-cybersecurity-teams-assess-effectiveness-of-risk-management-controls-to-make-more-cost-effective-business-decisions (publisher announcements; fetched — release dates)
- Jack Jones, *NIST CSF & FAIR — Part 1*, FAIR Institute, 16 March 2016 — https://www.fairinstitute.org/blog/nist-csf-fair-part-1 (author's own statement of the "lists of good practices" argument; fetched)
- US Securities and Exchange Commission, *Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure*, final rule, 88 FR 51896 (4 August 2023), effective 5 September 2023 — https://www.federalregister.gov/documents/2023/08/04/2023-16194/cybersecurity-risk-management-strategy-governance-and-incident-disclosure (official legal text, read in the govinfo.gov edition of the same issue — Item 1.05 four-business-day clock, "without unreasonable delay" determination standard, Item 106)
- eCFR, 17 CFR 229.106 (Item 106, Cybersecurity), current as of 17 September 2026 — https://www.ecfr.gov/current/title-17/section-229.106 (official codified text; fetched — confirms Item 106 remains in force, source note 88 FR 51942)
- **Not retrievable:** the full text of O-RT 3.1, O-RA 2.1 and O-RA 2.0.1, and the FAIR-CAM, FAIR-MAM and FAIR-TAM white papers. The Open Group PDF and HTML editions sit behind a free account sign-in and the Institute's white papers require contributing membership, so the taxonomy detail here rests on the archived O-RT 3.0.1 text plus the Institute's 2025 model diagram; nothing that changed between 3.0.1 and 3.1 could be checked.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
