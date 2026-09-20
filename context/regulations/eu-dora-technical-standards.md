# DORA Level-2 and Level-3 Layer — RTS/ITS Technical Standards, Delegated Acts and ESA Guidelines

This pack covers the delegated/implementing regulations and ESA guidelines that put numbers on Regulation (EU) 2022/2554. It does not restate the level-1 summary — read [dora.md](dora.md) first for scope, the five pillars and supervisory architecture.

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | 12 Commission delegated/implementing regulations adopted under DORA empowerments (Arts. 15, 16(3), 18(4), 20, 26(11), 28(9), 28(10), 30(5), 31(6), 41, 43(2)) plus two sets of joint ESA guidelines (Arts. 11(11), 32(7)) |
| Legal nature | Directly applicable EU regulations, no transposition; each entered into force on the 20th day after Official Journal (OJ) publication and applies alongside DORA (applicable since 17 January 2025) |
| Drafters / adopters | Ten drafted by the three ESAs (EBA, EIOPA, ESMA) through the Joint Committee and adopted by the Commission; two (criticality criteria, fees) adopted by the Commission directly under Arts. 31(6) and 43(2); two ESA drafts (register ITS, subcontracting RTS) were first rejected and re-adopted with changes |
| Publication window | 30 May 2024 (criticality criteria, fees) to 2 July 2025 (subcontracting RTS) — the last standard landed almost six months after DORA started applying |
| Headline clocks | Major incident: initial notification within 4 h of classification and no later than 24 h of awareness; intermediate report within 72 h of the initial; final report within 1 month of the (last) intermediate |
| Headline thresholds | Major = critical services affected + either a successful malicious unauthorised access or any two other thresholds (e.g. >10% of clients or >100,000 clients; >24 h duration or >2 h downtime of a critical/important function; impact in ≥2 Member States; costs above EUR 100,000) |
| Oversight economics | Minimum annual CTPP oversight fee EUR 50,000; opt-in application fee EUR 50,000 (non-refundable); Lead Overseer periodic penalty payments up to 1% of average daily worldwide turnover per day, max six months (DORA Art. 35) |
| First CTPP list | 19 providers published by the ESAs in November 2025 (DORA Art. 31(9) list, updated yearly); unchanged at the time of this review |
| Who must read this | Any team building a DORA incident playbook, register of information, ICT contract checklist, TLPT programme or CTPP-exposure assessment — the level-1 text alone is not enough to be compliant |

## What it is

DORA is a two-tier regime. The regulation sets principles and mandates the ESAs to draft Regulatory Technical Standards (RTS, adopted as Commission Delegated Regulations) and Implementing Technical Standards (ITS, adopted as Commission Implementing Regulations). Two delegated acts (CTPP criticality criteria and oversight fees) were adopted by the Commission directly under DORA Arts. 31(6) and 43(2) rather than on ESA draft standards. The ESAs add a level-3 layer of joint guidelines, Q&As, decisions on data collection and non-binding "operational instructions". Together these carry nearly every number a practitioner needs: materiality thresholds, report deadlines, register templates, TLPT phase durations, tester qualifications, fee formulas.

The standards were delivered in two batches (first-batch final drafts January 2024, second batch July 2024) and published between May 2024 and July 2025. Two were politically contested: the Commission rejected the ESAs' draft register ITS on 3 September 2024 because it mandated LEI-only identification of providers (the adopted text allows LEI or EUID for EU-established providers), and rejected the draft subcontracting RTS on 21 January 2025 because draft Art. 5 went beyond the Art. 30(5) empowerment (ESAs' Opinion, 7 March 2025) before adopting a revised version on 24 March 2025.

## Who it covers / Scope

Every instrument follows DORA's scope (Art. 2 financial entities; ICT third-party providers via contract and, for CTPPs, direct oversight). Specific carve-outs in the level-2 layer:

