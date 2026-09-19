# EU product cybersecurity via sector legislation — RED cybersecurity delegated act (Delegated Regulation (EU) 2022/30) and Machinery Regulation (EU) 2023/1230

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | **RED**: Directive 2014/53/EU (Radio Equipment Directive), Art. 3(3)(d), (e), (f) activated by Commission Delegated Regulation (EU) 2022/30 (OJ L 7, 12.1.2022), as amended/corrected by Delegated Regulation (EU) 2023/2444 and repealed prospectively by Delegated Regulation (EU) 2026/339. **Machinery**: Regulation (EU) 2023/1230 (OJ L 165, 29.6.2023; corrigendum OJ L 169, 4.7.2023), as amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI) |
| Legal nature | RED is a directive transposed nationally (New Legislative Framework CE-marking regime); the delegated act and the Machinery Regulation are directly applicable |
| Publisher / regulator | European Commission (DG GROW) for both; national market surveillance authorities enforce; notified bodies (NANDO) perform third-party conformity assessment |
| Key dates | RED cyber requirements apply to equipment placed on the market from **1 August 2025** (postponed from 1 August 2024); EN 18031-1/-2/-3:2024 cited in the OJ 30 January 2025 (with restrictions); Delegated Regulation 2022/30 **repealed with effect from 11 December 2027** when the Cyber Resilience Act (CRA) applies in full. Machinery Regulation applies from **20 January 2027**; Directive 2006/42/EC repealed the same day |
| Who is covered | RED act: manufacturers (and importers/distributors) of internet-connected radio equipment, plus childcare, toy and wearable radio equipment processing personal/traffic/location data, plus internet-connected equipment handling money or virtual currency. Machinery Regulation: manufacturers of machinery, related products and partly completed machinery, and anyone making a "substantial modification" (physical or digital) |
| Cyber content | RED: essential requirements on network protection, personal data/privacy safeguards and fraud protection. Machinery: essential health and safety requirements (EHSRs) in Annex III sections 1.1.9 (protection against corruption) and 1.2.1 (safety and reliability of control systems, including "reasonably foreseeable malicious attempts from third parties") |
| Assessment model | CE marking with EU declaration of conformity. Self-assessment (module A) is available only where harmonised standards are applied in full; otherwise EU type-examination (module B + C), full quality assurance (module H) or, for machinery, unit verification (module G) via a notified body |
| Penalties | Set by Member States: "effective, proportionate and dissuasive", may include criminal penalties (RED Art. 46; Machinery Regulation Art. 50). No EU-level fine ceilings — contrast the CRA's EUR 15 million / 2.5 % turnover tier |
| Relationship to neighbours | The CRA (Regulation (EU) 2024/2847) absorbs the RED cyber requirements from 11 December 2027 and applies cumulatively to machinery that is a product with digital elements; the AI Act interface for machinery was rewritten by the Digital Omnibus on AI in July 2026 |

## What it is

The EU has no single "product security law" in force yet. Until the CRA applies in full on 11 December 2027, product cybersecurity is imposed through sector-specific CE-marking legislation, of which two instruments matter most to security and GRC teams. The first is the **RED cybersecurity delegated act**: Directive 2014/53/EU always contained latent essential requirements that radio equipment "does not harm the network", "incorporates safeguards to ensure that the personal data and privacy of the user and of the subscriber are protected" and "supports certain features ensuring protection from fraud" (Art. 3(3)(d), (e), (f)), but they only bite once the Commission specifies the equipment classes concerned. Delegated Regulation (EU) 2022/30 did that in October 2021, originally for 1 August 2024; Delegated Regulation (EU) 2023/2444 pushed application to 1 August 2025 because CEN/CENELEC needed more time to deliver harmonised standards, which arrived as the EN 18031 series.

The second is the **Machinery Regulation (EU) 2023/1230**, which replaces the 2006 Machinery Directive from 20 January 2027 and, for the first time, makes protection against digital corruption and malicious interference with control systems a health-and-safety requirement. Its recital 25 frames the intent narrowly: manufacturers must adopt "proportionate measures which are limited to the protection of the safety of the product", without prejudice to other Union acts specifically addressing cybersecurity (i.e. the CRA).

