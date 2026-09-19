# EU Cybersecurity Act (Regulation (EU) 2019/881, "CSA") and the European cybersecurity certification framework

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Regulation (EU) 2019/881 of 17 April 2019 (OJ L 151, 7.6.2019) — directly applicable; amended by Regulation (EU) 2025/37 (managed security services) |
| Publisher / regulator | European Commission (adopts schemes by implementing act); ENISA (prepares schemes, maintains the certification website); national cybersecurity certification authorities (NCCAs) supervise and enforce; the European Cybersecurity Certification Group (ECCG) coordinates |
| Status and key dates | In force 27 June 2019; Arts. 58, 60, 61, 63, 64, 65 (NCCAs, CABs, notification, complaints, remedies, penalties) applied from 28 June 2021; first scheme (EUCC) applicable 27 February 2025; repeal-and-replace proposal "Cybersecurity Act 2" (COM(2026) 11) tabled 20 January 2026 and under negotiation |
| Who is covered | Title II: ENISA. Title III: anyone who seeks, holds or issues a European cybersecurity certificate or EU statement of conformity for an ICT product, service, process or (since 2025) managed security service; NCCAs; conformity assessment bodies (CABs) |
| Structure | 69 articles in four titles: I subject matter and definitions (Arts. 1–2); II ENISA mandate, tasks, organisation (Arts. 3–45); III European cybersecurity certification framework (Arts. 46–65); IV final provisions (Arts. 66–69); one Annex (CAB requirements) |
| Assurance model | Three assurance levels — basic, substantial, high (Art. 52); conformity self-assessment (EU statement of conformity) only at basic (Art. 53) |
| Voluntary or mandatory? | Certification is voluntary unless Union or Member State law specifies otherwise (Art. 56(2)); NIS2 Art. 24, CRA Arts. 8 and 27, and AI Act Art. 42(2) are the hooks that make it (potentially) mandatory or conformity-relevant |
| Penalties | Member States set "effective, proportionate and dissuasive" penalties for infringements of Title III and of schemes (Art. 65); NCCAs may withdraw certificates and impose penalties under national law (Art. 58(8)) |
| Certifiable? | Yes — that is its purpose. Certificates and EU statements of conformity are recognised in all Member States (Arts. 53(5), 56(10)) |
| Adopted schemes | EUCC (Common Criteria-based, Implementing Regulation (EU) 2024/482, as amended by (EU) 2024/3144). Candidates in preparation: EUCS (cloud), EU5G, EUDI Wallet, EUMSS (managed security services) |

## What it is

The Cybersecurity Act does two things. First, it gives ENISA a permanent mandate (Art. 68(4): established for an indefinite period as of 27 June 2019) as the EU's reference point for cybersecurity advice, operational cooperation (CSIRTs network secretariat, EU-level exercises, situational reports — Art. 7) and market/standardisation support (Art. 8). Second, it creates the **European cybersecurity certification framework** (Title III): a single EU mechanism for adopting cybersecurity certification schemes for ICT products, services and processes, so that one certificate is valid across the internal market instead of a patchwork of national schemes (Art. 46). Its stated purpose (Art. 1) is the functioning of the internal market with a high level of cybersecurity, resilience and trust; it is without prejudice to Member State competences for public security, defence, national security and criminal law (Art. 1(2)).

Schemes are made in a three-step process: the Commission publishes a **Union rolling work programme** (URWP) of strategic priorities (Art. 47, updated at least every three years; first URWP published February 2024 alongside the EUCC), the Commission (or, in justified cases, the ECCG) requests ENISA to prepare a **candidate scheme** (Art. 48), and ENISA drafts it with an ad hoc working group and open consultation, takes the ECCG's opinion, and hands it to the Commission, which adopts it as an **implementing act** (Art. 49). ENISA must evaluate each adopted scheme at least every five years (Art. 49(8)).

Regulation (EU) 2025/37 (adopted 19 December 2024 with the Cyber Solidarity Act, in force 4 February 2025) extended the framework to **managed security services** (incident handling, penetration testing, security audits, consulting related to technical support — new Art. 2 definition) and added Art. 51a security objectives for such services (competence and integrity of staff, internal quality procedures, protection of customer data). It also tightened transparency of scheme preparation (ENISA must report on stakeholder consultation when transmitting a candidate scheme; Parliament and Council may invite the Commission and ENISA to discuss schemes).

## Who it covers / Scope

