# EU Critical Entities Resilience Directive (CER Directive, Directive (EU) 2022/2557)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Directive (EU) 2022/2557 of 14 December 2022 on the resilience of critical entities, OJ L 333, 27.12.2022, p. 164 — a directive, so obligations bind through national transposing law, not the EU text itself |
| Repeals | Council Directive 2008/114/EC (European Critical Infrastructure Directive, energy and transport only), repealed with effect from 18 October 2024 (Art. 27) |
| Regulators | National competent authorities and a single point of contact per Member State (Art. 9); Commission-chaired Critical Entities Resilience Group (CERG, Art. 19); European Commission (DG Migration and Home Affairs) for guidelines, advisory missions and infringement action |
| Key dates | Entry into force 16 January 2023; transposition and application 17 October / 18 October 2024 (Art. 26); national strategy and Member State risk assessment by 17 January 2026 (Arts. 4–5); identification of critical entities by 17 July 2026 (Art. 6(1)); Chapter III obligations apply 10 months after an entity is notified (Art. 6(3)) |
| Who is covered | Public or private entities in the 11 sectors of the Annex that a Member State *identifies* as critical (Art. 2(1), Art. 6) — a designation model, not self-identification |
| Scope of hazards | All-hazards: natural and man-made, accidental or intentional, including hybrid and terrorist threats (Arts. 5(1), 12(2)); cyber matters are carved out to NIS2 (Art. 1(2)) |
| Core obligations | Entity risk assessment (Art. 12), technical/security/organisational resilience measures and a resilience plan (Art. 13), background checks (Art. 14), incident notification (Art. 15), liaison officer (Art. 13(3)) |
| Incident clock | Initial notification ≤ 24 hours after becoming aware; detailed report ≤ 1 month thereafter, where relevant (Art. 15(1)) |
| Penalties | Set by each Member State; must be "effective, proportionate and dissuasive" (Art. 22) — no EU-level fine ceiling, unlike NIS2 |
| Relationship to neighbours | Twin of NIS2 (physical resilience vs cybersecurity); CER critical entities are automatically NIS2 essential entities; banking, financial market infrastructure and digital infrastructure entities are identified but exempt from Chapters III, IV and VI (Art. 8) because DORA/NIS2 already cover them |

## What it is

The CER Directive is the EU's horizontal law on the physical and operational resilience of the organisations that provide essential services. It replaces the 2008 European Critical Infrastructure Directive, which the Commission's 2019 evaluation found too narrow (energy and transport only, asset-protection focus) for an interconnected, cross-border economy (recital 2). CER shifts the object of regulation from *infrastructure* to *entities*, expands coverage to 11 sectors, and requires every Member State to run a strategy → national risk assessment → identification → supervision cycle, while identified entities must assess their own risks and take resilience measures.

It was adopted in the same package as NIS2 and DORA (all three dated 14 December 2022, all published in OJ L 333). Art. 1(2) draws the boundary: CER does not apply to matters covered by NIS2, and the two directives must be implemented "in a coordinated manner". In practice CER is the non-cyber, all-hazards counterpart: sabotage, terrorism, natural disasters, public-health emergencies, supply-chain failure and insider risk, with cybersecurity handled under NIS2 by the same or cooperating authorities.

CER is minimum harmonisation (Art. 3): Member States may impose stricter national rules. The directive is short on prescriptive detail; the operational specifics live in national transposing acts, the Commission's non-binding guidelines (2025 on identification, 2026 on resilience measures) and future implementing acts under Arts. 13(6) and 18(6).

## Who it covers / Scope

An organisation is in scope only once a Member State identifies it as a critical entity. Identification (Art. 6(2)) requires all three criteria:

| Criterion | Test |
|---|---|
| (a) Essential service | The entity provides one or more essential services — services "crucial for the maintenance of vital societal functions, economic activities, public health and safety, or the environment" (Art. 2(5)), drawn from the non-exhaustive list in Delegated Regulation (EU) 2023/2450, which Member States may extend nationally (Art. 7(2)(a)) |
| (b) Territorial nexus | The entity operates, and its critical infrastructure is located, on the territory of that Member State |
| (c) Significant disruptive effect | An incident would have significant disruptive effects on that service or on dependent services in other Annex sectors, judged against the Art. 7(1) criteria: number of users; cross-sector dependency; degree and duration of impact on economic and societal activities, environment, public safety or health; market share; geographic area including cross-border impact and isolation (islands, remote, mountainous areas); availability of alternatives |

Member States must also apply the outcomes of their national risk assessment and strategy, and may set thresholds for the Art. 7(1) criteria, which they report to the Commission (Art. 7(2)(c)). The Commission's September 2025 guidelines (C(2025) 6094) restate the three criteria as cumulative and set out five steps to consider — sector/category, essential service, territory, significant disruptive effect, exclusions — which Member States may take in any order, with practical guidance per criterion.

### Annex sectors, subsectors and categories of entity

| # | Sector | Subsectors / categories (summarised) |
|---|---|---|
| 1 | Energy | Electricity (suppliers, DSOs, TSOs, producers, NEMOs, aggregation/demand-response/storage market participants); district heating and cooling; oil (pipelines, production/refining/storage, central stockholding entities); gas (supply, DSOs, TSOs, storage, LNG, natural gas undertakings, refining/treatment); hydrogen (production, storage, transmission) |
| 2 | Transport | Air (commercial air carriers, airport managing bodies and airports incl. TEN-T core airports, ATC providers); rail (infrastructure managers, railway undertakings, service-facility operators); water (passenger/freight water transport companies, port managing bodies and facilities, VTS operators); road (traffic-management road authorities, ITS operators); public transport (public service operators) |
| 3 | Banking | Credit institutions (CRR Art. 4(1)) |
| 4 | Financial market infrastructure | Operators of trading venues; central counterparties |
| 5 | Health | Healthcare providers; EU reference laboratories; medicinal-product R&D entities; manufacturers of basic pharmaceutical products and preparations (NACE C.21); manufacturers of devices on the public-health-emergency critical devices list; wholesale distribution authorisation holders |
| 6 | Drinking water | Suppliers and distributors of water intended for human consumption (excluding distributors for whom it is non-essential) |
| 7 | Waste water | Undertakings collecting, disposing of or treating urban, domestic or industrial waste water (excluding those for whom it is non-essential) |
| 8 | Digital infrastructure | IXPs; DNS service providers (excluding root name servers); TLD registries; cloud computing, data centre and CDN providers; trust service providers; public electronic communications networks and publicly available electronic communications services (definitions cross-referenced to NIS2 Art. 6, eIDAS and the EECC) |
| 9 | Public administration | Public administration entities of central governments as defined by national law (Art. 2(10) definition excludes judiciary, parliaments, central banks) |
| 10 | Space | Operators of ground-based infrastructure supporting space-based services (excluding public electronic communications network providers) |
| 11 | Production, processing and distribution of food | Food businesses (Reg. 178/2002 Art. 3(2)) engaged exclusively in logistics and wholesale distribution and large-scale industrial production and processing |

### Exclusions and carve-outs

