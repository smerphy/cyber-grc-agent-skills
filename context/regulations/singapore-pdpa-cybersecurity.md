# Singapore: PDPA, Cybersecurity Act 2018 (as amended 2024) and MAS technology risk requirements

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | Personal Data Protection Act 2012 (PDPA, 2020 Rev. Ed., as amended by Act 40 of 2020); Personal Data Protection (Notification of Data Breaches) Regulations 2021 (S 64/2021); Cybersecurity Act 2018 (Act 9 of 2018) as amended by the Cybersecurity (Amendment) Act 2024 (Act 19 of 2024); Cybersecurity (Provider-Owned CII) Regulations 2018 (S 519/2018, as amended S 678/2025); MAS Notices FSM-N05 (Technology Risk Management) and FSM-N06 (Cyber Hygiene) for banks, with parallel FSM-N03 to FSM-N26 for other FI types; MAS Guidelines on Risk Management Practices – Technology Risk (18 Jan 2021); MAS Notice 658 / Guidelines on Outsourcing (Banks) |
| Regulators | Personal Data Protection Commission (PDPC) — PDPA; Commissioner of Cybersecurity / Cyber Security Agency of Singapore (CSA) — Cybersecurity Act; Monetary Authority of Singapore (MAS) — financial institutions |
| Status and key dates | PDPA mandatory breach notification since 1 Feb 2021; turnover-based penalty ceiling since 1 Oct 2022. Cybersecurity Act in force 31 Aug 2018; 2024 amendments passed 7 May 2024, main provisions commenced 31 Oct 2025; Cybersecurity Code of Practice for CII 2026 (CCoP 2026) effective 29 Jul 2026. MAS FSM-series TRM and Cyber Hygiene Notices effective 10 May 2024; new MAS incident-reporting template mandatory via MAS-Tx from 1 Feb 2026 |
| Who is covered | PDPA: every "organisation" (any individual, company or body, whether or not formed or resident in Singapore) except individuals acting in a personal/domestic capacity, employees and public agencies. Cybersecurity Act: designated owners of critical information infrastructure (CII) in essential-service sectors, providers responsible for third-party-owned CII, owners of systems of temporary cybersecurity concern (STCC), plus (once commenced) entities of special cybersecurity interest (ESCI) and major foundational digital infrastructure (FDI) providers such as cloud and data-centre operators; licensed penetration-testing and managed SOC providers. MAS: all MAS-regulated financial institutions |
| Structure | PDPA: data protection obligations in Parts 3–6A (including Part 6A breach notification); Part 6B (data portability, ss. 26F onwards, inserted by Act 40 of 2020) is enacted but absent from the in-force text; enforcement in Part 9C (ss. 48G–48O). Cybersecurity Act: Parts 3–3D (regulated systems and entities), Part 4 (CSA response powers), Part 5 (licensing), s. 35A codes of practice. MAS: binding Notices (hard clocks and minimum controls) layered under non-binding Guidelines (best practice) |
| Breach / incident clocks | PDPC: notify within 3 calendar days of assessing a breach as notifiable. CSA (CII): 2 hours initial, 72 hours supplementary, 30 days final report. MAS: 1 hour notification of a relevant incident, root-cause and impact report within 14 days; initial incident report within 24 hours under the Dec 2025 circular |
| Penalties | PDPA: financial penalty up to 10% of annual Singapore turnover (turnover above S$10m) or S$1m; private right of action; individual offences up to S$5,000 fine and/or 2 years. Cybersecurity Act: failure to report a CII incident up to S$100,000 fine and/or 2 years; Commissioner may issue binding written directions. MAS: supervisory action under the Financial Services and Markets Act 2022 and sectoral Acts |
| Certifiable? | No statutory certification for PDPA. CSA Cyber Essentials and Cyber Trust marks are voluntary, but CCoP 2026 requires CII owners to hold Cyber Trust Mark Advocate (Tier 5) or equivalent, and from the Feb 2026 licensing review licensed cybersecurity service providers must hold Cyber Trust Promoter (Tier 3) or ISO/IEC 27001 |
| Relationship to neighbours | PDPA is a general-purpose privacy law comparable in role to GDPR but consent-centric and with a harm/scale breach test; the Cybersecurity Act is the NIS2/CER-style critical-infrastructure regime; MAS requirements parallel DORA and APRA CPS 234/230 for the financial sector |

