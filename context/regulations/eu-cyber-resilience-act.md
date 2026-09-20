# EU Cyber Resilience Act — Regulation (EU) 2024/2847 (CRA)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Regulation (EU) 2024/2847 of 23 October 2024 on horizontal cybersecurity requirements for products with digital elements (OJ L, 2024/2847, 20.11.2024) — directly applicable, no transposition; adopted under Art. 114 TFEU as New Legislative Framework product law (CE marking) |
| Publisher / regulators | European Commission (DG CONNECT) owns policy, guidance, delegated and implementing acts; national **market surveillance authorities** enforce (Art. 52); **CSIRTs designated as coordinators** and **ENISA** receive Art. 14 reports; notified bodies perform third-party conformity assessment |
| Status and key dates | In force 10 December 2024. Chapter IV (notified bodies, Arts. 35–51) applies from **11 June 2026**; Art. 14 reporting applies from **11 September 2026** (live, single reporting platform operational); everything else from **11 December 2027** (Art. 71) |
| Who is covered | Manufacturers, authorised representatives, importers and distributors of **products with digital elements** made available on the EU market, wherever the manufacturer is established; a light regime for **open-source software stewards** (Art. 24) |
| Structure | 8 chapters, 71 articles, 8 annexes. Annex I = essential requirements (Part I product properties, Part II vulnerability handling); Annex II = user information; Annex III = important products (class I / II); Annex IV = critical products; Annex VII = technical documentation; Annex VIII = conformity modules A, B+C, H |
| Penalties | Administrative fines up to **EUR 15 million or 2.5 % of worldwide annual turnover** (Annex I, Arts. 13–14); EUR 10 million / 2 % for other operator obligations; EUR 5 million / 1 % for misleading information to authorities (Art. 64). Plus withdrawal, recall and market bans (Arts. 54–58); consumer representative actions (Art. 65) |
| Assessment model | Manufacturer self-assessment (module A) by default; notified-body assessment (module B+C or H) mandatory for important class II and, absent applicable harmonised standards, class I; European cybersecurity certification at level "substantial" foreseen for critical products (Arts. 8, 27, 32) |
| Reporting clock | Actively exploited vulnerability or severe incident: early warning **24 h**, notification **72 h**, final report **14 days** after a fix is available (vulnerabilities) or **1 month** after the 72 h notification (incidents) — via ENISA's Single Reporting Platform (Arts. 14, 16) |
| Support period | Manufacturer-determined, **minimum 5 years** unless the product is expected to be used for less; security updates must stay available for at least 10 years or the support period, whichever is longer (Art. 13(8)–(9)) |
| Neighbours | Complements NIS2 (supply-side vs operator-side), Cybersecurity Act certification schemes, RED delegated act 2022/30 (repealed from 11 December 2027), AI Act, GPSR, Product Liability Directive (EU) 2024/2853 |

## What it is

The CRA is the EU's first horizontal product-security law. It treats cybersecurity the way EU law has long treated electrical safety or radio emissions: as an essential requirement that hardware and software must meet before it can be CE-marked and sold, backed by market surveillance rather than sectoral supervisors. Recital 1 names the two problems it targets — a low level of product cybersecurity reflected in widespread vulnerabilities and inconsistent security updates, and users' inability to tell secure products from insecure ones (Art. 1 lists the four things the Regulation lays down: market-access rules, design/development requirements, vulnerability-handling requirements, and market surveillance).

Unlike NIS2 or DORA, which regulate the organisations that *use* technology, the CRA regulates the organisations that *make and sell* it. Obligations follow the product through its whole lifecycle: risk assessment at design, secure-by-default configuration at delivery, vulnerability handling and free security updates for a defined support period, and mandatory reporting of actively exploited vulnerabilities to EU authorities. Its detail layer is still being built: an implementing regulation on product categories (2025), a delegated act on notification withholding (2026), a Commission guidance document (July 2026), and 41 harmonised standards under mandate M/606 that are not yet cited in the Official Journal.

## Who it covers / Scope

