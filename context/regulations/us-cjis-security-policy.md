# FBI CJIS Security Policy (CJISSECPOL) — Criminal Justice Information

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | *Criminal Justice Information Services (CJIS) Security Policy*, current version **6.1, dated 25 June 2026** (prepared by the FBI CJIS Information Security Officer; approved by the CJIS Advisory Policy Board and the Compact Council). Not a statute or rule: a policy imposed through user agreements, management control agreements and the Security Addendum |
| Legal underpinnings | 28 U.S.C. §534 (FBI record exchange); **28 CFR Part 20** (criminal history record information — CHRI), notably §20.3(d) definition, §20.21(f) state security standards, §20.33(a)(7) private-contractor access via an Attorney-General-approved Security Addendum, §20.35 (Advisory Policy Board), §20.38 (cancellation of access for non-compliance). The policy's executive summary also cites the Federal Information Security Modernization Act of 2014 |
| Publisher / governance | FBI CJIS Division; changes recommended by the **CJIS Advisory Policy Board (APB)** and approved by the FBI Director; the National Crime Prevention and Privacy Compact Council governs interstate CHRI exchange for noncriminal justice purposes |
| Structure | Sections 1–4 (introduction, approach, roles, CJI/CHRI/PII); Section 5 = Policy Area 1 (Information Exchange Agreements) + requirements organised by **NIST SP 800-53 Rev. 5 control family** (AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PS, RA, SA, SC, SI, SR) + Policy Area 20 (Mobile Devices); Appendices A–I (terms, sample agreements, best practices incl. G.3 Cloud Computing and G.6 Encryption, H Security Addendum) |
| Who is covered | "All entities with access to, or that operate systems which are used to process, store, or transmit CJI" (§1.2) — criminal justice agencies, noncriminal justice agencies, and every contractor/private entity supporting them, including cloud providers |
| Enforcement | Triennial audits (CSA of its agencies; FBI CJIS Division of each CSA/SIB/Interface Agency); administrative sanctions up to termination of CJIS services; contractor access suspended/terminated under the Security Addendum; 28 CFR §20.25 civil penalty (inflation-adjusted to **$36,498** per violation for penalties assessed after 3 July 2025); state and federal criminal penalties for misuse of CHRI |
| Certifiable? | **No.** The FBI does not certify products or providers. Compliance is attested contractually (Security Addendum, state CJIS agreements) and verified by CSA/FBI audit; third-party assessments and FedRAMP/StateRAMP/SOC 2 may be leveraged but "do not guarantee compliance" (App. G.3) |
| Sanctionable set | Since **1 October 2024**: all pre-modernisation ("existing") requirements plus **[Priority 1]** modernised controls. [Priority 2]–[Priority 4] controls sit in a **"zero-cycle" from 1 October 2024 to 30 September 2027** (§1.4) |
| Neighbours | NIST SP 800-53 Rev. 5 (control source), FedRAMP/StateRAMP (cloud assurance), FISMA (federal agencies), state breach-notification laws (CJI is PII), IRS Publication 1075 (parallel federal-data regime) |

## What it is

The CJIS Security Policy is the minimum security baseline for **Criminal Justice Information (CJI)** — the data flowing through FBI CJIS systems such as NCIC, the Interstate Identification Index (III) and biometric services. Its executive summary describes it as integrating presidential directives, federal laws, FBI directives and decisions of the criminal and noncriminal justice community under a "shared management philosophy": the FBI sets the floor, each state's **CJIS Systems Agency (CSA)** administers it locally, and agencies may impose stricter controls (§1.3, §3.2.1).

Two structural facts drive practical work. First, the policy was **modernised**: v6.0 (27 December 2024, "Policy Modernization Completion") replaced the thirteen numbered policy areas of the 5.9.x series with NIST SP 800-53 Rev. 5 control-family text, and v6.1 (25 June 2026) folded in the APB's Spring 2025 corrections plus administrative changes approved by the Security and Access Subcommittee on 14 November 2025. Second, since v5.9.5 every modernised control carries an **[Existing]** or **[Priority 1–4]** marking that determines whether it is currently sanctionable (§1.4). Since v6.0 the policy is a public document that "may be posted and shared without restrictions" (§1.5) — earlier versions were distribution-restricted.