## What it is

Singapore regulates cybersecurity through three separate but overlapping regimes. The **PDPA** (2012, substantially amended in 2020) is the horizontal privacy statute: it imposes a "reasonable security arrangements" protection obligation on all private-sector organisations and, since 1 February 2021, a mandatory data-breach assessment and notification duty administered by the PDPC. The **Cybersecurity Act 2018** created the Commissioner of Cybersecurity (heading CSA), a designation-based regime for critical information infrastructure supporting essential services, investigation and emergency powers, and licensing for penetration-testing and managed SOC providers. The **Cybersecurity (Amendment) Act 2024** rewrote the CII regime around "provider-owned" and "third-party-owned" CII (so cloud-hosted and outsourced CII stay in scope), added supply-chain incident reporting, and created new regulated classes: STCCs, ESCIs and major FDI providers. Most of the amendment commenced on 31 October 2025.

For financial institutions, **MAS** adds sector rules: legally binding Notices on Technology Risk Management and Cyber Hygiene (re-issued under the Financial Services and Markets Act 2022 as the FSM-N series on 10 May 2024), the 2021 Technology Risk Management Guidelines, and an outsourcing regime for banks anchored in Banking Act s. 47A (Notice 658) and outsourcing guidelines for all FIs, both effective 11 December 2024. MAS recorded an open consultation on proposed Guidelines on Third-Party Risk Management as at 6 March 2026; final guidelines had not been issued as of September 2026.

## Who it covers / Scope

| Regime | Applicability test | Notable exclusions / limits |
|---|---|---|
| PDPA (s. 2, s. 4) | Any organisation collecting, using or disclosing personal data in Singapore, "whether or not formed or recognised under the law of Singapore" or resident there — extraterritorial by design | Individuals acting in a personal/domestic capacity; employees acting in the course of employment; public agencies (governed separately); business contact information; records over 100 years old |
| PDPA data intermediaries (s. 4(2)–(3)) | A processor under a written contract is bound only by s. 24 (protection), s. 25 (retention), s. 26C(3)(a) (notify the controlling organisation of a breach) and s. 26E; the controlling organisation remains liable as if it processed the data itself | Contract must be evidenced or made in writing to obtain intermediary treatment |
| Cybersecurity Act — provider-owned CII (s. 7) | Commissioner designates a computer/system that is "necessary for the continuous delivery of an essential service" whose loss or compromise would have "a debilitating effect" on availability of that service in Singapore, located wholly or partly in Singapore; s. 7(1A) allows designation of systems located wholly outside Singapore that would otherwise qualify | Essential services are listed in the First Schedule (46 service entries across energy, infocomm, water, healthcare, banking and finance, security and emergency services, aviation, land transport, maritime, government and media). Designation lasts 5 years; 14 days minimum for representations; appeal to the Minister |
| Third-party-owned CII (Part 3A, s. 16A) | An essential-service provider is designated as responsible where a system it depends on (in or outside Singapore) meets the CII test but is not owned by the provider; duties include obtaining a legally binding commitment from the owner that prescribed standards are maintained (s. 16F) and that the owner will report incidents to the provider within 72 hours (s. 16I(1) with reg. 5), reporting to the Commissioner on the 2h/72h/30-day cycle (s. 16I(4) with reg. 7), and notifying material changes to that commitment within 14 days (s. 16K) | Regulations S 490/2026 in operation 13 Jul 2026 |
| STCC (Part 3B, s. 17) | Temporary designation of systems at elevated risk because of an event or situation | Regulations S 680/2025 in operation 31 Oct 2025 |
| ESCI (Part 3C) and major FDI providers (Part 3D) | Entities holding sensitive information or performing functions of national interest; providers of foundational digital infrastructure services (Third Schedule) to persons in Singapore, from within or outside Singapore | Parts 3C and 3D and the Third Schedule were enacted by Act 19 of 2024 but are absent from the in-force consolidation of the Act as at September 2026 — not yet commenced |
| Virtual systems (s. 2) | "Computer" and "computer system" include virtual computers; a virtual system is in Singapore if any physical computing resource simulating it is located in Singapore | Brings cloud-hosted CII squarely within scope |
| MAS Notices | Apply by licence category (banks: FSM-N05/N06; insurers FSM-N03/N04; finance companies FSM-N09/N10; payment service providers FSM-N13/N14; capital markets FSM-N21/N22; etc.) | FSM-N06 relief where the FI cannot exercise direct or indirect control over a system and cannot reasonably procure an alternative provider |