**Product test (Art. 2(1), Art. 3(1)):** a *product with digital elements* is any software or hardware product, and its remote data processing solutions, including components placed on the market separately, whose intended purpose or reasonably foreseeable use includes a direct or indirect logical or physical data connection to a device or network. "Remote data processing" is only in scope where the manufacturer designs it and the product cannot perform a function without it (Art. 3(2)) — on this definition a standalone cloud service with no product dependency is generally read as outside the CRA (the July 2026 Commission guidance addresses remote data processing; verify per product), while the provider may still be a NIS2 entity.

**Exclusions (Art. 2(2)–(8)):** products under the Medical Devices Regulation (EU) 2017/745, IVDR (EU) 2017/746, vehicle type-approval Regulation (EU) 2019/2144; products certified under civil-aviation Regulation (EU) 2018/1139; marine equipment under Directive 2014/90/EU; identical spare parts; products developed or modified exclusively for national security or defence, or designed to process classified information. The Commission may limit application by delegated act where sectoral rules give equal or higher protection (Art. 2(5)).

**Economic operators and reach:**

| Role | Test | Core obligations |
|---|---|---|
| Manufacturer (Art. 3(13)) | Develops/has developed a product and markets it under its own name or trademark, paid or free of charge — no EU establishment needed | Arts. 13–14 in full |
| Deemed manufacturer (Arts. 21–22) | Importer/distributor selling under own brand, or anyone making a **substantial modification** and placing the result on the market | Arts. 13–14 for the modified part or whole product |
| Authorised representative (Art. 18) | EU-established person with written mandate | Keeps declaration of conformity and technical documentation for 10 years / support period; answers authorities |
| Importer (Art. 19) | EU-established, places a non-EU-branded product on the market | Verifies conformity assessment, documentation, CE marking, Annex II instructions and Art. 13(15),(16),(19) before placing; passes vulnerabilities to manufacturer; informs authorities of significant risk |
| Distributor (Art. 20) | Makes a product available without changing it | Due-care check of CE marking and upstream compliance; corrective action; vulnerability pass-through |
| Open-source software steward (Arts. 3(14), 24) | Legal person (foundations, not-for-profits, businesses) that systematically supports development of FOSS intended for commercial activities without itself being the manufacturer | Documented cybersecurity policy; cooperate with authorities; Art. 14(1),(3),(8) reporting to the extent involved — **no administrative fines** (Art. 64(10)) |

**Free and open-source software:** only FOSS *made available on the market in the course of a commercial activity* is in scope (Recital 18); non-monetised FOSS and individual contributors to code they do not control are out; merely hosting on repositories or package managers is not "making available" (Recital 20). FOSS manufacturers of Annex III products may self-assess if they publish their technical documentation (Art. 32(5)). Voluntary security attestation programmes may be created by delegated act (Art. 25).

**Products already on the market:** the Regulation applies to products placed on the market before 11 December 2027 only if they are substantially modified after that date — except Art. 14 reporting, which applies to all in-scope products regardless of placement date (Art. 69(2)–(3)). Free-movement and SME relief: reduced conformity-assessment fees (Art. 32(6)), Member State support measures (Art. 33), simplified technical documentation format for micro and small enterprises, to be specified by implementing act (Art. 33(5)); optional national cyber resilience regulatory sandboxes (Art. 33(2)).

## Core obligations

### Essential requirements (Annex I)

| Part | Requirement (abbreviated) |
|---|---|
| I(1) | Designed, developed and produced to ensure an appropriate level of cybersecurity based on the risks |
| I(2)(a)–(c) | No known exploitable vulnerabilities at release; secure-by-default configuration with factory reset; security updates, automatic by default where applicable with opt-out, notified to users, separable from feature updates |
| I(2)(d)–(g) | Access control incl. authentication and reporting of unauthorised access; confidentiality (state-of-the-art encryption at rest and in transit); integrity of data, commands, programs and configuration; data minimisation |
| I(2)(h)–(k) | Availability of essential functions incl. DoS resilience; limit impact on other devices/networks; minimise attack surface incl. external interfaces; exploitation-mitigation mechanisms |
| I(2)(l)–(m) | Security logging and monitoring with user opt-out; secure permanent deletion and secure data transfer |
| II(1)–(3) | Identify and document vulnerabilities and components, including a **machine-readable SBOM** covering at least top-level dependencies; remediate without delay, security updates separate from functionality updates where feasible; regular security tests and reviews |
| II(4)–(6) | Public disclosure of fixed vulnerabilities once an update is available (delay permitted where risk outweighs benefit); enforced **coordinated vulnerability disclosure policy**; contact address for vulnerability reports and information-sharing facilitation |
| II(7)–(8) | Secure update distribution mechanisms; updates disseminated without delay and **free of charge** (except tailor-made B2B products) with advisory messages |

