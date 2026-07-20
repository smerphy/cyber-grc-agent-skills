# EU Cyber Resilience Act (Regulation (EU) 2024/2847)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Regulation (EU) 2024/2847 — directly applicable in all member states, no national transposition |
| Regulates | "Products with digital elements" (PDEs) placed on the EU market — hardware and software, including their remote data processing solutions |
| Entered into force | 10 December 2024 |
| Applicability | Staged: conformity-assessment-body provisions from 11 June 2026; vulnerability/incident reporting obligations (Art. 14) from 11 September 2026; main obligations from 11 December 2027 (verify exact dates against the official text) |
| Who is covered | Manufacturers, importers, and distributors of PDEs made available in the EU, wherever established; light-touch regime for open-source software stewards |
| Core obligations | Annex I essential cybersecurity requirements (secure by design/default, vulnerability handling), conformity assessment + CE marking, support period with security updates, reporting of actively exploited vulnerabilities and severe incidents |
| Reporting deadlines | Early warning ≤24h, notification ≤72h, final report (14 days for vulnerabilities / 1 month for incidents) — via ENISA's single reporting platform to the CSIRT designated as coordinator |
| Maximum fines | Up to €15M or 2.5% of worldwide annual turnover for breaches of essential requirements; lower tiers (€10M/2%, €5M/1%) for other infringements (verify against Art. 64) |
| Supervisors | National market surveillance authorities; ENISA and the Commission at EU level; ADCO group for coordination |

## What it is

The CRA is the EU's horizontal product-security law. Where NIS2 regulates the security of *organizations* delivering services, the CRA regulates the security of *products* — any software or hardware with a digital component placed on the EU market, from IoT devices and operating systems to standalone commercial software. It is a **regulation**, so it applies directly and uniformly; there are no national implementing laws to track. Compliance follows the New Legislative Framework model familiar from other CE-marked product law: essential requirements, conformity assessment, technical documentation, EU declaration of conformity, CE marking, and market surveillance.

Practical consequence: any software vendor selling into the EU becomes a regulated *manufacturer* with product-lifecycle security duties, regardless of where it is headquartered.

## Scope

**In scope:** products with digital elements whose intended or reasonably foreseeable use includes a direct or indirect logical or physical data connection to a device or network — hardware products, embedded software, and standalone software, plus "remote data processing solutions" without which the product could not perform its functions (e.g., a companion cloud backend for a device).

**Out of scope (covered by sector law or excluded):**

- Medical devices under the MDR/IVDR
- Motor vehicles under the type-approval regime, civil aviation, and marine equipment
- Products developed exclusively for national security/defence purposes
- SaaS as such — cloud services are NIS2 territory, *unless* they qualify as remote data processing solutions integral to a product
- Free and open-source software supplied **outside the course of a commercial activity** (monetized or commercially supported open source is in scope; see the steward regime below)

Spare parts and products already covered by equivalent sectoral rules have carve-outs — verify edge cases against the official text.

## Product classes and conformity assessment

Risk-tiered classification drives the conformity-assessment route:

| Class | Examples (indicative) | Assessment route |
|---|---|---|
| Default (unclassified) — the large majority of products | Most applications, standard software, ordinary connected devices | Self-assessment (internal control) against Annex I |
| Important — Class I (Annex III) | Identity management, browsers, password managers, VPNs, malware detection, smart home security devices, network management | Self-assessment **only if** harmonised standards/common specifications are applied in full; otherwise third-party assessment |
| Important — Class II (Annex III) | Hypervisors and container runtimes, firewalls/IDS/IPS, tamper-resistant microcontrollers | Third-party conformity assessment by a notified body |
| Critical (Annex IV) | Hardware devices with security boxes, smart meter gateways, smartcards/secure elements | Third-party assessment; the Commission may mandate European cybersecurity certification (EUCC-type schemes) |

Exact Annex III/IV category lists and module choices (Module A internal control, Module B+C EU-type examination, Module H full quality assurance) should be verified against the official text — the Commission can amend the class lists by delegated act. Products bearing an EU cybersecurity certificate at assurance level "substantial" or higher benefit from a presumption of conformity for covered requirements, as do products conforming to harmonised standards once those are published (standardisation work was still maturing as of mid-2026 — track it, since it determines whether Class I products can stay on the self-assessment route).

