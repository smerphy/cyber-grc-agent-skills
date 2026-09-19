# Switzerland — Federal Act on Data Protection (FADP, SR 235.1) and the Information Security Act cyberattack reporting obligation (ISA, SR 128)

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | **FADP** (Federal Act on Data Protection of 25 September 2020, SR 235.1) with the **Data Protection Ordinance** (DPO, SR 235.11); **ISA** (Information Security Act of 18 December 2020, SR 128) Arts. 74a–74h with the **Cybersecurity Ordinance** (CSO/CSV, AS 2025 169); **FINMA Circular 2023/1** and FINMA Guidance 05/2020 / 03/2024 for supervised financial institutions |
| Regulators | **FDPIC** (Federal Data Protection and Information Commissioner) for the FADP; **NCSC / Federal Office for Cybersecurity (BACS)** in the DDPS for ISA reporting; **FINMA** for financial-sector cyber reporting; cantonal prosecutors for criminal fines |
| Key dates | FADP + DPO in force 1 September 2023; ISA in force 1 January 2024; ISA reporting obligation and CSO in force 1 April 2025; ISA fines (Arts. 74g–74h) in force 1 October 2025; USA added to the Swiss adequacy list 15 September 2024; EU re-confirmed Swiss adequacy 15 January 2024 |
| Who is covered | FADP: any private person or federal body processing personal data of **natural persons** (legal-entity data no longer covered) with an effect in Switzerland; ISA: 21 categories of critical-infrastructure authorities and organisations (Art. 74b) unless exempted by the CSO |
| Breach clocks | FADP Art. 24: controller notifies FDPIC "as quickly as possible" where a breach is likely to result in a **high risk**; ISA Art. 74e: report to NCSC/BACS within **24 hours of discovery**, completion within **14 days** (CSO Art. 16); FINMA: preliminary notification within **24 hours**, EHP report within **72 hours** |
| Penalties | FADP: **criminal fines up to CHF 250,000 on the responsible natural person** (Arts. 60–63), wilful conduct, mostly on complaint; business may be fined instead where ≤ CHF 50,000 (Art. 64); ISA: fine up to **CHF 100,000** for wilfully ignoring a final BACS ruling (Art. 74h). No GDPR-style turnover-based administrative fines |
| Supervisory powers | FDPIC investigates (Art. 49) and can order processing modified, suspended or terminated, data deleted, transfers abroad prohibited (Art. 51) — but cannot itself fine |
| Extraterritorial reach | FADP applies to circumstances with an effect in Switzerland even if initiated abroad (Art. 3); foreign controllers may need a Swiss representative (Art. 14); ISA reporting covers attacks with an effect in Switzerland even if the IT is abroad (Art. 74b(3)) |
| Relationship to EU law | GDPR-aligned but not identical: no accountability-style fines, no mandatory DPO, no fixed 72-hour breach clock; EU adequacy decision for Switzerland maintained (Commission review report of 15 January 2024) |

## What it is

The **revised FADP** is Switzerland's total revision of the 1992 Data Protection Act, adopted 25 September 2020 and in force since 1 September 2023 together with the DPO and the Data Protection Certification Ordinance. Its stated purpose is the protection of the personality and fundamental rights of natural persons whose personal data is processed (Art. 1). The revision aligned Swiss law with the modernised Council of Europe Convention 108 and, in substance, with the GDPR — sufficiently for the European Commission to confirm on 15 January 2024, in its first review of the pre-GDPR adequacy decisions, that Switzerland continues to offer an adequate level of protection. Switzerland is not bound by the GDPR itself; only Directive (EU) 2016/680 applies as part of the Schengen acquis.

The **ISA** governs information security across the federal administration (classification, personnel security screening, ICT security) and, since the amendment of 29 September 2023 brought into force on 1 April 2025, contains Switzerland's first cross-sector **mandatory cyberattack reporting obligation for critical infrastructure** (Arts. 74a–74h), implemented by the Cybersecurity Ordinance of 7 March 2025. The obligation exists solely so that the NCSC can recognise attack patterns early and warn other potentially affected operators (Art. 74a(4)); reporting entities gain a right to NCSC incident-response support (Art. 74a(3)).