- **Banking, financial market infrastructure, digital infrastructure (Annex points 3, 4, 8):** Member States identify these entities (so the strategy, risk-assessment and support chapters apply, and NIS2/DORA authorities learn who they are), but Art. 11 and Chapters III, IV and VI — the entity-level obligations, European-significance regime and supervision/penalties — do not apply (Art. 8, Art. 6(3)). Equivalence with DORA and NIS2 is the stated reason (recitals). Member States may keep or add stricter national rules.
- **Sector-specific equivalence (Art. 1(3)):** where sector-specific EU law imposes resilience measures recognised as at least equivalent, the corresponding CER provisions (including supervision and enforcement) do not apply.
- **National security (Art. 1(5)–(8)):** the directive does not apply to public administration entities active in national security, public security, defence or law enforcement; Member States may disapply Art. 11 and Chapters III, IV, VI for specific critical entities in those fields; no obligation to supply information contrary to essential security interests.
- **Extraterritorial reach:** none in the direct sense — identification requires operation and infrastructure on the Member State's territory. Cross-border exposure enters via Art. 11 consultations, the six-or-more-Member-States European-significance test (Art. 17) and dependency analysis in risk assessments (Art. 12(2), which expressly includes dependencies on entities in neighbouring Member States and third countries).
- **SMEs:** no size threshold or exemption; national strategies must describe measures to help SMEs identified as critical meet Chapter III (Art. 4(2)(h)).

## Core obligations

### Member State duties (Chapter II) — the pipeline that produces designations

| Art. | Duty | Deadline / cadence |
|---|---|---|
| 4 | National strategy on the resilience of critical entities, including a coordination framework with NIS2 authorities and SME support measures; communicated to the Commission within 3 months of adoption | By 17 January 2026; updated at least every 4 years |
| 5 | Member State risk assessment using the Delegated Regulation 2023/2450 list of essential services; all-hazards; accounts for cross-sector and cross-border dependencies and notified incidents; relevant elements shared with identified entities | By 17 January 2026; at least every 4 years; outcomes to Commission within 3 months |
| 6 | Identify critical entities; keep a list; notify each entity within 1 month of identification and tell it which obligations apply from when; notify NIS2 authorities within 1 month | By 17 July 2026; list reviewed at least every 4 years |
| 7(2) | Report to Commission: additional national essential services, number of entities per sector/subsector/service, thresholds applied | Without undue delay after identification; at least every 4 years |
| 9 | Designate competent authority(ies) and a single point of contact; publish their identity; biennial summary report on incident notifications received | First summary report by 17 July 2028, then every 2 years |
| 10–11 | Support critical entities (guidance, exercises, training, possible funding); facilitate voluntary information sharing; consult other Member States on cross-border entities | Ongoing |
| 22 | Lay down effective, proportionate and dissuasive penalties and notify them to the Commission | By 17 October 2024 |

### Critical entity duties (Chapter III) — apply from 10 months after the Art. 6(3) notification

| Art. | Obligation | What it requires |
|---|---|---|
| 12 | Critical entity risk assessment | Within 9 months of notification (a separate, earlier clock than the 10-month Chapter III start), then whenever necessary and at least every 4 years. All relevant natural and man-made risks, including cross-sectoral/cross-border, accidents, natural disasters, public-health emergencies, hybrid and antagonistic threats and terrorism. Must analyse dependencies in both directions (who depends on the entity; what the entity depends on, including in other Member States and third countries). Existing risk assessments under other laws may be reused; the authority may declare them compliant in whole or part |
| 13(1) | Resilience measures | "Appropriate and proportionate technical, security and organisational measures" covering six areas: (a) prevention, including disaster risk reduction and climate adaptation; (b) physical protection of premises and critical infrastructure (fencing, barriers, perimeter monitoring, detection, access control); (c) response, resistance and mitigation (risk and crisis management procedures, alert routines); (d) recovery (business continuity, alternative supply chains); (e) employee security management (critical-function roles, access rights, background-check procedures, training/qualifications — external service providers' personnel included); (f) awareness among relevant personnel (training, materials, exercises) |
| 13(2) | Resilience plan | A resilience plan "or equivalent document or documents" describing the Art. 13(1) measures; documents produced under other legal acts may be reused, and the authority may declare existing measures compliant |
| 13(3) | Liaison officer | A named liaison officer or equivalent as point of contact with the competent authority |
| 13(4) | Advisory missions (voluntary) | At the Member State's request and with the entity's agreement, the Commission organises an advisory mission on Chapter III compliance |
| 14 | Background checks | Member States set the conditions under which an entity may request checks on persons in sensitive roles, persons with direct or remote access to premises, information or control systems, and candidates for such positions. Checks must be proportionate, limited to evaluating security risk, and at minimum corroborate identity and check relevant criminal records; cross-border records via ECRIS (central authorities reply within 10 working days). GDPR and the Law Enforcement Directive apply |
| 15 | Incident notification | See below |
| 16 | Standards | Member States encourage use of European and international standards and technical specifications without mandating specific technology |

### Incident notification (Art. 15)

| Element | Rule |
|---|---|
| Trigger | Incidents that "significantly disrupt or have the potential to significantly disrupt" the provision of essential services; "incident" is any event with that potential (Art. 2(3)), not just security events |
| Significance parameters | Number and proportion of users affected; duration; geographical area affected, including whether it is isolated |
| Initial notification | Without undue delay and no later than 24 hours after becoming aware, unless operationally unable |
| Detailed report | Where relevant, no later than 1 month after the initial notification |
| Content | Any available information on nature, cause and possible consequences, including what is needed to judge cross-border impact; notification does not increase the entity's liability |
| Onward flow | Authority informs other affected Member States' single points of contact; where 6+ Member States are or may be significantly affected, authorities notify the Commission; authority gives the entity follow-up information; public may be informed in the public interest |

The Chapter III clock and the NIS2 clock differ: NIS2 requires an early warning within 24 hours *and* an incident notification within 72 hours before the one-month final report; CER has only the 24-hour initial notification and the one-month detailed report. A CER entity that is also a NIS2 entity may face both regimes for the same event (see Interplay and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md)).

