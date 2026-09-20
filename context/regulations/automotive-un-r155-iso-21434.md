# Automotive cybersecurity — UN Regulation No. 155 / No. 156 and ISO/SAE 21434

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | UN Regulation No. 155 (cyber security and cyber security management system) and UN Regulation No. 156 (software update and software update management system), adopted under the 1958 Agreement; both entered into force 22 January 2021 |
| Current consolidated text | R155 incorporating Supplement 3, in force 10 January 2025 (OJ L, 2025/5). Authentic texts: ECE/TRANS/WP.29/2020/79 (as amended by 2020/94 and 2020/97), 2022/54, 2023/70, 2024/55 |
| Publisher / forum | UNECE World Forum for Harmonization of Vehicle Regulations (WP.29); applied and enforced by each Contracting Party's type-approval authority and its technical services |
| Who is covered | Vehicle manufacturers seeking type approval. R155 (current text): categories L, M, N, O fitted with at least one electronic control unit. R156: categories M, N, O, R, S, T that permit software updates |
| Approval model | Two artefacts: a Certificate of Compliance for CSMS (and for SUMS), valid a **maximum of three years**, plus a per-vehicle-type approval that the authority may refuse or withdraw |
| EU application | Regulation (EU) 2019/2144 (General Safety Regulation) Annex II item D4 "Protection of vehicle against cyberattacks", marked "B": refusal of EU type-approval from **6 July 2022**, prohibition of registration and placing on the market from **7 July 2024** |
| UK (GB) application | SI 2025/1110 inserted UN R155 and R156 into Annexes II, IV and XII of Regulation (EU) 2018/858 as it has effect in GB; in force 13 November 2025. GB refusal of type-approval for new types applied from **1 June 2026**; Annex XII Table 1 makes the **original version** of each Regulation compulsory (not Supplement 3) |
| Companion standard | ISO/SAE 21434:2021 "Road vehicles — Cybersecurity engineering", first edition 2021-08, jointly ISO/TC 22/SC 32 and SAE TEVEES18A; supersedes SAE J3061:2016. Voluntary and paywalled; R155 cites it only as one of three examples in an explanatory footnote to para. 5.3.1(a) on approval-authority competence, never normatively |
| Continuous duty | Monitoring outcomes reported to the approval authority **at least once a year** (R155 para. 7.4.1); conformity-of-production checks normally **every three years** (para. 9.1.2) |
| Penalties | No monetary ceiling in the UN text — the sanction is refusal, non-extension or withdrawal of type approval (paras. 5.1.3, 6.8, 10.1). Fines come from national market-surveillance law |

## What it is

R155 and R156 turned vehicle cybersecurity from an engineering preference into a condition of market access. They are type-approval regulations, not data-protection or incident-reporting laws: the regulator's leverage is the approval certificate, and the assessment is performed by an approval authority or its technical service rather than by a commercial certification body.

The pair is deliberately split. **R155** governs *how the organisation works* (a Cyber Security Management System covering development, production and post-production) and *how the vehicle type behaves* (risk assessment, proportionate mitigations, detection, forensic data, testing before approval). **R156** governs *how software gets changed after sale* (a Software Update Management System, the RXSWIN software-identification scheme, and over-the-air execution safety). A manufacturer cannot obtain a vehicle type approval under R155 without a valid CSMS certificate, subject only to legacy transitional provisions.

**ISO/SAE 21434:2021** supplies the engineering method the regulations presuppose but never name. It specifies cybersecurity risk-management requirements across concept, product development, production, operation, maintenance and decommissioning of electrical and electronic (E/E) systems, defines the TARA vocabulary (asset, damage scenario, threat scenario, attack path, attack feasibility, cybersecurity goal), and produces a **cybersecurity case** — "a structured argument supported by evidence to state that risks are not unreasonable". In practice, 21434 work products are the evidence pack presented at a CSMS audit; the standard is applicable to series-production E/E systems whose development or modification began after its publication.

## Who it covers / Scope

