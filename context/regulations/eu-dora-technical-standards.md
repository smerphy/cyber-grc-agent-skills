# DORA Level-2 and Level-3 Layer — RTS/ITS Technical Standards, Delegated Acts and ESA Guidelines

This pack covers the delegated/implementing regulations and ESA guidelines that put numbers on Regulation (EU) 2022/2554. It does not restate the level-1 summary — read [dora.md](dora.md) first for scope, the five pillars and supervisory architecture.

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | 12 Commission delegated/implementing regulations adopted under DORA empowerments (Arts. 15, 16(3), 18(4), 20, 26(11), 28(9), 28(10), 30(5), 31(6), 41, 43(2)) plus two sets of joint ESA guidelines (Arts. 11(11), 32(7)) |
| Legal nature | Directly applicable EU regulations, no transposition; each entered into force on the 20th day after Official Journal (OJ) publication and applies alongside DORA (applicable since 17 January 2025) |
| Drafters / adopters | Drafted by the three ESAs (EBA, EIOPA, ESMA) through the Joint Committee; adopted by the European Commission; two drafts (register ITS, subcontracting RTS) were first rejected by the Commission and re-adopted with changes |
| Publication window | 30 May 2024 (criticality criteria, fees) to 2 July 2025 (subcontracting RTS) — the last standard landed almost six months after DORA started applying |
| Headline clocks | Major incident: initial notification within 4 h of classification and no later than 24 h of awareness; intermediate report within 72 h of the initial; final report within 1 month of the (last) intermediate |
| Headline thresholds | Major = critical services affected + either a successful malicious unauthorised access or any two other thresholds (e.g. >10% of clients or >100,000 clients; >24 h duration or >2 h downtime of a critical/important function; impact in ≥2 Member States; costs ≥ EUR 100,000) |
| Oversight economics | Minimum annual CTPP oversight fee EUR 50,000; opt-in application fee EUR 50,000 (non-refundable); Lead Overseer periodic penalty payments up to 1% of average daily worldwide turnover per day, max six months (DORA Art. 35) |
| First CTPP list | 19 providers published by the ESAs in November 2025 (Art. 31(9) list; updated annually) |
| Who must read this | Any team building a DORA incident playbook, register of information, ICT contract checklist, TLPT programme or CTPP-exposure assessment — the level-1 text alone is not enough to be compliant |

## What it is

DORA is a two-tier regime. The regulation sets principles and mandates the ESAs to draft Regulatory Technical Standards (RTS, adopted as Commission Delegated Regulations) and Implementing Technical Standards (ITS, adopted as Commission Implementing Regulations). The Commission separately adopted two delegated acts on its own initiative (CTPP criticality criteria and oversight fees). The ESAs add a level-3 layer of joint guidelines, Q&As, decisions on data collection and non-binding "operational instructions". Together these carry nearly every number a practitioner needs: materiality thresholds, report deadlines, register templates, TLPT phase durations, tester qualifications, fee formulas.

The standards were delivered in two batches (first-batch final drafts January 2024, second batch July 2024) and published between May 2024 and July 2025. Two were politically contested: the Commission rejected the ESAs' draft register ITS on 3 September 2024 because it mandated LEI-only identification of providers (the adopted text allows LEI or EUID for EU-established providers), and rejected the draft subcontracting RTS in early 2025 (ESAs' Opinion on the rejection, 7 March 2025) before adopting a revised version on 24 March 2025.

## Who it covers / Scope

Every instrument follows DORA's scope (Art. 2 financial entities; ICT third-party providers via contract and, for CTPPs, direct oversight). Specific carve-outs in the level-2 layer:

