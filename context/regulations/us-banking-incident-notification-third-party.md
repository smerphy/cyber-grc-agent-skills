# US federal banking regulators: Computer-Security Incident Notification Rule, third-party risk guidance and cyber examination expectations (OCC / FRB / FDIC / NCUA)

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | **Computer-Security Incident Notification Rule** — 12 CFR Part 53 (OCC), 12 CFR Part 225 subpart N, §§ 225.300–303 (Federal Reserve Board), 12 CFR Part 304 subpart C, §§ 304.21–24 (FDIC); final rule 86 FR 66424 (23 Nov 2021). **NCUA cyber incident rule** — 12 CFR 748.1(c); 88 FR 12811 (1 Mar 2023). **Interagency Guidelines Establishing Information Security Standards** — 12 CFR Part 30 App. B (OCC), Part 208 App. D-2 and Part 225 App. F (FRB), Part 364 App. B (FDIC), Part 748 App. A (NCUA), each with a response-program/customer-notice supplement. **Interagency Guidance on Third-Party Relationships: Risk Management** — 88 FR 37920 (9 Jun 2023); FRB SR 23-4 |
| Regulators | OCC (national banks, federal savings associations, federal branches/agencies of foreign banks); FRB (bank and savings-and-loan holding companies, state member banks, US operations of foreign banking organizations, Edge/agreement corporations); FDIC (insured state nonmember banks, insured state savings associations, insured state branches of foreign banks); NCUA (federally insured credit unions) |
| Status and key dates | 36-hour rule effective 1 Apr 2022, compliance 1 May 2022. NCUA 72-hour rule effective 1 Sep 2023. 2023 third-party guidance in force, but **proposed replacement guidance published 15 Sep 2026** (91 FR 58536; comments to 16 Nov 2026). FFIEC Cybersecurity Assessment Tool (CAT) sunset 31 Aug 2025 |
| Who is covered | Every federally supervised banking organization and credit union; **bank service providers** (any person performing services subject to the Bank Service Company Act, 12 U.S.C. 1861–1867) are directly bound by the service-provider notification duty; designated financial market utilities are carved out |
| Structure | Binding rules (incident notification; Guidelines issued as safety-and-soundness standards under s.39 FDI Act) plus non-binding but examined supervisory guidance (third-party risk, FFIEC IT Examination Handbook, agency bulletins/SR letters/FILs) |
| Penalties / enforcement | No rule-specific penalty schedule. Enforcement through the general supervisory toolkit: matters requiring attention, s.39 compliance plans, cease-and-desist orders and civil money penalties under 12 U.S.C. 1818 (three statutory tiers, inflation-adjusted annually) |
| Assessment model | Continuous supervision and periodic IT/safety-and-soundness examinations; no certification. Examiners use the FFIEC IT Examination Handbook; the CAT self-assessment is retired in favour of NIST CSF 2.0 and CISA Cybersecurity Performance Goals |
| Relationship to neighbours | Banking-side counterpart to the FTC Safeguards Rule (non-bank financial institutions — see [glba-ftc-safeguards.md](glba-ftc-safeguards.md)); overlaps with SEC cyber disclosure for listed holding companies, NYDFS Part 500 for New York licensees, state breach laws, and (once final) CIRCIA reporting to CISA |

## What it is

US bank supervision has no single "cyber law". Three federal banking agencies (OCC, Federal Reserve Board, FDIC) and the NCUA regulate information security through a layered set of instruments: (1) the GLBA section 501(b) safeguarding standards, issued as the Interagency Guidelines Establishing Information Security Standards in 2001 and supplemented in 2005 with response-program and customer-notice guidance; (2) the 2021 Computer-Security Incident Notification Rule, the first *mandatory* regulator-notification clock for operational cyber incidents at banks and their service providers; (3) the NCUA's parallel 2023 rule for credit unions; (4) interagency third-party risk management guidance (2023), which replaced three divergent agency issuances; and (5) examination expectations set out in the FFIEC IT Examination Handbook and agency bulletins.