## Core obligations

### PDPA — protection and breach notification

| Provision | Requirement |
|---|---|
| s. 11 Accountability | Act as a reasonable person would; designate one or more individuals (data protection officer) responsible for compliance and publish business contact details |
| s. 12 Policies and practices | Develop, implement and communicate policies; complaints process; make information available on request |
| s. 24 Protection | "Reasonable security arrangements" against unauthorised access, collection, use, disclosure, copying, modification or disposal, and against loss of storage media or devices |
| s. 25 Retention | Cease retention when no longer necessary for business or legal purposes |
| s. 26 Transfer limitation | No transfer outside Singapore except under prescribed requirements ensuring comparable protection; PDPC may exempt |
| s. 26A–26B Notifiable breach | A data breach is notifiable if it results or is likely to result in **significant harm** to an affected individual, or is or is likely to be of **significant scale**. Breaches confined to within the organisation are deemed not notifiable |
| Regs 2021 r. 3–4 Deeming rules | Significant harm is deemed where the breach involves full name/alias or identification number plus prescribed data (Schedule Part 1), or an account identifier together with a password, security code, biometric or similar access data. Significant scale = **500 or more** affected individuals |
| s. 26C Assessment | On reason to believe a breach has occurred, assess notifiability "in a reasonable and expeditious manner"; data intermediaries must notify the controlling organisation "without undue delay". PDPC guidance sets an expected assessment window (commonly cited as 30 days — verify against the current PDPC breach-management guide) |
| s. 26D Notification | Notify the PDPC "as soon as is practicable, but in any case no later than **3 calendar days**" after assessing the breach as notifiable; then notify each affected individual where significant harm is likely, in any reasonable manner. Exceptions: remedial action or pre-existing technological measures (e.g. encryption) making significant harm unlikely; law-enforcement instruction or PDPC direction not to notify; PDPC waiver on application. Notification runs concurrently with any other statutory reporting duty |
| Regs 2021 r. 5–6 Content | PDPC notification: date and circumstances of awareness, chronology including the assessment, cause, number of individuals, data categories, potential harm, remediation, individual-notification plan, contact point; reasons and evidence for any late notification; grounds for not notifying individuals. Individual notification: circumstances, data affected, potential harm, remediation, self-help steps, contact point |

### Cybersecurity Act — CII owner duties (Part 3, mirrored in Parts 3A–3B)

| Provision | Requirement |
|---|---|
| s. 10 Information | Furnish design, configuration, security and operational information on notice |
| s. 12 Written directions | Comply with Commissioner's directions (general or specific), including on threat response and prescribed standards |
| s. 13 Change of ownership | Report changes in ownership of the CII |
| s. 14 Incident reporting | Report prescribed incidents affecting the CII, systems interconnected with or communicating with it, other owner-controlled systems, and **supplier-controlled systems interconnected with the CII**, plus any incident type the Commissioner directs; maintain detection mechanisms per the code of practice. Offence: fine up to S$100,000 and/or 2 years |
| Regs S 519/2018 r. 5 Reporting clock | Initial notification within **2 hours** of becoming aware; supplementary details (cause, impact, remediation) within **72 hours**; final incident report within **30 days** of the supplementary submission. Incidents on owner-controlled systems that are not interconnected with the CII and do not disrupt the essential service instead go into a consolidated quarterly report due by the third working day after quarter end; the full 2h/72h/30d cycle is then triggered if the incident becomes publicly observable, exploited a zero-day vulnerability, matched a Commissioner-notified advanced-persistent-threat indicator, or is suspected to be APT-related (r. 5(2A)–(2D)) |
| s. 15 Audits and risk assessments | Compliance audit by a Commissioner-approved auditor at least once every **2 years**; cybersecurity risk assessment at least **annually**; furnish reports within **30 days** of completion; Commissioner may order re-audit |
| s. 16 Exercises | Participate in CSA cybersecurity exercises when directed (fine up to S$100,000) |
| s. 35A Codes of practice | Comply with codes and standards of performance issued by the Commissioner (CCoP 2026 is binding under s. 35A(6)); non-compliance can be enforced by s. 12 direction |
| Part 3B STCC (s. 17F) | Same reporting structure as CII, including supplier-controlled interconnected systems; S 680/2025 r. 4 sets the same 2h/72h/30-day cycle |
| Part 4 Response powers (ss. 19–23) | CSA investigation and prevention powers scaled to incident severity; Minister may impose emergency cybersecurity measures |

