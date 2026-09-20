# Swift Customer Security Programme (CSP) and Customer Security Controls Framework (CSCF)

## At a glance

| Attribute | Detail |
|---|---|
| Publisher | Swift (S.W.I.F.T. SC), the Belgian cooperative that operates the interbank messaging network; headquartered in La Hulpe, overseen by the G-10 central banks with the National Bank of Belgium in the lead role |
| Instrument | Customer Security Programme (CSP), announced 27 May 2016, built on five strategic initiatives; its control baseline is the Customer Security Controls Framework (CSCF), first issued 2017 |
| Current edition | CSCF v2026, published on the Swift Knowledge Centre in July 2025 (file `CSCF_v2026_202507015.pdf`) and in force for the 2026 attestation cycle. A v2027 edition is expected under the July cadence but could not be confirmed from public pages as of September 2026 (verify) |
| Who is covered | Every Swift user, scoped to its own local Swift infrastructure; applicable controls depend on which of the **five architecture types** (A1–A4, B) the user falls into |
| Structure | 3 objectives → 7 principles → numbered controls, each marked **mandatory** or **advisory**; control definitions are written in line with ISO 27002, PCI DSS, SOC 2 and NIST CSF |
| Control count | Low 30s in recent editions; the mandatory/advisory split moves every year, so read the count off the CSCF document for the version you are attesting against (verify) |
| Annual cycle | New version published each July for the *following* year; attestation window **1 July – 31 December**; attest no later than 31 December and re-attest at least annually |
| Certifiable? | No certificate. Annual **self-attestation in KYC-SA**, which must be supported by an **independent assessment** (internal, external, or a mixed team) performed under the Independent Assessment Framework (IAF) |
| Enforcement | Swift reserves the right to report non-attesting or non-compliant users to their local supervisors; non-compliance is surfaced in a real-time application accessible to the user's supervisor, and attestation status is visible to counterparties in KYC-SA |

## What it is

The CSP is Swift's community security programme: a mandatory security baseline plus a transparency mechanism. It was announced on 27 May 2016, weeks after the theft of USD 81 million from Bangladesh Bank's account at the Federal Reserve Bank of New York, in which attackers used malware on the victim's own local Swift interface estate to issue fraudulent payment messages and suppress the confirmations that would have revealed them. The lesson Swift drew — and the premise of the whole programme — is that the network was not breached; the *users' own endpoints* were. The CSCF therefore governs what each institution does inside its own perimeter, not what Swift does inside the network.

Three things make CSP unusual among frameworks. First, it is contractual and near-universal: every Swift user must attest, there is no scoping-out, and there is no "we are too small" tier. Second, compliance data is **shared**: counterparties can read each other's attestations through KYC-SA, which turns CSCF status into a commercial and correspondent-banking due-diligence signal rather than a private audit artefact. Third, it is explicitly annual and ratcheting — advisory controls are published as a preview of future mandatory controls, so this year's advisory list is next year's project plan.

Swift also publishes product-specific **Security Guidance (SG)** documents for its messaging interfaces (configuration-level guidance that complements the product-agnostic CSCF), and the **Customer Security Controls Policy**, which carries the attestation rules, timelines and non-compliance follow-up.

## Who it covers / Scope

- **All Swift users.** The CSCF defines the security baseline applicable to all users; which controls apply depends on the user's connectivity to Swift.
- **Architecture types.** Swift publishes an architecture decision tree that places each user in one of five types (A1, A2, A3, A4, B). Broadly, the A types describe increasing degrees of *local* Swift-related footprint (messaging interface, communication interface, connector, hardware security modules) and type B describes users with no such local footprint; the applicable mandatory and advisory control set follows from that classification. Confirm the exact definitions in the current CSCF before relying on a classification (verify).
- **Scope creep via connectors.** CSCF v2025 began classifying **customer client connectors** (API consumers, middleware, file-transfer clients) as in-scope customer connectors regardless of whether the endpoint is a server or a client. CSCF v2026 makes those requirements mandatory, which can reclassify a type B user that uses an application-to-application client connector into **type A4**. A type B user connecting only through user-to-application flows (for example a browser GUI) is not affected.
- **Service providers in the chain.** Users connecting through a Swift connectivity provider (service bureau, L2BA, Business Connect) still own the controls covering their own footprint, and connecting through a *non-compliant* provider is itself a breach of the attestation policy.
- **Outsourcing is not a transfer of accountability.** Control 2.8 covers protection of the local Swift infrastructure from risks created by outsourcing critical activities; the user remains the attesting party.

