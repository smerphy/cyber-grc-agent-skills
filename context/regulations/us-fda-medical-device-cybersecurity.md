# US FDA Medical Device Cybersecurity — FD&C Act §524B (21 U.S.C. 360n-2) and FDA premarket/postmarket guidance

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Federal Food, Drug, and Cosmetic Act §524B "Ensuring Cybersecurity of Devices", codified at 21 U.S.C. 360n-2; added by §3305 of the Consolidated Appropriations Act, 2023 (Pub. L. 117-328, div. FF, title III — often cited as FDORA), signed 29 December 2022 |
| Effective | 29 March 2023 (90 days after enactment). Submissions filed before that date are not subject to §524B(a)–(b) |
| Regulator | FDA — Center for Devices and Radiological Health (CDRH) and, for device-biologics, CBER; enforcement via premarket review, Refuse-to-Accept decisions, inspections and the prohibited-acts machinery of 21 U.S.C. 331/333 |
| Who is covered | Any person submitting a 510(k), PMA (incl. supplements), PDP, De Novo or HDE for a **cyber device** (software + ability to connect to the internet + characteristics vulnerable to cyber threats) |
| Statutory duties | (1) postmarket vulnerability plan incl. coordinated vulnerability disclosure; (2) processes/procedures for reasonable assurance of cybersecurity plus patches on a regular cycle and out-of-cycle for critical vulnerabilities; (3) SBOM; (4) any further requirements FDA sets by regulation |
| Guidance layer | Premarket: "Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions" (issued 3 February 2026 as a Level 2 revision under 21 CFR 10.115(g)(4), superseding the 27 June 2025 final; docket FDA-2021-D-1158). Postmarket: "Postmarket Management of Cybersecurity in Medical Devices" (December 2016) |
| Quality system hook | 21 CFR Part 820 Quality Management System Regulation (QMSR), effective 2 February 2026, incorporates ISO 13485:2016 by reference; cybersecurity is treated as part of design controls and risk management |
| Penalties | Failure to comply with §524B(b)(2) is a prohibited act (21 U.S.C. 331(q)(3)); device civil penalties under 21 U.S.C. 333(f)(1)(A) — statutory $15,000 per violation / $1,000,000 per proceeding, currently $35,466 / $2,364,503 under the inflation table at 45 CFR 102.3; plus non-acceptance, NSE/not-approvable decisions, recalls and injunctions |
| Certifiable? | No. Compliance is demonstrated through submission content, QMS records and FDA inspection; standards cited in FDA guidance (IEC 81001-5-1, ANSI/ISA 62443-4-1, ANSI/AAMI SW96) are evidence, not certification |
| Neighbours | HIPAA (health data at the provider); HHS 405(d) HICP (provider-side practices); EU MDR/IVDR Annex I via MDCG 2019-16; IMDRF cybersecurity principles |

## What it is

Before 2023, FDA regulated medical device cybersecurity purely through its general safety-and-effectiveness authority and non-binding guidance (the 2014 premarket guidance and the 2016 postmarket guidance). Section 3305 of the Consolidated Appropriations Act, 2023 changed that by inserting §524B into the FD&C Act: for the first time, sponsors of connected, software-bearing devices have **express statutory** obligations to document a postmarket vulnerability plan, build and maintain cybersecurity processes with defined patching behaviour, and supply a software bill of materials as a condition of premarket submission. Congress also directed FDA to update its premarket cybersecurity guidance within two years (§3305(e)) and to refresh public cybersecurity resources at least annually (§3305(f)), and preserved FDA's pre-existing authority to demand reasonable assurance of cybersecurity for any device, including those cleared or approved before 29 December 2022 (§3305(c)).

The regime is two-tier. The statute is short; the operational detail lives in FDA guidance, which is non-binding but sets the review expectations that determine whether a submission is accepted. The premarket guidance has been revised repeatedly since §524B (final September 2023, draft "select updates" March 2024, final June 2025, and a February 2026 Level 2 re-issue aligning it with the new QMSR). The 2016 postmarket guidance remains the reference for controlled/uncontrolled risk, routine patching and remediation clocks.

## Who it covers / Scope