### CCoP 2026 (issued and effective 29 July 2026; supersedes CCoP 2.0 of 4 July 2022)

- Sections: audit remediation (2), governance (3), identification (4), protection (5), detection (6), response and recovery (7), cyber resiliency (8), training and awareness (9), OT security (10), domain-specific practices incl. DNSSEC (11), securing CII-interconnected systems (12), Annex A enterprise-posture guidance.
- Compliance timeline for existing CII owners: new clauses (board accountability 3.1.4–3.1.5, senior management 3.2, asset management 4.1.2–4.1.4, monitoring 6.2.4, exercises 7.3.1–7.3.2, 7.3.7 and 7.3.10, section 12) by **29 July 2027**; Cyber Trust Mark certification (3.3) by **31 December 2027**.
- Governance: documented board-approved cyber resilience framework and risk appetite reviewed at least every 12 months (3.1.2); annual board cybersecurity training, new members within 12 months (3.1.3–3.1.4); board threat briefing at least every 6 months (3.1.5); cloud use does not shift accountability and the risk assessment must be submitted to the Commissioner (3.9); outsourcing management (3.10).
- Certification: CII owners must hold **Cyber Trust Mark Advocate (Tier 5)** or equivalent within 24 months of designation, scoped to enterprise-wide governance and systems (3.3.1–3.3.2); the s. 15 audit firm must itself be Tier 5 certified (3.3.3).
- Testing: penetration test of IT CII at least every 12 months and OT CII every 24 months, plus after major changes (5.15); red/purple-team attack simulation plan (5.16); threat-hunting reports to the Commissioner within 30 days of request (6.3.4); audit-finding remediation plan within 30 working days of the audit report (2.1.1).

### MAS — binding Notices and Guidelines

| Instrument | Requirement |
|---|---|
| FSM-N05 Technology Risk Management (banks; issued 9 May 2024, effective 10 May 2024, FSMA 2022 s. 29(1)) | Framework to identify critical systems; maximum unscheduled downtime per critical system **4 hours in any 12 months**; RTO of not more than **4 hours**, validated at least every 12 months; notify MAS "as soon as possible, but not later than **1 hour**" after discovering a relevant incident; **root cause and impact analysis report within 14 days** (executive summary, root cause, impact on compliance/operations/customers, remediation); IT controls protecting customer information |
| FSM-N06 Cyber Hygiene (banks; effective 10 May 2024) | Secure all administrative accounts; apply security patches within risk-commensurate timeframes and mitigate where none exists; written security standards for every system with conformance or compensating controls; network perimeter controls; malware protection on every system; **MFA** for administrative accounts on critical systems and for all accounts accessing customer information over the internet |
| Circular MAS/TCRS/2025/08 (16 Dec 2025) | From 1 Feb 2026 reportable incidents are submitted on MAS-Tx using the FSB FIRE-aligned template: initial notification within the statutory clock (review officer or 24-hour duty line), **Initial Incident Report within 24 hours** of discovery, **Final Incident Report within 14 days** |
| TRM Guidelines (18 Jan 2021) | Non-binding best practice across 15 chapters: board and senior management oversight, third-party services, risk framework, security-by-design and DevSecOps, IT service management, resilience and DR testing, access control, cryptography, data and infrastructure security, cyber security operations (threat intelligence, monitoring, incident response), cyber security assessment (vulnerability assessment, penetration testing, cyber exercises, adversarial attack simulation), online financial services, IT audit; staff training at least annually |
| Notice 658 (banks) / Notice 1121 (merchant banks), dated 11 Dec 2023, effective 11 Dec 2024 | Requirements on outsourced relevant services, focused on material services and services involving disclosure of customer information; register of all ongoing outsourced relevant services and of those involving disclosure of customer information, updated promptly and submitted to MAS semi-annually and on request (MAS template v1.1 from 11 Dec 2024) |
| Guidelines on Outsourcing (Banks) and (FIs other than Banks), dated Dec 2023, effective 11 Dec 2024 | Supervisory expectations on board and senior-management responsibility, risk evaluation, service-provider assessment, outsourcing agreements, sub-contracting and monitoring; for banks read with Notices 658/1121 and excluding the arrangements exempted in their Annex D |

