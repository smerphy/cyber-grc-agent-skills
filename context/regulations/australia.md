# Australia: Privacy Act, NDB Scheme, SOCI Act, and APRA CPS 234

Australia's cyber/privacy regime is a stack of four instruments that frequently apply to the same organization at once: the Privacy Act 1988 (Cth) with its Australian Privacy Principles and Notifiable Data Breaches scheme, the Security of Critical Infrastructure (SOCI) Act 2018 for designated infrastructure sectors, APRA's prudential standards CPS 234 and CPS 230 for regulated financial entities, and the Cyber Security Act 2024 (ransomware payment reporting). The reporting clocks differ sharply — SOCI's 12 hours is among the world's shortest — so scoping which instruments bind you is the first task, not an afterthought.

## At a glance

| Item | Detail |
|---|---|
| Jurisdiction | Australia (Commonwealth); extraterritorial reach where an organization carries on business in Australia and handles Australians' personal information |
| Instrument(s) | Privacy Act 1988 (Cth) incl. APPs (Schedule 1) and NDB scheme (Part IIIC); SOCI Act 2018 (as amended 2021–2024); APRA CPS 234 (2019) and CPS 230 (2025); Cyber Security Act 2024 |
| In force | Privacy Act 1988; APPs 2014; NDB scheme Feb 2018; SOCI 2018 with major amendments 2021–22; CPS 234 Jul 2019; CPS 230 Jul 2025 |
| Regulator | OAIC (privacy/NDB); Dept. of Home Affairs / Cyber and Infrastructure Security Centre with ACSC as incident recipient (SOCI); APRA (CPS 234/230) |
| Max penalties | Serious/repeated privacy interference (body corporate): greater of A$50m, 3× the benefit obtained, or — if the benefit cannot be determined — 30% of adjusted turnover for the breach turnover period (verify formula against s 13G as amended 2022); SOCI and CPS carry separate civil penalty and enforcement regimes |
| Who's covered | Privacy Act: agencies + organizations with annual turnover > A$3m, plus prescribed smaller entities (health service providers, data traders, credit bodies); SOCI: responsible entities for critical infrastructure assets in 11 sectors; CPS 234/230: all APRA-regulated entities |

## Privacy Act 1988 and the Australian Privacy Principles

Thirteen APPs (Schedule 1) govern the personal-information lifecycle for "APP entities." The small-business exemption (turnover ≤ A$3m) still stands but is a stated target of the ongoing reform program — do not assume it survives long term.

Condensed map of the 13 principles:

- **APP 1** — open and transparent management: a privacy policy, and practices/procedures/systems to ensure compliance (the "privacy program" hook).
- **APP 2** — anonymity and pseudonymity options where practicable.
- **APP 3–4** — collection of solicited information (necessity test; higher bar and consent default for "sensitive information") and treatment of unsolicited information.
- **APP 5** — collection notices.
- **APP 6** — use and disclosure limited to the primary purpose, related secondary purposes within reasonable expectations, consent, or listed exceptions.
- **APP 7** — direct marketing limits; **APP 9** — government identifiers.
- **APP 8** — cross-border disclosure: an accountability model, not a transfer-mechanism model. Before disclosing offshore, take reasonable steps to ensure the recipient complies with the APPs — and the discloser generally remains liable for the recipient's breaches unless an exception applies (informed consent, recipient bound by a substantially similar scheme with enforcement access).
- **APP 10** — quality; **APP 12** — access; **APP 13** — correction.
- **APP 11** — **security**: take reasonable steps to protect personal information from misuse, interference, and loss, and from unauthorized access, modification, or disclosure; and destroy or de-identify information no longer needed for a permitted purpose. The 2024 amendments clarified on the face of the Act that reasonable steps include **technical and organisational measures** — bringing the drafting closer to GDPR Art. 32 language. OAIC guidance and determinations flesh out what "reasonable" means (governance, access control, encryption, testing, destruction practices); OAIC enforcement after major breaches has centred on APP 11 and APP 1 failures together.

## Notifiable Data Breaches (NDB) scheme — Part IIIC