- **Simplified-framework entities** (DORA Art. 16(1)): covered by Title III of the ICT-risk RTS (2024/1774, Arts. 28–41) instead of Title II. **Microenterprises** stay in Title II but with derogations (e.g. periodic rather than annual network-architecture review, Art. 13). Both are outside the recurring-incident aggregation rule (2024/1772 Art. 8(2)) and outside TLPT (DORA Art. 26(1)).
- **TLPT population**: only entities identified by the TLPT authority under 2025/1190 Art. 2 (see below); microenterprises and Art. 16(1) entities are outside.
- **Weekend/bank-holiday relief** on report deadlines does not apply to initial or intermediate reports from credit institutions, CCPs, trading-venue operators or entities that are essential/important under NIS2 (2025/301 Art. 5(5)); authorities may withdraw it from other significant entities (Art. 5(6)).
- **Aggregated incident reporting** by a provider on behalf of several entities is barred for significant credit institutions (SSM), trading-venue operators and CCPs (2025/302 Art. 7(2)).
- **CTPP designation** is assessed per provider or, where the provider belongs to a group, per group (DORA Art. 31(3)); the ESAs may also assess and designate a provider's ICT subcontractors (2024/1502 recitals).

## Core obligations

### Instrument map

| Instrument | Subject (DORA basis) | OJ date | In force | Key numbers |
|---|---|---|---|---|
| Delegated Reg. (EU) 2024/1502 | Criteria for designating CTPPs (Art. 31(6)) | 30 May 2024 | 19 Jun 2024 | Two-step test; step-1 quantitative shares of ≥10% of a financial-entity category; G-SII/O-SII counts; sub-criterion 1.4 applied from 16 Jan 2025 |
| Delegated Reg. (EU) 2024/1505 | CTPP oversight fees (Art. 43(2)) | 30 May 2024 | 19 Jun 2024 | Fee ∝ EU turnover from ICT services to financial entities (year n-2, audited, due 31 Dec); minimum EUR 50,000; opt-in fee EUR 50,000; pay by 30 Apr |
| Delegated Reg. (EU) 2024/1772 | Incident classification, materiality thresholds, significant cyber threats (Art. 18(4)) | 25 Jun 2024 | 15 Jul 2024 | Thresholds in Art. 9; major-incident rule in Art. 8; recurring incidents ≥2 in 6 months |
| Delegated Reg. (EU) 2024/1773 | Policy on contracts for ICT services supporting critical or important functions (Art. 28(10)) | 25 Jun 2024 | 15 Jul 2024 | Management body reviews policy at least yearly; lifecycle phases; exit plans reviewed and tested |
| Delegated Reg. (EU) 2024/1774 | ICT risk-management tools/policies + simplified framework (Arts. 15, 16(3)) | 25 Jun 2024 | 15 Jul 2024 | 42 articles; weekly vulnerability scans on critical/important-function assets; access reviews every 6 months for those systems, yearly otherwise |
| Implementing Reg. (EU) 2024/2956 | Register-of-information templates (Art. 28(9)) | 2 Dec 2024 | 22 Dec 2024 | 15 templates (B_01.01 to B_99.01) in Annex I; 19 ICT service types (S01–S19) in Annex III; LEI or EUID; corrigendum to the annexes published 19 Sep 2025 |
| Delegated Reg. (EU) 2025/295 | Harmonised conditions for oversight activities (Art. 41) | 13 Feb 2025 | 5 Mar 2025 | Opt-in application content; CTPP information and remediation-plan reporting; subcontracting template |
| Delegated Reg. (EU) 2025/301 | Content and time limits of major-incident reports; cyber-threat notification (Art. 20) | 20 Feb 2025 | 12 Mar 2025 | 4 h / 24 h; 72 h; 1 month; noon-next-working-day relief |
| Implementing Reg. (EU) 2025/302 | Forms, templates and procedures for incident reports and threat notifications (Art. 20) | 20 Feb 2025 | 12 Mar 2025 | Single incident template (Annex I) with glossary (Annex II); threat template (Annex III) |
| Delegated Reg. (EU) 2025/420 | Joint examination teams (Art. 41) | 24 Mar 2025 | 13 Apr 2025 | Composition set by Lead Overseer with the Joint Oversight Network after consulting the Oversight Forum; members nominated by Art. 40(2) authorities |
| Delegated Reg. (EU) 2025/1190 | TLPT criteria, methodology, internal testers, cooperation (Art. 26(11)) | 18 Jun 2025 | 8 Jul 2025 | Mirrors TIBER-EU; active red-team phase ≥12 weeks; 3/6-month preparation deadlines; 4/10/8-week closure clocks |
| Delegated Reg. (EU) 2025/532 | Subcontracting of ICT services supporting critical or important functions (Art. 30(5)) | 2 Jul 2025 | 22 Jul 2025 | Pre-contract subcontracting decision; notice-and-objection right on material changes; termination triggers |
| ESA Guidelines JC/GL/2024/34 | Estimating aggregated annual costs and losses from major ICT incidents (Art. 11(11)) | final report 17 Jul 2024 | applies from 19 May 2025 | Gross costs/losses and financial recoveries per reference year, reported on competent-authority request (DORA Art. 11(10)) |
| ESA Guidelines JC/GL/2024/36 | Cooperation between ESAs and competent authorities on oversight (Art. 32(7)) | issued 6 Nov 2024 | applies from 17 Jan 2025 | Information exchange and structure of oversight cooperation |