- **R155 scope (Supplement 3 text, para. 1.1):** vehicles of categories **L, M, N and O if fitted with at least one electronic control unit**. The original 2021 text covered M and N, O with an ECU, and L6/L7 with automated driving level 3 or above; Supplement 3 replaced that with the broader L/M/N/O formulation.
- **R156 scope (para. 1.1):** vehicles of categories **M, N, O, R, S and T that permit software updates**. Categories R, S and T are in R156 but not in R155, so a towed-machinery programme can need a SUMS without needing a CSMS certificate.
- **Transitional relief (R155 para. 7.3.1):** for type approvals of M, N and O vehicles first issued **before 1 July 2024**, and of L-category vehicles **before 1 July 2029**, and for each extension of those approvals, a manufacturer that can demonstrate the type could not be developed in compliance with the CSMS may instead demonstrate that cyber security was adequately considered during development. The same dates gate the "technically not feasible" carve-out for Annex 5 Part B/C mitigations (para. 7.3.4).
- **Suppliers** are not directly approved. R155 para. 7.2.2.5 requires the manufacturer to demonstrate how the CSMS manages dependencies on contracted suppliers, service providers and sub-organisations — the obligation is passed down by contract, and ISO/SAE 21434 Clause 7 (distributed cybersecurity activities) is the usual vehicle for it.
- **Territorial reach:** R155/R156 bind only Contracting Parties to the 1958 Agreement that apply them. The EU and the UK apply both, on the dates above. Japan and South Korea are commonly listed as applying them, with their own national phase-in dates (verify against the UNECE status document TRANS/WP.29/343 and the relevant ministry). The United States has no equivalent type-approval requirement; see Interplay.

## Core obligations

### R155 — the Cyber Security Management System (organisational, para. 7.2)

The manufacturer must demonstrate that the CSMS applies to the **development, production and post-production phases** (7.2.2.1) and that its processes cover:

| Ref | Process the manufacturer must demonstrate |
|---|---|
| 7.2.2.2(a) | Processes used within the organisation to manage cyber security |
| 7.2.2.2(b) | Identification of risks to vehicle types, considering the threats in Annex 5 Part A and other relevant threats |
| 7.2.2.2(c) | Assessment, categorisation and treatment of identified risks |
| 7.2.2.2(d) | Verification that identified risks are appropriately managed |
| 7.2.2.2(e) | Testing the cyber security of a vehicle type |
| 7.2.2.2(f) | Keeping the risk assessment current |
| 7.2.2.2(g) | Monitoring for, detecting and responding to cyberattacks, threats and vulnerabilities, and reassessing whether existing measures remain effective |
| 7.2.2.2(h) | Providing relevant data to support analysis of attempted or successful cyberattacks |
| 7.2.2.3 | Mitigating threats and vulnerabilities that require a response "within a reasonable timeframe" — no fixed clock is stated |
| 7.2.2.4 | Making the monitoring under (g) **continual** |
| 7.2.2.5 | Managing dependencies on contracted suppliers, service providers and sub-organisations |

### R155 — the vehicle type (technical, para. 7.3)

| Ref | Requirement |
|---|---|
| 7.3.1 | A valid Certificate of Compliance for CSMS relevant to the type being approved (subject to the transitional provision above) |
| 7.3.3 | An **exhaustive risk assessment** of the vehicle type covering its individual elements, their interactions, interactions with external systems, and all threats in Annex 5 Part A |
| 7.3.4 | Proportionate mitigations, including all relevant Annex 5 Part B and Part C mitigations; where one is not relevant or not sufficient, another appropriate mitigation must be implemented |
| 7.3.5 | Secure dedicated environments for storage and execution of aftermarket software, services, applications or data, where provided |
| 7.3.6 | Appropriate and sufficient testing **prior to type approval** to verify the effectiveness of implemented measures |
| 7.3.7 | Vehicle-level capability to detect and prevent attacks, support manufacturer monitoring, and provide **data forensic capability** |
| 7.3.8 | Cryptographic modules in line with consensus standards, or a documented justification for departing from them |
| 7.4.1 | Report monitoring outcomes to the approval authority or technical service **at least annually**, including new cyberattacks, and confirm that mitigations remain effective |