- **Simplified-framework entities** (DORA Art. 16(1)) and **microenterprises**: covered by Title III of the ICT-risk RTS (2024/1774, Arts. 28–41) instead of Title II; exempt from the recurring-incident aggregation rule (2024/1772 Art. 8(2)); no TLPT.
- **TLPT population**: only entities identified by the TLPT authority under 2025/1190 Art. 2 (see below); microenterprises and Art. 16(1) entities are outside.
- **Weekend/bank-holiday relief** on report deadlines does not apply to initial or intermediate reports from credit institutions, CCPs, trading-venue operators or entities that are essential/important under NIS2 (2025/301 Art. 5(5)); authorities may withdraw it from other significant entities (Art. 5(6)).
- **Aggregated incident reporting** by a provider on behalf of several entities is barred for significant credit institutions (SSM), trading-venue operators and CCPs (2025/302 Art. 7(2)).
- **CTPP designation** is assessed per provider or per group, and can extend to subcontractors of a provider (2024/1502 recital and Art. 1).

## Core obligations

### Instrument map

| Instrument | Subject (DORA basis) | OJ date | In force | Key numbers |
|---|---|---|---|---|
| Delegated Reg. (EU) 2024/1502 | Criteria for designating CTPPs (Art. 31(6)) | 30 May 2024 | 19 Jun 2024 | Two-step test; step-1 quantitative shares of ≥10% of a financial-entity category; G-SII/O-SII counts; sub-criterion 1.4 applied from 16 Jan 2025 |
| Delegated Reg. (EU) 2024/1505 | CTPP oversight fees (Art. 43(2)) | 30 May 2024 | 19 Jun 2024 | Fee ∝ EU turnover from ICT services to financial entities (year n-2, audited, due 31 Dec); minimum EUR 50,000; opt-in fee EUR 50,000; pay by 30 Apr |
| Delegated Reg. (EU) 2024/1772 | Incident classification, materiality thresholds, significant cyber threats (Art. 18(4)) | 25 Jun 2024 | 15 Jul 2024 | Thresholds in Art. 9; major-incident rule in Art. 8; recurring incidents ≥2 in 6 months |
| Delegated Reg. (EU) 2024/1773 | Policy on contracts for ICT services supporting critical or important functions (Art. 28(10)) | 25 Jun 2024 | 15 Jul 2024 | Management body reviews policy at least yearly; lifecycle phases; exit plans reviewed and tested |
| Delegated Reg. (EU) 2024/1774 | ICT risk-management tools/policies + simplified framework (Arts. 15, 16(3)) | 25 Jun 2024 | 15 Jul 2024 | 42 articles; weekly vulnerability scans on critical/important-function assets; access reviews every 6 months for those systems, yearly otherwise |
| Implementing Reg. (EU) 2024/2956 | Register-of-information templates (Art. 28(9)) | 2 Dec 2024 | 22 Dec 2024 | 15 templates (B_01.01 to B_99.01) in Annex I; 19 ICT service types (S01–S19) in Annex III; LEI or EUID |
| Delegated Reg. (EU) 2025/295 | Harmonised conditions for oversight activities (Art. 41) | 13 Feb 2025 | 5 Mar 2025 | Opt-in application content; CTPP information and remediation-plan reporting; subcontracting template |
| Delegated Reg. (EU) 2025/301 | Content and time limits of major-incident reports; cyber-threat notification (Art. 20) | 20 Feb 2025 | 12 Mar 2025 | 4 h / 24 h; 72 h; 1 month; noon-next-working-day relief |
| Implementing Reg. (EU) 2025/302 | Forms, templates and procedures for incident reports and threat notifications (Art. 20) | 20 Feb 2025 | 12 Mar 2025 | Single incident template (Annex I) with glossary (Annex II); threat template (Annex III) |
| Delegated Reg. (EU) 2025/420 | Joint examination teams (Art. 41) | 24 Mar 2025 | 13 Apr 2025 | Composition set by Lead Overseer with the Joint Oversight Network after consulting the Oversight Forum; members nominated by Art. 40(2) authorities |
| Delegated Reg. (EU) 2025/1190 | TLPT criteria, methodology, internal testers, cooperation (Art. 26(11)) | 18 Jun 2025 | 8 Jul 2025 | Mirrors TIBER-EU; active red-team phase ≥12 weeks; 3/6-month preparation deadlines; 4/10/8-week closure clocks |
| Delegated Reg. (EU) 2025/532 | Subcontracting of ICT services supporting critical or important functions (Art. 30(5)) | 2 Jul 2025 | 22 Jul 2025 | Pre-contract subcontracting decision; notice-and-objection right on material changes; termination triggers |
| ESA Guidelines JC 2024 34 | Estimating aggregated annual costs and losses from major ICT incidents (Art. 11(11)) | — | applies from 19 May 2025 | Gross costs/losses and financial recoveries per reference year, on competent-authority request |
| ESA Guidelines JC/GL/2024/36 | Cooperation between ESAs and competent authorities on oversight (Art. 32(7)) | — | applies from 17 Jan 2025 | Information exchange and structure of oversight cooperation |

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
| Initial notification | As early as possible, within 4 h of classifying the incident as major and no later than 24 h from becoming aware; if classified as major after the 24 h mark, within 4 h of classification | Entity reference code, detection date/time and classification, impact description, Member States affected, whether third-party originated (Art. 2) |
| Intermediate report | Within 72 h of the initial notification even if nothing changed; updated without undue delay and in any case when regular activities are recovered | Authority reference code, occurrence date/time, threshold data, actions taken (Art. 3) |
| Final report | No later than 1 month after the intermediate report or the latest updated intermediate | Root causes, actual impact figures, costs and losses, recurrence information (Art. 4) |