## Structure and requirements

Three objectives, seven principles (Swift's own phrasing, September 2026):

| Objective | Principles |
|---|---|
| Secure your environment | 1. Restrict internet access and segregate critical systems from the general IT environment · 2. Reduce attack surface and vulnerabilities · 3. Physically secure the environment |
| Know and limit access | 4. Prevent compromise of credentials · 5. Manage identities and segregate privileges |
| Detect and respond | 6. Detect anomalous activity to system or transaction records · 7. Plan for incident response and information sharing |

Controls are numbered `principle.control`. A trailing **A** marks a control that is advisory in that edition; when it is promoted, the suffix is dropped. The list below reflects control objectives as published in the CSCF mappings for v2022 and assessor material for v2025/v2026 — check numbering, titles and mandatory status against the edition you are attesting against.

| # | Control objective (abbreviated) |
|---|---|
| 1.1 | Protect the local Swift infrastructure from compromised elements of the general IT and external environment (the "secure zone") |
| 1.2 | Restrict and control allocation and use of administrator-level operating system accounts |
| 1.3 | Secure the virtualisation or cloud platform and the VMs hosting Swift-related components to the same level as physical systems |
| 1.4 | Control and protect internet access from operator PCs and systems inside the secure zone |
| 1.5 / 1.5A | Protect the customer's connectivity infrastructure (customer environment protection) |
| 2.1 | Confidentiality, integrity and authenticity of application data flows between local Swift components |
| 2.2 | Minimise known technical vulnerabilities: vendor support, mandatory software updates, risk-aligned security updates |
| 2.3 | System hardening of Swift-related components |
| 2.4 | Back-office data flow security — confidentiality, integrity and mutual authenticity to the back-office first hops (**mandatory from v2026**) |
| 2.5A | Protect Swift-related data transmitted or stored outside the secure zone |
| 2.6 | Confidentiality and integrity of interactive operator sessions |
| 2.7 | Regular vulnerability scanning of the local Swift environment, with follow-up |
| 2.8A | Protect the local Swift infrastructure from risks created by outsourcing critical activities |
| 2.9 | Keep outbound transaction activity within the expected bounds of normal business |
| 2.11A | Restrict transaction activity to validated and approved business counterparties (relationship management) |
| 3.1 | Physical security of sensitive equipment, workplaces, hosting sites and storage |
| 4.1 | Password policy resistant to common password attacks |
| 4.2 | Multi-factor authentication for access to Swift-related systems and applications |
| 5.1 | Logical access control: need-to-know, least privilege, separation of duties for operator accounts |
| 5.2 | Management, tracking and use of connected/disconnected hardware or personal tokens |
| 5.3A | Regular screening of staff operating the local Swift environment |
| 5.4 | Physical and logical protection of the recorded-password repository |
| 6.1 | Malware protection, with follow-up on results |
| 6.2 | Software integrity of Swift-related components |
| 6.3 | Database integrity for the messaging interface or customer connector |
| 6.4 | Record security events; detect anomalous actions and operations (logging and monitoring) |
| 6.5A | Detect and contain anomalous network activity in the local or remote Swift environment |
| 7.1 | Consistent and effective cyber incident management |
| 7.2 | Security awareness for all staff and maintained security knowledge for privileged staff |
| 7.3A | Penetration testing to validate the operational security configuration |
| 7.4A | Scenario-based risk and readiness assessment against plausible cyber-attack scenarios |

**Change management.** Changes are announced mid-year and users get up to 18 months to implement them; new mandatory controls are first introduced as advisory, giving at least two cycles to plan and budget. Emergency releases are possible but rare.

## Assessment, certification and evidence

| Element | Requirement |
|---|---|
| Attestation | Submitted annually in the **KYC-Security Attestation (KYC-SA)** application; the new controls version appears in KYC-SA in early July; submit between July and December, no later than 31 December; new joiners attest before going live |
| Independent assessment | Every user must undergo a **Community Standard Assessment** under the IAF to support the attestation. Self-assessment is still technically possible in the tool but is treated as non-compliant |
| Who may assess | Internal team, external provider, or a mixed team — all equally valid, provided the assessment is independent. Internal teams must sit outside the first line of defence (typically Internal Audit, Risk, or a purpose-built independent team) |
| Assessor qualification | Demonstrable cyber-security assessment experience against an industry standard such as PCI DSS, ISO 27002 or NIST CSF; the lead assessor must hold at least one industry-relevant certification (for example CISA); Swift also runs a **CSP Assessor Certification** for external and internal assessors and publishes a certified-assessor directory |
| Report re-use | A previous assessment may be referenced on re-attestation if the assessor agrees, the in-scope footprint has not materially changed, and the new CSCF adds no uncovered mandatory controls — with a hard ceiling of **two years from the issuance date of the report** |
| Disclosure in the attestation | Naming the internal department or external firm that performed the assessment is mandatory; naming the individual lead assessor is advisory |
| Mandated external assessment | Swift can require a specific user to undergo an external assessment; failure to complete it is a policy breach |
| Breach conditions | No valid (or expired) attestation · not compliant with applicable mandatory controls · no independent assessment · connecting through a non-compliant service provider · not completing a Swift-mandated external assessment |
| Consequence | Swift reserves the right to report such users to their local supervisors, and non-compliance is made visible in a real-time application accessible to the user's supervisor. Counterparties can also read attestation data in KYC-SA and act on it commercially |

There is no fine schedule and no certificate: the sanctions are supervisory visibility and counterparty reaction. For evidence handling see [audit-preparation](../../skills/audit-preparation/SKILL.md) and the [audit evidence request list](../../templates/audit-evidence-request-list.md).

## Timeline and status

| Date | Event |
|---|---|
| February 2016 | USD 81 million taken from Bangladesh Bank's account at the New York Fed through the victim's own Swift interface estate — the trigger event |
| 27 May 2016 | Swift announces the Customer Security Programme (five strategic initiatives) |
| 2017 | First CSCF published |
| 2018 | Attestation against applicable mandatory controls becomes an annual obligation (secondary source) |
| July 2021 | Independent assessment required to support the attestation, under the Independent Assessment Framework (secondary source) |
| July 2024 | CSCF v2025 published (`CSCF_v2025_20240701.pdf`); customer client connectors start being brought into scope, with type B → A4 consequences |
| July 2025 | CSCF v2026 published (`CSCF_v2026_202507015.pdf`): control 2.4 back-office data flow security becomes mandatory and customer connectors become mandatory in-scope components for controls 1.2, 1.3, 1.4, 2.2, 2.3, 2.6, 2.7, 3.1, 4.1, 4.2, 5.1, 5.4, 6.1 and 6.4 |
| 1 July – 31 December 2026 | Attestation window for CSCF v2026 — the live cycle as of September 2026 |
| July 2026 (expected) | CSCF v2027 publication under the standard cadence — not confirmed from public sources at the time of writing (verify) |

## Key obligations for security/GRC teams

1. **Fix the architecture type first.** Run the decision tree before anything else; the whole control scope, and therefore the assessment fee and remediation budget, follows from it. Re-run it whenever connectivity changes. See [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md).
2. **Re-scope for customer connectors.** Inventory every application-to-application endpoint (API clients, middleware, file transfer) touching Swift directly or through a provider; under v2026 these are mandatory in-scope components and may move a type B user to A4.
3. **Close control 2.4 before the window.** Back-office data flow security is the v2026 promotion — mutual authentication, integrity and confidentiality on the first hop to core banking and payment hubs is a project, not a configuration change.
4. **Book the independent assessment early.** Assessor capacity is concentrated in H2; agree scope, architecture type and evidence list in writing, and decide internal vs external vs mixed team against the IAF independence tests. See [control-testing](../../skills/control-testing/SKILL.md).
5. **Track report validity.** If you plan to re-use last year's assessment, check the two-year ceiling, the "no material change" condition and whether the new CSCF adds uncovered mandatory controls — all three must hold.
6. **Diarise the attestation.** KYC-SA opens in early July and the deadline is 31 December; treat an expired attestation as an incident, because the breach conditions include expiry as well as non-compliance.
7. **Manage gaps as formal exceptions.** A partially implemented mandatory control must be declared truthfully in the attestation; run it through [exception-management](../../skills/exception-management/SKILL.md) with an owner and a date rather than rounding up the score.
8. **Use counterparty attestation data.** Pull correspondent attestations from KYC-SA into third-party risk assessment and correspondent due diligence. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md) and the [vendor security questionnaire](../../templates/vendor-security-questionnaire.md).
9. **Report status to the board with the supervisory angle.** Non-compliance is visible to your supervisor in real time; that is the framing executives need. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).
10. **Wire Swift-specific scenarios into incident response.** Control 7.1 and 7.4A expect plausible-scenario readiness — fraudulent message issue, confirmation suppression, operator credential compromise — and Swift incidents frequently trigger separate regulatory clocks. See [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md).

