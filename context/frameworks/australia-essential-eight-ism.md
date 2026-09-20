# Australia — ASD Essential Eight Maturity Model and Information Security Manual (ISM)

## At a glance

| Attribute | Detail |
|---|---|
| Publisher | Australian Signals Directorate (ASD), through the Australian Cyber Security Centre (ACSC). ISM advice is given under ASD's designated functions in the *Intelligence Services Act 2001* |
| Instruments | *Information Security Manual* (ISM) — the full control catalogue; *Essential Eight Maturity Model* (November 2023 release) — eight prioritised mitigation strategies expressed as four maturity levels (Maturity Level Zero to Three; ML0 simply records that ML1 is not met), mapped by ASD onto ISM controls |
| Current release | ISM document **v2026.09.03** and matching OSCAL catalog **v2026.09.4**, both published 3 September 2026. ISM content releases are quarterly (March, June, September, December); OSCAL artefacts are sometimes re-issued between quarters |
| Size | **1,143 security controls** plus **49 cyber security principles**, across 23 guideline chapters. Controls are cited as ISM-nnnn (highest current identifier ISM-2167); principles carry function labels GOV-nn (14), IDE-nn (6), PRO-nn (17), DET-nn (5), RES-nn (5), REC-nn (2) |
| Applicability markings | Each control is marked NC (non-classified), OS (OFFICIAL: Sensitive), P (PROTECTED), S (SECRET), TS (TOP SECRET). Counts in v2026.09.4: NC 1,017 · OS 1,028 · P 1,028 · S 1,092 · TS 1,101 |
| Essential Eight baselines | ML1 = 46 ISM controls · ML2 = 87 · ML3 = 123 (v2026.09.4 resolved profiles) |
| Legal status | Voluntary by default: "An organisation is not required as a matter of law to comply with the ISM, unless legislation, or a direction given under legislation or by some other lawful authority, compels them to comply." Mandating instruments (PSPF for Commonwealth entities, SOCI CIRMP Rules for critical infrastructure) supply the obligation |
| Assessment model | No certificate. Security control assessment inside a six-step risk management framework ending in an **authorisation to operate**; assessors are the organisation's own, IRAP-registered, or ASD assessors for TOP SECRET |
| Machine-readable | ASD publishes the ISM in OSCAL (catalog + profiles per classification and per Essential Eight maturity level) at `cyber.gov.au/ism/oscal` — the practical ingestion path for GRC tooling |
| Neighbours | Mandated or referenced by the PSPF and the SOCI CIRMP Rules; conceptually adjacent to NIST SP 800-53/800-37, CIS Controls and ISO/IEC 27001 |

## What it is

Australia runs two complementary artefacts from one source. The **ISM** is a full-spectrum control catalogue organised as cyber security principles (strategic, grouped into the six functions *govern, identify, protect, detect, respond, recover*) plus cyber security guidelines (practical controls by topic). Its stated purpose is to "outline a cyber security framework that an organisation can apply, using their risk management framework, to protect their information technology (IT) and operational technology (OT) systems from cyber threats"; its intended audience is CISOs, CIOs, cyber security professionals and IT/OT managers.

The **Essential Eight** is the prioritised subset: eight mitigation strategies ASD considers the baseline against the intrusion tradecraft it observes, expressed at four maturity levels. ML1 to ML3 are graduated against increasing attacker tradecraft and targeting; Maturity Level Zero carries no requirements and exists only to record that ML1 is not met. ASD maps every maturity-level requirement onto ISM controls and ships that mapping as OSCAL profiles (`ISM_E8_ML1/2/3-baseline`), so Essential Eight reporting and ISM compliance become the same evidence exercise at different scopes. ASD's own implementation advice is to reach the same maturity level across all eight strategies before moving up, and it states that no independent certification of an Essential Eight implementation is required unless a government directive, a regulator or a contract demands one.

The ISM is advisory in itself. Its force comes from elsewhere: the Protective Security Policy Framework (administered by the Department of Home Affairs) for Commonwealth entities, the SOCI critical infrastructure risk management program rules for critical infrastructure, and contractual flow-down for suppliers and cloud providers. The ISM text is explicit that it does not override legislation and that where the two conflict, legislation prevails.

