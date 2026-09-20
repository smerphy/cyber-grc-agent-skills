# Swift Customer Security Programme (CSP) and Customer Security Controls Framework (CSCF)

## At a glance

| Attribute | Detail |
|---|---|
| Publisher | Swift, a member-owned cooperative society under Belgian law that operates the interbank messaging network; headquartered in La Hulpe, Belgium. Swift has been subject to cooperative central bank oversight since 1998, with the National Bank of Belgium as lead overseer supported by the G-10 central banks |
| Instrument | Customer Security Programme (CSP), announced 27 May 2016, built on five strategic initiatives; its control baseline is the Customer Security Controls Framework (CSCF), first issued 2017 |
| Current edition | CSCF v2026, published on the Swift Knowledge Centre in July 2025 (file `CSCF_v2026_202507015.pdf`), in force for the 2026 attestation cycle. Swift's public CSP document centre still listed v2026 as the latest edition in June 2026; a v2027 edition is expected under the July cadence and Swift's own CSP refresher webinar advertises "CSCF v2027 readiness", but its publication could not be confirmed from public pages as of September 2026 (verify) |
| Who is covered | Every Swift user, scoped to its own local Swift infrastructure; applicable controls depend on which of the **five architecture types** (A1–A4, B) the user falls into |
| Structure | 3 objectives → 7 principles → numbered controls, each marked **mandatory** or **advisory**; control definitions are written in line with ISO 27002, PCI DSS, SOC 2 and NIST CSF |
| Control count | 32 controls in both v2025 and v2026. The split moves each year: v2025 was 25 mandatory / 7 advisory; v2026 is 26 mandatory / 6 advisory after control 2.4 was promoted. Whether a given control applies, and whether it is mandatory, still depends on architecture type |
| Annual cycle | New version published each July for the *following* year; attestation window **1 July – 31 December**; attest no later than 31 December and re-attest at least annually |
| Certifiable? | No certificate. Annual **self-attestation in KYC-SA**, which must be supported by an **independent assessment** (internal, external, or a mixed team) performed under the Independent Assessment Framework (IAF) |
| Enforcement | Swift reserves the right to report non-attesting or non-compliant users to their local supervisors; non-compliance is surfaced in a real-time application accessible to the user's supervisor, and attestation status is visible to counterparties in KYC-SA |

## What it is

The CSP is Swift's community security programme: a mandatory security baseline plus a transparency mechanism. It was announced on 27 May 2016, months after roughly USD 80 million was taken from Bangladesh Bank's account at the Federal Reserve Bank of New York, in an attack the US Treasury attributes to the Lazarus Group and Bluenoroff: stolen Swift credentials and malware inside the victim's own environment were used to issue fraudulent payment messages, out of some USD 851 million attempted. The lesson Swift drew — and the premise of the whole programme — is that the network was not breached; the *users' own endpoints* were. The CSCF therefore governs what each institution does inside its own perimeter, not what Swift does inside the network.

Three things make CSP unusual among frameworks. First, it is contractual and near-universal: every Swift user must attest, there is no scoping-out, and there is no "we are too small" tier. Second, compliance data is **shared**: counterparties can read each other's attestations through KYC-SA, which turns CSCF status into a commercial and correspondent-banking due-diligence signal rather than a private audit artefact. Third, it is explicitly annual and ratcheting — advisory controls are published as a preview of future mandatory controls, so this year's advisory list is next year's project plan.

Swift also publishes product-specific **Security Guidance (SG)** documents for its messaging interfaces (configuration-level guidance that complements the product-agnostic CSCF), and the **Customer Security Controls Policy**, which carries the attestation rules, timelines and non-compliance follow-up.

## Who it covers / Scope

