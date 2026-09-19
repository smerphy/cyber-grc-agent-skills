# European Digital Identity Framework — eIDAS 2.0 (Regulation (EU) 2024/1183 amending Regulation (EU) No 910/2014)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Regulation (EU) 2024/1183 of 11 April 2024 (OJ L, 30.4.2024), amending Regulation (EU) No 910/2014 ("eIDAS"). Directly applicable; article numbers below refer to the consolidated 910/2014 text |
| Entered into force | 20 May 2024 (20th day after OJ publication). Art. 19 of 910/2014 was separately deleted by NIS2 Art. 42 with effect from 18 October 2024 |
| Regulators | National supervisory bodies for trust services (Art. 46b) and for wallets (Art. 46a); single points of contact (Art. 46c); European Digital Identity Cooperation Group chaired by the Commission (Art. 46e); ENISA for wallet cybersecurity certification |
| Who is covered | Notified eID schemes, European Digital Identity Wallets (EUDI Wallets) provided by Member States, trust service providers (TSPs) established in the EU (Art. 2(1)); wallet-relying parties (Art. 5b); web-browser providers (Art. 45); certain private relying parties and very large online platforms must accept wallets (Art. 5f) |
| Structure | Chapter II eID and wallets (Arts. 5a–12b); Chapter III trust services (Arts. 13–45l: general, non-qualified, qualified, signatures, seals, time stamps, registered delivery, website authentication, attestations of attributes, archiving, ledgers); Chapter IVa governance (Arts. 46a–46e); Annexes I–VII |
| Key clocks | TSP security-breach notification: 24 hours (Arts. 19a(1)(b), 24(2)(fb)); certificate revocation published within 24 hours of request (Art. 24(3)); QTSP conformity audit at least every 24 months, report to supervisor within 3 working days (Art. 20(1)); wallet suspension notices within 24 hours (IR 2025/847) |
| Penalties | Member States must set fines for TSPs of a maximum of at least EUR 5 000 000, or for legal persons EUR 5 000 000 or 1 % of total worldwide annual turnover, whichever is higher (Art. 16(2)); without prejudice to NIS2 Art. 31 |
| Assessment model | Qualified status granted by the supervisory body on a conformity assessment body (CAB) report, constitutive listing on the national trusted list (Arts. 20–22); wallets certified under Cybersecurity Act schemes plus national schemes, valid up to 5 years with biennial vulnerability assessment (Art. 5c) |
| Wallet deadlines | Each Member State must provide at least one wallet within 24 months of the entry into force of the Art. 5a(23)/5c(6) implementing acts — those entered into force 24 December 2024, so the deadline is 24 December 2026 (confirmed by IR 2025/846 and 2025/848 applying from that date); private-sector acceptance duty 36 months on, i.e. 24 December 2027 |
| Neighbours | NIS2 (QTSPs are essential entities regardless of size; audits cover NIS2 Art. 21), GDPR (Art. 2(4) without prejudice; wallet processing must demonstrably comply, Art. 5a(17)), Cybersecurity Act (Art. 5c(2)), DSA (Art. 5f(3) VLOPs) |

## What it is

Regulation 910/2014 created the EU internal market for electronic identification and trust services: mutual recognition of notified national eID schemes, and a graded legal regime for electronic signatures, seals, time stamps, registered delivery and website-authentication certificates, with "qualified" services enjoying the strongest legal effect (a qualified electronic signature is equivalent to a handwritten signature, Art. 25(2)). The Commission's own evaluation found eID had underperformed — few schemes notified, weak private-sector uptake — and in 2021 it proposed a revision.

Regulation (EU) 2024/1183 is that revision. It (i) obliges every Member State to provide a European Digital Identity Wallet, certified and provided at assurance level "high", free of charge to natural persons, with user-controlled selective disclosure; (ii) adds new trust services — electronic attestations of attributes, electronic archiving, electronic ledgers, and management of remote qualified signature/seal creation devices; (iii) forces web browsers to recognise qualified website authentication certificates (QWACs); (iv) rewires TSP security supervision around NIS2 Art. 21; and (v) creates a governance layer (supervisory bodies, single points of contact, Cooperation Group). It is a two-tier regime: most technical content sits in Commission implementing regulations adopted in batches from November 2024 onward (see Timeline).