## Who it covers / Scope

| Question | Answer (v6.1) |
|---|---|
| Applicability test | Access to CJI, or operation of a system that processes, stores or transmits CJI (§1.2). Applies to "every individual — contractor, private entity, noncriminal justice agency representative, or member of a criminal justice entity" (Executive Summary) |
| CJI categories (§4.1) | Biometric data; identity history data; biographic data; property data (when accompanied by PII); case/incident history. Transaction control numbers (ORI, NIC, UCN) alone are exempt |
| CHRI (§4.1.1) | Subset of CJI with additional access/use/dissemination controls; defined and governed by 28 CFR Part 20; III and NCIC are the named CHRI systems. CJI released to the public through the courts or authorised dissemination leaves scope |
| Criminal Justice Agency (CJA) (§3.2.4) | Court, governmental agency or subunit performing the administration of criminal justice under statute/executive order and allocating a substantial part of its budget to it |
| Noncriminal Justice Agency (NCJA) (§3.2.5) | Entity providing services primarily for purposes other than the administration of criminal justice (e.g., licensing bodies using CHRI); interstate NCJA use is also governed by Compact Council rules |
| Contractors | Reach CJI only under a specific agreement with a CJA/NCJA that incorporates the **Security Addendum** (28 CFR §20.33(a)(7); App. H) or, for noncriminal justice functions, the Compact Council Outsourcing Standard for Non-Channeling (SA-9) |
| Geographic limit | CJI, encrypted or not, may be stored only in environments physically within an **APB-member country (US, US territories, Indian Tribes, Canada)** under the legal authority of an APB-member agency (SC-28) — with narrow exceptions for international exchange agreements |
| Role vocabulary (§3.2) | CSA; CJIS Systems Officer (CSO — cannot be outsourced); Terminal Agency Coordinator (TAC); Contracting Agency (CA); Agency Coordinator; CSA Information Security Officer (CSA ISO); "Organizational Personnel with Security Responsibilities" (formerly LASO); FBI CJIS ISO; Repository Manager; Interface Agency (IA) Official; State Compact Officer |

## Core obligations

### Governance and agreements

| Requirement | Where | Detail |
|---|---|---|
| Formal information exchange agreements before CJI is exchanged | §5.1, CA-3, App. D | Agreements specify security controls, roles and data ownership; reviewed at least triennially or on change of responsibilities/signatories; log secondary dissemination of CHRI |
| CSO duties | §3.2.2 | Sets personnel selection/supervision/separation standards; approves access to FBI CJIS systems; appoints CSA ISO; ensures a TAC and a security-responsible person at every agency with access |
| System authorisation | CA-6 | Named senior official authorises each system before operation; authorisations refreshed at least every 3 years |
| Control assessment | CA-2 (P3) | Assess controls at least every 3 years; report results to the CJIS User Agreement signatory |
| Local policy | §1.3 | Agency must maintain documented policy and procedures implementing the CJISSECPOL; the policy is always the minimum standard |

### Technical and operational controls (selected, with priority marking)