**Annex 5** is the mandatory threat baseline. Part A lists vulnerabilities and attack methods under seven high-level headings — back-end servers related to vehicles in the field; communication channels; update procedures; unintended human actions; external connectivity and connections; vehicle data and code; and potential vulnerabilities that could be exploited if not sufficiently protected or hardened. Part B lists mitigations intended for vehicles, Part C mitigations outside the vehicle (for example IT back ends), each cross-indexed to Part A. Annex 5 also enumerates the attack impacts the threat analysis must consider, from "safe operation of vehicle affected" through data confidentiality and availability loss.

### R156 — Software Update Management System and update execution

- **Twelve processes verified at initial assessment (7.1.1.1–7.1.1.12):** secure documentation of regulation-relevant information; unique identification of every initial and updated software version with integrity-validation data; access to and updating of the **RXSWIN** before and after an update; verification that software present on a component matches its RXSWIN; identification of interdependencies; identification of target vehicles; confirmation of compatibility with the target configuration before issue; assessment of whether an update affects type-approved systems; assessment of whether it adds, alters or disables legislated functions; assessment of effects on systems needed for safe operation; informing the vehicle user; and making records available to authorities for type approval, conformity of production, market surveillance, recalls and periodic technical inspection.
- **Records (7.1.2.3):** for every RXSWIN, an **auditable register** of all relevant software before and after each update, with versions and integrity-validation data; para. 7.1.2.5 adds per-update documentation of purpose, systems affected, approval sought and verification passed.
- **RXSWIN handling (para. 7.2.1.2 onwards):** each RXSWIN uniquely identifiable and updated when type-approval-relevant software changes; readable in a standardised way at least via the OBD port; protected against unauthorised modification, with the protection means disclosed confidentially at approval.
- **Safe execution (7.2.2.1.1, 7.2.2.1.3):** the vehicle must be able to restore the previous version after a failed or interrupted update, or enter a safe state; where an update may affect vehicle safety, technical means must ensure the vehicle is in a state where it can be executed safely.
- **User information (7.2.2.2, 7.2.2.4):** before execution the user is informed of the purpose, the changes to vehicle functions, the expected time to complete, functions unavailable during execution and any instructions for safe execution; after execution, of success or failure and of the changes implemented.
- **Certificate validity:** a Certificate of Compliance for SUMS is valid a maximum of three years and is renewable for a further three; existing vehicle type approvals do not lapse merely because the SUMS certificate expires (paras. 6.6, 6.9, 6.10).

## Enforcement and penalties

- **Refusal grounds (R155 para. 5.1.3–5.1.4):** the authority *shall* refuse type approval where the manufacturer did not perform the exhaustive risk assessment (including failing to consider all Annex 5 Part A threats), did not protect the type against identified risks or implement proportionate mitigations, did not secure aftermarket-software environments, or did not test sufficiently before approval — and where it has not received enough information to assess the type at all.
- **Testing by the authority (5.1.2):** the authority or technical service verifies implementation by testing a vehicle of the type, by sampling focused on risks assessed as high.
- **Certificate lifecycle (6.7–6.11):** the CSMS certificate is valid a maximum of three years; the authority may verify continued compliance at any time and **shall withdraw** it if requirements are no longer met; the manufacturer must notify changes affecting its relevance; expiry or withdrawal is treated as a modification of approval under para. 8 and may lead to withdrawal of the type approval.
- **Reporting failure (7.4.2):** if annual reporting or the manufacturer's response is insufficient, the authority may withdraw the CSMS certificate.
- **Conformity of production:** production-facility control methods verified normally **once every three years** (para. 9.1.2); records retained for a period agreed with the authority, **not exceeding 10 years** from definitive discontinuation of production (para. 9.1.1).
- **Withdrawal (10.1–10.2):** approval may be withdrawn for non-compliance or failing sample vehicles, with notification to all Contracting Parties applying the regulation. Monetary penalties are a matter for national law — in the EU through the market-surveillance and penalty provisions of Regulation (EU) 2018/858, in GB through the same framework as retained and amended.

## Timeline and status

