# New Zealand Privacy Act 2020 and cyber reporting expectations (Privacy Act 2020 No 31)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Privacy Act 2020 (Public Act 2020 No 31), replacing the Privacy Act 1993; amended by the Privacy Amendment Act 2025 (Royal Assent 23 September 2025) |
| Regulator | Office of the Privacy Commissioner (OPC); disputes and enforcement proceedings go to the Human Rights Review Tribunal |
| Key dates | Most of the Act in force 1 December 2020 (s 2(2)); Privacy Amendment Act 2025 technical amendments in force 24 September 2025; new IPP 3A in force 1 May 2026; Biometric Processing Privacy Code 2025 in force 3 November 2025 (new processing) / 3 August 2026 (pre-existing processing) |
| Who is covered | Every "agency" — any person or body, public or private, that collects or holds personal information; New Zealand agencies wherever they act, and overseas agencies "carrying on business in New Zealand" even with no local presence or revenue (s 4) |
| Structure | 13 Information Privacy Principles (IPPs) plus IPP 3A (s 22); codes of practice modify IPPs per sector (s 32); Part 6 notifiable privacy breaches; compliance notices (ss 123–133); transfer prohibition notices (s 193); offences (s 212) |
| Breach clock | Notify the Commissioner and affected individuals "as soon as practicable" after becoming aware of a notifiable privacy breach (ss 114–115); OPC's stated expectation is within 72 hours |
| Penalties | Criminal fines capped at NZ$10,000 (ss 118, 212); Tribunal damages for interference with privacy (s 103, no statutory cap stated in the section); no civil pecuniary penalty regime as of September 2026 |
| Cyber reporting ecosystem | NCSC (which absorbed CERT NZ) receives incident reports; RBNZ requires material cyber incident reports from banks, deposit takers and insurers within 72 hours (from 8 April 2024); FMA licence conditions carry a 72-hour material-incident notification; a mandatory critical-infrastructure cyber regime was consulted on February–April 2026 |
| International status | EU adequacy under Commission Implementing Decision 2013/65/EU (19 December 2012), reaffirmed in the Commission's first review report of 15 January 2024 |

## What it is

The Privacy Act 2020 is New Zealand's general, principles-based data protection statute. It restates the 1993 Act's information privacy principles in modern form and added the features the 1993 Act lacked: mandatory breach notification, compliance notices, binding OPC decisions on access complaints, a cross-border disclosure principle (IPP 12), explicit extraterritorial reach, and new offences. Its stated purpose (s 3) is to give effect to internationally recognised privacy obligations, including the OECD Guidelines and the ICCPR. The Act's enforcement model is deliberately light: OPC investigates and conciliates complaints, can issue compliance notices, and can take matters to the Human Rights Review Tribunal, but cannot fine agencies. The only monetary penalties are criminal fines capped at NZ$10,000.

Cyber incident reporting in New Zealand sits outside the Privacy Act. There is no general statutory duty to report cyber incidents to the National Cyber Security Centre (NCSC); sectoral regulators (Reserve Bank of New Zealand, Financial Markets Authority) impose their own reporting conditions on licensed financial entities; and the Government's February 2026 discussion document proposes the first mandatory cross-sector cyber regime, limited to critical infrastructure. Security teams therefore run three parallel questions after an incident: is it a notifiable privacy breach, is it reportable to a sectoral regulator, and should it be reported to NCSC.

## Who it covers / Scope