Both regimes follow the New Legislative Framework pattern: essential requirements in the act, technical detail in voluntary harmonised standards that confer a presumption of conformity when their references are published in the Official Journal, conformity-assessment modules chosen by risk class, and a manufacturer-signed EU declaration of conformity backing the CE mark.

## Who it covers / Scope

### RED delegated act (Delegated Regulation (EU) 2022/30, Art. 1–2)

| Essential requirement | Equipment class captured | Carve-outs |
|---|---|---|
| Art. 3(3)(d) — no harm to the network, no misuse of network resources | Any radio equipment "that can communicate itself over the internet, whether it communicates directly or via any other equipment" (internet-connected radio equipment) | Equipment under the Medical Devices Regulation (EU) 2017/745 or IVD Regulation (EU) 2017/746 |
| Art. 3(3)(e) — safeguards for personal data and privacy | Internet-connected radio equipment; radio equipment designed or intended exclusively for childcare; toy radio equipment (Directive 2009/48/EC); wearable radio equipment (worn on, strapped to or hung from the body or clothing) — in each case only if capable of processing personal data (GDPR Art. 4(1)) or traffic or location data (ePrivacy Directive Art. 2(b), (c)) | As above, plus equipment under the civil-aviation Regulation (EU) 2018/1139, the vehicle general-safety Regulation (EU) 2019/2144, or the electronic-tolling Directive (EU) 2019/520 |
| Art. 3(3)(f) — protection from fraud | Internet-connected radio equipment that enables the holder or user to transfer money, monetary value or virtual currency (Directive (EU) 2019/713 definition) | As for (e) |

"Radio equipment" (RED Art. 2(1)) is any electrical or electronic product that intentionally emits and/or receives radio waves for radio communication or radiodetermination — in practice anything with Wi-Fi, Bluetooth, cellular, Zigbee, LoRa, UWB or GNSS. The RED itself excludes amateur-radio kits, marine equipment, airborne products and custom-built professional evaluation kits (Annex I), and equipment used exclusively for public security, defence or State security (Art. 1(3)). Placing on the market is what triggers the duty (RED Art. 2(10): first making available in the Union), so the 1 August 2025 date applies per unit, not per model.

### Machinery Regulation (Art. 2)

- **In scope**: machinery; interchangeable equipment; safety components; lifting accessories; chains, ropes and webbing; removable mechanical transmission devices; and partly completed machinery. A "safety component" is "a physical or digital component, including software", independently placed on the market to fulfil a safety function (Art. 3(3)) — standalone safety software is in scope.
- **Out of scope** (Art. 2(2)) — the exclusions most relevant to connected products: household appliances, audio/video equipment, IT equipment, ordinary office machinery (except 3D printers), low-voltage switchgear and electric motors insofar as they fall under the Low Voltage Directive 2014/35/EU or the RED; road, agricultural and two/three-wheel vehicles under their own type-approval regulations; aircraft, seagoing vessels, weapons, and machinery for military, police or laboratory research use.
- **Substantial modification** (Art. 3(16), Art. 18): a modification "by physical or digital means" after placing on the market, not foreseen by the manufacturer, that creates a new hazard or increases an existing risk requiring new guards, protective devices or measures. The person making it — including an operator pushing a safety-relevant software change — becomes the manufacturer and must redo conformity assessment. Non-professional users modifying their own machinery are exempt.
- Importers and distributors who rebrand or modify a product inherit manufacturer obligations (Art. 17).

## Core obligations

### RED cyber requirements — manufacturer duties and conformity route