## Enforcement and penalties

| Regime | Mechanism |
|---|---|
| PDPA (ss. 48I–48J) | PDPC directions (stop processing, destroy data, comply) and financial penalties for intentional or negligent contravention of Parts 3–6B: up to **10% of annual turnover in Singapore** where turnover exceeds S$10m (contraventions on or after 1 Oct 2022), otherwise **S$1m**; Part 9 (Do Not Call) penalties up to S$200,000 for individuals / S$1m otherwise |
| PDPA (s. 48O) | Private right of action for loss or damage directly resulting from a contravention of Parts 4–6B, exercisable once any PDPC decision is final |
| PDPA (ss. 48D–48F) | Individual offences for knowing or reckless unauthorised disclosure, use for gain/harm, or re-identification of anonymised data: fine up to S$5,000 and/or imprisonment up to 2 years |
| Cybersecurity Act | Criminal offences for failing to report incidents, comply with directions or participate in exercises (typically up to S$100,000 and/or 2 years; continuing daily fines of S$5,000 for some information failures); Commissioner directions; composition of offences (S 305/2022); appeals to the Minister via the Cybersecurity (Appeals) Regulations 2025 (S 679/2025) |
| MAS | Notices are legally binding under FSMA 2022 s. 29 / Banking Act s. 47A; breach exposes the FI to supervisory and enforcement action; Guidelines inform MAS's risk assessment of the institution |

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| 2 Jul 2014 | PDPA data protection provisions in force |
| 31 Aug 2018 | Cybersecurity Act 2018 in force, except ss. 24–35 and the Second Schedule (licensing), which commenced separately; Cybersecurity (Cybersecurity Service Providers) Regulations 2022 (S 304/2022) now govern licensing |
| 1 Sep 2018 / 4 Jul 2022 | CCoP 1.0 / CCoP 2.0 effective (Rev 1, 12 Dec 2022) |
| 18 Jan 2021 | MAS TRM Guidelines (current edition) published |
| 1 Feb 2021 | PDPA (Amendment) Act 2020 main commencement: mandatory breach notification (Part 6A) and the Notification of Data Breaches Regulations 2021 |
| 1 Oct 2022 | PDPA turnover-based financial penalty ceiling (s. 48J(3)) in force |
| 7 May / 23 May 2024 | Cybersecurity (Amendment) Bill passed / assented (Act 19 of 2024) |
| 10 May 2024 | MAS FSM-N03 to FSM-N26 TRM and Cyber Hygiene Notices take effect; legacy Notices 644/655 etc. cancelled |
| 11 Dec 2024 | MAS Notice 658/1121 and Guidelines on Outsourcing (Banks / FIs other than Banks) take effect |
| 22 Sep – 21 Oct 2025 | CSA consultation on the licensing framework for cybersecurity service providers |
| 31 Oct 2025 | Cybersecurity (Amendment) Act 2024 main commencement (Parts 3, 3A, 3B, virtual systems, supply-chain reporting, s. 35A); S 678/2025, S 679/2025 (appeals) and S 680/2025 regulations in operation |
| 1 Feb 2026 | MAS incident reports via MAS-Tx with revised template (Circular MAS/TCRS/2025/08) |
| 25 Feb 2026 | CSA closing note on the licensing consultation: Cyber Trust Promoter (Tier 3) or ISO/IEC 27001 required of licensees with a grace period to 31 Dec 2026; licence validity extended to 5 years; change-notification window widened from 14 to 30 calendar days; DPTM certification not mandated; revised licence conditions effective 30 days after publication |
| 6 Mar 2026 | MAS third-party risk management page records an open consultation on proposed Guidelines on Third-Party Risk Management |
| 13 Jul 2026 | Cybersecurity (Providers of Essential Service Responsible for Third-Party-Owned CII) Regulations 2026 in operation |
| 29 Jul 2026 | CCoP 2026 effective; new-clause compliance date 29 Jul 2027; Cyber Trust Mark deadline 31 Dec 2027 |
| Pending | Commencement of Cybersecurity Act Parts 3C (ESCI), 3D (major FDI providers) and the Third Schedule; commencement of PDPA Part 6B (data portability); final MAS Guidelines on Third-Party Risk Management |

## Key obligations for security/GRC teams

