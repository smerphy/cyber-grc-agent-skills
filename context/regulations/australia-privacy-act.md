# Privacy Act 1988 (Cth) — Australian Privacy Principles and the Notifiable Data Breaches scheme

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Privacy Act 1988 (Cth), Act No. 119, 1988. Current compilation No. 104 (C2026C00227), compiled 4 June 2026, incorporating amendments to Act No. 75, 2025. Supported by the Privacy Regulations 2025 (in force 1 April 2026, replacing the Privacy Regulation 2013 without substantive change) |
| Regulator | Office of the Australian Information Commissioner (OAIC) — Information Commissioner and Privacy Commissioner. Administered by the Attorney-General's Department (and Treasury for credit reporting) |
| Structure | Part II definitions and exemptions; Part IIIA credit reporting; Part IIIC Notifiable Data Breaches (NDB); Part V investigations; Part VIB compliance and enforcement (civil penalties, infringement and compliance notices); Schedule 1 — 13 Australian Privacy Principles (APPs); Schedule 2 — statutory tort for serious invasions of privacy |
| Who is covered | "APP entities": Commonwealth agencies and "organisations" — private-sector bodies that are not small business operators (annual turnover A$3,000,000 or less, s 6D). Health service providers, information traders and several other classes lose the exemption regardless of turnover. Extraterritorial reach via the "Australian link" test (s 5B) |
| Breach clock | NDB scheme: suspected breach → reasonable and expeditious assessment, all reasonable steps to complete within **30 days** (s 26WH); reasonable grounds to believe → statement to the Commissioner and notification of individuals **as soon as practicable** (ss 26WK–26WL) |
| Penalty ceiling | Serious interference (s 13G): body corporate — greatest of A$50,000,000, 3× benefit obtained, or 30% of adjusted turnover in the breach turnover period; individual — A$2,500,000. Mid tier (s 13H): 2,000 penalty units. Administrative tier (s 13K): 200 penalty units, enforceable by infringement notice or compliance notice. Penalty unit = A$364 from 1 July 2026 |
| Private right of action | Statutory tort for serious invasions of privacy (Schedule 2) from 10 June 2025; complaints to the OAIC for APP breaches (no direct APP cause of action) |
| Status (Sept 2026) | Tranche 1 reforms (Privacy and Other Legislation Amendment Act 2024) largely in force; automated-decision-making transparency (APP 1.7–1.9) commences 10 December 2026; Children's Online Privacy Code must be registered by 10 December 2026; tranche-2 exposure draft (Privacy Amendment (Personal Data Protection) Bill 2026) released 31 August 2026, submissions closed 18 September 2026 |
| Relationship to neighbours | Principles-based, consent-light regime with GDPR-style penalties since December 2022; sits alongside state/territory public-sector privacy laws, the Consumer Data Right, the Digital ID Act 2024, telecommunications and health-records statutes |

## What it is

The Privacy Act 1988 is Australia's federal privacy statute. It originally bound only Commonwealth agencies; the Privacy Amendment (Private Sector) Act 2000 extended it to larger private-sector organisations from 21 December 2001, the Privacy Amendment (Enhancing Privacy Protection) Act 2012 replaced the earlier principle sets with the 13 APPs from 12 March 2014, and the Privacy Amendment (Notifiable Data Breaches) Act 2017 added mandatory breach notification (Part IIIC) from 22 February 2018. The Privacy Legislation Amendment (Enforcement and Other Measures) Act 2022, commenced 13 December 2022, introduced the A$50 million / 3× benefit / 30% turnover penalty tier.

The Act is deliberately principles-based: the APPs set outcomes ("reasonable steps") rather than prescribing controls, and the OAIC's APP Guidelines and data-breach guidance supply the operational detail. A multi-year Privacy Act Review led to the Privacy and Other Legislation Amendment Act 2024 (assented 10 December 2024) — the first tranche of reform — and to the 2026 exposure draft of a much larger second tranche (see Timeline).

## Who it covers / Scope