| Test | Detail (statute and February 2026 guidance §VII) |
|---|---|
| Submission types triggering §524B | 510(k) (original, special, abbreviated), PMA and PMA supplements, Product Development Protocol, De Novo, HDE and HDE supplements (§524B(a); guidance §VII.A). IDE, BLA and IND submissions are outside §524B but inside the guidance's documentation recommendations (Appendix 3 covers IDEs) |
| "Cyber device" (§524B(c)) | All three prongs: (1) includes software validated, installed or authorized by the sponsor as or in a device — FDA reads this to include firmware and programmable logic; (2) has the ability to connect to the internet; (3) contains technological characteristics that could be vulnerable to cybersecurity threats |
| "Ability to connect to the internet" | Read broadly: any device that *can* connect, intentionally or not, through any means — network/server/cloud connections, RF (Wi-Fi, cellular, Bluetooth/BLE), magnetic inductive links, and hardware connectors such as USB, ethernet or serial ports (a device serviced briefly via USB qualifies) |
| Timing | Applies to submissions made on or after 29 March 2023; earlier authorisations are untouched until a modification requires a new submission, at which point §524B applies to that submission (§3305(d) of Pub. L. 117-328; guidance §VII.D) |
| Modifications | A submission for a device change must meet §524B. FDA distinguishes changes that may affect cybersecurity (authentication/encryption changes, new connectivity, changed update mechanism — full documentation) from changes unlikely to (materials, sterilisation, algorithm change without architectural change — reference the prior plan, state whether any critical vulnerabilities with uncontrolled risk exist or were remediated, provide the SBOM) |
| Exemptions | FDA may exempt devices or categories by Federal Register notice (§524B(d)); no such list has been published in the Federal Register as of September 2026 |
| Broader guidance scope | The premarket guidance applies to every device with cybersecurity considerations (software, firmware, programmable logic — not only networked devices), including 510(k)-exempt devices and the device constituent of combination products |
| Who is *not* directly regulated | Healthcare delivery organisations, third-party servicers and refurbishers (QMSR final rule declined to extend Part 820 to them). Their duties come from HIPAA, contracts and HHS 405(d) practices |

## Core obligations

### Statutory requirements for cyber devices (§524B(b))

| Provision | Requirement | FDA expectation (February 2026 guidance §VII.C) |
|---|---|---|
| §524B(b)(1) | Submit a plan to monitor, identify and address, in a reasonable time, postmarket cybersecurity vulnerabilities and exploits, including coordinated vulnerability disclosure (CVD) and related procedures | Use the Cybersecurity Management Plan content (§VI.B): responsible personnel; vulnerability sources and monitoring frequency (NVD, researchers, third-party suppliers); handling of CISA Known Exploited Vulnerabilities; periodic security testing; patch development timeline; update process and patching capability (rate of delivery); CVD process; customer communication. CVD covers externally and internally found vulnerabilities and the procedures for disclosing them |
| §524B(b)(2)(A) | Make available updates and patches for **known unacceptable vulnerabilities** on a **reasonably justified regular cycle** | Cycle length is risk-based and must be justified in the plan (an interconnected thermometer vs a surgical robot); covers controlled-risk vulnerabilities and supportability updates |
| §524B(b)(2)(B) | Make available, **as soon as possible out of cycle**, patches for **critical vulnerabilities that could cause uncontrolled risks** | Mapped to the 2016 postmarket guidance's uncontrolled-risk remediation expectations (see below) |
| §524B(b)(2) | Design, develop and maintain processes and procedures for reasonable assurance that the device **and related systems** are cybersecure | "Related systems" include other devices, "other function" software, software/firmware update servers and connections to facility networks. Evidence = the SPDF documentation set in Appendix 4. Non-compliance with (b)(2) is itself a prohibited act |
| §524B(b)(3) | Provide an SBOM covering commercial, open-source and off-the-shelf components | Machine-readable, consistent with the NTIA October 2021 minimum elements, plus for each component its support level (actively maintained / no longer maintained / abandoned) and end-of-support date; list known vulnerabilities incl. CISA KEV with a safety-and-security risk assessment; justify any gaps |
| §524B(b)(4) | Comply with further requirements FDA sets by regulation | No such regulation published as of September 2026 |