## Who it covers / Scope

- **Commonwealth government.** The PSPF, administered by the Department of Home Affairs, is given force by a Ministerial direction to accountable authorities of non-corporate Commonwealth entities subject to the *Public Governance, Performance and Accountability Act 2013*. **PSPF Release 2026** (published 1 July 2026) requires each of the eight mitigation strategies to be implemented to **Maturity Level Two** (section 14.2, Requirements 0099–0106, effective 31 October 2024), requires ISM cyber security principles to be applied across every stage of a system's lifecycle and ISM controls and guidelines to be applied on a risk-based approach (Requirements 0084–0085), and requires gateway capabilities that have completed an IRAP assessment — or an ASD assessment for TOP SECRET — against the latest ISM within the previous 24 months (Requirement 0114, from 1 July 2026).
- **Critical infrastructure.** The SOCI *Critical Infrastructure Risk Management Program* Rules (LIN 23/006) 2023 — current compilation F2026C00562, registered 7 July 2026 and in force from 10 June 2026 — list the Essential Eight Maturity Model at **Maturity Level One** as one of five acceptable frameworks for the baseline cyber and information security hazard obligation (section 8(4)) and at **Maturity Level Two** for the enhanced obligations applying to systems of national significance (section 8A(3)). The wider CIRMP duties, including the credential-compromise and lateral-movement sections added by that compilation, are in [../regulations/australia-soci-cyber-security-act.md](../regulations/australia-soci-cyber-security-act.md).
- **Suppliers to government.** Managed service providers, outsourced cloud service providers and gateways serving non-classified, OFFICIAL: Sensitive, PROTECTED and SECRET systems must undergo an **IRAP assessment at least every 24 months**, using the latest ISM release available before the assessment begins (or a later one) — ISM-1793 (managed services), ISM-1570 (cloud services), ISM-0100 (gateways). TOP SECRET equivalents are assessed by ASD assessors on the same 24-month cycle (ISM-1971, ISM-1972).
- **Everyone else.** Private-sector use is voluntary but widespread: Essential Eight maturity is the de facto Australian shorthand in board reporting, cyber insurance questionnaires and vendor due diligence. Nothing in the ISM restricts its use to government.
- **Classification-driven tailoring.** Scope within an organisation is set per system: define the system boundary and business criticality, then select controls by applicability marking (NC/OS/P/S/TS). Only ~1,017 of the 1,143 controls apply to a non-classified system.

## Structure and requirements

### ISM chapters (v2026.09.4 control counts)

| Guideline | Controls | Guideline | Controls |
|---|---|---|---|
| System hardening | 161 | Communications systems | 33 |
| System access | 123 | Email | 26 |
| Software development | 114 | Cyber security incidents | 21 |
| Networking | 78 | Physical security | 19 |
| Cryptography | 71 | Personnel security | 17 |
| Gateways | 63 | Data transfers | 14 |
| System management | 61 | Database systems | 13 |
| Media | 56 | Cyber security documentation | 11 |
| Communications infrastructure | 53 | Evaluated products | 5 |
| Enterprise mobility | 51 | Procurement and outsourcing | 40 |
| Cyber security roles | 42 | Security assurance | 36 |
| IT equipment | 35 | | |

### The eight mitigation strategies and where they live in the ISM

