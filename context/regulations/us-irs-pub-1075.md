# IRS Publication 1075 — Tax Information Security Guidelines for Federal, State and Local Agencies (Pub 1075 / IRC § 6103(p)(4))

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | IRS Publication 1075, *Tax Information Security Guidelines for Federal, State and Local Agencies* — Rev. 11-2021 (Catalog Number 46937O); supersedes the November 2016 edition and took effect 6 months after publication. IRS Safeguards pages reviewed as late as 18 September 2026 still cite Rev. 11-2021 as current |
| Legal basis | IRC § 6103 (confidentiality of returns and return information); § 6103(p)(4) safeguard conditions (A)–(F); § 6103(p)(9) contractor safeguards (added by Taxpayer First Act § 2004); § 6103(p)(7) and 26 CFR 301.6103(p)(7)-1 (suspension, termination, administrative review) |
| Regulator | IRS Office of Safeguards (safeguardreports@irs.gov); Treasury Inspector General for Tax Administration (TIGTA) investigates incidents |
| Protected data | Federal Tax Information (FTI): returns and return information received from the IRS or an authorized secondary source (SSA, OCSE, BFS, CMS) **plus anything derived from it**; categorized Sensitive But Unclassified; may not be "masked" to escape § 6103 |
| Who is covered | Federal, state, tribal and local agencies (and other recipients listed in § 6103(p)(4)) that receive FTI under a § 6103 exception, plus their contractors, sub-contractors, consolidated data centers and state consolidated IT organizations |
| Structure | Section 1.0 Federal Tax Information, reviews and other requirements; Section 2.0 physical security keyed to § 6103(p)(4)(A)–(F) (2.A–2.F); Section 3.0 cybersecurity and technology-specific rules; Section 4.0 NIST SP 800-53 Rev. 5 control catalog (20 families, 4.1–4.20); Exhibits 1–9 (statute, CFR, sanctions, 45-day procedures, contract language, banners, retention) |
| Core clocks | Incident/breach: TIGTA and Office of Safeguards **within 24 hours** of discovery. Initial SSR **≥ 90 days** before first receipt of FTI. **45-day** advance notification for cloud, contractors, sub-contractors, tax modeling, live-data testing. SRR/CAP issued **within 45 days** of closing conference; critical-finding mitigation plan **within 7 days** |
| Penalties | § 7213 willful disclosure: felony, fine ≤ $5,000 and/or ≤ 5 years, plus costs; § 7213A willful inspection: misdemeanor, fine ≤ $1,000 and/or ≤ 1 year; § 7431 civil damages: greater of $1,000 per act or actual damages, punitive damages for willful/grossly negligent acts, costs and fees. Administrative: IRS may suspend or terminate FTI disclosures |
| Assessment model | Not certifiable. Annual Safeguard Security Report (SSR) with head-of-agency certification, semi-annual Corrective Action Plan (CAP), IRS-led Safeguard Reviews (on-site, remote or hybrid) using SCSEM test matrices, agency internal inspections |
| Neighbours | Built on [NIST SP 800-53 Rev. 5](../frameworks/nist-800-53.md); relies on FedRAMP for cloud; sits alongside FISMA for federal recipients and state privacy/breach laws for state agencies |

## What it is

Publication 1075 is the IRS's binding interpretation of the safeguard conditions Congress attached to every disclosure of tax data outside the IRS. IRC § 6103 makes returns and return information confidential and then lists exceptions (child support, human services, state tax administration, statistical use, law enforcement, and so on). Section 6103(p)(4) conditions those exceptions: a recipient must keep a permanent system of records of requests and disclosures (A), store FTI in a secure area (B), restrict access to persons whose duties require it (C), provide "such other safeguards" as the Secretary prescribes (D), report on its procedures to the IRS (E), and return or destroy the data when done (F). Pub 1075 is where (D) and (E) get operational content.

