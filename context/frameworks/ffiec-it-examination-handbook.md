# FFIEC Information Technology Examination Handbook (FFIEC IT Handbook)

## At a glance

| Attribute | Detail |
|---|---|
| Publisher | Federal Financial Institutions Examination Council — a statutory interagency body (12 U.S.C. 3303) whose members are the Comptroller of the Currency, the FDIC Chairman, a designated Federal Reserve Governor, the CFPB Director, the NCUA Board Chairman, and the Chairman of the State Liaison Committee |
| What it is | A series of examiner booklets (each with narrative guidance plus examination work programs) that define supervisory expectations for IT and cybersecurity risk management at banks, thrifts, credit unions and their technology service providers |
| Status | Living series; booklets are revised individually and superseded editions are kept in an archive section. Ten booklets were current as of September 2026. The series replaced the 1996 FFIEC Information Systems Examination Handbook, retired when the last two booklets were issued in 2004 (FDIC FIL-119-2004, 10 November 2004) |
| Legal force | Supervisory guidance, not a rule. It is the lens examiners use to apply rules that *do* bind — GLBA §501(b) security standards, the Bank Service Company Act, the computer-security incident notification rules |
| Who is covered | Federally insured depository institutions — banks, thrifts and credit unions — supervised by an FFIEC member agency, plus the technology service providers examined under the Bank Service Company Act |
| Rating model | Uniform Rating System for Information Technology (URSIT): four components — Audit, Management, Development and Acquisition, Support and Delivery (AMDS) — plus a composite, each on a 1–5 scale in ascending order of supervisory concern (64 FR 3109) |
| Certifiable? | No. There is no certification or attestation; the output is an examination rating and, where warranted, supervisory findings and enforcement |
| Self-assessment tooling | The FFIEC Cybersecurity Assessment Tool (June 2015) was removed from the FFIEC website on 31 August 2025 with no replacement; the FFIEC declined to update it for NIST CSF 2.0 and CISA's Cybersecurity Performance Goals and pointed institutions to industry-developed self-assessment resources |
| Live 2026 issue | Interagency third-party risk management guidance is being rewritten: proposed guidance at 91 FR 58536 and a companion community-bank guide at 91 FR 58438 (both 15 September 2026), comments close 16 November 2026 |

## What it is

The FFIEC IT Handbook is the shared examination doctrine of the US federal banking agencies. Each booklet pairs a narrative statement of expectations with a work program examiners actually execute, so the Handbook simultaneously tells an institution what "sound" looks like and how it will be tested. It is not a control catalogue in the ISO or NIST 800-53 sense: it states outcomes and management processes, and leaves control selection to the institution.

Its authority is indirect but real. The Handbook interprets binding requirements — principally the Interagency Guidelines Establishing Information Security Standards issued under Gramm-Leach-Bliley Act §501(b) (12 CFR part 30 App. B for OCC-supervised banks, 12 CFR part 364 App. B for FDIC-supervised banks) and the Bank Service Company Act's examination authority over service providers. Because examiners rate against URSIT and cite Handbook expectations in findings, a Handbook gap can become a supervisory finding long before it becomes a rule violation — though the OCC and FDIC final rule at 91 FR 56004 (effective 2 November 2026) defines "unsafe or unsound practice" and revises the framework for issuing matters requiring attention.

Two structural features matter for GRC planning. First, booklets age at very different rates: the Information Security and Management booklets predate NIST CSF 2.0 and mainstream cloud adoption, while Architecture, Infrastructure, and Operations (2021) explicitly addresses cloud computing, microservices, zero trust, artificial intelligence and the internet of things, and Development, Acquisition, and Maintenance (2024) rewrote change control and acquisition expectations around enterprise-wide, process-oriented delivery. Second, much current supervisory expectation now arrives *outside* the Handbook — as interagency statements, agency-specific examination programs and rules — so a Handbook-only reading of the regime is incomplete.

## Who it covers / Scope