### Incident classification (2024/1772)

| Criterion (DORA Art. 18(1)) | Materiality threshold (Art. 9) |
|---|---|
| Clients, financial counterparts, transactions | >10% of clients using the affected service, or >100,000 clients; >30% of financial counterparts; >10% of daily average number or value of transactions; or "relevant" clients/counterparts affected |
| Reputational impact | Media coverage; repetitive complaints; likely inability to meet regulatory requirements; likely loss of clients with material business impact (Art. 2) |
| Duration and downtime | Incident duration >24 h, or service downtime >2 h for ICT services supporting critical or important functions |
| Geographical spread | Impact in two or more Member States (Art. 4) |
| Data losses | Availability/authenticity/integrity/confidentiality impact that hits business objectives or regulatory compliance; or any successful, malicious, unauthorised access that may cause data loss (Art. 9(5)) |
| Economic impact | Costs and losses exceed, or are likely to exceed, EUR 100,000 |
| Criticality of services (gate) | Affects ICT services or systems supporting critical or important functions, authorised/supervised financial services, or constitutes successful malicious unauthorised access (Art. 6) |

- **Major incident** (Art. 8(1)): critical services affected **and** either the malicious-access threshold in Art. 9(5)(b) is met **or** any two other thresholds are met.
- **Recurring incidents** (Art. 8(2)): non-major incidents with the same apparent root cause occurring at least twice in 6 months that collectively meet the test count as one major incident; assess monthly (not for microenterprises or Art. 16(1) entities).
- **Significant cyber threat** (Art. 10): could affect critical or important functions or other entities, high probability of materialisation, and would meet the criticality, client/transaction or geographic thresholds if realised; notification is voluntary.
- Duration is measured from occurrence (or detection/log evidence) to resolution; estimates are used where data is unavailable (Arts. 1, 3).

### Incident reporting clocks and mechanics (2025/301 and 2025/302)

| Stage | Deadline (2025/301 Art. 5) | Content highlights |
|---|---|---|
| Initial notification | As early as possible, within 4 h of classifying the incident as major and no later than 24 h from becoming aware; if classified as major after the 24 h mark, within 4 h of classification | Incident reference code assigned by the entity, date/time of detection, classification and the criteria met, description, Member States impacted, how it was discovered, origin where available, whether a continuity plan was activated (Art. 2) |
| Intermediate report | Within 72 h of the initial notification even if nothing changed; updated without undue delay and in any case when regular activities are recovered | Reference code assigned by the authority, occurrence and recovery date/time, how the classification criteria were met, incident type, affected functional areas and infrastructure, impact on clients' financial interest, temporary measures (Art. 3) |
| Final report | No later than 1 month after the intermediate report or the latest updated intermediate | Root causes, resolution dates/times, direct and indirect costs and losses and financial recoveries, recurring-incident information (Art. 4) |