| Date | Event |
|---|---|
| 22 January 2021 | UN R155 and R156 enter into force |
| August 2021 | ISO/SAE 21434:2021 published (first edition, dated 2021-08) |
| 6 July 2022 | EU: refusal to grant EU type-approval for new types without D4 cyberattack protection (Reg. (EU) 2019/2144 Annex II) |
| 2023 | ISO 24089 "Road vehicles — Software update engineering" published, the engineering counterpart to R156 (ISO catalogue not reachable; edition details verify) |
| 1 July 2024 | R155 transitional relief for M, N and O type approvals ends (para. 7.3.1) |
| 7 July 2024 | EU: prohibition on registration and placing on the market of non-compliant new vehicles |
| 10 January 2025 | R155 Supplement 3 in force; scope becomes categories L, M, N, O with at least one ECU (OJ L, 2025/5) |
| 16 January 2025 | US: BIS connected-vehicle final rule published, 90 FR 5360, creating 15 CFR part 791 subpart D (regulatory text at 90 FR 5414) |
| 23 July 2025 | Commission Delegated Regulation (EU) 2025/1455 adopted (OJ 29 October 2025), making UN R155 the cybersecurity requirement for L-category vehicles under Delegated Regulation (EU) No 44/2014, except L1e vehicles designed to pedal |
| 13 November 2025 | UK: SI 2025/1110 in force, adding R155 and R156 to the GB type-approval scheme |
| 2026 | China: GB 44495-2024 and GB 44496-2024 reported to take effect for new vehicle types, with existing types following later; no official Chinese source was reachable, so treat the dates as unconfirmed (verify) |
| 1 June 2026 | UK: refusal of GB type-approval for new types of complete and base vehicles (R155 and R156); registration prohibitions follow 1 June 2027, 1 June 2028 (R155 completed vehicles) and 7 July 2029 |
| 12 September 2026 | EU: Data Act Article 3(1) (data accessible by design) starts to bite for connected products placed on the market after this date |
| 11 December 2027 | EU: UN R155 applies to new L-category vehicle types; existing L-category types from 11 June 2029 (Reg. (EU) 2025/1455) |
| 1 July 2029 | R155 transitional relief for L-category type approvals ends |

As of September 2026 the position is: R155 and R156 are fully applicable in the EU to new M, N and O vehicles and to registration of such vehicles; the GB refusal date has passed (1 June 2026) and the next GB milestone is the registration prohibition of 1 June 2027; the EU L-category dates are still ahead (11 December 2027 / 11 June 2029). Supplement 3 remains the most recent R155 text published in the Official Journal and the 2021 text the most recent for R156 — a search of the EU Publications Office register found no later publication of either Regulation. ISO/SAE 21434:2021 is still the only edition that could be confirmed; the ISO catalogue page could not be fetched, so a second edition or revision project cannot be ruled out. UNECE's own pages (including the status document TRANS/WP.29/343, which alone is authoritative on the in-force version) were unreachable — check them before quoting a supplement number.

## Key obligations for security/GRC teams

1. **Establish which approval regimes bite.** EU type approval, GB type approval, Japanese and Korean national schemes and Chinese GB standards have different dates and different scopes for the same vehicle programme. Run the applicability test per market and per vehicle category. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Treat the CSMS certificate as an asset with an expiry date.** Diary re-assessment well before the three-year mark (R155 para. 6.10 requires application "in due time"), and track every change that could affect its relevance.
3. **Make Annex 5 Part A the mandatory input to TARA.** An assessment that cannot show coverage of all Part A threats is a refusal ground; map each Part A entry to the corresponding Part B/C mitigation and record the justification wherever an alternative mitigation is used. See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).
4. **Operationalise annual reporting.** Para. 7.4.1 is a standing regulatory report, not an incident notification: monitoring outcomes, new attacks, and confirmation that mitigations remain effective. Keep it on the same calendar as other regulatory filings. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
5. **Build the cybersecurity case as an audit artefact.** ISO/SAE 21434 work products (RQ/RC/PM/WP identifiers, Annex A activity summary) are what a CSMS audit consumes; ISO/PAS 5112 is reported to give audit-programme guidance for exactly this, though the ISO catalogue could not be fetched (verify). See [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).
6. **Flow obligations to suppliers.** Para. 7.2.2.5 makes supplier dependency management part of the CSMS; use distributed-activity agreements that assign 21434 responsibilities and give audit and evidence rights. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
7. **Keep the RXSWIN register auditable.** The R156 register of software before and after each update, with integrity-validation data, is the single artefact authorities, market surveillance and periodic technical inspection all draw on.
8. **Document every deviation as a formal exception.** Transitional reliance on para. 7.3.1, "technically not feasible" Annex 5 mitigations, and non-consensus cryptographic modules (7.3.8) each require a justification held for the authority. See [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
9. **Reconcile the vehicle programme with the enterprise control framework.** CSMS governance, monitoring and incident processes overlap heavily with ISO 27001 and NIST CSF 2.0 but are assessed separately; map once and test once. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
10. **Evidence the pre-approval testing (7.3.6) and the sampling the authority will run (5.1.2).** Penetration-test scope should be traceable to the high-risk findings of the TARA. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).

