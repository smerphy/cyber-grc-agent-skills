# India: Digital Personal Data Protection Act 2023, DPDP Rules 2025, CERT-In Directions and sectoral cyber rules (DPDP / CERT-In)

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023, assented 11 August 2023); Digital Personal Data Protection Rules, 2025 (G.S.R. 846(E), 13 November 2025); CERT-In Directions No. 20(3)/2022-CERT-In of 28 April 2022 under s.70B(6) of the Information Technology Act, 2000; RBI, SEBI and IRDAI sectoral cyber frameworks |
| Regulators | Data Protection Board of India ("Board", DPDP Act s.18) for personal data; CERT-In (Ministry of Electronics and IT, MeitY) for cyber incidents; RBI, SEBI, IRDAI for banks/NBFCs, securities-market entities and insurers respectively |
| Status (Sept 2026) | DPDP Act commencing in phases via notification (s.1(2)); DPDP Rules: rules 1, 2 and 17–21 (Board machinery) in force 13 Nov 2025; rule 4 (Consent Managers) from 13 Nov 2026; rules 3, 5–16, 22, 23 (all substantive fiduciary duties incl. security, breach, children, SDF, rights) from 13 May 2027. CERT-In Directions in force since 2022; SEBI CSCRF applicable to all regulated entities since 31 Aug 2025 |
| Who is covered | DPDP: any "Data Fiduciary" processing digital personal data in India, plus processing abroad connected with offering goods/services to individuals in India (s.3). CERT-In: all service providers, intermediaries, data centres, body corporates and government organisations; per the CERT-In FAQ, "any entity whatsoever" for incident reporting |
| Breach / incident clocks | DPDP: affected individuals and Board "without delay", detailed Board report within 72 hours of becoming aware (rule 7). CERT-In: 6 hours from noticing for 20 listed incident types. SEBI: 6 hours to SEBI and CERT-In, portal details within 24 hours |
| Penalties | DPDP Schedule: up to INR 250 crore for failing reasonable security safeguards; INR 200 crore for breach-notification failure; INR 200 crore children's duties; INR 150 crore SDF duties; INR 50 crore any other breach. CERT-In non-compliance: penal provisions of IT Act s.70B(7) |
| Structure | DPDP Act: 9 chapters, 44 sections, 1 Schedule; DPDP Rules: 23 rules, 7 Schedules. CERT-In Directions: 6 directions + 3 annexures |
| Certifiable? | No. DPDP compliance is self-assessed; Significant Data Fiduciaries need an independent data auditor. SEBI requires ISO 27001 certification for MIIs and Qualified REs |
| Relationship to neighbours | Replaces IT Act s.43A / SPDI Rules 2011 regime once DPDP s.44 is commenced; sits alongside (not above) CERT-In and sectoral rules, which keep their own tighter clocks; DPDP s.16(2) preserves stricter sectoral localisation/transfer rules |

## What it is

The DPDP Act is India's first comprehensive personal-data statute. It is deliberately lean: a consent-or-"legitimate use" model (ss.4–7), a short list of fiduciary duties (s.8), extra duties for children's data (s.9) and for government-notified **Significant Data Fiduciaries** (s.10), individual rights (ss.11–14), broad State exemptions (s.17), a digital-first **Data Protection Board** that adjudicates and fines (ss.18–33), and a fixed penalty Schedule. Most operational detail — notice content, security safeguards, breach reporting, retention, verifiable parental consent, cross-border conditions — was left to the DPDP Rules, 2025, notified on 13 November 2025 after a draft published 3 January 2025 (G.S.R. 02(E)). The Rules phase in over 18 months, so most fiduciary duties bite from 13 May 2027.

The cyber-incident layer is older and separate. CERT-In, the national CSIRT under IT Act s.70B, issued binding Directions on 28 April 2022 (effective 60 days later; 25 September 2022 for MSMEs) that impose a 6-hour incident-reporting clock, 180-day log retention and customer-record duties on cloud/VPN/data-centre providers. Financial regulators layer their own frameworks on top: RBI's Cyber Security Framework in Banks (2016) and Master Direction on IT Governance (2023, effective 1 April 2024), SEBI's Cybersecurity and Cyber Resilience Framework (CSCRF, August 2024) and IRDAI's Information and Cyber Security Guidelines (2023, superseded by a 2026 edition issued 6 April 2026).