- **Manufacturers and providers** that choose (or are required by other law) to certify an ICT product, ICT service, ICT process or managed security service, or that issue an EU statement of conformity. Definitions (Art. 2): ICT product = element or group of elements of a network or information system; ICT service = service consisting fully or mainly in transmission, storing, retrieving or processing of information by such systems; ICT process = activities to design, develop, deliver or maintain an ICT product or service. NIS2 and the CRA import these definitions by reference.
- **Certificate holders** carry continuing duties: supplementary cybersecurity information (Art. 55), vulnerability reporting to the issuer (Art. 56(8)), scheme-specific monitoring and record-keeping.
- **Conformity assessment bodies**: must be accredited by the national accreditation body under Regulation (EC) No 765/2008 against the CSA Annex, for a maximum of five years renewable (Art. 60), and notified to the Commission per scheme (Art. 61); schemes may add authorisation requirements (Art. 54(1)(f), Art. 60(3)).
- **NCCAs**: at least one per Member State, independent of the entities it supervises, with issuing activities strictly separated from supervision (Art. 58(1)–(4)); subject to peer review (Art. 59).
- **Assurance level "high"** certificates may only be issued by an NCCA, or by a CAB with per-certificate prior approval or a general delegation from the NCCA (Art. 56(6)); a scheme may reserve issuance to public bodies (Art. 56(5)).
- **Territorial reach**: the framework is EU-internal-market law, but non-EU vendors selling into the EU use it in the same way; third-country recognition is via mutual recognition agreements foreseen in each scheme (Art. 54(1)(t); EUCC Art. 44).
- **Not covered**: the CSA itself imposes no security obligations on operators or users; obligations to *use* certified products come from other acts (NIS2 Art. 24, CRA Art. 8) or national law.

## Core obligations

### Framework rules (Title III)

| Article | Requirement |
|---|---|
| Art. 51 | Ten minimum security objectives every scheme must pursue: confidentiality and integrity/availability of data across the life cycle; access limited to authorised persons/programs; documented dependencies and vulnerabilities; logging and auditability of access; no known vulnerabilities; timely restoration after incidents; secure by default and by design; up-to-date software/hardware with secure update mechanisms |
| Art. 52 | Assurance levels commensurate with risk of intended use. **Basic**: minimise known basic risks; at least a technical documentation review. **Substantial**: minimise known risks and attacks by actors with limited skills/resources; review for absence of publicly known vulnerabilities plus testing of security functionality. **High**: minimise risk of state-of-the-art attacks by actors with significant skills/resources; adds resistance assessment via penetration testing. Schemes may define evaluation levels under each assurance level |
| Art. 53 | Conformity self-assessment (EU statement of conformity) only for low-risk items at basic; manufacturer assumes responsibility, keeps technical documentation available to the NCCA for the scheme-defined period, and files a copy with the NCCA and ENISA |
| Art. 54 | 22 mandatory scheme elements (a)–(v): scope, standards/technical specifications, assurance levels, self-assessment permitted or not, CAB requirements, evaluation methods, marks/labels, compliance monitoring, certificate maintenance/renewal, consequences of non-compliance, vulnerability handling rules, record retention, related national/international schemes, certificate content and format, maximum validity, disclosure policy, third-country mutual recognition, peer assessment for "high" issuers, supplementary-information procedures. Art. 54(3): a certificate may give presumption of conformity with another Union act where that act so provides |
| Art. 55 | Holder must publish, in electronic form and until the certificate expires: secure configuration/installation/operation guidance; the security-support period (availability of updates); contact details and accepted channels for vulnerability reports; links to public vulnerability repositories and advisories |
| Art. 56 | Certified items presumed compliant with the scheme (56(1)); certification voluntary unless law says otherwise (56(2)); Commission must assess by 31 December 2023 and at least every two years thereafter whether a scheme should be made mandatory (56(3)); holder must inform the issuer of subsequently detected vulnerabilities or irregularities affecting compliance (56(8)); validity and renewal per scheme (56(9)) |
| Art. 57 | National schemes covering the same items cease to have effect from the date fixed in the scheme's implementing act; no new national schemes for items already covered; existing national certificates remain valid until expiry |
| Art. 58(7)–(8) | NCCA tasks: supervise compliance monitoring, enforce self-assessment obligations, assist accreditation bodies, authorise/suspend CABs, handle complaints, report annually to ENISA and the ECCG. Powers: request information, audit CABs/holders/issuers, access premises, withdraw certificates, impose penalties, order immediate cessation of infringements |
| Arts. 63–64 | Right to complain to the issuer (or NCCA for CAB-issued "high" certificates) and to an effective judicial remedy in the courts of the Member State where the authority or body sits |

