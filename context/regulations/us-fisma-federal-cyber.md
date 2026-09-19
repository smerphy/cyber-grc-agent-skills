# US Federal Government Cybersecurity — FISMA 2014, OMB Circular A-130, CISA Directives and Executive Orders

## At a glance

| Attribute | Detail |
|---|---|
| Core statute | Federal Information Security Modernization Act of 2014 (FISMA), Pub. L. 113-283 (enacted 18 Dec 2014), codified at 44 U.S.C. §§ 3551–3558; replaced the 2002 FISMA subchapters. Minor amendments 2015 (emergency directives) and 2018 (supply-chain duties, Pub. L. 115-390) |
| Policy layer | OMB Circular A-130 *Managing Information as a Strategic Resource* (2016 revision; Appendix I security/RMF responsibilities, Appendix II PII/privacy program); annual OMB FISMA guidance memoranda (latest located: M-25-04, 15 Jan 2025); topic memoranda (M-22-09 zero trust, M-26-05 software/hardware security, M-26-14 logging, M-26-15 post-quantum cryptography) |
| Standards layer | NIST under 40 U.S.C. § 11331: FIPS 199 (Feb 2004) categorization, FIPS 200 (Mar 2006) minimum requirements, SP 800-53 Rev. 5 (Sept 2020; Release 5.2.0, 27 Aug 2025), SP 800-37 Rev. 2 RMF (Dec 2018) |
| Operational layer | DHS/CISA Binding Operational Directives (§ 3553(b)(2)) and Emergency Directives (§ 3553(h)); CISA Federal Incident Notification Guidelines (effective 1 Apr 2017); CDM programme and CyberScope reporting |
| Who is covered | Federal executive-branch agencies and information systems "used or operated by an agency or by a contractor of an agency or other organization on behalf of an agency" (§ 3554(a)(1)(A)). National security systems follow separate direction (§ 3557) and sit outside DHS/CISA authority |
| Governance roles | Agency head accountable (§ 3554(a)); CIO delegated compliance authority (§ 3554(a)(3)); a designated senior agency information security officer (CISO) (§ 3554(a)(3)(A)); Senior Agency Official for Privacy (A-130 App. II); Inspector General annual evaluation (§ 3555) |
| Incident clocks | Any incident: CISA within **1 hour** of identification by the agency's top-level CSIRT/SOC/IT function (CISA guidelines). Major incident: CISA and OMB OFCIO within **1 hour** of the determination (M-25-04); Congress within **7 days** of reasonable basis to conclude it occurred (§ 3554(b)(7)(C)(iii)(III)) |
| Enforcement | No civil penalties. Levers: OMB budget/IT-investment authority (§ 3553(a)(5) via 40 U.S.C. § 11303), compulsory CISA directives, IG findings, GAO audits, congressional reporting, ATO withdrawal |
| Assessment model | Risk Management Framework: categorize → select → implement → assess → authorize (ATO) → monitor; annual IG effectiveness evaluation; quarterly/annual CIO metrics |
| Contractor reach | FAR 52.204-21 (15 basic safeguards for Federal Contract Information); proposed FAR CUI clause re-issued 23 June 2026 (not final); FedRAMP for cloud (44 U.S.C. §§ 3607–3616) |

## What it is

FISMA is the organic statute for civilian federal information security. It does not itself list controls; it assigns roles (OMB sets policy, DHS/CISA operates and directs, NIST writes the standards, agency heads own the risk, IGs evaluate) and mandates an agency-wide information security program with defined minimum components (§ 3554(b)). Its stated purposes include "development and maintenance of minimum controls" and oversight "through automated security tools to continuously diagnose and improve security" (§ 3551) — the statutory hook for CDM and continuous monitoring.

The regime is layered. Congress fixed the statute in 2014; the executive branch continuously reshapes the obligations beneath it through OMB circulars and memoranda, NIST standards, CISA directives and presidential executive orders. In practice a federal security programme is measured less against the statute than against the current year's OMB/CISA FISMA metrics, the active BODs and the RMF artifacts (system security plan, assessment report, POA&M, ATO letter). The 2025–2026 period saw substantial churn in that policy layer (see Timeline), so any compliance artifact must cite the memorandum or directive version it relies on.