For banks and securities firms, **FINMA Circular 2023/1 "Operational risks and resilience – banks"** (dated 7 December 2022, in force 1 January 2024) sets ICT and cyber risk-management expectations, and FINMA Guidance 05/2020 (clarified by Guidance 03/2024 of 7 June 2024) specifies the cyberattack reporting duty under Art. 29(2) FINMASA for all supervised institutions.

## Who it covers / Scope

**FADP**

| Test | Rule |
|---|---|
| Material scope (Art. 2) | Processing of personal data of natural persons by private persons or federal bodies. Excluded: purely personal use, parliamentary deliberations, institutional beneficiaries with immunity |
| Legal entities | Data of legal entities is outside the Act (federal bodies keep certain legacy rules for five years, Art. 71) |
| Territorial scope (Art. 3) | Circumstances that have an effect in Switzerland, even if initiated abroad |
| Representative (Art. 14) | Foreign private controllers must appoint a representative in Switzerland when **all** of the following hold: processing relates to offering goods/services to, or monitoring the behaviour of, persons in Switzerland; is large scale; is regular; and poses a high risk to data subjects. The representative keeps the record of processing and is the contact point for data subjects and the FDPIC (Art. 15) |
| Sensitive personal data (Art. 5(c)) | Religious, philosophical, political, trade-union views; health, private sphere, race/ethnicity; **genetic data**; **biometric data uniquely identifying a person**; administrative/criminal proceedings and sanctions; social assistance measures |
| Profiling / high-risk profiling (Art. 5(f)–(g)) | Defined terms; high-risk profiling triggers logging, processing regulations and consent requirements |

**ISA reporting obligation (Art. 74b)** — 21 categories, including: universities; federal, cantonal and communal authorities and inter-cantonal/communal organisations; security and rescue, drinking-water, wastewater and waste organisations; energy supply, trading, metering and control; institutions under the Banking Act, Insurance Supervision Act or Financial Market Infrastructure Act; hospitals on cantonal hospital lists; licensed medical laboratories; pharmaceutical manufacturers/importers; social and health insurers; SRG SSR and national news agencies; registered postal providers; rail and concessioned public transport; civil aviation and national airports; Rhine shipping and the port of Basel; suppliers of essential daily goods; registered telecoms providers; domain registries and registrars; providers of infrastructure for political rights; **Swiss-domiciled cloud, search-engine, digital security/trust-service and data-centre providers**; and **manufacturers of hardware/software used by critical infrastructures** where the product has remote-maintenance access or is used for OT control/monitoring or public safety. Mixed-activity entities report only attacks affecting the critical activity (Art. 74b(2)). BACS confirms on request whether an entity is subject and issues a ruling (Art. 74a(2)).

**CSO exemptions (Art. 12)** — e.g. universities with fewer than 2,000 students; electricity operators not required to meet protection level A or B under the Electricity Supply Ordinance; gas pipeline operators below 400 GWh/year (five-year average); transport operators without system tasks or jointly ordered services; aviation organisations not required to run an ISMS under the applicable EU rules; cloud/search/trust/data-centre providers that do not provide services to third parties for remuneration; and laboratories, pharma companies, postal providers and essential-goods suppliers employing **fewer than 50 persons** in the affected area with turnover or balance sheet **not exceeding CHF 10 million**.

## Core obligations

### FADP — controller and processor duties