| Strategy | ISM sections carrying the controls | ML1 / ML2 / ML3 controls |
|---|---|---|
| Application control | Operating system hardening → Application control | 3 / 8 / 11 |
| Patch applications | System maintenance → Mitigating known vulnerabilities, Cessation of support; Security assessments → Vulnerability scanning | counted jointly with OS patching: 9 / 10 / 17 for maintenance + cessation, 6 / 7 / 9 for scanning |
| Configure Microsoft Office macro settings | User application hardening → Office productivity suites | 4 / 11 / 17 |
| User application hardening | User application hardening → Web browsers, PDF applications; OS hardening → Command Shell, PowerShell | 3 / 9 / 11 |
| Restrict administrative privileges | Identity and access management → Privileged access, Suspension of access; System administration → Separate privileged operating environments, Administrative infrastructure | 7 / 13 / 16 |
| Patch operating systems | System maintenance → Mitigating known vulnerabilities; OS hardening → OS releases and versions | shares the sections above; see the clocks table |
| Multi-factor authentication | Identity and access management → Multi-factor authentication | 7 / 13 / 15 |
| Regular backups | Data backup and restoration → performing/retaining, backup access, modification and deletion, testing restoration | 6 / 8 / 11 |

One further section, *Hardening operating system configurations* (1 / 1 / 3), carries Essential Eight controls without mapping cleanly to a single strategy — it includes ISM-1654, disabling or removing Internet Explorer 11. Supporting sections pulled into ML2/ML3 include centralised event logging, event log monitoring, credential protection, built-in administrator and service account credentials, operating system releases and versions, incident reporting to the CISO (ISM-0123) and to ASD (ISM-0140), and enacting the incident response plan (ISM-1819).

### Patching clocks (the most-cited numbers)

| Asset class | Critical / working exploit | Non-critical | Scan cadence | Level |
|---|---|---|---|---|
| Online services | 48 hours (ISM-1876) | two weeks (ISM-1690) | daily (ISM-1698) | ML1+ |
| Internet-facing server/network-device OS | 48 hours (ISM-1877) | two weeks (ISM-1694) | daily (ISM-1701) | ML1+ |
| Office suites, browsers + extensions, email clients, PDF apps, security products | — | two weeks (ISM-1691) | weekly (ISM-1699) | ML1–ML2 |
| Same, at ML3 | 48 hours (ISM-1692) | two weeks (ISM-1901) | weekly (ISM-1699) | ML3 |
| Workstation / non-internet-facing OS | — | one month (ISM-1695) | fortnightly (ISM-1702) | ML1–ML2 |
| Same, at ML3 | 48 hours (ISM-1696) | one month (ISM-1902) | fortnightly (ISM-1702) | ML3 |
| Other applications | — | one month (ISM-1693) | fortnightly (ISM-1700) | ML2+ |
| Drivers | 48 hours (ISM-1879) | one month (ISM-1697) | fortnightly (ISM-1703) | ML3 |
| Firmware | 48 hours (ISM-1903) | one month (ISM-1904) | — | ML3 |

Unsupported software is removed or replaced at every level: online services (ISM-1905), user applications (ISM-1704), operating systems (ISM-1501). Automated asset discovery at least fortnightly (ISM-1807) underpins the scanning.

### What each maturity step actually adds

| Step | Representative additions |
|---|---|
| ML1 → ML2 | Application control on internet-facing servers (ISM-1490) and outside user/temp folders (ISM-1871); Microsoft's recommended application blocklist (ISM-1544); annual ruleset validation (ISM-1582); MFA for privileged (ISM-1173) and unprivileged (ISM-0974) system users, phishing-resistant (ISM-1682, ISM-1872); central logging of privileged access (ISM-1509), MFA events (ISM-1683) and application control events (ISM-1660); log protection (ISM-1815); analysis of internet-facing server logs (ISM-1906); incident reporting to ASD (ISM-0140) and IR plan enactment (ISM-1819) |
| ML2 → ML3 | Application control on non-internet-facing servers (ISM-1656) and drivers (ISM-1658); Microsoft vulnerable driver blocklist (ISM-1659); just-in-time administration (ISM-1649) and least-privilege validation (ISM-1508); MFA for data repositories (ISM-1505, ISM-1894); 48-hour patching of workstation OS and user applications; driver and firmware patching; log analysis extended to non-internet-facing servers (ISM-1907) and workstations (ISM-0109); accounts blocked from accessing even their own backups (ISM-1813 unprivileged, ISM-1706 privileged other than backup administrators) |