### Critical entities of particular European significance (Chapter IV)

| Art. | Rule |
|---|---|
| 17 | An identified critical entity that provides the same or similar essential services to or in **six or more Member States** must inform its competent authority (services and Member States concerned); the Member State tells the Commission; after consultations the Commission notifies the entity of its status. Chapter IV applies from receipt of that notification |
| 18 | The Commission organises **advisory missions** (Member State, Commission and other-Member-State experts) to assess the entity's Chapter III measures — at the identifying Member State's request, or on Commission/other-Member-State initiative with that State's agreement. The entity must give access to information, systems and facilities. Findings reported within 3 months; the Commission issues an opinion the entity and its authority must take into account. Procedural rules come via an implementing act (Art. 18(6)) |

### Non-binding Commission guidelines (the practical detail layer)

| Document | Adopted | Content |
|---|---|---|
| Delegated Regulation (EU) 2023/2450 | 25 July 2023 (OJ L, 30.10.2023) — binding | Non-exhaustive list of essential services per Annex sector/subsector, used for national risk assessments and identification |
| Communication C(2025) 6094 — guidelines under Arts. 5(5), 6(6) and 7(3) | 11 September 2025 | Voluntary common template for reporting national risk-assessment outcomes; step-by-step identification methodology; guidance on each Art. 7(1) significance criterion (users, dependency, impact, market share, geography, alternatives) and thresholds |
| Communication C/2026/3712 — guidelines under Art. 13(5) | 10 July 2026 (OJ C, 13.7.2026) | Non-exhaustive catalogue of resilience-enhancing measures in seven domains (A general considerations, B prevention, C physical protection, D response/resistance/mitigation, E recovery, F employee security management, G awareness), mirroring Art. 13(1)(a)–(f); includes drone detection, mitigation and counter-drone cooperation measures, identified as a key action under the EU Action Plan on Drone and Counter-Drone Security (COM(2026) 81 final, 11 February 2026) |

## Enforcement and penalties

