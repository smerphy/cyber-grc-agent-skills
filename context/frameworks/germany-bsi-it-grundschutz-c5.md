# Germany — BSI standards: IT-Grundschutz, BSI-Standards 200-x, C5 and the BSIG/KRITIS regime

## At a glance

| Attribute | Detail |
|---|---|
| Publisher / regulator | Bundesamt für Sicherheit in der Informationstechnik (BSI), Bonn — standards body, certification authority, national CSIRT and NIS2 supervisor in one |
| Three distinct things | (1) **IT-Grundschutz** — an ISMS methodology + control catalogue, ISO/IEC 27001-compatible, voluntary; (2) **C5** — an auditable cloud criteria catalogue attested under ISAE 3000; (3) **BSIG** — the BSI Act, binding law implementing NIS2 in Germany |
| IT-Grundschutz components | BSI-Standards 200-1 (ISMS requirements), 200-2 (methodology: Basis-, Kern-, Standard-Absicherung), 200-3 (risk management), 200-4 (BCMS); IT-Grundschutz-Kompendium Edition 2023 (available since 1 February 2023), Bausteine in 10 thematic layers (ISMS … APP … IND) |
| C5 current versions | **C5:2020** (121 criteria) and **C5:2026** (168 criteria), both in 17 subject areas. C5:2026 v1.0.0 published 7 April 2026; the fetched PDF is v1.0.1 |
| C5 transition | C5:2026 applies to type 1 engagements as of / type 2 periods beginning on or after **1 June 2027**; earlier adoption permitted. No mixing of C5:2020 and C5:2026 in one engagement |
| Certifiable? | IT-Grundschutz: **ISO 27001 certificate on the basis of IT-Grundschutz**, issued by BSI on a BSI-certified auditor's report (Standard- or Kern-Absicherung); a BSI *Testat* for Basis-Absicherung. C5: not a BSI certificate — an **audit attestation** (ISAE 3000 (Revised), German equivalent IDW PS 860; type 1 or type 2) issued by the provider's own auditor; BSI neither selects auditors nor reviews reports |
| Binding law | **BSI-Gesetz (BSIG)** of 2 December 2025 (BGBl. 2025 I Nr. 301), in force **6 December 2025**, plus the **KRITIS-Dachgesetz** of 11 March 2026 (BGBl. 2026 I Nr. 66), in force 17 March 2026 |
| Incident clock (BSIG § 32) | Early warning ≤ **24 h**, full notification ≤ **72 h**, interim report on request, final report ≤ **1 month** after the 72-h notification — to a joint BSI/BBK reporting point |
| Penalty ceiling (BSIG § 65) | Up to **€10 m** (besonders wichtige Einrichtungen) / **€7 m** (wichtige Einrichtungen); for entities with group turnover > €500 m, up to **2 %** / **1.4 %** of total worldwide turnover for core risk-management and reporting breaches |
| Relationship to neighbours | IT-Grundschutz ≈ a prescriptive German implementation route to ISO/IEC 27001; C5 ≈ a German SOC 2-style cloud attestation, now aligned to EUCS "Substantial"; BSIG = NIS2 transposition |

## What it is

Germany runs three loosely coupled layers under one authority. **IT-Grundschutz** is the oldest: a full ISMS methodology plus a catalogue of modelled threats and requirements, designed so that an organisation can reach an ISO/IEC 27001 certificate without having to invent its own control set. **C5** (Cloud Computing Compliance Criteria Catalogue), first published in 2016, is a criteria catalogue for cloud services audited by public accountants and reported on in a standardised format; BSI states that over a hundred attestations have been granted to national, European and global providers. **The BSIG** is the statute — it defines BSI's powers, and since the December 2025 recast it carries Germany's NIS2 obligations for "besonders wichtige" and "wichtige" entities.

The two standards are deliberately non-legislative: both are recommendatory for the private sector, and both acquire teeth only where another instrument points at them — C5 through the federal minimum standard for external cloud services and through § 393 SGB V for health data, IT-Grundschutz through federal administration rules, sector security standards (B3S) and procurement.