### Secure Product Development Framework (SPDF) — premarket guidance §§IV–VI

| Element | What FDA expects in the submission |
|---|---|
| QMS integration | Cybersecurity is part of device safety and of the QMSR; ISO 13485:2016 clause 7.3 design and development (required for class II, class III and listed class I devices under 21 CFR 820.10(c)) is the hook. FDA encourages an SPDF; JSP2, IEC 81001-5-1 and ANSI/ISA 62443-4-1 are named as acceptable frameworks |
| Security objectives | Authenticity (incl. integrity), authorization, availability, confidentiality, secure and timely updatability and patchability — applied across the architecture, explicitly including AI-containing and cloud-based devices |
| Security risk management | Separate from but traceable to ISO 14971 safety risk management (AAMI TIR57, ANSI/AAMI SW96 cited); threat modeling; cybersecurity risk assessment framed around exploitability; interoperability risks; third-party components and SBOM; security assessment of unresolved anomalies; TPLC risk management with traceability between threat model, risk assessment, SBOM and testing |
| Security architecture | Control categories (Appendix 1): authentication, authorization, cryptography, code/data/execution integrity, confidentiality, event detection and logging, resiliency and recovery, firmware and software updates. Architecture views: Global System, Multi-Patient Harm, Updatability/Patchability, Security Use Case(s) |
| Cybersecurity testing | Security requirements testing; threat-mitigation testing against the threat model; vulnerability testing per ANSI/ISA 62443-4-1 (abuse/misuse cases, robustness, fuzzing, attack-surface analysis, vulnerability chaining, closed-box scanning, software composition analysis of binaries, static and dynamic analysis incl. hard-coded/default credentials); penetration testing with a report stating tester independence and expertise, scope, duration, methods and findings |
| Transparency / labeling | Recommended cybersecurity controls for the use environment; network ports and interfaces; infrastructure requirements; SBOM made available to users continuously in machine-readable form; secure update procedures; security-event notification and logging; backup/restore; secure shipped configuration; forensic log details for IDS/SIEM; end-of-support and end-of-life information; secure decommissioning. MDS2 and JSP2 customer security documentation can address much of this |
| Documentation scaling | Cybersecurity documentation scales with cybersecurity risk, **independently** of the software Documentation Level in the premarket software guidance; Appendix 4 tabulates the recommended package (risk management report, threat model, risk assessment, SBOM, architecture views, testing, labeling, management plan) and which parts are recommended for IDEs |

### Postmarket management (December 2016 guidance) and reporting clocks

| Topic | Rule |
|---|---|
| Controlled vs uncontrolled risk | Assessed from exploitability of the vulnerability and severity of patient harm. Controlled = acceptable residual risk; uncontrolled = unacceptable residual risk due to insufficient mitigations |
| Routine updates and patches | Changes addressing only controlled-risk vulnerabilities are device enhancements, not repairs; **not** reportable as corrections under 21 CFR Part 806. PMA holders report them in the annual report (21 CFR 814.84) |
| Uncontrolled risk | Must be reported under 21 CFR Part 806 (unless reported under Parts 803/1004). FDA does not intend to enforce Part 806 reporting where **all** of: no known serious adverse events or deaths; within **30 days** of learning of the vulnerability the manufacturer notifies customers, identifies interim compensating controls and documents a remediation plan; within **60 days** it fixes, validates and distributes the fix; and it is an **active ISAO participant** (member; ISAO has documented policies; manufacturer shares vulnerability information; documented process for acting on ISAO intelligence, traceable to risk assessments) |
| 21 CFR 806.10 | Reports of corrections or removals initiated to reduce a risk to health are due within **10 working days** of initiation; non-reportable corrections must still be recorded (§806.20) |
| 21 CFR Part 803 (MDR) | Manufacturer reports within **30 calendar days** of becoming aware that a device may have caused or contributed to a death or serious injury, or malfunctioned in a way likely to do so if repeated (§803.50); **5 work days** where FDA has requested or remedial action is needed to prevent unreasonable public-health risk (§803.53) |
| Program alignment | FDA recommends structuring the postmarket program on the NIST Cybersecurity Framework functions (Identify, Protect, Detect, Respond, Recover) |