- **Supervised institutions.** National banks and federal savings associations (OCC), state member banks and holding companies (Federal Reserve), state nonmember banks and state savings associations (FDIC), and federally insured credit unions (NCUA). State supervisors participate through the State Liaison Committee and generally examine to the same Handbook.
- **Technology service providers.** Under the Bank Service Company Act, where a supervised depository institution has services performed for it by contract or otherwise, "such performance shall be subject to regulation and examination by such agency to the same extent as if such services were being performed by the depository institution itself on its own premises" (12 U.S.C. 1867(c)(1)). Core processors, item processors and major cloud/fintech providers to banks are examined on this basis and receive their own URSIT ratings; examiners review the resulting service provider reports of examination at the client institution. The NCUA states that it lacks direct regulatory authority over credit union service organizations, and reviews them independently or jointly with state supervisory authorities instead.
- **Notification of service relationships.** The institution must notify its federal banking agency of the existence of a covered service relationship within **thirty days** after the contract is made or the service begins, whichever occurs first (12 U.S.C. 1867(c)(2)).
- **No size exemption.** There is no asset threshold below which the Handbook stops applying; proportionality is applied in examination judgment. Separate rules do carry thresholds — for example, the OCC Heightened Standards apply to banks with average total consolidated assets of **$50 billion or more** (12 CFR part 30 App. D, para. I.A.).
- **Not covered.** Non-bank financial firms outside FFIEC member supervision (broker-dealers, insurers, most fintechs contracting directly with consumers) are outside the Handbook, though they often meet it indirectly as bank service providers or through contractual flow-down.

## Structure and requirements

### The booklets

| Booklet | Current edition | Notes |
|---|---|---|
| Architecture, Infrastructure, and Operations (AIO) | June 2021 | Replaced the Operations booklet (June 2004); covers cloud computing, microservices, zero trust, AI/ML and IoT in a dedicated "Evolving Technologies" section |
| Development, Acquisition, and Maintenance (DA&M) | August 2024 | Issued 29 August 2024; replaced Development and Acquisition (April 2004); governance of IT development, acquisition, maintenance and change control; the issuance "does not impose new requirements on examined entities" |
| Business Continuity Management (BCM) | November 2019 | Replaced the Business Continuity Planning booklet (February 2015), which carried Appendix J on third-party resilience and was superseded on 14 November 2019 |
| Management | November 2015 | IT governance, risk management, board and senior management responsibilities |
| Information Security | September 2016 | Replaced the July 2006 edition on 9 September 2016; the security-program booklet examiners cite alongside the GLBA Security Guidelines |
| Supervision of Technology Service Providers (TSP) | October 2012 | Rescinded the March 2003 edition; describes the interagency risk-based TSP supervision program; its Appendix A restates URSIT |
| Outsourcing Technology Services | June 2004 | Never revised; overlaps heavily with, and is being overtaken by, interagency third-party guidance |
| Audit | Edition date not printed in the published booklet (verify) | Feeds the URSIT Audit component; covers internal audit programs, outsourced internal audit and third-party reviews of service providers |
| Retail Payment Systems | April 2016 | Includes Appendix E on mobile financial services |
| Wholesale Payment Systems | July 2004 | Interbank/intrabank payment, messaging and securities settlement |

The FFIEC keeps superseded editions on an archived-booklets page; an E-Banking booklet that once sat in the series appears on neither the current nor the archived list as of 2026. Booklet titles and edition dates should be confirmed against the FFIEC's own Handbook site before being quoted in an audit deliverable; the series is revised booklet-by-booklet without a version number for the whole Handbook.

### Adjacent FFIEC and interagency issuances that examiners apply