The 2021 rule was deliberately narrow: an *early alert* to the primary federal regulator, with no prescribed form, content or recordkeeping, expected to affect an estimated ~150 incidents a year sector-wide. The agencies rejected a "good faith belief" trigger in favour of a "determination" standard and narrowed "computer-security incident" to *actual* harm. Everything else — the substantive security program, board oversight, vendor due diligence, testing — is driven by the Guidelines and by supervisory guidance that is technically non-binding but enforced through examination findings.

## Who it covers / Scope

| Population | Instrument | Notes |
|---|---|---|
| National banks, federal savings associations, federal branches/agencies of foreign banks | 12 CFR 53; Part 30 App. B | OCC-supervised |
| US bank holding companies and S&L holding companies, state member banks, US operations of foreign banking organizations, Edge/agreement corporations | 12 CFR 225.300–303; Part 208 App. D-2 / Part 225 App. F | Holding companies are in scope of the notification rule, not only the bank |
| Insured state nonmember banks, insured state savings associations, insured state-licensed branches of foreign banks | 12 CFR 304.21–24; Part 364 App. B | FDIC-supervised |
| Federally insured credit unions | 12 CFR 748.1(c); Part 748 App. A and B | NCUA; 72-hour clock, broader trigger |
| Bank service providers | 12 CFR 53.4 / 225.303 / 304.24 | Any "bank service company or other person" performing **covered services** subject to the Bank Service Company Act — core processors, cloud and hosting providers, payment processors and similar. Duty is owed to each affected banking-organization customer and applies "independent of any contractual provisions" |
| Designated financial market utilities | excluded | Not a "banking organization" or "bank service provider" under the rule |
| Non-bank financial institutions (fintechs, lenders, brokers, dealers) | out of scope | FTC Safeguards Rule or SEC/CFTC regimes apply instead; they may still be *bank service providers* when they serve a bank |

The third-party guidance applies to "all banking organizations supervised by the agencies" and defines a third-party relationship as *any business arrangement* with another entity, by contract or otherwise — including affiliates, fintech partners, referral arrangements and merchant payment processing.

## Core obligations

### 1. Computer-Security Incident Notification Rule (banks: 36 hours)

| Element | Requirement (12 CFR 53 / 225 subpart N / 304 subpart C) |
|---|---|
| Computer-security incident | "An occurrence that results in **actual harm** to the confidentiality, integrity, or availability of an information system or the information that the system processes, stores, or transmits" |
| Notification incident | A computer-security incident that has materially disrupted or degraded, or is **reasonably likely** to materially disrupt or degrade: (i) ability to carry out banking operations or deliver products/services to a **material portion of the customer base** in the ordinary course; (ii) **business line(s)** whose failure would cause material loss of revenue, profit or franchise value; or (iii) operations whose failure would **threaten US financial stability** |
| Clock | Regulator must *receive* notice "as soon as possible and no later than **36 hours** after the banking organization **determines** that a notification incident has occurred". The determination may take a reasonable time; the 36 hours runs from it, not from detection. Preamble: same-day notice is the "effective practice" for sector-critical organizations |
| Form and content | None prescribed — email, telephone or "other similar methods" the agency prescribes; only the fact that a notification incident occurred need be conveyed. No recordkeeping requirement. Notices fall under agency confidentiality rules |
| Channels | OCC: BankNet incident submission, BankNet help desk (BankNet@occ.treas.gov, (800) 641-5925) or supervisory office (OCC Bulletin 2022-8, 29 Mar 2022). FDIC: case manager, any on-site examiner, or incident@fdic.gov (FIL-12-2022, 29 Mar 2022). FRB: Board-designated email and telephone (866) 364-0096 (SR 22-4 / CA 22-3, 29 Mar 2022) |
| Examples cited by agencies | Large-scale distributed denial of service, ransomware, failed system upgrades causing widespread outages, and similar events that disrupt customer access or core operations |

