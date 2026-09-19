# US transportation cybersecurity — TSA security directives (pipeline, rail, aviation), the Surface Cyber Risk Management NPRM, and the Coast Guard maritime cyber rule (33 CFR Part 101 Subpart F)

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | (1) TSA Security Directives (SDs) issued under 49 U.S.C. 114(l)(2)(A) without notice-and-comment: SD Pipeline-2021-01 and -02 series, SD 1580-21-01 / 1582-21-01 series, SD 1580/82-2022-01 series; (2) TSA emergency amendments to aviation security programs (March 2023); (3) NPRM "Enhancing Surface Cyber Risk Management", 89 FR 88488 (7 Nov 2024), RIN 1652-AA74; (4) Coast Guard final rule "Cybersecurity in the Marine Transportation System", 90 FR 6298 (17 Jan 2025), codified at 33 CFR 101.600–101.670 |
| Regulators | TSA (DHS) for pipeline, rail, transit, bus and aviation; CISA receives TSA-mandated incident reports; U.S. Coast Guard (DHS) for vessels, port facilities and OCS facilities, with reports to the National Response Center (NRC) |
| Status (Sept 2026) | SDs renewed annually and still in force — current versions: SD Pipeline-2021-01G and SD 1580-21-01E / 1582-21-01E (16 Jan 2026 – 15 Jan 2027); SD Pipeline-2021-02G and SD 1580/82-2022-01E (3 May 2026 – 2 May 2027). Surface NPRM comment period closed 5 Feb 2025; final rule "to be determined" and listed as a long-term action in the 2026 Unified Agenda. Coast Guard rule effective 16 Jul 2025 with phased deadlines to 16 Jul 2027 |
| Who is covered | TSA-designated "critical" hazardous liquid / natural gas pipelines and LNG facilities (the "top 100" population under 6 U.S.C. 1207(b)); freight railroads under 49 CFR 1580.101 plus TSA-designated freight and passenger railroads / rail transit; TSA-regulated airport and aircraft operators (aviation EA); owners/operators of U.S.-flagged vessels, facilities and OCS facilities that must hold a security plan under 33 CFR parts 104–106 (maritime) |
| Core model | Cybersecurity Coordinator / Cybersecurity Officer; incident reporting on a fixed clock; incident response plan exercised annually; TSA-approved Cybersecurity Implementation Plan (CIP) with four security outcomes (segmentation, access control, monitoring, patching); annual Cybersecurity Assessment Plan (CAP) with architecture design review and one-third-per-year testing; maritime Cybersecurity Plan approved by the Coast Guard |
| Incident clocks | TSA SDs: report to CISA "as soon as practicable, but no later than 72 hours" after identifying a cybersecurity incident (earlier SD versions required 24 hours; the NPRM still proposes 24 hours). Maritime: report reportable cyber incidents "without delay" to the NRC (or "immediately" under 33 CFR 6.16-1 to FBI, CISA and the Captain of the Port) |
| Penalties | TSA civil penalties per 49 CFR 1503.401: $14,602 per violation, up to $73,011 (individual / small business) or $584,078 (other persons) per civil penalty action for surface modes; aviation-related violations $17,062 or $42,657 per violation up to $1,200,000 per action. Coast Guard: civil penalty under 46 U.S.C. 70119 for MTSA violations (33 CFR 101.415(b); inflation-adjusted maximum $43,527 per 33 CFR 27.3) |
| Certifiable? | No. Compliance is evidenced by TSA plan approvals, inspections and records; Coast Guard plan approval by COTP / OCMI / Marine Safety Center, drills, exercises and inspections |
| Neighbours | CISA's CIRCIA reporting rule (72-hour incident / 24-hour ransom-payment reporting, per the NPRM's description); NIST CSF and CISA Cross-Sector Cybersecurity Performance Goals (the stated basis of the NPRM); PHMSA pipeline safety rules (49 CFR parts 192/195); SEC cyber disclosure for listed operators |