| Duty | Source | Detail |
|---|---|---|
| Design to the essential requirements | RED Art. 3(3)(d)–(f), Art. 10(1) | The three requirements above; the EN 18031 series translates them into assessable security mechanisms with per-clause assessment criteria (the OJ notices single out its clauses on default passwords, access control for toys/childcare equipment and secure updates) |
| Technical documentation and 10-year retention | RED Art. 10(3)–(4), Art. 21 | Keep technical documentation and the EU declaration of conformity for 10 years after placing on the market |
| Series-production controls and post-market monitoring | RED Art. 10(5) | Track design changes and changes in the harmonised standards relied on; sample-test, register complaints, non-conformities and recalls where risk warrants |
| Instructions, identification, DoC with the product | RED Art. 10(6)–(9) | Type/batch/serial number; manufacturer contact point; instructions including description of software allowing intended operation; copy of the EU DoC or simplified DoC with the exact internet address of the full text |
| Corrective action and authority notification | RED Art. 10(11)–(12) | Immediate corrective measures, withdrawal or recall for non-conforming equipment; inform national authorities where the equipment presents a risk; supply documentation on reasoned request |
| Conformity assessment | RED Art. 17(3)–(4) | Harmonised standards applied in full: module A (Annex II), B + C (Annex III) or H (Annex IV) at the manufacturer's choice. Standards not applied, or applied only in part, or non-existent: B + C or H — i.e. a notified body is mandatory |

**EN 18031:2024 and its restrictions.** Commission Implementing Decision (EU) 2025/138 (28 January 2025) added EN 18031-1:2024 (network, Art. 3(3)(d)), EN 18031-2:2024 (data and privacy, Art. 3(3)(e), covering internet-connected, childcare, toy and wearable equipment) and EN 18031-3:2024 (virtual money/monetary value, Art. 3(3)(f)) to the OJ list under Implementing Decision (EU) 2022/2191, entries 164–166, **with restrictions** that determine whether self-assessment is available:

| Restriction | Applies to | Effect (Commission guidance on the EN 18031 series) |
|---|---|---|
| "Rationale" and "guidance" sections confer no presumption of conformity | All three parts | Informative only; no third-party assessment triggered |
| No presumption if, applying clauses 6.2.5.1 and 6.2.5.2, the user is allowed not to set and use any password | All three parts | Presumption retained if the manufacturer designs out the "no password" option; otherwise notified body |
| No presumption for toy and childcare equipment (clauses 6.1.3–6.1.6) if parental or guardian access control is not ensured | EN 18031-2 | Presumption retained if parental/guardian control is implemented; otherwise notified body |
| No presumption for the secure-update assessment criteria in clause 6.3.2.4 | EN 18031-3 | None of the four update mechanisms alone was judged sufficient for financial assets: third-party conformity assessment is mandatory for products to which 6.3.2.4 applies, regardless of design |

Commission guidance is explicit that self-assessment "is allowed only if the relevant harmonised standards of the EN 18031:2024 family is applied to the product and is not affected by the restrictions". Only notified bodies specifically listed for Art. 3(3)(d)/(e)/(f) in NANDO may issue EU type-examination certificates for these requirements (24 such bodies at the time the guidance was issued). Voluntary third-party assessment remains possible at any time.

### Machinery Regulation — cybersecurity-relevant EHSRs and manufacturer duties