Both are mid-transition. IT-Grundschutz is being rebuilt ("Fortentwicklung des IT-Grundschutz") into a fully process-oriented, machine-readable **JSON rule set** that will replace the Kompendium; the Basis/Standard/erhöhter-Schutzbedarf tiers give way to weighted "Leistungszahlen" with dynamic thresholds, the WiBA checklists become a permanent component, and BSI states the current IT-Grundschutz stays applicable through a multi-year transition with a Kompendium update also planned. C5 has already completed its equivalent step with C5:2026. (BSI's own page does not use the label "IT-Grundschutz++" — treat that name as informal.)

## Who it covers / Scope

**IT-Grundschutz and C5** are voluntary for the general market. Binding hooks:

| Hook | Effect |
|---|---|
| Federal authorities procuring cloud for official data | C5 compliance required via the BSI minimum standard on the use of external cloud services |
| § 393 SGB V (cloud use in healthcare) | Providers, sickness and care funds and their processors may process social and health data in a cloud service only with a current **C5 attestation against the C5 basic criteria**, plus implementation of the complementary customer criteria in the report. Type 1 sufficed until 30 June 2025; a **type 2** attestation is required from 1 July 2025 (18-month type 1 grace for systems first placed on the market after that date). An attestation to a standard of comparable or higher assurance may substitute |
| B3S (branchenspezifische Sicherheitsstandards) | Operators of critical installations, besonders wichtige Einrichtungen and their sector associations may codify "state of the art" (BSIG § 30(8)–(9)); BSI formally determines suitability on application. There is **no legal duty to produce a B3S**, but operators audited against a recognised one gain legal certainty on state of the art |

**BSIG scope** (§ 28) — two tiers, sized on the EU SME Recommendation 2003/361/EC (excluding Art. 3(4) of its annex):

| Tier | Test |
|---|---|
| Besonders wichtige Einrichtungen | **Operators of critical installations** (§ 28(1) no. 1, regardless of size); qualified trust service providers, TLD name registries, DNS service providers (no size test); public telecoms with ≥ 50 staff **or** > €10 m turnover *and* balance-sheet total; other Annex 1 entity types with **≥ 250 staff** or **> €50 m turnover and > €43 m balance-sheet total** |
| Wichtige Einrichtungen | Trust service providers; smaller public telecoms; other Annex 1 and Annex 2 entity types with **≥ 50 staff** or **> €10 m turnover and balance-sheet total** |

Carve-outs: DORA financial entities are excluded from §§ 30, 31, 32, 35, 36, 38, 39 (§ 28(6)); so are telematics-infrastructure operators under SGB V. § 28(5) disapplies §§ 30, 31, 32, 35, 36, 38, 39, 61 and 62 for operators of public telecoms networks and providers of publicly available telecoms services, and for EnWG energy network, energy installation and digital energy service operators subject to §§ 5c–5e EnWG — but not for any further critical installations or further Annex 1/2 activities they run. Negligible business activities may be disregarded when assigning an entity type (§ 28(3)).

## Structure and requirements

### IT-Grundschutz

| Element | Content |
|---|---|
| BSI-Standard 200-1 | General ISMS requirements; compatible with ISO/IEC 27001 and informed by ISO/IEC 27002 |
| BSI-Standard 200-2 | The methodology, in three routes: **Basis-Absicherung** (broad first-pass hardening), **Kern-Absicherung** (crown jewels first), **Standard-Absicherung** (the classic full-scope route) |
| BSI-Standard 200-3 | All risk-related steps bundled, designed to attach directly to the IT-Grundschutz analysis |
| BSI-Standard 200-4 | BCMS build-and-run guidance, modernised standard **Version 1.0, May 2023**; a companion requirement catalogue carries a mapping to ISO 22301:2019, and BSI states no certification against 200-4 is currently planned |
| IT-Grundschutz-Kompendium Edition 2023 | **Bausteine** (modules) of roughly ten pages each: elementary threats for a topic, then its security requirements, arranged in **10 layers**. A risk assessment for *normal* protection needs is already baked into each Baustein, so only above-normal needs require a separate 200-3 analysis. Published with cross-reference tables, an XML version, checklists and an ISO-to-IT-Grundschutz mapping table |
| Umsetzungshinweise | Companion implementation guidance per Baustein — the "how", kept out of the requirement text |
| WiBA | "Weg in die Basis-Absicherung": checklists that let small institutions implement basics without running an ISMS |

### C5

Seventeen areas, each with an identifier used throughout reports: OIS (organisation of information security), SP (policies and procedures), HR (personnel), AM (asset management), PS (physical security), OPS (operations), IAM (identity and access management; IDM in C5:2020), CRY (cryptography and key management), COS (communication security), PI (portability and interoperability), DEV (procurement, development and modification), SSO (control and monitoring of service providers and suppliers), SIM (security incident management), BCM (business continuity), COM (compliance), INQ (dealing with government investigation requests), PSS (product safety and security).

- **Basic vs additional criteria.** Basic criteria are BSI's stated minimum level and define the minimum audit scope; additional criteria serve customers with higher protection needs. C5:2026 splits additional **sub-criteria** into *sharpen* (replace the corresponding basic sub-criterion with a stricter requirement) and *complement* (add a requirement that must also be audited). The applicable criteria are named in the report.
- **Criteria are auditable statements only** — C5 never prescribes the measure by which a criterion is met.
- **General conditions of the service** — a separate reporting section (C5:2026 section 4, criteria GC-01 to GC-06, outside the 168) on applicable law and jurisdiction, countries, regions and locations, availability and incident handling, recovery parameters, handling of government investigation requests and existing certifications. Often the most decision-relevant pages for a customer.
- **C5:2026 content drivers**: EUCS level Substantial (via the CEN/CENELEC Technical Specification derived from C5:2020), CSA Cloud Controls Matrix v4, ISO/IEC 27001:2022 and NIS2; new material on container management, supply chain, post-quantum cryptography, confidential computing, tenant separation and technical sovereignty. First C5 release published machine-readable as YAML alongside PDF and Excel.

### BSIG duties (binding)

| § | Duty |
|---|---|
| 30(1)–(2) | Appropriate, proportionate and effective technical and organisational measures on an all-hazards basis, state of the art; **10 minimum topics** (risk-analysis and IT-security policies; incident handling; business continuity incl. backup, disaster recovery and crisis management; supply-chain security; security in acquisition, development and maintenance incl. vulnerability handling and disclosure; effectiveness assessment; basic training and awareness; cryptography policy; personnel security, access control and asset management; MFA or continuous authentication and secured voice/video/text and emergency communication). **Compliance must be documented** (§ 30(1) sentence 3) |
| 30(3)–(5) | Commission implementing acts under NIS2 Art. 21(5) take precedence for digital-infrastructure and digital-provider entity types; BMI may specify the rest by ordinance |
| 31 | Operators of critical installations: measures may go beyond the general level where proportionate, and **attack detection systems** are mandatory — continuous, automatic capture and evaluation of operating parameters |
| 32 | 24 h / 72 h / interim on request / 1 month final; a **progress report** replaces the final report if the incident is still running, with the final report due after completion |
| 33 | Register with BSI within **3 months** of first/again qualifying; notify changes within **2 weeks**; BSI may register a non-compliant entity itself |
| 38 | Management must **implement and supervise** the § 30 measures, is liable to its own entity under applicable company law, and must **attend training regularly** |
| 39 | Operators of critical installations prove implementation by audits, tests or certifications **every 3 years** (first no earlier than 3 years after qualifying), submitting results including identified deficiencies; BSI may demand a remediation plan and proof of remediation |

## Assessment, certification and evidence

| Route | Mechanics |
|---|---|
| ISO 27001 on the basis of IT-Grundschutz | Available for Standard- and Kern-Absicherung. A **BSI-certified ISO 27001 Grundschutz auditor** reviews the reference documents, performs an on-site audit and writes an audit report; the report goes to BSI, which decides on issuing the certificate. Scope may be an *Informationsverbund* or a component such as a data centre. Certificate validity period not verified here |
| Testat nach Basis-Absicherung | Lighter attestation of Basis-Absicherung, issuable **only** by a BSI-certified auditor |
| Person certification | IT-Grundschutz-Praktiker → IT-Grundschutz-Berater; separate certification as audit team leader for ISO 27001 audits on the basis of IT-Grundschutz |
| C5 attestation | Engagement under **ISAE 3000 (Revised)**, the German IDW PS 860 or another national equivalent; ISAE 3402 and IDW PS 951 n.F. are named only as supplementary standards for service-organisation reporting questions. **Type 1** = design and implementation at a point in time; **Type 2** = plus operating effectiveness over a period, typically 6 or 12 months. BSI's position: type 2 is required for meaningful assurance; type 1 should be used only for a first audit and never repeatedly. Either an audit of the provider's own statement or a direct engagement |
| C5 report contents | Auditor's report with opinion; management statement (omitted in a direct engagement); description of the service-related internal control system; the applicable criteria with provider controls, test procedures and results; optional other information (not covered by the opinion) |
| Customer-side use | BSI expects customers to obtain and analyse the report annually, implement the complementary customer controls, and carry the residual risk themselves — BSI does not review reports. An evaluation guideline and report-summary template are published for C5:2020 |
| BSIG evidence | § 39 three-year cycle for critical installations; § 61 lets BSI order audits of individual besonders wichtige Einrichtungen at any time and, from **three years after entry into force** (i.e. from 6 December 2028), demand evidence from others — five years for hospitals admitted under § 108 SGB V |

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| 2016 | First C5 published |
| January 2020 | C5:2020 final; BSI recommended it for audit periods ending on or after 15 February 2021 |
| 1 February 2023 | IT-Grundschutz-Kompendium Edition 2023 replaces Edition 2022 — still the current edition |
| 1 July 2025 | § 393 SGB V: C5 **type 2** attestation required for cloud processing of social/health data |
| 2 December 2025 | BSIG enacted as Art. 1 of the NIS2 implementation act (BGBl. 2025 I Nr. 301) |
| 6 December 2025 | BSIG in force |
| 6 March 2026 | End of the § 33 three-month registration window for entities already in scope on 6 December 2025; BSI's NIS-2 page now states the statutory registration deadline has passed. Registration runs through the BSI portal with an ELSTER organisation certificate (§ 33(6)) |
| 11 / 17 March 2026 | KRITIS-Dachgesetz enacted / in force (BGBl. 2026 I Nr. 66); its § 14(3)–(5) enter into force 1 January 2030 |
| 7 April 2026 | C5:2026 v1.0.0 published (PDF, editable, YAML, changelog) after a public community draft |
| 15 May 2026 | BSI-Kritisverordnung of 22 April 2016 amended again (BGBl. 2026 I Nr. 148) — it remains the operative threshold ordinance |
| 21 July 2026 | Act of 21 July 2026 (BGBl. 2026 I Nr. 221) amends both BSIG and KRITIS-DachG; recorded on the consolidated texts but not yet fully documented there |
| 23 July 2026 | Most recent BSIG amendment recorded on the official consolidated text (BGBl. 2026 I Nr. 226) |
| **Pending** | The ordinance under §§ 4(3) and 5(1) KRITIS-DachG that sets critical-installation thresholds. Until it is in force, BSIG § 2 nos. 22 and 24 and § 33(2), (5) apply in their earlier wording (§ 66), so the **BSI-Kritisverordnung** (22 April 2016, last amended 15 May 2026; sector thresholds derived from a reference value of 500,000 supplied persons) still determines who operates a critical installation, and KRITIS-DachG § 8(8) has BBK fix the registration procedure within four weeks of that ordinance |
| After registration | KRITIS-DachG § 8(7): § 12 risk-analysis duties bite nine months, and §§ 13, 18 and 20 ten months, after a critical installation is registered |
| **Pending** | C5:2026 cross-reference table to international standards "scheduled for publication in the near future" |
| 1 June 2027 | C5:2026 becomes the applicable revision for new engagements |
| Multi-year | IT-Grundschutz JSON rule set replaces the Kompendium; no commencement date published |

## Key obligations for security/GRC teams

1. **Settle BSIG tier and carve-outs first** — Annex 1/2 entity type, headcount and financial thresholds, and whether DORA, EnWG §§ 5c–5e or the telematics carve-out displaces §§ 30–39. See [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md) and [../regulations/nis2.md](../regulations/nis2.md).
2. **Register within 3 months and keep the record current within 2 weeks** of any change (§ 33) — the registration data, not the controls, is the first enforceable deadline, and for entities already in scope on 6 December 2025 that window closed on 6 March 2026.
3. **Wire the 24 h / 72 h / 1 month chain into incident response** against the joint BSI/BBK reporting point, with a progress-report branch for incidents still running at the one-month mark. See [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
4. **Document § 30 compliance as a deliverable, not a by-product** — § 30(1) sentence 3 makes the documentation itself the obligation, and § 65(2) no. 3 makes failing to document a separate fineable offence.
5. **Map the 10 § 30(2) topics onto the existing control set** (ISO/IEC 27001:2022 Annex A, or IT-Grundschutz Bausteine if you are already on that methodology) before building anything new. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md), [control-mapping](../../skills/control-mapping/SKILL.md) and [iso-27001-2022.md](iso-27001-2022.md).
6. **Critical-installation operators: stand up attack detection (§ 31(2)) and plan the three-year § 39 evidence cycle**, including auditor selection and the remediation-plan path for findings. See [audit-preparation](../../skills/audit-preparation/SKILL.md).
7. **Put management training and oversight on the record** (§ 38) — attendance logs, board minutes showing supervision of the § 30 measures, and a documented liability position. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).
8. **Cloud buyers: request the C5 report, not the logo.** Read the framework-conditions section (sub-service providers, data-centre locations, government investigation requests), confirm type 2 rather than repeat type 1, and implement the complementary customer controls named in the report. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
9. **Cloud providers: plan the C5:2020 → C5:2026 migration now.** Engagements from 1 June 2027 use C5:2026; for periods ending on or after 28 February 2027 the system description must disclose planned control changes (criterion ID, nature, implementation status and date), which the auditor checks for fair presentation but does not yet evaluate.
10. **Health-sector cloud: verify the § 393 SGB V chain** — current type 2 C5 attestation covering the basic criteria for the systems and technology actually used, plus evidence that the complementary customer criteria are implemented. Neighbouring EU health-data rules are covered in [../regulations/eu-ehds.md](../regulations/eu-ehds.md).