## What it is

After the 2021 Colonial Pipeline ransomware incident (the NPRM cites the federal response to it), TSA moved from voluntary pipeline guidelines to mandatory security directives: SD Pipeline-2021-01 (first effective 28 May 2021) imposed a Cybersecurity Coordinator, incident reporting to CISA and a vulnerability assessment; SD Pipeline-2021-02 (July 2021) added prescriptive mitigation measures, then was rewritten as performance-based in SD Pipeline-2021-02C (effective 27 July 2022). TSA extended the same two-tier model to higher-risk freight railroads and passenger/transit rail (SD 1580-21-01 and 1582-21-01, effective 31 Dec 2021; SD 1580/82-2022-01, 18 Oct 2022) and, by emergency amendment, to certain airport and aircraft operators (7 Mar 2023). Each SD series is renewed roughly annually and must be ratified by the Transportation Security Oversight Board (TSOB) within 90 days unless the TSOB has pre-authorised extension.

Because SDs are emergency instruments, TSA is codifying them: an ANPRM (30 Nov 2022) and the NPRM "Enhancing Surface Cyber Risk Management" (7 Nov 2024) would create permanent Cyber Risk Management (CRM) program requirements in 49 CFR parts 1580, 1582, 1584 and a new part 1586. In parallel, the Coast Guard finalised the first binding cybersecurity requirements for the maritime sector under MTSA authority (33 CFR Part 101 Subpart F), replacing the guidance-only approach of NVIC 01-20 and the vessel work instruction CVC-WI-027.

## Who it covers / Scope

| Population | Applicability test | Source |
|---|---|---|
| Critical pipelines and LNG facilities | Owner/operators "notified by TSA that their pipeline system or facility is critical" — criticality based on volume transported, service to other critical sectors, etc. (the 100 most critical pipeline operators reviewed under 9/11 Act §1557(b)). TSA notifies newly designated operators and sets bespoke compliance deadlines. Requirements apply to the operator's **Critical Cyber Systems** (any IT/OT system or data whose compromise could result in operational disruption, including business services); an operator with none must tell TSA in writing within 60 days | SD Pipeline-2021-01G / -02G |
| Freight railroads | Each freight railroad carrier identified in 49 CFR 1580.101 plus other TSA-designated freight railroads; SD 1580/82-2022-01 adds TSA-designated passenger railroads notified on a risk basis | SD 1580-21-01E, SD 1580/82-2022-01E |
| Public transportation and passenger rail | TSA-specified higher-risk rail transit and passenger railroads (SD 1582-21-01 series); all other surface operators received the voluntary Information Circulars IC-2021-01 and IC Surface-2025-01 | TSA ICR notices, April and Sept 2026 |
| Aviation | "Certain TSA-regulated airport and aircraft operators" via emergency amendments to their security programs (referred to in the NPRM as Joint EA 23-01) | TSA press release 7 Mar 2023; NPRM |
| Proposed CRM rule | 73 freight railroads (Class I; Class II/III railroads that switch for two or more Class I railroads, host covered operations, or serve as STRACNET links); 34 rail transit / passenger railroads (Amtrak; passenger railroads with ≥5,000 average daily unlinked trips; rail transit with ≥50,000); 115 of ~2,105 PHMSA-regulated pipeline facilities/systems; incident-reporting only for 71 over-the-road bus (OTRB) operators. All freight and PTPR operators that already need a security coordinator would need a Cybersecurity Coordinator and CISA reporting | NPRM section III.C |
| Maritime | Owners/operators of U.S.-flagged vessels, facilities and OCS facilities required to have a VSP/FSP/OCS FSP under 33 CFR parts 104, 105, 106. **Foreign-flagged vessels are excluded** (33 CFR 101.605(b)); the rule preempts conflicting state law for part 105 facilities (101.610) | 33 CFR 101.605 |