The November 2021 revision re-based Section 4.0 on SP 800-53 Rev. 5 (privacy controls integrated, SR family added), adapted NIST SP 800-63 digital identity requirements, folded in Treasury Directive 85-01 requirements as IRS-defined parameters, changed most "should" statements to "must", added an offshore-operations section (2.C.7), split Exhibit 7 into 7a (general services) and 7b (technology services), and replaced the former fixed Safeguard Review Cycle table with a risk-based assessment process. The older "Safeguard Procedures Report (SPR)" no longer appears in Rev. 11-2021; the SSR is the single reporting vehicle, though some older IRS technical-assistance pages still use the SPR term.

## Who it covers / Scope

| Test | Detail |
|---|---|
| Recipient type | Any federal agency, state or local agency, body or commission, appropriate State officer, tribal grantee or other person named in § 6103(p)(4) that receives FTI "as a condition for receiving returns or return information". Typical: state revenue departments, child support (§ 6103(l)(6), (l)(8), (l)(10)), human services (§ 6103(l)(7)), Medicaid/CMS (§ 6103(l)(12)), law enforcement (§ 6103(i)). Pub. L. 118-258 (4 Jan 2025) put tribal child support enforcement agencies, and Indian tribes or tribal organizations holding a Social Security Act § 455(f) grant, on the same footing as state recipients in § 6103(a)(2), (l)(6), (l)(8), (p)(4) and (p)(9) |
| Data trigger | Possession or control of FTI, including information the agency itself creates from FTI. An IRS-sourced address entered into agency records stays FTI unless it is overwritten from an independent taxpayer or third-party source (2.C.5) |
| Secondary receipt | FTI obtained via SSA, OCSE, Bureau of the Fiscal Service, CMS or another IRS agent under a § 6103(p)(2)(B) agreement is in scope and covered by Safeguard Reviews |
| Contractors and agents | In scope through the agency: § 6103(p)(9) forbids disclosure to any contractor or agent unless the agency has safeguard requirements in effect, conducts an **on-site review every 3 years** (at the mid-point for contracts shorter than 3 years; contracts under 6 months need none), reports the findings in its § 6103(p)(4)(E) report, and certifies compliance annually on the IRS contractor worksheet (name, address, contract description, duration). Pub 1075 records the requirements as effective 31 December 2022; the IRS Taxpayer First Act § 2004 page states 1 January 2023 |
| Contractor restriction | Human services agencies receiving FTI under § 6103(l)(7) may not disclose FTI to contractors for any purpose (Exhibit 6) |
| Assessment boundary | Every system that receives, processes, stores, accesses, protects or transmits FTI — agency-owned, state consolidated IT, contractor/sub-contractor, constituent counties — including workstations, hypervisors, storage, cloud environments, firewalls, VPN, wireless, VoIP |
| Territorial rule | No offshore access, storage, processing, transmission, support or disposal (Section 2.C.7). "United States" means the states, DC, territories, embassies and military installations |
| Exit | Agencies that stop receiving FTI must document termination; where statute forces retention of residual FTI (e.g. 5 or 10 years), they keep submitting an annual SSR and remain subject to reviews until destruction is certified by the head of agency |

## Core obligations

### Reporting to the IRS (§ 6103(p)(4)(E) — Section 2.E)

| Deliverable | Requirement |
|---|---|
| Safeguard Security Report (SSR) | Initial SSR ≥ 90 days before scheduled receipt of FTI; new agencies also need an approved Security Assessment Report and Authority to Operate before onboarding. Updated and resubmitted **annually** on the prior year's returned template, with head-of-agency certification, internal inspection reports (HQ, all data centers, 10 % of field offices), contractor list and § 6103(p)(9) certification. No waiver process, even when a review is scheduled |
| SSR/CAP due dates | Federal agencies: reporting period 1 Jan–31 Dec, due 31 January. States and territories are grouped into monthly cohorts (e.g. AK/AL/AR/AS/AZ/CA due 28 February; NC/NH/NJ/NM/NV/NY due 31 July; WI/WV/WY due 30 November). CAP-only submissions fall six months after the SSR date (Table 4 and Table 5) |
| Corrective Action Plan (CAP) | Updated and submitted **semi-annually** until all review findings are accepted as closed; each item needs evidence of action and an actual or planned implementation date; a CAP due within 60 days of a review is not required |
| 45-day notifications (Section 2.E.6, Table 6) | Notify safeguardreports@irs.gov at least **45 days** before: implementing cloud computing (notify); disclosing FTI to a contractor (notify); contractor re-disclosure to a sub-contractor (notify **and obtain approval**); using FTI in tax modeling (approval, valid up to 3 years); using live FTI in a pre-production/test environment via a Data Testing Request (approval, also valid up to 3 years). Noting a change in the SSR does not satisfy the notification duty |
| Contractor notification letter (Exhibit 6) | On agency letterhead over the head of agency's (or a delegate's) signature: POC, contractor name/address, contract number, dates and period, service type, headcount, program supported, FTI to be disclosed, work and phasing, oversight procedures, work locations, sub-contractor details, and certification that all personnel and systems are within the US |
| Safeguards documents | PFR, SRR, SSR and CAP are IRS property; public-records requests must be referred to the IRS FOIA process, though internal and oversight distribution is allowed |