### 2. Bank service provider notification (4-hour threshold)

| Element | Requirement (§§ 53.4 / 225.303 / 304.24) |
|---|---|
| Trigger | Provider **determines** it has experienced a computer-security incident that has materially disrupted or degraded, or is reasonably likely to materially disrupt or degrade, **covered services** to a banking organization for **four or more hours** |
| Clock | "As soon as possible" after that determination — the agencies explicitly rejected 36- or 72-hour windows for providers |
| Recipient | At least one **bank-designated point of contact** (email, phone or other contact previously supplied by the bank); if none was supplied, the bank's **CEO and CIO** (or two comparable individuals) by any reasonable means |
| Exemption | Scheduled maintenance, testing or software updates previously communicated to the bank |
| Contract interaction | Contractual notice clauses that meet the standard satisfy the rule, but the duty exists regardless of contract terms |

### 3. NCUA cyber incident rule (credit unions: 72 hours)

| Element | Requirement (12 CFR 748.1(c)) |
|---|---|
| Clock | NCUA must receive notice "as soon as possible but no later than **72 hours** after a federally insured credit union **reasonably believes** that it has experienced a reportable cyber incident" — or, for third-party-caused incidents, within 72 hours of being notified by the third party, whichever is sooner |
| Reportable cyber incident | Any *substantial* cyber incident leading to: (A) substantial loss of confidentiality, integrity or availability of a network or member information system from unauthorized access/exposure of sensitive data, disruption of vital member services, or serious impact on operational resiliency; (B) disruption of business operations, vital member services or a member information system from a cyberattack or exploited vulnerability; or (C) disruption or unauthorized data access "facilitated through, or caused by, a compromise of a credit union service organization, cloud service provider, or other third-party data hosting provider or by a supply chain compromise" |
| Exclusion | Events performed in good faith at the specific request of the system owner/operator (authorized testing) |
| Channel and content | Telephone 1-833-CYBERCU or cybercu@ncua.gov; an early alert only — no detailed assessment required within 72 hours. NCUA aligned the "substantial"/72-hour language with CIRCIA |

### 4. Interagency Guidelines Establishing Information Security Standards (GLBA s.501(b))

Issued as safety-and-soundness standards (12 U.S.C. 1831p-1) — for the OCC, 12 CFR Part 30 App. B; equivalents at Part 208 App. D-2 / Part 225 App. F (FRB), Part 364 App. B (FDIC), Part 748 App. A (NCUA, "member information").

| Section (App. B) | Obligation |
|---|---|
| II.A–B | Comprehensive **written** information security program with administrative, technical and physical safeguards, sized to the institution, designed to ensure security and confidentiality of customer information, protect against anticipated threats and unauthorized access causing substantial harm, and ensure proper disposal |
| III.A | **Board** (or committee) approves the written program and oversees development, implementation and maintenance, assigning specific responsibility and reviewing management reports |
| III.B | **Risk assessment**: identify reasonably foreseeable internal/external threats, assess likelihood and potential damage, assess sufficiency of controls |
| III.C.1 | Consider and adopt as appropriate: access controls; physical access restrictions; **encryption** in transit and at rest; change-control consistent with the program; dual control, segregation of duties and background checks; **intrusion monitoring**; **response programs** including reports to regulators and law enforcement; environmental/technology-failure protections |
| III.C.2–4 | Train staff; **regularly test** key controls with tests conducted or reviewed by independent parties; disposal measures |
| III.D | **Service providers**: due diligence in selection; **contractual** requirement to implement appropriate measures; risk-based monitoring, reviewing audits, test summaries or equivalent evaluations |
| III.E–F | Adjust the program for changes in technology, threats and business arrangements (M&A, outsourcing); **report to the board at least annually** on program status, risk assessment, control decisions, service-provider arrangements, test results, security breaches and management responses |
| Supplement A (2005) — response program | At minimum: assess nature and scope; **notify the primary federal regulator "as soon as possible"** on awareness of unauthorized access to or use of *sensitive customer information*; notify law enforcement and file a timely SAR where required; contain and control while preserving evidence; notify customers when warranted. Where the incident is at a service provider, the institution stays responsible for regulator and customer notice (it may contract the provider to do it); provider contracts should require notice to the institution "as soon as possible" |
| Supplement A — customer notice | Investigate promptly; if misuse "has occurred or is reasonably possible", notify affected customers **as soon as possible** (delay only on a law-enforcement **written** request). *Sensitive customer information* = name/address/phone plus SSN, driver's licence, account or card number, PIN/password, or any combination allowing account access. If the affected group cannot be pinpointed, notify the whole group. Notice must be clear and conspicuous, describe the incident and data types, protective steps, a contact number, a 12–24-month vigilance reminder and identity-theft guidance; notify nationwide consumer reporting agencies before large mailings |

