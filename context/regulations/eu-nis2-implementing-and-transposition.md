# NIS2 level-2 detail and member-state transposition (Implementing Regulation (EU) 2024/2690 and national laws)

This pack complements [nis2.md](nis2.md), which covers the Directive itself (scope, Art. 21 measures, Art. 23 clocks, fines). It does not restate that content. It covers the two layers that sit beneath the Directive: the Commission's implementing act for digital-infrastructure and digital-provider entities, and the national laws that actually bind entities.

## At a glance

| Attribute | Detail |
|---|---|
| Level-2 instrument | Commission Implementing Regulation (EU) 2024/2690 of 17 October 2024 (OJ L, 18.10.2024) — directly applicable; adopted under NIS2 Art. 21(5) first subparagraph and Art. 23(11) second subparagraph |
| Entry into force | Twentieth day after OJ publication (18 October 2024); repeals Implementing Regulation (EU) 2018/151 (the NIS1 digital-service-provider act) |
| Who it binds | "Relevant entities": DNS service providers, TLD name registries, cloud computing, data centre, CDN, managed service and managed security service providers, online marketplaces, online search engines, social networking platforms, and trust service providers (Art. 1) |
| Content | Art. 2 + Annex: technical and methodological requirements for each Art. 21(2) measure (13 Annex sections); Arts. 3–14: general and sector-specific "significant incident" thresholds |
| Basis of the Annex | Recital 3: built on ISO/IEC 27001, ISO/IEC 27002, ETSI EN 319 401 and CEN/TS 18026:2024 |
| Regulator guidance | ENISA "NIS2 Technical Implementation Guidance" (26 June 2025) with mapping table v1.2; Commission guidelines on Art. 3(4) and Art. 4(1)–(2) (14 September 2023) |
| Transposition deadline | 17 October 2024 (NIS2 Art. 41(1)); letters of formal notice 28 November 2024; reasoned opinions to 19 member states 7 May 2025; Ireland, Spain, France, Netherlands referred to the CJEU 8 July 2026 |
| Entity lists / registries | Member-state lists of essential and important entities due by 17 April 2025, refreshed at least every two years (Art. 3(3)); ENISA registry of digital entities fed by data due 17 January 2025 (Art. 27) |
| Pending change | Commission proposal COM(2026) 13 (20 January 2026) for targeted NIS2 amendments — still a proposal as of September 2026 (verify) |
| Penalties | Set by national law within NIS2 Art. 34 floors; e.g. Germany BSIG § 65: up to €10M / €7M, or 2% / 1.4% of total turnover for groups above €500M turnover |

## What it is

NIS2 is a directive: the Art. 21 measure list and Art. 23 clocks only bind an entity through the national law of each member state where it operates, and national laws differ on registration mechanics, portals, sector definitions, evidence duties and fines. The Commission was, however, required (Art. 21(5), Art. 23(11)) to adopt by 17 October 2024 an implementing act that fixes, EU-wide and directly, both the technical detail of the ten measures and the incident-significance thresholds for the eleven cross-border digital entity types listed above. That act is Implementing Regulation (EU) 2024/2690. For those entities it is the operative text; for all other essential and important entities it is persuasive only, pending any further implementing acts under Art. 21(5) second subparagraph.

The transposition picture as of September 2026 is uneven. Seven member states were recorded as "transposed" on the Commission's tracker in July 2025 (Belgium, Croatia, Greece, Italy, Lithuania, Romania, Slovakia); Malta was "not yet transposed"; the other nineteen received reasoned opinions on 7 May 2025. Since then Germany's law entered into force (6 December 2025) and the Netherlands' law took effect (15 August 2026), while France and Ireland still had bills pending and, with Spain and the Netherlands, were referred to the Court of Justice on 8 July 2026 with a request for lump-sum and daily penalties.

## Who it covers / Scope