## Who it covers / Scope

- **Agencies:** "agency" takes the 44 U.S.C. § 3502 meaning (§ 3552(a)). CFO Act agencies report all CIO metrics; non-CFO Act agencies report only annually (FY2026–27 CIO metrics instructions).
- **Contractor-operated systems:** the agency head's duty explicitly extends to systems operated by contractors or others on the agency's behalf (§ 3554(a)(1)(A)(ii)); OMB directs the same for information collected or maintained on behalf of an agency (§ 3553(a)(2)). Contractual flow-down is the mechanism — see Contractors below.
- **National security systems (NSS):** defined at § 3552(b)(6); excluded from OMB annual FISMA guidance and from DHS/CISA directive authority (§ 3553(b), (h)(1)(B)); governed by § 3557 and NSS-specific direction. OMB memoranda M-26-14 and M-26-15 each state they do not apply to NSS.
- **Definitions that drive scope:** "incident" (§ 3552(b)(2)) covers anything that actually or imminently jeopardizes confidentiality, integrity or availability, or violates security policy — far broader than a breach; "binding operational directive" (§ 3552(b)(1)) is a compulsory direction to safeguard federal information from a known or reasonably suspected threat, vulnerability or risk.
- **Not covered:** private-sector entities as such, state/local government, and the legislative and judicial branches (subject to their own rules). Sector regulators may import FISMA/NIST concepts by contract or rule, but that is a separate obligation.

## Core obligations

### Statutory duties (44 U.S.C. §§ 3553–3556)

| Section | Duty |
|---|---|
| § 3553(a) | OMB Director oversees agency security policy, requires risk-commensurate protections, enforces accountability including via 40 U.S.C. § 11303 budget actions |
| § 3553(b) | DHS Secretary (through CISA) administers implementation for non-NSS systems, issues BODs (including incident-reporting and annual-report content requirements, exigent-risk mitigation), monitors agencies, deploys technology on request; must consult NIST on directives implementing NIST standards |
| § 3553(h) | Emergency directives against substantial threats; Secretary may act directly on systems in limited cases, with 7-day notice to Congress |
| § 3554(a) | Agency head: risk-commensurate protections; compliance with NIST standards, BODs, EDs, OMB policy and 41 U.S.C. § 1326 supply-chain duties; integrate security into strategic/budget planning; delegate to CIO; designate a qualified senior agency information security officer; CIO reports annually to the agency head on programme effectiveness and remediation progress |
| § 3554(b) | Agency-wide programme: periodic risk assessments; risk-based, cost-effective policies; subordinate plans for networks, facilities and systems; security awareness training; **testing of management, operational and technical controls of every inventoried system at least annually** using automated tools; a documented remedial-action (POA&M) process; incident detection/reporting/response procedures consistent with the § 3556 centre; continuity of operations plans |
| § 3554(c) | Annual report to OMB, DHS, GAO and named congressional committees: each major incident (threats, prior risk assessments, compliance status, response), total incident counts, PII breaches with individuals affected; unclassified form with optional classified annex |
| § 3554(d)–(e) | Performance-plan disclosure of time and resources needed; public notice and comment on security policies affecting communication with the public |
| § 3555 | Annual independent evaluation by the IG (or an IG-selected external auditor; agencies without an IG engage one), testing a representative subset of systems; results to OMB by the date OMB sets |
| § 3556 | Central federal incident centre (CISA) provides technical assistance, compiles and analyses incident data, warns of threats |

Pub. L. 113-283 § 2(b) requires OMB to define "major incident"; OMB does so in the annual FISMA memorandum.

### Incident and major-incident reporting