| Test | Provision | Detail |
|---|---|---|
| APP entity | s 6 | An agency (Commonwealth) or an organisation |
| Organisation | s 6C | Individual, body corporate, partnership, unincorporated association or trust that is not a small business operator, registered political party, agency, or State/Territory authority |
| Small business exemption | s 6D(1) | Business with annual turnover of A$3,000,000 or less in the previous financial year; turnover defined in s 6DA. The exemption is lost (s 6D(4)) if the entity has ever exceeded A$3m, provides a health service and holds health information, discloses personal information for a benefit (trades in data), or provides a benefit to collect personal information. Small business operators can choose to be treated as organisations (s 6EA), and s 6E treats certain small business operators as organisations |
| Commonwealth contractors | s 7B(2), s 13(3) | Contracted service providers for a Commonwealth contract are covered for contract activities even if otherwise small |
| Employee records | s 7B(3) | Acts directly related to a current or former employment relationship and an employee record held by the employer are exempt |
| Journalism / politics / households | ss 7B(4), 7C, 16 | Media organisations committed to published privacy standards; registered political parties and political acts; individuals' personal, family or household affairs |
| Extraterritorial reach | s 5B(1A)–(3) | The Act applies to acts outside Australia by an organisation or small business operator with an "Australian link": Australian citizen or resident, partnership/trust formed in Australia, Australian-incorporated body corporate, association centrally managed in Australia, or any entity that "carries on business in Australia" (no requirement to collect or hold data in Australia). Schedule 2 (tort) is excluded from s 5B |
| NDB scheme entities | s 26WE(1) | APP entities holding personal information; credit reporting bodies (s 20Q); credit providers (s 21S); tax file number recipients (s 17 rules) |
| Overseas recipients | s 26WC | Information disclosed offshore under APP 8.1 is deemed still "held" by the discloser for NDB purposes — an offshore processor's breach is the Australian entity's notifiable breach |

## Core obligations

### Australian Privacy Principles (Schedule 1)

| APP | Subject | What it requires (as relevant to security/GRC) |
|---|---|---|
| 1 | Open and transparent management | 1.2: reasonable steps to implement practices, procedures and systems ensuring APP compliance and handling complaints (the "privacy program" duty); 1.3–1.4: clearly expressed, up-to-date privacy policy with prescribed contents; 1.7–1.9 (from 10 Dec 2026): policy must describe the kinds of personal information used by, and kinds of decisions made or substantially and directly assisted by, computer programs where the decision could reasonably be expected to significantly affect an individual's rights or interests |
| 2 | Anonymity and pseudonymity | Option not to identify where lawful and practicable |
| 3 | Collection of solicited information | Reasonably necessary for functions; sensitive information generally needs consent; lawful and fair means |
| 4 | Unsolicited information | Assess and destroy/de-identify if not collectable under APP 3 |
| 5 | Notification of collection | Collection notice at or before collection where practicable |
| 6 | Use or disclosure | Primary purpose, or secondary purpose with consent / reasonable expectation / permitted general situation (s 16A) |
| 7 | Direct marketing | Opt-out mechanisms; several sub-clauses are s 13K infringement-notice provisions |
| 8 | Cross-border disclosure | 8.1: reasonable steps to ensure an overseas recipient does not breach the APPs; s 16C makes the discloser accountable for the recipient's breach. Exceptions (8.2): recipient bound by substantially similar law with enforcement mechanisms; prescribed country or binding scheme under APP 8.3 (regulations under s 100(1A) — the 2024 "white list" mechanism); express informed consent; required by Australian law |
| 9 | Government identifiers | Restrictions on adopting/using government-related identifiers |
| 10 | Quality | Accurate, up-to-date, complete |
| 11 | Security | 11.1: reasonable steps to protect personal information from misuse, interference and loss, and from unauthorised access, modification or disclosure; 11.2: destroy or de-identify when no longer needed (unless Commonwealth record or legal retention); 11.3 (added December 2024): such steps "include technical and organisational measures" |
| 12–13 | Access and correction | Access on request and correction; APP 13.5 (dealing with requests) is a s 13K provision |