## Who it covers / Scope

| Actor | Test | Source |
|---|---|---|
| Trust service providers | Any TSP established in the Union providing a "trust service" (Art. 3(16) list: certificates, signatures, seals, time stamps, registered delivery, website authentication, attestations of attributes, archiving, ledgers, remote device management). Qualified vs non-qualified regime. Exclusion: services used exclusively within closed systems under national law or agreements between a defined set of participants (Art. 2(2)) | Arts. 2, 3, 19a, 24 |
| Wallet providers | Wallets provided directly by, under mandate from, or independently of but recognised by a Member State (Art. 5a(2)); Art. 24(2)(b),(d)–(h) QTSP duties apply mutatis mutandis (Art. 5a(20)) | Art. 5a |
| Wallet-relying parties | Anyone intending to rely on wallets to provide public or private services by digital interaction must register in the Member State of establishment; intermediaries acting for relying parties are deemed relying parties and must not store transaction content (Art. 5b(1),(10)) | Art. 5b |
| Mandatory acceptors | Public-sector bodies requiring eID for online services (Art. 5f(1)); private relying parties (other than micro/small enterprises) required by law or contract to use strong user authentication — transport, energy, banking, financial services, social security, health, drinking water, postal, digital infrastructure, education, telecoms are named — from 36 months after the wallet implementing acts, on the user's voluntary request (Art. 5f(2)); very large online platforms under DSA Art. 33 (Art. 5f(3)) | Art. 5f |
| Web-browser providers | Must recognise QWACs and display attested identity data; micro/small browser providers exempt for their first 5 years (Art. 45(1a)); precautionary measures allowed only for substantiated security concerns, with notification to Commission and supervisor (Art. 45a) | Arts. 45, 45a |
| Third-country TSPs | Legal equivalence only via Commission implementing act or EU agreement, requiring an equivalent trusted list (Art. 14) | Art. 14 |

Wallet use is voluntary and non-use may not restrict access to public or private services or the labour market (Art. 5a(15)). Pseudonyms chosen by the user may not be prohibited (Art. 5); relying parties may not refuse pseudonyms where identification is not legally required (Art. 5b(9)).

## Core obligations

### Trust service providers (qualified and non-qualified)

