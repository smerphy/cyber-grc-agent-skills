# NIS2 Directive (EU 2022/2555)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Directive (EU) 2022/2555 — requires national transposition; obligations bind via member-state law |
| Replaces | NIS Directive (EU) 2016/1148 ("NIS1") |
| Entered into force | 16 January 2023 |
| Transposition deadline | 17 October 2024 (several member states missed it — always check local implementing law) |
| Who is covered | "Essential" and "important" entities in Annex I and Annex II sectors, generally medium-sized or larger |
| Core obligations | Risk-management measures (Art. 21), incident reporting (Art. 23), management accountability and training (Art. 20), registration |
| Reporting deadlines | Early warning ≤24h, incident notification ≤72h, final report ≤1 month (significant incidents) |
| Maximum fines | Essential: ≥ €10M or 2% of worldwide annual turnover; Important: ≥ €7M or 1.4% (whichever is higher) |
| Supervisors | National competent authorities and CSIRTs per member state; ENISA at EU level |

## What it is

NIS2 is the EU's horizontal cybersecurity law for critical and important sectors. It is a **directive**, not a regulation: each member state transposes it into national law, and the national statute — not the directive text — is what an entity must comply with. Transposition has been uneven; national laws differ in registration mechanics, incident-reporting portals, sector interpretations, and penalty regimes. **Treat the directive as the baseline and always verify the implementing law of each member state where the entity operates.**

Compared with NIS1, NIS2 broadens sector scope substantially, replaces the operator-of-essential-services designation model with a self-identifying size-cap rule, hardens incident-reporting deadlines, adds explicit management-body liability, and sets minimum fine ceilings.

## Scope: essential vs important entities

Two classes of covered entity, with the same substantive security obligations but different supervision intensity and fine ceilings.

### Annex I — sectors of high criticality

- Energy (electricity, district heating/cooling, oil, gas, hydrogen)
- Transport (air, rail, water, road)
- Banking
- Financial market infrastructure
- Health (healthcare providers, EU reference labs, pharma, medical-device manufacture critical during public-health emergencies)
- Drinking water
- Waste water
- Digital infrastructure (IXPs, DNS service providers, TLD registries, cloud computing, data centres, CDNs, trust service providers, public electronic communications networks/services)
- ICT service management (B2B managed service providers and managed security service providers)
- Public administration (central and, at member-state discretion, regional level)
- Space

### Annex II — other critical sectors

- Postal and courier services
- Waste management
- Manufacture, production and distribution of chemicals
- Food production, processing and distribution
- Manufacturing (medical devices; computer, electronic and optical products; electrical equipment; machinery; motor vehicles, trailers and semi-trailers; other transport equipment)
- Digital providers (online marketplaces, online search engines, social networking platforms)
- Research organisations

### Size-cap rule and its exceptions

Default rule: an entity in an Annex I or II sector is in scope if it is at least **medium-sized** under EU SME definitions (≥50 employees or annual turnover/balance sheet > €10M). Large entities (≥250 employees or turnover > €50M / balance sheet > €43M) in Annex I sectors are generally **essential**; other in-scope entities are generally **important**.

Entities in scope **regardless of size** include:

- Providers of public electronic communications networks or publicly available electronic communications services
- Qualified trust service providers, TLD name registries, and DNS service providers
- Sole providers in a member state of a service essential to critical societal or economic activities
- Entities whose disruption could significantly impact public safety, security, or health, or create systemic risk
- Entities identified as critical under the Critical Entities Resilience (CER) Directive (EU) 2022/2557
- Certain public administration entities

Classification is largely self-assessed against national criteria, and entities must register with national authorities. Member states maintain entity lists; some national laws add sectors or lower thresholds.

## Cybersecurity risk-management measures (Art. 21)

Entities must take "appropriate and proportionate technical, operational and organisational measures," based on an all-hazards approach, proportionate to risk exposure, entity size, and the likelihood and severity of incidents. Art. 21(2) lists **ten minimum measures**:

1. Policies on risk analysis and information system security
2. Incident handling
3. Business continuity — backup management, disaster recovery, and crisis management
4. Supply chain security, including security aspects of relationships with direct suppliers and service providers
5. Security in network and information systems acquisition, development and maintenance, including vulnerability handling and disclosure
6. Policies and procedures to assess the effectiveness of the risk-management measures
7. Basic cyber hygiene practices and cybersecurity training
8. Policies and procedures on the use of cryptography and, where appropriate, encryption
9. Human resources security, access control policies, and asset management
10. Multi-factor or continuous authentication solutions, secured voice/video/text communications, and secured emergency communication systems where appropriate

These map cleanly onto mainstream control frameworks — see [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md). An ISO 27001 ISMS or a CIS v8 program covers most of the list but rarely all of it explicitly (items 4, 6, and 10 are the common gaps). Commission Implementing Regulation (EU) 2024/2690 specifies detailed technical requirements and significant-incident thresholds for digital-infrastructure-type entities (DNS, TLD, cloud, data centre, CDN, managed (security) service providers, marketplaces, search engines, social networks, trust services).

## Incident reporting (Art. 23)