### The EUCC scheme (Implementing Regulation (EU) 2024/482)

| Topic | Rule |
|---|---|
| Scope and standards | ICT products (hardware, software, components) and protection profiles, evaluated under Common Criteria (ISO/IEC 15408) and the Common Evaluation Methodology (ISO/IEC 18045) (Arts. 1, 3). Builds on the SOG-IS MRA |
| Assurance levels | Only substantial and high (Art. 4): substantial = AVA_VAN 1–2; high = AVA_VAN 3–5. No self-assessment (Art. 6). Technical domains in Annex I (e.g., smart cards and similar devices) carry mandatory state-of-the-art documents |
| Issuance | Certification body (CB) issues on an ITSEF evaluation; the applicant signs commitments (correct information, no promotion before issuance, promote only within scope, cease on suspension/withdrawal, product identical to what was certified, mark/label rules) (Art. 9). "High" CBs need NCCA authorisation and cooperate with an authorised ITSEF (Art. 21) |
| Validity and review | Maximum five years unless the NCCA approves longer (Art. 12); review may confirm, withdraw, or withdraw-and-reissue (Art. 13); suspension up to 42 days, extendable by the NCCA to at most one year, with purchasers and the public informed (Art. 30) |
| Monitoring | NCCA samples annually at least 4 % of EUCC certificates on a risk basis (Art. 25(3)); CB monitors holders; holders monitor vulnerability information on the product and its dependencies (Art. 27) |
| Vulnerability management | Holder maintains procedures (EN ISO/IEC 30111 where needed), publishes intake channels, records and impact-analyses every potential vulnerability, informs holders of dependent composite-product certificates, proposes remediation to the CB, which triggers a certificate review (Arts. 33–36). NCCA shares information with other NCCAs and ENISA (Arts. 37–38). On withdrawal, remediated public vulnerabilities go to the European vulnerability database or the Art. 55 repositories (Art. 39) |
| Records | CBs/ITSEFs and holders retain records (and a specimen of the product) for at least five years after withdrawal (Arts. 40–41) |
| Peer assessment | CBs issuing at "high" undergo peer assessment at least every five years (Art. 45) |
| Standard versions | Implementing Regulation (EU) 2024/3144 (in force 8 January 2025) fixed CC:2022 / ISO/IEC 15408:2022 and CEM:2022 as the applicable versions, with CC 3.1 rev. 5 accepted for certificates until 31 December 2027 |
| Transition | Applicable from 27 February 2025; national CC schemes for covered products ceased 12 months after entry into force (27 February 2025), with processes started under them to finish within 24 months (27 February 2026) (Arts. 49–50) |

## Enforcement and penalties

- **Decentralised**: NCCAs enforce Title III and the schemes (Art. 58); penalties are national (Art. 65) — there is no EU-level fine in the CSA. Sanctions in practice are certificate suspension/withdrawal, CAB authorisation withdrawal, corrective orders, and national penalties.
- **Market-surveillance hooks**: where a CSA certificate gives presumption of conformity under another act (e.g., the CRA), the NCCA must inform that act's market surveillance authority of suspensions (EUCC Art. 30(4)); CRA market surveillance authorities cooperate with NCCAs (CRA Art. 52(4)).
- **Accreditation lever**: national accreditation bodies must restrict, suspend or revoke a CAB's accreditation where conditions are no longer met (Art. 60(4)).
- **Complaints and remedies**: any natural or legal person may complain about a certificate to the issuer/NCCA and seek judicial review (Arts. 63–64).
- **Proposed CSA2 (not yet law)**: keeps national penalties for the certification title, but its new supply-chain Title IV would carry EU-set ceilings of 1 %, 2 % or 7 % of total worldwide annual turnover depending on the obligation breached (proposal Art. 115).

## Timeline and status