| Issuance | Date | Substance |
|---|---|---|
| Authentication and Access to Financial Institution Services and Systems | 11 August 2021 | Replaced the 2005 *Authentication in an Internet Banking Environment* and its 2011 supplement; risk assessment drives authentication; covers customers, employees, third parties and **service accounts**; MFA or controls of equivalent strength |
| Cybersecurity Assessment Tool (CAT) | June 2015 – 31 August 2025 | Voluntary inherent-risk/maturity self-assessment; the FFIEC announced the sunset on 29 August 2024 (Announcement 2024-03) and the FDIC relayed it on 5 September 2024 (FIL-61-2024), because the FFIEC chose not to update the tool for NIST CSF 2.0 and the CISA Cybersecurity Performance Goals |
| Interagency Guidance on Third-Party Relationships: Risk Management | 88 FR 37920, 9 June 2023 | Federal Reserve, FDIC, OCC; replaced each agency's own general third-party guidance; life cycle of planning, due diligence and third-party selection, contract negotiation, ongoing monitoring and termination, with oversight and accountability running throughout rather than as a stage |
| Third-Party Risk Management: A Guide for Community Banks | 3 May 2024 | Supplemental resource to the 2023 guidance (FDIC FIL-20-2024) |
| Statement on Bank Arrangements with Third Parties to Deliver Deposit Products, issued with a request for information on bank-fintech arrangements | 25 July 2024 | Bank-fintech deposit arrangements (FDIC FIL-46-2024) |

### The rules the Handbook interprets

| Requirement | Citation | Core duty |
|---|---|---|
| Information security program (GLBA §501(b)) | 12 CFR part 364 App. B (FDIC); 12 CFR part 30 App. B (OCC) | Written, risk-based program; assess risk; manage and control; train; test; adjust |
| Service provider oversight | Same appendices, para. III.D | Exercise due diligence in selection; **require service providers by contract** to implement measures meeting the Guidelines' objectives; monitor |
| Board reporting | Same appendices, para. III.F | Report to the board or a board committee **at least annually** on program status, risk decisions, service provider arrangements, testing results and breaches |
| Incident response and customer notice | Supplement A to App. B | Response program; notify the primary federal regulator as soon as possible on unauthorized access to sensitive customer information; notify affected customers where misuse has occurred or is reasonably possible, subject to law-enforcement delay |
| Computer-security incident notification | 12 CFR 304.22–304.24 (FDIC); parallel OCC and Federal Reserve rules | Notify the agency **as soon as possible and no later than 36 hours** after determining a notification incident occurred; a **bank service provider** must notify affected bank customers as soon as possible when a covered service is materially disrupted or degraded for **four or more hours** |
| Credit union incident notification | 12 CFR 748.1(c) | Notify NCUA as soon as possible but **no later than 72 hours** after reasonably believing a reportable cyber incident occurred |
| Heightened standards (large national banks) | 12 CFR part 30 App. D | Risk governance framework with three lines — front line units, independent risk management, internal audit — for banks at or above $50 billion average total consolidated assets |

See [us-banking-incident-notification-third-party.md](../regulations/us-banking-incident-notification-third-party.md) for the notification rules in depth.

## Assessment, certification and evidence

- **URSIT (64 FR 3109, 20 January 1999).** Replaced the 1978 Information Systems rating system. Composite and component ratings run 1–5 in ascending order of supervisory concern. The composite is a qualitative summary, explicitly **not** an arithmetic average: the notice states that where the audit function is inadequate, "the overall integrity of the IT systems is not readily verifiable," so a composite of 3–5 would normally be appropriate. Ratings apply to service providers as well as institutions.
- **FDIC InTREx.** The Information Technology Risk Examination program took effect 1 July 2016, replacing the IT-RMP. It is built on URSIT with Core Modules for the Audit, Management, Development and Acquisition, and Support and Delivery components, incorporates procedures to assess compliance with the Part 364 App. B security standards, and uses a pre-examination **Information Technology Profile** — sent roughly 90 days ahead — with **65 percent fewer questions** than the legacy IT Officer's Questionnaire. Updated 29 September 2023 to add examiner steps for the computer-security incident notification rule (effective 1 April 2022) and for reviewing service provider reports of examination.
- **NCUA Information Security Examination (ISE).** Implemented in 2023 to standardize credit union information security examinations; supported by the voluntary Automated Cybersecurity Evaluation Toolbox (ACET), whose declarative statements map to FFIEC IT Handbook practices, regulatory guidance and the NIST Cybersecurity Framework. The program also draws on the NCUA Examiner's Guide, the National Supervision Policy Manual and credit union service organization reviews.
- **Evidence that examiners expect.** Board and committee minutes showing the annual security-program report; the current risk assessment; the service provider inventory with BSCA notifications; contracts showing the required security clauses; internal and external audit reports with tracked remediation; testing results (penetration tests, vulnerability scans, BCM exercises); incident logs with notification decisions and timestamps. See [audit-preparation](../../skills/audit-preparation/SKILL.md) and [control-testing](../../skills/control-testing/SKILL.md).
- **No certification exists.** Claims that a firm is "FFIEC certified" are meaningless; what exists is an examination rating, a service provider report of examination, or a self-assessment against a mapped framework.