Obligation attaches to **significant incidents**: an incident that (a) has caused or is capable of causing severe operational disruption of services or financial loss for the entity, or (b) has affected or is capable of affecting other natural or legal persons by causing considerable material or non-material damage.

Multi-stage reporting to the CSIRT or competent authority (per national law):

| Stage | Deadline | Content |
|---|---|---|
| Early warning | ≤ 24 hours of becoming aware | Whether suspected to be unlawful/malicious; whether cross-border impact is possible |
| Incident notification | ≤ 72 hours of becoming aware | Update of early warning; initial assessment of severity and impact; indicators of compromise where available |
| Intermediate report | On authority request | Status updates |
| Final report | ≤ 1 month after the incident notification | Detailed description, severity and impact, root cause (likely), mitigation applied, cross-border impact |
| Progress + final report | If incident ongoing at 1 month | Progress report at 1 month; final report within 1 month of incident handling concluding |

Entities must also notify recipients of their services of significant incidents likely to adversely affect service delivery, and, where relevant, of significant cyber threats and available remedies. National portals and forms differ — pre-map them per jurisdiction. See [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) for the cross-regime deadline matrix and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) for the operational workflow.

## Management accountability and training (Art. 20)

- Management bodies must **approve** the Art. 21 risk-management measures and **oversee** their implementation.
- Management bodies **can be held liable** for infringements, per national law.
- Members of management bodies must **undergo cybersecurity training**, and entities are required to offer similar training to employees on a regular basis.
- For essential entities, national enforcement can extend to a **temporary ban on individuals exercising managerial functions** (CEO or legal-representative level) for persistent non-compliance.

This is the strongest general-purpose lever for board engagement in EU cyber law; use it explicitly in board reporting — see [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).

## Supervision and enforcement

| | Essential entities | Important entities |
|---|---|---|
| Supervision model | **Proactive (ex ante) and reactive** — regular and targeted audits, on-site inspections, security scans, information requests, evidence of implementation | **Reactive (ex post) only** — triggered by evidence or indication of non-compliance |
| Enforcement tools | Warnings, binding instructions, orders to remediate and to inform affected recipients, compliance deadlines | Same core toolkit, applied after the fact |
| Escalation (essential only) | Temporary suspension of certification/authorisation for services; temporary ban on managerial functions | — |
| Fine ceiling | ≥ €10,000,000 or 2% of total worldwide annual turnover, whichever is higher | ≥ €7,000,000 or 1.4% of total worldwide annual turnover, whichever is higher |

Fine ceilings are minimums that national laws must provide; member states may set higher amounts. Jurisdiction generally follows main establishment; certain digital infrastructure and digital-provider entities fall under a main-establishment mechanism with ENISA registration.

## Key obligations for security/GRC teams

1. **Determine applicability and classification** per member state: sector match against Annex I/II, size-cap test, size-cap exceptions, national additions. Document the analysis — see [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Register** with the national authority in each relevant member state; track differing national deadlines and portals.
3. **Gap-assess against the ten Art. 21 measures** using existing framework evidence (ISO 27001, CIS v8, NIST CSF 2.0); close the common gaps: supply-chain security, effectiveness-assessment procedures, MFA/secured-communications coverage. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).
4. **Build the 24h/72h/1-month reporting machinery**: significant-incident criteria wired into incident severity classification, pre-drafted report templates per national portal, on-call decision authority for the 24-hour early warning.
5. **Stand up management-body governance**: board approval of the measure set, recurring board training with attendance records, documented oversight cadence.
6. **Extend third-party risk management** to direct suppliers and service providers with security requirements in contracts — see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
7. **Prepare for supervision**: essential entities should maintain audit-ready evidence continuously (see [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md)); important entities still need the same evidence, just without scheduled inspections.

## Interplay

- **DORA (lex specialis):** financial entities covered by DORA apply DORA's ICT risk-management and incident-reporting provisions instead of the corresponding NIS2 provisions. Banking and financial market infrastructure appear in NIS2 Annex I largely for completeness; in practice DORA governs. See [dora.md](dora.md).
- **GDPR:** one incident can trigger both regimes — NIS2 reporting to the CSIRT/competent authority (24h/72h/1 month) and a GDPR Art. 33 personal-data-breach notification to the supervisory authority (72 hours), plus Art. 34 data-subject communication. Different recipients, thresholds, and content; run them in parallel, not as one filing. Where a GDPR fine is imposed for the same conduct, NIS2 administrative fines for the same infringement are constrained. See [gdpr.md](gdpr.md).
- **CER Directive (EU) 2022/2557:** entities designated critical under CER are automatically essential entities under NIS2, and gain physical-resilience obligations on top.
- **Sector rules:** sector-specific EU acts with at-least-equivalent security and reporting requirements displace NIS2 for those matters (the DORA situation generalized).
- **EU AI Act:** no direct overlap in reporting, but Art. 21 supply-chain and secure-development measures extend to AI systems an entity operates; see [eu-ai-act.md](eu-ai-act.md).

## Primary sources

- [Directive (EU) 2022/2555 (NIS2) — official text on EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)
- [ENISA (implementing guidance, technical standards support)](https://www.enisa.europa.eu)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