## Who it covers / Scope

| Instrument | Applicability test | Notable exclusions |
|---|---|---|
| DPDP Act (s.3) | Processing of digital personal data in India (collected digitally, or non-digital and later digitised); processing outside India "in connection with any activity related to offering of goods or services to Data Principals within the territory of India" | Personal/domestic processing; personal data made publicly available by the individual or under a legal obligation (s.3(c)). s.17(1)(d) exempts processing of non-Indian individuals' data by an Indian entity under contract with a person outside India (the outsourcing carve-out) — but s.8(1) accountability and s.8(5) security still apply. Research/archiving/statistics exempt under rule 16 if Second Schedule standards are met |
| Roles | **Data Fiduciary** decides purpose and means; **Data Processor** acts on its behalf and may be engaged only under a valid contract (s.8(2)); the fiduciary stays responsible for processor conduct (s.8(1)). **Child** = under 18 (s.2(f)). **Consent Manager** = Board-registered interoperable consent platform (s.2(g); rule 4, First Schedule: Indian company, net worth not less than INR 2 crore) | No "controller/processor" contract content is prescribed beyond rule 6(1)(f) (security clause) |
| Significant Data Fiduciary (s.10) | Notified by Central Government on volume/sensitivity of data, risk to individuals, sovereignty, electoral democracy, security of State, public order | None; obligations apply from notification |
| CERT-In Directions | Service providers, intermediaries, data centres, body corporates, government organisations; plus data centres, VPS, cloud and VPN service providers (direction v) and virtual-asset providers (direction vi) | Individual citizens (FAQ Q7); enterprise/corporate VPNs are outside the VPN-registration duty (FAQ Q34). Foreign firms serving Indian users are covered for incident reporting (FAQ Q26) and must name a Point of Contact (FAQ Q29) |
| RBI Master Direction 2023 | Commercial banks, SFBs, payments banks, NBFCs in Top/Upper/Middle layers, credit information companies, AIFIs | Local Area Banks, NBFC-Core Investment Companies; foreign bank branches on a comply-or-explain basis |
| SEBI CSCRF | All SEBI-regulated entities in five graded categories: MIIs, Qualified, Mid-size, Small-size, Self-certification REs, set each financial year on prior-year thresholds (e.g., AIF AUM bands starting below INR 100 crore) | Vault Managers, REITs/InvITs, Qualified Depository Participants, FPIs, FVCIs, the Limited Purpose Clearing Corporation and RTAs servicing fewer than 10,000 folios are excluded from CSCRF compliance submission |
| IRDAI Guidelines 2026 | All insurers incl. FRBs (foreign reinsurance branches), insurance intermediaries (brokers, corporate agents, web aggregators, TPAs, IMFs, repositories, ISNPs, corporate surveyors, MISPs, CSCs) and IIB | — |

## Core obligations

### DPDP Act and Rules — fiduciary duties