| Obligation | Article | What it requires |
|---|---|---|
| Principles | Art. 6 | Lawfulness, good faith, proportionality, purpose limitation, accuracy, retention limits; consent only where required and then explicit for sensitive data / high-risk profiling |
| Privacy by design and by default | Art. 7 | Technical and organisational arrangement from the planning stage; default settings limit processing to the minimum. Not applied to processing begun before 1 September 2023 if purpose unchanged and no new data (Art. 69) |
| Data security | Art. 8; DPO Arts. 1–6 | Risk-appropriate TOMs for confidentiality, integrity, availability, traceability; DPO Art. 4 **logging** (large-scale sensitive data or high-risk profiling; log retained **at least one year**, separate from the processing system); DPO Art. 5 **processing regulations** for the same cases. Wilful failure to meet the DPO minimum requirements is a criminal offence (Art. 61(c)) |
| Processors | Art. 9; DPO Art. 7 | Contract or law; processor may only process as the controller could; controller must satisfy itself the processor guarantees data security; sub-processing needs prior (specific or general) approval, with objection right |
| Data protection officer | Art. 10; DPO Art. 23 | **Voluntary** for private controllers; if independent, expert, published and notified to the FDPIC, the controller may skip FDPIC consultation after a DPIA (Art. 23(4)) |
| Record of processing activities | Art. 12; DPO Art. 24 | Controller and processor each keep a record (minimum content listed). Exempt: organisations with **fewer than 250 employees** unless large-scale sensitive data or high-risk profiling |
| Duty to inform | Arts. 19–21 | Inform at collection (identity, purpose, recipients; state of destination and safeguards for transfers); indirect collection: within one month; inform of automated individual decisions with review by a natural person |
| DPIA | Art. 22–23; DPO Art. 14 | Prior DPIA where likely high risk (esp. large-scale sensitive data, large-scale systematic monitoring of public areas); consult FDPIC if residual high risk — FDPIC responds within **two months** (+1 for complex cases); retain DPIA **two years** after processing ends. See [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md) and [../../templates/dpia-template.md](../../templates/dpia-template.md) |
| Data subject rights | Arts. 25–29; DPO Art. 18 | Access within **30 days** (extension must be notified); data portability for automated processing based on consent or contract |
| Cross-border disclosure | Arts. 16–18; DPO Annex 1 | Allowed to states on the Federal Council's adequacy list (DPO Annex 1); otherwise treaty, contractual clauses notified to the FDPIC, FDPIC-approved/recognised standard clauses, or approved BCRs; Art. 17 exceptions (explicit consent, contract, legal claims, vital interests). **United States** listed since 15 September 2024 for organisations certified under the Swiss-U.S. Data Privacy Framework only |

### FADP — breach notification (Art. 24; DPO Art. 15)

| Element | Rule |
|---|---|
| Trigger | Breach of data security (Art. 5(h): accidental or unlawful loss, deletion, destruction, modification, or unauthorised disclosure/access) **likely to lead to a high risk** to the data subject's personality or fundamental rights |
| Clock | "As quickly as possible" after becoming aware — no fixed hour count. FDPIC guidelines (v1.2, 23 April 2025): where high risk cannot quickly be excluded, notify; ransomware normally warrants assuming likely high risk; notify **before** deciding on any ransom payment |
| Content (DPO Art. 15(1)) | Form of breach; time and duration; categories/approximate volume of data and of data subjects; consequences and risks; measures taken or planned; contact person. Missing details supplied as quickly as possible |
| Processor | Must notify the controller of **any** breach as quickly as possible — no risk threshold (Art. 24(3)) |
| Data subjects | Inform where required for their protection or when the FDPIC requests; may be limited/delayed where confidentiality duties, impossibility/disproportionate effort, or an equivalent public announcement apply |
| Documentation | Controller documents all breaches (circumstances, effects, measures) and retains for **at least two years** (DPO Art. 15(4)) |
| Channel | FDPIC DataBreach portal (issues time-stamped confirmation, allows follow-up reports); voluntary reports of low-risk breaches accepted |
| Safeguard | A notification may only be used against the notifier in criminal proceedings with their consent (Art. 24(6)) |

### ISA — cyberattack reporting for critical infrastructure