- **Eligible data breach test:** (1) unauthorized access to, unauthorized disclosure of, or loss of personal information; (2) a reasonable person would conclude it is **likely to result in serious harm** to any affected individual; and (3) remedial action has not prevented that likely serious harm. "Serious harm" is assessed on listed factors: kinds and sensitivity of information, protections (encryption), who obtained or could obtain it, and the nature of possible harm (identity theft, financial loss, physical, psychological, reputational).
- **Suspected breaches:** if you suspect but cannot yet conclude a breach is eligible, carry out a reasonable and expeditious assessment and complete it **within 30 days** of becoming aware of the grounds for suspicion. The 30 days is a ceiling, not an entitlement — OAIC expects most assessments to conclude much faster.
- **Notification:** once you hold reasonable grounds to believe an eligible data breach has occurred, prepare a statement to the **OAIC** and notify **affected individuals as soon as practicable** (directly where practicable; otherwise publish the statement and publicize it). Content: entity identity, description of the breach, kinds of information, and recommended steps for individuals.
- **Remedial action exception:** effective remediation that removes the likelihood of serious harm takes the incident out of the scheme — document that analysis contemporaneously; the burden of the conclusion sits with you.
- Multi-party breaches (e.g., processor-style vendors): one entity's compliant notification can discharge others holding the same information jointly — allocate this in contracts before an incident.

## Penalties and the 2022 uplift

The Privacy Legislation Amendment (Enforcement and Other Measures) Act 2022 — passed in the aftermath of the Optus and Medibank breaches — raised the civil penalty for a **serious or repeated interference with privacy** (s 13G) from A$2.22m to the **greater of A$50m, three times the value of the benefit obtained, or (where the benefit cannot be determined) 30% of adjusted turnover during the breach turnover period** (verify the current formula and definitions against the Act). It also strengthened OAIC information-gathering and the extraterritoriality test (removing the requirement that information be collected or held in Australia).

## 2024 reform wave — Privacy and Other Legislation Amendment Act 2024

The first tranche of the long-running Privacy Act review passed in late 2024. Confirmed elements (commencement dates vary — verify each before advising):

- **Statutory tort for serious invasions of privacy** (intrusion upon seclusion or misuse of information; intentional or reckless; serious; countervailing public-interest balancing) — commenced mid-2025.
- **Criminal doxxing offences** (menacing/harassing release of personal data) in the Criminal Code — commenced on assent.
- **Tiered civil penalties:** new mid-tier (interferences without the "serious" element) and low-tier (administrative breaches, infringement-notice style) penalties below the s 13G ceiling, plus expanded OAIC enforcement tools.
- **Automated-decision transparency** in privacy policies (with a multi-year lead time), a **Children's Online Privacy Code** to be made by the OAIC, and the APP 11 technical-and-organisational-measures clarification noted above.