## Interplay

- **NIS2 and the CER Directive.** BSIG is the German NIS2 transposition; the KRITIS-Dachgesetz is the physical-resilience counterpart, carrying risk analysis (§ 12), resilience duties and a resilience plan (§ 13), evidence (§ 16), incident reporting (§ 18), management duties (§ 20) and its own fines (§ 24). Critical-installation *registration* moves to KRITIS-DachG § 8, with BBK as recipient — but BSIG § 66 defers § 33(2) until the § 4(3)/§ 5(1) ordinance is in force, so the BSIG wording in force until 16 March 2026 still governs meanwhile. See [../regulations/nis2.md](../regulations/nis2.md), [../regulations/eu-nis2-implementing-and-transposition.md](../regulations/eu-nis2-implementing-and-transposition.md) and [../regulations/eu-cer-directive.md](../regulations/eu-cer-directive.md).
- **DORA.** Financial entities in scope of Regulation (EU) 2022/2554 are carved out of the BSIG risk-management, reporting, training and evidence sections — but not of the rest of the Act. See [../regulations/dora.md](../regulations/dora.md).
- **GDPR.** BSIG § 65(11) bars a second fine for conduct already fined by a data protection authority under GDPR Art. 58(2)(i). The reporting clocks still run in parallel to Art. 33. See [../regulations/gdpr.md](../regulations/gdpr.md).
- **EU Cybersecurity Act / EUCS.** C5:2020 fed the draft EUCS level Substantial via CEN/CENELEC, and C5:2026 was built back from it — the clearest national-to-EU convergence path in cloud assurance. BSIG § 30(6) also lets an ordinance make European certification schemes mandatory for named ICT products, services and processes. See [../regulations/eu-cybersecurity-act.md](../regulations/eu-cybersecurity-act.md).
- **ISO/IEC 27001.** IT-Grundschutz is an alternative *route* to the same certificate, not a competing scheme; the certificate issued is an ISO 27001 certificate. Where an organisation already runs a generic ISMS, the Kompendium is usually better used as a control library than as a migration target. See [iso-27001-2022.md](iso-27001-2022.md).
- **C5 vs SOC 2 vs CSA STAR vs FedRAMP.** C5 is the closest European analogue to SOC 2: same assurance plumbing (ISAE 3000 / type 1 vs type 2), different criteria set and a mandatory disclosure section for data location and government access. Providers commonly hold C5, SOC 2 and CSA STAR in parallel and reuse one control set. See [soc2-tsc.md](soc2-tsc.md), [csa-ccm-star.md](csa-ccm-star.md), [iso-27017-27018-cloud.md](iso-27017-27018-cloud.md) and [fedramp.md](fedramp.md).
- **BCM.** BSI-Standard 200-4 and BSIG § 30(2) no. 3 overlap heavily with ISO 22301 — one BCMS can serve all three. See [iso-22301-business-continuity.md](iso-22301-business-continuity.md) and [risk-assessment](../../skills/risk-assessment/SKILL.md).
- **BSI TR-03161** sets security requirements for health applications and is a separate technical guideline, not part of IT-Grundschutz or C5 (contents not examined here).