- Deadline falling on a weekend or bank holiday: submit by noon of the next working day (Art. 5(4)) — except initial/intermediate reports from credit institutions, CCPs, trading-venue operators and NIS2 essential/important entities (Art. 5(5)).
- Cannot meet a deadline: inform the authority before it expires with reasons (Art. 5(3)).
- One template for all three stages (2025/302 Art. 1, Annex I); stages may be combined if deadlines are still met (Art. 2); submit via the authority's secure electronic channel (Art. 4); reclassification from major to non-major must be notified (Art. 5); outsourcing of reporting must be notified to the authority before the first report (Art. 6); provider-led aggregated reports allowed only within one Member State, same authority, each entity having classified the incident as major, and with explicit authority permission (Art. 7).
- Cyber-threat notifications use Annex III/IV (Art. 8; content in 2025/301 Art. 6).
- ESA staff "Operational Instructions" on incident reporting (16 September 2026) harmonise field-level practice for authorities — non-binding, but they reveal how reports are read (English templates, versioning of corrected reports, third-party origin field).

### ICT risk-management framework detail (2024/1774)

- **Title II (Arts. 2–27)** — full framework: ICT risk-management policy with annual review of accepted residual risks (Art. 3); asset management (Arts. 4–5); encryption and key management (Arts. 6–7); operations, capacity, vulnerability and patch management including weekly automated scanning for critical/important-function assets (Arts. 8–10); data/system security, logging, network security with annual architecture review (Arts. 11–14); project, acquisition and change management (Arts. 15–17); physical security and HR policy (Arts. 18–19); identity and access control with access-rights reviews at least yearly, and every 6 months for critical/important-function systems (Arts. 20–21); incident management policy and detection criteria (Arts. 22–23); ICT business continuity policy, plan testing with switchover scenarios, and response/recovery plans (Arts. 24–26); the Art. 6(5) framework-review report to the authority in searchable electronic format (Art. 27).
- **Title III (Arts. 28–41)** — simplified framework: management-body accountability and annual budget review (Art. 28), a single information security policy (Art. 29), classification, risk management, physical security, access control, operations security, data/network security, security testing plan, acquisition/change management, continuity plan and testing, and a review report (Arts. 30–41).

### Third-party layer (2024/1773, 2025/532, 2024/2956)

- **Contractual policy RTS 2024/1773**: management-body-approved policy reviewed at least yearly (Art. 3); method for identifying ICT services supporting critical or important functions; senior-management owner; consistency with the ICT risk framework, information-security policy, continuity policy and incident reporting; lifecycle phases (Art. 4); ex-ante risk assessment covering operational, legal, ICT, reputational, data-protection, data-location and entity-level concentration risks (Art. 5); due diligence (Art. 6); conflicts of interest (Art. 7); contract clauses including audit rights exercised via own/appointed audits, pooled audits and pooled testing including TLPT, and third-party certifications (Art. 8); monitoring (Art. 9); documented exit plans, periodically reviewed and tested (Art. 10).
- **Subcontracting RTS 2025/532**: decide before contracting whether subcontracting of critical/important-function services is allowed, subject to ten conditions covering provider due diligence, subcontractor identification, flow-down of access/audit rights, location and concentration risk (Art. 3); mandatory contract content on subcontracted services (Art. 4); provider must give notice of material subcontracting changes with a notice period for the entity to approve or object, and may implement only after approval or non-objection (Art. 5); termination rights where changes are implemented over an objection, before the notice period ends, or where unapproved subcontracting occurs (Art. 6).
- **Register ITS 2024/2956**: templates in Annexes I–IV maintained at entity and, where relevant, sub-consolidated and consolidated level (Arts. 3(1), 5, 6); every provider ranked in the supply chain (rank 1 = direct provider, subcontractors higher, Art. 2); all direct providers plus all subcontractors that effectively underpin critical/important-function services (Art. 3(2)); a valid and active LEI or EUID for every provider that is a legal person (Art. 3(5)–(6)) — the recitals expect third-country providers to be identified by LEI only; six data-quality principles (accuracy, completeness, consistency, integrity, uniformity, validity, Art. 3(4)); one value per cell (Art. 4).
- **Collection calendar** (ESAs Decision ESA 2024 22, 8 Nov 2024, amended January 2025): competent authorities transmitted 2025 registers to the ESAs by 30 April 2025 (reference date 31 March 2025); thereafter annually by 31 March with a 31 December reference date (Arts. 4–5). National deadlines for entity-to-authority submission sit earlier — check the authority's own notice.
- In the 2024 dry run 1,039 entities took part; of the 947 registers that cleared integration checks and were analysed, only 6.5% passed all 116 data-quality checks — expect validation failures on identifiers, function mapping and consolidation consistency.