| Mechanism | Detail |
|---|---|
| Supervisory powers (Art. 21(1)) | On-site inspections of critical infrastructure and premises; off-site supervision of Art. 13 measures; conduct or order audits |
| Information and audit demands (Art. 21(2)) | For entities that are also NIS2 entities: require information needed to assess Art. 13 compliance and "evidence of the effective implementation of those measures, including the results of an audit conducted by an independent and qualified auditor selected by that entity and conducted at its expense" |
| Remediation orders (Art. 21(3)) | Orders to take necessary and proportionate measures within a set time limit and to report back; seriousness of the infringement taken into account |
| Safeguards (Art. 21(4)) | Objective, transparent, proportionate exercise; protection of trade secrets; right to be heard, right of defence, effective judicial remedy |
| NIS2 coordination (Art. 21(5)) | CER authorities inform NIS2 authorities of compliance assessments and may ask them to use their own supervisory and enforcement powers against a dual-regime entity |
| Penalties (Art. 22) | Purely national: "effective, proportionate and dissuasive"; no EU minimum or maximum fine. Amounts, personal liability of managers and criminal sanctions therefore vary by Member State and must be checked in each transposing act |
| Commission review (Art. 25) | Report on Member State compliance by 17 July 2027; first functioning review (including whether to amend the Annex) by 17 June 2029 |

Enforcement against Member States is separate: for non-transposition the Commission sent letters of formal notice in November 2024 and reasoned opinions in July 2025, and on 29 April 2026 referred Bulgaria, France, Luxembourg, the Netherlands, Poland, Spain and Sweden to the Court of Justice, asking the Court to impose financial sanctions on each of them (IP/26/910).

## Timeline and status

| Date | Event |
|---|---|
| 14 Dec 2022 | Adopted (same day as NIS2 and DORA); published OJ L 333 on 27 Dec 2022 |
| 16 Jan 2023 | Entry into force (Art. 28: 20th day after publication) |
| 25 Jul 2023 | Delegated Regulation (EU) 2023/2450 on essential services adopted (published 30 Oct 2023) |
| 25 Jun 2024 | Council Recommendation C/2024/4371 on a blueprint for coordinated EU response to cross-border critical-infrastructure disruptions (complements CER; not part of it) |
| 17 Oct 2024 | Transposition deadline; penalties to be notified (Art. 22) |
| 18 Oct 2024 | National measures apply; Directive 2008/114/EC repealed |
| Nov 2024 | Letters of formal notice to Member States that had not notified transposition |
| 17 Jan 2025 | First CERG biennial work programme due (Art. 19(4)); a 2025–2026 CERG work programme is published on the Commission's CER page |
| Jul 2025 | Reasoned opinions to remaining non-transposing Member States |
| 11 Sep 2025 | Commission guidelines on identification and risk-assessment reporting template, C(2025) 6094 |
| 17 Jan 2026 | Deadline for national strategies and Member State risk assessments |
| 29 Apr 2026 | Commission refers seven Member States (BG, FR, LU, NL, PL, ES, SE) to the CJEU with a request for financial sanctions |
| 10 Jul 2026 | Commission guidelines on resilience measures, C/2026/3712 (published OJ C 13 Jul 2026) |
| 17 Jul 2026 | Deadline for identifying critical entities; notifications to entities within 1 month; entity risk assessment due 9 months and Chapter III obligations 10 months after notification (so May–June 2027 for entities notified on time) |
| 17 Jan 2027 | Commission summary report to CERG on strategies and risk assessments (Art. 19(7)) |
| 17 Jul 2027 | Commission report on Member State compliance (Art. 25) |
| 17 Jul 2028 | First biennial single-point-of-contact summary reports on incident notifications (Art. 9(3)) |
| 17 Jun 2029 | First periodic review of the directive, including possible Annex changes (Art. 25) |