Managed security service providers and "authorized representatives" may perform SD measures, but the owner/operator retains sole responsibility for compliance, and authorized representatives are jointly liable for their own non-compliance.

## Core obligations

### 1. TSA "Enhancing … Cybersecurity" SDs (SD Pipeline-2021-01G, SD 1580-21-01E, SD 1582-21-01E)

| Requirement | Detail (current 2026 versions) |
|---|---|
| Cybersecurity Coordinator | Primary and at least one alternate at corporate level; at least one must be a U.S. citizen eligible for a security clearance who is the primary contact for intelligence that cannot be shared with non-U.S. persons; **new Jan 2026:** any non-U.S. citizen coordinator must hold current NEXUS, Global Entry or a TSA-recognised equivalent, with the programme number filed with TSA. Coordinator accessible to TSA and CISA 24x7; contact details updated within 7 days of any change |
| Incident reporting | Report to CISA (cisa.gov/report or 844-729-2472) unauthorised access, malware discovery, denial of service, physical attack on network infrastructure, or any incident that results or could result in operational disruption — "as soon as practicable, but no later than 72 hours" after identification, with supplemental information within 24 hours of becoming available. The report must state it is made under the SD and describe systems affected, dates of compromise and detection, indicators, impact and planned response. The clock was 12 hours when first issued in 2021 and 24 hours from May 2022 (per the NPRM); the shift to 72 hours occurred in a 2025 renewal (verify exact version) and is reflected in TSA's 2026 information-collection notices. IC Surface-2025-01 recommends earlier voluntary notification to TSA |
| Incident response plan | Develop and maintain an up-to-date Cybersecurity Incident Response Plan (CIRP) to reduce the risk of operational disruption |
| Vulnerability assessment | One-time assessment on the TSA form (pipeline: against Section 7 of the 2018 Pipeline Security Guidelines with Change 1; rail: a form structured on NIST CSF functions/categories), identifying gaps and remediation timelines. TSA's Sept 2026 ICR notes the rail population has already satisfied this and expects fewer than 10 new respondents a year |

### 2. TSA "Mitigation Actions, Contingency Planning and Testing" SDs (SD Pipeline-2021-02G, SD 1580/82-2022-01E)

| Element | Requirement |
|---|---|
| Cybersecurity Implementation Plan (CIP) | TSA-approved plan describing the measures and the schedule for achieving four outcomes on Critical Cyber Systems: (a) **network segmentation** so OT keeps operating if IT is compromised and vice versa — inventory of IT/OT interdependencies, all external OT connections, zone boundaries and boundary controls; (b) **access control** — password-reset schedule (with documented mitigations for components that cannot comply), MFA or compensating controls of equivalent risk mitigation (pipeline control-room workstations under 49 CFR parts 192/195 need documented compensating controls if MFA is not applied), least privilege and separation of duties, restricted shared accounts, review of domain trust relationships; (c) **continuous monitoring and detection**, including the ability to isolate ICS when an IT incident threatens OT; (d) **patching** of OS, applications, drivers and firmware under a risk-based methodology, with documented mitigations and timelines where patches cannot be applied without severe operational degradation. A request to amend an approved CIP must be filed with TSA no later than 50 days after a permanent change (one intended to last 45 or more days) takes effect, or after a change of ownership/control; denials may be petitioned within 30 days |
| CIRP | Maintained and exercised **at least annually**; each exercise must test at least two plan objectives and involve the personnel named (by position) in the plan; plan must set out isolation capability and governance |
| Cybersecurity Assessment Plan (CAP) | Submitted annually to TSA **for approval**; assesses the effectiveness of the approved CIP; includes a **cybersecurity architecture design review at least every two years** (rail: within 12 months of CIP approval, then biennially) covering network-traffic verification and log analysis; incorporates penetration testing and red/purple-team testing; schedule must assess **at least one-third of CIP policies, procedures, measures and capabilities each year, 100% over any three-year period**. Rail: initial CAP due 60 days after CIP approval |
| Annual CAP report | Report of assessment methods used and results for the previous 12 months, due to TSA no later than 12 months after TSA's approval of the most recent CAP (also provided to corporate leadership per the NPRM's description) |
| Records | Keep documentation establishing compliance, available to TSA on request; submissions are Sensitive Security Information under 49 CFR part 1520 |