A second tranche — a "fair and reasonable" processing test, removal of the small-business exemption, direct rights of action under the Act — remained government-committed but unlegislated at last review. Treat any tranche-two specifics as proposals; track via [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## SOCI Act 2018 — critical infrastructure

Covers **responsible entities** for critical infrastructure assets across **11 sectors** (communications, data storage/processing, financial services, water, energy, healthcare, higher education/research, food/grocery, transport, space, defence industry), divided into 20+ defined asset classes. Amendments in 2021–22 built the operative regime; the 2024 Enhancing Response and Prevention amendments extended coverage to data storage systems holding business-critical data and added consequence-management powers — verify current asset-class definitions when scoping.

- **Register** (Part 2): report ownership and operational information for critical infrastructure assets.
- **Critical Infrastructure Risk Management Program (CIRMP)** (Part 2A): adopt and maintain a written program addressing cyber, personnel, supply-chain, and physical/natural hazards; the cyber component must meet a recognized framework — the ACSC **Essential Eight** (Maturity Level 1), ISO 27001, NIST CSF, AESCSF, or equivalent (see [../frameworks/essential-eight.md](../frameworks/essential-eight.md)). The board must approve an **annual attestation** of the program.
- **Mandatory cyber incident reporting** (Part 2B), to the ACSC: **within 12 hours** for incidents having a **significant impact** on the availability of the asset, **within 72 hours** for other incidents having a relevant impact — verify the current impact definitions; oral reports must be confirmed in writing within 84 hours.
- **Government assistance powers** (Part 3A): for serious cyber incidents, government can issue information-gathering directions, action directions, and — as a last resort — intervention requests authorizing the Australian Signals Directorate to act on the entity's systems ("step-in"). Build this scenario into IR plans: it changes evidence handling, communications, and legal posture.
- **Systems of National Significance:** declared assets carry enhanced obligations — incident response planning, exercises, vulnerability assessments, and potentially system information reporting to ASD.

## APRA CPS 234 and CPS 230 — financial sector

- **CPS 234 (Information Security):** binds all APRA-regulated entities (banks/ADIs, insurers, superannuation trustees). The **board is ultimately responsible** for information security. Requirements: security capability commensurate with threats; classification of information assets by criticality/sensitivity; controls proportionate to that classification, including for assets **managed by third parties**; systematic testing of control effectiveness (with independence requirements); internal audit review; notify **APRA within 72 hours** of a material information security incident, and within **10 business days** of identifying a material control weakness that cannot be remediated in a timely way.
- **CPS 230 (Operational Risk Management, effective July 2025):** consolidates operational risk, business continuity, and service-provider management — critical operations mapping, tolerance levels for disruption, comprehensive service-provider registers and management of material arrangements. For cyber/GRC teams it is the resilience-and-third-party layer on top of CPS 234; feed it from [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).

## Cyber Security Act 2024 (brief)

Australia's first standalone Cyber Security Act added: **mandatory ransomware payment reporting** (businesses above a turnover threshold must report ransomware/extortion payments within **72 hours** — verify threshold and commencement), a **limited-use** protection for incident information voluntarily shared with the National Cyber Security Coordinator/ASD, a Cyber Incident Review Board, and security standards for smart devices. The ransomware clock runs from making the payment — wire it into extortion-decision playbooks.

## Key obligations for security/GRC teams

1. **Scope instrument-by-instrument** — Privacy Act (turnover/sector), SOCI (asset class), APRA (regulated entity), Cyber Security Act (ransomware reporting) each has its own applicability test; see [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Build one incident matrix with four clocks** — SOCI 12h/72h (ACSC), APRA 72h, ransomware payment 72h, NDB "as soon as practicable" with a 30-day assessment ceiling. The shortest applicable clock drives the process — see [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
3. **Treat APP 11 as a control mandate** — documented technical and organisational measures, plus a working destruction/de-identification pipeline for data past its retention purpose; over-retention was the aggravating factor in Australia's landmark breaches.
4. **Operationalize the NDB serious-harm assessment** — a templated, factor-based analysis with owner and deadline tracking; document non-notifiable conclusions as rigorously as notifications.
5. **CIRMP as a living program** — annual board attestation means evidence, not narrative: framework mapping (Essential Eight ML1 or equivalent), hazard coverage, and review records. See [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).
6. **Contract the multi-party questions in advance** — who runs the NDB assessment, who notifies, vendor breach-reporting windows shorter than your regulatory clocks.
7. **Prepare for government assistance powers** — a SOCI step-in scenario in tabletop exercises, with legal and communications pre-positioned.
8. **Track tranche-two privacy reform** — fair-and-reasonable test and small-business exemption removal would materially expand scope.

## Interplay

- **vs. GDPR** ([./gdpr.md](gdpr.md)): no lawful-basis architecture — Australian collection/use runs on notice, purpose, and consent-for-sensitive-data rather than six legal bases; APP 8 is accountability-based rather than mechanism-based (no SCC equivalent); NDB has a higher notification threshold ("likely serious harm" vs. GDPR's "risk") and no fixed 72-hour regulator clock. Penalty ceilings post-2022 are GDPR-magnitude. A GDPR program covers most APP substance but not the NDB assessment mechanics, SOCI, or APRA layers.
- **SOCI vs. NIS2** ([./nis2.md](nis2.md)): similar sector-based critical-infrastructure logic; SOCI's 12-hour clock is comparable to NIS2's 24-hour early warning, but SOCI adds registration, board-attested risk programs, and unique government intervention powers.
- **CPS 234/230 vs. DORA** ([./dora.md](dora.md)): the same board-accountability, testing, and third-party themes — a DORA program maps well onto CPS 230, but APRA's notification triggers and timelines are distinct.
- OAIC (privacy), ACSC (SOCI incidents), and APRA notifications for one incident are separate filings with different content — expect to file all three for a major breach at a regulated financial entity.

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