| Trigger | Recipient | Clock | Source |
|---|---|---|---|
| Any incident (§ 3552 definition) | CISA | Within 1 hour of identification by the top-level CSIRT/SOC/IT department; seven mandatory data elements (functional impact, information impact, recoverability, detection time, systems/records/users affected, network location, POC); severity per CISA Cyber Incident Severity Schema | CISA Federal Incident Notification Guidelines (effective 1 Apr 2017) |
| Major incident determination | CISA and OMB OFCIO | Within 1 hour of determining a major incident occurred (or that an already-reported incident is major); reach out to both directly | M-25-04 |
| Major incident | Congressional committees in § 3554(c)(1) | Not later than 7 days after there is a reasonable basis to conclude it occurred; supplemental updates as information develops; description in the annual report | § 3554(b)(7)(C)(iii)(III) |
| Major incident (CISA back to agencies) | Federal enterprise | CISA shares scope, relevance, impact and recommendations within 10 days of the declaration | M-25-04 |

M-25-04 definition: a major incident is **either** (A) an incident likely to result in demonstrable harm to national security interests, foreign relations, the economy, public confidence, civil liberties, or public health and safety (CISA severity Level 3 orange and above), **or** (B) a breach of PII likely to cause such harm — with a mandatory major-incident determination for unauthorized modification, deletion, exfiltration of, or access to the PII of **100,000 or more people**. A major incident is also a "significant cyber incident" under PPD-41. Breach handling follows OMB M-17-12. Record every clock in the [incident notification log template](../../templates/incident-regulatory-notification-log.md); see [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).

### OMB Circular A-130 and the NIST/RMF layer

- **A-130 Appendix I** requires agencies to designate authorizing officials; complete an **initial authorization to operate (ATO)** for every system and agency-designated common controls, based on explicit risk acceptance, **before operational status**; transition eligible systems to **ongoing authorization**; reauthorize on a time- or event-driven basis per risk tolerance; and maintain an information security continuous monitoring (ISCM) strategy. A robust ISCM and privacy continuous monitoring programme is a precondition for ongoing authorization. **Appendix II** vests agency-wide privacy programme accountability in the SAOP.
- **FIPS 199** categorizes information and systems as Low/Moderate/High per confidentiality, integrity and availability impact; **FIPS 200** sets minimum security requirements and the risk-based control-selection process; **SP 800-53 Rev. 5** supplies the control catalogue (baselines in SP 800-53B, assessment procedures in SP 800-53A); **SP 800-37 Rev. 2** defines the RMF steps (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor). See [../frameworks/nist-800-53.md](../frameworks/nist-800-53.md).
- **SP 800-53 Release 5.2.0** (27 Aug 2025) added SA-15(13), SA-24 and SI-02(07) and revised SI-07(12), with updated discussion on secure patch/update deployment — the NIST deliverable EO 14306 required by 2 Sept 2025.

### OMB memoranda in force (September 2026)

| Memo | Date | Requirement |
|---|---|---|
| M-25-04 FY2025 FISMA guidance | 15 Jan 2025 | Rescinds M-24-04. Major-incident definition and 1-hour OMB/CISA reporting; FY2025 deadlines (IG metrics 1 Aug 2025; annual CIO/SAOP metrics, agency and IG reports, agency-head letter 31 Oct 2025; quarterly CIO metrics). IG metrics on a multi-year cycle: core metrics annually, remainder on a 2-year cycle; CFO Act IGs summarize results by CSF capability level. No FY2026 successor memorandum appears on OMB's memoranda index as of Sept 2026 (verify) |
| FY2026 & FY2027 CIO FISMA Metrics v1.0 (OMB/CISA/FMSC) | 3 Aug 2026 | CyberScope deadlines: FY26 Q4/annual 30 Oct 2026; FY27 Q1 29 Jan 2027, Q2 30 Apr 2027, Q3 30 Jul 2027, Q4/annual 29 Oct 2027; CDM-populated values available four weeks ahead from FY27; domains include inventory (HVA, OT/IoT, EOL/EOS, cloud, critical software), ATO, MFA/encryption, identity, logging maturity (M-26-14) |
| M-22-09 Federal zero trust strategy | 26 Jan 2022 | Goals to be met by end of FY2024 across five CISA pillars (Identity, Devices, Networks, Applications and Workloads, Data): enterprise-managed identity with phishing-resistant MFA, complete device inventory, encrypted DNS/HTTP, applications treated as internet-connected and externally tested, data categorization and enterprise logging |
| M-26-05 Risk-based software and hardware security | 23 Jan 2026 | **Rescinds M-22-18 (Sept 2022) and M-23-16 (June 2023)** — the common Secure Software Development Attestation Form is no longer mandatory. Agencies keep complete software/hardware inventories, set assurance policies matched to risk, may still use the form, request SBOMs contractually, and reference SP 800-218 (SSDF), CISA 2025 SBOM minimum elements and the HBOM framework |
| M-26-14 Logging and network visibility | 22 May 2026 | **Rescinds M-21-31.** Two objectives: Continuous Event Monitoring (SOC real-time) and Threat Hunting, Investigation, Response and Forensics (hot/cold storage, centralized retrieval); applies to all agency and third-party-operated systems including IoT/OT. CISA publishes a Logging Reference Architecture within 90 days; agencies submit an Agency Logging Plan to OMB and CISA within 90 days; revised maturity model (Appendix C) reported as percentage of systems per level; logs provided to CISA/FBI on request |
| M-26-15 Post-quantum cryptography migration | 24 Jun 2026 | Implements the 22 June 2026 EO on advanced cryptographic attacks and the Quantum Computing Cybersecurity Preparedness Act: prioritized migration of cryptographic systems as feasible by 31 Dec 2030, phased to full migration by 2035; migration plan to OMB/ONCD within 120 days; automated cryptographic inventory; TLS 1.3 by 2 Jan 2030 |