## Interplay

- **DORA.** For EU financial entities the Swift estate sits inside DORA's ICT risk-management, testing and third-party scope. CSCF evidence is reusable for DORA's ICT controls and for the register of information, but DORA's major-incident reporting clocks are independent of CSP — a fraudulent-message incident is reported to the financial supervisor under DORA regardless of attestation status. See [dora.md](../regulations/dora.md) and [breach notification timelines](../crosswalks/breach-notification-timelines.md).
- **NIS2.** Banks in scope of both generally follow DORA as *lex specialis* for ICT risk and incident reporting; CSCF remains a contractual overlay on top of either. See [nis2.md](../regulations/nis2.md).
- **PCI DSS.** The closest operational cousin: segmentation of a defined zone, hardening, MFA, logging, annual independent validation. Assessors and evidence often overlap, and Swift explicitly accepts PCI DSS assessment experience as an assessor qualification. See [pci-dss-4.md](pci-dss-4.md).
- **ISO 27001 / NIST CSF / SOC 2.** Swift writes control definitions in line with ISO 27002, PCI DSS, SOC 2 and NIST CSF, so an ISO-certified or CSF-aligned programme covers much of the CSCF conceptually — but the CSCF's prescriptive, architecture-specific detail (secure zone, token handling, message-level controls) is not satisfied by a generic ISMS. See [iso-27001-2022.md](iso-27001-2022.md), [nist-csf-2.md](nist-csf-2.md), [soc2-tsc.md](soc2-tsc.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).
- **CIS Controls.** Useful as the implementation-level layer for CSCF hygiene controls (inventory, hardening, logging, malware, recovery). See [cis-controls-v8.md](cis-controls-v8.md).
- **Mapping discipline.** CSCF applicability is architecture-driven, so mappings from other frameworks are coverage aids only, never equivalence claims. See [control-mapping](../../skills/control-mapping/SKILL.md) and [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).