| Duty | Act | Rules (in force 13 May 2027 unless stated) | What it requires |
|---|---|---|---|
| Lawful basis | ss.4–7 | — | Consent (free, specific, informed, unconditional, unambiguous, affirmative — s.6) or a listed "legitimate use" (s.7: voluntarily provided data for the specified purpose, State benefits/functions, legal obligations, court orders, medical emergency, epidemic, disaster, employment) |
| Notice | s.5 | rule 3 | Standalone, plain-language notice with itemised personal data, purposes, link to withdraw consent (as easy as giving it), exercise rights and complain to the Board; retrospective notice for pre-Act consents (s.5(2)) |
| Security safeguards | s.8(5) | rule 6 | Minimum: encryption/obfuscation/masking/tokenisation; access control; access logging, monitoring and review; backups/continuity; **retain logs and personal data 1 year** for detection/investigation; processor contract clause; technical and organisational measures |
| Breach intimation | s.8(6) | rule 7 | To **each affected Data Principal without delay** (nature, extent, timing; likely consequences; mitigation; self-protection steps; contact). To the **Board without delay** (description, nature, extent, timing, location, likely impact) and **within 72 hours of becoming aware** (extendable by Board on written request): detailed facts, causes, mitigation, findings on perpetrator, remediation, report on individual notifications. "Personal data breach" (s.2(u)) has no harm or risk threshold |
| Retention and erasure | s.8(7) | rule 8, Third Schedule | Erase when purpose no longer served or consent withdrawn. E-commerce (≥2 crore registered users), online gaming intermediaries (≥50 lakh) and social media intermediaries (≥2 crore) must erase after **3 years** of user inactivity, with 48 hours' prior notice; all fiduciaries keep personal data, traffic data and processing logs **at least 1 year** (rule 8(3)) |
| Accuracy, processors | s.8(1)–(4) | — | Ensure completeness/accuracy where data drives decisions or is shared; processors only under valid contract; fiduciary liable regardless |
| Children | s.9 | rules 10–12, Fourth Schedule | Verifiable parental consent with due diligence on the parent's identity/age (existing reliable details, or voluntarily provided details/virtual token from an authorised entity); no detrimental processing, tracking, behavioural monitoring or targeted advertising. Carve-outs for clinical/mental-health establishments, healthcare and allied professionals, educational institutions, crèches (Part A) and listed purposes (Part B) |
| Significant Data Fiduciary | s.10 | rule 13 | DPO based in India, responsible to the board; independent data auditor; **DPIA and audit every 12 months** with significant observations reported to the Board; due diligence that algorithmic software does not risk individuals' rights; government-specified data and its traffic data **must not leave India** (committee-driven localisation) |
| Rights and grievances | ss.11–14 | rule 14 | Access (incl. identities of all fiduciaries/processors data was shared with), correction/erasure, grievance redressal (respond within a published period **not exceeding 90 days**), nomination. Individuals must exhaust the fiduciary's grievance channel before going to the Board (s.13(3)) |
| Cross-border transfer | s.16 | rule 15 | Transfers allowed except to countries the Central Government notifies (blacklist); rule 15 conditions transfers on government orders about making data available to foreign States. Stricter sectoral localisation (e.g., RBI payments data) survives (s.16(2)) |
| Consent Managers | s.2(g), s.6 | rule 4 (from 13 Nov 2026), First Schedule | Board registration; fiduciary duty to the individual; no sub-contracting; conflict-of-interest and audit mechanisms; own security safeguards |
| Government information calls | s.36 | rule 23, Seventh Schedule | Central Government may require any fiduciary or intermediary to furnish information, with possible non-disclosure orders |

### CERT-In Directions (28 April 2022) — six binding directions

| # | Direction | Detail |
|---|---|---|
| i | Clock synchronisation | Sync all ICT system clocks to NIC/NPL NTP servers (or traceable sources) |
| ii | **6-hour incident reporting** | Report Annexure I incident types to CERT-In within 6 hours of noticing or being notified (incident@cert-in.org.in; 1800-11-4949). Annexure I lists 20 types incl. unauthorised access, ransomware/malicious code, data breach, data leak, DoS/DDoS, attacks on critical infrastructure/SCADA/OT, cloud, IoT, digital payments, AI/ML systems. FAQ Q30: report what is available and supplement later; FAQ Q13: the duty is non-transferable to outsourcing partners; FAQ Q22: overrides contractual confidentiality via IT Act s.81 |
| iii | Orders and Point of Contact | Act on CERT-In orders within stated timeframes; designate a Point of Contact (Annexure II format, to info@cert-in.org.in) |
| iv | **Log retention** | Enable logs of all ICT systems; keep a rolling **180 days** within Indian jurisdiction; produce with incident reports or on order. FAQ Q35: logs may also be stored outside India provided they can be produced in reasonable time |
| v | Cloud/VPN/DC customer records | Data centres, VPS, cloud and VPN providers register validated customer name, hire period, IPs, registration email/IP/timestamp, purpose, address/contact, ownership pattern; keep **5 years** after cancellation |
| vi | Virtual-asset KYC | VASPs, exchanges and custodian wallet providers keep KYC and transaction records 5 years (Annexure III KYC documents) |

Non-compliance may attract the penal provisions of IT Act s.70B(7) (FAQ Q23: exercised when non-compliance is deliberate).

