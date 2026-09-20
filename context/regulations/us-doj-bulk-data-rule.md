# US DOJ Data Security Program — bulk sensitive personal data and countries of concern (28 CFR Part 202)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Executive Order 14117 (28 February 2024, 89 FR 15421) implemented by DOJ final rule "Preventing Access to U.S. Sensitive Personal Data and Government-Related Data by Countries of Concern or Covered Persons", 90 FR 1636 (8 January 2025), codified at 28 CFR Part 202; corrected at 90 FR 16466 (18 April 2025). Statutory authority: IEEPA (50 U.S.C. 1701 et seq.) |
| Regulator | DOJ National Security Division (NSD), Foreign Investment Review Section; security requirements written by CISA (DHS) and incorporated by reference (§ 202.248) |
| Status and key dates | In force. Prohibitions and restrictions effective 12:01 a.m. ET, 8 April 2025 (§ 202.216); due-diligence, audit and reporting duties (subpart J, §§ 202.1103–202.1104) operative from 6 October 2025; NSD limited-enforcement policy covered 8 April–8 July 2025; Part 202 unamended since the 18 April 2025 correcting amendment |
| Who is covered | Every U.S. person (citizens, permanent residents, U.S.-organized entities incl. foreign branches, anyone in the U.S.) that knowingly engages in a "covered data transaction" giving a country of concern or covered person access to government-related data or bulk U.S. sensitive personal data |
| Countries of concern | China (incl. Hong Kong and Macau), Cuba, Iran, North Korea, Russia, Venezuela (§ 202.601) |
| Structure | 14 subparts: definitions (B), prohibited transactions (C), restricted transactions (D), exemptions (E), countries of concern (F), covered persons (G), licensing (H), advisory opinions (I), due diligence and audits (J), reporting and recordkeeping (K), submissions (L), penalties (M), Government-Related Location Data List (N) |
| Penalties | IEEPA: civil up to the greater of $368,136 (the figure in § 202.1301(a)(2); IEEPA amounts are inflation-adjusted) or twice the transaction value; criminal (willful) up to $1,000,000 and 20 years' imprisonment (§ 202.1301(a)(3)). Knowledge standard, not strict liability |
| Assessment model | Not a certification. Restricted transactions require a data compliance program, annual officer certification, and an annual independent audit; records kept 10 years |
| Neighbours | PADFA (15 U.S.C. 9901, FTC-enforced data-broker ban); CFIUS; OFAC/BIS export-control style compliance; sectoral privacy law (HIPAA, GLBA, state privacy) does not displace it |

## What it is

The Data Security Program (DSP) is a national-security regime, not a privacy law. EO 14117 declared that access by countries of concern to Americans' bulk sensitive personal data and to U.S. Government-related data is an unusual and extraordinary threat under IEEPA and directed the Attorney General to prohibit or restrict U.S. persons from engaging in classes of transactions that enable such access (EO Sec. 2). DOJ issued an ANPRM (5 March 2024), an NPRM (29 October 2024) and the final rule (8 January 2025). NSD describes the result as "effectively export controls" for data: some transactions are flatly prohibited, others are permitted only if CISA-defined security requirements are met, and the whole thing is backed by licensing, advisory opinions and IEEPA penalties in the manner of OFAC sanctions programs.

Two features distinguish it from privacy regimes. First, it turns on *who gets access* (a country of concern or covered person) and on *transaction type* (data brokerage, vendor, employment, investment agreements), not on consent or purpose — there is no consent-based exception. Second, thresholds are volumetric: the rule bites only when data about more than a set number of U.S. persons or devices is involved, aggregated over the preceding 12 months (§ 202.205), except for government-related data, which is covered regardless of volume.

## Who it covers / Scope

**Covered data transaction** (§ 202.210) = any transaction that involves access by a country of concern or covered person to government-related data or bulk U.S. sensitive personal data *and* involves (1) data brokerage, (2) a vendor agreement, (3) an employment agreement, or (4) an investment agreement. The obligation sits on the U.S. person; the prohibitions apply to transactions engaged in "knowingly" (actual knowledge or reason to know).