| Requirement | Source | What it demands |
|---|---|---|
| Risk assessment drives everything | Annex III, General Principles pt. 1 | Iterative risk assessment and reduction determining applicable EHSRs; must cover the product lifecycle, foreseeable evolution of self-evolving (machine-learning) behaviour, and interactions between machines. Annex IV Part A(b) requires the risk-assessment documentation, listing each applicable EHSR and the protective measures for it |
| Protection against corruption | Annex III 1.1.9 | Connecting another device (local or remote) must not lead to a hazardous situation; hardware transmitting signals/data relevant to safety-critical software must be protected against accidental or intentional corruption and must collect evidence of legitimate or illegitimate intervention; safety-critical software and data must be identified and protected; the machine must identify the software needed for safe operation and provide that information at all times; it must log interventions in or modifications to installed software or its configuration |
| Safety and reliability of control systems | Annex III 1.2.1 | Control systems must withstand "intended and unintended external influences, including reasonably foreseeable malicious attempts from third parties leading to a hazardous situation"; hardware/logic faults and human error must not create hazards; safety-function limits are fixed in the risk assessment and settings or machine-generated rules must not be modifiable where hazardous (including during a learning phase); a tracing log of interventions and of safety-software versions uploaded after placing on the market must be enabled for **five years** after each upload, for authorities' reasoned requests only |
| Self-evolving / autonomous control systems | Annex III 1.2.1, second set of points | Must not act beyond the defined task and movement space; safety-related decision data must be recorded and retained for **one year**; it must always be possible to correct the machine to maintain inherent safety |
| Technical documentation | Art. 10(2)–(3), Annex IV Part A | Includes the risk-assessment file, applied standards/common specifications, test reports, series-production controls, a description of data, development, testing and validation processes for sensor-fed, remotely driven or autonomous machinery (A(n)), and — on reasoned request from a national authority — the source code or programming logic of safety-related software (A(m)). Keep technical documentation and the EU DoC at least 10 years |
| Instructions and declarations | Art. 10(7)–(8), Art. 21 | Digital instructions allowed but must stay online for the expected lifetime and at least 10 years, be downloadable/printable, and be supplied on paper within one month on request; a single EU DoC covers all applicable Union acts (Art. 21(3)) — the same document will carry RED, EMC, LVD and, later, CRA references |
| Post-market duties | Art. 10(4), (9)–(10) | Series-production conformity, sample testing and complaint/recall registers where risk warrants; immediate corrective action, withdrawal or recall for non-conforming products; inform authorities where health, safety, property or the environment is at risk |

### Machinery Regulation — conformity assessment (Art. 25, Annex I)

| Product category | Route |
|---|---|
| Annex I Part A — e.g. removable mechanical transmission devices and their guards, vehicle servicing lifts, cartridge-operated fixing tools, **safety components with fully or partially self-evolving behaviour using machine learning approaches ensuring safety functions**, and **machinery with embedded self-evolving ML systems ensuring safety functions** (for those systems only) | Mandatory third party: EU type-examination + conformity to type (modules B + C), full quality assurance (module H) or unit verification (module G) |
| Annex I Part B — 19 categories including logic units to ensure safety functions, protective devices detecting the presence of persons, presses, woodworking saws, refuse trucks, person-lifting devices, ROPS/FOPS | Internal production control (module A) **only if** designed and built in accordance with harmonised standards or common specifications covering all relevant EHSRs for that category; otherwise B + C, H or G |
| Everything else | Module A (internal production control) |

Where a notified body is involved, its identification number follows the CE mark (Art. 24(3)). The Commission may add, remove or move Annex I categories by delegated act based on probability and severity of harm (Art. 6).

### Presumption of conformity — standards and certificates