| Element | Rule |
|---|---|
| Reportable attacks (Art. 74d; CSO Art. 14) | (a) functionality of the critical infrastructure endangered — staff or third parties affected by system outages, or operations only sustainable via emergency plans; (b) manipulation or leakage of information — business-relevant information viewed/altered/disclosed by unauthorised persons, **or an FADP Art. 24 breach notification has been made**; (c) undetected for an extended period — incident more than **90 days** old, esp. staging for further attacks; (d) extortion, threats or coercion against the entity or its personnel |
| Clock (Art. 74e; CSO Art. 16) | Report within **24 hours of discovery**; if information is incomplete, BACS grants **14 days** to complete; after that, BACS demands the missing details or a confirmation they do not exist |
| Content (Art. 74e(2); CSO Art. 15) | Reporting entity; nature and execution of the attack; effects; measures taken; planned next steps; date/time of detection and of attack; attacker details; whether extortion involved and whether a criminal complaint was filed; severity of impact on availability, integrity, confidentiality; impact on functionality |
| Channel (Art. 74f; CSO Art. 17) | NCSC Cyber Security Hub reporting form; unregistered entities by e-mail form. The system lets the reporter forward the report, in whole or in part, to other authorities (e.g. FINMA, FDPIC); information beyond Art. 74e goes directly to those authorities without BACS access |
| Protections | No self-incriminating statements required (Art. 74e(4)); third-party information in reports is excluded from Freedom of Information Act access |
| Enforcement (Arts. 74g–74h, from 1 October 2025) | BACS first notifies the entity and sets a deadline; then issues a ruling with a new deadline and a penalty warning; only wilful non-compliance with a final ruling is punishable — fine up to **CHF 100,000**; business may be fined instead of individuals where ≤ CHF 20,000; cantons prosecute |

### FINMA — banks and other supervised institutions

| Element | Rule |
|---|---|
| Circular 2023/1 scope | Banks, persons under Art. 1b BA, securities firms, financial groups and conglomerates; proportional application; Category 4 and 5 institutions exempt from listed margin numbers. Transitional periods of one and two years from 1 January 2024 for the operational-resilience requirements |
| Cyber risk management | Identify institution-specific threat landscape; protect inventoried ICT assets and electronic critical data; timely logging and detection; response and containment; recovery — per internationally recognised standards; scenario-based cyber exercises (red teaming expected for systemically important institutions, Guidance 03/2024) |
| Cyber reporting (Art. 29(2) FINMASA; Guidance 05/2020, 03/2024) | Initial criticality assessment and **preliminary notification to FINMA within 24 hours** of discovery (e-mail/phone to key account manager); report via the **EHP platform within 72 hours**; conclusive root-cause analysis at case close. Deadlines run on bank working days except "severe" attacks (24 hours, calendar). Clock starts when the institution **or its outsourcing provider** identifies the incident. ISA-subject institutions may send the 24-hour notice via the NCSC form with forwarding to FINMA; the 72-hour EHP report remains mandatory |

## Enforcement and penalties

| Regime | Mechanism |
|---|---|
| FADP — criminal fines (Arts. 60–63) | Up to **CHF 250,000** on private persons who **wilfully**: give false/incomplete information to data subjects or fail the duty to inform; give false information to or refuse cooperation with the FDPIC; disclose data abroad in breach of Arts. 16–17; engage a processor without meeting Art. 9; fail the DPO minimum security requirements; breach professional confidentiality; or disregard an FDPIC ruling. Prosecuted by the cantons, mostly on complaint (the FDPIC may file); five-year limitation (Art. 66). Fines target the responsible **individual**; under Art. 64 the business may be ordered to pay instead where a fine of at most CHF 50,000 is in play and identifying the perpetrator would be disproportionate |
| FADP — administrative measures (Arts. 49–51) | FDPIC investigation ex officio or on report; binding orders to modify, suspend or terminate processing, delete data, prohibit transfers abroad, conduct a DPIA, inform data subjects or the FDPIC; official warning where compliance restored during investigation; publication of findings where public interest requires |
| ISA (Arts. 74g–74h) | Graduated: notice with deadline → ruling with new deadline and penalty warning → criminal complaint; fine up to CHF 100,000 for wilful disregard of the final ruling. Sanctions in force since 1 October 2025 |
| FINMA | Supervisory law enforcement under FINMASA (no separate fine schedule for cyber reporting in the circular); reporting failures surface through audits and on-site reviews |

## Timeline and status