1. **Determine which regimes bite**: PDPA (almost everyone), CII designation notice, STCC designation, MAS licence category and its FSM-N pair. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Build a three-clock incident playbook**: PDPC 3 calendar days from assessment; CSA 2h/72h/30d; MAS 1 hour, 24-hour initial report and 14-day final report via MAS-Tx — with pre-drafted content matching Regs 2021 r. 5 and the CSA/MAS templates. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
3. **Encode the PDPA deeming rules** (identifier plus Schedule data; credentials; 500 individuals) into breach triage so notifiability is decided quickly and documented; log every assessment with the [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
4. **Evidence "reasonable security arrangements"** under s. 24 with a risk-based control set mapped to ISO/IEC 27001 or NIST CSF 2.0; PDPC enforcement turns on documented, tested controls rather than policy text. See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md) and [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md).
5. **CII owners**: run the s. 15 cycle (annual risk assessment, biennial approved audit, 30-day report submission), remediation plans within 30 working days, annual IT / biennial OT penetration testing, and the Cyber Trust Mark Tier 5 programme before 31 Dec 2027. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md) and [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).
6. **Extend incident detection and contracts to suppliers**: s. 14(1)(bb) makes supplier-controlled systems interconnected with CII reportable, and MAS Notice 658 requires a register and controls for material outsourcing — align vendor due diligence, contractual reporting clauses and the outsourcing register. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
7. **Financial institutions**: prove 4-hour RTO validation and downtime tracking for critical systems, FSM-N06 hygiene controls (admin-account security, patching, baselines, perimeter, anti-malware, MFA), and TRM Guidelines assessments (VA, PT, cyber exercises, adversarial simulation). See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).
8. **Board reporting**: CCoP 2026 requires a board cyber risk appetite, annual training and six-monthly threat briefings with minuted decisions; MAS expects board and senior-management ownership of technology risk. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md) and [../../templates/grc-board-report.md](../../templates/grc-board-report.md).
9. **Horizon-scan** the commencement of Parts 3C/3D, the revised cybersecurity service provider licence conditions (Tier 3 certification by 31 Dec 2026), MAS third-party risk guidelines and CCoP releases. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

- **PDPA vs GDPR**: both are extraterritorial, but PDPA's breach trigger is a harm/scale test with deemed categories rather than GDPR's risk-based 72-hour rule, and the PDPA clock starts at the organisation's assessment rather than awareness. Multinationals handling EU and Singapore data need parallel decision logs; see [gdpr.md](gdpr.md) and [eu-gdpr-international-transfers.md](eu-gdpr-international-transfers.md) for transfer mechanics that must be reconciled with PDPA s. 26.
- **Cybersecurity Act vs NIS2 / CER**: designation-based like NIS2's essential entities but narrower (named systems, not whole entities), with faster clocks (2 hours vs NIS2's 24-hour early warning) and explicit cloud/virtual-system and offshore reach; see [nis2.md](nis2.md) and [eu-cer-directive.md](eu-cer-directive.md).
- **MAS vs DORA / APRA CPS 234**: MAS Notices set hard availability and reporting numbers (4-hour RTO, 1-hour notification) where DORA relies on RTS thresholds; MAS's outsourcing register parallels DORA's register of information. Banks operating in the EU or Australia should maintain one incident taxonomy mapped to all three; see [dora.md](dora.md) and [australia-apra-cps-234-230.md](australia-apra-cps-234-230.md).
- **PDPA and MAS overlap**: a customer-data breach at a bank is a PDPC notifiable breach (3 days) and a MAS relevant incident (1 hour) simultaneously; s. 26D(9) makes the duties concurrent.
- **CII and Cyber Trust Mark**: CCoP 2026 converts a voluntary CSA certification into a mandatory baseline for CII owners and their auditors, extending regulatory expectations to the whole enterprise environment, not just designated systems.
- Regional overview: [other-jurisdictions.md](other-jurisdictions.md); comparable Asia-Pacific regime: [japan-appi-cyber.md](japan-appi-cyber.md).

## Primary sources

