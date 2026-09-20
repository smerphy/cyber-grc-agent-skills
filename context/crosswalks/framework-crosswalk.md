# Framework Crosswalk (Domain Level)

A navigation aid mapping ~15 common security domains across six frameworks: ISO/IEC 27001:2022 Annex A (control numbering per ISO/IEC 27002:2022), NIST CSF 2.0, CIS Controls v8/v8.1, SOC 2 Trust Services Criteria (2017, revised 2022 points of focus), NIST SP 800-53 Rev. 5 control families, and PCI DSS v4.0.1 requirements.

## How to use this crosswalk — read first

- **Domain granularity only.** Cells point to the control *area* most relevant to each domain, not clause-by-clause equivalence. Two frameworks landing in the same row does NOT mean their controls are interchangeable or that satisfying one satisfies the other.
- **Not compliance evidence.** Never present this table to an auditor or regulator as a mapping deliverable. For defensible mappings, use official sources: the CIS Controls Mappings (published by CIS for ISO 27001, CSF, PCI DSS, and others), [NIST's OLIR / Informative References program](../frameworks/nist-csf-profiles-and-companion-resources.md) (available via NIST's Cybersecurity and Privacy Reference Tool), AICPA's SOC 2 mapping publications, and the PCI SSC's own mapping documents. Then validate against your actual control implementations — see [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).
- **Frameworks slice domains differently.** ISO puts secure development under "Technological" controls; CIS has no physical security control; SOC 2 merges logical and physical access into CC6; PCI scopes everything to the cardholder data environment. Expect one-to-many and many-to-one relationships in every row.
- **Abbreviated identifiers.** ISO cells cite Annex A controls (e.g., A.5.15). CSF cells cite categories (e.g., PR.AA) or specific subcategories where a domain maps narrowly. CIS cells cite control numbers 1–18. SOC 2 cells cite common criteria series (CC1–CC9) and category criteria (A, C, PI, P). 800-53 cells cite two-letter families. PCI cells cite requirements 1–12.

Framework detail lives in the per-framework context files — link there rather than restating:
[ISO 27001:2022](../frameworks/iso-27001-2022.md) · [NIST CSF 2.0](../frameworks/nist-csf-2.md) · [CIS v8](../frameworks/cis-controls-v8.md) · [SOC 2 TSC](../frameworks/soc2-tsc.md) · [NIST 800-53](../frameworks/nist-800-53.md) · [PCI DSS v4](../frameworks/pci-dss-4.md)

## Table 1 — ISO 27001 Annex A · NIST CSF 2.0 · CIS Controls v8

| Domain | ISO 27001:2022 Annex A | NIST CSF 2.0 | CIS v8 |
|---|---|---|---|
| Governance & risk management | A.5.1–A.5.8 (+ ISMS clauses 4–10) | GV (all categories), ID.RA, ID.IM | No dedicated control; policy/process expectations embedded per safeguard (v8.1 adds governance emphasis) |
| Asset management | A.5.9–A.5.11 (+ A.5.12–A.5.13 classification) | ID.AM | 1 (enterprise assets), 2 (software) |
| Access control & identity | A.5.15–A.5.18, A.8.2–A.8.5, A.8.18 | PR.AA | 5 (accounts), 6 (access) |
| Cryptography & data protection | A.8.24; A.5.12–A.5.14, A.8.10–A.8.12 | PR.DS | 3 (data protection) |
| Physical & environmental | A.7.1–A.7.14 | PR.AA-06 (physical access); PR.IR (partial) | Not covered |
| Operations security (config, change, malware) | A.8.1, A.8.6–A.8.7, A.8.9, A.8.19, A.8.32, A.5.37 | PR.PS | 4 (secure config), 9 (email/browser), 10 (malware) |
| Network security | A.8.20–A.8.23 | PR.IR-01 (+ PR.DS-02 in transit) | 12 (network infrastructure), 13 (network monitoring/defense) |
| Secure development | A.8.25–A.8.31, A.8.33 | PR.PS-06 | 16 (application software security) |
| Supplier / third-party management | A.5.19–A.5.23 | GV.SC | 15 (service provider management) |
| Incident management | A.5.24–A.5.28, A.6.8 | DE.AE, RS (all), RC (partial) | 17 (incident response management) |
| Continuity & resilience | A.5.29–A.5.30, A.8.13–A.8.14 | RC.RP, RC.CO, PR.IR-03/-04 | 11 (data recovery) |
| Compliance, audit & assurance | A.5.31–A.5.36, A.8.34 | GV.OC-03, GV.OV | No dedicated control |
| HR / people security & awareness | A.6.1–A.6.7 | PR.AT, GV.RR-04 | 14 (awareness & skills training) |
| Logging & monitoring | A.8.15–A.8.17 | DE.CM, DE.AE | 8 (audit logs), 13 (network monitoring) |
| Vulnerability & threat management | A.8.8, A.5.7 (threat intel) | ID.RA-01 (+ ID.RA generally) | 7 (vulnerability management), 18 (penetration testing) |