### CISA Binding Operational Directives (active unless noted)

| Directive | Issued | Core requirement |
|---|---|---|
| BOD 23-01 Asset visibility and vulnerability detection | 3 Oct 2022 | Automated asset discovery every 7 days; vulnerability enumeration on all assets (incl. roaming devices) every 14 days; detection signatures updated at least every 24 hours; results into CDM within 72 hours; on-demand discovery within 72 hours of a CISA request with results in 7 days; compliance by 3 Apr 2023 |
| BOD 23-02 Internet-exposed management interfaces | 13 Jun 2023 | Within 14 days of CISA notification, remove the management interface (routers, switches, firewalls, VPN concentrators, proxies, load balancers, OOB management) from the internet or enforce zero-trust access controls; CSP management consoles excluded |
| BOD 25-01 Secure cloud practices (SCuBA) | 17 Dec 2024 | Microsoft 365 at issuance: tenant inventory by 21 Feb 2025; SCuBA assessment tooling and continuous/quarterly reporting by 25 Apr 2025; all mandatory SCuBA policies by 20 Jun 2025; baselines in place before ATO for new tenants |
| BOD 26-02 End-of-support edge devices | 5 Feb 2026 | Immediately update supported devices running EOS software; inventory devices on CISA's EOS list within 3 months; decommission pre-existing EOS devices within 12 months; all identified EOS edge devices within 18 months; continuous discovery and lifecycle process within 24 months |
| BOD 26-04 Prioritizing security updates based on risk | 10 Jun 2026 | **Supersedes and revokes BOD 19-02 and BOD 22-01 (KEV).** Remediation tiers set by asset exposure, KEV status, exploit automatability and technical impact — 3 days for publicly exposed, automatable KEVs giving total control; 6 days partial control; 30 days for exposed, automatable non-KEV; lowest tier fixed on system upgrade. Phase II within 60 days, Phase III within 180 days (7 Dec 2026). KEV status via CDM or bi-weekly manual report; quarterly attestation of public IP space; asset tagging every 7 days |

Emergency Directives are issued under § 3553(h) for specific campaigns (e.g., ED 25-03 Cisco ASA devices; ED 26-03 Cisco SD-WAN) and carry short, product-specific deadlines; track the directives index for supplements and V1 revisions. The FedRAMP PMO mirrored BOD 26-04 for cloud providers: Vulnerability Detection and Response / Vulnerability Evaluation and Reporting rules mandatory 7 Dec 2026, non-compliant authorizations revoked after 7 Mar 2027.

### Executive orders