### 3. Aviation emergency amendment (7 March 2023)

TSA amended, on an emergency basis, the security programs of certain airport and aircraft operators to require the same four outcomes: network segmentation policies protecting OT if IT is compromised, access control for critical cyber systems, continuous monitoring and detection, and risk-based patching. The amendment text itself is not public; obligations flow through each operator's approved security program.

### 4. Proposed permanent CRM program (NPRM, 89 FR 88488)

| Proposed element | Content |
|---|---|
| Governance | Named **accountable executive** (senior, distinct from day-to-day IT/OT management) plus Cybersecurity Coordinator(s); TSA sought comment on requiring a security threat assessment for both |
| Cybersecurity evaluation | Annual enterprise-wide current-profile vs target-profile evaluation (NIST CSF style); a vulnerability assessment completed within the prior year may serve as the initial evaluation |
| Cybersecurity Operational Implementation Plan (COIP) | Defence-in-depth plan (physical and logical controls) identifying Critical Cyber Systems, network architecture and baseline communications, protective measures, detection/monitoring, response and recovery; includes a Plan of Action and Milestones for gaps; once approved it becomes a TSA-approved security program (proposed 49 CFR 1580.307, 1582.207, 1586.207) |
| Cybersecurity Assessment Plan | Annual assessment/audit schedule (one-third per year), annual report, unaddressed vulnerabilities, independent assessors (proposed 1580.329, 1582.229, 1586.229) |
| Incident reporting | Mirrors the SDs as they stood in 2024: report to CISA **within 24 hours** of identification (proposed 1580.325, 1582.225, 1584.107, 1586.225); TSA said it would revisit against the final CIRCIA rule |
| Supply chain | Supply-chain incident reporting in procurement documents and contracts, following CISA CPG 1.G (proposed 1580.315, 1582.215, 1586.215) |
| Procedure | Would add SD/IC issuance procedures for surface modes mirroring aviation, and require notice to TSA within 24 hours of temporary substantive changes to an approved program |

### 5. Coast Guard maritime cybersecurity rule (33 CFR 101.600–101.670)

| Section | Requirement |
|---|---|
| 101.620 Owner/operator | Ensure a Cybersecurity Plan is developed, approved and maintained; designate in writing a **Cybersecurity Officer (CySO)** reachable by the Coast Guard 24x7; ensure exercises, audits, inspections and the Cybersecurity Assessment occur; develop and execute a Cyber Incident Response Plan; report all reportable cyber incidents to the NRC unless already reported under 33 CFR 6.16-1 |
| 101.625 CySO | May cover multiple assets and hold other roles; ensures annual audit of the Plan, drills/exercises, training, records, incident recording and reporting, submission of Plan amendments, and identification and mitigation of all KEVs in critical IT/OT systems "without delay"; 12 qualification areas |
| 101.630 Cybersecurity Plan | 14 mandated sections (organisation, training, drills, records, communications, systems and maintenance, access control, physical security of IT/OT, monitoring, audits/amendments, audit reports, unresolved vulnerabilities including risk-accepted ones, incident reporting procedures, Cybersecurity Assessment); submitted to COTP/OCMI (facilities) or Marine Safety Center (vessels) for approval; may sit inside, annexed to, or separate from the VSP/FSP/OCS FSP or an Alternative Security Program; at least 60 days to submit amendments curing deficiencies; treated as SSI under 49 CFR part 1520 |
| 101.635 Drills and exercises | Drills **at least twice per calendar year**; exercises **at least once per calendar year, no more than 18 months apart** (full-scale, tabletop or combined), with active CySO participation and documented corrective actions |
| 101.650 Measures | Account security (auto lockout, default-password change, password strength, **MFA** on password-protected IT and remotely accessible OT or documented compensating controls, least privilege, separate credentials on critical systems, credential revocation on departure); device security (approved hardware/firmware/software list, executable code disabled by default on critical systems, inventory of network-connected systems, network map and OT configuration documentation); data security (protected logs, encryption where feasible); training (all personnel with IT/OT access including contractors; new personnel within 5 days of access and no later than 30 days of hire; annually); risk management (annual Cybersecurity Assessment, **penetration test at each Plan renewal** with a CySO letter listing vulnerabilities, KEV patching or compensating controls without delay, vulnerability scanning, no OT on the public internet without documented justification, no exploitable channels exposed to internet-accessible systems); supply chain (cyber capability as procurement criterion, vendor vulnerability/incident notification without delay, monitoring of third-party remote connections); resilience (Cyber Incident Response Plan, annual validation, protected and tested backups); network segmentation between IT and OT with logged, monitored connections; physical security of OT/HMIs and blocking of unused ports |
| 101.665 | Waivers and equivalence determinations available after the Cybersecurity Assessment; temporary deviations notified to the COTP |