- **Implementing Regulation 2024/2690** applies only to the eleven entity types in Art. 1, regardless of whether they are classed essential or important. Art. 2(2) embeds proportionality: entities weigh risk exposure, size and incident likelihood/severity, and where the Annex says "where appropriate / applicable / to the extent feasible" and the entity does not apply a requirement, it must document its reasoning comprehensibly. Recital 5 allows compensating measures (e.g., targeted management oversight, extra monitoring and logging) where size prevents segregation of duties.
- **National laws** cover all Annex I/II sectors per the Directive's size-cap rule, but each transposition sets its own classification labels, registration route and supervisory bodies. Germany, for example, uses "besonders wichtige Einrichtungen" (essential) and "wichtige Einrichtungen" (important) in BSIG § 28 with the Directive's 50-employee / €10M and 250-employee / €50M-€43M thresholds, treats KRITIS operators, qualified trust service providers, TLD registries and DNS providers as essential regardless of size, and carves DORA financial entities out of the core risk-management, reporting and management-duty sections (§ 28(6)).
- **Multi-country groups** must run the applicability test per member state, because the same subsidiary can be in scope in one state and out of scope in another until every state has transposed. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).

## Core obligations

### Implementing Regulation 2024/2690 — Annex: technical and methodological requirements

| Annex § | Topic (NIS2 Art. 21(2) point) | Notable requirements |
|---|---|---|
| 1 | Policy on the security of network and information systems (a) | 1.1 security policy; 1.2 roles, responsibilities and authorities |
| 2 | Risk management policy (a) | 2.1 risk management framework; 2.2 compliance monitoring; 2.3 independent review of information and network security |
| 3 | Incident handling (b) | 3.1 incident handling policy; 3.2 monitoring and logging; 3.3 event reporting; 3.4 event assessment and classification; 3.5 incident response; 3.6 post-incident reviews |
| 4 | Business continuity and crisis management (c) | 4.1 BC/DR plan; 4.2 backup and redundancy management; 4.3 crisis management |
| 5 | Supply chain security (d) | 5.1 supply chain security policy; 5.2 directory of suppliers and service providers |
| 6 | Acquisition, development and maintenance (e) | 6.1 secure acquisition of ICT services/products; 6.2 secure development life cycle; 6.3 configuration management; 6.4 change management, repairs and maintenance; 6.5 security testing; 6.6 security patch management; 6.7 network security; 6.8 network segmentation; 6.9 protection against malicious and unauthorised software; 6.10 vulnerability handling and disclosure |
| 7 | Assessing effectiveness of measures (f) | Policies and procedures to assess effectiveness |
| 8 | Basic cyber hygiene and security training (g) | 8.1 awareness raising and basic cyber hygiene practices; 8.2 security training |
| 9 | Cryptography (h) | Policy and procedures on cryptography and, where appropriate, encryption |
| 10 | Human resources security (i) | 10.1 HR security; 10.2 verification of background; 10.3 termination or change of employment; 10.4 disciplinary process |
| 11 | Access control (i), (j) | 11.1 access control policy; 11.2 management of access rights; 11.3 privileged and system administration accounts; 11.4 administration systems; 11.5 identification; 11.6 authentication; 11.7 multi-factor authentication |
| 12 | Asset management (i) | 12.1 asset classification; 12.2 handling of assets; 12.3 removable media policy; 12.4 asset inventory; 12.5 deposit, return or deletion of assets on termination |
| 13 | Environmental and physical security (c), (e), (i) | 13.1 supporting utilities; 13.2 protection against physical and environmental threats; 13.3 perimeter and physical access control |