## Primary sources

- Swift, *Customer Security Programme (CSP)* programme page — attestation and independent-assessment deadline of 31 December, annual July CSCF release (publisher page; swift.com blocks scripted access, read via the Internet Archive capture of 2 February 2026).
- Swift, *Swift Customer Security Controls Framework* (security controls page) — mandatory vs advisory controls, three objectives, change-management process (publisher page, via Internet Archive capture of 16 January 2026).
- Swift, *Understand Controls* — three objectives and seven principles, five architecture types and decision tree, alignment with ISO 27002 / PCI DSS / SOC 2 / NIST CSF, July publication a year ahead of effect (publisher page, via Internet Archive capture of 7 August 2026).
- Swift, *Security Attestation* and *Submit KYC-Security Attestation* — attestation window, breach conditions, supervisor reporting and real-time supervisor visibility (publisher pages, via Internet Archive captures of 28 October 2025 and 10 May 2026).
- Swift, *Independent assessment* and *Perform an Independent Assessment* — IAF, Community Standard Assessment, internal/external/mixed teams, assessor qualification, two-year re-use ceiling, assessor certification and directory (publisher pages, via Internet Archive captures of 22 January 2026 and 11 March 2026).
- Swift, *Counterparty Risk Management* — use of counterparty attestation data (publisher page, via Internet Archive capture of 16 December 2025).
- Swift Knowledge Centre document index — CSCF edition filenames and publication dates (`CSCF_v2024_20231017.pdf`, `CSCF_v2025_20240701.pdf`, `CSCF_v2026_202507015.pdf`). **The CSCF PDFs themselves are behind the Swift login and could not be fetched**; control counts and exact control text must be read there.
- Swift press release, *Swift launches customer security programme to reinforce the security of the global banking system*, 27 May 2016 (publisher page, via Internet Archive).
- Microsoft Azure regulatory-compliance mapping for SWIFT CSP-CSCF v2021 and v2022 — used only for control numbering and objective wording of older editions (secondary).
- usd AG (a CSP assessment provider), *Changes to CSCFv2026* (9 October 2025) and *CSCFv2025 changes for architecture type B* (25 April 2025) — v2026 promotion of control 2.4 and the customer-connector scope change (secondary).
- Schellman (a CSP assessment provider), *SWIFT CSP* service page — attestation obligation since 2018 and independent assessment required as of July 2021 (secondary; its control count predates the current edition).
- Wikipedia, *Society for Worldwide Interbank Financial Telecommunication* — cooperative status, G-10 oversight with the National Bank of Belgium in the lead role, and the 2016 Bangladesh Bank theft (secondary, used only for background).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