| Test | Rule (section) |
|---|---|
| Agency | "Agency means a person described in section 4 to whom this Act applies" (s 7) — public sector, private sector, incorporated or not; no size or turnover threshold |
| Personal information | "Information about an identifiable individual" (s 7); the Act applies to living individuals, with deceased persons covered only where a code of practice says so (s 112(1)) |
| New Zealand agency | Covered for any action in respect of personal information it collects or holds, whether or not present in New Zealand when acting (s 4(1)(a)) |
| Overseas agency | Covered for actions "in the course of carrying on business in New Zealand" (s 4(1)(b)); it does not matter where the information was collected or is held, or where the individual is located (s 4(2)) |
| "Carrying on business" | May be satisfied without being a commercial operation, having a place of business in New Zealand, receiving payment, or intending to make a profit (s 4(3)) |
| Processors / hosting | Information held by an agent (A) on behalf of another agency (B), for safe custody or processing, is treated as held by B, not A — regardless of whether A or the data is outside New Zealand; A becomes a holder too if it uses or discloses the information for its own purposes (s 11) |
| Information held overseas | An action in relation to information held overseas does not breach an IPP if required by the law of another country (s 23) |
| Personal/domestic affairs | Restricted application of the IPPs (s 27); breaches of information held solely for personal or domestic affairs are not notifiable (s 112(1)) |
| Offences | s 212 applies to New Zealand agencies, overseas agencies, individuals present in New Zealand, and persons outside New Zealand where an element of the offence occurs in New Zealand (s 4(5)) |

The cloud consequence of s 11 is that a New Zealand agency remains the accountable holder of data placed with an offshore processor, and IPP 5(b) requires it to do "everything reasonably within [its] power" to prevent unauthorised use or disclosure by service providers.

## Core obligations

### Information Privacy Principles (s 22)

| IPP | Subject | Security/GRC relevance |
|---|---|---|
| 1 | Purpose of collection | Collect only for a lawful purpose connected with a function, and only where necessary |
| 2 | Source — collect from the individual | Indirect collection needs an exception under IPP 2(2) |
| 3 | Notice on direct collection | What to tell the individual at collection |
| 3A | Notice on indirect collection (from 1 May 2026) | Reasonable steps, as soon as reasonably practicable after collection, to tell the individual: the fact and purpose of collection, intended recipients, names and addresses of the collecting and holding agencies, any authorising law, and access/correction rights; exceptions include prior awareness, publicly available information, no prejudice to the individual, law enforcement and court proceedings |
| 4 | Manner of collection | Lawful, fair, not unreasonably intrusive |
| 5 | Storage and security | Safeguards "reasonable in the circumstances" against loss, unauthorised access, use, modification or disclosure, and other misuse; flow-down duty for service providers (IPP 5(b)) |
| 6–7 | Access and correction | OPC can issue binding access directions; appeal to the Tribunal |
| 8 | Accuracy before use | Reasonable steps to check accuracy, completeness, currency |
| 9 | Retention | Keep no longer than required for the purposes of use |
| 10–11 | Use and disclosure limits | Purpose limitation with listed exceptions |
| 12 | Disclosure outside New Zealand | Disclosure to a foreign person or entity permitted only if the individual expressly authorises after being told protection may not be comparable, the recipient carries on business in New Zealand and is subject to the Act, the recipient is subject to comparable privacy laws, a prescribed binding scheme (s 213) or prescribed country (s 214) applies, or the agency reasonably believes the recipient is bound (e.g., by contract) to comparable safeguards; the requirement is relaxed where it is not reasonably practicable and the disclosure relies on the IPP 11(1)(e) or (f) grounds |
| 13 | Unique identifiers | Assign only where necessary; do not reuse other agencies' identifiers |

Codes of practice issued under s 32 modify the IPPs for a sector or class of information and have the same enforceability. Current codes: Health Information Privacy Code 2020, Credit Reporting Privacy Code 2020, Telecommunications Information Privacy Code 2020, Justice Sector Unique Identifier Code 2020, Superannuation Schemes Unique Identifier Code 2020, Civil Defence National Emergencies (Information Sharing) Code 2020, and the Biometric Processing Privacy Code 2025 (issued 21 July 2025; in force 3 November 2025 for new biometric processing, 3 August 2026 for processing that started earlier; Amendment No 1 of March 2026 added rule 3A). OPC's 2025 inquiry found a supermarket chain's live facial-recognition trial compliant with the Act, and OPC publishes detailed biometrics guidance and factsheets.

Every agency must appoint one or more privacy officers (s 201) whose responsibilities include encouraging compliance and handling requests under the Act.

### Notifiable privacy breaches (Part 6, subpart 1)