The Annex reads like a condensed ISO/IEC 27002 control set with explicit review cadences and documentation duties; an ISO 27001-certified ISMS covers most of it but should be gap-checked section by section (see [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) and ENISA's mapping table).

### Implementing Regulation 2024/2690 — significant-incident thresholds

**General criteria (Art. 3(1))** — an incident is significant if it meets any one of: (a) direct financial loss to the entity exceeding **€500,000 or 5% of total annual turnover** in the preceding financial year, whichever is lower; (b) exfiltration of trade secrets; (c) death of a natural person; (d) considerable damage to a natural person's health; (e) a successful, suspectedly malicious, unauthorised access to network and information systems capable of causing severe operational disruption; (f) the recurring-incident test in Art. 4; (g) a sector criterion in Arts. 5–14. Scheduled interruptions and planned maintenance consequences are excluded (Art. 3(2)). User counts include contracted customers plus the natural and legal persons associated with business customers who use the service (Art. 3(3)).

**Recurring incidents (Art. 4)** — incidents that are individually below threshold count collectively as one significant incident if they occurred at least twice within 6 months, share the same apparent root cause, and collectively meet the Art. 3(1)(a) financial-loss test.

| Art. | Entity type | Sector-specific triggers (any one suffices) |
|---|---|---|
| 5 | DNS service providers | Recursive or authoritative resolution completely unavailable > 30 min; average response time > 10 s for > 1 h; integrity/confidentiality/authenticity of authoritative-resolution data compromised (misconfiguration of < 1,000 domain names and ≤ 1% of managed names excepted) |
| 6 | TLD name registries | Authoritative resolution completely unavailable (no minimum duration); average response time > 10 s for > 1 h; data related to TLD technical operation compromised |
| 7 | Cloud computing | Service completely unavailable > 30 min; availability limited for > 5% of EU users or > 1 million EU users (whichever smaller) for > 1 h; data compromised by suspectedly malicious action; data compromised affecting > 5% / > 1 million EU users |
| 8 | Data centre services | Service of a data centre completely unavailable (no minimum duration); availability limited > 1 h; data compromised by suspectedly malicious action; physical access to a data centre compromised |
| 9 | CDN providers | Same pattern as cloud: > 30 min total outage; > 5% / > 1 million users limited for > 1 h; malicious data compromise; data compromise affecting > 5% / > 1 million users |
| 10 | Managed service / managed security service providers | Same pattern as cloud (30 min; 5% / 1 million for > 1 h; malicious compromise; 5% / 1 million impact) |
| 11–13 | Online marketplaces, online search engines, social networking platforms | Completely unavailable for > 5% or > 1 million EU users; limited availability affecting > 5% / > 1 million users; malicious data compromise; data compromise affecting > 5% / > 1 million users |
| 14 | Trust service providers | Completely unavailable > 20 min; unavailable to users/relying parties > 1 h per calendar week; limited availability affecting > 1% or > 200,000 users/relying parties; compromised physical access to restricted areas; data compromise affecting > 0.1% or > 100 users/relying parties |

These thresholds define *what* to report; the 24 h / 72 h / 1-month clocks in [nis2.md](nis2.md) and the national law define *when* and *to whom*. Log both in [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).

### Registration and entity lists (Directive Arts. 3 and 27)

- Member states had to establish their list of essential and important entities (plus domain-name registration service providers) by **17 April 2025** and must refresh it at least every two years (Art. 3(3)); competent authorities notify entity counts to the Commission on the same cadence (Art. 3(5)).
- Minimum registration data (Art. 3(4)): entity name; address and up-to-date contact details including email addresses, IP ranges and telephone numbers; sector and subsector; the member states where in-scope services are provided. Changes must be notified without delay and within **two weeks**. States may run self-registration mechanisms.
- Digital entities (DNS, TLD, domain-name registration, cloud, data centre, CDN, MSP/MSSP, marketplaces, search engines, social networks) had to submit registry data to their competent authority by **17 January 2025** for ENISA's EU-level registry (Art. 27).

### National transposition snapshot (as of September 2026)

| Member state | Status and instrument | Registration / practical mechanics |
|---|---|---|
| Germany | BSI-Gesetz (BSIG) of 2 December 2025 (BGBl. 2025 I Nr. 301), in force **6 December 2025**; already amended in March and July 2026 | Register with BSI within **3 months** of first qualifying (§ 33(1)), via the BSI-Portal using an ELSTER organisation certificate; changes within 2 weeks; BSI states the initial deadline has expired. § 30 lists the ten measures and requires "state of the art"; § 31 mandates attack-detection systems for KRITIS operators; § 32 mirrors 24 h / 72 h / 1-month reporting to a joint BSI–BBK reporting office; § 38 imposes implementation, oversight and training duties on management with personal liability to the entity; § 39 KRITIS evidence submissions at the earliest 3 years after qualifying |
| Netherlands | Cyberbeveiligingswet (Cbw), in force **15 August 2026**, replacing the Wbni; NCSC estimates > 8,000 organisations in scope | Mandatory registration in the entity register via MijnNCSC (eHerkenning / SSOnRijk); incidents to the CSIRT and supervisor within 24 h; board approves and oversees measures. Referred to the CJEU on 8 July 2026, before the law took effect |
| Italy | Legislative Decree 138 of 4 September 2024, in force 16 October 2024; ACN is competent authority; 18 sectors (11 highly critical, 7 critical) and 80+ entity types | Annual ACN-portal registration window **1 January–28 February**; information updates **15 April–31 May**; significant-incident reporting from January 2026; basic security measures due by October 2026 |
| France | Still a bill ("projet de loi Résilience") per ANSSI; referred to the CJEU 8 July 2026 | ANSSI published the Référentiel Cyber France (ReCyF) on **17 March 2026** as a working document — the non-mandatory reference framework foreseen in Art. 14 of the bill, which entities may invoke during ANSSI inspections; MonEspaceNIS2 portal for applicability checks |
| Belgium | Transposed (Commission tracker) | CCB's CyberFundamentals (CyFun) framework — Basic / Important / Essential assurance levels, grounded in NIST CSF — is the national reference scheme (details verify on ccb.belgium.be; the site blocks scripted access) |
| Ireland | Bill not enacted; General Scheme published September 2024; registration and incident portals not yet open; referred to the CJEU 8 July 2026 | Draft Risk Management Measures guidance and CyFun adoption announced 24 June 2025; Ireland is a CyFun scheme co-owner and recommends it as a voluntary route, alongside ISO 27001 and 62443 |
| Spain | Reasoned opinion 7 May 2025; referred to the CJEU 8 July 2026 | No national NIS2 law notified as of the referral |
| Croatia, Greece, Lithuania, Romania, Slovakia | Transposed (Commission tracker, July 2025) | Check national portals; not detailed here |
| Austria, Bulgaria, Cyprus, Czechia, Denmark, Estonia, Finland, Hungary, Latvia, Luxembourg, Poland, Portugal, Slovenia, Sweden | Reasoned opinion 7 May 2025; not referred to the CJEU in July 2026 | Several have since adopted laws (verify each against the national gazette; the Commission tracker pages were last updated July 2025) |
| Malta | "Not yet transposed" on the Commission tracker (July 2025) | Verify current status |

### EU-level crisis and cooperation machinery

- **EU-CyCLONe** (NIS2 Art. 16): the network of national cyber crisis management authorities, launched in 2020 and formalised on 16 January 2023; ENISA provides the secretariat; chaired by the member state holding the Council presidency; the Commission joins as a member for large-scale incidents affecting NIS2 services and otherwise observes. It reports to the European Parliament and Council every 18 months (first by 17 July 2024). ENISA runs CySOPex (officer-level) and BlueOLEx (executive-level) exercises.
- **CSIRTs network** and **NIS Cooperation Group** handle operational and strategic cooperation respectively; the Cooperation Group's non-binding guidance and the Commission guidelines of 14 September 2023 on Art. 3(4) (entity lists) and Art. 4(1)–(2) (sector-specific lex specialis) are the main interpretive aids.

## Enforcement and penalties

- Fines are national. NIS2 Art. 34 sets floors (see [nis2.md](nis2.md)); transpositions convert them to ceilings and add tiers. Germany's BSIG § 65 illustrates the pattern: up to €10M for essential entities and €7M for important entities, with intermediate tiers of €5M and €2M for lesser breaches, and for entities with total turnover above €500M up to 2% (essential) or 1.4% (important) of total turnover for the core risk-management, reporting and registration breaches.
- Management liability is transposed differently: Germany's § 38(2) makes management liable to the entity for culpably caused damage under the company-law rules applicable to its legal form (the BSIG's own liability rule applies only where company law has none); other states rely on general director-liability rules.
- Supervision timing lags transposition: Germany allows BSI to demand evidence from most essential entities only three years after entry into force (five for hospitals); Italy phases incident reporting (January 2026) and baseline measures (October 2026). Early years are dominated by registration enforcement rather than audits.
- For the eleven digital entity types, non-compliance with Implementing Regulation 2024/2690 is enforced through the national NIS2 law of the main-establishment state; there is no separate EU-level fine.