| Date | Event |
|---|---|
| 25 Sep 2020 | Parliament adopts revised FADP |
| 1 Sep 2023 | FADP, DPO and Data Protection Certification Ordinance in force |
| 29 Sep 2023 | Parliament adopts ISA amendment introducing the cyberattack reporting obligation |
| 1 Jan 2024 | ISA (except reporting provisions) in force; FINMA Circular 2023/1 in force |
| 15 Jan 2024 | European Commission review report maintains the EU adequacy decision for Switzerland |
| 7 Jun 2024 | FINMA Guidance 03/2024 clarifies 24h/72h cyber reporting and NCSC forwarding |
| 15 Sep 2024 | Swiss-U.S. Data Privacy Framework: USA added to DPO Annex 1 for certified organisations |
| 6 Feb 2025 (v1.2: 23 Apr 2025) | FDPIC guidelines on Art. 24 breach reporting and informing data subjects |
| 7 Mar 2025 | Federal Council adopts the Cybersecurity Ordinance and sets commencement |
| 1 Apr 2025 | ISA reporting obligation (Arts. 74a–74f) and CSO in force |
| 29 Sep 2025 | NCSC six-month review: 164 mandatory reports (DDoS 18.1%, hacking 16.1%, ransomware 12.4%); financial sector most affected (19%) |
| 1 Oct 2025 | ISA Arts. 74g–74h (fines) in force |
| H1 2026 | 200 mandatory critical-infrastructure reports per the BACS semi-annual report (secondary summary — verify against the report) |
| Sep 2026 status | No FADP amendment pending on the Federal Office of Justice dossier (updated 18 March 2026). The EU-U.S. DPF, on which the Swiss framework is modelled, was upheld by the EU General Court on 3 September 2025 (Latombe, T-553/23) with an appeal pending before the CJEU — a monitoring item for Swiss-U.S. DPF reliance (verify current status) |

## Key obligations for security/GRC teams

1. **Confirm applicability on both axes**: FADP (any effect in Switzerland; representative test under Art. 14) and ISA Art. 74b category plus CSO Art. 12 exemptions — request a BACS ruling if unclear. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Build a three-clock incident playbook**: NCSC within 24 hours of discovery (+14 days to complete), FINMA 24h/72h where supervised, FDPIC "as quickly as possible" for high-risk personal-data breaches — and remember CSO Art. 14(2)(b): an FDPIC notification itself makes the attack ISA-reportable. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md), [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md) and [../../workflows/incident-regulatory-response.md](../../workflows/incident-regulatory-response.md).
3. **Register on the NCSC Cyber Security Hub** before an incident and pre-configure forwarding to FINMA/FDPIC; capture the CSO Art. 15 data fields (detection time, attack time, attacker, extortion, criminal complaint, CIA severity) in the incident record.
4. **Meet the DPO minimum security requirements** (DPO Arts. 1–6): risk-based TOMs, logging with one-year separate retention, processing regulations for large-scale sensitive data or high-risk profiling — these are the criminally sanctioned baseline (Art. 61(c)). Map to [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) Annex A via [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).
5. **Contract processors to Art. 9 / DPO Art. 7**: security assurance, sub-processor approval mechanics, and unconditional breach notification to the controller; for FINMA institutions add the provider's duty to report cyber incidents so the 24-hour clock can be met. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
6. **Maintain the record of processing and DPIA register** (250-employee exemption with sensitive-data/profiling carve-back; DPIA retained two years; FDPIC consultation or DPO route documented).
7. **Manage transfers**: check DPO Annex 1, use FDPIC-recognised standard clauses elsewhere, verify Swiss-U.S. DPF certification status of US recipients and keep fallback clauses given the pending CJEU appeal.
8. **Assign personal accountability**: because FADP fines hit individuals, name the accountable decision-makers for transfers, processor engagement and security minimums in policy and evidence their sign-offs. See [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).
9. **Track developments**: FDPIC guidance updates, BACS semi-annual reports, FINMA guidance and the EU-U.S. DPF litigation. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