### TLPT mechanics (2025/1190)

| Element | Rule |
|---|---|
| Who is required (Art. 2(2)) | Unless the authority's impact/ICT-risk assessment says otherwise: G-SII/O-SII credit institutions and their group members; payment institutions >EUR 150 bn payment transactions in each of the two preceding years; e-money institutions >EUR 150 bn transactions or >EUR 40 bn outstanding e-money; CSDs; CCPs; trading venues with the highest national market share or >5% EU share by turnover; (re)insurers above gross-written-premium/technical-provision thresholds (Art. 2(2)(g)); other entities by assessment (Art. 2(1)) |
| Governance | TLPT authority runs a TLPT cyber team of test managers (Art. 3); entity appoints a control-team lead; need-to-know secrecy, blue team excluded (Art. 4) |
| Preparation | TLPT initiation information within 3 months of the authority's notification; scope specification document (Annex II), approved by the management body, within 6 months (Art. 9) |
| Providers (Art. 7) | Threat-intelligence team: manager ≥5 years plus one member ≥2 years, ≥3 references; testers: manager ≥5 years plus ≥2 testers ≥2 years; CVs and certifications on file |
| Testing | Targeted threat-intelligence report approved by the authority (Art. 10); red-team test plan; active red-team phase at least 12 weeks with weekly progress reports and leg-ups (Art. 11) |
| Closure (Art. 12) | Red-team report within 4 weeks of the active phase; blue-team report and replay/purple-teaming within 10 weeks; test summary report to the authority within 8 weeks of its notification that reports are complete |
| Remediation and attestation | Remediation plan (per finding: shortcoming, measures, root cause, owner, risk of non-remediation) within 8 weeks of that notification (Art. 13); attestation per Annex VIII (Art. 14); internal testers require a policy and safeguards, external testers every three tests per DORA Art. 26(8) (Art. 15); pooled/joint tests and cross-border cooperation with a lead TLPT authority (Arts. 8, 16) |

### CTPP oversight layer (2024/1502, 2024/1505, 2025/295, 2025/420)

- **Designation** (2024/1502): step 1 quantitative screens on each Art. 31(2) criterion (e.g. provider serves ≥10% of a financial-entity category by number and assets; counts of G-SIIs/O-SIIs and "systemic" entities relying on it; substitutability shares ≥10%), then step 2 qualitative assessment; designation by the Joint Committee on Oversight Forum recommendation after the provider's reasoned statement period.
- **Fees** (2024/1505): annual fee = ESAs' estimated oversight cost apportioned by a turnover coefficient on the provider's EU revenue from DORA-listed ICT services to financial entities (audited, year n-2, supplied by 31 December); minimum EUR 50,000; fixed first-year fee; opt-in fee EUR 50,000 not refunded; single instalment by 30 April (or 31 December if designated in-year); late payment accrues default interest.
- **Conduct of oversight** (2025/295): content of a voluntary designation application (Art. 1); information CTPPs must submit — group structure, value chain and subcontractors, third-country risk measures, ICT third-party management framework (Art. 2); remediation plan and progress reports after Lead Overseer recommendations (Art. 3); subcontracting template (Art. 5); competent authorities must assess how recommendations affect the entities they supervise and share results with the Lead Overseer (Art. 6).
- **Joint examination teams** (2025/420): established after each first designation with the Joint Oversight Network; members drawn from ESAs and competent authorities, full- or part-time; tasks include the annual oversight plan, assessing CTPP information, benchmarks and ad-hoc work (Arts. 1–3).
- **Enforcement on CTPPs**: DORA Art. 35(6)–(8) periodic penalty payments after at least 30 calendar days' non-compliance, imposed daily, up to 1% of the provider's average daily worldwide turnover in the preceding business year, for no more than six months; publicly disclosed unless that would cause disproportionate damage (Art. 35(10)).

## Enforcement and penalties