| Date | Event |
|---|---|
| 27 June 2019 | CSA in force; Regulation (EU) No 526/2013 repealed; ENISA re-established for an indefinite period |
| 28 June 2021 | Arts. 58, 60, 61, 63, 64, 65 apply (NCCAs, CABs, notification, complaints, remedies, penalties) |
| 3 February 2021 | Commission requests ENISA to prepare an EU5G candidate scheme (outside the URWP, Art. 48(2)); still listed by ENISA as "under development" — no candidate scheme adopted as of September 2026 |
| 7 February 2024 | EUCC published (Implementing Regulation (EU) 2024/482); in force 27 February 2024; first URWP published |
| 19 December 2024 | Regulation (EU) 2025/37 adopted (managed security services); in force 4 February 2025 |
| 8 January 2025 | Implementing Regulation (EU) 2024/3144 amending the EUCC (standard versions, transition to CC:2022, accreditation state-of-the-art documents) |
| 27 February 2025 | EUCC applicable; first certificates issued April 2025 (ANSSI); ENISA registry lists 105 valid EUCC certificates from eight certification bodies under five NCCAs (FR, DE, ES, SE, NL) as of 18 September 2026 |
| 20 January 2026 | Commission proposes the **Cybersecurity Act 2** (COM(2026) 11, 2026/0011(COD)) to repeal and replace 2019/881, with a companion directive amending NIS2 (2026/0012(COD)). Content: recast ENISA mandate (early alerts, EU Cybersecurity Reserve operation, single reporting platform, vulnerability services, skills attestation schemes, Board of Appeal); recast certification framework with a 12-month deadline for ENISA candidate schemes, a European Cybersecurity Certification Assembly, scheme maintenance/review mechanism, scope extended to "cyber posture of entities", assurance levels retained; new **trusted ICT supply chain framework** allowing the Commission to designate third countries of concern and high-risk suppliers, identify key ICT assets in NIS2 sectors, impose mitigation measures, and require phase-out of high-risk components from mobile networks within at most 36 months of entry into force |
| 3 April 2026 | ENISA public consultation on the draft candidate EUDI Wallet scheme (closed 30 April 2026) |
| 22 May 2026 | Council Presidency progress report on CSA2; Member States seeking clarity on supply-chain methodology, scope and governance. Parliament work at an early stage; adoption not expected before late 2026/2027 (secondary sources) |
| 24 July 2026 | ENISA public consultation on the draft candidate EUMSS scheme (incident response profile first; basic/substantial/high), closing 13 September 2026; EU Cybersecurity Reserve providers must be EUMSS-certified within two years of the scheme being in place |
| EUCS (cloud) | Candidate scheme drafted since 2020 (basic/substantial/high; three-year certificates; C5/SecNumCloud/ISO 27001 lineage). Not adopted as of September 2026 — blocked by the dispute over sovereignty requirements; NCCAs describe it as "waiting for final adoption" |
| 31 December 2027 | End of EUCC transition for CC 3.1 rev. 5-based certificates |
| United Kingdom | Regulation 2019/881 revoked in UK law from 20 January 2021 (S.I. 2019/1444); no UK equivalent framework |

## Key obligations for security/GRC teams