APP codes: the Commissioner can develop binding APP codes. Section 26GC (2024) requires the Commissioner to make a **Children's Online Privacy Code** binding APP entities that provide a social media service, relevant electronic service or designated internet service (Online Safety Act 2021 meanings) likely to be accessed by children, other than health services; breach of a registered APP code is an interference with privacy (s 13(1)(b)).

### Notifiable Data Breaches scheme (Part IIIC)

| Step | Provision | Rule |
|---|---|---|
| Trigger | s 26WE(2) | Eligible data breach = unauthorised access to, or disclosure of, information that a reasonable person would conclude is likely to result in serious harm to any affected individual; or loss of information where such access/disclosure is likely to occur and would likely cause serious harm |
| Serious-harm factors | s 26WG | Kind and sensitivity of information; whether protected by security measures and the likelihood they can be overcome (encryption and key exposure are called out); who obtained or could obtain it and their intent; nature of the harm |
| Remedial-action exception | s 26WF | Action taken before serious harm results, such that a reasonable person would no longer conclude serious harm is likely, means the event is taken never to have been an eligible data breach (or removes the duty to notify particular individuals) |
| Assessment | s 26WH | On reasonable grounds to *suspect*: carry out a reasonable and expeditious assessment and take all reasonable steps to complete it within **30 days**. OAIC guidance treats 30 days as a maximum, not a target |
| Statement to Commissioner | s 26WK | On reasonable grounds to *believe*: prepare and give the OAIC a statement **as soon as practicable**, setting out entity identity and contact details, description of the breach, kinds of information, and recommended steps for individuals (s 26WK(3)); may name other entities involved (s 26WK(4)). A non-compliant statement is a s 13K(2) contravention |
| Notify individuals | s 26WL | As soon as practicable after the statement: notify all affected individuals, or only those at risk of serious harm, or — if neither is practicable — publish the statement on the website and take reasonable steps to publicise it. Usual communication channel may be used |
| Exceptions | ss 26WJ, 26WM–26WQ | One notifying entity suffices where several entities hold the same data; enforcement-body prejudice; inconsistency with Commonwealth secrecy provisions; Commissioner declaration that notification is not required or must occur by a specified time |
| Commissioner direction | s 26WR | The Commissioner may direct an entity to prepare a statement and notify |
| Eligible data breach declaration | ss 26X–26XB (2024) | The Minister may declare that specified entities may collect, use or disclose personal information to prevent or reduce harm following a breach (e.g. banks re-verifying identities after a large-scale leak) |

Notification volumes (OAIC statistics, January–June 2025, published 4 November 2025): 532 notifications (down 10% from the record 591 in the prior half); 59% from malicious or criminal attacks, 37% from human error; health (18%), finance (14%) and Australian Government (13%) were the top sectors. Log every assessment and notification decision in a register such as [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).

### Statutory tort for serious invasions of privacy (Schedule 2, s 94A)

In force 10 June 2025. Cause of action (cl 7): intrusion upon seclusion or misuse of information relating to the plaintiff; a reasonable expectation of privacy; the invasion was intentional or reckless; and it was serious — with defences for lawful authority, consent, necessity and defamation-style publication defences (cl 8). Non-economic plus exemplary damages are capped at the greater of A$478,550 and the defamation non-economic-loss cap (cl 11(5)); proceedings generally within 3 years, extendable to a maximum of 6 years (cl 14); exemptions for journalists, under-18 defendants, intelligence and enforcement bodies. The tort applies to anyone, including small businesses outside the APPs.

### Doxxing offences (Criminal Code, inserted by Schedule 3 of the 2024 Act)