## Timeline and status

| Date | Event |
|---|---|
| 20 January 1999 | URSIT published (64 FR 3109), introducing the AMDS components |
| 2003–2004 | Modern booklet series issued; the 1996 IS Examination Handbook was retired with the Operations and Wholesale Payment Systems booklets, issued by the FFIEC on 26 August 2004 (FDIC FIL-119-2004, 10 November 2004) |
| June 2015 | Cybersecurity Assessment Tool released |
| 1 July 2016 | FDIC InTREx examination program effective |
| 11 August 2021 | Authentication and Access guidance replaces the 2005/2011 authentication guidance |
| 1 April 2022 | Computer-security incident notification rule (36-hour clock) effective |
| 9 June 2023 | Interagency Guidance on Third-Party Relationships published (88 FR 37920) |
| 29 September 2023 | FDIC updates InTREx procedures for the incident notification rule and service provider report review (FIL-52-2023) |
| 29 August 2024 | Development, Acquisition, and Maintenance booklet issued (FDIC FIL-60-2024) |
| 29 August – 5 September 2024 | CAT sunset announced by the FFIEC (Announcement 2024-03) and communicated to supervised institutions (FDIC FIL-61-2024) |
| 31 August 2025 | CAT removed from the FFIEC website |
| 28 November 2025 | Interagency request for information on community banks' engagement with core service providers and other essential third-party service providers (90 FR 54882; comments closed 27 January 2026) |
| 19 May 2026 | FFIEC proposes revisions to the Uniform Financial Institutions Rating System (CAMELS) — 91 FR 29128; comment period closed 17 August 2026. The proposal addresses UFIRS, not URSIT |
| 1 September 2026 | OCC and FDIC final rule defining "unsafe or unsound practice" and revising the matters-requiring-attention framework — 91 FR 56004, effective 2 November 2026 |
| 11–15 September 2026 | OCC, Federal Reserve, FDIC and NCUA — the NCUA was not party to the 2023 guidance — propose third-party risk management guidance that would **rescind and replace** the 2023 guidance and certain supplemental resources (91 FR 58536), with a companion Proposed Third-Party Risk Management Guide for Traditional Community Banking Organizations (91 FR 58438); comments on both close 16 November 2026. Issued with a Joint Statement on Community Banks' Engagement with Core Service Providers (FDIC FIL-58-2026, 11 September 2026) |

As of September 2026 the proposed third-party guidance is not final; the 2023 guidance, the community bank guide and the bank-fintech deposit statement remain in effect until any final replacement is issued. No FFIEC IT Handbook booklet has been revised since the August 2024 DA&M booklet.

## Key obligations for security/GRC teams