- Deadline falling on a weekend or bank holiday: submit by noon of the next working day (Art. 5(4)) — except initial/intermediate reports from credit institutions, CCPs, trading-venue operators and NIS2 essential/important entities (Art. 5(5)).
- Cannot meet a deadline: inform the authority before it expires with reasons (Art. 5(3)).
- One template for all three stages (2025/302 Art. 1, Annex I); stages may be combined if deadlines are still met (Art. 2); submit via the authority's secure electronic channel (Art. 4); reclassification from major to non-major must be notified (Art. 5); outsourcing of reporting must be notified to the authority before the first report (Art. 6); provider-led aggregated reports allowed only within one Member State, same authority, each entity having classified the incident as major, and with explicit authority permission (Art. 7).
- Cyber-threat notifications use Annex III/IV (Art. 8; content in 2025/301 Art. 6).
- ESA staff "Operational Instructions" on incident reporting (16 September 2026) harmonise field-level practice for authorities — non-binding, but they reveal how reports are read (English templates, versioning of corrected reports, third-party origin field).

### ICT risk-management framework detail (2024/1774)

- **Title II (Arts. 2–27)** — full framework: ICT risk-management policy with annual review of accepted residual risks (Art. 3); asset management (Arts. 4–5); encryption and key management (Arts. 6–7); operations, capacity, vulnerability and patch management including weekly automated scanning for critical/important-function assets (Arts. 8–10); data/system security, logging, network security with annual architecture review (Arts. 11–14); project, acquisition and change management (Arts. 15–17); physical security and HR policy (Arts. 18–19); identity and access control with access-rights reviews at least yearly, and every 6 months for critical/important-function systems (Arts. 20–21); incident management policy and detection criteria (Arts. 22–23); ICT business continuity policy, plan testing with switchover scenarios, and response/recovery plans (Arts. 24–26); the Art. 6(5) framework-review report to the authority in searchable electronic format (Art. 27).
- **Title III (Arts. 28–41)** — simplified framework: management-body accountability and annual budget review (Art. 28), a single information security policy (Art. 29), classification, risk management, physical security, access control, operations security, data/network security, security testing plan, acquisition/change management, continuity plan and testing, and a review report (Arts. 30–41).