## Enforcement and penalties

- **Premarket gate.** FDA's March 2023 Refuse-to-Accept policy stated it would generally not RTA a cyber-device submission solely for missing §524B content before **1 October 2023**; from that date it may. §524B content (plan, SBOM, process evidence) is therefore a threshold acceptance item, then a substantive review item — the February 2026 guidance describes FDA finding a device not substantially equivalent where cybersecurity deficiencies undermine safety and effectiveness, and treats "reasonable assurance of cybersecurity" as part of the safety-and-effectiveness determination for all five pathways.
- **Prohibited act.** 21 U.S.C. 331(q)(3): failure to comply with any requirement under §524B(b)(2) (processes/procedures and patch availability) is a prohibited act, exposing the manufacturer to the FD&C Act's civil and criminal machinery, seizure and injunction.
- **Civil money penalties.** 21 U.S.C. 333(f)(1)(A): up to $15,000 per device-related violation and $1,000,000 per proceeding by statute; the HHS inflation-adjustment table at 45 CFR 102.3 currently lists **$35,466 per violation and $2,364,503 aggregate** (the 2025 adjustment, published 28 January 2026 and applied to penalties assessed on or after that date).
- **Adulteration/misbranding.** The guidance notes a device with inadequate cybersecurity may be adulterated or misbranded (e.g., FD&C Act §502(j), dangerous to health when used as labelled), and remediation of an uncontrolled risk is a reportable correction or removal under 21 CFR Part 806 unless FDA's enforcement-discretion criteria are met.
- **Inspection.** QMSR inspections now audit design and development, risk management, complaint handling and corrective-action records against ISO 13485:2016 as incorporated — cybersecurity records sit inside those files.
- **Safety communications.** FDA publishes device-specific cybersecurity safety communications (e.g., 30 January 2025 on Contec CMS8000 / Epsimed MN-120 patient monitors), which are effectively public findings against the product.

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| 2014 | First final premarket cybersecurity guidance ("Content of Premarket Submissions for Management of Cybersecurity in Medical Devices") |
| 28 Dec 2016 | Final "Postmarket Management of Cybersecurity in Medical Devices" (docket FDA-2015-D-5105) — still current |
| 8 Apr 2022 | Draft premarket guidance (docket FDA-2021-D-1158) |
| 29 Dec 2022 | Consolidated Appropriations Act, 2023 signed; §3305 adds §524B and amends §301 (prohibited acts) |
| 29 Mar 2023 | §524B takes effect; submissions from this date must contain §524B information |
| 30 Mar 2023 | FDA Refuse-to-Accept policy guidance published (no RTA solely on §524B grounds before 1 Oct 2023) |
| 27 Sep 2023 | Final premarket guidance (Quality System Considerations…) |
| 1 Oct 2023 | RTA grace period ends; FDA may refuse to accept submissions lacking §524B content |
| 2 Feb 2024 | QMSR final rule published (89 FR 7496); correction 15 Oct 2024 (89 FR 82945) |
| 13 Mar 2024 | Draft "Select Updates for the Premarket Cybersecurity Guidance: Section 524B" (89 FR 18421) |
| 27 Jun 2025 | Final premarket guidance re-issued, finalising the select updates and adding the §524B section (Section VII) |
| 4 Dec 2025 | Conforming technical amendments to the device regulations for the QMSR (90 FR 55978), effective 2 Feb 2026 |
| 2 Feb 2026 | QMSR effective — 21 CFR Part 820 now incorporates ISO 13485:2016 (and ISO 9000:2015 clause 3) with US-specific additions at §§820.10, 820.35, 820.45 |
| 3 Feb 2026 | Premarket guidance re-issued as "…Quality Management System Considerations…" under Level 2 procedures (21 CFR 10.115(g)(4)) to align with the QMSR, superseding the June 2025 version; Level 2 revisions carry no Federal Register availability notice |
| 29 Jun 2026 | MDIC white paper "Validating Medical Device Cybersecurity Through Penetration Testing" published — industry reference for the guidance's testing expectations |
| Pending | No §524B(b)(4) regulation and no §524B(d) exemption list appear in the Federal Register as of September 2026; FDA must review and, as appropriate, update the premarket guidance periodically under §3305(e) |