### Sectoral cyber frameworks (financial sector)

| Regulator / instrument | Governance | Testing and assurance | Incident reporting |
|---|---|---|---|
| RBI Cyber Security Framework in Banks (RBI/2015-16/418, 2 June 2016; scheduled commercial banks excl. RRBs) | Board-approved cyber-security policy distinct from IT/IS policy; Cyber Crisis Management Plan; board and top-management awareness | SOC with continuous surveillance; Annex 1 indicative baseline controls; Annex 2 indicative SOC configuration; one-off gap assessment submitted to the CSITE Cell by the CISO (deadline 31 July 2016) | Report all unusual cyber incidents (successful or attempted) promptly to RBI in the Annex 3 format; banks are also encouraged to report to IB-CART. The circular itself fixes no hour-count; the Annex 3 PDF sits behind an anti-bot challenge and could not be retrieved |
| RBI Master Direction on IT Governance, Risk, Controls and Assurance Practices (RBI/2023-24/107, 7 Nov 2023; effective 1 April 2024) | Board-level IT Strategy Committee; IT Steering Committee; Information Security Committee headed from risk; CISO senior-level, no reporting line to Head of IT, no business targets, reports to ED overseeing risk, quarterly cyber-risk review to Board/RMCB/ITSC | VA/PT by trained independent experts; audit trails and log monitoring; strong cryptography; IS audit overseen by Audit Committee, risk-based, policy reviewed annually; BCP/DR tested under multiple scenarios | Written incident response and recovery procedures; escalation to board and customers; proactively notify CERT-In and RBI (HFCs notify NHB); repeals the 2017 NBFC IT framework for Top/Upper/Middle-layer NBFCs |
| SEBI CSCRF (SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2024/113, 20 Aug 2024) | Graded five-category model; policy reviews annually; IT Committee quarterly (except small/self-cert); Cyber Capability Index — MIIs third-party assessed half-yearly, Qualified REs self-assess annually | ISO 27001 certification for MIIs and Qualified REs within 1 year; VAPT by CERT-In-empanelled auditors — twice yearly for NCIIPC protected systems/CII, otherwise at least annually, report within 1 month, closure within 3 months, revalidation within 5 months; red teaming and threat hunting (MIIs/Qualified REs, half-yearly/quarterly); SBOM for critical systems within 6 months and at procurement; Market SOC (NSE/BSE) by 1 Jan 2025 with small/self-cert REs onboarded | CERT-In-listed incidents to SEBI (mkt_incidents@sebi.gov.in) and CERT-In within **6 hours**, details on SEBI Incident Reporting Portal within **24 hours**; brokers/DPs also to exchanges/depositories; other incidents within 24 hours to SEBI, CERT-In, NCIIPC. Adoption: REs with prior circulars by 1 Jan 2025, first-time REs by 1 April 2025; extended to 30 June 2025, then to 31 Aug 2025 for all REs except MIIs, KRAs and QRTAs (SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2025/96, 30 June 2025) |
| SEBI circulars of 24 Aug 2026 | IT Resilience Index (ITRI) for MIIs: nine weighted parameters (availability 20, security 20, integrity 10, governance 10 ...); system-driven half-yearly computation within 60 days; ISF sub-parameters by 30 Nov 2026; SOP by 31 Jan 2027; operational by 28 Feb 2027; first submission for half-year ending 31 Mar 2027 | — | Cyber Incident Reporting Portal (siportal.sebi.gov.in) aligned to the FSB **FIRE** format with staged initial/intermediate/final reports; 6h/24h clocks unchanged |
| IRDAI Information and Cyber Security Guidelines 2023 (IRDAI/GA&HR/GDL/MISC/88/04/2023, 24 Apr 2023) → 2026 edition (IRDAI/GA&HR/CIR/MISC/51/4/2026, 6 Apr 2026) | Minimum standards and governance for all insurers, intermediaries and IIB; 2026 edition mandatory from FY 2026-27 | The 2023 cover circular references an annual security audit cycle; control and audit detail sits in Annexure B of the 2026 circular (not reviewed — verify) | Incident-reporting timelines sit in the guideline annexure (not reviewed — verify) |

## Enforcement and penalties