1. **Decide whether certification is voluntary or effectively required for you**: check NIS2 Art. 24 national measures, CRA Art. 8 delegated acts for critical products, AI Act Art. 42(2), public-procurement specifications, and sectoral law before assuming "voluntary". See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Procurement teams**: ask for the certificate identifier, scheme, assurance level and AVA_VAN level, and verify it in the ENISA registry; treat national CC certificates as valid until expiry (Art. 57(3)) but expect renewals under EUCC. Fold this into vendor due diligence — [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
3. **Vendors/holders**: stand up the Art. 55 supplementary-information page (secure-configuration guidance, support period, vulnerability intake, advisory links) before issuance and keep it current for the certificate's life.
4. **Vendors/holders**: build the EUCC vulnerability-management loop (intake, impact analysis against the target of evaluation, remediation proposal, CB review, notification of dependent-certificate holders) and align it with CRA Art. 14 reporting so one process feeds both. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
5. **Retention**: keep certification records and a product specimen for five years after withdrawal (EUCC Art. 41) — put this in the records schedule. See [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).
6. **Control mapping**: map the Art. 51 security objectives and EUCC assurance components onto the ISO 27001 / NIST CSF control set so certification evidence is reusable — [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md), [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
7. **Cloud and MSSP buyers**: track EUCS and EUMSS; contract clauses that require "EU certification when available" should name the scheme and assurance level and allow a transition period. Watch the CSA2 supply-chain title for high-risk-supplier phase-outs in NIS2 sectors. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).
8. **Board reporting**: report certification coverage of critical products, expiry dates, suspensions, and exposure to prospective high-risk-supplier restrictions — [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **NIS2**: NIS2 borrows the CSA definitions of cybersecurity, cyber threat, ICT product/service/process. Art. 24 lets Member States require essential and important entities to use CSA-certified products/services to demonstrate Art. 21 compliance, and empowers the Commission to mandate this by delegated act; where no scheme exists, the Commission may request one under CSA Art. 48(2). Managed security service providers are NIS2 entities themselves, which is why the CSA was extended to their services. See [nis2.md](nis2.md).
- **Cyber Resilience Act**: CRA Art. 27(8) gives products certified (or self-declared) under a CSA scheme a presumption of conformity with the CRA essential requirements to the extent covered; a certificate at least at "substantial" removes the CRA third-party assessment obligation for the corresponding requirements (Art. 27(9)). CRA Art. 8 lets the Commission require Annex IV critical products to obtain a CSA certificate at least at "substantial". ENISA published a CRA–EUCC interplay study on 27 February 2025. CABs notified under the CSA must be separately notified under the CRA.
- **EU AI Act**: high-risk AI systems certified under a CSA scheme whose references are published in the Official Journal are presumed to meet the Art. 15 cybersecurity requirement to the extent covered (Art. 42(2)). See [eu-ai-act.md](eu-ai-act.md).
- **Cyber Solidarity Act (Regulation (EU) 2025/38)**: the EU Cybersecurity Reserve draws on "trusted" managed security service providers; EUMSS certification is the intended selection signal.
- **DORA**: no direct link, but CSA certificates are usable evidence in DORA ICT third-party due diligence; DORA does not mandate them. See [dora.md](dora.md).
- **eIDAS 2 / EUDI Wallet**: wallet certification runs under Regulation (EU) 2024/1183; the CSA candidate EUDI Wallet scheme is designed to serve it. Member States are to provide at least one certified wallet by end-2026.
- **ISO/IEC 15408 and the CCRA**: EUCC is Common Criteria; CCRA participants recognise EUCC certificates issued by public CBs that are CCRA authorising participants, while private-CB certificates need NCCA per-certificate oversight for CCRA recognition — full mutual recognition is still pending. See [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) for the management-system side of the ISO ecosystem.

## Primary sources

- Regulation (EU) 2019/881 (Cybersecurity Act), consolidated official text via the Publications Office (CELEX 32019R0881) — legal text.
- Regulation (EU) 2025/37 amending Regulation (EU) 2019/881 as regards managed security services (CELEX 32025R0037) — legal text.
- Regulation (EU) 2025/38 (Cyber Solidarity Act) (CELEX 32025R0038) — legal text, for the EU Cybersecurity Reserve link.
- Commission Implementing Regulation (EU) 2024/482 (EUCC) (CELEX 32024R0482) and amending Implementing Regulation (EU) 2024/3144 (CELEX 32024R3144) — legal text.
- Regulation (EU) 2024/2847 (CRA), Directive (EU) 2022/2555 (NIS2), Regulation (EU) 2024/1689 (AI Act) — legal texts, for the cross-references cited above.
- Proposal COM(2026) 11 final, Cybersecurity Act 2 (Council document ST 5611/2026 INIT, data.consilium.europa.eu) and Council progress report ST 9399/2026 of 22 May 2026 — legislative documents.
- European Commission, "EU Cybersecurity Certification Framework" policy page (digital-strategy.ec.europa.eu) — regulator guidance (EUCC product scope, URWP priorities, CSA2 announcement).
- ENISA certification website (certification.enisa.europa.eu): EUCC topic page and FAQ, "EUCC in Application" news (27 February 2025), certificate registry, CAB finder, 2026 European Cybersecurity Certification Conference page — regulator guidance.
- ENISA news: EU5G request (3 February 2021), EUDI Wallet consultation (3 April 2026), EUMSS consultation (24 July 2026); ENISA EUCS publication page (December 2020 draft) — regulator guidance.
- Dutch NCCA (dutchncca.nl) EUCS page — regulator guidance on EUCS status and assurance levels.
- legislation.gov.uk/eur/2019/881 — UK revocation status.
- Secondary (for CSA2 legislative status and first-year EUCC statistics only): Jones Day (July 2026), Inside Privacy (January 2026), eucrim, CRA Evidence blog on the April 2026 ENISA conference. ENISA's own topic page for EUCS returned access denied and was not used.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