Supplement A section III was amended by the interagency reputation-risk rule (91 FR 18279, 10 Apr 2026; effective 9 Jun 2026) — wording changes to the customer-notice rationale only; the notice standard is unchanged.

### 5. Interagency Guidance on Third-Party Relationships: Risk Management (June 2023)

Rescinded and replaced OCC Bulletin 2013-29 and its 2020 FAQs (OCC Bulletin 2020-10), FRB SR 13-19 and FDIC FIL-44-2008. Principles-based, "does not impose any new requirements", but is the yardstick examiners apply.

| Stage / theme | Expectation |
|---|---|
| Inventory and risk tiering | Complete inventory of all third-party relationships; periodic risk assessment per relationship; identify **critical activities** (could cause significant risk if the third party fails, significant customer impact, or significant impact on financial condition/operations) for more comprehensive oversight |
| Planning | Assess risk, strategic fit, complexity and resources before engaging, in proportion to criticality |
| Due diligence and selection | Scaled to risk: strategies and goals, legal/regulatory compliance, financial condition, business experience, key personnel, risk management, **information security**, management of information systems, **operational resilience**, **incident reporting and management**, physical security, reliance on subcontractors, insurance, contracts with other parties; document limitations where information is unavailable |
| Contract negotiation | Nature and scope, performance measures, information handling and retention, **right to audit and require remediation**, compliance responsibility, confidentiality and integrity, **operational resilience and business continuity**, indemnification and liability limits, insurance, subcontracting, foreign-based third parties, default and termination, **regulatory supervision**; acknowledge limited leverage with dominant providers and manage the residual gap |
| Ongoing monitoring | Commensurate with risk; may use collaborative arrangements or external parties; review performance, control effectiveness, audits, financial condition, and changes in the third party's environment |
| Termination | Plan for orderly exit, **timely return or destruction of data**, post-termination access/connection controls and continuity of critical activities |
| Oversight and accountability | Runs throughout the life cycle: board has ultimate oversight; management establishes policies and executes; independent review and documentation/reporting |
| Supervisory reviews | Agencies review the effectiveness of the program as part of supervision; separately, services subject to the Bank Service Company Act are themselves subject to agency examination |

Supplemental resources (which the 2026 proposal would also replace): *Third-Party Risk Management: A Guide for Community Banks* (3 May 2024 — OCC Bulletin 2024-11, SR 24-2/CA 24-1, FIL-19-2024); joint statement on bank arrangements with third parties to deliver deposit products (25 Jul 2024 — OCC Bulletin 2024-20, SR 24-5, FIL-45-2024); interagency RFI on community banks' engagement with core service providers (90 FR 54882, 28 Nov 2025).

### 6. Examination expectations