**Status as of September 2026.** The directive is in force and unamended: EUR-Lex holds no consolidated version and no corrigendum, and no amending proposal has been identified. Transposition is uneven — the Commission stated in April 2026 that "most Member States have notified complete transposition", while seven were referred to the Court of Justice. National laws differ on designation mechanics, penalty levels and incident-reporting portals: Germany's KRITIS-Dachgesetz of 11 March 2026 (BGBl. 2026 I Nr. 66), in force 17 March 2026 and already amended by the Act of 21 July 2026, works by operator self-registration with the federal civil-protection office rather than pure designation, and runs the 9-month and 10-month clocks from registration. No implementing act under Art. 13(6) (technical and methodological specifications for resilience measures) or Art. 18(6) (advisory-mission procedures) is listed on the Commission's CER page as of September 2026 — both remain pending (verify). Identification decisions were due 17 July 2026 and notifications within one month of identification, so the first wave of Chapter III obligations falls due around May–June 2027 for entities notified on time, later where Member States missed the deadline.

## Key obligations for security/GRC teams

1. **Determine designation status, not self-classification.** Track whether your entity has received (or expects) an Art. 6(3) notification in each Member State where it operates and record the notification date — it starts the 9-month (risk assessment) and 10-month (Chapter III) clocks. Map Annex categories to legal entities and sites. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Check for the Art. 8 carve-out.** Banks, trading venues, CCPs and digital-infrastructure providers are identified but owe no Chapter III/IV duties under CER — their equivalents sit in DORA and NIS2. Do not build a duplicate CER programme there; do confirm the NIS2 essential-entity consequence.
3. **Run an all-hazards entity risk assessment** within 9 months of notification and at least every 4 years, explicitly covering upstream and downstream dependencies (including third-country suppliers) and the Member State risk-assessment inputs. Reuse existing BCM, ISO 22301/27001 and Seveso-type assessments where the authority will accept them. See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md) and [../risk-scoring.md](../risk-scoring.md).
4. **Build or consolidate the resilience plan** against the six Art. 13(1) areas and the C/2026/3712 domains; treat it as the CER equivalent of an ISMS statement of applicability and keep evidence per measure. See [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md) and [../../templates/statement-of-applicability.md](../../templates/statement-of-applicability.md).
5. **Physical and personnel security become auditable controls**: perimeter, access control, critical-function role inventories (including contractor personnel), background-check procedures compliant with GDPR, and awareness exercises. Integrate with HR and facilities; log the legal basis for each check. See [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md) for the background-check privacy assessment.
6. **Wire the 24-hour / 1-month notification into incident response**, with significance triage on users, duration and geography, and a parallel path for NIS2 (24h/72h/1 month) and GDPR (72h) where the same event qualifies. Pre-register the national portal and the liaison officer. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
7. **Third-party and supply-chain resilience**: Art. 13(1)(d) alternative supply chains and Art. 12(2) dependency analysis require a mapped supplier-criticality view; add resilience and personnel-security clauses for providers whose staff exercise critical functions. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
8. **Prepare for inspection, audit orders and advisory missions**: on-site inspection rights, independent-audit-at-your-expense demands (Art. 21(2)(b)) and, for six-plus-Member-State providers, Commission advisory missions with access to systems and facilities. Maintain an evidence pack. See [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md) and [../../templates/audit-evidence-request-list.md](../../templates/audit-evidence-request-list.md).
9. **Watch transposition and secondary law** per Member State: penalty regimes, designation vs registration models, incident portals, and the pending Art. 13(6)/18(6) implementing acts. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md) and [../../workflows/new-regulation-impact-assessment.md](../../workflows/new-regulation-impact-assessment.md).

## Interplay