### Third-party layer (2024/1773, 2025/532, 2024/2956)

- **Contractual policy RTS 2024/1773**: management-body-approved policy reviewed at least yearly (Art. 3); method for identifying ICT services supporting critical or important functions; senior-management owner; consistency with the ICT risk framework, information-security policy, continuity policy and incident reporting; lifecycle phases (Art. 4); ex-ante risk assessment including concentration and sub-outsourcing (Art. 5); due diligence (Art. 6); conflicts of interest (Art. 7); contract clauses including audit rights exercised via own/appointed audits, pooled audits and pooled testing including TLPT, and third-party certifications (Art. 8); monitoring (Art. 9); documented exit plans, periodically reviewed and tested (Art. 10).
- **Subcontracting RTS 2025/532**: decide before contracting whether subcontracting of critical/important-function services is allowed, subject to ten conditions covering provider due diligence, subcontractor identification, flow-down of access/audit rights, location and concentration risk (Art. 3); mandatory contract content on subcontracted services (Art. 4); provider must give notice of material subcontracting changes with a notice period for the entity to approve or object, and may implement only after approval or non-objection (Art. 5); termination rights where changes are implemented over an objection, before the notice period ends, or where unapproved subcontracting occurs (Art. 6).
- **Register ITS 2024/2956**: 15 templates across entity, sub-consolidated and consolidated levels (Art. 5); every provider ranked in the supply chain (rank 1 = direct provider, subcontractors >1, Art. 2); all direct providers plus all subcontractors that effectively underpin critical/important-function services (Art. 3(2)); LEI or EUID for EU legal persons, LEI only for third-country providers (Art. 3(5)–(6)); six data-quality principles; one value per cell (Art. 4).
- **Collection calendar** (ESAs Decision ESA 2024 22, 8 Nov 2024, updated 29 Jan 2025): competent authorities transmitted 2025 registers to the ESAs by 30 April 2025 (reference date 31 March 2025); thereafter annually by 31 March with a 31 December reference date. National deadlines for entity-to-authority submission sit earlier — check the authority's own notice.
- The 2024 dry run (~1,000 entities) saw only 6.5% of registers pass all 116 data-quality checks — expect validation failures on identifiers, function mapping and consolidation consistency.

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
- **Enforcement on CTPPs**: DORA Art. 35(6)–(8) periodic penalty payments after 30 days' non-compliance, daily, up to 1% of average daily worldwide turnover, for no more than six months; publicly disclosed unless disproportionate.

## Enforcement and penalties

The level-2 acts create no new sanctions. Breach of any RTS/ITS is a breach of DORA and is enforced by the national competent authority under the Member State's Art. 50 administrative-penalty regime (see [dora.md](dora.md)); the only EU-level pecuniary tool is the Lead Overseer's periodic penalty payment on CTPPs above. Practically, the standards define the evidence supervisors ask for: the register (annual collection), the Art. 6(5) framework-review report, incident reports in the ITS template, TLPT attestations and remediation plans, and contract files against the 2024/1773 and 2025/532 checklists. The ESAs' report on 2025 major incidents (JC 2026 16, 3 June 2026, under DORA Art. 22) counted 3,383 major incidents reported in 2025, over 60% in the credit sector and 16% in payments, about one third with cross-border impact and almost one third originating from third-party failures — and noted divergent reporting practices across jurisdictions, which the September 2026 operational instructions aim to narrow.

## Timeline and status