## Key obligations for security/GRC teams

1. **Classify every product against the three-prong cyber-device test** early in design, treating any physical or wireless interface (including service USB ports) as "ability to connect"; record the determination and the submission pathway. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Embed an SPDF in the QMSR design-control process** (ISO 13485 clause 7.3) with threat modeling, a cybersecurity risk assessment separate from but traceable to ISO 14971, and architecture views; map it to IEC 81001-5-1 or ANSI/ISA 62443-4-1 for evidence. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md) and [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).
3. **Operate an SBOM pipeline**: machine-readable, NTIA minimum elements plus support status and end-of-support dates, refreshed on every software change, cross-checked against NVD and CISA KEV, and published to customers continuously. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../workflows/vendor-onboarding.md](../../workflows/vendor-onboarding.md) for supplier flow-down (source-code escrow, support commitments).
4. **Write and version the Cybersecurity Management Plan / §524B(b)(1) plan** with a justified regular patch cycle, an out-of-cycle path for uncontrolled risks, a CVD policy and customer-communication procedure; re-submit deltas with each modification. See [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).
5. **Wire the 30/60-day uncontrolled-risk clocks, 10-working-day Part 806 reports and 30-day/5-day MDR reports into incident response**, with a documented controlled/uncontrolled decision record per vulnerability and ISAO evidence retained. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md), [../../workflows/incident-regulatory-response.md](../../workflows/incident-regulatory-response.md) and [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
6. **Run and document security testing** (requirements, threat mitigation, vulnerability testing, independent penetration testing with the five report elements) before each submission and periodically postmarket. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
7. **Maintain security labeling and customer documentation** (MDS2, ports/interfaces, secure configuration, logging, end-of-support) as controlled QMS records; labeling errors are misbranding exposure.
8. **Track fielded-version risk**: assess vulnerabilities against every software configuration in the field, and pre-communicate end-of-support risk transfer.
9. **Horizon-scan** for the §524B(d) exemption list, any §524B(b)(4) rulemaking and further guidance re-issues; treat the premarket guidance version as a controlled input. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).
10. **Report to the board** on submission readiness, open uncontrolled risks, patch-cycle adherence and SBOM coverage. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **HIPAA:** §524B binds the manufacturer; HIPAA binds the covered entity or business associate that operates the device. A manufacturer that hosts or accesses ePHI (cloud-connected devices, remote service) is usually a business associate and needs a BAA; a device compromise exposing ePHI triggers HIPAA breach clocks at the provider in parallel with the manufacturer's Part 806/803 duties. See [hipaa.md](hipaa.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
- **HHS 405(d) HICP (2023 edition):** voluntary, consensus practices for healthcare delivery organisations under §405(d) of the Cybersecurity Act of 2015 — five threats (incl. attacks on network-connected medical devices) and ten practices, with CSP 9 "Network Connected Medical Devices" and two technical volumes (small; medium/large organisations). It is the provider-side complement to FDA's manufacturer-side rules; manufacturers' labeling and SBOMs should feed the provider's asset and vulnerability management practices. IEC 80001-1:2021 covers risk management for IT networks incorporating medical devices on the provider side.
- **NIST CSF:** FDA's postmarket guidance is built on the CSF functions; the premarket guidance points healthcare facilities to the CSF for managing devices. See [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md).
- **EU MDR/IVDR and MDCG 2019-16 rev.1 (July 2020):** the EU equivalent is not a standalone cyber statute but General Safety and Performance Requirements in MDR Annex I — 17.2 (state-of-the-art development lifecycle incl. information security), 17.4 (minimum IT requirements), 18.8 (protection against unauthorised access), 14.2(d)/14.5 (IT environment, interoperability), 23.4 (IFU minimum IT requirements) — with IVDR Annex I 16.2/16.4 counterparts, and post-market surveillance/vigilance under Arts. 83–89. A single SPDF and SBOM programme can serve both regimes; IEC 81001-5-1 is the common lifecycle standard. Check [eu-cyber-resilience-act.md](eu-cyber-resilience-act.md) for how that act treats devices already regulated under MDR/IVDR before double-counting obligations.
- **IMDRF:** FDA states its guidance aligns with IMDRF's "Principles and Practices for Medical Device Cybersecurity" (final, March 2020), the harmonisation baseline for total-product-lifecycle, shared-responsibility and CVD expectations.
- **SEC disclosure and CIRCIA:** a listed manufacturer's material device-cyber incident may also be a Form 8-K Item 1.05 event; healthcare-sector entities may also face CIRCIA reporting once that regime is in force (see [us-circia.md](us-circia.md)). See [sec-cyber-disclosure.md](sec-cyber-disclosure.md).
- **ISO 27001 / SOC 2:** neither substitutes for §524B evidence, but the vulnerability-management, supplier and logging controls provide reusable evidence for the management plan. See [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).