### Manufacturer duties (Art. 13)

| Provision | Duty |
|---|---|
| 13(2)–(3) | Documented product cybersecurity risk assessment, maintained through the support period, stating which Annex I Part I(2) requirements apply and how |
| 13(5)–(6) | Due diligence on third-party and open-source components; report component vulnerabilities upstream and remediate |
| 13(7) | Systematically document cybersecurity aspects, including vulnerabilities and third-party information |
| 13(8) | Determine the **support period** reflecting expected use time, user expectations, product nature and Union law on product lifetime; **at least 5 years** unless expected use is shorter; reasoning recorded in technical documentation; Commission may set category minimums by delegated act |
| 13(9)–(11) | Each security update remains available for **10 years or the remainder of the support period**, whichever is longer; only the latest substantially modified software version need be patched if users can move to it free of charge; archives of unsupported versions must carry risk warnings |
| 13(12)–(13) | Technical documentation (Annex VII) drawn up before placing on the market; kept with the EU declaration of conformity for **10 years or the support period**, whichever is longer |
| 13(15)–(20) | Product identification; manufacturer contact details; **single point of contact** for users and vulnerability reporters; Annex II information and instructions (kept available online 10 years / support period); support-period end date (at least month and year) shown at purchase; EU declaration of conformity or simplified declaration with URL |
| 13(21)–(23) | Immediate corrective action, withdrawal or recall on non-conformity; cooperation with authorities; notify authorities and users before ceasing operations |
| 13(24) | Commission may prescribe SBOM format and elements by implementing act |

Technical documentation (Annex VII) must include the product description and software versions, design/development and vulnerability-handling process descriptions (SBOM, CVD policy, contact address, update mechanism), the cybersecurity risk assessment, support-period rationale, standards applied, test reports and the declaration of conformity; the SBOM itself is supplied to authorities on reasoned request.

### Reporting obligations (Art. 14) — applying since 11 September 2026