## Interplay

- **EU Cyber Resilience Act.** Regulation (EU) 2024/2847 Article 2(2), point (c) disapplies the CRA in its entirety to products with digital elements to which Regulation (EU) 2019/2144 applies; recital 27 explains the carve-out by reference to UN R155 and the certified cybersecurity management system. CRA Article 68 separately amended Regulation (EU) No 168/2013 Annex II Part C1 to add "protection of vehicle against cyberattacks" for L-category vehicles, which Delegated Regulation (EU) 2025/1455 then filled in with UN R155. Aftermarket and accessory digital products that are not part of a type-approved vehicle stay inside the CRA. See [eu-cyber-resilience-act.md](eu-cyber-resilience-act.md).
- **ISO 26262 (functional safety).** ISO/SAE 21434 normatively references ISO 26262-3:2018 for the concept phase; safety and cybersecurity analyses share item definitions and must be reconciled, because a cybersecurity mitigation can create a safety hazard and vice versa. ISO/PAS 8800 extends the family to AI-related safety (verify).
- **ISO 24089** is to R156 what 21434 is to R155 — the engineering method for software update management; ISO/PAS 5112 covers auditing cybersecurity engineering against 21434-derived CSMS processes. Neither could be confirmed against the ISO catalogue, which blocked access (verify).
- **NIS2.** Directive (EU) 2022/2555 Annex II, point 5(e) covers "manufacture of motor vehicles, trailers and semi-trailers" (NACE Rev. 2 section C division 29), so a vehicle manufacturer above the size thresholds is an important entity; check the national transposition for any widening. NIS2 governs the *enterprise*, R155 the *product and its lifecycle*. Incident duties run in parallel and to different authorities. See [nis2.md](nis2.md).
- **GDPR.** Connected-vehicle telemetry, forensic logging under R155 para. 7.3.7 and diagnostic data are frequently personal data; the forensic-capability obligation must be reconciled with data minimisation and retention limits. See [gdpr.md](gdpr.md).
- **EU Data Act.** Regulation (EU) 2023/2854 has applied since 12 September 2025 and gives vehicle users access to readily available product and related-service data, constraining how manufacturers gate it — directly in tension with security arguments for closing interfaces. The Article 3(1) "accessible by design" duty bites for connected products placed on the market after 12 September 2026 (Article 50). See [eu-data-act.md](eu-data-act.md).
- **United States.** There is no federal vehicle cybersecurity type approval. NHTSA's "Cybersecurity Best Practices for the Safety of Modern Vehicles" (87 FR 55459, 9 September 2022, Docket NHTSA-2020-0087) is a notice of federal guidelines and non-binding. The binding US rule is supply-chain-based: 15 CFR part 791 subpart D prohibits import or sale of connected vehicles incorporating covered VCS/ADS software with PRC or Russian nexus from **model year 2027**, and import of VCS hardware from **model year 2030** (or 1 January 2029 for units without a model year) — 15 CFR 791.308. Connected vehicle manufacturers and VCS hardware importers file a Declaration of Conformity with BIS at least 60 days before the first import or sale for each model or calendar year, and keep primary business records for at least 10 years (15 CFR 791.305, 791.312). See [us-doj-bulk-data-rule.md](us-doj-bulk-data-rule.md) for the adjacent US data-transfer restrictions.
- **China.** GB 44495-2024 (vehicle cybersecurity) and GB 44496-2024 (software update) are mandatory national standards administered through the Chinese type-approval and access process, reported effective for new vehicle types from 1 January 2026, though no official Chinese source was reachable to confirm the date (verify); their structure parallels R155/R156 but compliance is assessed domestically. See [china-pipl-dsl-csl.md](china-pipl-dsl-csl.md).
- **Enterprise frameworks.** CSMS audits accept ISO 27001-style governance evidence for the organisational clauses, but neither ISO 27001 nor NIST CSF 2.0 satisfies R155 on its own — the vehicle-type requirements have no analogue there. See [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) and [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md).