- **Board powers (s.27):** on a breach intimation, direct urgent remedial or mitigation measures, inquire and fine; hear complaints from individuals and references from government; supervise Consent Managers. The Board is "digital by design" (s.28; rule 20). Appeals go to the Telecom Disputes Settlement and Appellate Tribunal (s.2(a), s.29; rule 22 — digital filing, fee as under the TRAI Act). Mediation (s.31) and **voluntary undertakings** (s.32) are available; breach of an undertaking revives the original proceeding.
- **Penalty factors (s.33(2)):** nature, gravity and duration; type of data; repetition; gain or loss avoided; mitigation and its timeliness; proportionality and deterrence; likely impact on the person. Penalties go to the Consolidated Fund (s.34).

| Schedule item | Ceiling (INR) |
|---|---|
| Failure to take reasonable security safeguards (s.8(5)) | 250 crore |
| Failure to notify the Board or affected individuals of a breach (s.8(6)) | 200 crore |
| Breach of children's-data duties (s.9) | 200 crore |
| Breach of Significant Data Fiduciary duties (s.10) | 150 crore |
| Breach of Data Principal duties (s.15) | 10,000 |
| Breach of a voluntary undertaking (s.32) | Up to the amount applicable to the underlying breach |
| Any other breach of the Act or Rules | 50 crore |

- **Blocking (s.37):** after penalties in two or more instances the Central Government may, on the Board's reference, order intermediaries to block the fiduciary's services in India.
- **CERT-In:** failure to furnish information or comply with directions may attract IT Act s.70B(7) penalties "and other laws as applicable". **RBI/SEBI/IRDAI** enforce through supervisory action under their parent statutes; SEBI compliance is reported to the RE's authority (exchanges/depositories for brokers and DPs, SEBI for MIIs and others).

## Timeline and status

| Date | Event |
|---|---|
| 2 June 2016 | RBI Cyber Security Framework in Banks |
| 28 April 2022 / 27 June 2022 / 25 Sept 2022 | CERT-In Directions issued / effective (60 days) / effective for MSMEs and for customer-validation duties of DC/VPS/cloud/VPN providers |
| 24 April 2023 | IRDAI Information and Cyber Security Guidelines 2023 (supersede 2017 guidelines and 2020/2022 circulars) |
| 11 August 2023 | DPDP Act assented and published; commencement by notification, different dates for different provisions (s.1(2)) |
| 7 Nov 2023 / 1 April 2024 | RBI Master Direction on IT Governance issued / effective |
| 20 Aug 2024 | SEBI CSCRF issued (version 1.0); adoption 1 Jan 2025 (existing-circular REs) and 1 April 2025 (others); Market SOC by 1 Jan 2025 |
| 31 Dec 2024 | SEBI places the CSCRF data-classification/data-localisation requirement in abeyance (SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2024/184) |
| 3 Jan 2025 | Draft DPDP Rules published (G.S.R. 02(E)), 45-day consultation |
| 28 Mar 2025 / 30 Jun 2025 | SEBI extends CSCRF compliance to 30 June 2025, then by a further two months to 31 Aug 2025 for all REs except MIIs, KRAs and QRTAs |
| 9 Jul 2025 | CERT-In Technical Guidelines on SBOM, QBOM and CBOM, AIBOM and HBOM, version 2.0 (guidance, not a s.70B direction) |
| 28 Aug 2025 | SEBI technical clarifications to CSCRF: Principles of Exclusivity and Equivalence for REs with another primary regulator, re-categorisation of Portfolio Managers and Merchant Bankers, CERT-In cyber security audit policy guidelines |
| 13 Nov 2025 | DPDP Rules 2025 notified (G.S.R. 846(E)) under s.40; rules 1, 2 and 17–21 (Board appointment, procedure, digital office, staff) in force from publication. Which Act sections stand commenced, and whether the Board has been constituted and its Chairperson appointed, could not be confirmed from a primary source (verify) |
| 6 April 2026 | IRDAI Information and Cyber Security Guidelines 2026 (compliance from FY 2026-27) |
| 24 Aug 2026 | SEBI: FIRE-format incident portal; ITRI for MIIs (operational by 28 Feb 2027) |
| 13 Nov 2026 | DPDP rule 4 (Consent Manager registration) in force |
| 13 May 2027 | DPDP rules 3, 5–16, 22, 23 in force — notice, security safeguards, breach intimation, retention, children, SDF, rights, transfers, appeals |
| On commencement of DPDP s.44 | IT Act s.43A (compensation for negligent security practices) and s.87(2)(ob) omitted, ending the SPDI Rules 2011 regime; RTI Act s.8(1)(j) substituted with a bare "personal information" exemption (verify commencement date) |