Sections 474.17C (6 years' imprisonment) and 474.17D (7 years where targeting a group by protected attribute) criminalise using a carriage service to publish personal data in a menacing or harassing way — in force 11 December 2024; an independent review must commence after 24 months of operation (s 4 of the 2024 Act).

## Enforcement and penalties

| Tier | Provision | Maximum | Notes |
|---|---|---|---|
| Serious interference | s 13G | Body corporate: greatest of A$50m, 3× benefit, 30% adjusted turnover over the breach turnover period (minimum 12 months, s 13G(7)); individual A$2.5m | Seriousness factors (s 13G(1B)) include sensitivity, consequences, number affected, children or vulnerable persons, repetition or continuity, and failure to implement practices, procedures and systems — repetition is a factor, not a separate limb |
| Interference | s 13H | 2,000 penalty units (multiplied ×5 for bodies corporate under Regulatory Powers Act s 82(5)(a) — verify) | Court may fall back to s 13H where s 13G seriousness is not proven (s 13J) |
| Administrative | s 13K | 200 penalty units | Breaches of APP 1.3, 1.4, 2.1, 6.5, 7.2(c)/7.3(c), 7.3(d), 7.7, 13.5, APP 1.7 once commenced, and non-compliant NDB statements |
| Infringement notices | s 80UB | Regulatory Powers Act Part 5; listed corporations: 200 penalty units per alleged contravention (s 80UB(1A)) | Also covers failure to give information (s 66(1)) and to comply with a compliance notice |
| Compliance notices | s 80UC | Failure to comply: 200 penalty units | Compliance bars later civil-penalty proceedings for the same conduct (s 80UC(8)) |

Penalty unit value: A$364 for contraventions from 1 July 2026 (Crimes Act 1914 s 4AA indexation), so 200 units = A$72,800 and 2,000 units = A$728,000 before any corporate multiplier. Other Commissioner tools: complaint investigations and determinations (Part V), enforceable undertakings, injunctions (s 80W), privacy assessments and Commissioner-initiated investigations.

Enforcement record: the first court-imposed civil penalties came in *Australian Information Commissioner v Australian Clinical Labs Ltd (No 2)* [2025] FCA 1224 (8 October 2025) — A$5.8m in total (A$4.2m for APP 11.1, A$800,000 for the s 26WH assessment failure, A$800,000 for the s 26WK notification failure) over a February 2022 breach affecting more than 223,000 individuals, under the pre-December 2022 penalty ceiling. Civil-penalty proceedings against Optus were filed on 8 August 2025 (alleged s 13G contravention affecting about 9.5 million people; conduct 17 October 2019–20 September 2022; pre-2022 maximum A$2.22m per contravention, pleaded per individual). Proceedings against Medibank over its 2022 breach are also on foot (verify current status).

## Timeline and status

| Date | Event |
|---|---|
| 21 Dec 2001 | Private-sector coverage commences |
| 12 Mar 2014 | 13 APPs replace earlier principles |
| 22 Feb 2018 | NDB scheme (Part IIIC) commences |
| 13 Dec 2022 | Privacy Legislation Amendment (Enforcement and Other Measures) Act 2022: A$50m / 3× / 30% penalty tier |
| 10 Dec 2024 | Privacy and Other Legislation Amendment Act 2024 (No. 128, 2024) assented |
| 11 Dec 2024 | Most of Schedule 1 in force: s 13G seriousness factors, new s 13H and s 13K tiers, infringement and compliance notices, APP 11.3 technical and organisational measures, APP 8.3 white-list mechanism, s 26GC Children's Online Privacy Code mandate, eligible data breach declarations (s 26X) and expanded Commissioner powers; Schedule 3 doxxing offences |
| 10 Jun 2025 | Schedule 2 statutory tort commences (default date, no earlier proclamation) |
| 8 Oct 2025 | First civil penalty (Australian Clinical Labs) |
| 1 Apr 2026 | Privacy Regulations 2025 replace the Privacy Regulation 2013 |
| 31 Mar–5 Jun 2026 | OAIC consultation on the exposure draft Privacy (Children's Online Privacy) Code 2026 |
| 1 Jul 2026 | Penalty unit indexed to A$364 |
| 31 Aug–18 Sep 2026 | Exposure draft Privacy Amendment (Personal Data Protection) Bill 2026 (tranche 2) consultation |
| 10 Dec 2026 | APP 1.7–1.9 automated-decision transparency commences; statutory deadline to register the Children's Online Privacy Code |

**Tranche 2 (pending, as at 18 September 2026).** The exposure draft has six schedules: (1) core definitions — personal information that "relates to" an individual, "precise geolocation tracking data" and genetic *or genomic* information as sensitive information, a new s 6FC definition of "trade"; (2) handling — a "fair and reasonable in the circumstances" requirement for collection, use and disclosure, express consent conditions, consent for trading in personal information, direct-marketing opt-outs; (3) data security — a statement to the Commissioner **within 72 hours** of forming reasonable grounds to believe an eligible data breach has occurred (replacing "as soon as practicable"), a new s 26WDB duty to take reasonable steps to prevent or reduce harm from actual or suspected breaches, and APP 11.5 requiring regular evaluation of the effectiveness of security and destruction practices; (4) access and erasure — a right to erasure limited to "large digital platforms" (revenue of at least A$500m or at least 2.5 million end users in the previous financial year), with a "technically impossible or infeasible" limit; (5) a research exception; (6) an information-processor (controller/processor) exception. Commencement rows are blank; the small business (A$3m) and employee-records exemptions are not removed (the draft amends s 6D(8) only to align with the new "trade" definition). Law-firm commentary reports a government intention to introduce a bill before the end of 2026 — treat as unconfirmed.

## Key obligations for security/GRC teams

1. **Settle applicability** — turnover history against the A$3m test, the s 6D(4) carve-outs (health services, data trading), Commonwealth-contract work, and the s 5B "carries on business in Australia" limb for offshore group entities. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Make APP 1.2 and APP 11 demonstrable**: a documented privacy program plus technical and organisational security measures mapped to a recognised control set; ACL was penalised for APP 11.1 on the facts of ordinary security hygiene. Map via [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) or [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md); test with [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
3. **Build the NDB clock into incident response**: suspicion → 30-day assessment; belief → immediate statement to the OAIC and individual notification; remedial-action analysis documented at each step. Run the [../../workflows/incident-regulatory-response.md](../../workflows/incident-regulatory-response.md) workflow and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md); plan now for the proposed 72-hour deadline.
4. **Treat offshore processors as your breach** (s 26WC, s 16C): APP 8 due diligence, contractual breach-notification SLAs shorter than your own clock, and data-location inventories. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
5. **Retention and destruction (APP 11.2)**: over-retention multiplies breach harm and penalty exposure; evidence a schedule and its execution.
6. **Privacy policy hygiene is now an infringement-notice matter** (APP 1.3–1.4, s 13K): review annually and add automated-decision disclosures before 10 December 2026. See [../../skills/policy-review/SKILL.md](../../skills/policy-review/SKILL.md) and [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).
7. **Run privacy impact assessments** for new collections, sensitive data, children's services and automated decisions, and keep them as evidence for APP 1.2. See [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).
8. **Track tranche 2 and the Children's Code** through horizon scanning and an impact assessment before the bill is introduced. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md) and [../../workflows/new-regulation-impact-assessment.md](../../workflows/new-regulation-impact-assessment.md).
9. **Report to the board** on NDB volumes and timeliness, APP 11 control coverage, and penalty exposure under s 13G; seriousness factors expressly include failure to implement practices, procedures and systems. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **GDPR:** no lawful-basis catalogue, no DPO mandate, no 72-hour clock (yet), but comparable penalty scale and extraterritorial reach; APP 8 accountability for overseas recipients is stricter than GDPR Chapter V in that the discloser is liable for the recipient's breach. Groups subject to both should run one breach-assessment process producing two notifications. See [gdpr.md](gdpr.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
- **State and territory laws:** the Act does not cover state public-sector agencies (each has its own privacy statute; some also run their own breach-notification schemes — verify per state), and state health-records Acts apply in parallel to health providers.
- **Sectoral overlays:** APRA CPS 234 (information security) and CPS 230 for regulated financial entities; Security of Critical Infrastructure Act obligations; the Consumer Data Right privacy safeguards; telecommunications data-retention rules (service providers are treated as organisations for retained data, s 6C note); the Digital ID Act 2024. Several carry their own incident-reporting clocks — reconcile them in the notification log.
- **Frameworks:** APP 11.1 names no control baseline; evidence "reasonable steps" against a recognised set — the ACSC Essential Eight/ISM domestically, or ISO/IEC 27001 and NIST CSF 2.0 for multinational programs. See [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) and [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md).
- **Other jurisdictions:** for New Zealand, Singapore and other APAC regimes see [other-jurisdictions.md](other-jurisdictions.md); for US state analogues to the tort and breach duties see [us-state-privacy.md](us-state-privacy.md).

## Primary sources

- Privacy Act 1988 (Cth), compilation No. 104, 4 June 2026 — legal text: https://www.legislation.gov.au/C2004A03712/latest/text (compiled text served at https://www.legislation.gov.au/C2004A03712/2026-06-04/2026-06-04/text/original/epub/OEBPS/document_1/document_1.html)
- Privacy and Other Legislation Amendment Act 2024 (No. 128, 2024), as made — legal text: https://www.legislation.gov.au/C2024A00128/asmade/text
- Privacy Regulations 2025 (F2025L01377) — legal text: https://www.legislation.gov.au/F2025L01377/asmade; Office of Impact Analysis summary: https://oia.pmc.gov.au/published-impact-analyses-and-reports/privacy-regulations-2025
- Exposure draft Privacy Amendment (Personal Data Protection) Bill 2026 and consultation page — Attorney-General's Department: https://consultations.ag.gov.au/rights-and-protections/privacy-reform/ (bill PDF at .../user_uploads/exposure-draft-bill-2026.pdf)
- OAIC, Data breach preparation and response, Part 4: NDB scheme — regulator guidance: https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/preventing-preparing-for-and-responding-to-data-breaches/data-breach-preparation-and-response/part-4-notifiable-data-breach-ndb-scheme
- OAIC, Guide to privacy regulatory action, Chapter 7 (civil penalties) — regulator guidance: https://www.oaic.gov.au/about-the-OAIC/our-regulatory-approach/guide-to-privacy-regulatory-action/chapter-7-privacy-assessments
- OAIC, Children's Online Privacy Code — regulator page: https://www.oaic.gov.au/privacy/privacy-registers/privacy-codes/childrens-online-privacy-code
- OAIC, History of the Privacy Act — regulator page: https://www.oaic.gov.au/privacy/privacy-legislation/the-privacy-act/history-of-the-privacy-act
- OAIC, NDB statistics January–June 2025 — regulator page: https://www.oaic.gov.au/news/blog/latest-notifiable-data-breach-statistics-for-january-to-june-2025
- OAIC media release, Australian Clinical Labs penalty (8 Oct 2025): https://www.oaic.gov.au/news/media-centre/australian-clinical-labs-ordered-to-pay-penalties-in-relation-to-medlab-pathology-data-breach-in-first-for-privacy-act
- OAIC media release, Optus civil-penalty proceedings (8 Aug 2025): https://www.oaic.gov.au/news/media-centre/australian-information-commissioner-takes-civil-penalty-action-against-optus
- OAIC media release on passage of the 2024 Bill (29 Nov 2024): https://www.oaic.gov.au/news/media-centre/pasing-of-bill-a-significant-step-for-australias-privacy-law
- ASIC, Fines and penalties (penalty unit value from 1 July 2026): https://www.asic.gov.au/about-asic/asic-investigations-and-enforcement/fines-and-penalties
- Not reachable when checked: Attorney-General's Department privacy and Privacy Act Review pages (ag.gov.au, HTTP 503); OAIC Medibank proceedings release. Tranche-2 commentary cross-checked against law-firm summaries (Johnson Winter Slattery; Allens, 4 September 2026) — secondary sources.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