- **All Swift users.** The CSCF defines the security baseline applicable to all users; which controls apply depends on the user's connectivity to Swift.
- **Architecture types.** Swift publishes an architecture decision tree that places each user in one of five types (A1, A2, A3, A4, B). Broadly, the A types describe increasing degrees of *local* Swift-related footprint (messaging interface, communication interface, connector, hardware security modules) and type B describes users with no such local footprint; the applicable mandatory and advisory control set follows from that classification. Confirm the exact definitions in the current CSCF before relying on a classification (verify).
- **Scope creep via connectors.** CSCF v2025 began classifying **customer client connectors** (API consumers, middleware, file-transfer clients) as in-scope customer connectors regardless of whether the endpoint is a server or a client. CSCF v2026 makes those requirements mandatory, which can reclassify a type B user that uses an application-to-application client connector into **type A4**. A type B user connecting only through user-to-application flows (for example a browser GUI) is not affected.
- **Service providers in the chain.** Users connecting through a Swift connectivity or service provider (for example under the Business Connect programme) still own the controls covering their own footprint, and connecting through a *non-compliant* service provider is itself one of Swift's listed breach conditions.
- **Outsourcing is not a transfer of accountability.** Control 2.8 (Outsourced Critical Activity Protection) covers the local Swift infrastructure against risks created by outsourcing critical activities, and Swift publishes separate Outsourcing Agent Requirements; the user remains the attesting party.

## Structure and requirements