| Element | Rule (section) |
|---|---|
| Privacy breach | Unauthorised or accidental access to, or disclosure, alteration, loss or destruction of, personal information; or an action that prevents the agency from accessing the information temporarily or permanently (ransomware is OPC's own example) — whether caused inside or outside the agency, and whether or not ongoing (s 112) |
| Notifiable | A breach it is "reasonable to believe has caused serious harm to an affected individual or individuals or is likely to do so" (s 112) |
| Serious-harm factors | Mandatory considerations: mitigating action taken; sensitivity of the information; nature of the harm; who has or may obtain the information; whether it was protected by a security measure (e.g., encryption); any other relevant matter (s 113). OPC lists physical harm, financial fraud, identity theft, psychological harm, employment harm, blackmail and threats to safety as harm types |
| Notify the Commissioner | "As soon as practicable after becoming aware" (s 114). OPC's guidance: within 72 hours of becoming aware it is notifiable — "a guide only". Knowledge of employees and agents (including third-party providers) counts as the agency's knowledge. Notify via OPC's NotifyUs tool; updates by email against the PBN reference |
| Notify individuals | "As soon as practicable" (s 115(1)); public notice, with no individual identified, where individual notice is not reasonably practicable (s 115(2)–(3)) |
| Exceptions and delay | No individual notice where it would prejudice security/defence/international relations, prejudice maintenance of the law, endanger safety, or reveal a trade secret (s 116(1)); notice may instead go to a representative — a parent or guardian for an affected individual under 16, or a person appearing to act lawfully on an individual's behalf (s 116(3), (6)); delay of individual notice — but never of Commissioner notice — only while security risks of notifying outweigh the benefits (s 116(4)) |
| Content | Commissioner notice: description including number affected and suspected recipients, response steps and whether individuals contacted, reasons for public notice or any exception/delay, other agencies contacted, contact person (s 117(1)). Individual notice: description, whether a recipient is identified (not who, save to prevent a serious threat to life or health), response steps, mitigation steps for the individual, confirmation the Commissioner was notified, the right to complain, contact person (s 117(2)–(4)). Information may be provided incrementally as it becomes available (s 117(5)) |
| Offence | Failing without reasonable excuse to notify the Commissioner: fine up to NZ$10,000 (s 118(1)); taking remedial steps is no defence, but a reasonable belief the breach was not notifiable is (s 118(2)–(3)) |
| Civil exposure | Failing to notify individuals under s 115 is itself an "interference with privacy" (s 69(2)(a)(iv)) and can ground a complaint and Tribunal proceedings |
| Transitional | Breaches that occurred before 1 December 2020 are outside the regime even if continuing (Sch 1, cl 10) |

OPC received 1,093 privacy breach notifications in 2024/25 (a 27% increase per its annual report; the accompanying release says serious breaches notified rose 43%). OPC's review of the regime's first eleven months found fewer than half of serious breaches were notified within 72 hours (per a secondary summary of that report).

### Cyber incident reporting expectations beyond the Privacy Act

| Regime | Who | Trigger and clock | Basis / status |
|---|---|---|---|
| NCSC / CERT NZ | Any organisation or individual | No general statutory duty; NCSC receives and responds to incident reports (specialist "Report it" tool) and is the channel for vulnerability reports. CERT NZ, created within MBIE in 2016, was integrated into NCSC (part of GCSB) following a 2023 decision, with the transition completed in 2024 | Voluntary; NCSC established 2011 within GCSB |
| RBNZ cyber resilience reporting | Registered banks, licensed non-bank deposit takers, licensed insurers | Material cyber incidents "as soon as practicable" and within 72 hours, from 8 April 2024, using an initial / update / post-incident template; periodic reports of all cyber incidents (six-monthly for large entities with total assets of at least NZ$2 billion, annually for others); self-assessment against RBNZ's Guidance on Cyber Resilience (April 2021) annually for large entities, two-yearly for others, first due 1 October 2024 | Collected under statutory information-gathering powers (Banking (Prudential Supervision) Act 1989 s 93; Insurance (Prudential Supervision) Act 2010 s 121; Non-bank Deposit Takers Act 2013 s 47; Reserve Bank of New Zealand Act 2021 s 262); non-supply penalties of up to NZ$1 million (banks) / NZ$500,000 (insurers) — figures from a secondary source, verify against RBNZ |
| FMA | Financial institutions licensed under the Financial Markets (Conduct of Institutions) Amendment Act 2022; market services licensees under Part 6 of the Financial Markets Conduct Act 2013 | Standard licence condition: keep critical technology systems operationally resilient and notify FMA of an event materially affecting supply of services as soon as possible and no later than 72 hours after determining it is material; post-incident report as soon as practicable after resolution; FMA information sheet on cyber security and operational systems resilience dated 22 June 2022 | Licence conditions and guidance — secondary sources only, verify against FMA |
| Proposed critical-infrastructure cyber regime | About 200 entities across seven essential services (communications and data, defence, energy, finance, health, transport, water), with a "critical infrastructure of national significance" subset | Proposed: significant incidents reported to NCSC and the sector regulator with an early warning within 24 hours and a full report within 72 hours of detection; regular reporting of all incidents; a risk management programme aligned with an NCSC-endorsed or internationally recognised framework such as NIST CSF or ISO/IEC 27001:2022; directors responsible for compliance; penalties from administrative fines of NZ$50,000 up to criminal penalties of NZ$5 million or 2% of annual turnover (entity) and NZ$500,000 (director) | DPMC discussion document, consultation 27 February – 19 April 2026; no bill located as of September 2026 |

## Enforcement and penalties

| Mechanism | Detail |
|---|---|
| Complaints and conciliation | Individuals complain to OPC about an "interference with privacy" (s 69: breach of an IPP, of an information-sharing or matching agreement, or of s 115); OPC investigates and conciliates, and enforcement proceedings are heard by the Tribunal |
| Human Rights Review Tribunal | Declarations, restraining orders and other remedies (s 102); damages for pecuniary loss, expenses, loss of benefit, and humiliation, loss of dignity and injury to feelings (s 103); OPC's 2024/25 report cites an average negotiated settlement above NZ$13,000 |
| Access directions | Binding OPC decisions on IPP 6 access complaints, appealable to the Tribunal within 20 working days; failure to comply with a Tribunal access order is an offence (fine up to NZ$10,000) |
| Compliance notices | OPC may issue a notice for any breach of the Act or a code, at any time and alongside a complaint (s 123); the agency may respond (s 126); OPC may publish details (s 129), enforce in the Tribunal (s 130), and the Tribunal may order compliance and progress reporting (s 133); appeal lies under s 131 |
| Transfer prohibition notices | OPC may prohibit onward transfer of information received from another country to a third country lacking comparable safeguards (s 193); non-compliance is an offence (s 197) |
| Criminal offences | Fines up to NZ$10,000 for: failing to notify a notifiable breach (s 118); obstructing the Commissioner, failing to comply with a lawful requirement, giving false information, impersonating an individual to obtain or alter their information, or destroying a document subject to an access request (s 212) |
| Information powers | OPC may require an agency to supply information (s 202) |

There is no civil pecuniary penalty regime, no turnover-based fine, and no mandatory privacy management programme. OPC's November 2025 annual report reiterated its call for a "significantly stronger penalty regime", a right to erasure, demonstrable privacy management programmes and automated decision-making protections; the Government's 2026 Cyber Security Action Plan reportedly floats a civil pecuniary penalty regime under the Privacy Act (secondary source — verify).

## Timeline and status

| Date | Event |
|---|---|
| 19 December 2012 | Commission Implementing Decision 2013/65/EU finds New Zealand adequate under Directive 95/46/EC |
| 1 December 2020 | Privacy Act 2020 in force (except provisions commencing the day after assent, s 2(1)); mandatory breach notification begins |
| June 2021 | OPC sets its 72-hour notification expectation (date per secondary source) |
| April 2021 | RBNZ publishes Guidance on Cyber Resilience (publisher page not fetchable — verify) |
| 22 June 2022 | FMA information sheet on cyber security and operational systems resilience (secondary source) |
| 2023–2024 | CERT NZ integration into NCSC announced (2023) and completed (2024) |
| 15 January 2024 | European Commission first review of eleven pre-GDPR adequacy decisions: New Zealand "continues to provide an adequate level of protection"; the Commission welcomed the then-pending bill on indirect-collection transparency |
| 8 April 2024 | RBNZ material cyber incident reporting obligation starts (rules confirmed 4 March 2024) |
| 21 July / 3 November 2025 | Biometric Processing Privacy Code 2025 issued / in force for new processing |
| 23–24 September 2025 | Privacy Amendment Act 2025 Royal Assent; technical amendments in force the next day |
| 13 November 2025 | OPC Annual Report 2024/25 and renewed call for Privacy Act modernisation |
| February 2026 | New Zealand Cyber Security Strategy 2026–2030 and DPMC critical-infrastructure cyber discussion document; consultation 27 February – 19 April 2026 |
| March 2026 | Codes of practice amended to add rule 3A (Biometric Code Amendment No 1 and others) |
| 1 May 2026 | IPP 3A in force; applies to information collected on or after that date (transitional provision, s 25A — verify) |
| 3 August 2026 | Biometric Code transition period ends for pre-existing biometric processing |
| Pending (September 2026) | Critical-infrastructure cyber legislation (post-consultation, no bill located); Privacy Act penalty reform (advocated, not introduced) |

## Key obligations for security/GRC teams

1. **Confirm applicability under s 4** — overseas groups serving New Zealand users are caught without a local entity or revenue; map which group companies "carry on business in New Zealand". See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Wire the s 112–113 serious-harm assessment into incident triage** — document the six s 113 factors for every incident involving personal information (including ransomware and availability losses), record the decision and reasons, and re-assess as facts change. Log it in [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
3. **Run the 72-hour clock from "becoming aware", including awareness by staff and vendors** — pre-build the s 117(1) Commissioner notice and s 117(2) individual notice, use incremental notification under s 117(5), and never delay the Commissioner notice for security reasons (s 116(4)). See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
4. **Map parallel cyber reporting duties** — RBNZ and FMA 72-hour material-incident reports for licensed financial entities, and NCSC reporting; keep a single incident classification that answers all regimes at once. See [../../workflows/incident-regulatory-response.md](../../workflows/incident-regulatory-response.md).
5. **Treat IPP 5 as the security standard of care** — "reasonable in the circumstances" is judged against sensitivity and scale; evidence it with a control framework ([../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md), [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md)) and testing ([../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md)).
6. **Flow down IPP 5(b) and s 11 to processors** — contracts must bind hosting and SaaS providers to security, breach reporting to you (their knowledge is your knowledge), and no own-purpose use. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../templates/vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md).
7. **Gate cross-border disclosures under IPP 12** — record the ground relied on per destination (comparable law, contract, prescribed scheme/country, or express informed authorisation); note s 193 transfer prohibition powers for onward transfers.
8. **Update collection notices for IPP 3A** — every indirect data source (data brokers, partners, scraping, group transfers) needs a notification path or a documented exception; codes of practice now carry rule 3A. Use [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md) and [../../templates/dpia-template.md](../../templates/dpia-template.md).
9. **Biometrics need a code-specific assessment** — facial recognition and other biometric processing must meet the Biometric Processing Privacy Code 2025 from 3 August 2026 at the latest for existing deployments.
10. **Appoint and empower privacy officers (s 201)** and track the pending critical-infrastructure and penalty reforms. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md) and [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).