Compliance dates (101.650(d)(4), 101.650(e)(1), 101.655): incident reporting from **16 Jul 2025**; all training topics by **12 Jan 2026**, then annually; Cybersecurity Assessment, CySO designation and Cybersecurity Plan submission by **16 Jul 2027**; Plan-specific training within 60 days of Plan approval. The Coast Guard invited comment (to 18 Mar 2025) on a possible 2-to-5-year delay for U.S.-flagged vessels; no delay rule was located in the Federal Register as of September 2026 (verify before relying on the vessel deadlines). MARSEC Directives 105-4 (Feb 2024) and 105-5 (Nov 2024) impose additional, non-public cyber risk-management actions for PRC-manufactured ship-to-shore cranes.

## Enforcement and penalties

- **TSA** enforces through plan approval/disapproval, inspections, records review and civil penalty actions under 49 CFR part 1503. Maximum amounts (as adjusted 29 Dec 2025): surface and other non-aviation violations $14,602 per violation, capped per civil penalty action at $73,011 for individuals and small businesses and $584,078 for other persons; aviation-related violations $17,062 per violation (up to $100,000 for individuals/small businesses, $1,200,000 for others) and $42,657 per violation (up to $1,200,000) for operators carrying passengers or property for compensation. Operators may request alternative measures; SD comments do not delay effectiveness.
- **Coast Guard** enforces through COTP/OCMI/MSC plan approval, inspections and drills; 33 CFR 101.415(b) makes non-compliance with any MTSA subchapter requirement, including a MARSEC Directive, subject to a civil penalty under 46 U.S.C. 70119 (statutory text $25,000; inflation-adjusted maximum $43,527 per violation, $78,210 for continuing violations, per 33 CFR 27.3), with criminal exposure under 46 U.S.C. 70036/70052 for violations of 101.405 orders.
- Information reported under the SDs is shared between TSA and CISA (PPD-41) and protected as SSI; it may feed anonymised indicators and trend analysis.

## Timeline and status