**Covered persons** (§ 202.211): (1) foreign entities 50%-or-more owned by, organized under the laws of, or with principal place of business in a country of concern; (2) foreign entities 50%-or-more owned by covered persons; (3) foreign individuals who are employees or contractors of a country of concern or covered-person entity; (4) foreign individuals primarily resident in a country of concern; (5) any person the Attorney General designates, published in the Federal Register and carried on NSD's Covered Persons List (§ 202.701) — no designations had been published as of September 2026. The 50% rule aggregates direct and indirect ownership (OFAC-style). Country-of-concern citizens located in the U.S. are U.S. persons, not covered persons, unless designated.

**Sensitive personal data** (§ 202.249) and **bulk thresholds** (§ 202.205, counted over the preceding 12 months, per U.S.-person/foreign-person pair, whether one transaction or aggregated):

| Category | Definition anchor | Bulk threshold |
|---|---|---|
| Human genomic data | § 202.224 (subset of human 'omic data) | > 100 U.S. persons |
| Other human 'omic data (epigenomic, proteomic, transcriptomic) | § 202.224 | > 1,000 U.S. persons |
| Biometric identifiers | § 202.204 (facial images, voice prints, iris, fingerprints, gait, keyboard usage patterns enrolled in a biometric system, and templates) | > 1,000 U.S. persons |
| Precise geolocation data | § 202.242 (location within 1,000 metres, real-time or historical) | > 1,000 U.S. devices |
| Personal health data | § 202.241 (broader than HIPAA PHI; includes fitness logs, vitals, medication purchases) | > 10,000 U.S. persons |
| Personal financial data | § 202.240 (card/account data, statements, credit reports) | > 10,000 U.S. persons |
| Covered personal identifiers | § 202.212 (listed identifiers in combination, e.g. SSN + device ID; demographic/contact data linked only to other contact data is excluded) | > 100,000 U.S. persons |
| Combined data | § 202.205(g) | lowest threshold of any category present |

Exclusions from sensitive personal data: data not about an individual (trade secrets), data lawfully available from public government records or widely distributed media, personal communications, and information or informational materials.

**Government-related data** (§ 202.222), covered at *any* volume: precise geolocation data for any area on the Government-Related Location Data List (§ 202.1401, geofenced coordinates around military and national-security sites), and any sensitive personal data that a transacting party *markets* as linked to current or recent former U.S. Government employees, contractors or former senior officials, including military and Intelligence Community.

**Exempt transactions** (subpart E; the § 202.1102 on-demand reporting and § 202.1104 rejected-transaction reporting duties still apply): personal communications; information or informational materials; travel; official U.S. Government business, grants and contracts (§ 202.504); financial services ordinarily incident to banking, capital markets, insurance, payments, e-commerce (§ 202.505); intra-corporate-group administrative transactions with a country-of-concern subsidiary — HR, payroll, tax, permits, audit and legal, risk management, travel, customer support, benefits, communications (§ 202.506); transactions required or authorized by federal law or listed international agreements (§ 202.507); investment agreements subject to a CFIUS action (§ 202.508); telecommunications services, other than data brokerage (§ 202.509); FDA regulatory-approval data and clinical-investigation/post-marketing data that is de-identified or pseudonymized to 21 CFR 314.80 standards (§§ 202.510–202.511).

## Core obligations

### Prohibited transactions (subpart C) — authorized only by a general or specific licence (subpart H)

| Section | Prohibition |
|---|---|
| § 202.301 | Data brokerage (sale, licensing of access, or similar commercial transfer to a recipient that did not collect the data directly from the individuals; § 202.214) with a country of concern or covered person. DOJ's own example treats licensing an AI model that can regurgitate bulk training data as data brokerage |
| § 202.302 | Data brokerage with *any* foreign person (not a covered person) unless the contract bars onward transfer to countries of concern/covered persons and the U.S. person reports known or suspected breaches of that clause to NSD within 14 days |
| § 202.303 | Any covered data transaction giving a country of concern or covered person access to bulk human 'omic data or to human biospecimens from which it could be derived — subpart D does not apply, so vendor, employment and investment agreements are prohibited rather than merely restricted (§ 202.401(b)) |
| § 202.304 | Evasions, attempts, causing violations, conspiracies |
| § 202.305 | Knowingly directing a prohibited or non-compliant restricted transaction (e.g. a U.S. officer of a foreign company approving one); payment processing and lending are expressly not "directing" |

### Restricted transactions (subpart D) — permitted only with the CISA security requirements

§ 202.401: vendor agreements (including cloud computing, § 202.258), employment agreements (§ 202.217, including board seats and executive roles) and investment agreements (§ 202.228; passive holdings in public securities, registered funds and LP interests are excluded) with a country of concern or covered person are allowed only if the U.S. person complies with the **Security Requirements for Restricted Transactions** (CISA, January 2025; notice of availability 90 FR 1528). Substituting "equivalent" controls is non-compliance and makes the transaction prohibited (§ 202.401 Example 2).

| CISA requirement (Section I: organizational and covered-system level) | Specific |
|---|---|
| Asset inventory of covered systems with IP addresses | Updated at least monthly for IT assets (NIST CSF 2.0 ID.AM-01/08, CPG 1.A) |
| Accountable executive for cybersecurity and for GRC | Named individual(s), e.g. CISO (GV.RR-02) |
| Known exploited vulnerabilities on internet-facing systems | Remediate all within 45 calendar days; compensating controls if patching infeasible; post-patch compromise assessment |
| Vendor/supplier agreements for covered systems | Documented with contractual IT and cybersecurity requirements |
| Network topology; hardware/software allowlist; incident response plan | Maintained; approval before deployment; IR plan reviewed annually |
| MFA on all covered systems | AAL2/AAL3 per NIST SP 800-63B, or passwords of 15+ characters where MFA infeasible |
| Access revocation on termination or role change | Promptly, e.g. day of departure |
| Security and access logging | Central store (SIEM or equivalent), retained at least 12 months; until final resolution if a breach or violation is under U.S. Government review; access to logs restricted |
| Deny-by-default connections; organization-level identity and credential management | Least privilege by transaction/function |
| Internal data risk assessment (Section I.C) | Evaluates whether the chosen Section II mix prevents access to data that is linkable, identifiable, unencrypted or decryptable with commonly available technology; includes mitigation strategy; reviewed annually (NIST Privacy Framework ID.RA-P1, P3–P5) |

Section II (data level) requires a combination sufficient to prevent such access: data minimization and masking backed by a written retention and deletion policy reviewed annually (aggregation must reach the § 202.205 bulk count; pseudonymization, de-identification, anonymization); encryption in transit and at rest (TLS 1.2+ minimum) with keys not co-located with data, not stored in a country of concern, and never accessible to covered persons; privacy-enhancing technologies (homomorphic encryption, differential privacy) that reveal nothing reconstructable to covered persons; and IAM configured to deny covered persons access to covered data. Systems performing the processing or holding keys are themselves covered systems.

### Compliance program, audit, records and reports (subparts J–K)

| Duty | Section | Requirement |
|---|---|---|
| Data compliance program | § 202.1001 | By 6 October 2025 for anyone in restricted transactions: risk-based, auditable verification of data types and volumes, counterparties (ownership, citizenship, residence), end use and transfer method; vendor identity verification; written program policy and written security-requirements policy, each **certified annually** by an officer, executive or compliance employee |
| Independent audit | § 202.1002 | Once per calendar year in which restricted transactions occur, covering the preceding 12 months; auditor must be qualified, independent, and not a covered person (internal audit acceptable only if sufficiently independent — FAQ 85/93); scope covers transactions, compliance program, records and security requirements; written report to the U.S. person within 60 days of completion; report retained 10 years |
| Recordkeeping | § 202.1101 | Full and accurate record of every transaction subject to the Part, available for examination for at least 10 years; for restricted transactions also the certified policies, audit results, due-diligence documentation, transfer method, start/end dates, agreements, licences/advisory opinions and an annual certification of record completeness |
| Reports on demand | § 202.1102 | NSD may require complete information on any transaction (applies even to exempt transactions) |
| Annual report | § 202.1103 | Only U.S. persons in restricted *cloud-computing* transactions that are 25%-or-more owned by a country of concern or covered person; due 1 March for the prior calendar year |
| Rejected prohibited transactions | § 202.1104 | Report within 14 days of affirmatively rejecting (including by automated tooling) an offer to engage in prohibited data brokerage |
| Onward-transfer breach reports | § 202.302(b) | Within 14 days of learning of a known or suspected breach of the contractual bar |

Submissions go electronically to NSD (NSD.FIRS.datasecurity@usdoj.gov or the official portal) and must be certified as true, accurate and complete by an officer, director or responsible compliance employee (§ 202.1201). NSD's Compliance Guide expects senior-management ownership: a named compliance lead with senior authority and resources, CEO review, and the annual certification reported to the board and audit committee.

### Licences and advisory opinions (subparts H–I)

General licences (§ 202.801) authorize classes of transactions on stated terms and may impose reporting conditions; failing to file the required reports can nullify the authorization. Specific licences are case-by-case, and DOJ policy is not to grant one where a general licence applies (§ 202.801(b)). No general licence had been published among NSD's Data Security Program resources as of September 2026. Advisory opinions (§ 202.901) state the Department's present enforcement intentions for an actual, disclosed transaction, and only for the prospective portion of it; hypothetical, anonymous, non-party and ex post facto requests are excluded.

## Enforcement and penalties

- **Civil** (IEEPA § 206 via § 202.1301): up to the greater of $368,136 or twice the value of the violative transaction, per violation, adjusted annually for inflation. Pre-penalty notice, opportunity to respond, and finding-of-violation procedures at §§ 202.1302–202.1306; administrative collection and litigation available.
- **Criminal**: willful violation, attempt, conspiracy, or aiding and abetting — fine up to $1,000,000 and/or up to 20 years' imprisonment for natural persons. False statements prosecutable under 18 U.S.C. 1001.
- **Standard of liability**: "knowingly" — actual knowledge or reason to know (FAQ 103/107). NSD weighs sophistication, scale and sensitivity of data, and evidence of evasion; voluntary self-disclosure and cooperation are mitigating. NSD has said further enforcement guidance on self-disclosure and mitigating factors is forthcoming (FAQ 107); none had been published among its Data Security Program resources as of September 2026.
- **Limited-enforcement window**: 8 April–8 July 2025, NSD did not prioritize civil enforcement against persons making good-faith efforts to comply (evidence: data-flow reviews, contract renegotiation, deploying the CISA measures). Egregious willful violations were still pursued. The window has closed and NSD has published no successor policy; its resources page listed none as of September 2026. No public DSP enforcement action had been announced as of that date.

## Timeline and status

| Date | Event |
|---|---|
| 28 Feb 2024 | EO 14117 signed (published 1 Mar 2024, 89 FR 15421) |
| 5 Mar 2024 | ANPRM published by DOJ NSD |
| 24 Apr 2024 | PADFA enacted as Division I of Pub. L. 118-50; effective 60 days later (23 June 2024) |
| 29 Oct 2024 | NPRM published (Docket NSD 104, RIN 1124-AA01) |
| 8 Jan 2025 | Final rule (90 FR 1636) and CISA security requirements notice of availability (90 FR 1528) published |
| 8 Apr 2025 | Part 202 effective; prohibitions and restrictions apply |
| 11 Apr 2025 | NSD publishes Compliance Guide, FAQs and Implementation and Enforcement Policy through 8 July 2025 |
| 18 Apr 2025 | Correcting amendment (cross-reference fix in § 202.401) effective, 90 FR 16466 |
| 8 Jul 2025 | Limited-enforcement period ends |
| 24 Sep 2025 | FAQs updated (108 FAQs) |
| 6 Oct 2025 | Subpart J (compliance program, audits) and §§ 202.1103–202.1104 (annual and rejected-transaction reports) operative (DOJ's resources page describes this phase-in as 5 October 2025; the rule text and NSD's enforcement policy both say 6 October) |
| 24 Oct 2025 | NIH Policy on Enhancing Security Measures for Human Biospecimens takes effect (published 12 Dec 2025), written to align NIH-funded biospecimen handling with EO 14117 and 28 CFR Part 202 |
| 1 Mar 2026 | First annual reports due under § 202.1103 for calendar 2025 (only the cloud/25%-owned cohort) |
| 1 Apr 2026 | FinCEN proposes an IEEPA whistleblower program (31 CFR part 1010) whose preamble expressly names the DSP as a covered IEEPA program; comments closed 1 June 2026, not final as of September 2026 |
| 13 May 2026 | Presidential notice continues the EO 13873 national emergency on which the DSP's IEEPA authority rests |
| Sep 2026 | No Federal Register document affecting Part 202 has been published since 18 April 2025, and the FAQs remain at the 24 September 2025 version. RIN 1124-AA01 was carried as a completed action in the Spring 2025 Unified Agenda and does not appear in the 2026 agenda. EO 14117 Sec. 5 required an Attorney General report to the President within one year of the regulations' effective date (i.e. by 8 April 2026); no published report was located (verify). Watch for general licences, Covered Persons List designations, enforcement guidance and new FAQs |

## Key obligations for security/GRC teams

1. **Know your data**: inventory sensitive personal data by the six § 202.249 categories and count U.S. persons/devices against the § 202.205 thresholds on a rolling 12-month basis; flag any dataset marketed as government-linked and any precise geolocation touching the § 202.1401 geofences. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md) and [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).
2. **Screen counterparties, staff and investors** for covered-person status — country-of-concern organization, 50% aggregate ownership, residence, employment — and against the NSD Covered Persons List at a frequency set by documented risk; the list is not exhaustive. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../templates/vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md).
3. **Classify every covered data transaction**: prohibited (data brokerage, 'omic data) must stop or be licensed; restricted (vendor incl. cloud, employment, investment) needs the full CISA control set before the transaction proceeds. Offshore IT support, SOC or development staff in a country of concern with access to bulk data are restricted employment/vendor transactions.
4. **Add the onward-transfer clause** to every data-brokerage contract with any foreign person and stand up the 14-day breach-report path (§ 202.302).
5. **Implement and map the CISA requirements** to existing controls: monthly asset inventory, 45-day KEV remediation, MFA/AAL2, 12-month central logging, key custody outside countries of concern, data-level minimization or encryption. Map to [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md) and [../frameworks/cis-controls-v8.md](../frameworks/cis-controls-v8.md); see [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).
6. **Build the data compliance program and certification cycle**: written program policy, written security-requirements policy, annual officer certification, board/audit-committee reporting. Use [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md) and [../../templates/policy-template.md](../../templates/policy-template.md).
7. **Commission the annual audit** (independent, non-covered-person auditor; 60-day report; 10-year retention) and plan evidence with [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md) and [../../templates/audit-evidence-request-list.md](../../templates/audit-evidence-request-list.md).
8. **Wire reporting clocks into incident and deal processes**: 14-day rejected-transaction and onward-transfer reports, 1 March annual report where applicable, on-demand § 202.1102 responses. Log them in [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md); see [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
9. **Track gaps as exceptions, not workarounds** — "equivalent" controls do not authorize a restricted transaction. See [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
10. **Horizon-scan** for general licences, Covered Persons List updates, FAQ revisions and NSD enforcement guidance. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

- **PADFA (Protecting Americans' Data from Foreign Adversaries Act of 2024, 15 U.S.C. 9901)**: bans *data brokers* (entities selling data they did not collect directly, to non-service-providers) from making "personally identifiable sensitive data" of U.S. individuals available to a foreign adversary country (China, Iran, North Korea, Russia per 10 U.S.C. 4872(d)(2)) or an entity it controls (20% ownership stake, or under its direction). FTC enforces as an unfair or deceptive practice under FTC Act § 18(a)(1)(B). Broader data list (includes minors, private communications, intimate imagery, video-viewing, online activity), no volume threshold, an exclusion for data transmitted at the individual's own request or direction, and no licensing or advisory-opinion mechanism. DSP covers two more countries, all U.S. persons, first-party data, and onward transfers. Treat PADFA as a floor for data-broker business lines and DSP as the operating regime.
- **HIPAA / GLBA / state privacy law**: "personal health data" and "personal financial data" are wider than PHI and NPI, and DSP thresholds are counted differently; compliance with [hipaa.md](hipaa.md), [glba-ftc-safeguards.md](glba-ftc-safeguards.md) or [us-state-privacy.md](us-state-privacy.md) does not satisfy the DSP, and DSP compliance does not satisfy them. De-identification under HIPAA Safe Harbor is not automatically sufficient — CISA requires linkability to be minimized against data the recipient is known to hold.
- **GDPR transfer thinking, inverted**: GDPR restricts exports from the EU; the DSP restricts access *by* specific foreign parties regardless of where data sits. A vendor with a subsidiary in a country of concern can trip both regimes on one contract. See [gdpr.md](gdpr.md).
- **CFIUS**: an investment agreement covered by a CFIUS mitigation agreement or order that recites it is a "CFIUS action" is exempt from Part 202 from that instrument's effective date (§ 202.508); before then the DSP applies.
- **AI systems**: DOJ's § 202.301 example treats licensing access to a model that can reproduce bulk training data as data brokerage; model licensing, fine-tuning vendors and offshore annotation teams belong in the transaction inventory. See [eu-ai-act.md](eu-ai-act.md) and [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).
- **SEC disclosure**: a DSP enforcement action or a forced vendor exit can be a material cybersecurity or business risk for registrants; see [sec-cyber-disclosure.md](sec-cyber-disclosure.md).
- **Framework anchors**: the CISA requirements cite NIST CSF 2.0, NIST Privacy Framework 1.0 and CISA Cross-Sector Cybersecurity Performance Goals control-by-control; use [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md) to reuse existing evidence.

## Primary sources

- 28 CFR Part 202, current eCFR text (legal text; fetched via the eCFR versioner API): https://www.ecfr.gov/current/title-28/chapter-I/part-202
- DOJ final rule, 90 FR 1636, 8 January 2025 (legal text and preamble incl. the October 2025 phase-in rationale): https://www.federalregister.gov/documents/2025/01/08/2024-31486/preventing-access-to-us-sensitive-personal-data-and-government-related-data-by-countries-of-concern
- Correcting amendment, 90 FR 16466, 18 April 2025 (legal text): https://www.federalregister.gov/documents/2025/04/18/2025-06477/pertaining-to-preventing-access-to-us-sensitive-personal-data-and-government-related-data-by
- Executive Order 14117, 89 FR 15421, 1 March 2024 (legal text, GovInfo): https://www.govinfo.gov/content/pkg/FR-2024-03-01/html/2024-04573.htm
- CISA, Security Requirements for Restricted Transactions (E.O. 14117 Implementation), January 2025 (incorporated by reference at § 202.248; PDF): https://www.cisa.gov/sites/default/files/2025-01/Security_Requirements_for_Restricted_Transaction-EO_14117_Implementation508.pdf — landing page https://www.cisa.gov/resources-tools/resources/EO-14117-security-requirements
- CISA notice of availability of the security requirements, 90 FR 1528, 8 January 2025 (Federal Register notice and comment responses): https://www.federalregister.gov/documents/2025/01/08/2024-31479/notice-of-availability-of-security-requirements-for-restricted-transactions-under-executive-order
- DOJ NSD Data Security Program page (regulator guidance index): https://www.justice.gov/nsd/data-security
- DOJ NSD, Data Security Program: Compliance Guide, 11 April 2025 (regulator guidance): https://www.justice.gov/opa/media/1396356/dl
- DOJ NSD, Data Security Program: Frequently Asked Questions, updated 24 September 2025 (regulator guidance): https://justice.gov/nsd/media/1415006/dl
- DOJ NSD, Implementation and Enforcement Policy Through July 8, 2025, 11 April 2025 (regulator guidance; also restated in FAQ 4): https://www.justice.gov/opa/media/1396346/dl?inline
- Pub. L. 118-50, Division I — Protecting Americans' Data from Foreign Adversaries Act of 2024, 138 Stat. 960 (legal text, GovInfo): https://www.govinfo.gov/content/pkg/PLAW-118publ50/html/PLAW-118publ50.htm
- Unified Agenda entry, DOJ/NSD RIN 1124-AA01, Spring 2025 — listed as a completed action (status check): https://www.reginfo.gov/public/do/eAgendaViewRule?pubId=202504&RIN=1124-AA01
- NIH Policy on Enhancing Security Measures for Human Biospecimens, effective 24 October 2025, published 12 December 2025 (adjacent federal policy aligned to EO 14117 and 28 CFR Part 202): https://www.federalregister.gov/documents/2025/12/12/2025-22618/nih-policy-on-enhancing-security-measures-for-human-biospecimens
- FinCEN, Whistleblower Incentives and Protections, proposed rule, 1 April 2026 (pending IEEPA whistleblower program naming the DSP): https://www.federalregister.gov/documents/2026/04/01/2026-06271/whistleblower-incentives-and-protections
- Continuation of the National Emergency With Respect to Securing the Information and Communications Technology and Services Supply Chain, 13 May 2026 (presidential notice continuing the EO 13873 emergency): https://www.federalregister.gov/documents/2026/05/13/2026-09671/continuation-of-the-national-emergency-with-respect-to-securing-the-information-and-communications

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