- Personal Data Protection Act 2012 (2020 Rev. Ed., informal consolidation in force from 5 Dec 2025), Singapore Statutes Online: https://sso.agc.gov.sg/Act/PDPA2012 (legal text)
- Personal Data Protection (Notification of Data Breaches) Regulations 2021 (S 64/2021): https://sso.agc.gov.sg/SL/PDPA2012-S64-2021 (legal text)
- Cybersecurity Act 2018 (2020 Rev. Ed., informal consolidation in force from 31 Oct 2025): https://sso.agc.gov.sg/Act/CA2018 (legal text)
- Cybersecurity (Amendment) Act 2024 (Act 19 of 2024), Acts Supplement: https://sso.agc.gov.sg/Acts-Supp/19-2024 (legal text)
- Cybersecurity (Provider-Owned Critical Information Infrastructure) Regulations 2018 (S 519/2018, as amended by S 678/2025): https://sso.agc.gov.sg/SL/CA2018-S519-2018 (legal text)
- Cybersecurity (Cybersecurity Service Providers) Regulations 2022 (S 304/2022) and Cybersecurity (Composition of Offences) Regulations 2022 (S 305/2022): https://sso.agc.gov.sg/SL/CA2018-S304-2022 and https://sso.agc.gov.sg/SL/CA2018-S305-2022 (legal text)
- Cybersecurity (Appeals) Regulations 2025 (S 679/2025): https://sso.agc.gov.sg/SL/CA2018-S679-2025 (legal text)
- Personal Data Protection (Amendment) Act 2020 (Act 40 of 2020), which inserted Parts 6A and 6B: https://sso.agc.gov.sg/Acts-Supp/40-2020 (legal text)
- Cybersecurity (Systems of Temporary Cybersecurity Concern) Regulations 2025 (S 680/2025): https://sso.agc.gov.sg/SL/CA2018-S680-2025 (legal text)
- Cybersecurity (Providers of Essential Service Responsible for Cybersecurity of Third-Party-Owned CII) Regulations 2026 (S 490/2026): https://sso.agc.gov.sg/SL/CA2018-S490-2026 (legal text)
- CSA, Cybersecurity Act overview: https://www.csa.gov.sg/legislation/cybersecurity-act/ (regulator guidance)
- CSA, Codes of Practice page and Cybersecurity Code of Practice for Critical Information Infrastructure 2026 (PDF, 29 Jul 2026): https://www.csa.gov.sg/legislation/codes-of-practice/ (regulator code)
- CSA, Cyber Essentials and Cyber Trust mark pages: https://www.csa.gov.sg/our-programmes/support-for-enterprises/sg-cyber-safe-programme/cybersecurity-certification-for-organisations/ (regulator guidance)
- CSA, Closing Note to the Consultation on the Licensing Framework for Cybersecurity Service Providers (25 Feb 2026): https://www.csa.gov.sg/legislation/consultations/closing-note-to-the-consultation-on-the-licensing-framework-for-cybersecurity-service-providers/ (regulator decision)
- MAS Notice FSM-N05 Technology Risk Management and FSM-N06 Cyber Hygiene (banks): https://www.mas.gov.sg/regulation/notices/notice-fsm-n05 and https://www.mas.gov.sg/regulation/notices/notice-fsm-n06 (binding notices)
- MAS, Cyber Security regulation page (FSM-N03 to FSM-N26 mapping table): https://www.mas.gov.sg/regulation/cyber-security (regulator guidance)
- MAS Guidelines on Risk Management Practices – Technology Risk (18 Jan 2021): https://www.mas.gov.sg/regulation/guidelines/technology-risk-management-guidelines (regulator guidance)
- MAS Circular MAS/TCRS/2025/08 on Financial Institution Incident Reporting (16 Dec 2025): https://www.mas.gov.sg/regulation/circulars/circular-on-financial-institution-incident-reporting (regulator guidance)
- MAS Guidelines on Outsourcing (Banks), Dec 2023, effective 11 Dec 2024: https://www.mas.gov.sg/regulation/guidelines/guidelines-on-outsourcing-banks (regulator guidance)
- MAS Notice 658 and Third-Party Risk Management page (outsourcing notices, guidelines and 2026 consultation): https://www.mas.gov.sg/regulation/notices/notice-658 and https://www.mas.gov.sg/regulation/third-party-risk-management (binding notice / regulator guidance)
- PDPC, Data Breach Management Guide landing page: https://www.pdpc.gov.sg/organisations/resources/guidance-by-topic/data-breach-management-guide (regulator guidance) — the guide itself could not be retrieved in text form during this review, so the 30-day assessment expectation is marked (verify) above.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