Three objectives, seven principles (Swift's own phrasing, September 2026):

| Objective | Principles |
|---|---|
| Secure your environment | 1. Restrict internet access and segregate critical systems from the general IT environment · 2. Reduce attack surface and vulnerabilities · 3. Physically secure the environment |
| Know and limit access | 4. Prevent compromise of credentials · 5. Manage identities and segregate privileges |
| Detect and respond | 6. Detect anomalous activity to system or transaction records · 7. Plan for incident response and information sharing |

Controls are numbered `principle.control`. A trailing **A** marks a control that is advisory in that edition; when it is promoted, the suffix is dropped (control 2.4A became 2.4 in v2026). The 32 controls below carry Swift's own short titles as transcribed in a public v2025 control library; status shown is v2026. Always check numbering, titles, applicability and mandatory status against the CSCF edition you are attesting against.

| # | Control (Swift title) — what it requires |
|---|---|
| 1.1 | Swift Environment Protection — protect the local Swift infrastructure from compromised elements of the general IT and external environment (the "secure zone") |
| 1.2 | Operating System Privileged Account Control — restrict and control allocation and use of administrator-level operating system accounts |
| 1.3 | Virtualisation or Cloud Platform Protection — secure the platform and the virtual machines hosting Swift-related components to the same level as physical systems |
| 1.4 | Restriction of Internet Access — control and protect internet access from operator PCs and from systems inside the secure zone |
| 1.5 | Customer Environment Protection — protect the customer's own connectivity infrastructure from the general IT environment |
| 2.1 | Internal Data Flow Security — confidentiality, integrity and authenticity of application data flows between local Swift components |
| 2.2 | Security Updates — minimise known technical vulnerabilities: vendor support, mandatory software updates, risk-aligned security updates |
| 2.3 | System Hardening — hardening of Swift-related components |
| 2.4 | Back Office Data Flow Security — confidentiality, integrity and mutual authenticity of flows to the back-office first hops (**advisory 2.4A until v2025, mandatory from v2026**) |
| 2.5A | External Transmission Data Protection — protect Swift-related data transmitted or stored outside the secure zone |
| 2.6 | Operator Session Confidentiality and Integrity — protect interactive operator sessions |
| 2.7 | Vulnerability Scanning — regular scanning of the local Swift environment, with follow-up |
| 2.8 | Outsourced Critical Activity Protection — protect the local Swift infrastructure from risks created by outsourcing critical activities |
| 2.9 | Transaction Business Controls — keep outbound transaction activity within the expected bounds of normal business |
| 2.10 | Application Hardening — reduce the attack surface of Swift-related applications |
| 2.11A | RMA Business Controls — restrict transaction activity to validated and approved business counterparties |
| 3.1 | Physical Security — protect sensitive equipment, workplaces, hosting sites and storage |
| 4.1 | Password Policy — password policy resistant to common password attacks |
| 4.2 | Multi-Factor Authentication — MFA for access to Swift-related systems and applications |
| 5.1 | Logical Access Control — need-to-know, least privilege and separation of duties for operator accounts |
| 5.2 | Token Management — management, tracking and use of connected/disconnected hardware or personal tokens |
| 5.3A | Staff Screening Process — regular screening of staff operating the local Swift environment |
| 5.4 | Password Repository Protection — physical and logical protection of the recorded-password repository |
| 6.1 | Malware Protection — malware protection with follow-up on results |
| 6.2 | Software Integrity — integrity checking of Swift-related components |
| 6.3 | Database Integrity — integrity of the messaging interface or customer connector database |
| 6.4 | Logging and Monitoring — record security events; detect anomalous actions and operations |
| 6.5A | Intrusion Detection — detect and contain anomalous network activity in the local or remote Swift environment |
| 7.1 | Cyber Incident Response Planning — consistent and effective cyber incident management |
| 7.2 | Security Training and Awareness — awareness for all staff and maintained security knowledge for privileged staff |
| 7.3A | Penetration Testing — validate the operational security configuration |
| 7.4A | Scenario-based Risk Assessment — readiness assessment against plausible cyber-attack scenarios |

**Change management.** Changes are announced mid-year and users get up to 18 months to implement them; new controls and newly in-scope components are introduced as advisory first, giving users time to plan, budget and implement. Emergency releases are possible but rare.

## Assessment, certification and evidence

| Element | Requirement |
|---|---|
| Attestation | Submitted annually in the **KYC-Security Attestation (KYC-SA)** application; the new controls version appears in KYC-SA in early July; submit between July and December, no later than 31 December; new joiners attest before going live |
| Independent assessment | Every user must undergo a **Community Standard Assessment** under the IAF to support the attestation, and must repeat it annually. Swift's 2021 guidance introduced the requirement and stated that the self-assessment option remained available in the tool but counted as non-compliant |
| Who may assess | Internal team, external provider, or a mixed team — all equally valid, provided the assessment is independent. Internal teams must sit outside the first line of defence (typically Internal Audit, Risk, or a purpose-built independent team) |
| Assessor qualification | Demonstrable cyber-security assessment experience against an industry standard such as PCI DSS, ISO 27002 or NIST CSF; the lead assessor must hold at least one industry-relevant certification (for example CISA); Swift also runs a **CSP Assessor Certification** for external and internal assessors and publishes a certified-assessor directory |
| Report re-use | A previous assessment may be referenced on re-attestation if the assessor agrees, the in-scope Swift footprint has not changed significantly, and the new CSCF adds no new or changed mandatory controls the earlier assessment did not cover. Reliance is allowed **only once**: relying in 2026 on a 2025 assessment means a full assessment in 2027 (this replaced the earlier "report issuance date + two years" validity rule) |
| Disclosure in the attestation | Naming the internal department or external firm that performed the assessment is mandatory; naming the individual lead assessor is advisory |
| Mandated external assessment | Swift can require a specific user to undergo an external assessment; failure to complete it is a policy breach |
| Breach conditions | No valid (or expired) attestation · not compliant with applicable mandatory controls · no independent assessment · connecting through a non-compliant service provider · not completing a Swift-mandated external assessment |
| Consequence | Swift reserves the right to report such users to their local supervisors, and non-compliance is made visible in a real-time application accessible to the user's supervisor. Counterparties can also read attestation data in KYC-SA and act on it commercially |

There is no fine schedule and no certificate: the sanctions are supervisory visibility and counterparty reaction. For evidence handling see [audit-preparation](../../skills/audit-preparation/SKILL.md) and the [audit evidence request list](../../templates/audit-evidence-request-list.md).

## Timeline and status

| Date | Event |
|---|---|
| Early 2016 | Roughly USD 80 million taken from Bangladesh Bank's account at the New York Fed using stolen Swift credentials and malware in the victim's own environment, out of some USD 851 million attempted — the trigger event |
| 27 May 2016 | Swift announces the Customer Security Programme (five strategic initiatives) |
| 2017 | First CSCF published |
| 2018 | Attestation against applicable mandatory controls becomes an annual obligation. Swift's attestation page is archived only from September 2020, by which point the annual July–December rule is already stated; the 2018 start date rests on assessor publications (verify) |
| 2021 | Independent assessment (Community Standard Assessment) required to support the attestation under the Independent Assessment Framework; self-assessment alone counts as non-compliant from that year |
| July 2024 | CSCF v2025 published (`CSCF_v2025_20240701.pdf`); customer client connectors start being brought into scope, with type B → A4 consequences |
| July 2025 | CSCF v2026 published (`CSCF_v2026_202507015.pdf`): control 2.4 back-office data flow security becomes mandatory and customer connectors become mandatory in-scope components for controls 1.2, 1.3, 1.4, 2.2, 2.3, 2.6, 2.7, 3.1, 4.1, 4.2, 5.1, 5.4, 6.1 and 6.4 |
| 1 July – 31 December 2026 | Attestation window for CSCF v2026 — the live cycle as of September 2026 |
| July 2026 (expected) | CSCF v2027 publication under the standard cadence. Swift's CSP refresher webinar page (captured April 2026) covers "CSCF v2027 readiness", but the public document centre still showed v2026 as the latest edition in June 2026 and v2027 publication is not confirmed from public pages as of September 2026 (verify) |

## Key obligations for security/GRC teams

1. **Fix the architecture type first.** Run the decision tree before anything else; the whole control scope, and therefore the assessment fee and remediation budget, follows from it. Re-run it whenever connectivity changes. See [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md).
2. **Re-scope for customer connectors.** Inventory every application-to-application endpoint (API clients, middleware, file transfer) touching Swift directly or through a provider; under v2026 these are mandatory in-scope components and may move a type B user to A4.
3. **Close control 2.4 before the window.** Back-office data flow security is the v2026 promotion — mutual authentication, integrity and confidentiality on the first hop to core banking and payment hubs is a project, not a configuration change.
4. **Book the independent assessment early.** Assessor capacity is concentrated in H2; agree scope, architecture type and evidence list in writing, and decide internal vs external vs mixed team against the IAF independence tests. See [control-testing](../../skills/control-testing/SKILL.md).
5. **Track report re-use.** Reliance on a previous assessment is allowed only once and only if the assessor agrees, the in-scope footprint has not changed significantly and the new CSCF adds no uncovered mandatory controls — so a year of reliance commits you to a full assessment the year after.
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

Swift's public site blocks scripted access, so the pages below were read through Internet Archive captures; the canonical URLs are given.

- Swift, *Customer Security Programme* — programme overview and the four-step compliance journey: https://www.swift.com/myswift/customer-security-programme (publisher page; capture of 2 September 2026)
- Swift, *CSP: Understand Controls* — three objectives and seven principles, mandatory vs advisory, five architecture types and decision tree, alignment with ISO 27002 / PCI DSS / SOC 2 / NIST CSF, July publication a year ahead of effect, 18-month change-management window: https://www.swift.com/myswift/customer-security-programme/understand-controls (publisher page; capture of 7 August 2026)
- Swift, *CSP: Submit KYC-Security Attestation* — July–December window, 31 December deadline, new joiners, breach conditions, supervisor reporting and real-time supervisor visibility: https://www.swift.com/myswift/customer-security-programme/submit-kyc-security-attestation (publisher page; capture of 10 May 2026)
- Swift, *CSP: Perform an Independent Assessment* — IAF, Community Standard Assessment, internal/external/mixed teams, independence from the first line, assessor qualification, once-only report re-use, assessor certification and directory: https://www.swift.com/myswift/customer-security-programme/perform-independent-assessment (publisher page; capture of 18 May 2026)
- Swift, *CSP document centre* — CSCF v2026 listed as the latest edition (last updated 11 July 2025), CSCF v2025, IAF, Outsourcing Agent Requirements: https://www.swift.com/myswift/customer-security-programme-document-centre (publisher page; capture of 8 June 2026)
- Swift, *Swift oversight* — cooperative central bank oversight since 1998, National Bank of Belgium as lead overseer supported by the G-10 central banks, Swift Oversight Forum: https://www.swift.com/about-us/organisation-governance/swift-oversight (publisher page; capture of 14 September 2026)
- Swift press release, *Swift launches customer security programme to reinforce the security of the global banking system*, Brussels, 27 May 2016 — five mutually reinforcing strategic initiatives: https://www.swift.com/news-events/press-releases/swift-launches-customer-security-programme-reinforce-security-global-banking-system (publisher page; capture of 15 May 2026)
- Swift, *CSP refresher sessions* webinar page — recap of CSCF v2026 and "CSCF v2027 readiness": https://www.swift.com/news-events/webinars/swift-customer-security-programme-csp-refresher-sessions (publisher page; capture of 11 April 2026)
- Swift, *Independent assessment* (previous CSP page, 2021 wording) — independent assessment required as of 2021, self-assessment treated as non-compliant, and the then-applicable "issuance date + two years" report validity rule: https://web.archive.org/web/2021/https://www.swift.com/myswift/customer-security-programme-csp/independent-assessment (publisher page, archived)
- Swift Knowledge Centre — CSCF edition files (`CSCF_v2024_20231017.pdf`, `CSCF_v2025_20240701.pdf`, `CSCF_v2026_202507015.pdf`): https://www2.swift.com/knowledgecentre/ . **The CSCF PDFs are behind the Swift login and could not be fetched**; exact control text, applicability matrices and per-architecture status must be read there.
- US Department of the Treasury press release, *Treasury Sanctions North Korean State-Sponsored Malicious Cyber Groups*, 13 September 2019 — approximately USD 80 million taken from the Bangladesh central bank's New York Federal Reserve account using stolen Swift credentials, out of USD 851 million attempted: https://home.treasury.gov/news/press-releases/sm774
- usd AG (a CSP assessment provider), *Was ändert sich mit CSCFv2026?*, 9 October 2025 — promotion of control 2.4 and the 14 controls that list the customer connector as a mandatory in-scope component: https://www.usd.de/swift-cscfv2026-assessment-aenderungen/ (secondary)
- usd AG, *SWIFT CSCFv2025: Änderungen für Architekturtyp B* — customer-client-connector scope change and type B to A4 reclassification: https://www.usd.de/swift-cscfv2025-architekturtyp-b/ (secondary)
- Dionach (a CSP assessment provider), *Swift CSCF v2026: What You Need to Know*, 10 April 2026 — 2.4A to mandatory, connectors in scope, reclassification: https://www.dionach.com/swift-cscf-v2026-what-you-need-to-know-and-why-it-matters/ (secondary)
- Elevate Consult, *SWIFT CSP Controls: The CSCF v2026 Framework Explained*, 26 June 2026 — 32 controls, 26 mandatory / 6 advisory in v2026 against 25 / 7 in v2025: https://elevateconsult.com/insights/swift-csp-controls/ (secondary; used only for the counts)
- CISO Assistant community control library, *swift-cscf-v2025* — transcription of the v2025 control numbering and Swift's short control titles: https://raw.githubusercontent.com/intuitem/ciso-assistant-community/main/backend/library/libraries/swift-cscf-v2025v1.0.yaml (secondary)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