1. **Map the control set to booklet expectations, not to the CAT.** With the CAT retired, pick a durable spine — NIST CSF 2.0 or the CRI Profile — and map booklet expectations into it once. See [nist-csf-2.md](nist-csf-2.md), [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).
2. **Keep the GLBA security-program artifacts current and board-visible** — risk assessment, program document, testing results, and the at-least-annual board report required by App. B para. III.F. See [glba-ftc-safeguards.md](../regulations/glba-ftc-safeguards.md).
3. **Maintain the service provider inventory as a regulatory record**: BSCA 30-day notifications, criticality tiering, contract security clauses, and current service provider reports of examination. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md) and [vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md).
4. **Re-baseline third-party programs against the September 2026 proposals** — tailoring practices to the reasonably assessed risk of each relationship is their central theme; comment or prepare to re-tier before any final guidance lands. See [new-regulation-impact-assessment.md](../../workflows/new-regulation-impact-assessment.md).
5. **Wire the notification clocks into incident response**: the 36-hour agency clock (72 hours for credit unions), the service provider's four-hour disruption trigger, and the separate Supplement A customer-notice path. See [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md) and [breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
6. **Treat authentication as a risk-assessment output**, covering customers, employees, third parties and service accounts, per the 2021 guidance — service accounts are the most common gap.
7. **Protect the URSIT Audit component.** A weak IT audit function drags the composite rating down independently of control quality; keep an independent, risk-based IT audit plan with tracked remediation.
8. **Exercise and evidence business continuity and recovery** against the BCM booklet, including third-party dependency scenarios. See [iso-22301-business-continuity.md](iso-22301-business-continuity.md).
9. **Report IT risk to the board in supervisory language** — ratings, findings, remediation status, third-party concentration. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md) and [risk-assessment](../../skills/risk-assessment/SKILL.md).

## Interplay

- **GLBA Security Guidelines** are the binding layer under the Handbook for banks; the FTC Safeguards Rule covers non-bank financial institutions instead — see [glba-ftc-safeguards.md](../regulations/glba-ftc-safeguards.md).
- **NIST CSF 2.0 and CISA's Cybersecurity Performance Goals** are the resources the agencies named when retiring the CAT — see [nist-csf-2.md](nist-csf-2.md) and [cisa-cpg-secure-by-design.md](cisa-cpg-secure-by-design.md).
- **CRI Profile v2.2** is the financial-sector overlay most commonly used in examinations and third-party due diligence: aligned to NIST CSF v2, with 318 diagnostic statements, about 40 mappings to regulatory and standards references, and an impact questionnaire that scopes which statements apply.
- **SOC reports** are the usual evidence substitute where on-site review of a provider is impractical; they do not discharge the institution's own oversight duty. See [soc2-tsc.md](soc2-tsc.md) and [soc1-isae3402-soc-reports.md](soc1-isae3402-soc-reports.md).
- **SOX ITGC** work overlaps the URSIT Audit and Development and Acquisition components for public banking organizations, but tests financial-reporting assertions rather than safety and soundness — see [sox-itgc.md](../regulations/sox-itgc.md).
- **State and sectoral overlays** add their own clocks and program requirements on the same estate — see [us-nydfs-part-500.md](../regulations/us-nydfs-part-500.md) and [us-naic-insurance-data-security.md](../regulations/us-naic-insurance-data-security.md).
- **Non-US analogues** for a group with cross-border operations: [dora.md](../regulations/dora.md), [uk-financial-operational-resilience.md](../regulations/uk-financial-operational-resilience.md) and [australia-apra-cps-234-230.md](../regulations/australia-apra-cps-234-230.md). DORA's register of information and the BSCA service-relationship inventory can be built from one dataset.

## Primary sources