| Order | Date / citation | Status and content |
|---|---|---|
| EO 14028 Improving the Nation's Cybersecurity | 12 May 2021, 86 FR 26633 | In force. Threat-information sharing (s.2), federal modernization — zero trust, cloud, MFA and encryption (s.3), software supply chain — SSDF, SBOM, critical software (s.4), Cyber Safety Review Board (s.5), standard incident playbook (s.6), EDR and hunting (s.7), logging (s.8). Implementing memos M-22-09 remain; M-21-31, M-22-18 and M-23-16 have been rescinded (above) |
| EO 14144 Strengthening and Promoting Innovation in the Nation's Cybersecurity | 16 Jan 2025, 90 FR 6755 | In force **as amended** by EO 14306 |
| EO 14306 Sustaining Select Efforts to Strengthen the Nation's Cybersecurity | 6 Jun 2025, 90 FR 24723 | Struck EO 14144 ss.2(a)–(b) (FAR contract language for machine-readable secure-software attestations and artifacts), 3(a)–(b) (WebAuthn/phishing-resistant pilots), 4(b)(iv), 4(d)(ii)–(iii) and the digital-identity-document section 5; rewrote s.1 policy (PRC as most active threat). Retained/re-set: NIST SSDF consortium by 1 Aug 2025; SP 800-53 patch-deployment guidance by 2 Sept 2025; preliminary SSDF update by 1 Dec 2025 with final within 120 days; CISA list of PQC-ready product categories by 1 Dec 2025; TLS 1.3 support by 2 Jan 2030; AI-vulnerability handling in existing processes by 1 Nov 2025; OMB guidance including A-130 revision within 3 years (by June 2028); rules-as-code pilot within 1 year; FAR amendment requiring Cyber Trust Mark on consumer IoT bought by government by 4 Jan 2027; NSS and debilitating-impact systems excluded except for s.4(f) |

## Enforcement and penalties

FISMA carries no fines or private right of action. Consequences are institutional: OMB may withhold or condition IT funding (§ 3553(a)(5), 40 U.S.C. § 11303); CISA directives are compulsory and non-compliance is reported to OMB and Congress; the IG's annual evaluation and FISMA metrics feed public scorecards, GAO reports and appropriations oversight; an authorizing official may deny or revoke an ATO. For contractors, the practical sanctions are contractual — cure notices, termination, past-performance impact and, for misrepresented security compliance, False Claims Act exposure via the Department of Justice's civil cyber-fraud enforcement (verify current initiative status).

## Timeline and status

| Date | Event |
|---|---|
| 18 Dec 2014 | Pub. L. 113-283 enacted; 44 U.S.C. §§ 3551–3558 replace FISMA 2002 |
| 1 Apr 2017 | CISA Federal Incident Notification Guidelines effective — 1-hour reporting |
| 12 May 2021 | EO 14028 |
| 26 Jan 2022 | M-22-09 zero trust strategy (targets end FY2024) |
| 23 Dec 2022 | FedRAMP Authorization Act (Pub. L. 117-263 § 5921) codifies FedRAMP at 44 U.S.C. §§ 3607–3616; statutory repeal of those sections effective 5 years after enactment (23 Dec 2027) unless extended |
| 15 Jan 2025 | M-25-04 FY2025 FISMA guidance; proposed FAR CUI rule (90 FR 4278, 8-hour incident reporting) |
| 16 Jan / 6 Jun 2025 | EO 14144, then EO 14306 amending it |
| 27 Aug 2025 | SP 800-53 Release 5.2.0 |
| 23 Jan 2026 | M-26-05 rescinds M-22-18/M-23-16 attestation mandate |
| 5 Feb 2026 | BOD 26-02 EOS edge devices |
| 22 May 2026 | M-26-14 rescinds M-21-31 logging memo |
| 10 Jun 2026 | BOD 26-04 replaces BOD 22-01/19-02; Phase III due 7 Dec 2026 |
| 23 Jun 2026 | FAR CUI clause re-proposed as FAR 52.240-7 within the FAR overhaul (FAR Case 2026-001); comments closed 23 Jul 2026; **not final as of Sept 2026** |
| 24 Jun 2026 | M-26-15 PQC migration (plans due within 120 days; 2030/2035 milestones) |
| 3 Aug 2026 | FY2026–27 CIO FISMA metrics published; FY26 annual submission due 30 Oct 2026 |
| Pending | FISMA statutory reform bills have been introduced in successive Congresses (e.g., 118th Congress S. Rept. 118-271) without enactment as of the sources reviewed (verify); OMB A-130 revision required by EO 14306 within 3 years |