Maturity levels are **near-cumulative, not strictly cumulative**: ML1 is a subset of ML2, but three controls present at lower levels are replaced by stricter ML3 equivalents (ISM-1691 by the split ISM-1692/ISM-1901 pair, ISM-1695 by ISM-1696/ISM-1902, and ISM-1873's "phishing-resistant option" for customers by ISM-1874's mandatory phishing-resistant MFA). Do not compute ML3 coverage by summing lower-level results.

## Assessment, certification and evidence

There is no ISM or Essential Eight certificate. The ISM defines a six-step risk management framework drawn from **NIST SP 800-37 Rev. 2**: define the system → select security controls → implement → assess → authorise → monitor.

| Element | Detail |
|---|---|
| Authorising officer | The organisation's CISO (or delegate) for non-classified, OFFICIAL: Sensitive, PROTECTED and SECRET systems; **Director-General ASD** (or delegate) for TOP SECRET and sensitive compartmented information systems. For commercial providers, the authorising officer is the CISO of the supported organisation |
| Who may assess | The organisation's own assessors or **IRAP** (Infosec Registered Assessors Program) assessors for NC/OS/P/S; ASD assessors (or delegates) for TOP SECRET. Assessors must hold an appropriate clearance and relevant experience |
| Authorisation package | System security plan (+ annex listing selected controls and their implementation), cyber security incident response plan, change and configuration management plan, continuous monitoring plan, security assessment report, plan of action and milestones |
| Outcome | Ongoing authorisation to operate; a constrained ATO (limited functionality or an expiry date); or denial pending remediation |
| Reassessment triggers | Policy change, new or emerging threats, controls found less effective than planned, a major incident involving the system, major architectural change |
| Third-party cadence | Managed service providers, outsourced cloud service providers and gateways: IRAP assessment **at least every 24 months** against the latest ISM release available at assessment start |
| Incident reporting | Report to the CISO or delegate as soon as possible (ISM-0123) and to ASD as soon as possible (ISM-0140); both are ML2/ML3 Essential Eight controls. A **limited use obligation** on ASD, enacted by the *Intelligence Services and Other Legislation Amendment (Cyber Security) Act 2024*, restricts how voluntarily provided incident information may be used and disclosed; it does not displace statutory reporting duties |
| Essential Eight assessments | ASD's *Essential Eight assessment process guide* (first published 24 November 2022; current release October 2024, written against the November 2023 maturity model) sets out four assessment stages — plan and prepare, determine scope and approach, assess the controls, write the security assessment report — plus report and test-plan templates |
| Evidence quality | The same guide ranks evidence in four tiers: **excellent** (testing the control with a simulated activity), **good** (reviewing live system configuration through its interface), **fair** (reviewing a copy of configuration, such as a report or screenshot), **poor** (a policy statement or verbal assertion). Assessors are told to use the highest tier reasonably practicable |

## Timeline and status (as at September 2026)