The level-2 acts create no new sanctions. Breach of any RTS/ITS is a breach of DORA and is enforced by the national competent authority under the Member State's Art. 50 administrative-penalty regime (see [dora.md](dora.md)); the only EU-level pecuniary tool is the Lead Overseer's periodic penalty payment on CTPPs above. Practically, the standards define the evidence supervisors ask for: the register (annual collection), the Art. 6(5) framework-review report, incident reports in the ITS template, TLPT attestations and remediation plans, and contract files against the 2024/1773 and 2025/532 checklists. The ESAs' report on 2025 major incidents (JC 2026 16, 3 June 2026, under DORA Art. 22) counted 3,383 major incidents reported in 2025, over 60% in the credit sector and 16% in payments, about one third with cross-border impact and almost one third originating from third-party failures — and noted divergent reporting practices across jurisdictions, which the September 2026 operational instructions aim to narrow.

## Timeline and status

| Date | Event |
|---|---|
| 17 Jan 2024 | DORA deadline for the ESAs' first-batch drafts, including the register ITS (DORA Art. 28(9)) |
| 30 May 2024 | Delegated Regs. 2024/1502 (criticality) and 2024/1505 (fees) published |
| 25 Jun 2024 | Delegated Regs. 2024/1772, 2024/1773, 2024/1774 published |
| 17 Jul – 26 Jul 2024 | ESAs submit second-batch drafts (incident reporting RTS/ITS, TLPT, oversight harmonisation, JET, subcontracting RTS; costs/losses guidelines final report 17 Jul; subcontracting final report published 26 Jul) |
| 3 Sep 2024 | Commission rejects the draft register ITS over LEI-only identification (draft Art. 3(5)–(6)); ESAs' Opinion 15 Oct 2024 |
| 2 Dec 2024 | Implementing Reg. 2024/2956 (register ITS) published with LEI-or-EUID rule |
| 17 Jan 2025 | DORA applies; JC/GL/2024/36 oversight-cooperation guidelines apply |
| 21 Jan 2025 | Commission rejects the draft subcontracting RTS (draft Art. 5 beyond the Art. 30(5) mandate) |
| 13 Feb – 24 Mar 2025 | 2025/295 (oversight harmonisation), 2025/301 and 2025/302 (incident reporting), 2025/420 (JET) published |
| 7 Mar 2025 | ESAs' Opinion on the Commission's rejection of the draft subcontracting RTS |
| 30 Apr 2025 | First register-of-information collection reaches the ESAs (reference date 31 Mar 2025) |
| 19 May 2025 | JC/GL/2024/34 costs/losses guidelines apply |
| 18 Jun 2025 | Delegated Reg. 2025/1190 (TLPT) published |
| 2 Jul 2025 | Delegated Reg. 2025/532 (subcontracting) published — the last mandated standard |
| 19 Sep 2025 | Corrigendum to the register ITS 2024/2956 (annex code lists and cell references) published in the OJ |
| Nov 2025 | ESAs publish the first list of designated CTPPs (19 providers, including major cloud, data, telecom and IT-services groups) |
| 4 Dec 2025 | ESAs' Art. 58(3) report (JC 2025 85) on whether statutory auditors and audit firms should be brought into DORA scope |
| Jan 2026 | ESAs–UK (BoE, PRA, FCA) MoU on cooperation and coordination of CTPP oversight |
| 31 Mar 2026 | Standing annual register calendar takes over: authorities report to the ESAs by 31 March on a 31 December reference date (ESA 2024 22 Arts. 4–5) |
| 3 Jun 2026 | First ESAs annual report on major ICT incidents (JC 2026 16, covering 2025) |
| 31 Jul 2026 | ESAs statement (JC 2026 25) on a consistent, risk-based approach to ICT risks from frontier AI models |
| 16 Sep 2026 | ESA staff operational instructions on DORA incident reporting |

**Status as of September 2026:** all twelve mandated RTS/ITS and both sets of joint guidelines are adopted, in force and applying. No amending delegated or implementing act had been published in the sources reviewed — the only change to an adopted text is the 19 September 2025 corrigendum to the register ITS (plus language-version corrigenda to 2024/1774, 2025/301 and 2025/1190 that do not affect the English text). The November 2025 CTPP list of 19 providers was still the current list at the time of review; the next yearly update is pending. Watch items: the annual CTPP list refresh, further ESA work on incident-reporting consistency following the September 2026 operational instructions, and any EU simplification initiative touching DORA reporting (verify).