## Primary sources

- 21 U.S.C. 360n-2 (FD&C Act §524B) — legal text, Office of the Law Revision Counsel: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title21-section360n-2&num=0&edition=prelim
- 21 U.S.C. 331 (prohibited acts, incl. (q)(3)) and 21 U.S.C. 333 (penalties) — legal text: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title21-section331&num=0&edition=prelim and https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title21-section333&num=0&edition=prelim
- 45 CFR 102.3 — HHS civil monetary penalty inflation table (eCFR): https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-102/section-102.3
- FDA final guidance "Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions" (3 February 2026, docket FDA-2021-D-1158) — regulator guidance, PDF: https://www.fda.gov/media/119933/download ; landing page: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-management-system-considerations-and-content-premarket
- FDA final guidance "Postmarket Management of Cybersecurity in Medical Devices" (December 2016, docket FDA-2015-D-5105) — regulator guidance, PDF: https://www.fda.gov/media/95862/download
- FDA medical device cybersecurity hub (guidance history, safety communications, resources) — regulator page: https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity
- Federal Register — QMSR final rule, 2 February 2024 (89 FR 7496): https://www.federalregister.gov/documents/2024/02/02/2024-01709/medical-devices-quality-system-regulation-amendments ; QMSR conforming technical amendments, 4 December 2025 (90 FR 55978): https://www.federalregister.gov/documents/2025/12/04/2025-21955/medical-devices-quality-management-system-regulation-technical-amendments
- Federal Register — RTA policy guidance availability notice, 30 March 2023 (88 FR 19148): https://www.federalregister.gov/documents/2023/03/30/2023-06646/cybersecurity-in-medical-devices-refuse-to-accept-policy-for-cyber-devices-and-related-systems-under ; premarket guidance availability notice, 27 June 2025 (90 FR 27634): https://www.federalregister.gov/documents/2025/06/27/2025-11669/cybersecurity-in-medical-devices-quality-system-considerations-and-content-of-premarket-submissions
- 21 CFR Part 820 (QMSR), Part 806 (corrections and removals), Part 803 (MDR) — legal text, eCFR: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820 ; https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-806 ; https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803
- HHS 405(d) "Health Industry Cybersecurity Practices: Managing Threats and Protecting Patients", 2023 edition — publisher document: https://405d.hhs.gov/Documents/HICP-Main-508.pdf
- MDCG 2019-16 rev.1 "Guidance on Cybersecurity for medical devices" (July 2020) — publisher document: https://health.ec.europa.eu/document/download/b23b362f-8a56-434c-922a-5b3ca4d0a7a1_en?filename=md_cybersecurity_en.pdf
- IEC 80001-1:2021 — IEC webstore catalogue page: https://webstore.iec.ch/en/publication/34263
- MDIC, "Validating Medical Device Cybersecurity Through Penetration Testing" (29 June 2026) — industry white paper: https://www.mdic.org/resource/validating-medical-device-cybersecurity-through-penetration-testing/
- IEC 81001-5-1, ANSI/ISA 62443-4-1, ANSI/AAMI SW96, AAMI TIR57 and the IMDRF cybersecurity principles are paywalled or blocked to automated retrieval; their titles, dates and roles above are taken from the FDA premarket guidance that cites them. IEC catalogue: https://webstore.iec.ch/

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