- **FFIEC IT Examination Handbook** — the examiner's reference; booklets updated on their own cycle: *Architecture, Infrastructure, and Operations* (June 2021, FIL-47-2021); *Development, Acquisition, and Maintenance* (August 2024, FIL-60-2024); *Business Continuity Management* (2019 (verify)); *Information Security* (2016 (verify)).
- **FFIEC Cybersecurity Assessment Tool** — voluntary self-assessment available since 2015, **sunset 31 Aug 2025** (OCC Bulletin 2024-25, 29 Aug 2024; FIL-61-2024). Agencies point instead to NIST CSF 2.0 and CISA's Cybersecurity Performance Goals; see [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md).
- **Largest firms** — Interagency Paper on Sound Practices to Strengthen Operational Resilience (SR 20-24) and, for large OCC banks, the Heightened Standards risk-governance framework at 12 CFR Part 30 App. D.

## Enforcement and penalties

| Mechanism | Detail |
|---|---|
| Examination findings | Matters requiring attention and downgraded management/IT ratings are the everyday consequence; guidance breaches surface here, not in court |
| s.39 FDI Act (12 U.S.C. 1831p-1) | Failure to meet the Guidelines can require a **compliance plan**; failure to submit or implement one supports an enforceable order under 12 U.S.C. 1818(b) |
| Cease-and-desist and formal agreements | 12 U.S.C. 1818(b); violation of the Guidelines "may be an unsafe and unsound practice" (12 CFR 30.1(b)) |
| Civil money penalties (12 U.S.C. 1818(i)(2)) | Statutory base tiers: first tier up to $5,000 per day; second tier (reckless/pattern) up to $25,000 per day; third tier (knowing, with substantial loss or gain) up to the lesser of $1,000,000 per day or 1% of total assets. Amounts are inflation-adjusted annually (OCC: 12 CFR 19.240) — current adjusted ceilings are materially higher; verify the agency's latest notice before quoting |
| Notification rule specifics | No penalty schedule or recordkeeping duty in the rule itself; late or missed notice is pursued as a violation of regulation through the tools above |
| Service providers | Reachable directly under the Bank Service Company Act examination authority and through the bank's contract |

## Timeline and status

| Date | Event |
|---|---|
| 1 Jul 2001 | Interagency Security Guidelines compliance date (66 FR 8633) |
| 29 Mar 2005 | Response-program and customer-notice guidance added as Supplement A (70 FR 15751) |
| 12 Jan 2021 | Notification rule proposed |
| 23 Nov 2021 | Final Computer-Security Incident Notification Rule, 86 FR 66424 |
| 1 Apr 2022 / 1 May 2022 | Rule effective / compliance date; agencies publish points of contact (29 Mar 2022) |
| 1 Mar 2023 | NCUA final rule, 88 FR 12811; effective 1 Sep 2023 |
| 9 Jun 2023 | Interagency Guidance on Third-Party Relationships, 88 FR 37920 (SR 23-4 dated 7 Jun 2023) |
| 3 May 2024 / 25 Jul 2024 | Community bank TPRM guide; joint statement on deposit-product arrangements plus bank-fintech RFI |
| 29 Aug 2024 → 31 Aug 2025 | CAT sunset announced → CAT retired |
| 28 Nov 2025 | RFI on community banks' engagement with core service providers |
| 10 Apr 2026 (eff. 9 Jun 2026) | Reputation-risk rule amends Part 30 and Part 364 App. B Supplement A wording |
| 19 May 2026 | Executive Order 14405 on integrating fintech innovation into regulatory frameworks — cited as a driver of the 2026 proposal |
| 15 Sep 2026 | **Proposed Third-Party Risk Management Guidance** (OCC, FRB, FDIC, NCUA), 91 FR 58536: four components — risk identification and assessment, risk oversight, residual risk acceptance, governance; expressly "non-enforceable"; would replace the 2023 guidance and supplemental resources. Same day, FRB proposed a *Third-Party Risk Management Guide for Traditional Community Banking Organizations* (< $30 billion in assets), 91 FR 58438. Comments on both due 16 Nov 2026 |