| Date | Event |
|---|---|
| 30 June 2017 | Essential Eight maturity model first published |
| 27 November 2023 | Last substantive update to the Essential Eight maturity model. Still the current edition as at late August 2026 |
| October 2024 | Current release of the *Essential Eight assessment process guide* (first published 24 November 2022) |
| 31 October 2024 | PSPF Essential Eight requirements (0099–0106, Maturity Level Two) and ISM requirements (0084–0085) take effect |
| Quarterly since at least March 2022 | ISM content releases in March, June, September and December; control-level `updated` tags confirm an unbroken cadence |
| Jun 2025 / Sep 2025 / Dec 2025 | 86 / 14 / 53 controls amended |
| Mar 2026 / Jun 2026 | 21 / 120 controls amended — the June 2026 release was a substantial revision |
| 10 June 2026 | SOCI CIRMP Rules compilation F2026C00562 takes effect, adding credential-compromise and lateral-movement obligations alongside the existing Essential Eight framework options |
| 15 June – 12 July 2026 | ASD consults its Cyber Security Partnership Program network on **evolving the Essential Eight into a new "Essentials" series**, the first chapter being *Essentials for enterprise IT*, grounded in the ISM and promising strong alignment with existing Essential Eight controls. **Pending:** no replacement guidance had been published as at September 2026, and the November 2023 maturity model remains the operative document |
| 1 July 2026 | **PSPF Release 2026** published, carrying the Maturity Level Two requirement forward and adding gateway IRAP currency (Requirement 0114) |
| 3 September 2026 | **ISM v2026.09.03 / OSCAL v2026.09.4** — 146 controls touched, including **44 entirely new controls, ISM-2124 to ISM-2167** |
| September 2026 emphasis | New controls concentrate in system access (16), networking (8), system hardening (6), software development (6), system management (4) and procurement and outsourcing (2). Themes: service-provider access restricted to approved tools, source addresses and time windows with independent tamper-proof logging (ISM-2124, ISM-2125); OAuth device-code flow disabled unless required (ISM-2140); unauthorised remote monitoring and management or remote-access tools blocked at gateways (ISM-2150); management interfaces reachable only from a segregated management network (ISM-2160); AD CS web enrolment hardening (ISM-2130) |
| September 2026 terminology | **35 controls now say "human users"** rather than "users" — every one of them carries a September 2026 update tag. Non-human identities (service accounts, automation) are no longer covered by those control statements. Affected controls include ML1 staples: MFA (ISM-1504, ISM-1679), Office macros (ISM-1671, ISM-1489), browser settings (ISM-1585), dedicated privileged accounts (ISM-0445) |

## Key obligations for security/GRC teams

1. **Establish which instrument makes the ISM binding for you** — PSPF, SOCI CIRMP, a contract, or nothing at all — before choosing a target maturity level. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md) and [../regulations/australia-soci-cyber-security-act.md](../regulations/australia-soci-cyber-security-act.md).
2. **Pin the ISM release in every artefact.** Controls move quarterly and 146 changed in September 2026 alone; an assessment that does not name the release version is unreproducible. Ingest the OSCAL catalog rather than transcribing the PDF.
3. **Assess at the right scope.** Essential Eight ML1 is 46 controls; a PROTECTED system is 1,028. Do not present an Essential Eight score as ISM compliance. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).
4. **Treat maturity as per-strategy, not an average.** ASD's model is strategy-by-strategy; a "ML1.6 overall" figure hides the weakest strategy, which is what matters. Report the minimum across the eight. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).
5. **Instrument the patch clocks.** 48 hours / two weeks / one month with daily, weekly and fortnightly scanning are measurable; build the evidence pipeline from the scanner, not from a spreadsheet. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
6. **Re-baseline for the "human users" change** and for the new service-provider access controls (ISM-2124, ISM-2125) — non-human identities now need their own treatment, and provider access needs approved tools, source addresses, time windows and independent logging. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
7. **Run the authorisation package as a living set**, not a point-in-time deliverable: SSP + annex, IR plan, change/configuration plan, continuous monitoring plan, security assessment report, POA&M. Track unimplemented controls as formal exceptions ([../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md)).
8. **Diarise IRAP cycles at 24 months** for in-scope managed services, cloud services and gateways, and check which ISM release the provider's current report was assessed against. See [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).
9. **Track the Essentials series.** ASD consulted through mid-2026 on replacing the Essential Eight with a broader Essentials series; target maturity levels, PSPF requirements and CIRMP framework options all reference the current maturity model by name, so a replacement would cascade. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).
10. **Wire ASD reporting into the incident plan** alongside statutory clocks — ISM-0140 is "as soon as possible", while SOCI and privacy duties carry hard deadlines. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).

## Interplay