## Timeline and status

| Date | Event |
|---|---|
| 14 September 2023 | Commission guidelines on Art. 3(4) and on Art. 4(1)–(2) published |
| 17 October 2024 | Transposition deadline (Art. 41); Implementing Regulation 2024/2690 adopted (published 18 October 2024) |
| 28 November 2024 | Letters of formal notice to non-transposing member states |
| 17 January 2025 | Digital entities' registry data due (Art. 27) |
| 17 April 2025 | Member-state lists of essential and important entities due (Art. 3(3)) |
| 7 May 2025 | Reasoned opinions to 19 member states |
| 26 June 2025 | ENISA NIS2 Technical Implementation Guidance published (with "Cybersecurity roles and skills for NIS2 entities") |
| 6 December 2025 | Germany's BSIG (NIS2 transposition) in force |
| 20 January 2026 | Commission cybersecurity package: COM(2026) 13 proposes targeted NIS2 amendments (simplified jurisdiction rules, streamlined ransomware data collection, cross-border supervision with a reinforced ENISA coordinating role; complements the Digital Omnibus single-entry point for incident reporting; stated to ease compliance for 28,700 companies including 6,200 micro and small enterprises) — under negotiation (verify) |
| 17 March 2026 | ANSSI publishes ReCyF (France) as a working document |
| 8 July 2026 | Ireland, Spain, France, Netherlands referred to the CJEU with a request for financial penalties |
| 15 August 2026 | Netherlands' Cyberbeveiligingswet in force |
| October 2026 | Italian baseline security measures due (ACN) |
| Pending | Adoption of COM(2026) 13; remaining transpositions; possible further Commission implementing acts for other sectors (Art. 21(5) second subparagraph, Art. 23(11)) — none adopted as of September 2026 (verify) |