| Trigger | Stage | Deadline | Minimum content |
|---|---|---|---|
| **Actively exploited vulnerability** (reliable evidence of exploitation without the system owner's permission, Art. 3(42)) | Early warning | **24 h** of becoming aware | Member States where the product is known to be available |
| | Vulnerability notification | **72 h** of becoming aware | Product, general nature of exploit and vulnerability, corrective/mitigating measures taken and available to users, sensitivity indication |
| | Final report | **14 days** after a corrective or mitigating measure is available | Description, severity and impact; threat actor if known; details of the fix |
| **Severe incident** affecting product security (capable of affecting availability, authenticity, integrity or confidentiality of sensitive/important data or functions, or of introducing/executing malicious code in the product or a user's systems, Art. 14(5)) | Early warning | **24 h** | Whether unlawful/malicious acts are suspected; Member States affected |
| | Incident notification | **72 h** | Nature, initial assessment, measures taken and available to users, sensitivity |
| | Final report | **1 month** after the 72 h notification | Detailed description, severity, impact; likely threat or root cause; applied and ongoing mitigations |

- Notifications go **simultaneously** to the CSIRT designated as coordinator of the Member State of the manufacturer's main establishment (where product-cybersecurity decisions are predominantly taken) and to ENISA, through the **Single Reporting Platform** (Art. 16) — the receiving CSIRT may also request intermediate reports (Art. 14(6)). Non-EU manufacturers use the CSIRT of the Member State of their authorised representative, then importer, then distributor, then largest user base (Art. 14(7)).
- The receiving CSIRT disseminates the notification to the CSIRTs of every Member State where the product is available and to the market surveillance authorities. It may **delay dissemination** on cybersecurity grounds: Delegated Regulation (EU) 2026/881 allows this where a mitigation is expected within 72 hours, where the report would enable easy exploitation, where partial information suffices for mitigation, where the CSIRT is a CVD intermediary, or where a recipient CSIRT or the platform itself is compromised.
- Manufacturers must also **inform impacted users** (all users where appropriate) of the vulnerability or incident and of mitigations, in machine-readable form where appropriate; CSIRTs may do so if the manufacturer fails to (Art. 14(8)).
- **Voluntary reporting** (Art. 15) of any vulnerability, cyber threat, incident or near miss is open to manufacturers and third parties and cannot create additional obligations for the reporter.
- ENISA's platform (initial operating capability launched 11 September 2026) requires registration of **Assigned Representatives** for each manufacturer; ENISA publishes FAQs, a glossary, user manuals and the list of coordinator CSIRTs. Micro and small enterprises are exempt from fines for missing the 24-hour early-warning deadline only (Art. 64(10)(a)).
- Open-source software stewards' reporting duties apply from 11 December 2027 (Art. 24(3), Art. 71(2)).

### Product classes and conformity assessment (Arts. 7–8, 27, 32; Annexes III, IV, VIII)

| Class | Examples (Annex III / IV, technical descriptions in Implementing Regulation (EU) 2025/2392) | Permitted procedures |
|---|---|---|
| Default | Everything not listed — apps, games, smart speakers, memory chips | Internal control (module A), or any stricter route, or an EU certification scheme where listed (Art. 32(1)) |
| Important class I (19 categories) | Identity and privileged access management, browsers, password managers, anti-malware, VPN products, network management, SIEM, boot managers, PKI/certificate software, network interfaces, operating systems, routers/modems/switches, security-function microprocessors, microcontrollers, ASICs/FPGAs, smart-home assistants, smart-home security products, connected toys with social or location features, health-monitoring wearables not under MDR/IVDR | Module A **only if harmonised standards, common specifications or an EU scheme at level "substantial" are applied in full**; otherwise module B+C or H (Art. 32(2)) |
| Important class II (4 categories) | Hypervisors and container runtimes, firewalls and IDS/IPS, tamper-resistant microprocessors, tamper-resistant microcontrollers | Module B+C, module H, or an EU certification scheme at level "substantial" (Art. 32(3)) — notified body always involved |
| Critical (Annex IV) | Hardware devices with security boxes, smart meter gateways and secure cryptoprocessing devices, smartcards and secure elements | European cybersecurity certificate at level at least "substantial" where a delegated act under Art. 8(1) mandates it; until then, the class II routes (Art. 32(4)) |

Integrating an important component does not make the whole product important (Art. 7(1)). Harmonised standards published in the OJ, Commission common specifications and Cybersecurity Act certificates give a presumption of conformity (Art. 27); a certificate at level "substantial" removes the third-party assessment obligation for the requirements it covers (Art. 27(9)). High-risk AI systems that are also products with digital elements are deemed to meet AI Act Art. 15 cybersecurity requirements if they meet Annex I, and generally follow the AI Act conformity route, except important/critical products which follow CRA procedures (Art. 12).

## Enforcement and penalties

- **Market surveillance** under Regulation (EU) 2019/1020 (Art. 52): each Member State designates authorities; they cooperate with CSIRTs, ENISA, data protection authorities (who may access CRA documentation) and AI Act authorities (who take the lead for high-risk AI products). An administrative cooperation group (ADCO) coordinates, publishes statistics and indicative support periods per category, and may run Union-wide SBOM dependency assessments (Arts. 13(25), 52(15)–(16)).
- **Corrective procedure** (Art. 54): where a product, including its vulnerability handling, presents a significant cybersecurity risk (Art. 3(38): high likelihood of an incident with severe negative impact), the authority evaluates it, orders correction, withdrawal or recall within a prescribed period, and can prohibit or restrict the product nationally with EU-wide notification; non-technical risk factors from NIS2 Art. 22 supply-chain risk assessments count. Union safeguard, compliant-but-risky products and formal non-compliance procedures follow in Arts. 55–58.
- **Administrative fines** (Art. 64) are set and imposed nationally within EU ceilings; criteria include gravity, duration, repeat conduct and SME size, and fines can be stacked with corrective measures:

| Infringement | Ceiling |
|---|---|
| Annex I essential requirements; manufacturer obligations (Art. 13); reporting (Art. 14) | EUR 15 million or 2.5 % of total worldwide annual turnover, whichever is higher |
| Other operator obligations (Arts. 18–23), declaration of conformity (Art. 28), CE marking (Art. 30(1)–(4)), technical documentation (Art. 31(1)–(4)), conformity assessment (Art. 32(1)–(3)), Art. 33(5), notified-body rules (Arts. 39, 41, 47, 49), access to documentation (Art. 53) | EUR 10 million or 2 % |
| Incorrect, incomplete or misleading information to notified bodies or authorities | EUR 5 million or 1 % |

- Derogations: micro and small manufacturers are not fined for missing the 24-hour early-warning deadline; open-source software stewards are not fined at all (Art. 64(10)). Member States decide whether public bodies can be fined (Art. 64(7)).
- **Consumer collective redress** applies via Directive (EU) 2020/1828 (Art. 65); the recast Product Liability Directive (EU) 2024/2853, cited in the CRA's recitals, governs civil liability for defective products separately (its text was not reviewed for this pack).

## Timeline and status

| Date | Event |
|---|---|
| 23 Oct 2024 / 20 Nov 2024 | Adopted / published in OJ; entry into force 10 December 2024 |
| 1 Aug 2025 | RED Delegated Regulation (EU) 2022/30 cybersecurity requirements for radio equipment (RED Art. 3(3)(d)–(f)) became applicable — the interim regime for connected wireless products |
| 3 Apr 2025 | CEN, CENELEC and ETSI accepted standardisation request M/606 (41 harmonised standards, horizontal and product-specific); work led by CEN-CLC/JTC 13 WG 9, CEN/TC 224, CLC/TC 65X, CLC/TC 47X and ETSI TC CYBER (EUSR) |
| Nov 2025 | Commission **Digital Omnibus** proposal: a single-entry point for incident reporting to be run by ENISA, building on the CRA platform; first stage covers NIS2, GDPR, DORA, CER and eIDAS, and the Commission states it would not modify existing reporting obligations (CRA product reporting itself unchanged). Still a proposal rather than adopted law as of September 2026 (verify) |
| 28 Nov 2025 | Commission Implementing Regulation (EU) 2025/2392 (OJ 1.12.2025) — technical descriptions of Annex III and IV categories, adopted under Art. 7(4) |
| 11 Dec 2025 | Delegated Regulation (EU) 2026/881 adopted (OJ 20.4.2026) — terms for CSIRTs delaying dissemination of notifications (Art. 16(2)) |
| 16 Feb 2026 | Delegated Regulation (EU) 2026/339 (OJ 29.4.2026) repeals RED delegated act 2022/30 **with effect from 11 December 2027** to avoid double regulation |
| 11 Jun 2026 | Chapter IV applies: Member States designate notifying authorities; conformity assessment bodies can be notified (NANDO listing) |
| 27 Jul 2026 | Commission publishes first (non-binding) CRA guidance under Art. 26 (Communication C(2026) 5252 and its annex): scope incl. remote data processing and FOSS, substantial modification, support periods, reporting and risk assessment; 67 worked examples plus use cases and flowcharts; FAQ maintained alongside (reporting is Section 9.1 of the guidance, Section 5 of the FAQ) |
| 11 Sep 2026 | **Art. 14 reporting obligations apply; ENISA Single Reporting Platform live** (initial operating capability) |
| Q3 2026 (planned) | First standardisation deliverables, horizontal and product-specific (Commission implementation roadmap). The Commission's harmonised-standards index still lists no entry for the CRA as of September 2026, so no Art. 27 presumption of conformity from harmonised standards is available in practice yet — check the OJ before relying on one |
| Q4 2026 (planned) | Delegated act specifying presumption of conformity via the EUCC Common Criteria certification scheme (Commission implementation roadmap) |
| 11 Dec 2026 | Commission milestone: notification of sufficient conformity assessment bodies across Member States |
| 30 Oct 2027 (planned) | Further standardisation deliverables (Commission implementation roadmap) |
| 11 Dec 2027 | **Full application**; RED cybersecurity delegated act repealed; OSS steward reporting begins (Art. 24(3) read with Art. 71(2)); products placed on the market earlier are caught only on substantial modification |
| 11 Jun 2028 | Latest validity of pre-existing EU type-examination certificates for cybersecurity under other harmonisation law (Art. 69(1)) |
| 11 Sep 2028 / 11 Dec 2030 | Commission report on the reporting platform / first four-yearly evaluation (Art. 70) |

Pending or evolving as of September 2026: harmonised standards under M/606 (none yet cited in the OJ), the Art. 8(1) delegated act mandating certification for critical products, the Art. 27(9) delegated act listing usable certification schemes, any Art. 13(24) SBOM-format or Art. 14(10) notification-format implementing act, the Art. 33(5) simplified technical documentation form for micro and small enterprises, and the Digital Omnibus. Verify each before quoting it as law.

## Key obligations for security/GRC teams

1. **Classify every product and component** against Art. 2, Annex III/IV and Implementing Regulation 2025/2392; decide whether you are manufacturer, deemed manufacturer, importer, distributor or steward for each SKU, and whether remote data processing pulls backend services in. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Stand up the Art. 14 reporting process now** — it already applies to products already on the market: register Assigned Representatives on ENISA's platform, define "aware" in the incident playbook, pre-map the coordinator CSIRT, and rehearse the 24 h / 72 h / 14 day / 1 month cadence alongside GDPR and NIS2 clocks. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md), [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
3. **Build the product cybersecurity risk assessment** (Art. 13(2)–(3)) as a living artefact tied to Annex I Part I(2) applicability decisions; reuse the enterprise method in [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md) and [../risk-scoring.md](../risk-scoring.md).
4. **Operationalise Annex I Part II**: SBOM generation in a machine-readable format for every release, a published CVD policy and reporting contact, separated security updates, and a disclosure process for fixed vulnerabilities. Map to existing secure-SDLC controls with [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md) (for example ISO/IEC 27001:2022 Annex A 8.28 secure coding and the neighbouring secure-development controls).
5. **Set and publish support periods** per product with the Art. 13(8) reasoning documented, an update-retention plan of at least 10 years, and end-of-support dates surfaced at point of sale; own the end-of-life communications and the Art. 13(23) cessation duty.
6. **Component and supplier due diligence** (Art. 13(5)): contract for upstream vulnerability notification, SBOM delivery and support-period commitments; treat open-source dependencies as suppliers. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../workflows/vendor-onboarding.md](../../workflows/vendor-onboarding.md).
7. **Choose the conformity route early** — class II and critical products need a notified body, and notified-body capacity is a 2026–2027 bottleneck; track harmonised-standard publication because it changes whether class I can self-assess. Prepare Annex VII documentation with [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md) and the [../../templates/audit-evidence-request-list.md](../../templates/audit-evidence-request-list.md).
8. **Run the impact assessment and horizon scan** for the delegated acts, standards and the Digital Omnibus: [../../workflows/new-regulation-impact-assessment.md](../../workflows/new-regulation-impact-assessment.md) and [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).
9. **Board reporting**: CRA exposure is product-revenue exposure; report classification coverage, reporting-readiness test results, SBOM coverage and support-period commitments through [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **NIS2** ([nis2.md](nis2.md)): the CRA borrows NIS2's definitions of incident and near miss (Art. 3(43),(45)), uses NIS2's CSIRTs and CVD framework (NIS2 Art. 12) for reporting, and lets critical-product designation turn on essential entities' dependency (Art. 8). Operators subject to NIS2 supply-chain duties will increasingly demand CRA declarations of conformity, SBOMs and support-period commitments from vendors; a company can be both a NIS2 entity and a CRA manufacturer with separate reporting clocks and recipients.
- **GDPR** ([gdpr.md](gdpr.md)): Annex I embeds data minimisation, encryption and secure deletion; data protection authorities may access CRA documentation (Art. 52(7)). An exploited vulnerability that leads to a personal-data breach triggers a parallel Art. 33 GDPR notification within 72 hours to a different regulator.
- **EU AI Act** ([eu-ai-act.md](eu-ai-act.md)): Art. 12 CRA deems Annex I compliance to satisfy AI Act Art. 15 cybersecurity for high-risk AI products; AI Act market surveillance authorities lead for those products (Art. 52(14)). See [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).
- **DORA** ([dora.md](dora.md)): financial entities are users, not manufacturers, but DORA Art. 30 contract clauses and register-of-information entries are the natural place to capture supplier CRA conformity and support periods; the Digital Omnibus single-entry point is intended to join DORA, NIS2 and GDPR reporting, not CRA product reporting, in its first stage.
- **Cybersecurity Act (EU) 2019/881**: EUCC certificates at level "substantial" give presumption of conformity and can replace notified-body assessment (Art. 27(8)–(9)); a delegated act is expected to formalise the EUCC link.
- **Radio Equipment Directive**: Delegated Regulation 2022/30 remains the applicable cybersecurity rule for in-scope radio equipment until 11 December 2027, when it is repealed and the CRA takes over; manufacturers should plan one transition, not two.
- **General Product Safety Regulation (EU) 2023/988** applies to non-cyber risks of the same products (Art. 11); the Machinery Regulation, Product Liability Directive and toy safety rules are cross-referenced in the text.
- **Frameworks**: Annex I maps well to ISO/IEC 27001 Annex A secure-development controls ([../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md)), NIST CSF 2.0 Protect/Detect/Respond outcomes ([../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md)) and CIS Control 16 ([../frameworks/cis-controls-v8.md](../frameworks/cis-controls-v8.md)), but none of these gives presumption of conformity — only OJ-cited harmonised standards, common specifications or EU certification do. See [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).

## Primary sources

- Regulation (EU) 2024/2847 (Cyber Resilience Act), official text via the Publications Office / EUR-Lex, CELEX 32024R2847 — legal text: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- Commission Implementing Regulation (EU) 2025/2392 — technical descriptions of important and critical product categories, CELEX 32025R2392 — legal text: https://eur-lex.europa.eu/eli/reg_impl/2025/2392/oj
- Commission Delegated Regulation (EU) 2026/881 — cybersecurity-related grounds for delaying dissemination of notifications, CELEX 32026R0881 — legal text: https://eur-lex.europa.eu/eli/reg_del/2026/881/oj
- Commission Delegated Regulation (EU) 2026/339 — repeal of RED Delegated Regulation (EU) 2022/30 from 11 December 2027, CELEX 32026R0339 — legal text: https://eur-lex.europa.eu/eli/reg_del/2026/339/oj
- European Commission, Cyber Resilience Act policy, implementation roadmap, reporting, conformity assessment, open-source and standardisation pages — regulator guidance: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act ; https://digital-strategy.ec.europa.eu/en/factpages/cyber-resilience-act-implementation ; https://digital-strategy.ec.europa.eu/en/policies/cra-reporting ; https://digital-strategy.ec.europa.eu/en/policies/cra-conformity-assessment ; https://digital-strategy.ec.europa.eu/en/policies/cra-open-source ; https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation
- European Commission, library entry for the 27 July 2026 CRA guidance, with downloads of Communication C(2026) 5252 and its annex — regulator guidance: https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation (the guidance document itself was not fetched for this pack; the page's own summary is the basis for the description above)
- European Commission, Digital Package / Digital Omnibus questions and answers (single-entry point for incident reporting; page last updated 20 November 2025, so it evidences the proposal, not its current legislative status) — regulator guidance: https://digital-strategy.ec.europa.eu/en/faqs/digital-package
- ENISA, Single Reporting Platform page and 11 September 2026 launch press release — regulator guidance: https://www.enisa.europa.eu/topics/product-security-and-certification/single-reporting-platform-srp ; https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched
- CEN-CENELEC, acceptance of standardisation request M/606 (newsletter, 1 May 2025) — publisher page: https://www.cencenelec.eu/news-events/news/2025/newsletter/ots-62-cra/
- European Commission, harmonised standards index (no Cyber Resilience Act entry listed as of September 2026, the basis for the statement that no CRA harmonised standard is yet cited in the OJ) — publisher page: https://single-market-economy.ec.europa.eu/single-market/european-standards/harmonised-standards_en

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