| Date | Event |
|---|---|
| 17 Jan 2024 | ESAs submit the draft register ITS (part of the first batch of DORA standards) to the Commission |
| 30 May 2024 | Delegated Regs. 2024/1502 (criticality) and 2024/1505 (fees) published |
| 25 Jun 2024 | Delegated Regs. 2024/1772, 2024/1773, 2024/1774 published |
| 17 Jul – 26 Jul 2024 | ESAs deliver second-batch drafts (incident reporting RTS/ITS, TLPT, oversight harmonisation, JET, costs/losses guidelines; subcontracting RTS final report 26 Jul 2024) |
| 3 Sep 2024 | Commission rejects draft register ITS over LEI-only identification; ESAs' Opinion 15 Oct 2024 |
| 2 Dec 2024 | Implementing Reg. 2024/2956 (register ITS) published with LEI-or-EUID rule |
| 17 Jan 2025 | DORA applies; JC/GL/2024/36 oversight-cooperation guidelines apply |
| 13 Feb – 24 Mar 2025 | 2025/295 (oversight harmonisation), 2025/301 and 2025/302 (incident reporting), 2025/420 (JET) published |
| 7 Mar 2025 | ESAs' Opinion on the Commission's rejection of the draft subcontracting RTS |
| 30 Apr 2025 | First register-of-information collection reaches the ESAs (reference date 31 Mar 2025) |
| 19 May 2025 | JC 2024 34 costs/losses guidelines apply |
| 18 Jun 2025 | Delegated Reg. 2025/1190 (TLPT) published |
| 2 Jul 2025 | Delegated Reg. 2025/532 (subcontracting) published — the last mandated standard |
| Nov 2025 | ESAs publish the first list of designated CTPPs (19 providers, including major cloud, data, telecom and IT-services groups) |
| 4 Dec 2025 | ESAs' Art. 58(3) report on whether statutory auditors should be brought into DORA scope |
| Jan 2026 | ESAs–UK (BoE, PRA, FCA) MoU on cooperation and coordination of CTPP oversight |
| 3 Jun 2026 | First ESAs annual report on major ICT incidents (JC 2026 16, covering 2025) |
| 31 Jul 2026 | ESAs statement on ICT risks from frontier AI models |
| 16 Sep 2026 | ESA staff operational instructions on DORA incident reporting |

**Status as of September 2026:** all mandated RTS/ITS are adopted and in force; no amending delegated act had been published in the sources reviewed. Watch items: annual CTPP list updates, further ESAs guidance on incident reporting consistency, and any Commission simplification proposals touching DORA reporting (verify).

## Key obligations for security/GRC teams

1. **Embed the Art. 8/9 major-incident test in triage**: encode the six thresholds and the critical-services gate as decision fields; run the monthly recurring-incident check; log the classification timestamp because the 4 h clock starts there. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
2. **Pre-build the 2025/302 template** in the authority's portal format with the initial, intermediate and final field sets; decide in advance whether weekend relief applies to your entity type and whether reporting is outsourced (notify before first use).
3. **Own the register of information as a data product**: 15 templates, LEI/EUID validation, supply-chain ranks, function identifiers; reconcile to contracts and payables before the annual collection. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../workflows/vendor-onboarding.md](../../workflows/vendor-onboarding.md).
4. **Remediate contracts to two checklists**: 2024/1773 Art. 8 clauses plus 2025/532 Art. 4–6 subcontracting terms (notice period, objection right, termination triggers); track residual gaps as exceptions via [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
5. **Map 2024/1774 to the control set**: the RTS is effectively a control catalogue (weekly scanning, 6-month access reviews, annual network review, switchover testing); gap-assess it against ISO 27001 or NIST CSF and evidence it. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md) and [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
6. **Confirm TLPT designation status early**: if in the Art. 2(2) mandatory list, budget for a 3/6-month preparation window, ≥12-week red-team phase, provider qualification files and the 8-week remediation plan. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
7. **Assess CTPP exposure**: map which of the 19 designated providers underpin critical or important functions; expect Lead Overseer recommendations to flow to you through your competent authority (2025/295 Art. 6) and be ready to evidence how you addressed them.
8. **Prepare the Art. 11(11) cost/loss estimate**: gross costs/losses and recoveries per major incident for a reference year, on request — align with incident final reports. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).
9. **Write the policies the RTS names**: information-security policy, ICT risk-management policy, contractual-arrangements policy, internal-tester policy. See [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).