### Incident and breach reporting (Section 1.8; IR-6)

| Element | Requirement |
|---|---|
| Trigger | Any possible improper inspection or disclosure of FTI, including data incidents (actual or imminent jeopardy to CIA, policy violations, incidental and inadvertent access) and data breaches (loss, theft, unauthorized access or acquisition, authorized user acting for an unauthorized purpose, misdirected email, public posting, oral disclosure) |
| Clock | Contact the local TIGTA Field Division Special Agent-in-Charge **immediately, but no later than 24 hours** after identification (hotline 800-366-4484), and **concurrently** email the Office of Safeguards. Do not wait for an internal investigation to confirm FTI was involved |
| Content | Data incident report: agency and POC, date/time occurred and discovered, how discovered, description and data elements, potential number of FTI records (or range), address, IT involved, whether disciplinary action will be proposed. Encrypted, subject line "data incident report", **no FTI in the report**; supplement as facts emerge |
| Follow-through | Cooperate with TIGTA/Safeguards investigators; apply IR-1/IR-4 procedures; post-incident review; retrain immediately on any procedure change; annual tabletop test (IR-3) |
| Individuals and media | Written notice to the taxpayer (date of the event and § 7431 rights) when disciplinary or adverse action is proposed against the responsible employee; confirm completion to Safeguards; share draft media releases with Safeguards before distribution. Other individual notification follows the agency's own policy and applicable state law |
| Personnel | Initial and annual confidentiality certification must state the employee will report to TIGTA and Safeguards within 24 hours; contractor sanctions notified to designated agency personnel within 72 hours |

### Personnel, physical and handling controls (Section 2)

| Topic | Requirement |
|---|---|
| Background investigations (2.C.3) | Written policy with adjudication criteria; investigation initiated **before** FTI access for employees, contractors and sub-contractors; minimum elements: FBI fingerprint check (FD-258), local law-enforcement checks for the last 5 years of residence/work/school, and citizenship/work-authorization validation; state agencies must reinvestigate **within 5 years** (FBI Rap Back satisfies the recheck). IRS guidance notes Treasury treats FTI as Moderate Risk Public Trust (Tier 2, SF85P) |
| Training (2.D.2, AT-2/AT-3) | Disclosure awareness training before access and annually, covering §§ 7213, 7213A, 7431 and incident reporting; signed confidentiality statement (ink or electronic) at initial certification and each annual recertification, retained ≥ 5 years; security and privacy awareness updates at least quarterly; role-based, contingency and incident-response training |
| Physical security (2.B) | Minimum Protection Standards: **two barriers** (secured perimeter, security room, badged employee, locked container, etc.); restricted-area access lists; visitor logs retained 5 years; lock combinations changed annually or on staff change; monthly review of physical access logs (PE-6); warning banners on screens (Exhibit 8) |
| Recordkeeping (2.A) | Permanent logs of FTI receipt, movement and disclosure; requests and agreements retained ≥ 5 years; audit records retained **7 years** (AU-11) |
| Commingling and labeling (2.C.5) | Keep FTI physically and logically separate where possible; where mixed, the whole file, record, table or medium is treated as FTI and must be clearly labeled; IRS-sourced addresses entered into databases must be flagged as FTI |
| Offshore (2.C.7) | Absolute onshore rule for people and systems; foreign-travel procedures (no FTI-bearing devices, no remote access, battery and SIM removal, sanitization on return) |
| Disposal (2.F) | Burn or shred (crosscut ≤ 1 mm × 5 mm particles, or disintegrator with 3/32 in screen) or otherwise render unreadable; electronic media sanitized per NIST guidance; contractor spoilage returned or destroyed with a destruction statement |
| Internal inspections (2.D.3) | Review cycle: field offices receiving FTI at least every **3 years**; headquarters facilities housing FTI and the agency computer facility at least every **18 months**; all contractors and sub-contractors with FTI access, including consolidated data centers and off-site storage, at least every **18 months**. Documented plan covering the current year and the next two; inspections by personnel outside the FTI-using function (contractors may not self-certify); reports retained ≥ 5 years and summarized with the SSR |