| Date | Event |
|---|---|
| 28 May 2021 | SD Pipeline-2021-01 first effective (coordinator, 12-hour reporting, vulnerability assessment) |
| Jul 2021 | SD Pipeline-2021-02 first issued (19 Jul per the NPRM; the current SD text says 26 Jul — verify) with prescriptive mitigations; May 2022 reporting clock moved to 24 hours; 27 Jul 2022 SD Pipeline-2021-02C makes measures performance-based |
| 31 Dec 2021 | SD 1580-21-01 and SD 1582-21-01 effective for higher-risk rail; IC-2021-01 issued for others |
| 18 Oct 2022 | SD 1580/82-2022-01 (rail CIP/CAP model) |
| 30 Nov 2022 | ANPRM on surface cyber risk management (87 FR 73527) |
| 7 Mar 2023 | Aviation emergency amendments to airport and aircraft operator security programs |
| Jul/Oct 2023 | Cybersecurity Assessment *Program* renamed Assessment *Plan* and made subject to TSA approval (pipeline then rail) |
| 7 Nov 2024 | NPRM "Enhancing Surface Cyber Risk Management" (89 FR 88488); comments closed 5 Feb 2025 |
| 17 Jan 2025 | Coast Guard final rule (90 FR 6298); DHS notice of TSOB ratification of SD Pipeline-2021-01D and -02E |
| 3 May 2025 | SD Pipeline-2021-01E, SD Pipeline-2021-02F, SD 1580/82-2022-01D |
| 16 Jul 2025 | Maritime rule effective; NRC incident reporting begins |
| 22 Oct 2025 | SD 1580-21-01D, SD 1582-21-01D, SD Pipeline-2021-01F |
| 12 Jan 2026 | Maritime training deadline |
| 16 Jan 2026 | SD Pipeline-2021-01G, SD 1580-21-01E, SD 1582-21-01E (adds NEXUS/Global Entry vetting for non-U.S. citizen coordinators); run to 15 Jan 2027 |
| 3 May 2026 | SD Pipeline-2021-02G and SD 1580/82-2022-01E — no substantive changes; run to 2 May 2027 |
| Aug–Sept 2026 | 2026 Unified Agenda lists the surface CRM final rule as "to be determined" (long-term action); TSA ICR revisions (OMB 1652-0074 approved through 31 Aug 2026; 1652-0056 renewal sought) confirm the SD regime continues |
| 16 Jul 2027 | Maritime Cybersecurity Assessment, CySO designation and Cybersecurity Plan submission deadline |

Pending: the surface final rule (timing unknown); any Coast Guard delay rule for U.S.-flagged vessels; the interaction with CISA's CIRCIA rule (see the CIRCIA context pack when available).

## Key obligations for security/GRC teams