Pending as of September 2026: constitution of the Data Protection Board, notification of Significant Data Fiduciaries, blacklisted transfer countries under s.16, rule-15 transfer orders, and the SDF localisation list (rule 13(4)). No further CERT-In direction under s.70B(6) has been published beyond the 2022 Directions and the 2022 extension notice. Track these via [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Key obligations for security/GRC teams

1. **Confirm applicability and role** — Data Fiduciary vs Processor, offering goods/services to India from abroad (s.3(b)), outsourcing carve-out (s.17(1)(d)), SDF exposure, and which sectoral regulator applies. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Build a three-clock breach playbook**: CERT-In 6 hours (any of 20 incident types, no harm threshold), SEBI 6h/24h or RBI prompt reporting where applicable, and DPDP "without delay" to individuals and Board plus the 72-hour detailed Board report — with pre-drafted rule 7 content. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md), [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
3. **Map rule 6 safeguards to the control set** (encryption/masking, access control, logging and monitoring, backups, 1-year log and data retention, processor clauses) against ISO 27001 Annex A and NIST CSF 2.0. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md), [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md), [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md).
4. **Fix log retention policy**: 180 days rolling (CERT-In, all ICT systems, in Indian jurisdiction), 1 year of access logs and processing logs (DPDP rules 6 and 8(3)), and 3-year inactivity erasure for large platforms — reconcile with sectoral retention.
5. **Register a CERT-In Point of Contact and NTP-sync clocks**; if you provide cloud, VPS, data-centre or consumer VPN services, implement the 5-year customer-record register.
6. **Remediate processor contracts**: valid contract (s.8(2)), security-safeguard clause (rule 6(1)(f)), breach-notice flow-down to meet 6-hour/72-hour clocks. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
7. **Prepare for SDF designation**: India-based DPO reporting to the board, independent data auditor, annual DPIA and audit with Board reporting, algorithmic due diligence. See [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md) and [../../templates/dpia-template.md](../../templates/dpia-template.md).
8. **Children's data controls**: age/parent verification flows, suppression of tracking and targeted ads for under-18s, Fourth Schedule carve-out mapping.
9. **Sectoral testing calendars**: SEBI VAPT/red-team/CCI cadence, RBI VA/PT and IS audit, IRDAI annual audit — schedule and evidence them. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
10. **Board reporting**: RBI requires quarterly CISO cyber-risk reviews and SEBI ITRI half-yearly board insights; fold DPDP readiness into the same pack. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **GDPR:** DPDP is narrower — digital data only, no special-category concept, no legitimate-interest balancing (fixed "legitimate uses" instead), no harm threshold for breach notification, and a 72-hour clock that runs to a *detailed* report after an immediate "without delay" notice. A GDPR Art. 30 record and Art. 33 playbook are a starting point, not a substitute; see [gdpr.md](gdpr.md). CERT-In FAQ Q32 confirms the Directions do not alter existing confidentiality duties for personal data in logs.
- **IT Act 2000:** CERT-In Directions and the intermediary framework continue independently of DPDP. The CERT-In FAQ defines "body corporate" by reference to IT Act s.43A, which DPDP s.44(2) omits — expect a clarification (verify).
- **Financial-sector regimes:** RBI, SEBI and IRDAI clocks (6 hours, or "prompt") are tighter than DPDP's and address the sectoral regulator, not the Board; a personal-data breach at a bank or broker can trigger CERT-In, the sectoral regulator and the Board in parallel. DPDP s.16(2) keeps stricter sectoral localisation rules intact, but the CSCRF's own data-classification and localisation requirement has been in abeyance since SEBI's circular of 31 Dec 2024, so RBI payments-data localisation remains the binding sectoral constraint. Compare the EU pattern in [dora.md](dora.md) and [nis2.md](nis2.md).
- **Standards leverage:** SEBI mandates ISO 27001 for MIIs/Qualified REs and structures CSCRF around identify/protect/detect/respond/recover-style functions plus governance and "evolve"; an ISO 27001 ISMS with CSF 2.0 profile covers most of the RBI and IRDAI expectations too. See [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md).
- **Cross-jurisdiction summary:** the short India entry in [other-jurisdictions.md](other-jurisdictions.md) is superseded in detail by this pack.