### Cybersecurity and technology-specific requirements (Sections 3 and 4)

| Topic | Requirement |
|---|---|
| Control baseline | Section 4.0 catalogs the SP 800-53 Rev. 5 controls and enhancements agencies must implement, with IRS-defined parameters; assessed with Safeguards Computer Security Evaluation Matrices (SCSEM) and Nessus audit files per platform; a complete FTI system inventory is mandatory |
| Encryption (SC-8, SC-13, IA-7) | Latest FIPS 140-validated modules for all FTI in transit (WAN and LAN, file transfers, app-to-database), email containing FTI, wireless, mobile media and remote access; SHA-1 prohibited for digital signatures. At rest, encryption is required in cloud and on mobile media; a dedicated, SCSEM-configured system behind two physical barriers is exempt at rest |
| Identity (IA-2, IA-5) | Multi-factor authentication at NIST SP 800-63 Authenticator Assurance Level 2; updated password complexity; account managers notified within **24 hours** of termination, transfer or a need-to-know change (AC-2h), with system access disabled within **3 business days** of termination (PS-4); user accounts reviewed annually, privileged accounts semi-annually |
| Cloud (3.3.1; IRS cloud guidance, updated 4 Aug 2026) | Only FedRAMP-authorized cloud service offerings (moderate impact); 3PAO assessment and ATO/P-ATO; all FTI and all administrative access onshore; full data-center address list in the 45-day notification; FIPS 140 encryption in transit **and** at rest written into the SLA; agency-controlled keys (customer-managed keys on a FIPS 140 HSM) to deny CSP logical access — without this the CSP is a contractor needing its own notification; Exhibit 7 language in the CSP contract, not just the reseller's; annual agency assessment of agency-managed cloud controls. FTI found in a non-FedRAMP cloud, or offshore, is a **critical finding**. SaaS built on FedRAMP IaaS still needs its own authorization; ISV/SI solutions hosted inside a compliant CSO do not (FAQ added 31 July 2024) |
| Testing and monitoring | Penetration testing of the FTI environment **every 3 years** (CA-8); risk assessment updated at least every 3 years or on significant change (RA-3); continuous monitoring, vulnerability scanning and patch checks; SIEM/audit log review; proactive auditing of FTI access |
| Other technology rules (3.3.2–3.3.8) | Email, fax, mobile devices, multifunction devices and high-volume printers, network boundary, virtual desktop infrastructure, public-facing systems each carry mandatory configurations; IRS technical-assistance pages cover IVR, web portals, wireless networks, mobile devices, virtual desktops, SIEM, open-source software and collaborative computing environments |
| Contracts (Exhibit 7a/7b) | Mandatory clause set: contractor supervision, Pub 1075 background checks and named-access list, purpose limitation, accounting for FTI, certified purge at completion, Pub 1075-compliant systems, **no subcontracting without prior written IRS approval**, flow-down without modification, agency right to void, written notice of §§ 7213/7213A/7431 and Privacy Act penalties, annual recertification, agency and IRS inspection rights |

## Enforcement and penalties