## Key obligations for security/GRC teams

1. **Embed the Art. 8/9 major-incident test in triage**: encode the six thresholds and the critical-services gate as decision fields; run the monthly recurring-incident check; log the classification timestamp because the 4 h clock starts there. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
2. **Pre-build the 2025/302 template** in the authority's portal format with the initial, intermediate and final field sets; decide in advance whether weekend relief applies to your entity type and whether reporting is outsourced (notify before first use).
3. **Own the register of information as a data product**: 15 templates, LEI/EUID validation, supply-chain ranks, function identifiers; reconcile to contracts and payables before the annual collection. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../workflows/vendor-onboarding.md](../../workflows/vendor-onboarding.md).
4. **Remediate contracts to two checklists**: 2024/1773 Art. 8 clauses plus 2025/532 Art. 4–6 subcontracting terms (notice period, objection right, termination triggers); track residual gaps as exceptions via [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
5. **Map 2024/1774 to the control set**: the RTS is effectively a control catalogue (weekly scanning, 6-month access reviews, annual network review, switchover testing); gap-assess it against ISO 27001 or NIST CSF and evidence it. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md) and [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
6. **Confirm TLPT designation status early**: if in the Art. 2(2) mandatory list, budget for a 3/6-month preparation window, ≥12-week red-team phase, provider qualification files and the 8-week remediation plan. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
7. **Assess CTPP exposure**: map which of the 19 designated providers underpin critical or important functions; expect Lead Overseer recommendations to flow to you through your competent authority (2025/295 Art. 6) and be ready to evidence how you addressed them.
8. **Prepare the Art. 11(10) cost/loss estimate** using the JC/GL/2024/34 method: gross costs/losses and financial recoveries per reference year, on competent-authority request — align with incident final reports. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).
9. **Write the policies the RTS names**: information-security policy, ICT risk-management policy, contractual-arrangements policy, internal-tester policy. See [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).

## Interplay

- **DORA level 1**: this pack is the detail layer; scope, pillars and supervisory design are in [dora.md](dora.md). Where a level-2 figure and a playbook disagree, the level-2 text wins.
- **NIS2**: DORA is lex specialis, but 2025/301 Art. 5(5) explicitly borrows the NIS2 essential/important classification to remove weekend relief for those entities; NIS2's own reporting stages are similar in shape but not identical in trigger or content. See [nis2.md](nis2.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
- **GDPR**: a major incident with personal data runs the DORA 4 h/24 h/72 h/1-month sequence in parallel with the GDPR Art. 33 notification clock — different regulators and templates. See [gdpr.md](gdpr.md).
- **UK critical third parties**: the EU–UK MoU (January 2026) coordinates CTPP oversight with the UK CTP regime; groups spanning both should reconcile the two designation lists. See [uk-financial-operational-resilience.md](uk-financial-operational-resilience.md).
- **EU AI Act**: the ESAs' July 2026 statement (JC 2026 25) treats frontier-AI-accelerated cyber risk as a DORA ICT-risk, testing and incident-response matter for supervised entities rather than a separate regime; see [eu-ai-act.md](eu-ai-act.md).
- **Frameworks**: 2024/1774 maps naturally onto [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) Annex A and [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md); TLPT aligns with TIBER-EU by design.

## Primary sources