## Interplay

- **DORA level 1**: this pack is the detail layer; scope, pillars and supervisory design are in [dora.md](dora.md). Where a level-2 figure and a playbook disagree, the level-2 text wins.
- **NIS2**: DORA is lex specialis, but 2025/301 Art. 5(5) explicitly borrows the NIS2 essential/important classification to remove weekend relief for those entities; NIS2's own reporting stages are similar in shape but not identical in trigger or content. See [nis2.md](nis2.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
- **GDPR**: a major incident with personal data runs the DORA 4 h/24 h/72 h/1-month sequence in parallel with the GDPR Art. 33 notification clock — different regulators and templates. See [gdpr.md](gdpr.md).
- **UK critical third parties**: the EU–UK MoU (January 2026) coordinates CTPP oversight with the UK CTP regime; groups spanning both should reconcile the two designation lists. See [uk-financial-operational-resilience.md](uk-financial-operational-resilience.md).
- **EU AI Act**: the ESAs' July 2026 statement on frontier AI models signals that AI-supply-chain risk will be treated inside ICT third-party risk; see [eu-ai-act.md](eu-ai-act.md).
- **Frameworks**: 2024/1774 maps naturally onto [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) Annex A and [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md); TLPT aligns with TIBER-EU by design.

## Primary sources

- Commission Delegated Regulation (EU) 2024/1502 (CTPP criticality criteria) — official text, Publications Office (CELEX 32024R1502).
- Commission Delegated Regulation (EU) 2024/1505 (oversight fees) — official text (CELEX 32024R1505).
- Commission Delegated Regulation (EU) 2024/1772 (incident classification) — official text (CELEX 32024R1772).
- Commission Delegated Regulation (EU) 2024/1773 (contractual policy) — official text (CELEX 32024R1773).
- Commission Delegated Regulation (EU) 2024/1774 (ICT risk-management framework) — official text (CELEX 32024R1774).
- Commission Implementing Regulation (EU) 2024/2956 (register of information) — official text (CELEX 32024R2956).
- Commission Delegated Regulation (EU) 2025/295 (oversight harmonisation) — official text (CELEX 32025R0295).
- Commission Delegated Regulation (EU) 2025/301 and Implementing Regulation (EU) 2025/302 (incident reporting) — official texts (CELEX 32025R0301, 32025R0302).
- Commission Delegated Regulation (EU) 2025/420 (joint examination teams) — official text (CELEX 32025R0420).
- Commission Delegated Regulation (EU) 2025/532 (subcontracting) — official text (CELEX 32025R0532).
- Commission Delegated Regulation (EU) 2025/1190 (TLPT) — official text (CELEX 32025R1190).
- Regulation (EU) 2022/2554 (DORA) — official text (CELEX 32022R2554), for Arts. 19, 26, 28, 31, 35.
- ESMA DORA page and DORA Oversight page (https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/digital-operational-resilience-act-dora; https://www.esma.europa.eu/dora-oversight) — regulator guidance index, CTPP list (November 2025), opt-in process.
- ESAs Guidelines JC 2024 34 (costs and losses) and JC/GL/2024/36 (oversight cooperation) — regulator guidance PDFs on esma.europa.eu.
- ESAs Decision ESA 2024 22 on reporting of registers for CTPP designation; ESAs news on the 2024 dry run and on the Commission's rejection of the register ITS — regulator guidance.
- ESAs JC 2026 16 report on 2025 major ICT incidents (3 June 2026); ESA staff Operational Instructions on incident reporting (16 September 2026); ESAs–UK MoU on CTPP oversight (January 2026); JC 2025 85 Art. 58(3) report (4 December 2025) — regulator publications.
- EBA page "Preparations for reporting of DORA registers of information" — regulator guidance.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