| Mechanism | Detail |
|---|---|
| Criminal — § 7213(a) | Willful unauthorized disclosure by federal employees, § 6103(n) contractors, state and other employees, or later publication by anyone: felony, fine ≤ $5,000 and/or imprisonment ≤ 5 years plus costs of prosecution; federal employees are also dismissed |
| Criminal — § 7213A (Taxpayer Browsing Protection Act) | Willful unauthorized inspection: misdemeanor, fine ≤ $1,000 and/or imprisonment ≤ 1 year plus costs; federal employees dismissed |
| Civil — § 7431 | Taxpayer suit against the United States (federal actor) or the person (non-federal actor) for knowing or negligent inspection/disclosure: greater of $1,000 per act or actual damages; punitive damages where willful or grossly negligent; costs; attorney fees for qualifying plaintiffs; 2-year limitation from discovery; no liability for good-faith misinterpretation or taxpayer-requested disclosure. § 7431(e) obliges the Secretary to notify the taxpayer on indictment or proposed disciplinary action |
| Administrative — § 6103(p)(4), (p)(7); 26 CFR 301.6103(p)(7)-1 | IRS may suspend or terminate disclosures where the recipient allowed an unauthorized inspection/disclosure without adequate corrective action, or fails to maintain safeguards with no adequate improvement plan; written notice precedes termination and disclosures may be suspended meanwhile; the recipient has **30 days** from receipt of the preliminary determination to appeal in writing to the Commissioner (Exhibit 3) |
| Review findings | Safeguard Review yields a Preliminary Findings Report, then an SRR and CAP within 45 days of the closing conference; critical findings require a mitigation plan within 7 days and are reported to TIGTA; unresolved findings feed the semi-annual CAP and the next review |
| Personnel sanctions | Agencies must maintain disciplinary/adverse-action processes and report whether action is proposed; contractors need a formal sanction process |

## Timeline and status

| Date | Event |
|---|---|
| 4 Oct 1976 | Tax Reform Act (Pub. L. 94-455) enacts the modern § 6103 confidentiality regime including the (p)(4) safeguard conditions |
| 5 Aug 1997 | § 7213A added (Pub. L. 105-35, Taxpayer Browsing Protection Act) |
| 11 Feb 2009 | 26 CFR 301.6103(p)(7)-1 suspension/termination and administrative review procedure (T.D. 9445) |
| Sept 2016 | Minimum background-investigation elements introduced, effective immediately per IRS guidance; Pub 1075 Rev. 11-2016 |
| 1 Jul 2019 | Taxpayer First Act (Pub. L. 116-25) § 2004 adds § 6103(p)(9) contractor safeguards; Pub 1075 records the requirements as effective 31 Dec 2022 |
| Nov 2021 | Pub 1075 Rev. 11-2021 published; effective six months after publication; re-based on SP 800-53 Rev. 5 |
| 31 Jul 2024 | IRS cloud guidance FAQ additions (ISV/SI authorization, customer-managed keys) |
| 4 Jan 2025 | Supporting America's Children and Families Act (Pub. L. 118-258) § 202(a)(2) amends § 6103(a)(2), (l)(6), (l)(8), (l)(10), (p)(4) and (p)(9) to cover tribal child support enforcement agencies and § 455(f) tribal grantees; effective on enactment, no delayed date |
| Jun–Sep 2026 | IRS Safeguards pages (program and internal-inspections pages 28 Jun 2026; incident page 30 Jul 2026; cloud page 4 Aug 2026; 45-day notification and background-investigation pages 17 Aug 2026; encryption page 2 Sep 2026; SSR, Taxpayer First Act § 2004 and contractor pages 18 Sep 2026) reviewed and still cite Rev. 11-2021 — no successor edition located as of 19 September 2026 |
| Watch items | Pub 1075 Section 4.0 maps to SP 800-53 Rev. 5 as published in 2020; later NIST patch releases are not reflected (verify the current release against the [nist-800-53](../frameworks/nist-800-53.md) pack). Section 3.3.1 and the IRS cloud page still describe authorization by "the Joint Advisory Board (JAB) or a Federal Agency"; that wording is overtaken by the FedRAMP Authorization Act, under which GSA grants authorizations consistent with the FedRAMP Board (44 U.S.C. § 3609), and by FedRAMP's consolidated 2026 ruleset — confirm the current pathway against the [fedramp](../frameworks/fedramp.md) pack. Fetched IRS guidance references FedRAMP only; no StateRAMP equivalence is stated |

## Key obligations for security/GRC teams