| Obligation | Non-qualified TSP | Qualified TSP (QTSP) |
|---|---|---|
| Risk management | Policies and measures for legal, business, operational and other risks covering registration/onboarding, procedural/administrative checks, and service management — notwithstanding NIS2 Art. 21 (Art. 19a(1)(a)); standards in IR 2025/2160 (references ETSI EN 319 401) | Same, as Art. 24(2)(fa); trustworthy systems and suitable cryptography (24(2)(e)); anti-forgery measures (24(2)(g)); staff competence and training (24(2)(b)); financial resources/liability insurance (24(2)(c)); records kept as long as necessary after cessation (24(2)(h)); up-to-date termination plan verified by the supervisor (24(2)(i)); certificate database (24(2)(k)); reference standards in IR 2025/2530 |
| Security-breach notification | Notify supervisory body, identifiable affected individuals, the public if of public interest, and other competent authorities of breaches or disruptions with significant impact on the service or the personal data held, without undue delay and no later than **24 hours after becoming aware** (Art. 19a(1)(b)) | Same recipients (public at the supervisor's request), without undue delay and **within 24 hours of the incident** (Art. 24(2)(fb)). NIS2 incident reporting runs in parallel (see Interplay) |
| Identity verification when issuing | — | Verify identity and attributes before issuing a qualified certificate or qualified attestation of attributes, by: wallet or notified eID at level high; a qualified signature/seal certificate; other CAB-confirmed high-confidence methods; or physical presence (Art. 24(1)–(1b)); standards in IR 2025/1566 (applies 19 August 2027) |
| Change control | — | Inform supervisor at least 1 month before any change to qualified services, 3 months before cessation; supervisor may condition permission (Art. 24(2)(a)) |
| Revocation | — | Register and publish revocation within 24 hours of the request; free, automated per-certificate status beyond validity (Art. 24(3)–(4)); same for qualified attestations (24(4a)) |
| Supervision cycle | Ex post supervision only (Art. 46b(3)(b)) | CAB audit at least every 24 months at own expense, covering the Regulation and NIS2 Art. 21; report to supervisor within 3 working days; supervisor notified 1 month before audits and may observe (Art. 20(1)–(1a)); ad hoc audits at any time (20(2)); CAB accreditation and assessment schemes in IR 2025/2162 |
| Initiation | — | Notify supervisor with a CAB report; supervisor verifies within 3 months (NIS2 authority input within 2 months); service may start only once listed on the trusted list (Art. 21); formats in IR 2025/1572 (applies 19 August 2026) |
| Liability | Claimant must prove intent/negligence (Art. 13(1)) | Intent/negligence presumed unless the QTSP proves otherwise (Art. 13(1)); limitation-of-use disclosures cap liability (13(2)) |
| Status loss | — | Supervisor withdraws qualified status after unremedied failure, or on information from the NIS2 competent authority or the GDPR supervisory authority (Art. 20(3)–(3c)); trusted list updated and EU trust mark use ends (Arts. 22–23) |

### Trust services and their implementing standards

| Service | Key rule | Implementing act (all "laying down rules for the application of Regulation (EU) No 910/2014") |
|---|---|---|
| Qualified certificates for signatures/seals | Annexes I and III; mutual recognition (Art. 24a) | IR 2025/1943 (29 Sept 2025) |
| Validation and preservation | Arts. 32, 32a, 33, 34, 40, 40a | IR 2025/1945 (validation, 29 Sept 2025); preservation and validation-service acts listed as adopted on the Commission overview (numbers not verified here) |
| Remote QSCD/QSealCD management (new qualified service) | Arts. 29a, 39a; transitional until 21 May 2026 (Art. 51(3)) | IR 2025/1567 (applies 19 August 2027) |
| Qualified electronic time stamps | Art. 42 | IR 2025/1929 (29 Sept 2025) |
| Qualified electronic registered delivery | Art. 44 | IR 2025/1944 (29 Sept 2025) |
| Qualified website authentication certificates (QWACs) | Annex IV; browser recognition (Art. 45(1a)); no other mandatory requirements (45(1b)) | IR 2025/2527 (applies 6 January 2027) |
| Electronic attestations of attributes (EAA/QEAA) | Legal effect equal to paper attestations for QEAA and public-sector authentic-source attestations (Art. 45b); Annex V/VII requirements; Annex VI attributes verifiable against authentic sources within 24 months of the wallet acts (Art. 45e) | IR 2025/1569 (Arts. 6–9 apply 19 August 2026); amendment out for feedback in 2026 |
| Qualified electronic archiving (new) | Durability and legibility beyond technological validity, integrity, automated integrity report signed/sealed by the provider (Art. 45j) | IR 2025/2532 (16 Dec 2025) |
| Qualified electronic ledgers (new) | Presumption of unique sequential chronological ordering and integrity (Art. 45k(2)); created by QTSPs, origin established, changes immediately detectable (Art. 45l) | IR 2025/2531 (16 Dec 2025) |
| Trusted lists | Art. 22 | Implementing Decision 2025/2164 (new list-format version, applies 29 April 2026) |

### European Digital Identity Wallet

| Topic | Requirement |
|---|---|
| Provision | At least one wallet per Member State by 24 December 2026 (Art. 5a(1)); application-software components open-source licensed (5a(3)); provided under an eID scheme at assurance level high (5a(11)); security by design (5a(12)); free issuance, use and revocation for natural persons (5a(13)); accessible under Directive 2019/882 (5a(21)) |
| Functions | Request, store, selectively disclose and present person identification data and attestations online and offline; generate locally encrypted pseudonyms; wallet-to-wallet exchange; transaction log dashboard with GDPR Art. 17 erasure requests and reporting of relying parties to the DPA; qualified signing free of charge for natural persons (Art. 5a(4)–(5)) |
| Privacy | Provider may not collect unnecessary usage data or combine wallet data with other services; logical separation where other services are offered (Art. 5a(14)); no tracking, linking or correlation of transactions by attestation providers or others unless the user authorises; unlinkability techniques (5a(16)); GDPR compliance must be demonstrated (5a(17)) |
| Certification | By Member-State-designated CABs (Art. 5c(1)); cybersecurity-relevant parts under Cybersecurity Act schemes, remainder under national schemes built to IR 2024/2981 (5c(2)–(3)); valid up to 5 years with vulnerability assessment every 2 years, cancelled if vulnerabilities are not remedied in time (5c(4)); Commission publishes the list of certified wallets in the OJ (Art. 5d; IR 2025/849) |
| Security breach | Member State must suspend provision and use without undue delay where the wallet, its validation mechanism or its eID scheme is breached or partly compromised; withdraw if severity justifies; withdraw and revoke if not remedied within 3 months; inform users, single points of contact, relying parties and the Commission (Art. 5e). IR 2025/847: suspension/withdrawal information within 24 hours; assessment criteria include unavailability > 12 consecutive hours or > 16 hours in a calendar week and > 1 % of users or relying parties impacted; notifications via ENISA's CIRAS (Art. 10, applies 7 May 2026) |
| Relying-party registration | Register in the Member State of establishment with name/registration number, contacts, intended use and the data to be requested; request nothing beyond what is registered; identify to the user; keep registration current (Art. 5b). IR 2025/848 (applies 24 December 2026) adds wallet-relying-party access certificates (issued only to registered parties) and registration certificates describing the attributes the party may request |
| Supervision | Wallet supervisory bodies with ex ante/ex post powers, on-site inspection, orders to suspend or cease provision, suspension of relying-party registrations for illegal or fraudulent use, duty to inform NIS2 authorities of significant breaches and DPAs of personal data breaches (Art. 46a); annual activity report by 31 March (46a(6), 46b(6); IR 2025/1571); Member-State statistics incl. a summary of significant security incidents and data breaches by 31 March each year (Art. 48a) |

## Enforcement and penalties

- **Administrative fines (Art. 16(2))**: Member States must provide maxima of at least EUR 5 000 000 for a natural-person TSP, or for a legal-person TSP EUR 5 000 000 or 1 % of total worldwide annual turnover of the undertaking in the preceding financial year, whichever is higher. Fines may be initiated by the supervisor and imposed by national courts (16(3)). All penalties must be effective, proportionate and dissuasive, without prejudice to NIS2 Art. 31 penalties for the same providers.
- **Qualified-status withdrawal** (Art. 20(3)) is the operative sanction for QTSPs: loss of listing on the trusted list ends the right to provide the service and its cross-border legal effect.
- **Civil liability** (Art. 13): presumed fault for QTSPs; compensation for material and non-material damage under national liability rules.
- **Wallet-side enforcement**: supervisory orders to suspend or cease wallet provision (Art. 46a(5)); Member-State suspension/withdrawal duties under Art. 5e; browser precautionary measures are investigated and can be ordered to end (Art. 45a(4)).
- **Mutual assistance and cooperation** across Member States via Arts. 46d–46e; guidance on organisational aspects issued by the Cooperation Group from 21 May 2025 and every two years.

## Timeline and status

| Date | Event |
|---|---|
| 1 July 2016 | Original eIDAS (910/2014) applied |
| 20 May 2024 | Regulation (EU) 2024/1183 entered into force (OJ L, 30.4.2024); corrigendum published OJ L, 9.4.2025 |
| 18 October 2024 | NIS2 Art. 42 deleted eIDAS Art. 19; TSP cyber-risk and incident-reporting duties move to NIS2 Art. 21/23 |
| 24 December 2024 | First wallet implementing package in force (OJ 4.12.2024): IR 2024/2977 (PID and attestations), 2024/2979 (integrity and core functionalities), 2024/2980 (notifications to the Commission), 2024/2981 (certification), 2024/2982 (protocols and interfaces) — starts the 24/36-month clocks |
| 7 May 2025 | OJ publication of IR 2025/846 (cross-border identity matching), 2025/847 (wallet security breaches), 2025/848 (relying-party registration), 2025/849 (list of certified wallets) |
| 21 May 2025 | Level-1 deadline for most trust-service implementing acts (Arts. 19a(2), 20(4), 21(4), 24(5), 45(2), 45j(2), 45l(3) etc.) — largely met late: July 2025 (IR 2025/1566–1572), September 2025 (2025/1929, 1943, 1944, 1945), October 2025 (2025/2160, 2162; Decision 2025/2164), December 2025 (2025/2527, 2530, 2531, 2532) |
| 21 May 2026 | Transitional cut-offs (Art. 51): legacy qualified certificates for natural persons cease to count; remote-device management without qualified status ends; QTSPs qualified before 20 May 2024 must have filed a conformity report proving Art. 24(1)–(1b) compliance. Commission review report due (Art. 49(1)) — no published report located as of September 2026 (verify) |
| 8 April 2026 | IR 2026/798 (remote onboarding of wallet users) published |
| April 2026 | ENISA public consultation (to 30 April 2026) on the draft candidate EU Digital Wallet cybersecurity certification scheme; adoption status thereafter not verified |
| 22 July 2026 | IR 2026/1731 (15 July 2026) amending the four 2024 wallet acts' standards and specifications (Art. 3(4) applies 11 August 2028); draft amendments to IR 2025/848 and 2025/1569 closed public feedback on 5 March 2026 |
| 19 August 2026 | IR 2025/1572 (qualified-service initiation formats) and IR 2025/1569 Arts. 6–9 apply |
| 24 December 2026 | Wallet provision deadline; IR 2025/846 and 2025/848 apply; Annex VI authentic-source verification due (Art. 45e(1)). Press reporting of 16 September 2026 indicates only 3 of 27 Member States have launched wallets and most will miss the date (secondary source) |
| 6 January 2027 | IR 2025/2527 (QWAC reference standards) applies |
| 21 May 2027 | Legacy secure signature creation devices cease to count as qualified devices (Art. 51(1)) |
| 19 August 2027 | IR 2025/1566 and 2025/1567 apply |
| 24 December 2027 | Private relying parties in Art. 5f(2) sectors must accept wallets on request |
| 21 May 2030 | First four-yearly progress report (Art. 49(3)) |

## Key obligations for security/GRC teams

1. **Classify your role**: TSP (qualified or not), wallet provider, wallet-relying party, mandatory acceptor under Art. 5f, or browser provider — each carries different clocks and registration duties. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **TSPs: wire the 24-hour breach clock** (Arts. 19a/24(2)(fb)) into incident response alongside the NIS2 24-hour early warning and GDPR 72-hour notification; pre-map the supervisory body, affected-individual comms and public-disclosure decision. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
3. **QTSPs: run the 24-month conformity cycle** against the Regulation plus NIS2 Art. 21, file reports within 3 working days, give 1 month's notice of audits and of service changes, and keep the termination plan current. See [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).
4. **Map the implementing-act standards** (ETSI EN 319 401 family and the acts in the tables above) onto the ISMS; treat each act's application date as a control deadline. See [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md) and [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md).
5. **Relying parties: register before integrating** (Art. 5b), obtain access and registration certificates (IR 2025/848), enforce data minimisation to the registered attribute set, and design for pseudonymous use where identification is not legally required.
6. **Regulated private sectors (banking, telecoms, energy, health, etc.)**: plan wallet acceptance for strong-authentication flows by 24 December 2027; align with existing customer-authentication controls. Financial entities should reconcile with [dora.md](dora.md) ICT-change and third-party processes.
7. **Privacy by design**: wallet-related processing must demonstrably comply with GDPR (Art. 5a(17)); run a DPIA for wallet, attestation or relying-party integrations. See [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md) and [gdpr.md](gdpr.md).
8. **Vendor diligence on trust services**: verify qualified status on the national trusted list rather than on marketing claims; the list is constitutive. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
9. **Horizon-scan the implementing-act pipeline** — acts were still being amended in July 2026 and the ENISA wallet certification scheme was in consultation in April 2026. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

- **NIS2** ([nis2.md](nis2.md)): trust service providers are an Annex I digital-infrastructure sector and qualified TSPs are essential entities regardless of size (NIS2 Art. 3(1)(b)). eIDAS security requirements now build on NIS2 Art. 21: QTSP audits and initiation checks cover NIS2 Art. 21 (Arts. 20(1), 21(1)); the NIS2 competent authority can trigger loss of qualified status (Art. 20(3a)); eIDAS Art. 16 fines are without prejudice to NIS2 Art. 31. Expect parallel notifications — the eIDAS 24-hour breach notice to the supervisory body and affected individuals, plus NIS2 Art. 23 reporting to the CSIRT/competent authority (24-hour early warning; and, by the Art. 23(4) derogation for TSPs, the incident notification itself within 24 hours of becoming aware for significant incidents affecting trust services) — to potentially different bodies unless the Member State has merged them.
- **GDPR** ([gdpr.md](gdpr.md)): Regulation is without prejudice to GDPR (Art. 2(4)); supervisory bodies must inform DPAs of apparent personal data breaches (Arts. 20(2), 46a(4)(g), 46b(4)(f)) and the DPA can trigger status withdrawal (Art. 20(3b)); wallet data-protection compliance may be certified under GDPR (Art. 5c(5)); wallet dashboards embed GDPR Art. 17 erasure requests.
- **Cybersecurity Act (Regulation 2019/881)**: cybersecurity-relevant wallet requirements are certified under European cybersecurity certification schemes (Art. 5c(2)); ENISA's candidate EUDI Wallet scheme was in consultation in April 2026.
- **DSA**: very large online platforms must accept wallet authentication on user request with minimum data (Art. 5f(3)).
- **DORA** ([dora.md](dora.md)) and sectoral rules: banks and financial services are named in Art. 5f(2), so wallet acceptance becomes a customer-authentication change subject to DORA ICT-change and third-party controls; QWACs and qualified seals used in sector interfaces should be sourced from listed QTSPs.
- **ISO/IEC 27001** ([../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md)): the implementing acts reference ETSI EN 319 401 (general TSP policy requirements) rather than ISO 27001 directly; an ISMS is a practical foundation but does not by itself evidence eIDAS conformity.

## Primary sources

- Regulation (EU) 2024/1183 — official legal text (Publications Office, CELEX 32024R1183): https://eur-lex.europa.eu/eli/reg/2024/1183/oj — fetched
- Consolidated Regulation (EU) No 910/2014 as of 18.10.2024 incl. 2024/1183 and corrigendum (CELEX 02014R0910-20241018) — legal text — fetched
- Directive (EU) 2022/2555 (NIS2), Arts. 3 and 42 and Annex I — legal text (CELEX 32022L2555) — fetched
- Commission Implementing Regulations (EU) 2024/2977, 2024/2979, 2024/2980, 2024/2981, 2024/2982; 2025/846, 2025/847, 2025/848, 2025/849; 2025/1566–1572; 2025/1929, 2025/1943, 2025/1944, 2025/1945; 2025/2160, 2025/2162; 2025/2527, 2025/2530, 2025/2531, 2025/2532; 2026/798; 2026/1731; Implementing Decision (EU) 2025/2164 — legal texts (Publications Office, CELEX 3YYYYRNNNN) — fetched
- Commission, "The European Digital Identity Regulation" implementing-acts overview (updated 22 July 2026): https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/pages/915931811/The+European+Digital+Identity+Regulation — regulator guidance — fetched
- Commission, "Questions & Answers on Trust Services under the European Digital Identity Regulation": https://digital-strategy.ec.europa.eu/en/faqs/questions-answers-trust-services-under-european-digital-identity-regulation — regulator guidance — fetched
- Commission, "European Digital Identity (EUDI) Regulation" and "eIDAS Regulation" policy pages: https://digital-strategy.ec.europa.eu/en/policies/eudi-regulation and https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation — regulator guidance — fetched
- ENISA, "ENISA advances the certification of EU Digital Wallets" (3 April 2026): https://www.enisa.europa.eu/news/enisa-advances-the-certification-of-eu-digital-wallets — regulator guidance — fetched
- Euronews, "EU digital wallet: 24 of 27 members will miss the deadline" (16 September 2026) — secondary source for rollout status only — fetched

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