- **NIS2 (Directive (EU) 2022/2555):** the two are designed as a pair. Every entity identified as critical under CER is a NIS2 essential entity regardless of size (NIS2 Art. 2(3) and Art. 3(1)(f)) — a CER designation can therefore pull a small or "important"-tier organisation into the strictest NIS2 supervision and fine tier. CER authorities must notify NIS2 authorities of identifications within one month, exchange information on risks and incidents, and may ask NIS2 authorities to exercise their powers; NIS2 CSIRTs pass incident data on CER entities back to CER authorities. Digital-infrastructure entities are identified under CER but their physical security is handled entirely within NIS2 risk-management measures. See [nis2.md](nis2.md).
- **DORA (Regulation (EU) 2022/2554):** credit institutions, trading venues and CCPs are identified under CER but exempt from its entity-level chapters because DORA and financial-services law already cover operational resilience; their CER competent authorities are, in principle, the DORA Art. 46 authorities (CER Art. 9(1)). See [dora.md](dora.md).
- **GDPR and Law Enforcement Directive:** background checks (Art. 14) and incident notifications containing personal data must comply with GDPR; CER is expressly without prejudice to data-protection law (Art. 1(9)). A disruptive incident that is also a personal-data breach triggers the 72-hour GDPR clock in parallel. See [gdpr.md](gdpr.md).
- **Sector rules:** Art. 1(3) equivalence and Art. 18(9) references to aviation/maritime/port security inspections (Regs 300/2008, 725/2004, Directive 2005/65/EC) mean sector security regimes can displace or feed CER obligations; Seveso III, gas-supply and electricity risk-preparedness assessments are inputs to Member State risk assessments (Art. 5(2)).
- **Frameworks:** CER's six measure areas map naturally onto ISO 22301 (continuity), ISO/IEC 27001:2022 physical and people controls (Annex A 6.x and 7.x) and NIST CSF 2.0 Govern/Protect/Recover; use them as the control library and CER as the obligation set. See [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md), [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
- **Crisis coordination:** Council Recommendation C/2024/4371 (Critical Infrastructure Blueprint) governs EU-level response to cross-border disruptions and sits alongside, not inside, CER.

## Primary sources

- Directive (EU) 2022/2557 (legal text, EUR-Lex CELEX 32022L2557): https://eur-lex.europa.eu/eli/dir/2022/2557/oj
- Commission Delegated Regulation (EU) 2023/2450 establishing a list of essential services (legal text, CELEX 32023R2450): https://eur-lex.europa.eu/eli/reg_del/2023/2450/oj
- Directive (EU) 2022/2555 (NIS2) Arts. 2(3), 3(1)(f), 13, 23(10), 32(9) on CER coordination (legal text, CELEX 32022L2555): https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- Commission Communication C(2025) 6094 — guidelines and reporting template under Arts. 5(5), 6(6), 7(3) (regulator guidance, PDF): https://home-affairs.ec.europa.eu/document/download/d9dca1da-3daf-4c11-beb7-702c0da55591_en
- Commission Communication C/2026/3712 — guidelines on Art. 13(5) resilience measures (regulator guidance, OJ C 13.7.2026, CELEX 52026XC03712): https://eur-lex.europa.eu/eli/C/2026/3712/oj
- DG Migration and Home Affairs, "Critical infrastructure resilience at EU-level" (regulator page: timeline, CERG, guidelines): https://home-affairs.ec.europa.eu/policies/internal-security/counter-terrorism-and-radicalisation/protection/critical-infrastructure-resilience-eu-level_en
- Commission news, 11 September 2025 (identification guidelines) and 10 July 2026 (resilience-measures guidelines): https://home-affairs.ec.europa.eu/news/commission-adopts-guidelines-enhance-resilience-critical-entities-eu-2025-09-11_en and https://home-affairs.ec.europa.eu/news/commission-issues-guidance-strengthen-resilience-critical-infrastructure-2026-07-10_en
- Commission press release IP/26/910 of 29 April 2026 — referral of seven Member States to the CJEU for failure to transpose (regulator page): https://ec.europa.eu/commission/presscorner/detail/en/ip_26_910
- Council Recommendation C/2024/4371 of 25 June 2024 on the Critical Infrastructure Blueprint (legal text, OJ C 5.7.2024, CELEX 32024H04371): https://eur-lex.europa.eu/eli/C/2024/4371/oj
- Germany, KRITIS-Dachgesetz of 11 March 2026 (national transposing act; example of a self-registration model): https://www.gesetze-im-internet.de/kritisdachg/

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