- **RED**: harmonised standards listed under Implementing Decision (EU) 2022/2191 (as amended; latest amendment 4 September 2026 per the Commission's RED harmonised-standards page). Only the EN 18031 entries carry the cybersecurity presumption, subject to the restrictions above.
- **Machinery**: Art. 20(1) presumption via harmonised standards; Art. 20(3) common specifications as a fallback. The list under the 2006 Directive (Implementing Decision (EU) 2023/1586, last amended 4 September 2026) loses effect on 20 January 2027; as of September 2026 the Commission states that the first Machinery Regulation list "can be expected before the end of this year" and will clarify where existing standards do not yet fully address new or updated EHSRs — the cybersecurity and AI EHSRs are the ones most likely to lack full standards coverage at application. Plan for a period in which 1.1.9 and 1.2.1 are demonstrated by risk assessment and other technical specifications rather than a harmonised standard.
- **Art. 20(9)**: machinery certified, or covered by a statement of conformity, under a Cybersecurity Act (Regulation (EU) 2019/881) certification scheme whose references are published in the OJ is presumed to conform to sections 1.1.9 and 1.2.1 insofar as the certificate covers them. No such scheme reference had been published for machinery as of September 2026 (verify).
- **Art. 20(10)** (inserted by Regulation (EU) 2026/1744): until Machinery Regulation standards for high-risk AI systems exist, compliance with AI Act harmonised standards or common specifications gives the presumption for the AI-related EHSRs.

## Enforcement and penalties

| Regime | Mechanism |
|---|---|
| RED | National market surveillance under Regulation (EU) 2019/1020 and RED Chapter V (Union market surveillance, control of equipment entering the Union market and Union safeguard procedure). Penalties are national (Art. 46): effective, proportionate and dissuasive, criminal penalties possible for serious infringements. Enforcement continues after the 2027 repeal for equipment placed on the market between 1 August 2025 and 10 December 2027 (Delegated Regulation (EU) 2026/339, recital 5) |
| Machinery Regulation | Chapter VI market surveillance (Arts. 43–46); Art. 50 penalties are national, may include criminal penalties, and Member States must notify their rules to the Commission by **20 October 2026** (corrected date). Authorities may demand source code or programming logic of safety-related software (Art. 10(3), Annex IV A(m)) |
| CRA (successor regime) | Administrative fines up to EUR 15 000 000 or 2.5 % of worldwide annual turnover for breaches of Annex I essential requirements and Arts. 13–14; EUR 10 000 000 / 2 % for other operator obligations; EUR 5 000 000 / 1 % for misleading information to notified bodies or authorities (Art. 64) — the step-change in exposure when RED cyber obligations migrate |

## Timeline and status

| Date | Event |
|---|---|
| 13 June 2016 | RED applicable (Commission RED page) |
| 29 October 2021 / 12 January 2022 | Delegated Regulation (EU) 2022/30 adopted / published; original application date 1 August 2024 |
| 20 July 2023 / 27 October 2023 | Delegated Regulation (EU) 2023/2444 adopted / published: application deferred to 1 August 2025; Art. 1(2) wording corrected to "traffic data or location data" |
| 14 June 2023 / 29 June 2023 | Machinery Regulation adopted / published; corrigendum of 4 July 2023 fixed the application dates (entry into force 19 July 2023; notified-body provisions Arts. 26–42 from 20 January 2024) |
| 28 January 2025 / 30 January 2025 | Implementing Decision (EU) 2025/138 adopted / published: EN 18031-1/-2/-3:2024 cited with restrictions |
| 1 August 2025 | RED Art. 3(3)(d)–(f) requirements apply to in-scope radio equipment placed on the market |
| 20 January 2026 | Commission abandons the separate RED Art. 3(3)(i)/Art. 4 reconfigurable-radio-software initiative (Commission RED page) |
| 16 February 2026 / 29 April 2026 | Delegated Regulation (EU) 2026/339 adopted / published: repeals 2022/30 with effect from 11 December 2027 |
| 11 June 2026 | CRA Chapter IV (notification of conformity assessment bodies) applies |
| 8 July 2026 / 24 July 2026 / 27 July 2026 | Regulation (EU) 2026/1744 (Digital Omnibus on AI) adopted / published / in force: Machinery Regulation moved from Section A to Section B of AI Act Annex I; new Art. 8 third paragraph requires Commission delegated acts adding AI-related EHSRs to Annex III (reflecting AI Act Chapter III Section 2 and Arts. 17, 19, 72, 73) applying by 2 August 2028; new Art. 20(10) interim presumption via AI Act standards |
| 11 September 2026 | CRA Art. 14 reporting obligations apply to all products with digital elements, including those already on the market (24 h early warning, 72 h notification, 14-day final report for actively exploited vulnerabilities) |
| 20 October 2026 | Member States notify Machinery Regulation penalty rules |
| Q4 2026 (expected) | First OJ citation of harmonised standards under the Machinery Regulation (Commission statement, September 2026) |
| 20 January 2027 | Machinery Regulation applies; Directive 2006/42/EC repealed; products lawfully placed under the Directive before that date may continue to be made available (Art. 52); Directive-era EC type-examination certificates remain valid until expiry |
| 11 December 2027 | CRA applies in full; Delegated Regulation (EU) 2022/30 repealed. RED-era EU type-examination certificates on cybersecurity remain valid until 11 June 2028 unless they expire earlier (CRA Art. 69(1)); products placed on the market before this date fall under the CRA only if substantially modified (Art. 69(2)) |
| 2 August 2028 | Deadline for Machinery Regulation AI-related EHSR delegated acts to apply |

Status as of September 2026: the RED regime is live and will be replaced, not amended; the Machinery Regulation is four months from application with its cybersecurity standards not yet cited; the AI interface for machinery was materially rewritten in July 2026 and depends on delegated acts still to be adopted.

## Key obligations for security/GRC teams

1. **Classify the product portfolio against both scope tests** — radio interface + internet connectivity/personal data/payment for the RED act; Art. 2 categories and Annex I risk classes for machinery; note the Art. 2(2)(p) hand-off between the two. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Decide the conformity route deliberately**: map each RED product to EN 18031 clauses and check the four OJ restrictions; where a restriction bites (no-password option, missing parental control, any EN 18031-3 product under clause 6.3.2.4) budget for a notified body. For machinery, check whether ML-based safety functions push the product into Annex I Part A.
3. **Build a product-security risk assessment that feeds the technical file** — the machinery risk assessment must explicitly address malicious third-party attempts (1.2.1(a)) and software/hardware corruption (1.1.9); reuse the organisation's threat-modelling method and record residual risks per EHSR. See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).
4. **Engineer the evidence the law names**: tamper evidence on safety-relevant hardware, software-inventory readout, intervention/modification logs, the five-year safety-software version log and one-year decision-data retention for self-evolving systems, and access-controlled, printable digital instructions kept online for at least 10 years. Treat these as controls with owners and tests. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
5. **Run a dual-track compliance plan for 2025–2028**: RED EN 18031 evidence now, CRA Annex I essential requirements and vulnerability-handling processes in parallel, so that the 11 December 2027 switch is a re-labelling exercise, not a redesign. CRA Art. 14 reporting already applies. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
6. **Control "substantial modification" in the field**: a change-management gate for safety-relevant firmware/software updates on deployed machinery, so that neither the manufacturer nor an integrator or operator unknowingly becomes a new manufacturer under Art. 18. See [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
7. **Flow requirements to component and software suppliers** — radio modules, safety PLCs, cloud back-ends that count as remote data processing under the CRA — with contractual rights to security evidence, vulnerability notifications and long-term update support. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
8. **Track the open items on the horizon**: the first Machinery Regulation standards list, the AI-EHSR delegated acts due by 2 August 2028, any CRA delegated act limiting its application to sector rules (CRA Art. 2(5)), and Cybersecurity Act schemes that could unlock the Art. 20(9) presumption. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md) and [../../workflows/new-regulation-impact-assessment.md](../../workflows/new-regulation-impact-assessment.md).
9. **Prepare the audit trail**: technical documentation, DoC, notified-body certificates and standards versions organised so a market surveillance authority's reasoned request — including for source code or programming logic — can be met. See [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md) and [../../templates/audit-evidence-request-list.md](../../templates/audit-evidence-request-list.md).

## Interplay

- **Cyber Resilience Act (Regulation (EU) 2024/2847)** — see the separate Cyber Resilience Act context pack for the full regime. The CRA's Annex I essential cybersecurity requirements "include all the elements" of RED Art. 3(3)(d)–(f) (Delegated Regulation (EU) 2026/339, recital 3), which is why the RED act is repealed on 11 December 2027 rather than kept in parallel. The CRA excludes the same medical-device, IVD and vehicle products as the RED act (CRA Art. 2(2)) and products certified under the civil-aviation regulation (Art. 2(3)). For machinery the CRA is **cumulative**: recital 53 says manufacturers of machinery that is a product with digital elements must meet both sets of essential requirements, that CRA compliance "could facilitate" compliance with 1.1.9 and 1.2.1, and that synergies must be demonstrated by the manufacturer through harmonised standards or a risk assessment; both conformity assessment procedures still apply.
- **EU AI Act** — after the Digital Omnibus on AI, machinery with high-risk AI safety components is governed through the Machinery Regulation's own (forthcoming) AI EHSRs rather than the AI Act's full high-risk regime; see [eu-ai-act.md](eu-ai-act.md) and [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).
- **GDPR / ePrivacy** — the RED Art. 3(3)(e) trigger is defined by reference to GDPR Art. 4(1)–(2) and ePrivacy Art. 2(b)–(c); product-level safeguards do not replace controller/processor obligations. Connected products embedding personal-data processing usually also warrant a DPIA; see [gdpr.md](gdpr.md) and [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).
- **NIS2** — an operator deploying connected machinery in an essential or important entity must manage supply-chain and product security as part of its Art. 21 measures; manufacturer conformity evidence becomes procurement evidence. See [nis2.md](nis2.md).
- **Other CE-marking acts** — where several Union acts apply to one machine, Art. 21(3) requires a single EU DoC identifying all of them (LVD, EMC, RED and later CRA references on one document); the Machinery Regulation's Art. 2(2)(p) draws the line for IT and household electronics, which are RED/LVD (and, from 2027, CRA) products, not machinery.
- **Control frameworks** — EN 18031 mechanisms and the machinery EHSRs map naturally onto product-security controls in [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) Annex A (secure development, logging, cryptography) and the Protect/Detect functions of [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md); use [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md) for coverage analysis, not equivalence claims.

## Primary sources

- Directive 2014/53/EU (Radio Equipment Directive) — legal text, Publications Office (CELEX 32014L0053): https://eur-lex.europa.eu/eli/dir/2014/53/oj
- Commission Delegated Regulation (EU) 2022/30 — legal text (CELEX 32022R0030): https://eur-lex.europa.eu/eli/reg_del/2022/30/oj
- Commission Delegated Regulation (EU) 2023/2444 (postponement to 1 August 2025 and correction) — legal text (CELEX 32023R2444): https://eur-lex.europa.eu/eli/reg_del/2023/2444/oj
- Commission Implementing Decision (EU) 2025/138 (EN 18031 citation with restrictions) — legal text (CELEX 32025D0138): https://eur-lex.europa.eu/eli/dec_impl/2025/138/oj
- Commission Delegated Regulation (EU) 2026/339 (repeal of 2022/30 from 11 December 2027) — legal text (CELEX 32026R0339): https://eur-lex.europa.eu/eli/reg_del/2026/339/oj
- Regulation (EU) 2023/1230 (Machinery Regulation) — legal text, original OJ publication (CELEX 32023R1230), corrigendum of 4 July 2023 (OJ L 169, p. 35) and consolidated text of 27 July 2026 (CELEX 02023R1230-20260727): https://eur-lex.europa.eu/eli/reg/2023/1230/oj
- Regulation (EU) 2026/1744 (Digital Omnibus on AI; Art. 3 amends the Machinery Regulation) — legal text (CELEX 32026R1744): https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- Regulation (EU) 2024/2847 (Cyber Resilience Act) — legal text (CELEX 32024R2847): https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- European Commission, Radio Equipment Directive (RED) page — regulator guidance (application dates, repeal, reconfigurable-radio decision): https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red_en
- European Commission, "Guidance on the application of the harmonised standards series EN 18031:2024 in support of Commission Delegated Regulation 2022/30" (DG GROW, v1) — regulator guidance; consulted via an industry-association mirror: https://www.vdma.eu/documents/d/group-34568/com-red-hs-cyber-guidance_v1
- European Commission, harmonised standards pages for radio equipment and machinery — regulator guidance (OJ citation history, Machinery Regulation list status): https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards/radio-equipment_en and https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards/machinery-md_en
- European Commission, Machinery sector page — regulator guidance (20 January 2027 application, corrigendum, notified bodies): https://single-market-economy.ec.europa.eu/sectors/mechanical-engineering/machinery_en
- EN 18031-1/-2/-3:2024 themselves are CEN/CENELEC standards sold through national standards bodies; their full text is paywalled and was not consulted — clause references above are those quoted in Implementing Decision (EU) 2025/138 and the Commission guidance.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