| Control | Marking | Requirement (v6.1 text) |
|---|---|---|
| IA-2(1), IA-2(2) | P1 | **Multi-factor authentication for privileged and non-privileged accounts** |
| IA-5 j | — | Authentication at NIST **AAL2**: a multi-factor authenticator or two single-factor authenticators; cryptographic authenticators use approved cryptography; at least one authenticator replay-resistant; verifiers and authenticators used by federal agencies validated to FIPS 140 Level 1 |
| AC-7 | P3 (existing) | Lock after **5 consecutive invalid logons within 15 minutes**, until released by an administrator |
| AC-11 | P4 (existing) | Device lock after a maximum of **30 minutes** of inactivity (safety carve-outs for in-vehicle and dispatch devices) |
| AC-2 | P1 | Automatic removal of temporary and emergency accounts within 72 hours |
| SC-8 / SC-13 | P2 (existing) | Encrypt CJI in transit outside a physically secure location using **FIPS 140-3 certified modules or FIPS 197 (AES) with ≥256-bit keys**. Note: "FIPS 140-2 certificates will not be acceptable after **September 21, 2026**" |
| SC-28 | P2 (existing) | Same cryptographic bar for CJI at rest outside physically secure locations; metadata derived from unencrypted CJI protected as CJI and never used for advertising or commercial purposes by a cloud provider |
| PS-3 | P2 (existing) | **State-of-residency and national fingerprint-based record checks** before access (under an FBI-approved authority such as Public Law 92-544); felony conviction = denial (variance only via CSO/designee review); maintain a list of personnel with unescorted access to unencrypted CJI; rescreening recommended |
| AT-2 | P2 (existing) | Security/privacy literacy training before access to CJI and annually; within 30 days of an incident for those involved; content updated annually |
| RA-5 | P1 | Vulnerability scanning at least **monthly**; remediate **critical 15 / high 30 / medium 60 / low 90 days** |
| SI-2 | P1 (existing) | Install security-relevant updates within the same 15/30/60/90-day windows |
| AU-11 | P4 (existing) | Retain audit records at least **1 year** |
| IR-6 | P2 | Personnel report suspected incidents immediately, **not to exceed 1 hour after discovery**, to the organisation's IR capability; incident information goes to the CSO / SIB Chief / IA Official **and the FBI CJIS ISO**; supply-chain partners informed (IR-6(3)) |
| IR-8 | P2 (existing) | Documented incident response plan defining reportable incidents, metrics and resources; App. F.1 provides the Security Incident Response Form |
| SA-9 | — | Agencies must **triennially audit all external service providers** with system access, permit inspection of alleged violations, and may conduct unannounced inspections of contractor facilities; a CSA may audit a contractor on behalf of another CSA and share results |
| §5.20 | — | Mobile devices: usage restrictions, MDM, wireless controls and mobile-specific IR/authentication requirements augmenting the family controls |

### Third parties, cloud and the Security Addendum

- **Security Addendum (App. H)** — the Attorney-General-approved instrument required by 28 CFR §20.33(a)(7) whenever a private contractor performs the administration of criminal justice. The contractor must "maintain a security program consistent with … the CJIS Security Policy in effect when the contract is executed and all subsequent versions" (§3.01); the contracting government agency must give **every contractor employee** a copy of the Addendum and the policy and retain their signed (hand or digital) acknowledgment for audit (§2.01); security violations must be reported to the CSO and the FBI Director, can justify termination, and the FBI may suspend or terminate access and services; on termination contractor records containing CHRI are deleted or returned (§4.0).
- **Cloud (App. G.3, SC-28)** — no "CJIS-certified" status exists; the CJIS ISO Program advises against giving the cloud provider access to CJI encryption keys, restricts CJI storage to APB-member-country jurisdictions, and states that FedRAMP, StateRAMP, SOC 2 and similar authorisations "may be leveraged, however, they do not guarantee compliance." In practice hyperscalers sign the Security Addendum state by state, submit in-scope personnel to CSA fingerprint checks, and publish attestations or third-party assessment reports against v6.x.
- **Contractor personnel** — subject to the same PS-3 screening, AT training and audit exposure as agency staff; a criminal record found on a contractor triggers notification of the Contracting Agency and a fitness review before access.

## Enforcement and penalties