## Table 2 — SOC 2 TSC · NIST 800-53 r5 · PCI DSS v4

| Domain | SOC 2 TSC | 800-53 r5 families | PCI DSS v4 |
|---|---|---|---|
| Governance & risk management | CC1, CC2, CC3, CC5 | PM, PL, RA, CA | Req 12 |
| Asset management | CC6.1 (partial); no dedicated criterion | CM (CM-8), MP, PM-5 | Req 12.5 (scope/asset inventory), Req 9 (media) |
| Access control & identity | CC6.1–CC6.3 | AC, IA | Req 7, 8 |
| Cryptography & data protection | CC6.1, C-series (confidentiality) | SC (SC-12/13/28), MP | Req 3, 4 |
| Physical & environmental | CC6.4–CC6.5 | PE | Req 9 |
| Operations security (config, change, malware) | CC6.8, CC7.1, CC8.1 | CM, SI (SI-3), MA | Req 2, 5, 6.5 (change control) |
| Network security | CC6.6–CC6.7 | SC (SC-7), AC-4 | Req 1, 4 |
| Secure development | CC8.1 | SA, SI (input validation etc.), CM | Req 6 |
| Supplier / third-party management | CC9.2 | SR, SA-9 | Req 12.8–12.9 (TPSPs) |
| Incident management | CC7.3–CC7.5 | IR | Req 12.10 |
| Continuity & resilience | A1.1–A1.3 (availability), CC9.1 | CP | Not directly addressed |
| Compliance, audit & assurance | CC4.1–CC4.2 | CA, AU (records), PM | Req 12 (12.1 policy, 12.4 compliance program) |
| HR / people security & awareness | CC1.4–CC1.5 | PS, AT | Req 12.6 (awareness), 12.7 (screening) |
| Logging & monitoring | CC7.2 (+ CC7.1) | AU, SI-4 | Req 10 |
| Vulnerability & threat management | CC7.1 | RA (RA-5), SI-2 | Req 6.3 (patching), Req 11 (scans/pen tests) |

## Domain notes and known friction points