## Primary sources

- BSI-Gesetz (BSIG) of 2 December 2025, consolidated official text — https://www.gesetze-im-internet.de/bsig_2025/ (legal text; fetched, including §§ 28, 30, 31, 32, 33, 38, 39, 61, 65, 66)
- BSI-Kritisverordnung of 22 April 2016, consolidated official text — https://www.gesetze-im-internet.de/bsi-kritisv/ (legal text; fetched — still the operative critical-installation threshold ordinance)
- KRITIS-Dachgesetz of 11 March 2026, consolidated official text — https://www.gesetze-im-internet.de/kritisdachg/ (legal text; fetched, including §§ 8, 12, 13, 16, 18, 20, 24)
- § 393 SGB V (cloud use in healthcare) — https://www.gesetze-im-internet.de/sgb_5/__393.html (legal text; fetched)
- BSI, C5 criteria catalogue overview — https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html (publisher page; fetched)
- BSI, C5 introduction (ISAE 3000 methodology, type 1 vs type 2, report structure, federal minimum standard) — https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/C5_Einfuehrung/C5_Einfuehrung_node.html (publisher page; fetched)
- BSI, C5:2026 version page — https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/C5_2025/C5_2025_node.html (publisher page; fetched)
- BSI, C5:2020 version page — https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/C5_AktuelleVersion/C5_AktuelleVersion_node.html (publisher page; fetched)
- BSI, *Cloud Computing Compliance Criteria Catalogue (C5:2026)*, v1.0.1 — https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/CloudComputing/ComplianceControlsCatalogue/2026/C5_2026.pdf (publisher document; fetched — areas table, §§ 2.2, 3.2, 3.5, section 4; 168 criteria counted)
- BSI, *Cloud Computing Compliance Criteria Catalogue (C5:2020)* — https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/CloudComputing/ComplianceControlsCatalogue/2020/C5_2020.pdf (publisher document; fetched — 121 criteria counted, audit standards section)
- BSI, IT-Grundschutz hub incl. "Fortentwicklung des IT-Grundschutz" — https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html (publisher page; fetched)
- BSI, BSI-Standards 200-1 to 200-4 — https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/bsi-standards_node.html (publisher page; fetched)
- BSI, *BSI-Standard 200-4 Business Continuity Management*, Version 1.0 (May 2023) — https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_4.pdf (publisher document; fetched — change history)
- BSI, IT-Grundschutz-Kompendium Edition 2023 — https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html (publisher page; fetched)
- BSI, certified information security (Testat, person certification, certification scope) — https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/zertifizierte-informationssicherheit_node.html (publisher page; fetched)
- BSI, ISO 27001 certification on the basis of IT-Grundschutz — https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Zertifizierung-und-Anerkennung/Zertifizierung-von-Managementsystemen/ISO-27001-Basis-IT-Grundschutz/iso-27001-basis-it-grundschutz_node.html (publisher page; fetched)
- BSI, NIS-2-regulated companies (registration route, deadline status) — https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-regulierte-Unternehmen/nis-2-regulierte-unternehmen_node.html (regulator page; fetched)
- BSI, branchenspezifische Sicherheitsstandards (B3S) — https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/Kritische-Infrastrukturen/Branchenspezifische-Sicherheitsstandards-B3S/branchenspezifische-sicherheitsstandards-b3s_node.html (publisher page; fetched)
- BSI, TR-03161 (requirements for health applications) — https://www.bsi.bund.de/dok/TR-03161 (publisher page; fetched, contents not examined)
- Not verified against a fetched source: the certificate validity period for ISO 27001 on the basis of IT-Grundschutz, the number of Bausteine in Kompendium Edition 2023, and the basic/additional split of the 168 C5:2026 criteria.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