1. **Confirm applicability and data flow.** Establish under which § 6103 subsection FTI arrives, whether secondary sources (SSA, OCSE, BFS, CMS) deliver it, and where derived FTI lands; maintain the FTI system inventory and data-flow diagram the SSR and SCSEMs demand. See [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md).
2. **Run the SSR/CAP calendar.** Diary the cohort due date, head-of-agency certification, internal inspection coverage (HQ, all data centers, 10 % of field offices), contractor list and § 6103(p)(9) certification; submit CAP updates semi-annually until closure. See [audit-preparation](../../skills/audit-preparation/SKILL.md) and [audit-evidence-request-list](../../templates/audit-evidence-request-list.md).
3. **Operate the 24-hour incident path.** Pre-stage the TIGTA field-office contact, the Safeguards mailbox, an encrypted data-incident-report template with no FTI in it, and the taxpayer-notice text citing § 7431. Log the clock in [incident-regulatory-notification-log](../../templates/incident-regulatory-notification-log.md); see [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md) and the [incident-regulatory-response](../../workflows/incident-regulatory-response.md) workflow.
4. **Gate every third party on 45-day notice and Exhibit 7.** No cloud move, contractor, sub-contractor, tax-modeling or live-data-testing use of FTI without the notification (and approval where required); Exhibit 7a/7b in every contract, including cloud and shredding vendors; 3-year on-site contractor reviews and annual certification. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md), [vendor-security-questionnaire](../../templates/vendor-security-questionnaire.md) and [vendor-onboarding](../../workflows/vendor-onboarding.md).
5. **Enforce onshore and FedRAMP conditions in cloud architecture.** FedRAMP-moderate CSO, US-only data centers and admin access, FIPS 140 in transit and at rest, customer-managed keys on a FIPS 140 HSM, SLA clauses, and an annual assessment of agency-managed controls.
6. **Map Section 4.0 to your control set.** Treat Pub 1075 Section 4.0 as an SP 800-53 Rev. 5 overlay with IRS-defined parameters (AAL2 MFA, 7-year audit retention, 24-hour account-manager notification on termination, 3-year penetration testing); test against the current SCSEMs. See [control-mapping](../../skills/control-mapping/SKILL.md), [control-testing](../../skills/control-testing/SKILL.md) and [framework-crosswalk](../crosswalks/framework-crosswalk.md).
7. **Close the people controls.** Background investigations before access and 5-year reinvestigation, annual disclosure-awareness training with signed certifications retained 5 years, quarterly awareness updates, and personnel sanction processes; run the internal-inspection cycle (18 months for headquarters, the computer facility and every contractor site; 3 years for field offices) and keep evidence review-ready.
8. **Document exceptions honestly.** The IRS states that no SSR waiver process exists; where a control cannot be met, record the risk and compensating measures in the SSR/CAP rather than silently deviating. See [exception-management](../../skills/exception-management/SKILL.md) and [policy-authoring](../../skills/policy-authoring/SKILL.md) for the written policies Pub 1075 requires (incident management, background investigations, access control, risk assessment).

## Interplay