- **Governance.** CSF 2.0 elevated governance to its own function (GV) — the strongest governance articulation of the six. ISO covers it partly in Annex A (A.5.1–A.5.8) but mostly in the management-system clauses 4–10, which Annex A crosswalks miss. CIS v8 and PCI treat governance thinly (PCI concentrates it in Requirement 12). When assessing governance maturity, do not rely on a CIS- or PCI-anchored control set alone.
- **Asset management.** SOC 2 has no dedicated inventory criterion; auditors typically test inventories under CC6.1's identification of protected information assets. PCI v4 made scope/asset inventory explicit (12.5.1).
- **Access control.** The cleanest row in the crosswalk — every framework has a substantial, testable access domain. Fine-grained differences remain large (e.g., PCI Req 8 MFA specifics vs. ISO A.8.5's outcome-level "secure authentication").
- **Physical security.** CIS v8 deliberately excludes it. If CIS is your primary framework, source physical controls from ISO A.7 or 800-53 PE.
- **Continuity.** SOC 2 covers it only if Availability is in scope; PCI barely addresses it (incident response plan aside). ISO 27001 covers ICT readiness (A.5.30) but full BCM lives in [ISO 22301](../frameworks/iso-22301-business-continuity.md).
- **Logging vs. monitoring vs. detection.** Frameworks split these differently: CIS separates log management (8) from network defense (13); CSF splits continuous monitoring (DE.CM) from event analysis (DE.AE); PCI folds both into Req 10 plus testing in Req 11. Map at safeguard level before claiming coverage.
- **Vulnerability management.** ISO has a single control (A.8.8); PCI is the most prescriptive (defined scan cadence, ASV scans, pen testing under Req 11). A "compliant" ISO program can be far weaker than a compliant PCI one in this domain — granularity differs by an order of magnitude.

## Extended tables — further control frameworks

The same ~15 domain rows, applied to the control catalogues and national schemes that arrived in the library after Tables 1 and 2 were written. Everything in the preamble still applies: domain granularity only, no equivalence claim, not compliance evidence. Two further cautions specific to these tables:

- **These frameworks are less alike than the first six.** Some are control catalogues (800-171, CCM, HITRUST, ISM, C5), some are outcome frameworks scored by judgement (CAF, 62443 maturity levels), some are a fixed pass/fail baseline (Cyber Essentials), and some are an attestation regime wrapped around a short control list (SWIFT CSCF, TISAX). A row that lines up on paper can be a maturity score in one column and a binary requirement in another.
- **Empty cells are real.** Where a framework does not address a domain, the cell says so. Do not substitute a plausible-looking neighbour control — a deliberate exclusion (Cyber Essentials has no governance requirement; 800-171 has no availability family) is itself the finding.

### Table 3 — NIST SP 800-171 Rev. 3 / CMMC · CSA CCM v4.1 · HITRUST CSF

[SP 800-171 / CMMC](../frameworks/nist-800-171-cmmc.md) · [CSA CCM / CAIQ / STAR](../frameworks/csa-ccm-star.md) · [HITRUST CSF](../frameworks/hitrust-csf.md)

800-171 cells cite Rev. 3 requirement families (§ 3.1–3.17). CCM cells cite the 17 v4.1 domain codes. HITRUST cells cite the 14 CSF control categories (0–13) by number and title — finer placement (which of the 156 control specifications) must be read off the current MyCSF assessment object.

| Domain | 800-171 Rev. 3 family | CSA CCM v4.1 domain | HITRUST CSF category |
|---|---|---|---|
| Governance & risk management | 3.11 Risk Assessment, 3.15 Planning | GRC | 0 Information Security Management Program, 3 Risk Management, 4 Security Policy, 5 Organization of Information Security |
| Asset management | 3.4 Configuration Management (component inventory), 3.8 Media Protection | No stand-alone domain; nearest are DCS and UEM | 7 Asset Management |
| Access control & identity | 3.1 Access Control, 3.5 Identification and Authentication | IAM | 1 Access Control |
| Cryptography & data protection | 3.13 System and Communications Protection, 3.8 Media Protection | CEK, DSP | No titled category — read under 9 and 10; 13 Privacy Practices for PII |
| Physical & environmental | 3.10 Physical Protection | DCS | 8 Physical and Environmental Security |
| Operations security (config, change, malware) | 3.4 Configuration Management, 3.7 Maintenance, 3.14 System and Information Integrity | CCC, IVS, UEM | 9 Communications and Operations Management |
| Network security | 3.13 System and Communications Protection | IVS | No titled category — read under 9 Communications and Operations Management |
| Secure development | 3.16 System and Services Acquisition (new in Rev. 3) | AIS | 10 Information Systems Acquisition, Development, and Maintenance |
| Supplier / third-party management | 3.17 Supply Chain Risk Management (new in Rev. 3) | STA | No titled category — service providers are handled by risk factors, e1/i1 carve-outs and inheritance (no carve-out in an r2) |
| Incident management | 3.6 Incident Response | SEF | 11 Information Security Incident Management |
| Continuity & resilience | No contingency family — Rev. 3 addresses confidentiality only; integrity and availability arrive with SP 800-172r3 | BCR | 12 Business Continuity Management |
| Compliance, audit & assurance | 3.12 Security Assessment and Monitoring (SSP under 3.15 Planning) | A&A, GRC | 6 Compliance |
| HR / people security & awareness | 3.9 Personnel Security, 3.2 Awareness and Training | HRS | 2 Human Resources Security |
| Logging & monitoring | 3.3 Audit and Accountability | LOG | No titled category — read under 9 Communications and Operations Management |
| Vulnerability & threat management | 3.11 Risk Assessment, 3.14 System and Information Integrity | TVM | No titled category — read under 9 and 10 |

Reading notes:

- **CMMC does not have its own control set.** Level 1 draws 15 requirements from FAR 52.204-21, Level 2 the 110 requirements of SP 800-171 **Rev. 2**, and Level 3 twenty-four requirements selected from SP 800-172. The Rev. 3 families above are the direction of travel, not the baseline currently assessed — build documentation so both revisions' identifiers resolve.
- **CCM domains not in the row set:** IPY (interoperability and portability) and, in the AI Controls Matrix, MDS (model security). Neither has an equivalent in the other five columns.
- **Every CCM control carries a shared-responsibility (SSRM) designation.** A domain match tells you nothing about *who* owns the control in your service model.
- **HITRUST certification is decided per assessment domain, not per control category** — the scoring unit and the structural unit above are different things.

### Table 4 — IEC 62443 · UK Cyber Assessment Framework v4.0 · Cyber Essentials v3.3

[IEC 62443 / SP 800-82r3](../frameworks/iec-62443-ot-security.md) · [UK CAF and Cyber Essentials](../frameworks/uk-cyber-essentials-ncsc-caf.md)

62443 cells cite the eight asset-owner security programme elements (SPEs) of IEC 62443-2-1:2024 and, where a technical requirement is meant, the seven foundational requirements (FR 1–7). CAF cells cite v4.0 principles and contributing outcomes. Cyber Essentials cells cite the five technical controls.

| Domain | IEC 62443 (asset owner) | UK CAF v4.0 | Cyber Essentials v3.3 |
|---|---|---|---|
| Governance & risk management | SPE 1 ORG 1 security related organization and policies; risk assessment method in 62443-3-2 (zones, conduits, SL-T) | A1 Governance; A2 Risk Management (A2.a process, A2.b Understanding Threat, A2.c Assurance) | Not covered — the scheme is deliberately narrow and carries no governance, risk-management or incident-response requirement |
| Asset management | SPE 2 CM 1 inventory management of IACS hardware and software components | A3 Asset Management (A3.a) | Not a control theme; scoping and the assessed evidence expect asset and cloud service inventories |
| Access control & identity | SPE 6 USER 1 identification and authentication, USER 2 authorization and access control; FR 1 IAC, FR 2 UC | B2 Identity and Access Control (B2.a–d) | 4 User access control — least access, account removal, separate admin accounts, MFA wherever available and always for cloud services |
| Cryptography & data protection | SPE 5 DATA 1 classification, confidentiality, retention, cryptography; FR 4 DC | B3 Data security (B3.a–e) | Not covered |
| Physical & environmental | SPE 1 ORG 3 security of physical access | No dedicated principle at v4.0 | Not covered |
| Operations security (config, change, malware) | SPE 4 COMP 1 components and portable media, COMP 2 malware protection, COMP 3 patch management; SPE 2 CM 1 baselines and change control | B4 System security (B4.a–d) | 2 Secure configuration; 5 Malware protection |
| Network security | SPE 3 NET 1 system segmentation, NET 2 secure wireless access, NET 3 secure remote access; FR 5 RDF | B5 Resilient networks and systems | 1 Firewalls |
| Secure development | Not an asset-owner element — it sits with the product supplier in 62443-4-1 (secure product development lifecycle) | A4.b Secure Software Development and Support (new in v4.0) | Not a control theme; v3.3 introduces the Software Security Code of Practice in its software development section |
| Supplier / third-party management | 62443-2-4 security programme requirements for service providers; 4-1/4-2 conformance used as a procurement lever | A4 Supply Chain (A4.a, A4.b) | Not covered — Cyber Essentials is normally *imposed* on suppliers (PPN 014) rather than covering them |
| Incident management | SPE 7 EVENT 1 event and incident management; FR 6 TRE | D1 Response and recovery planning (D1.a–c); D2 Lessons learned (D2.a–b) | Not covered |
| Continuity & resilience | SPE 8 AVAIL 1 system availability and intended functionality, AVAIL 2 backup/restore/archive; FR 7 RA | B5 Resilient networks and systems; D1 Response and recovery planning | Not covered |
| Compliance, audit & assurance | SPE 1 ORG 2 security assessments and reviews; process maturity ML 1–4; certification through ISASecure / IECEE rather than the standard itself | A2.c Assurance — but the yardstick is the regulator-set CAF profile, and CAF carries no certification | The scheme is the assurance: verified self-assessment, board-signed, annual; CE Plus adds independent technical testing |
| HR / people security & awareness | No dedicated SPE — edition 2.0 removed duplication with the ISMS it sits alongside | B6 Staff awareness and training (B6.a–b) | Not covered |
| Logging & monitoring | SPE 7 EVENT 1; FR 6 TRE | C1 Security monitoring (C1.a–f, incl. C1.f Understanding User's and System's Behaviour) | Not covered |
| Vulnerability & threat management | SPE 4 COMP 3 patch management; IEC TR 62443-2-3 patch management in the IACS environment | A2.b Understanding Threat; C2 Threat Hunting (C2.a); B4 System security | 3 Security update management — updates within 14 days where the vendor rates the issue critical or high risk, or CVSS v3 base score is 7.0 or above |

Reading notes:

- **62443 requirements are addressed to roles, not organizations** (asset owner, service provider, product supplier). One company often holds several, and the column above is the asset-owner view only. A zone or conduit is rated as a seven-element SL vector, so "SL 3" in one FR says nothing about the other six.
- **CAF is not scored like a control framework.** Each of the 41 contributing outcomes is judged achieved / partially achieved / not achieved against its Indicators of Good Practice, and only the outcomes in the applicable profile count. Confirm the CAF version and profile with the oversight body before scoping.
- **Cyber Essentials is a pass/fail snapshot at certificate issue**, not a maturity picture. From April 2026 the MFA-for-cloud question and the two 14-day update questions are auto-fail regardless of other answers, so a CE certificate is a strong signal on three specific things and silent on most of this table.
- **OT priority ordering differs.** NIST SP 800-82r3 states that IT programmes prioritise confidentiality, integrity and availability in that order, while OT prioritises safety, then availability, integrity and confidentiality. Rows below "network security" in an IT-anchored table are frequently the highest-priority ones in a plant.

### Table 5 — Australian Essential Eight / ISM · BSI C5:2026 · FedRAMP CR26

[Essential Eight and ISM](../frameworks/australia-essential-eight-ism.md) · [BSI IT-Grundschutz and C5](../frameworks/germany-bsi-it-grundschutz-c5.md) · [FedRAMP](../frameworks/fedramp.md)

Australian cells name the ISM guideline chapter or section and, where one applies, the Essential Eight mitigation strategy. C5 cells cite the 17 subject-area identifiers used throughout a C5 report. FedRAMP cells cite the 10 Key Security Indicator families of the 20x certification type; the Rev5 route instead uses per-class lists drawn from SP 800-53 Rev. 5 (at least 155 controls for Class B, 322 for Class C, 409 for Class D), so read those rows off Table 2's 800-53 column.

| Domain | Australia — ISM chapter / Essential Eight | BSI C5:2026 area | FedRAMP CR26 (20x) |
|---|---|---|---|
| Governance & risk management | ISM *Cyber security roles*, *Cyber security documentation*, *Security assurance* | OIS organisation of information security; SP policies and procedures | KSI-PIY Policy and Inventory (executive support, security investment); the Security Decision Record |
| Asset management | ISM *IT equipment*, *Media* | AM asset management | KSI-PIY (inventories) |
| Access control & identity | ISM *System access*; E8 restrict administrative privileges, multi-factor authentication | IAM identity and access management | KSI-IAM Identity and Access Management |
| Cryptography & data protection | ISM *Cryptography*, *Media*, *Data transfers* | CRY cryptography and key management; INQ for government investigation requests | KSI-SVC Service Configuration (secret management, securing information); the Cryptographic Module Use ruleset, mandatory for Class D |
| Physical & environmental | ISM *Physical security* | PS physical security | No KSI family — 20x is written for cloud-native services and assumes the datacentre layer is inherited; the Rev5 route carries 800-53 PE |
| Operations security (config, change, malware) | ISM *System hardening*, *System management*; E8 application control, Microsoft Office macro settings, user application hardening | OPS operations | KSI-SVC Service Configuration; KSI-CMT Change Management |
| Network security | ISM *Networking*, *Gateways*, *Communications infrastructure*, *Communications systems* | COS communication security | KSI-CNA Cloud Native Architecture (logical networking, restricted traffic, minimised attack surface) |
| Secure development | ISM *Software development* | DEV procurement, development and modification | KSI-PIY (security in the SDLC); KSI-CMT |
| Supplier / third-party management | ISM *Procurement and outsourcing*; IRAP assessment at least every 24 months for managed service and cloud providers serving government | SSO control and monitoring of service providers and suppliers | KSI-SCR Supply Chain Risk |
| Incident management | ISM *Cyber security incidents* | SIM security incident management | KSI-INR Incident Response, plus the CR26 incident ruleset and its PAIN-rated reporting clocks |
| Continuity & resilience | ISM *Data backup and restoration*; E8 regular backups | BCM business continuity | KSI-RPL Recovery Planning |
| Compliance, audit & assurance | ISM *Security assurance*; assessment inside the six-step risk management framework, ending in an authorisation to operate — no certificate | COM compliance; the deliverable is an ISAE 3000 (Revised) / IDW PS 860 attestation, not a BSI certificate | FedRAMP Recognized independent assessment at least once a year for Classes B/C/D; Ongoing Certification |
| HR / people security & awareness | ISM *Personnel security* | HR personnel | KSI-CED Cybersecurity Education (a single KSI) |
| Logging & monitoring | ISM centralised event logging and event log monitoring (pulled into Essential Eight maturity levels 2 and 3) | No separately titled area — audited under OPS | KSI-MLA Monitoring, Logging and Auditing |
| Vulnerability & threat management | ISM *System maintenance* (mitigating known vulnerabilities, cessation of support), *Security assessments* (vulnerability scanning); E8 patch applications, patch operating systems | No separately titled area — audited under OPS | No KSI family; covered by the CR26 vulnerability detection/response and vulnerability evaluation/reporting rulesets, plus KSI-PIY vulnerability disclosure |

Reading notes:

- **The Essential Eight is a subset, not a framework.** Eight mitigation strategies at maturity levels 1–3 map onto 46 / 87 / 123 ISM controls out of 1,143. Most rows above are ISM-only; a board that reports "Essential Eight maturity" has reported on roughly a tenth of the catalogue.
- **IT-Grundschutz is not in the table** because it is a methodology plus a modelled Baustein catalogue rather than a flat control list: BSI-Standard 200-1 (ISMS), 200-2 (Basis-, Kern-, Standard-Absicherung), 200-3 (risk) and 200-4 (BCMS), with the IT-Grundschutz-Kompendium supplying the requirements. Use it as a route *to* ISO/IEC 27001 rather than as a column beside it, and note that BSI is rebuilding it into a machine-readable rule set.
- **C5 areas with no row here:** PI (portability and interoperability) and PSS (product safety and security). C5 also reports *general conditions of the service* (GC-01 to GC-06 — jurisdiction, locations, recovery parameters, government access requests) outside the 168 criteria; those pages are often the most decision-relevant in the report.
- **FedRAMP Certification Classes A–D replaced the Low / Moderate / High labels** and describe the assurance information a provider commits to supply, not how secure the service is. Agencies still categorise their own system under FIPS 199/200 first.

### Table 6 — SWIFT CSCF v2026 · TISAX (VDA ISA 6.0.3)

[SWIFT CSP and CSCF](../frameworks/swift-customer-security-programme.md) · [VDA ISA and TISAX](../frameworks/tisax-vda-isa.md)

Both are supply-chain attestation schemes rather than certifications: SWIFT produces an annual KYC-SA self-attestation supported by an independent assessment, TISAX produces labels held in the ENX portal. SWIFT cells cite CSCF control numbers (a trailing **A** marks an advisory control); ISA cells cite catalogue chapters.

| Domain | SWIFT CSCF v2026 | VDA ISA 6.0.3 / TISAX |
|---|---|---|
| Governance & risk management | 7.4A Scenario-based Risk Assessment; the Customer Security Controls Policy and attestation cycle | 1 IS Policies and Organization (policies, organisation, IS risk management) |
| Asset management | Not a control — the scope is fixed by the user's architecture type (A1–A4, B), not by an inventory requirement | Named in the Information Security catalogue's coverage but not a titled chapter — read under 1–7 |
| Access control & identity | 1.2 OS Privileged Account Control; 4.1 Password Policy; 4.2 Multi-Factor Authentication; 5.1 Logical Access Control; 5.2 Token Management; 5.4 Password Repository Protection | 4 Identity and Access Management |
| Cryptography & data protection | 2.1 Internal Data Flow Security; 2.4 Back Office Data Flow Security; 2.5A External Transmission Data Protection; 2.6 Operator Session Confidentiality and Integrity | Cryptography named in the catalogue's coverage; 9 Data Protection for personal data (GDPR Art. 28 processor duties, Art. 9 special categories) |
| Physical & environmental | 3.1 Physical Security | 3 Physical Security; chapter 8 Prototype Protection adds perimeter and building security, sight protection, intrusion monitoring and visitor management |
| Operations security (config, change, malware) | 1.3 Virtualisation or Cloud Platform Protection; 2.2 Security Updates; 2.3 System Hardening; 2.10 Application Hardening; 6.1 Malware Protection; 6.2 Software Integrity; 6.3 Database Integrity | 5 IT Security/Cyber Security (operations security named in coverage) |
| Network security | 1.1 Swift Environment Protection (the secure zone); 1.4 Restriction of Internet Access; 1.5 Customer Environment Protection; 6.5A Intrusion Detection | 5 IT Security/Cyber Security |
| Secure development | Not addressed — the CSCF governs the user's local Swift infrastructure, not software the user builds | No titled chapter |
| Supplier / third-party management | 2.8 Outsourced Critical Activity Protection, with separate Outsourcing Agent Requirements; connecting through a non-compliant service provider is itself a listed breach condition | 6 Supplier Relationships; subcontractor requirements in chapter 8 for prototype work |
| Incident management | 7.1 Cyber Incident Response Planning | Incident and crisis management named in the catalogue's coverage; 9.6 Requests and incidents on the data-protection side |
| Continuity & resilience | Not addressed as a titled control | No titled chapter — availability is carried by the *High availability* and *Very high availability* assessment objectives |
| Compliance, audit & assurance | Annual self-attestation in KYC-SA, supported by an independent assessment under the Independent Assessment Framework; status is visible to counterparties | 7 Compliance; target maturity level 3 on every question, with more than 10% below the maximum a minor and more than 30% a major non-conformity |
| HR / people security & awareness | 5.3A Staff Screening Process; 7.2 Security Training and Awareness | 2 Human Resources; 9.7 Human Resources on the data-protection side |
| Logging & monitoring | 6.4 Logging and Monitoring | No titled chapter — read under 5 IT Security/Cyber Security |
| Vulnerability & threat management | 2.7 Vulnerability Scanning; 7.3A Penetration Testing; 2.9 Transaction Business Controls and 2.11A RMA Business Controls add transaction-level anomaly detection | No titled chapter — read under 5 IT Security/Cyber Security |

Reading notes:

- **Applicability is conditional in both.** Which CSCF controls apply, and whether they are mandatory, depends on the user's architecture type; the v2026 treatment of customer client connectors can reclassify a type B user into an A type. In TISAX, requirement tiers (must / should / high protection needs / very high protection needs) are selected by the assessment objectives the customer demands.
- **TISAX scope is locations, not the legal entity**, and unlike ISO/IEC 27001 the assessment scope may be smaller than the ISMS scope so long as it sits inside it. All locations in one scope share one result — and one failure point.
- **Neither produces a certificate.** A SWIFT attestation and a TISAX label are both shared through a controlled exchange; treat a counterparty's status as dated, scoped evidence, and ask for the underlying assessment.

## Management-system and governance standards

These are not control catalogues and do not belong in the tables above. Putting them in a control-coverage column produces double counting — they govern *how the organization decides*, not *what technical control is implemented*. Reach for them when the question is about the management system, the risk method, or the assurance function.

| Standard | What it governs | Reach for it when |
|---|---|---|
| [ISO 31000:2018 / ISO/IEC 27005:2022](../frameworks/iso-31000-27005-risk-management.md) | Risk management principles, framework and process; information security risk management guidance. Both are **guidance, not requirements** — no "shall" clauses, no certification | You need a defensible risk method and vocabulary. The auditable risk requirements live in ISO/IEC 27001 clauses 6.1.2, 6.1.3, 8.2 and 8.3, not here |
| [ISO 22301:2019](../frameworks/iso-22301-business-continuity.md) | A certifiable business continuity management system; the discipline-specific requirements sit almost entirely in Clause 8 | Continuity is in scope beyond the ICT-readiness controls of ISO 27001 A.5.30 — see the continuity row in Table 1 |
| [ISO/IEC 27701:2025](../frameworks/iso-27701-privacy-management.md) | A certifiable privacy information management system, redrafted in the 2025 edition as a stand-alone standard with Annex A controls for PII controllers and processors | You need auditable privacy accountability evidence. It is **not** an approved GDPR Art. 42 certification mechanism |
| [ISO/IEC 42001:2023](../frameworks/iso-42001-ai-management.md) | A certifiable AI management system; distinguished by the AI system impact assessment and a Statement of Applicability over Annex A | You need an auditable wrapper around AI governance. It supports but does not satisfy EU AI Act Art. 17 |
| [COBIT 2019](../frameworks/cobit-2019.md) | Enterprise governance of information and technology — 5 domains, 40 governance and management objectives, tailored through 11 design factors and the goals cascade | The question is IT governance, decision rights or capability, not security controls. COBIT is explicitly an umbrella that references other standards |
| [COSO ICIF 2013 / ERM 2017](../frameworks/coso-internal-control-erm.md) | Internal control (5 components, 17 principles) and enterprise risk management (5 components, 20 principles); no organizational certification | You are working on ICFR, SOX s404 scoping, or need the conceptual backbone underneath the SOC 2 common criteria |
| [IIA Global Internal Audit Standards (2024)](../frameworks/iia-global-internal-audit-standards.md) | The internal audit function itself — 5 domains, 15 principles, 52 standards, plus the mandatory Cybersecurity Topical Requirement (17 requirements across governance, risk management and controls) | You are building or assessing an internal audit function, not an enterprise control set |
| [FAIR (Open FAIR O-RT 3.1 / O-RA 2.1)](../frameworks/fair-cyber-risk-quantification.md) | Probabilistic quantification of loss exposure in currency; not a control catalogue and not a maturity model | You need to size a named scenario, prioritise control spend, or price an audit finding. Catalogues say what good looks like; FAIR says which gap matters most |
| [NIST RMF (SP 800-37 Rev. 2, 800-39, 800-30 Rev. 1)](../frameworks/nist-rmf-800-37-800-30.md) | The seven-step federal process — Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor — ending in an authorization decision, not a certificate | You are operating a federal or federal-adjacent system, or want a process wrapper around the SP 800-53 controls of Table 2 |
| [NIST AI RMF 1.0 (AI 100-1)](../frameworks/nist-ai-rmf.md) | Voluntary AI risk management: 4 functions (Govern, Map, Measure, Manage), 19 categories, 72 subcategories, plus the Generative AI Profile (AI 600-1) | You need AI risk substance and profiles. There is no certification; ISO/IEC 42001 is the certifiable counterpart |
| [NIST Privacy Framework 1.0](../frameworks/nist-privacy-framework.md) | Privacy risk management in CSF shape — Core, Profiles and Implementation Tiers (5 Functions, 18 Categories, 100 Subcategories in 1.0) | You want privacy outcomes expressed alongside CSF outcomes. Using it does not establish compliance with any privacy law |

## Where to get defensible mappings

Every table in this file is a navigation aid. When a mapping has to survive scrutiny, start from the publisher's own mapping artifact and then validate against your implemented controls using [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).

- **NIST CPRT, the CSF 2.0 Reference Tool and the OLIR catalog** (IR 8278 Rev. 1, submission conformance per IR 8278A Rev. 1), with SP 1347 as the how-to. Read NIST's own caveat first: references are produced by NIST *and* non-NIST entities, NIST performs only limited conformance testing and **no correctness validation**, and automated mappings must retain identifiers, source context, provenance and review status. See [../frameworks/nist-csf-profiles-and-companion-resources.md](../frameworks/nist-csf-profiles-and-companion-resources.md).
- **CIS Controls Mappings** — one of the richest free mapping sets; directional and lossy, since safeguards are narrower than most ISO controls and broader than most 800-53 enhancements. See [../frameworks/cis-controls-v8.md](../frameworks/cis-controls-v8.md).
- **CSA CCM v4.1 workbook, *Scope Applicability (Mappings)* tab** — each mapped control carries a **no gap / partial gap / full gap** rating plus an addendum column proposing a compensating control. The gap rating is a discipline worth copying into your own crosswalks. Machine-readable bundles (JSON/YAML and OSCAL) ship separately; check the version before wiring them in. See [../frameworks/csa-ccm-star.md](../frameworks/csa-ccm-star.md).
- **HITRUST CSF authoritative sources** — v11.8.0 integrates 75 standards, regulations and frameworks into the requirement statements, which is the mapping. See [../frameworks/hitrust-csf.md](../frameworks/hitrust-csf.md).
- **ASD ISM in OSCAL** — catalog plus profiles per classification and per Essential Eight maturity level, published at `cyber.gov.au/ism/oscal`; the practical ingestion path for GRC tooling. See [../frameworks/australia-essential-eight-ism.md](../frameworks/australia-essential-eight-ism.md).
- **BSI IT-Grundschutz-Kompendium cross-reference tables and its ISO-to-IT-Grundschutz mapping table**, published with the Kompendium. See [../frameworks/germany-bsi-it-grundschutz-c5.md](../frameworks/germany-bsi-it-grundschutz-c5.md).
- **VDA ISA "Reference to other standards" column** — every control question cites ISO/IEC 27001, ISA/IEC 62443 and NIST CSF, with a companion column pointing to BSI-Standard 200-2, the IT-Grundschutz Compendium and NIST SP 800-53 Rev. 5. See [../frameworks/tisax-vda-isa.md](../frameworks/tisax-vda-isa.md).
- **FedRAMP Key Security Indicators**, each published with the related SP 800-53 Rev. 5 controls; the Rev5 route publishes per-class control lists outright. See [../frameworks/fedramp.md](../frameworks/fedramp.md).
- **NIST SP 800-82r3**, which maps its OT risk-management tasks to both the Cybersecurity Framework and IEC 62443 and carries an SP 800-53 OT overlay in Appendix F. See [../frameworks/iec-62443-ot-security.md](../frameworks/iec-62443-ot-security.md).
- **AICPA SOC 2 mapping publications** and **PCI SSC mapping documents**, as named in the preamble. See [../frameworks/soc2-tsc.md](../frameworks/soc2-tsc.md) and [../frameworks/pci-dss-4.md](../frameworks/pci-dss-4.md).
- **Treat AI crosswalks differently.** The AI RMF → ISO/IEC 42001 and → ISO/IEC 23894 crosswalks hosted on NIST's AI Resource Center are largely community-submitted, and NIST states that listing implies no endorsement. See [../frameworks/nist-ai-rmf.md](../frameworks/nist-ai-rmf.md).

Whatever the source, record the reference name **and its version** in the deliverable — Informative References carry their own version strings and the catalog changes underneath you.

## Related

- [../crosswalks/breach-notification-timelines.md](breach-notification-timelines.md) — regulatory deadline matrix
- [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md) — using this crosswalk in a gap assessment
- [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md) — producing defensible control-level mappings
- [../frameworks/nist-csf-profiles-and-companion-resources.md](../frameworks/nist-csf-profiles-and-companion-resources.md) — Profiles, Informative References, CPRT and OLIR
- [../../workflows/certification-readiness.md](../../workflows/certification-readiness.md) — taking one of these frameworks to certification or attestation

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