## Interplay

- **GDPR:** New Zealand holds EU adequacy (2013/65/EU, reaffirmed January 2024), so EU-to-NZ transfers need no SCCs; OPC reports to the Commission six-monthly. The reverse direction is governed by IPP 12, which is contract- and belief-based rather than an adequacy list (prescribed countries under s 214 exist as a mechanism). GDPR's Art. 33 "within 72 hours where feasible" clock is statutory; New Zealand's 72 hours is regulator guidance layered on "as soon as practicable". See [gdpr.md](gdpr.md).
- **Australia:** trans-Tasman groups should run the Australian notifiable data breaches assessment from the same incident record as the s 113 assessment — the harm test is similar in shape but the clocks, exceptions and penalty exposure differ (see the separate Australia Privacy Act pack). Other APAC regimes are summarised in [other-jurisdictions.md](other-jurisdictions.md).
- **Sectoral cyber regimes:** RBNZ and FMA reporting is operational-resilience driven and applies whether or not personal information is involved; a single ransomware event can be a Privacy Act notifiable breach, an RBNZ material cyber incident, an FMA licence-condition notification, and an NCSC report. Compare the EU approach in [dora.md](dora.md) and [nis2.md](nis2.md), and the proposed New Zealand critical-infrastructure regime's 24/72-hour model, which mirrors NIS2-style staged reporting.
- **Frameworks:** the DPMC proposal names NIST CSF and ISO/IEC 27001:2022 as acceptable anchors for the mandatory risk management programme; IPP 5 "reasonable safeguards" is most defensible when evidenced against the same frameworks. See [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md), [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
- **AI and biometrics:** OPC's biometric code and its automated decision-making reform agenda overlap with AI governance programmes; see [eu-ai-act.md](eu-ai-act.md) and [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).

## Primary sources

- Privacy Act 2020 No 31, legislation.govt.nz (official consolidated text; the live site blocks automated access — section references were checked against the official text as at 15 November 2022 via an archived copy, which pre-dates the 2025 amendment): https://www.legislation.govt.nz/act/public/2020/0031/latest/whole.html
- Privacy Amendment Act 2025, legislation.govt.nz (not fetchable; content taken from Ministry of Justice and OPC pages): https://www.legislation.govt.nz/act/public/2025/0053/latest/whole.html
- Ministry of Justice — Enhancing the Privacy Act (assent and commencement dates) and news release on IPP 3A: https://www.justice.govt.nz/justice-sector-policy/key-initiatives/enhancing-the-privacy-act/ ; https://www.justice.govt.nz/about/news-and-media/news/new-privacy-information-principle-in/
- OPC — Privacy Act 2020 principles pages (IPP text for 3A, 5 and 12), Comparing the Privacy Acts 1993 and 2020 (section mapping), Privacy Act 2020 information sheets and fact sheet (regulator guidance): https://www.privacy.org.nz/privacy-act-2020/privacy-principles/
- OPC — Sorting out privacy breaches, NotifyUs, and Poupou Matatapu Breach Management guide (72-hour expectation, serious harm, s 117 content): https://www.privacy.org.nz/responsibilities/privacy-breaches/notify-us/
- OPC — Biometric Processing Privacy Code 2025 page and New Zealand Gazette notice 2025-sl4213 (issue and commencement dates): https://www.privacy.org.nz/privacy-principles/codes-of-practice/biometric-processing-privacy-code/ ; https://gazette.govt.nz/notice/id/2025-sl4213
- OPC — Annual Report 2025 page, "New Zealand needs Privacy Act modernisation" (13 November 2025), "Privacy Amendment Act passes" (24 September 2025), and EU adequacy page: https://www.privacy.org.nz/about-us/corporate-reports/annual-reports/annual-report-of-the-privacy-commissioner-2025/
- European Commission — Implementing Decision 2013/65/EU (legal text) and COM(2024) 7 final, first review of adequacy decisions (15 January 2024): https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32013D0065 ; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52024DC0007
- NCSC — Who we are; Computer Emergency Response Team; Report an incident: https://www.ncsc.govt.nz/who-we-are/
- DPMC — Enhancing the cyber security of New Zealand's critical infrastructure system, discussion document (February 2026): https://www.dpmc.govt.nz/sites/default/files/2026-03/nz-cyber-security-discussion-doc-feb-2026-v2.pdf
- RBNZ — Cyber resilience for regulated entities, Guidance on Cyber Resilience (April 2021), Material Cyber Incident Notification FAQs (all blocked to automated access — not fetched): https://www.rbnz.govt.nz/regulation-and-supervision/cross-sector-oversight/improving-cyber-resilience-for-regular-entities
- FMA — Cyber security and operational systems resilience information sheet and incident notification guidance (blocked — not fetched): https://www.fma.govt.nz/library/guidance-library/cyber-security-infosheet/
- Secondary (used only where the regulator's site was unreachable): Bell Gully, "Cybersecurity update: new reporting obligations for financial sector" (RBNZ and FMA specifics) and "Privacy penalties and personal liability" (2026 strategy); Buddle Findlay, "Mandatory privacy breach reporting — where are we now?"; Incident Response Solutions note on the FMA June 2022 information sheet.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