- Regulation (EU) 2022/2554 (DORA level 1), for Arts. 11, 16, 18–20, 26, 28, 30, 31, 35, 41, 43 — https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- Delegated Regs. (EU) 2024/1502 (CTPP criticality criteria) and 2024/1505 (oversight fees) — https://eur-lex.europa.eu/eli/reg_del/2024/1502/oj and https://eur-lex.europa.eu/eli/reg_del/2024/1505/oj
- Delegated Regs. (EU) 2024/1772 (incident classification), 2024/1773 (contractual policy) and 2024/1774 (ICT risk management) — https://eur-lex.europa.eu/eli/reg_del/2024/1772/oj, https://eur-lex.europa.eu/eli/reg_del/2024/1773/oj, https://eur-lex.europa.eu/eli/reg_del/2024/1774/oj
- Implementing Reg. (EU) 2024/2956 (register of information) — https://eur-lex.europa.eu/eli/reg_impl/2024/2956/oj; corrigendum of 19 Sep 2025 — https://eur-lex.europa.eu/eli/reg_impl/2024/2956/corrigendum/2025-09-19/oj
- Delegated Regs. (EU) 2025/295 (conduct of oversight) and 2025/420 (joint examination teams) — https://eur-lex.europa.eu/eli/reg_del/2025/295/oj and https://eur-lex.europa.eu/eli/reg_del/2025/420/oj
- Delegated Reg. (EU) 2025/301 and Implementing Reg. (EU) 2025/302 (incident reporting) — https://eur-lex.europa.eu/eli/reg_del/2025/301/oj and https://eur-lex.europa.eu/eli/reg_impl/2025/302/oj
- Delegated Regs. (EU) 2025/532 (subcontracting) and 2025/1190 (TLPT) — https://eur-lex.europa.eu/eli/reg_del/2025/532/oj and https://eur-lex.europa.eu/eli/reg_del/2025/1190/oj
- ESMA DORA policy index — https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/digital-operational-resilience-act-dora; DORA Oversight page (opt-in process) — https://www.esma.europa.eu/dora-oversight; list of designated CTPPs, November 2025 — https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf
- Joint Guidelines JC/GL/2024/34 on aggregated annual costs and losses (final report, 17 Jul 2024) — https://www.esma.europa.eu/sites/default/files/2024-07/JC_2024-34_-_Final_report_GL_on_costs_and_losses.pdf
- Joint Guidelines JC/GL/2024/36 on oversight cooperation (6 Nov 2024) — https://www.esma.europa.eu/sites/default/files/2024-11/JC-GL-2024-36_Guidelines_on_DORA_oversight_cooperation.pdf
- ESAs Decision ESA 2024 22 on reporting for CTPP designation, consolidated text — https://www.esma.europa.eu/sites/default/files/2024-11/ESA_2024_22_Decision_on_reporting_of_information_for_CTPP_designation.pdf
- ESAs response to the Commission's rejection of the register ITS (15 Oct 2024) — https://www.esma.europa.eu/press-news/esma-news/esas-respond-european-commissions-rejection-technical-standards-registers; ESAs Opinion JC 2025 06 on the rejection of the subcontracting RTS (7 Mar 2025) — https://www.esma.europa.eu/sites/default/files/2025-03/JC_2025_06_-_ESAs_Opinion_on_the_rejection_of_the_RTS_on_subcontracting_under_DORA.pdf
- 2024 register dry-run summary report (ESA 2024 35) — https://www.eba.europa.eu/sites/default/files/2024-12/c1454b59-15cc-445e-be14-966e3338cedc/ESA%202024%2035%20DORA%20Dry%20Run%20exercise%20summary%20report%20for%20publication.pdf; EBA "Preparation for DORA application" (register tooling and validation feedback) — https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act/preparation-dora-application
- ESAs JC 2025 85 report under DORA Art. 58(3), 4 Dec 2025 — https://www.esma.europa.eu/sites/default/files/2025-12/JC-2025-85_Joint_ESAs_Report_in_response_to_the_European_Commission_consultation_pursuant_to_Article_58_3__of_Regulation__EU__20222554__DORA_.pdf
- ESAs–UK MoU on CTPP oversight, January 2026 — https://www.esma.europa.eu/sites/default/files/2026-01/MoU_DORA_oversight_ICT_CTPPs__EU-UK.pdf
- ESAs JC 2026 16, 2025 report on major ICT-related incidents (3 Jun 2026) — https://www.esma.europa.eu/sites/default/files/2026-06/JC_2026_16_ESAs_2025_report_on_major_ICT-related_incidents.pdf; ESAs JC 2026 25 statement on ICT risks from frontier AI models (31 Jul 2026) — https://www.esma.europa.eu/sites/default/files/2026-07/JC_2026_25_ESA_statement_on_frontier_AI_models.pdf
- ESA staff operational instructions on DORA incident reporting (16 Sep 2026) — https://www.esma.europa.eu/sites/default/files/2026-09/DORA_Incident_reporting_-_Operational_instructions.pdf


---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