As of September 2026 the 36-hour rule is unamended (only Paperwork Reduction Act renewals in 2024–2025), and the 2023 third-party guidance remains the operative standard until a final replacement is issued.

## Key obligations for security/GRC teams

1. **Map your charter to the right rule set** (OCC/FRB/FDIC/NCUA; holding company vs bank; whether you are also a *bank service provider* to other institutions). See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Wire the 36-hour (or 72-hour) determination into incident severity triage**: define who makes the "determination", log its timestamp, pre-load regulator contacts and a one-paragraph notice template. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
3. **Run the Supplement A response program in parallel**: regulator notice on unauthorized access to sensitive customer information, SAR/law-enforcement steps, and customer notice when misuse is reasonably possible — a data incident can trigger this even if it never reaches the 36-hour operational threshold.
4. **Give every bank service provider a designated point of contact** (monitored mailbox/phone), and require providers to notify "as soon as possible" for 4-hour disruptions and for any unauthorized access to customer information in contracts. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../workflows/vendor-onboarding.md](../../workflows/vendor-onboarding.md).
5. **Maintain a complete third-party inventory with criticality tiering**; evidence due diligence, contract clauses, monitoring and exit plans proportionate to tier — and track the 2026 proposal, which shifts emphasis to assessed risk and residual-risk acceptance. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).
6. **Keep the Guidelines evidence current**: board-approved written program, documented risk assessment, independent control testing, and the **annual board report** covering the enumerated topics. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md) and [../../templates/grc-board-report.md](../../templates/grc-board-report.md).
7. **Replace CAT-based self-assessment** with a NIST CSF 2.0 profile (or CIS-based baseline for smaller institutions) and retain crosswalks for examiners. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md) and [../frameworks/cis-controls-v8.md](../frameworks/cis-controls-v8.md).
8. **Prepare for IT examinations** against the FFIEC Handbook booklets in scope; keep prior MRAs and remediation evidence organised. See [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).
9. **Document accepted gaps** (e.g., a core provider that will not accept audit rights) as formal exceptions with compensating controls. See [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).

## Interplay