1. **Establish applicability per asset and mode** — TSA designation letters, 49 CFR 1580.101 status, MTSA security-plan status, foreign-flag exclusions — and record the governing SD version and expiry in the obligations register. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Inventory and defend the Critical Cyber System / critical IT-OT determination**: it scopes every SD measure, and TSA or the CySO can override it. Keep the methodology and the 60-day "no critical systems" notice evidence.
3. **Run the reporting clock as a playbook**: 72 hours to CISA under the SDs (24 hours if the NPRM is finalised unchanged), "without delay" to the NRC for maritime, plus CIRCIA and SEC 8-K clocks for listed operators. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
4. **Treat the CIP/COIP and Cybersecurity Plan as approved security programs**: change control that files CIP amendment requests within 50 days of a permanent change and obtains Coast Guard approval before amending the Cybersecurity Plan; map the four TSA outcomes and the 101.650 measures to your control set. See [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md) and [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md).
5. **Build the assessment calendar**: annual CAP approval and report, architecture design review every 2 years, one-third-per-year coverage, maritime annual assessment, biannual drills, annual exercises, penetration test at Plan renewal. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
6. **Exercise the incident response plan annually** with at least two objectives and named positions participating; retain attendance and after-action records.
7. **Document compensating controls formally** where MFA, patching or password resets are infeasible on OT — both regimes accept them only if documented with timelines. See [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
8. **Flow obligations to MSSPs, authorized representatives and vendors** (SD joint liability; 33 CFR 101.650(f) vendor notification and third-party remote-connection monitoring). See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
9. **Vet coordinators**: U.S.-citizen primary contact eligible for clearance; trusted-traveller membership for any non-U.S. citizen coordinator; 24x7 reachability for both TSA and Coast Guard roles.
10. **Track the rulemakings** (surface final rule, vessel delay, CIRCIA) as horizon items with owners. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

- **CIRCIA (CISA)**: the NPRM acknowledges a 72-hour covered-incident / 24-hour ransom-payment rule and that two federal reporting duties may coexist; the SDs' move to 72 hours narrows the gap, but the proposed rule text still says 24 hours. Report content should be drafted once and filed to both.
- **SEC cyber disclosure**: listed pipeline, rail and shipping operators must run the Item 1.05 materiality analysis in parallel with CISA/NRC reporting; see [sec-cyber-disclosure.md](sec-cyber-disclosure.md).
- **NIST CSF 2.0 and CISA CPGs**: the NPRM's evaluation is a CSF current-vs-target profile and its governance and supply-chain elements cite CPG 1.B and 1.G; the maritime measures track the CPGs closely. See [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md) and [../frameworks/nist-800-53.md](../frameworks/nist-800-53.md).
- **PHMSA / FAA / IMO**: PHMSA safety rules (49 CFR 192/195) define the control rooms the SDs reference and the population the NPRM counts; the FAA proposed "Equipment, Systems, and Network Information Security Protection" rules for aircraft and engines (89 FR 67564, 21 Aug 2024; no final rule located — verify); the Coast Guard defers foreign-flagged vessels to IMO instruments (MSC-FAL.1/Circ.3, Resolution MSC.428(98)) under ISM Code safety management systems.
- **Comparable regimes abroad**: EU NIS2 lists transport (air, rail, water, road) as a sector of high criticality and Australia's SOCI Act covers transport assets; see [nis2.md](nis2.md) and [australia-soci-cyber-security-act.md](australia-soci-cyber-security-act.md).

## Primary sources

- TSA, Security Directives and Emergency Amendments index (tsa.gov/sd-and-ea) — lists all cybersecurity SD versions with issue dates.
- SD Pipeline-2021-01G with transmittal memo (tsa.gov, PDF, 9 Jan 2026) — legal text.
- SD Pipeline-2021-02G with transmittal memo (tsa.gov, PDF, 1 May 2026) — legal text.
- SD 1580-21-01E with transmittal memo (tsa.gov, PDF, Jan 2026) — legal text.
- SD 1580/82-2022-01E with transmittal memo (tsa.gov, PDF, 1 May 2026) — legal text.
- TSA press release, "TSA issues new cybersecurity requirements for airport and aircraft operators", 7 Mar 2023 — regulator statement (the emergency amendment itself is not public).
- Federal Register, NPRM "Enhancing Surface Cyber Risk Management", 89 FR 88488, 7 Nov 2024 (federalregister.gov/d/2024-24704) — proposed rule and SD history.
- Federal Register, DHS "Ratification of Security Directives", 90 FR 5491, 17 Jan 2025 — TSOB ratification and SD chronology.
- Federal Register, TSA information-collection notices 91 FR 20475 (16 Apr 2026) and 91 FR 56154 (1 Sept 2026) on OMB 1652-0074, and 91 FR 149 (2 Jan 2026) on OMB 1652-0056 — current SD requirements, 72-hour clock, Jan 2026 revision.
- reginfo.gov Unified Agenda entry, RIN 1652-AA74 (Spring 2025 and 2026 editions) — rulemaking status.
- Federal Register, Coast Guard final rule "Cybersecurity in the Marine Transportation System", 90 FR 6298, 17 Jan 2025 (federalregister.gov/d/2025-00708) — legal text and preamble.
- eCFR, 33 CFR Part 101 Subpart F (101.600–101.670), 33 CFR 101.415, 33 CFR 27.3, 33 CFR 6.16-1; 49 CFR 1503.401 — current codified text.
- Federal Register, Coast Guard notice of MARSEC Directive 105-5, 89 FR 91413, 19 Nov 2024 — regulator notice.
- Not fetched: tsa.gov industry landing pages returned access errors to scripted requests; the 2022 rail and 2025 pipeline renewal press releases were not located.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