| Mechanism | Source | Detail |
|---|---|---|
| Triennial audit cycle | App. D.1 CJIS User Agreement; CA-2 | Each CSA/IA/SIB audits every agency accessing CJIS systems through it at least every three years; each CSA/IA/SIB is itself audited triennially by the FBI CJIS Division; the User Agreement is reviewed every three years by the FBI |
| Sanctionable requirements | §1.4 | From 1 October 2024: pre-modernisation ("existing") requirements and Priority 1 controls; P2–P4 in zero-cycle until 30 September 2027 |
| Administrative sanctions | §4.2.5.2; 28 CFR §20.38 | Improper access, use or dissemination of CHRI/NCIC data "may result in administrative sanctions including, but not limited to, termination of services and state and federal criminal penalties"; FBI may cancel system access for non-compliance with 28 CFR Part 20 subpart C |
| Civil penalty | 28 CFR §20.25, adjusted by 28 CFR §85.5 | Up to $36,498 per violation of subpart B (state/local CHRI systems) assessed after 3 July 2025 ($35,574 for the prior adjustment period); OJP may also initiate fund cut-off |
| Contractor consequences | App. H §4.0 | Report to CSO and FBI Director; termination of the agreement; FBI suspension/termination of access and telecommunications links, reinstated only after satisfactory assurances |

## Timeline and status