- **NIST SP 800-53 Rev. 5 / FISMA.** Section 4.0 is a tailored Rev. 5 catalog; federal recipients satisfy most of it through their FISMA RMF packages but must still add IRS-defined parameters and Pub 1075 physical, personnel and reporting duties. State agencies inherit a federal-style control set with no FISMA authorization infrastructure behind it. See [nist-800-53](../frameworks/nist-800-53.md) and [us-fisma-federal-cyber](us-fisma-federal-cyber.md).
- **FedRAMP.** Pub 1075 accepts FedRAMP authorization in place of IRS review of the CSP's own controls, but FedRAMP alone does not satisfy Pub 1075: onshore access, key ownership, Exhibit 7 and the 45-day notification are additional. See [fedramp](../frameworks/fedramp.md).
- **HIPAA and Medicaid programs.** Human services and CMS-linked agencies handling both PHI and FTI face two incident regimes: Pub 1075's 24-hour TIGTA/IRS clock is far shorter than HIPAA's 60-day individual-notice outer limit. See [hipaa](hipaa.md) and [breach-notification-timelines](../crosswalks/breach-notification-timelines.md).
- **GLBA / FTC Safeguards Rule.** Tax preparers and financial-aid administrators fall under GLBA rather than Pub 1075; Pub 1075 applies only to FTI received from the IRS under § 6103. See [glba-ftc-safeguards](glba-ftc-safeguards.md).
- **CJIS Security Policy.** State revenue, human services and law-enforcement recipients often hold criminal justice information as well as FTI; the FBI fingerprint check serves both, but the screening standards, audit cycles and reporting chains are separate. See [us-cjis-security-policy](us-cjis-security-policy.md).
- **State privacy and breach laws.** Pub 1075 governs notice to the IRS and TIGTA; individual notification is left to agency policy and state statute, which often carry their own deadlines. See [us-state-privacy](us-state-privacy.md) and [us-state-breach-notification-laws](us-state-breach-notification-laws.md).
- **NIST CSF 2.0.** Useful as the governance wrapper for the program the SSR describes, but the SSR itself is control-by-control against Section 4.0. See [nist-csf-2](../frameworks/nist-csf-2.md).

## Primary sources

- IRS Publication 1075 (Rev. 11-2021), full text — publisher document: https://www.irs.gov/pub/irs-pdf/p1075.pdf
- IRS Office of Safeguards program page (technical-assistance index; reviewed 28 Jun 2026) — regulator guidance: https://www.irs.gov/privacy-disclosure/safeguards-program
- IRS, Reporting improper inspections or disclosures (reviewed 30 Jul 2026) — regulator guidance: https://www.irs.gov/privacy-disclosure/reporting-improper-inspections-or-disclosures
- IRS, 45 day notifications (reviewed 17 Aug 2026) — regulator guidance: https://www.irs.gov/privacy-disclosure/45-day-notifications
- IRS, Safeguard Security Report (reviewed 18 Sep 2026) — regulator guidance: https://www.irs.gov/privacy-disclosure/safeguard-security-report
- IRS, Taxpayer First Act, Section 2004 — contractor on-site reviews, worksheet and annual certification (reviewed 18 Sep 2026) — regulator guidance: https://www.irs.gov/privacy-disclosure/safeguards-program/taxpayer-first-act-section-2004-tfa-2004
- IRS, Internal inspections reports — inspection cycle and templates (reviewed 28 Jun 2026) — regulator guidance: https://www.irs.gov/privacy-disclosure/internal-inspections-reports
- IRS, Cloud computing environment (reviewed 4 Aug 2026) — regulator guidance: https://www.irs.gov/privacy-disclosure/cloud-computing-environment
- IRS, Encryption requirements of Publication 1075 (reviewed 2 Sep 2026) — regulator guidance: https://www.irs.gov/privacy-disclosure/encryption-requirements-of-irs-publication-1075
- IRS, Background investigations (reviewed 17 Aug 2026) — regulator guidance: https://www.irs.gov/privacy-disclosure/background-investigations
- IRS, Safeguards technical assistance: policy and procedures involving a contractor (reviewed 18 Sep 2026) — regulator guidance: https://www.irs.gov/privacy-disclosure/safeguards-technical-assistance-policy-and-procedures-involving-a-contractor
- 26 U.S.C. § 6103 — legal text, Office of the Law Revision Counsel (current through 18 Sep 2026): https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6103&num=0&edition=prelim
- 26 U.S.C. § 7213 — legal text: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section7213&num=0&edition=prelim
- 26 U.S.C. § 7213A — legal text: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section7213A&num=0&edition=prelim
- 26 U.S.C. § 7431 — legal text: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section7431&num=0&edition=prelim
- 26 CFR 301.6103(p)(7)-1, suspension, termination and administrative review — legal text (eCFR): https://www.ecfr.gov/current/title-26/section-301.6103(p)(7)-1
- Public Law 118-258, Supporting America's Children and Families Act, Title II § 202 — legal text: https://www.govinfo.gov/content/pkg/PLAW-118publ258/html/PLAW-118publ258.htm
- 44 U.S.C. § 3609, GSA FedRAMP roles and the FedRAMP Board — legal text: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title44-section3609&num=0&edition=prelim

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