- **GDPR**: Swiss companies offering goods/services to or monitoring people in the EU face GDPR Art. 3(2) directly, with its 72-hour Art. 33 clock and administrative fines — run both regimes in parallel rather than treating FADP compliance as sufficient. FADP terminology differs (no "legitimate interest" balancing as a lawfulness gate for private controllers; "overriding interest" justifications under Art. 31 instead). See [gdpr.md](gdpr.md).
- **NIS2 / DORA**: Switzerland is outside both. Swiss groups with EU subsidiaries or EU-facing financial entities meet NIS2 or DORA there; the ISA 24-hour trigger set (functionality, leakage, dwell time, extortion) is broader in some respects than NIS2's "significant incident" test and DORA's "major incident" thresholds. See [nis2.md](nis2.md) and [dora.md](dora.md).
- **EU adequacy both ways**: EU→CH transfers rest on the Commission's maintained adequacy decision; CH→EU/EEA transfers are free because EU/EEA states sit on DPO Annex 1.
- **FINMA vs ISA**: banks, insurers and FMIs are ISA-subject (Art. 74b(1)(e)) and FINMA-supervised — one NCSC form can serve the 24-hour notice to both, but FINMA's 72-hour EHP report and root-cause analysis remain separate.
- **Breach timeline comparison**: see [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md); other non-EU regimes in [other-jurisdictions.md](other-jurisdictions.md).

## Primary sources

- Federal Act on Data Protection (FADP, SR 235.1), English translation, status 1 September 2023 — legal text: https://www.fedlex.admin.ch/eli/cc/2022/491/en
- Data Protection Ordinance (DPO, SR 235.11), status 15 September 2024 (Annex 1 adequacy list incl. USA) — legal text: https://www.fedlex.admin.ch/eli/cc/2022/568/en
- Information Security Act (ISA, SR 128), German consolidated text, status 1 October 2025 (Arts. 74a–74h) — legal text (no official English translation): https://www.fedlex.admin.ch/eli/cc/2022/232/de
- Cybersecurity Ordinance (CSO/CSV), AS 2025 169, of 7 March 2025 — legal text (German): https://www.fedlex.admin.ch/eli/oc/2025/169/de
- FDPIC, Guidelines on reporting data security breaches and informing data subjects under Art. 24 FADP, v1.2 (23 April 2025) — regulator guidance: https://www.edoeb.admin.ch/en/guidelines-data-breach
- FDPIC, Adequacy page and 15 January 2024 statement on the EU adequacy review — regulator guidance: https://www.edoeb.admin.ch/en/adequacy
- FDPIC, New Swiss-US Data Privacy Framework (15 August 2024) — regulator guidance: https://www.edoeb.admin.ch/en/15082024-new-swiss-us-data-privacy-framework
- Federal Office of Justice, New data protection legislation dossier (updated 18 March 2026) — publisher page: https://www.bj.admin.ch/en/new-data-protection-legislation
- NCSC/BACS, Reporting cyberattacks on critical infrastructure mandatory from 1 April 2025 (7 March 2025) and Legal basis for the reporting obligation — regulator guidance: https://www.bacs.admin.ch/en/25-mp-en ; https://www.bacs.admin.ch/en/legal-basis-for-the-reporting-obligation
- Federal press release, Six-month reporting obligation for cyberattacks on critical infrastructures (29 September 2025) — regulator guidance: https://www.bag.admin.ch/en/newnsb/gezctyF6KYR7UkCjXBC5s
- FINMA Circular 2023/1 Operational risks and resilience – banks (7 December 2022) — regulator text: https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/rundschreiben/finma-rs-2023-01-20221207.pdf
- FINMA Guidance 03/2024 (7 June 2024) and FINMA cyber-risk dossier pages — regulator guidance: https://www.finma.ch/en/documentation/dossier/dossier-cyberrisiken/new-cyber-supervisory-approach-and-guidance/
- Secondary (used only for the H1 2026 report count and DPF litigation context): eBanking – but secure! summary of the BACS semi-annual report 2026/1 (1 September 2026); Homburger and VISCHER client briefings on the Swiss-U.S. DPF and the ISA amendment.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