## Key obligations for security/GRC teams

1. **Establish applicability and system boundary**: agency vs contractor-operated vs NSS; FIPS 199 categorization per system; identify HVAs and cloud tenants — see [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Run the RMF to an ATO and keep it current**: SSP, SP 800-53A assessment, POA&M, authorizing-official decision before operation; move to ongoing authorization backed by an ISCM strategy — see [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md) and [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).
3. **Test every inventoried system at least annually** (§ 3554(b)(5)) and evidence it — the CIO metrics count "covered by an annual test" as within the past 365 days.
4. **Wire the incident clocks**: 1 hour to CISA for any incident; 1 hour to CISA and OMB on a major-incident determination; 7 days to Congress; 100,000-person PII threshold pre-built into triage — see [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../../workflows/incident-regulatory-response.md](../../workflows/incident-regulatory-response.md).
5. **Track every active BOD/ED as a dated control requirement** (BOD 23-01 cadences, BOD 25-01 SCuBA baselines, BOD 26-02 EOS milestones, BOD 26-04 remediation tiers) with exceptions formally approved — see [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md) and [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).
6. **Deliver the reporting calendar**: quarterly and annual CIO metrics in CyberScope, IG core metrics, SAOP metrics, agency-head letter and annual report — see [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md) and the [board report template](../../templates/grc-board-report.md).
7. **Prepare for the IG evaluation** as an annual audit with a two-year rotation of non-core metrics — see [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md) and [../../workflows/audit-readiness.md](../../workflows/audit-readiness.md).
8. **Re-baseline supply-chain and logging programmes** to M-26-05 (risk-based assurance, SBOM by contract) and M-26-14 (Agency Logging Plan, maturity model) rather than the rescinded M-22-18/M-21-31 checklists — see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
9. **Start the PQC inventory and migration plan** required by M-26-15 (plan within 120 days; TLS 1.3 by 2 Jan 2030) — see [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).
10. **Contractors**: implement FAR 52.204-21's 15 safeguards on any system holding Federal Contract Information and flow them to subcontractors; monitor the FAR CUI rule (SP 800-171 Rev. 3, 72-hour CUI incident reporting) and DoD CMMC — see [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).

## Interplay

- **NIST SP 800-53 / RMF**: the mandatory control catalogue and process for federal systems; FISMA supplies the legal duty, A-130 the policy, NIST the how — see [../frameworks/nist-800-53.md](../frameworks/nist-800-53.md). CIS Controls and ISO 27001 are used only as supplementary mappings — see [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md) and [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).
- **NIST CSF 2.0**: IG FISMA reporting for CFO Act agencies is summarized by CSF capability level, so gap assessments should carry CSF function tags — see [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md).
- **FedRAMP**: a FedRAMP authorization package is "presumed adequate" for an agency ATO of a cloud service (44 U.S.C. § 3613(e)) but does not relieve the agency's FISMA responsibility; agencies file their ATO letters with GSA (§ 3613(c)). The proposed FAR CUI clause requires FedRAMP Moderate-equivalent security for contractor cloud holding CUI. FedRAMP has its own pack (separate; not linked here).
- **Contractor rules**: FAR 52.204-21 (FCI) is the floor; CUI protection runs through the pending FAR clause, DFARS 252.204-7012 (72-hour DoD reporting) and CMMC (32 CFR part 170). The June 2026 FAR proposal aligned its 72-hour clock to CIRCIA and DFARS.
- **Privacy**: A-130 Appendix II, the Privacy Act and OMB M-17-12 breach guidance run alongside FISMA; a PII breach of 100,000+ people is automatically a major incident. Federal health, financial and education programmes may additionally face sectoral rules — see [hipaa.md](hipaa.md) for HIPAA-covered federal components.
- **Sectoral and state regimes**: FISMA does not bind private operators, but agency procurements routinely impose NIST 800-53/800-171 baselines on vendors, which then interact with the vendors' own obligations under [glba-ftc-safeguards.md](glba-ftc-safeguards.md), [sec-cyber-disclosure.md](sec-cyber-disclosure.md) or [us-state-privacy.md](us-state-privacy.md).

## Primary sources

- 44 U.S.C. Chapter 35, Subchapter II (§§ 3551–3559) — statutory text, Office of the Law Revision Counsel: https://uscode.house.gov/view.xhtml?path=/prelim@title44/chapter35/subchapter2&edition=prelim
- Pub. L. 113-283, Federal Information Security Modernization Act of 2014 — enrolled text, govinfo: https://www.govinfo.gov/content/pkg/PLAW-113publ283/html/PLAW-113publ283.htm
- 44 U.S.C. Chapter 36 (§§ 3607–3616, FedRAMP) — statutory text: https://uscode.house.gov/view.xhtml?path=/prelim@title44/chapter36&edition=prelim
- OMB Circular A-130, Managing Information as a Strategic Resource — policy text: https://www.whitehouse.gov/wp-content/uploads/legacy_drupal_files/omb/circulars/A130/a130revised.pdf
- OMB M-25-04, FY2025 FISMA guidance (archived): https://bidenwhitehouse.archives.gov/wp-content/uploads/2025/01/M-25-04-Fiscal-Year-2025-Guidance-on-Federal-Information-Security-and-Privacy-Management-Requirements.pdf
- OMB M-22-09 zero trust: https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf · M-26-05: https://www.whitehouse.gov/wp-content/uploads/2026/01/M-26-05-Adopting-a-Risk-based-Approach-to-Software-and-Hardware-Security.pdf · M-26-14: https://www.whitehouse.gov/wp-content/uploads/2026/05/M-26-14-Ensuring-Effective-and-Efficient-Agency-Logging-and-Network-Visibility-to-Defend-Against-Evolving-Cyber-Threats.pdf · M-26-15: https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf · OMB memoranda index: https://www.whitehouse.gov/omb/information-for-agencies/memoranda/
- FY2026 & FY2027 CIO FISMA Metrics v1.0 (OMB/CISA/FMSC, 3 Aug 2026): https://www.cisa.gov/sites/default/files/2026-08/FY2026-FISMA-cio-metrics.pdf
- CISA Federal Incident Notification Guidelines (regulator guidance): https://www.cisa.gov/federal-incident-notification-guidelines
- CISA directives index and BODs 22-01 (revoked), 23-01, 23-02, 25-01, 26-02, 26-04: https://www.cisa.gov/news-events/directives (individual directive pages under the same path)
- FedRAMP response to BOD 26-04 (programme notice): https://www.fedramp.gov/notices/0014/
- EO 14028 (86 FR 26633): https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity · EO 14144 (90 FR 6755): https://www.federalregister.gov/documents/2025/01/17/2025-01470/strengthening-and-promoting-innovation-in-the-nations-cybersecurity · EO 14306 (90 FR 24723): https://www.federalregister.gov/documents/2025/06/11/2025-10804/sustaining-select-efforts-to-strengthen-the-nations-cybersecurity-and-amending-executive-order-13694-and-executive
- NIST publication pages: FIPS 199 https://csrc.nist.gov/pubs/fips/199/final · FIPS 200 https://csrc.nist.gov/pubs/fips/200/final · SP 800-53 Rev. 5 https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final · SP 800-37 Rev. 2 https://csrc.nist.gov/pubs/sp/800/37/r2/final
- FAR 52.204-21 (acquisition.gov, FAC 2026-01): https://www.acquisition.gov/far/52.204-21 · Proposed FAR CUI rule, 15 Jan 2025 (90 FR 4278): https://www.federalregister.gov/documents/2025/01/15/2024-30437/federal-acquisition-regulation-controlled-unclassified-information · Re-proposal within the FAR overhaul, 23 Jun 2026: https://www.federalregister.gov/documents/2026/06/23/2026-12559/federal-acquisition-regulation-revolutionary-federal-acquisition-regulation-overhaul-parts-1-2-4-33
- Secondary (used only to confirm rescission dates already stated in the primary memoranda): law-firm and trade-press alerts on M-26-05 and M-26-14.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