- **GLBA / FTC Safeguards Rule**: same statute, different regulator. Banks follow the Guidelines above; non-bank financial institutions follow 16 CFR Part 314 and its 30-day FTC breach notice. A bank's fintech partner may sit under the FTC rule while also being the bank's *service provider*. See [glba-ftc-safeguards.md](glba-ftc-safeguards.md).
- **SEC cybersecurity disclosure**: a listed bank holding company faces Form 8-K materiality analysis alongside the 36-hour regulator alert — different tests, different audiences. See [sec-cyber-disclosure.md](sec-cyber-disclosure.md).
- **NYDFS Part 500**: New York-licensed institutions add a 72-hour DFS notice and stricter prescriptive controls (23 NYCRR 500.17); see the separate NYDFS Part 500 pack when available.
- **State breach-notification laws**: customer notice under Supplement A does not displace state statutes; many exempt GLBA-compliant institutions, but the exemption wording varies. See [us-state-privacy.md](us-state-privacy.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
- **CIRCIA**: CISA's 72-hour critical-infrastructure reporting (proposed 89 FR 23644, 4 Apr 2024) is designed to run alongside the banking rule; the NCUA already aligned its terminology. Confirm the final-rule status before building a combined playbook.
- **Cross-border groups**: US operations of foreign banks are inside the FRB/OCC rules; EU parents also face DORA's major-incident reporting ([dora.md](dora.md)) and UK groups the operational-resilience regime ([uk-financial-operational-resilience.md](uk-financial-operational-resilience.md)).
- **Frameworks**: NIST CSF 2.0 and CISA CPGs are the agencies' named CAT successors; SOC 2 reports remain the standard evidence for service-provider monitoring under Guidelines III.D ([../frameworks/soc2-tsc.md](../frameworks/soc2-tsc.md)).

## Primary sources

- 12 CFR Part 53 (OCC), 12 CFR 225.300–303 (FRB), 12 CFR 304.21–24 (FDIC) — eCFR, legal text: https://www.ecfr.gov/current/title-12/chapter-I/part-53 ; https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-225/subpart-N ; https://www.ecfr.gov/current/title-12/chapter-III/subchapter-B/part-304/subpart-C
- Final rule, 86 FR 66424 (23 Nov 2021) — Federal Register: https://www.federalregister.gov/documents/2021/11/23/2021-25510/computer-security-incident-notification-requirements-for-banking-organizations-and-their-bank-service-providers
- Agency points of contact — OCC Bulletin 2022-8: https://www.occ.gov/news-issuances/bulletins/2022/bulletin-2022-8.html ; FDIC FIL-12-2022: https://www.fdic.gov/news/financial-institution-letters/2022/fil22012.html ; FRB SR 22-4: https://www.federalreserve.gov/supervisionreg/srletters/SR2204.htm
- 12 CFR 748.1(c) (NCUA), legal text: https://www.ecfr.gov/current/title-12/chapter-VII/subchapter-A/part-748 ; final rule 88 FR 12811: https://www.federalregister.gov/documents/2023/03/01/2023-03682/cyber-incident-notification-requirements-for-federally-insured-credit-unions ; NCUA reporting page: https://www.ncua.gov/regulation-supervision/letters-credit-unions-other-guidance/cyber-incident-notification-requirements
- 12 CFR Part 30 App. B and Supplement A (Interagency Security Guidelines; response programs), legal text: https://www.ecfr.gov/current/title-12/chapter-I/part-30
- Interagency Guidance on Third-Party Relationships, 88 FR 37920 (9 Jun 2023): https://www.federalregister.gov/documents/2023/06/09/2023-12340/interagency-guidance-on-third-party-relationships-risk-management ; FRB SR 23-4: https://www.federalreserve.gov/supervisionreg/srletters/SR2304.htm
- Proposed Third-Party Risk Management Guidance, 91 FR 58536 (15 Sep 2026): https://www.federalregister.gov/documents/2026/09/15/2026-18859/proposed-third-party-risk-management-guidance ; FRB proposed community bank guide, 91 FR 58438: https://www.federalregister.gov/documents/2026/09/15/2026-18852/proposed-third-party-risk-management-guide-for-traditional-community-banking-organizations
- RFI on core service providers, 90 FR 54882 (28 Nov 2025): https://www.federalregister.gov/documents/2025/11/28/2025-21333/request-for-information-regarding-community-banks-engagement-with-core-service-providers-and-other
- Reputation-risk rule amending Part 30/364 App. B, 91 FR 18279 (10 Apr 2026): https://www.federalregister.gov/documents/2026/04/10/2026-06947/prohibition-on-the-use-of-reputation-risk-by-regulators
- CAT sunset — OCC Bulletin 2024-25: https://www.occ.gov/news-issuances/bulletins/2024/bulletin-2024-25.html ; FDIC FIL index 2024 (FIL-61-2024, FIL-60-2024, FIL-19-2024, FIL-45-2024): https://www.fdic.gov/news/financial-institution-letters/2024/ ; FDIC FIL index 2021 (FIL-47-2021): https://www.fdic.gov/news/financial-institution-letters/2021/
- 12 U.S.C. 1818 (enforcement, civil money penalty tiers): https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title12-section1818&num=0&edition=prelim ; 12 CFR 19.240 (OCC inflation adjustment): https://www.ecfr.gov/current/title-12/chapter-I/part-19/subpart-O
- Not reachable when checked: ffiec.gov / ithandbook.ffiec.gov (blocked) — FFIEC booklet dates for Business Continuity Management and Information Security are therefore marked (verify).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