## Primary sources

- Digital Personal Data Protection Act, 2023 — Gazette text hosted by MeitY (legal text): https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf
- Digital Personal Data Protection Rules, 2025, G.S.R. 846(E) — Gazette of India Extraordinary Part II s.3(i), 13 Nov 2025 (legal text; MeitY and eGazette pages could not be fetched, so the Gazette PDF was read from a mirror: https://dpdpa.com/DPDP_Rules_2025_English_only.pdf — verify against meity.gov.in / egazette.gov.in)
- CERT-In Directions No. 20(3)/2022-CERT-In, 28 April 2022 (legal text): https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf
- CERT-In extension for MSMEs and customer validation, 27 June 2022 (regulator notice): https://www.cert-in.org.in/PDF/CERT-In_directions_extension_MSMEs_and_validation_27.06.2022.pdf
- CERT-In FAQs on Cyber Security Directions, May 2022 (regulator guidance): https://www.cert-in.org.in/PDF/FAQs_on_CyberSecurityDirections_May2022.pdf
- RBI Cyber Security Framework in Banks, 2 June 2016 (regulator circular; Annexes 1–3 PDFs not retrievable): https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=10435
- RBI Master Direction on IT Governance, Risk, Controls and Assurance Practices, 7 Nov 2023 (regulator direction): https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12562
- CERT-In page listing the s.70B Directions, the extension notice and the FAQs (regulator page): https://www.cert-in.org.in/Directions70B.jsp
- CERT-In Technical Guidelines on SBOM, QBOM and CBOM, AIBOM and HBOM, version 2.0, 9 July 2025 (regulator guidance): https://www.cert-in.org.in/PDF/TechnicalGuidelines-on-SBOM,QBOM&CBOM,AIBOM_and_HBOM_ver2.0.pdf
- SEBI CSCRF circular, 20 Aug 2024 (regulator circular): https://www.sebi.gov.in/legal/circulars/aug-2024/cybersecurity-and-cyber-resilience-framework-cscrf-for-sebi-regulated-entities-res-_85964.html
- SEBI CSCRF framework text, version 1.0 (framework PDF, 205 pages): https://www.sebi.gov.in/sebi_data/attachdocs/aug-2024/1724326790365.pdf
- SEBI circular, Extension towards Adoption and Implementation of CSCRF, 30 June 2025 (regulator circular): https://www.sebi.gov.in/legal/circulars/jun-2025/extension-towards-adoption-and-implementation-of-cybersecurity-and-cyber-resilience-framework-cscrf-for-sebi-regulated-entities-res-_94902.html
- SEBI circular, Technical Clarifications to CSCRF, 28 Aug 2025 (regulator circular): https://www.sebi.gov.in/legal/circulars/aug-2025/technical-clarifications-to-cybersecurity-and-cyber-resilience-framework-cscrf-for-sebi-regulated-entities-res-_96329.html
- SEBI circular, Alignment of Cyber Incident Reporting Portal with FIRE format, 24 Aug 2026: https://www.sebi.gov.in/legal/circulars/aug-2026/alignment-of-sebi-s-cyber-incident-reporting-portal-with-fire-format_103915.html
- SEBI circular, IT Resilience Index for MIIs, 24 Aug 2026: https://www.sebi.gov.in/legal/circulars/aug-2026/it-resilience-index-for-market-infrastructure-institutions-miis-_103913.html
- IRDAI Guidelines page listing the 2023 and 2026 Information and Cyber Security Guidelines (regulator page; cover circulars fetched, full 2026 Annexure B not fetched): https://irdai.gov.in/web/guest/guidelines

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