- **SOCI Act / Cyber Security Act 2024:** the CIRMP Rules make Essential Eight maturity one of several acceptable cyber frameworks, and ASD receives SOCI incident reports. Reporting an incident to ASD under ISM-0140, and the limited use obligation that attaches to it, is not a substitute for the statutory SOCI notification clocks. See [../regulations/australia-soci-cyber-security-act.md](../regulations/australia-soci-cyber-security-act.md).
- **APRA CPS 234 / CPS 230:** APRA-regulated entities are supervised against prudential standards, not the ISM; Essential Eight is nonetheless a common way to evidence CPS 234 control effectiveness. See [../regulations/australia-apra-cps-234-230.md](../regulations/australia-apra-cps-234-230.md).
- **Privacy Act 1988:** the ISM names the Privacy Act among the legislation organisations should familiarise themselves with; Essential Eight maturity is frequently cited as "reasonable steps" under APP 11. See [../regulations/australia-privacy-act.md](../regulations/australia-privacy-act.md).
- **NIST:** the ISM's risk management framework is explicitly derived from SP 800-37 Rev. 2, and the ISM's six principle functions match the NIST CSF 2.0 function set. An organisation already running an 800-37 authorisation process or a CSF profile maps across cleanly. See [nist-rmf-800-37-800-30.md](nist-rmf-800-37-800-30.md), [nist-csf-2.md](nist-csf-2.md) and [nist-800-53.md](nist-800-53.md).
- **CIS Controls:** the Essential Eight and CIS IG1 occupy the same "essential hygiene" niche with heavy overlap (application control, patching, MFA, admin privileges, backups) but different granularity — the Essential Eight is deeper on Microsoft-ecosystem specifics, CIS broader on inventory and awareness. See [cis-controls-v8.md](cis-controls-v8.md).
- **ISO/IEC 27001:** complementary rather than competing — 27001 supplies the management system, the ISM supplies the technical control depth and a per-system authorisation model. See [iso-27001-2022.md](iso-27001-2022.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
- **Precedence inside ASD's own material:** the ISM states that ASD's Australian Communications Security Instructions and product- or platform-specific publications may take precedence over ISM advice.

## Primary sources

- ASD *Information Security Manual*, OSCAL catalog and resolved profiles, v2026.09.4 (3 September 2026) — `https://www.cyber.gov.au/ism/oscal`. Retrieved from ASD's own GitHub mirror, `https://github.com/AustralianCyberSecurityCentre/ism-oscal`, which that page announces and which carries the identical release. All control identifiers, statements, chapter and applicability counts, Essential Eight baselines, patch timeframes, risk management framework steps, IRAP cadence and incident-reporting controls in this pack come from that catalog.
- ISM landing page and guidelines, `https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism`; ISM PDF release v2026.09.03, `https://www.cyber.gov.au/ism/pdf/v2026.09.03-pdf` — canonical publisher locations named in the catalog's own back matter.
- ASD *Essential Eight maturity model*, `https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight/essential-eight-maturity-model` — first published 30 June 2017, last updated 27 November 2023; source of the four maturity levels, the tradecraft descriptions and the "no independent certification required" statement.
- ASD *Essential Eight assessment process guide*, `https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight/essential-eight-assessment-process-guide` — October 2024 release; source of the four assessment stages and the four evidence-quality tiers.
- ASD news item, *Consultation on evolution of Essential Eight*, 15 June 2026, `https://www.cyber.gov.au/about-us/view-all-content/news/consultation-on-evolution-of-essential-eight`.
- ASD IRAP overview, `https://www.cyber.gov.au/business-government/protecting-devices-systems/assessment-evaluation-programs/irap`.
- Department of Home Affairs, *Protective Security Policy Framework Release 2026*, published 1 July 2026 — `https://www.protectivesecurity.gov.au/publications-library/pspf-annual-release-2026` (full text at `https://www.protectivesecurity.gov.au/system/files/2026-07/pspf-release-2026_6.pdf`); source of Requirements 0084, 0085, 0099–0106 and 0114.
- Federal Register of Legislation, *Security of Critical Infrastructure (Critical infrastructure risk management program) Rules (LIN 23/006) 2023*, compilation F2026C00562 — `https://www.legislation.gov.au/F2023L00112/latest/text`; source of the Essential Eight framework options at sections 8(4) and 8A(3).
- Note on retrieval: `cyber.gov.au` and `protectivesecurity.gov.au` reject automated requests (HTTP 403). Their content was confirmed from Internet Archive captures of those exact pages taken in August and September 2026; the URLs above are the canonical publisher locations.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