## Key obligations for security/GRC teams

1. **Classify the entity type first, then the rulebook**: if the organisation is one of the eleven digital entity types, Implementing Regulation 2024/2690 is binding EU-wide — build the control set from its Annex, not from the Directive's ten headings. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Wire the Art. 3–14 thresholds into incident triage**: pre-compute the €500,000 / 5%-of-turnover figure, the user-count denominators (5% / 1 million; 1% / 200,000 for trust services) and the outage timers (20 / 30 / 60 minutes), and add the 6-month recurring-incident aggregation to post-incident review. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
3. **Maintain a per-country registration register**: who is registered where, under which classification, with the two-week change-notification duty tracked; Germany's three-month window and Italy's January–February window are hard dates.
4. **Document proportionality decisions**: every Annex requirement marked "where appropriate/applicable/feasible" that is not applied needs a written, comprehensible rationale (Art. 2(2)); manage these as formal exceptions — [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
5. **Map the Annex to the existing ISMS** using ENISA's mapping table and the repository crosswalk; the usual gaps are 2.2 compliance monitoring, 2.3 independent review, 5.2 supplier directory, 6.10 vulnerability disclosure and 11.7 MFA scope. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
6. **Build the supplier directory and contract clauses** required by Annex § 5 and mirrored in national laws; see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
7. **Evidence management-body duties nationally**: German § 38 requires demonstrable implementation oversight and regular training; keep attendance and decision records for board reporting — [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).
8. **Track the moving parts**: COM(2026) 13, CJEU referrals, late transpositions and any new sector implementing acts change jurisdiction and reporting mechanics; run them through [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md) and [../../workflows/new-regulation-impact-assessment.md](../../workflows/new-regulation-impact-assessment.md).

## Interplay

- **NIS2 Directive** ([nis2.md](nis2.md)): the Directive supplies scope, the ten measures, the clocks and fine floors; this pack supplies the level-2 detail and national mechanics. National laws prevail over the Directive text; Implementing Regulation 2024/2690 prevails over national detail for its eleven entity types (Germany's BSIG § 30(3)–(4) says so expressly).
- **DORA** ([dora.md](dora.md)): financial entities are carved out of national NIS2 risk-management and reporting duties (e.g., BSIG § 28(6)); a cloud or MSP serving banks remains a NIS2 relevant entity under 2024/2690 and may simultaneously be a DORA ICT third-party provider.
- **GDPR** ([gdpr.md](gdpr.md)): a data-compromise trigger under Arts. 7–14 of 2024/2690 will usually also be a personal-data breach; the 72-hour GDPR clock runs to a different authority.
- **ISO/IEC 27001** ([../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md)) and **NIST CSF 2.0** ([../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md)): the Annex is drafted on ISO/IEC 27001/27002 and ETSI EN 319 401; Belgium's and Ireland's CyFun scheme is grounded in NIST CSF; France's ReCyF and Germany's sector-specific standards (BSIG § 30(8)) are further national mappings.
- **EU AI Act** ([eu-ai-act.md](eu-ai-act.md)): no reporting overlap, but Annex § 6 secure-development and § 5 supply-chain requirements extend to AI components operated by relevant entities.
- **Cybersecurity Act / certification**: BSIG § 30(6) allows Germany to mandate EU-certified ICT products by ordinance; COM(2026) 13 is framed as aligning NIS2 with the Cybersecurity Act.

## Primary sources

- Commission Implementing Regulation (EU) 2024/2690 — official legal text (Publications Office, CELEX 32024R2690): https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj
- Directive (EU) 2022/2555 (NIS2) — official legal text (CELEX 32022L2555): https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- Commission, "NIS2 Directive: securing network and information systems" — policy page: https://digital-strategy.ec.europa.eu/en/policies/nis2-directive
- Commission, "NIS2 Directive transposition in EU countries" and per-country pages (last updated July 2025) — regulator tracker: https://digital-strategy.ec.europa.eu/en/policies/nis-transposition
- Commission press release, 8 July 2026, referral of Ireland, Spain, France and the Netherlands to the CJEU: https://digital-strategy.ec.europa.eu/en/news/commission-refers-ireland-spain-france-and-netherlands-court-justice-failing-transpose-rules
- Commission, COM(2026) 13 proposal page (20 January 2026): https://digital-strategy.ec.europa.eu/en/library/proposal-directive-regards-simplification-measures-and-alignment-cybersecurity-act
- Commission guidelines on Art. 3(4) and on Art. 4(1)–(2) (14 September 2023): https://digital-strategy.ec.europa.eu/en/library/commission-guidelines-application-article-34-directive-eu-20222555-nis-2-directive and https://digital-strategy.ec.europa.eu/en/library/commission-guidelines-application-article-4-1-and-2-directive-eu-20222555-nis-2-directive
- ENISA, "NIS2 Technical Implementation Guidance" (26 June 2025) — regulator guidance: https://www.enisa.europa.eu/publications/nis2-technical-implementation-guidance
- ENISA, EU-CyCLONe topic page: https://www.enisa.europa.eu/topics/eu-incident-response-and-cyber-crisis-management/eu-cyclone
- Germany: BSI-Gesetz (BSIG) consolidated text, gesetze-im-internet.de (§§ 28, 30–33, 38, 39, 65): https://www.gesetze-im-internet.de/bsig_2025/ ; BSI, "NIS-2-regulierte Unternehmen" (registration): https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-regulierte-Unternehmen/nis-2-regulierte-unternehmen_node.html
- Netherlands: NCSC, "Cyberbeveiligingswet (NIS2)": https://www.ncsc.nl/onderwerpen/cyberbeveiligingswet
- Italy: ACN, NIS portal (English): https://www.acn.gov.it/portale/en/nis
- France: ANSSI, "La directive NIS 2": https://cyber.gouv.fr/la-directive-nis-2
- Ireland: NCSC, NIS2 page and CyFun page: https://www.ncsc.gov.ie/nis2/ and https://www.ncsc.gov.ie/CyFun/
- Belgium: CCB NIS2 and CyberFundamentals pages (https://ccb.belgium.be/en/nis-2-directive) — not accessible at time of review (site blocks automated access); Belgian specifics above are drawn from the Commission tracker and the Irish NCSC CyFun page.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