- Statute — 12 U.S.C. 3303, FFIEC composition: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title12-section3303
- Statute — Bank Service Company Act, 12 U.S.C. 1861–1867: https://www.govinfo.gov/content/pkg/COMPS-254/pdf/COMPS-254.pdf
- Statute — 12 U.S.C. 1867, examination of services performed by contract and the thirty-day notice: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title12-section1867
- Official notice — Uniform Rating System for Information Technology, 64 FR 3109 (20 January 1999): https://www.govinfo.gov/content/pkg/FR-1999-01-20/pdf/99-1175.pdf
- Regulation — Interagency Guidelines Establishing Information Security Standards and Supplement A, 12 CFR part 364 App. B: https://www.ecfr.gov/current/title-12/chapter-III/subchapter-B/part-364
- Regulation — computer-security incident notification, 12 CFR part 304 subpart C: https://www.ecfr.gov/current/title-12/chapter-III/subchapter-A/part-304/subpart-C
- Regulation — NCUA cyber incident notification, 12 CFR 748.1(c): https://www.ecfr.gov/current/title-12/chapter-VII/subchapter-A/part-748/section-748.1
- Regulation — OCC Heightened Standards, 12 CFR part 30 App. D: https://www.ecfr.gov/current/title-12/chapter-I/part-30
- Regulator guidance — FDIC FIL-61-2024, *Sunset of FFIEC Cybersecurity Assessment Tool*: https://www.fdic.gov/news/financial-institution-letters/2024/sunset-ffiec-cybersecurity-assessment-tool
- Regulator guidance — FDIC FIL-60-2024, *Updated FFIEC IT Examination Handbook – Development, Acquisition, and Maintenance Booklet* (29 August 2024): https://www.fdic.gov/news/financial-institution-letters/2024/updated-ffiec-it-examination-handbook-development
- Regulator guidance — FDIC FIL-52-2023, *Information Technology Risk Examination (InTREx) Procedures* (29 September 2023), with the InTREx Information Technology Profile attached: https://www.fdic.gov/news/financial-institution-letters/2023/fil23052.html
- Regulator guidance — FDIC FIL-58-2026, *Proposed Interagency Third-Party Risk Management Guidance and Issuance of Joint Statement on Community Banks' Engagement with Core Service Providers* (11 September 2026): https://www.fdic.gov/news/financial-institution-letters/2026/proposed-interagency-third-party-risk-management-guidance
- Regulator guidance — FDIC FIL-20-2024, *Third-Party Risk Management: A Guide for Community Banks* (3 May 2024): https://www.fdic.gov/news/financial-institution-letters/2024/third-party-risk-management-guide-community-banks
- Regulator index — FDIC financial institution letters (FIL-47-2021 and FIL-55-2021 on the AIO booklet and the authentication guidance; FIL-43-2016 on InTREx; FIL-119-2004 on completion of the booklet series): https://www.fdic.gov/news/financial-institution-letters
- Regulator guidance — FDIC Banker Resource Center, *Information Technology (IT) and Cybersecurity*: https://www.fdic.gov/banker-resource-center/information-technology-it-and-cybersecurity
- Official notice — Interagency Guidance on Third-Party Relationships: Risk Management, 88 FR 37920: https://www.federalregister.gov/documents/2023/06/09/2023-12340/interagency-guidance-on-third-party-relationships-risk-management
- Official notice — Proposed Third-Party Risk Management Guidance, 91 FR 58536 (comments close 16 November 2026): https://www.federalregister.gov/documents/2026/09/15/2026-18859/proposed-third-party-risk-management-guidance
- Official notice — Proposed Third-Party Risk Management Guide for Traditional Community Banking Organizations, 91 FR 58438: https://www.federalregister.gov/documents/2026/09/15/2026-18852/proposed-third-party-risk-management-guide-for-traditional-community-banking-organizations
- Official notice — Request for Information Regarding Community Banks' Engagement With Core Service Providers and Other Essential Third-Party Service Providers, 90 FR 54882: https://www.federalregister.gov/documents/2025/11/28/2025-21333/request-for-information-regarding-community-banks-engagement-with-core-service-providers-and-other
- Final rule — Unsafe or Unsound Practices, Matters Requiring Attention, 91 FR 56004 (OCC and FDIC, effective 2 November 2026): https://www.federalregister.gov/documents/2026/09/01/2026-17823/unsafe-or-unsound-practices-matters-requiring-attention
- Official notice — FFIEC, Uniform Financial Institutions Rating System proposal, 91 FR 29128: https://www.federalregister.gov/documents/2026/05/19/2026-09944/uniform-financial-institutions-rating-system
- Regulator guidance — NCUA Information Security Examination and Cybersecurity Assessment Program (ISE, ACET): https://ncua.gov/regulation-supervision/regulatory-compliance-resources/cybersecurity-resources/ncuas-information-security-examination-and-cybersecurity-assessment
- Publisher page — Cyber Risk Institute, CRI Profile overview (v2.2): https://cyberriskinstitute.org/cri-profile-overview/
- Publisher site — FFIEC IT Handbook InfoBase, https://ithandbook.ffiec.gov — **blocks automated access (HTTP 403)**; the booklet editions above were taken from the booklets' own cover pages and the member agencies' issuance letters


---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