## Essential cybersecurity requirements (Annex I)

**Part I — product properties.** Products must be designed, developed, and produced to ensure an appropriate level of cybersecurity based on a documented risk assessment, and must be delivered:

- Without known exploitable vulnerabilities
- With a **secure-by-default configuration**, including the ability to reset to that state
- With protection against unauthorised access (authentication and identity management), and reporting of unauthorised access attempts where appropriate
- With confidentiality (encryption of relevant data at rest and in transit) and integrity protection for data, commands, and configuration
- Processing only data that is adequate, relevant, and limited to what is necessary (data minimisation)
- With availability protection for essential functions, including resilience to DoS, and minimisation of the product's own negative impact on other services
- With reduced attack surface, exploitation-mitigation mechanisms, and security-relevant logging/monitoring (with opt-out where appropriate)
- With the ability to receive **security updates**, including automatic updates with user opt-out as the default posture for consumer-relevant products, and the ability to securely remove user data

**Part II — vulnerability handling.** For the duration of the support period, manufacturers must:

- Identify and document vulnerabilities and components, including maintaining a **software bill of materials (SBOM)** in a machine-readable format covering at least top-level dependencies (SBOM is documentation for authorities, not a mandatory public artefact — verify current implementing detail)
- Remediate vulnerabilities without delay, providing **security updates free of charge**, separate from feature updates where technically feasible, with advisory information
- Apply regular security testing and reviews
- Publish a **coordinated vulnerability disclosure policy** and provide a contact address for reporting; take measures to facilitate sharing of vulnerability information
- Publicly disclose fixed vulnerabilities (with a delay allowance where users need time to patch)

## Manufacturer, importer, and distributor duties

**Manufacturers** carry the primary obligations: risk assessment as part of planning/design/development, due diligence on third-party components (including open-source components integrated into the product), technical documentation (Annex VII), conformity assessment, EU declaration of conformity, CE marking, user information and instructions (Annex II), and the Part II vulnerability-handling processes across the support period.

**Support period:** the manufacturer determines it based on expected product lifetime, but it must be **at least 5 years** unless the product is expected to be in use for a shorter time. The end date must be stated at the time of purchase. Security updates must remain available for at least 10 years after issuance or for the remainder of the support period, whichever is longer (verify the exact formulation).

**Importers** must verify that the manufacturer has carried out conformity assessment, that documentation and CE marking are in place, and must not place non-conforming products on the market; they inform the manufacturer and authorities of vulnerabilities and non-conformity they become aware of.

**Distributors** verify CE marking and documentation presence and act with due care; they escalate known non-conformity and vulnerabilities.

Anyone who substantially modifies a product or markets it under their own name becomes the manufacturer for CRA purposes.

## Open-source stewards

The CRA creates a distinct, light-touch category for **open-source software stewards** — legal persons (foundations, non-profits) that systematically support the development of open-source products intended for commercial activities but do not themselves monetise them. Stewards must put in place a cybersecurity policy for the product's development and vulnerability handling, cooperate with market surveillance authorities, and participate in reporting of actively exploited vulnerabilities and severe incidents to the extent they are involved. Stewards are not subject to the full manufacturer regime, and the administrative-fine provisions are attenuated for them (verify the exact enforcement treatment against Arts. 24 and 64). Individual unpaid open-source developers contributing outside a commercial activity are not in scope.

Manufacturers who integrate open-source components remain fully responsible for the product and owe due diligence on those components — and are expected to report vulnerabilities they find in open-source components back upstream.

## Reporting obligations (Art. 14) — applicable from 11 September 2026

Manufacturers must report two things, on NIS2-style clocks, via the **single reporting platform** operated by ENISA, addressed to the CSIRT designated as coordinator of the member state and to ENISA:

| Trigger | Early warning | Notification | Final report |
|---|---|---|---|
| **Actively exploited vulnerability** in the product | ≤ 24 hours of awareness | ≤ 72 hours — general information, nature of exploit, corrective/mitigating measures | ≤ 14 days after a corrective measure is available — description, severity/impact, fix |
| **Severe incident** having an impact on the security of the product | ≤ 24 hours of awareness (including whether unlawful/malicious is suspected) | ≤ 72 hours — initial assessment, mitigations, indicators | ≤ 1 month after the notification — detailed description, root cause, mitigation, cross-border impact where relevant |

Manufacturers must also inform **impacted users** of the vulnerability or incident and of corrective measures, without undue delay. These clocks run in parallel with, and independently of, any NIS2 or GDPR reporting duty the same event triggers in the manufacturer's own operations — see [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).

## Enforcement and penalties

Market surveillance authorities can require corrective action, restrict or prohibit products, and order recalls or withdrawals. Administrative-fine ceilings (verify against Art. 64):

- Up to **€15,000,000 or 2.5%** of total worldwide annual turnover, whichever is higher — non-compliance with Annex I essential requirements or the core manufacturer obligations (Arts. 13–14)
- Up to €10,000,000 or 2% — other obligations under the regulation
- Up to €5,000,000 or 1% — supplying incorrect, incomplete, or misleading information to notified bodies and authorities

## Key obligations for security/GRC teams

What a software or device vendor's GRC team should be doing now (mid-2026):

1. **Build the product inventory and scope determination.** Enumerate every product with digital elements sold into the EU, including embedded software and companion cloud services that qualify as remote data processing solutions. Classify each against Annex III/IV — see [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Stand up the Art. 14 reporting machinery first** — it goes live 11 September 2026, more than a year before the main obligations. Wire "actively exploited vulnerability in our product" and "severe incident impacting product security" into incident and PSIRT triage criteria, with a 24-hour decision path and pre-drafted templates for the ENISA platform.
3. **Gap-assess the SDLC against Annex I.** Secure-by-default configurations, update mechanisms, logging, attack-surface reduction, and exploit mitigations are engineering work with long lead times; start against the December 2027 deadline now. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).
4. **Operationalise vulnerability handling as a compliance process:** SBOM generation in the build pipeline, a published coordinated vulnerability disclosure policy, free security updates separated from feature releases, and a defined, published support period per product.
5. **Prepare conformity-assessment evidence:** product risk assessments, Annex VII technical documentation, and the EU declaration of conformity. For Class I products, track harmonised-standard publication — it decides whether you keep the self-assessment route. For Class II/critical products, engage a notified body early; capacity will be constrained.
6. **Extend third-party and open-source component due diligence** — component vulnerability monitoring, upstream reporting, and contractual security requirements on suppliers of integrated components. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
7. **Update customer-facing artefacts:** Annex II user information, support-period end dates at point of sale, and sales/legal awareness that CE marking now covers cybersecurity.

## Interplay

- **NIS2:** complementary, not overlapping — NIS2 secures the entity's services and operations ([./nis2.md](./nis2.md)); the CRA secures the products it ships. One security incident at a software vendor can trigger both: NIS2 reporting for the vendor's own service disruption and CRA reporting if the incident impacts product security. NIS2 entities buying software also gain leverage: CRA conformity becomes a natural supply-chain-security criterion under NIS2 Art. 21(2)(d).
- **GDPR:** Annex I's data-minimisation, confidentiality, and secure-erasure requirements overlap with data-protection-by-design (Art. 25 GDPR). An exploited vulnerability leading to a personal data breach triggers GDPR Art. 33 (72h) in parallel with CRA Art. 14. See [./gdpr.md](./gdpr.md).
- **EU AI Act:** high-risk AI systems that are also PDEs and meet the CRA's essential requirements gain a presumption of conformity with the AI Act's cybersecurity requirement (Art. 15 AI Act); conformity assessments can be coordinated. See [./eu-ai-act.md](./eu-ai-act.md).
- **DORA:** financial entities procuring ICT products can use CRA conformity as evidence within DORA's ICT third-party risk framework; the regimes do not displace each other. See [./dora.md](./dora.md).
- **RED delegated act:** the radio-equipment cybersecurity requirements (applicable from 2025) act as a bridge until the CRA fully applies; CRA compliance is expected to subsume them for covered products — verify transition mechanics.

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