## Primary sources

- UN Regulation No. 155, consolidated text incorporating Supplement 3, in force 10 January 2025 — Official Journal L, 2025/5: https://eur-lex.europa.eu/eli/reg/2025/5/oj (legal text, fetched)
- UN Regulation No. 155, original version as published in OJ L 82/30, 9 March 2021 — https://eur-lex.europa.eu/eli/reg/2021/387/oj (legal text, fetched)
- UN Regulation No. 156, OJ L 82/60, 9 March 2021 — https://eur-lex.europa.eu/eli/reg/2021/388/oj (legal text, fetched)
- Regulation (EU) 2019/2144 (General Safety Regulation), Annex II item D4 and implementation-date notes — https://eur-lex.europa.eu/eli/reg/2019/2144/oj (legal text, fetched)
- Commission Delegated Regulation (EU) 2025/1455 of 23 July 2025 (L-category cybersecurity) — https://eur-lex.europa.eu/eli/reg_del/2025/1455/oj (legal text, fetched)
- Regulation (EU) 2024/2847 (Cyber Resilience Act), Article 2(2)(c) exclusion, recital 27 and the Article 68 amendment to Regulation (EU) No 168/2013 — https://eur-lex.europa.eu/eli/reg/2024/2847/oj (legal text, fetched)
- Regulation (EU) 2023/2854 (Data Act), application date — https://eur-lex.europa.eu/eli/reg/2023/2854/oj (legal text, fetched)
- The Road Vehicles (Type-Approval) (Amendment) (No. 3) Regulations 2025, SI 2025/1110 — https://www.legislation.gov.uk/uksi/2025/1110/made (legal text, fetched)
- ISO/SAE 21434:2021, publisher preview of the published standard (scope, clause structure, definitions, abbreviations) — https://cdn.standards.iteh.ai/samples/70918/9c85ee86ba1945fe845ac38711773665/ISO-SAE-21434-2021.pdf (publisher document, fetched). Full text is paywalled; catalogue entry at https://www.iso.org/standard/70918.html could not be fetched (blocked)
- 15 CFR part 791 subpart D, ICTS Supply Chain: Connected Vehicles (final rule 90 FR 5360 of 16 January 2025; subpart D text at 90 FR 5414) — https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-E/part-791/subpart-D (legal text, fetched)
- NHTSA, "Cybersecurity Best Practices for the Safety of Modern Vehicles", notice of federal guidelines, 87 FR 55459, 9 September 2022, Docket NHTSA-2020-0087 — https://www.federalregister.gov/documents/2022/09/09/2022-19507/cybersecurity-best-practices-for-the-safety-of-modern-vehicles (regulator guidance)
- UK Department for Transport explanatory memorandum on Commission Delegated Regulation (EU) 2025/1455 — https://assets.publishing.service.gov.uk/media/6925d3a09fd433badebc3190/Annex_A_-_EM_on_UN_Regulation_155_and_eCall_systems.pdf (regulator guidance, fetched)
- UNECE status document TRANS/WP.29/343 (authoritative list of Contracting Parties applying each UN Regulation and of in-force versions) — https://unece.org/status-1958-agreement-and-annexed-regulations (publisher page, **could not be fetched** — access blocked; the Official Journal reproductions above were used instead)
- Directive (EU) 2022/2555 (NIS2), Annex II point 5(e) — https://eur-lex.europa.eu/eli/dir/2022/2555/oj (legal text, fetched)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