| Date | Event |
|---|---|
| 10 May 1999 | FBI notice of proposed rulemaking to revise 28 CFR §20.33(a)(7), creating the private-contractor / Security Addendum route (recounted in App. H) |
| 2022–2024 | v5.9.1 (Oct 2022) through v5.9.4 (Dec 2023) progressively "modernise" policy areas into 800-53 Rev. 5 control text; v5.9.5 (July 2024) adds Existing/Priority markings |
| 1 October 2024 | Existing requirements + Priority 1 controls become the sanctionable set; zero-cycle starts for P2–P4 |
| 27 December 2024 | **v6.0** — Policy Modernization Completion; 800-53 family structure throughout Section 5 |
| 25 June 2026 | **v6.1** — incorporates calendar-year 2025 APB changes (Spring 2025 APB #16, SA #1–3) and 14 November 2025 administrative changes; current version as of September 2026 |
| 21 September 2026 | FIPS 140-2 certificates no longer acceptable for CJI encryption (SC-13 note) |
| 30 September 2027 | Zero-cycle for P2–P4 modernised controls ends (§1.4); expect them to become auditable/sanctionable thereafter — confirm against the APB's implementing decision (verify) |
| Ongoing | APB meets twice yearly (spring/fall); administrative changes flow through the Security and Access Subcommittee; a v6.2 incorporating 2026 changes is plausible in 2027 (verify) |

## Key obligations for security/GRC teams

1. **Determine whether you touch CJI at all** — any system, vendor, SaaS or support path that stores, processes or transmits CJI (including encrypted backups and metadata) is in scope; map data flows before mapping controls. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Prioritise by marking**: build the control inventory from the v6.1 List of Priorities, close every [Existing] and [Priority 1] gap first (MFA, RA-5/SI-2 patch windows, AC-2), and schedule P2–P4 against the 30 September 2027 zero-cycle end. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md) and [../frameworks/nist-800-53.md](../frameworks/nist-800-53.md).
3. **Retire FIPS 140-2 dependencies** before 21 September 2026 — inventory VPNs, TLS terminators, HSMs, disk encryption and mobile crypto against active FIPS 140-3 certificates; track exceptions formally ([../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md)).
4. **Personnel security pipeline**: fingerprint-based checks under a valid statutory authority, felony-denial rule, unescorted-access list, annual training records — evidence the CSA auditor asks for first. Templates: [../../templates/audit-evidence-request-list.md](../../templates/audit-evidence-request-list.md).
5. **Wire the 1-hour internal report and FBI CJIS ISO notification into incident response**, alongside any state breach-notification clock triggered because CJI contains PII. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
6. **Contract hygiene**: every private contractor needs the executed Security Addendum plus per-employee acknowledgments; cloud contracts need US/APB-country residency, customer-controlled keys where feasible, no commercial use of metadata, and audit/inspection rights that satisfy SA-9. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../workflows/vendor-onboarding.md](../../workflows/vendor-onboarding.md).
7. **Run the triennial cadence as a programme**: control assessment (CA-2), authorisation refresh (CA-6), agreement review (CA-3), provider audits (SA-9) and CSA/FBI audits all sit on three-year clocks — align them on one calendar. See [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).
8. **Report to leadership** on sanctionable-control coverage, patch-window compliance, MFA coverage and audit findings; CSA findings carry service-termination risk. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **NIST SP 800-53 Rev. 5** — v6.x lifts control text, discussion and enhancement numbering directly from Rev. 5, with CJIS-specific parameters (e.g., 15/30/60/90-day remediation, 1-hour reporting). An existing 800-53 or FedRAMP Moderate implementation is the natural starting inventory; the deltas are the parameters, the personnel-screening regime and the Security Addendum. See [../frameworks/nist-800-53.md](../frameworks/nist-800-53.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
- **FedRAMP / StateRAMP** — useful evidence for a cloud provider's control inheritance but explicitly not a substitute for CJIS compliance (App. G.3); the state CSA, not FedRAMP, decides. StateRAMP now operates under the GovRAMP name (verify).
- **FISMA** — federal agencies using CJIS systems already run 800-53 baselines under FISMA; the policy cites FISMA 2014 as further legal basis (see the FISMA context pack, `us-fisma-federal-cyber`, if present in this repository).
- **IRS Publication 1075** — the closest sibling regime (federal tax information in state agencies): also 800-53-derived, also with background-check and on-site inspection expectations; agencies handling both should harmonise the two control sets.
- **State breach-notification and privacy laws** — CJI is PII; an incident can trigger the CJIS 1-hour/FBI ISO chain *and* state resident/AG notification duties. See [us-state-privacy.md](us-state-privacy.md).
- **CIS Controls / ISO 27001 / SOC 2** — acceptable as an operating framework beneath the policy, and SOC 2 reports are named as leverageable assurance, but none maps one-to-one; CJIS parameters override where stricter. See [../frameworks/cis-controls-v8.md](../frameworks/cis-controls-v8.md), [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md), [../frameworks/soc2-tsc.md](../frameworks/soc2-tsc.md).
- **HIPAA / GLBA** — no direct overlap, but the same personnel-screening, encryption and vendor-agreement evidence often serves multiple regimes; see [hipaa.md](hipaa.md) and [glba-ftc-safeguards.md](glba-ftc-safeguards.md).

## Primary sources

- CJIS Security Policy v6.1 (25 June 2026) — official policy text, FBI file repository: https://le.fbi.gov/file-repository/cjis_security_policy_v6-1_20260625.pdf (FBI site blocks scripted access; text was obtained from an archived copy of the same file)
- CJIS Security Policy Resource Center (current version, Requirements Companion Document PDF/Excel, Use Cases): https://le.fbi.gov/cjis-division/cjis-security-policy-resource-center (publisher page; read via archived copy)
- CJIS Security Policy v6.0 (27 December 2024) — prior version, used for the modernisation change summary: https://le.fbi.gov/file-repository/cjis_security_policy_v6-0_20241227.pdf (archived copy)
- 28 CFR Part 20 — Criminal Justice Information Systems (legal text, eCFR): https://www.ecfr.gov/current/title-28/chapter-I/part-20
- 28 CFR Part 85 §85.5 — DOJ civil penalty inflation adjustments (legal text, eCFR): https://www.ecfr.gov/current/title-28/chapter-I/part-85
- 28 CFR Part 20, 2025 annual edition (govinfo, legal text): https://www.govinfo.gov/content/pkg/CFR-2025-title28-vol1/pdf/CFR-2025-title28-vol1-part20.pdf
- Secondary (cloud-provider compliance pages, used only for the "no certification"/attestation practice and to corroborate the v6.1 date): Microsoft Learn CJIS offering page; AWS CJIS compliance page; Google Cloud CJIS compliance page

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
