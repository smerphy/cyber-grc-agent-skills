# Brazil — Lei Geral de Proteção de Dados Pessoais (LGPD, Law 13.709/2018)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Lei nº 13.709, de 14 de agosto de 2018 (LGPD), as amended — principally by Law 13.853/2019 (conversion of MP 869/2018; created the ANPD), Law 14.010/2020 (deferred sanctions), Law 14.460/2022 (ANPD became a special-regime autarchy) and Law 15.352/2026 (conversion of MP 1.317/2025; ANPD became a regulatory agency) |
| Constitutional anchor | Constitutional Amendment (EC) 115 of 10 February 2022 added Art. 5, LXXIX (right to protection of personal data, including in digital media) and gave the Union exclusive competence to legislate on data protection (Art. 22, XXX) |
| Regulator | Agência Nacional de Proteção de Dados (ANPD) — since Law 15.352/2026 a regulatory agency under Law 13.848/2019, linked to the Ministry of Justice and Public Security, with functional, technical, decision-making, administrative and financial autonomy (LGPD Art. 55-A) |
| Status and key dates | ANPD provisions in force 28 Dec 2018; substantive articles in force 24 months after publication (September 2020); administrative sanctions (Arts. 52–54) applicable from 1 Aug 2021 (Art. 65) |
| Who is covered | Any natural or legal person, public or private, processing personal data in Brazil, offering goods/services to or processing data of individuals located in Brazil, or processing data collected in Brazil (Art. 3) — extraterritorial, GDPR-style |
| Structure | 65 articles covering: scope and definitions; legal bases (10) and sensitive data; data-subject rights; public-sector processing; international transfers; controllers, processors and the DPO (encarregado); security and incident communication; good practices/governance; sanctions; ANPD and the National Council (CNPD) |
| Incident clock | 3 business days to the ANPD and to affected data subjects, counted from the controller's knowledge that the incident affected personal data (Res. CD/ANPD 15/2024) |
| Penalties | Warning; simple fine up to 2% of the private entity's/group's revenue in Brazil for the last fiscal year (net of taxes) capped at R$ 50,000,000 per infraction; daily fine (same cap); publicization; blocking; deletion; suspension of database or processing activity (up to 6 months, renewable); partial or total prohibition (Art. 52) |
| Certifiable? | No. Compliance is demonstrated through accountability evidence (Art. 6, X); seals, certificates and codes of conduct are contemplated as a transfer mechanism (Art. 33, II, d) and the ANPD may designate certification bodies (Art. 35 §3), but the ANPD's transfer page lists no certification-based mechanism among those it has regulated |
| Neighbours | GDPR family (mutual EU–Brazil adequacy since January 2026); Marco Civil da Internet (Law 12.965/2014); Consumer Defense Code (CDC) sanctions preserved (Art. 52 §2); ECA Digital (Law 15.211/2025) for children online, enforced by the ANPD |

## What it is

The LGPD is Brazil's omnibus data-protection statute, modelled closely on the GDPR: purpose-limited processing on one of ten enumerated legal bases, a catalogue of data-subject rights, accountability duties (records, impact reports, a designated encarregado), a security-incident communication duty, and administrative sanctions applied by a national authority. It applies equally to public and private bodies (Art. 1) and expressly to processing "including in digital media". Law 13.853/2019 fixed the original text's biggest gap by creating the ANPD; Law 14.460/2022 gave the ANPD legal personality as a special-regime autarchy; MP 1.317/2025, converted into Law 15.352 of 25 February 2026, turned it into a full regulatory agency (Agência Nacional de Proteção de Dados) under the general regulatory-agencies statute (Law 13.848/2019) and created a dedicated data-protection regulation and inspection career.

The statute is deliberately skeletal in places and delegates detail to ANPD regulation (Art. 55-J, XIII). Much of what an operations team needs — incident deadlines and content, the fine methodology, SCCs, DPO duties, the small-agent regime — therefore lives in Conselho Diretor resolutions rather than the law itself, and those resolutions are what change most often.

## Who it covers / Scope

| Test (Art. 3) | Detail |
|---|---|
| Territorial | Processing operation carried out in the national territory |
| Targeting | Processing whose purpose is offering or supplying goods or services to, or processing data of, individuals located in Brazil |
| Collection | Personal data collected in Brazil — data are "collected in Brazil" when the data subject is in Brazil at the moment of collection (§1) |
| Irrelevant | The medium, the country where the agent is headquartered, or where the data are located |

**Exclusions (Art. 4):** processing by a natural person for exclusively private, non-economic purposes; exclusively journalistic, artistic or academic purposes (Arts. 7 and 11 still apply to academic processing); public security, national defence, State security and criminal investigation/prosecution (to be governed by specific legislation; §1); and data originating abroad that are not shared with Brazilian agents or onward-transferred, provided the country of origin offers adequate protection (IV). The transfer regulation (Res. 19/2024, Art. 8) narrows the last exclusion to pure transit and to return of data to an ANPD-recognised adequate country under conditions stated in the adequacy decision.

**Key definitions (Art. 5):** *personal data* — information relating to an identified or identifiable natural person; *sensitive data* — racial or ethnic origin, religious conviction, political opinion, union or religious/philosophical/political organisation membership, health, sex life, genetic or biometric data; *anonymised data* fall outside the law unless reversible by reasonable means (Art. 12); *controller* decides; *operator* processes on the controller's behalf; *encarregado* (DPO) is the communication channel between controller/operator, data subjects and the ANPD; *treatment* is any operation on personal data.

**Small processing agents (Res. CD/ANPD 2/2022):** micro and small enterprises, startups, non-profits, natural persons and unincorporated private entities get a lighter regime — simplified records of processing (ANPD template), no mandatory DPO (but a data-subject contact channel is required), a simplified information-security policy, and doubled deadlines for data-subject requests and incident communication. The regime is lost if the agent performs high-risk processing (one general criterion — large scale or significant effect on rights — plus one specific criterion: emerging technologies, surveillance of public areas, solely automated decisions/profiling, or sensitive/children's/elderly data), exceeds the revenue ceilings of LC 123/2006 (or LC 182/2021 for startups), or belongs to a group that does (Arts. 3–4).

## Core obligations

### Principles and legal bases

| Item | Content |
|---|---|
| Principles (Art. 6) | Good faith plus ten principles: purpose, adequacy, necessity, free access, data quality, transparency, security, prevention, non-discrimination, accountability (responsabilização e prestação de contas) |
| Legal bases — general data (Art. 7) | (I) consent; (II) legal or regulatory obligation; (III) public administration executing public policies; (IV) studies by research bodies (anonymise where possible); (V) contract performance or pre-contractual steps at the data subject's request; (VI) regular exercise of rights in judicial, administrative or arbitral proceedings; (VII) protection of life or physical safety; (VIII) health protection by health professionals, services or authorities; (IX) legitimate interests of the controller or a third party, unless the data subject's fundamental rights prevail; (X) credit protection |
| Consent (Arts. 5 XII, 8) | Free, informed, unequivocal, for a specific purpose; in writing or another demonstrable form; sharing with other controllers needs specific consent (Art. 7 §5); manifestly public data do not require consent (Art. 7 §4) |
| Legitimate interest (Art. 10) | Only for legitimate purposes assessed from concrete situations; strictly necessary data; transparency; ANPD may require an impact report; records "especially" required for this basis (Art. 37) |
| Sensitive data (Art. 11) | Specific, highlighted consent, or one of seven consent-free grounds (legal obligation; public-policy sharing; research; exercise of rights; life/physical safety; health protection; fraud prevention and security in identification/authentication of registrations in electronic systems). The ANPD may prohibit or regulate the sharing of sensitive data between controllers for economic advantage (§3); sharing of health data for economic advantage is already prohibited except for health-service, pharmaceutical-assistance and portability cases (§4). Health data is a Phase 2 item on the 2025–2026 regulatory agenda |
| Children and adolescents (Art. 14) | Best-interest standard; children's data require specific, highlighted consent from at least one parent or legal guardian; no conditioning of games/apps on excess data; reasonable efforts to verify parental consent; child-appropriate notices. Overlaid since 17 March 2026 by the ECA Digital (Law 15.211/2025) — age assurance, parental supervision, advertising limits — which the ANPD enforces |

### Data-subject rights and clocks

| Right (Art. 18) | Notes |
|---|---|
| Confirmation of processing; access | Simplified format **immediately**, or a clear and complete declaration within **15 days** of the request, stating origin, absence of record, criteria used and purpose (Art. 19) |
| Correction; anonymisation, blocking or deletion of unnecessary, excessive or unlawfully processed data; deletion of consent-based data | Controller must notify agents with whom data were shared so they repeat the action (Art. 18 §6) |
| Portability | To another supplier on express request, per ANPD regulation, respecting trade secrets; excludes already-anonymised data (§7) |
| Information on sharing; on the option not to consent and its consequences; consent revocation | Requests are free of charge (§5); the data subject may petition the ANPD or consumer-protection bodies (§§1, 8) |
| Review of solely automated decisions (Art. 20) | Includes profiling for personal, professional, consumer and credit purposes; controller must explain criteria on request; ANPD may audit for discrimination where trade secrecy is invoked. The 2019 amendment removed the requirement that the reviewer be a natural person |

Data-subject rights (Arts. 9, 18, 19, 20) are Phase 1 of the ANPD's 2025–2026 regulatory agenda; a rights regulation may change these clocks — check before hard-coding them.

### Accountability, DPO and impact reports

| Duty | Source | Detail |
|---|---|---|
| Records of processing | Art. 37 | Controller **and** operator keep records of their processing operations, especially where based on legitimate interest |
| RIPD (relatório de impacto à proteção de dados pessoais) | Arts. 5 XVII, 38 | ANPD may require it from a controller (including for sensitive data); minimum content: data types, collection and security methodology, controller's analysis of measures, safeguards and mitigation. A general RIPD regulation is Phase 1 on the 2025–2026 agenda; today the trigger is regulator demand plus the high-risk criteria in Res. 2/2022. See [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md) and [../../templates/dpia-template.md](../../templates/dpia-template.md) |
| Encarregado (DPO) | Art. 41; Res. CD/ANPD 18/2024 | Every controller must appoint one by a formal, dated, signed act (produced to the ANPD on request); may be a natural person (internal or external) or a legal person; no certification or registration required; must communicate in Portuguese; identity and contact details published prominently on the website; must have resources, technical autonomy, direct access to top management; must avoid conflicts of interest (e.g., also taking strategic processing decisions); a substitute covers absences. Appointment by operators is optional and counts as a good-governance mitigating factor. Statutory tasks: handle data-subject complaints, receive ANPD communications, guide staff and contractors; the regulation adds assisting with incident records/communications, records of processing, RIPDs, security measures, contracts, transfers and privacy-by-design. The DPO is not personally liable to the ANPD for the controller's compliance (Art. 17) |
| Operator duties | Art. 39 | Process only on the controller's instructions; the controller verifies compliance. ANPD guidance: an operator must inform the controller of an incident without undue delay and supply everything needed for the communication |
| Good practices and governance | Art. 50 | Optional codes and a privacy governance programme (§2) whose existence is a statutory mitigating factor in sanctions (Art. 52 §1, IX) and a precondition for approved BCRs |

### Security and incident communication

- **Security (Arts. 46–49):** technical and administrative measures able to protect personal data against unauthorised access and accidental or unlawful destruction, loss, alteration, communication or diffusion; measures apply from product/service conception (privacy by design, Art. 46 §2); security obligations survive the end of processing (Art. 47); systems must be structured to meet security, good-practice and governance standards (Art. 49). The ANPD may set minimum technical standards (Art. 46 §1) — Phase 1 of the 2025–2026 agenda.
- **Incident communication (Art. 48; Res. CD/ANPD 15/2024, DOU 26 April 2024):**

| Element | Requirement |
|---|---|
| Trigger | An incident that **may cause relevant risk or damage** to data subjects: significant effect on interests/fundamental rights **and** at least one of — sensitive data; data of children, adolescents or the elderly; financial data; authentication credentials; data under legal, judicial or professional secrecy; large-scale data (Art. 5). "Security incident" is defined as any **confirmed** adverse event breaching the confidentiality, integrity, availability or authenticity of personal data (Art. 3, XII) |
| Clock to ANPD | **3 business days** from the controller's knowledge that the incident affected personal data, unless sector legislation sets another period (Art. 6). Doubled for small agents |
| Content to ANPD | Nature/category of data; number of data subjects (children, adolescents, elderly separately); security measures before and after; risks and impacts; reasons for any delay; mitigation measures; date of incident and of knowledge; DPO details; controller identification (and small-agent status); operator; description and root cause; total data subjects in the affected activities (Art. 6 §2). Supplementation allowed, with reasons, within **20 business days** (§3). Filed via the ANPD electronic form, by the DPO (with proof of appointment) or a representative with a power of attorney (§§4–5) |
| Clock and content to data subjects | Same **3 business days**; plain language; direct and individual (phone, e-mail, message, letter) or, if infeasible, public notice on website/app/social media/service channels for at least **3 months**; controller files a declaration of the notice within 3 business days after the deadline (Art. 9) |
| Incident register | Keep a record of **every** incident, including those not communicated, for at least **5 years**: date of knowledge, circumstances, data nature/category, number of data subjects, risk assessment, mitigation, form/content of communication or reasons for not communicating (Art. 10) |
| ANPD powers | May order wide publicity of the incident at the controller's expense, order mitigation measures, request the RIPD/records/incident report, audit or inspect, impose daily fines to enforce, and investigate un-notified incidents through a Procedimento de Apuração de Incidente (Arts. 8, 12, 15–19). Ordered measures are preventive, not sanctions (Art. 22) |

- See [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md), [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).

### International transfers (Arts. 33–36; Res. CD/ANPD 19/2024)

| Mechanism | Status as of September 2026 |
|---|---|
| Adequacy decision (Art. 33, I) | **European Union** recognised as an adequate international organisation by Res. CD/ANPD 32 of 26 January 2026 — covers all EU Member States, the three EEA-EFTA states (Iceland, Liechtenstein, Norway) and EU institutions; excludes transfers exclusively for public security, defence, State security or criminal prosecution; reassessment within 4 years. Reciprocally, Commission Implementing Decision (EU) 2026/179 of 26 January 2026 finds Brazil adequate under GDPR Art. 45 for controllers/processors subject to the LGPD. No other country is recognised yet |
| Standard contractual clauses (Art. 33, II, b) | ANPD SCCs in Annex II of Res. 19/2024 (23 August 2024; rectified 18 August 2025); must be adopted **in full and unaltered**; other contract terms may not contradict them; controllers had **12 months** from publication (i.e., to 23 August 2025) to migrate existing contractual transfers. The SCCs themselves carry the 3-business-day incident duty and 15-day data-subject response clock |
| Equivalent foreign SCCs | ANPD may recognise foreign SCCs as equivalent by resolution — none recognised yet |
| Specific contractual clauses (Art. 33, II, a) | Only where SCCs are demonstrably infeasible; prior ANPD approval; none approved yet |
| Global corporate rules / BCRs (Art. 33, II, c) | Intra-group only; require an Art. 50 §2 privacy governance programme, binding effect on all subscribing members, description of transfers and countries, group structure, and ANPD approval — none approved yet |
| Other grounds (Art. 33, III–IX) | International legal cooperation; protection of life; ANPD authorisation; international cooperation agreements; public policy; specific, highlighted consent with prior information on the international character; or where necessary for legal obligation, contract performance or exercise of rights (Art. 7, II, V, VI) |

The regulation clarifies that *international collection* (a foreign agent collecting directly from a data subject in Brazil) is not a transfer but is still subject to the LGPD under Art. 3 (Res. 19/2024, Art. 6), that a transfer needs both a legal basis and a valid mechanism (Art. 9), and that the controller must give the data subject the full clauses on request (Art. 17).

## Enforcement and penalties

**Sanctions (Art. 52)** are applied by the ANPD after an administrative process with full defence, gradually, singly or cumulatively: (I) warning with a deadline for corrective measures; (II) simple fine up to **2% of the revenue in Brazil** of the private legal entity, group or conglomerate in its last fiscal year, net of taxes, capped at **R$ 50 million per infraction**; (III) daily fine, same cap; (IV) publicization of the infraction; (V) blocking of the data; (VI) deletion of the data; (X) partial suspension of the database for up to 6 months, renewable once; (XI) suspension of the processing activity for up to 6 months, renewable once; (XII) partial or total prohibition of processing activities. Sanctions X–XII require a prior sanction under II–VI for the same case and consultation of any sectoral regulator (§6). Public bodies face I, IV, V, VI and X–XII (§3). Fine proceeds go to the Diffuse Rights Defence Fund (§5). Criteria (§1) include gravity, good faith, advantage obtained, economic condition, recidivism, degree of harm, cooperation, demonstrated internal mechanisms, a good-practices/governance policy, prompt correction, and proportionality. LGPD sanctions do not displace consumer-law (CDC) or other civil, administrative or criminal sanctions (§2); controllers and operators are civilly liable for damage (Art. 42) and collective actions are available (Art. 22).

**Dosimetry (Res. CD/ANPD 4/2023, 24 February 2023):** infractions are classified light, medium or grave; grave requires a significant effect on rights plus at least one aggravating feature (large scale; economic advantage; risk to life; sensitive, children's, adolescents' or elderly data; no legal basis; discriminatory effects; systematic irregular practice) or obstruction of inspection (Art. 8). Warnings are for light/medium non-recidivist cases or where corrective measures are needed (Art. 9); a simple fine applies to grave infractions, unmet preventive/corrective measures, or where no other sanction fits (Art. 10). The base value is computed from classification, revenue in the relevant business line and degree of harm (Art. 11); aggravators add +10% per specific recidivism (max 40%), +5% per generic recidivism (max 20%), +20% per unmet guidance/preventive measure (max 80%) and +30% per unmet corrective measure (max 90%) (Art. 12); mitigators include −75/50/30% for ceasing the infraction before, during or after the preparatory stage, −20% for an implemented governance programme, and −5% for cooperation (Art. 13); the result is capped at 2%/R$ 50 million (Art. 15). Daily fines accumulate up to R$ 50 million per infraction (Art. 16). Fines are payable within 20 business days, with a 25% reduction for waiving appeal and paying on time (Arts. 17–18). Recidivism looks back 5 years (Art. 2).

**Practice:** the ANPD describes its model as responsive regulation — monitoring, guidance and preventive measures first, sanctions when a regulated entity does not cooperate; it states that every sanctioning process to date was opened because of a non-collaborative posture. Requerimentos (complaints and petitions) rose from 768 (2021) to 4,029 (2024); the ANPD's published series stops at 2024. Its published list of concluded sanctioning processes (last updated 16 September 2025) holds eight cases: Telekall Infoservices, the Rio de Janeiro Botanical Garden research institute, the Federal District Education Secretariat, the Santa Catarina State Health Secretariat, the São Paulo state-servant assistance institute (IAMSPE), the INSS, the Ministry of Health and a state social-development secretariat (SDSCJ) — mostly for failure to communicate incidents to data subjects, absence of security measures, failure to produce a RIPD or records, or failure to answer the regulator. Ongoing cases are the Ministry of Health, ByteDance/TikTok (children's best interest) and RaiaDrogasil (profiling on sensitive data for monetised advertising). Two monitoring sweeps of 20 companies each — one concluded, one opened in 2025 — target missing DPO designation, identity or contact channels. Fine amounts are published on the federal Transparency Portal (sanctions panel, filter "Agência Nacional de Proteção de Dados") rather than on the ANPD site — check there for current figures.

## Timeline and status

| Date | Event |
|---|---|
| 14 Aug 2018 | Law 13.709 sanctioned |
| 28 Dec 2018 | ANPD/CNPD articles in force (MP 869/2018) |
| 8 Jul 2019 | Law 13.853 — ANPD created, text renamed LGPD, Art. 20 human-review wording removed |
| Sep 2020 | Substantive provisions in force (24 months after publication; a 2020 provisional measure that would have deferred this to May 2021 was not kept on conversion) |
| 1 Aug 2021 | Sanctions (Arts. 52–54) applicable (Law 14.010/2020) |
| 28 Oct 2021 | Res. CD/ANPD 1/2021 — inspection and sanctioning process regulation |
| 27 Jan 2022 | Res. CD/ANPD 2/2022 — small processing agents |
| 10 Feb 2022 | EC 115/2022 — data protection a constitutional fundamental right |
| 25 Oct 2022 | Law 14.460/2022 (conversion of MP 1.124/2022) — ANPD becomes a special-regime autarchy |
| 24 Feb 2023 | Res. CD/ANPD 4/2023 — dosimetry and sanctions |
| 24 Apr 2024 | Res. CD/ANPD 15/2024 — security-incident communication (3 business days) |
| 16 Jul 2024 | Res. CD/ANPD 18/2024 — encarregado (DPO) regulation |
| 23 Aug 2024 | Res. CD/ANPD 19/2024 — international transfers and SCCs; 12-month migration window ended 23 Aug 2025; rectification 18 Aug 2025 |
| 9 Dec 2024 | Res. 23/2024 — regulatory agenda 2025–2026 (amended by Res. CD/ANPD 31 of 22 Dec 2025) |
| 17 Sep 2025 | ECA Digital (Law 15.211/2025) enacted; Decree 12.622/2025 assigns its enforcement to the ANPD |
| 23 Dec 2025 | Res. CD/ANPD 30/2025 — priority enforcement topics map 2026–2027 |
| 26 Jan 2026 | Mutual adequacy: Res. CD/ANPD 32/2026 (EU/EEA adequate for Brazil) and Commission Decision (EU) 2026/179 (Brazil adequate for the EU) |
| 25 Feb 2026 | Law 15.352/2026 (conversion of MP 1.317/2025) — ANPD becomes a regulatory agency; ECA Digital commencement fixed at 17 Mar 2026 (new Art. 41-A of Law 15.211/2025) |
| 17–18 Mar 2026 | ECA Digital in force; Decree 12.880/2026 (18 Mar) details it and creates a national policy; Decree 12.881/2026 (18 Mar) approves the ANPD's new regimental structure; ANPD preliminary age-assurance guidance published; Stage I monitoring of app stores and proprietary operating systems begins |
| Apr–Jul 2026 | ANPD public consultations on an ECA Digital scope guide and on an updated age-assurance guide; app-store and operating-system suppliers required to file compliance documentation by July |

**Pending (regulatory agenda 2025–2026 as amended Dec 2025):** Phase 1 — data-subject rights (Arts. 9, 18, 19, 20), RIPD, public-sector data sharing, biometric data, minimum security standards, artificial intelligence, high-risk processing, religious organisations, anonymisation/pseudonymisation; Phase 2 — national data-protection policy guidelines, data aggregators/scraping, health data, ECA Digital scope guidance, revision of Res. 1/2021 and 4/2023 for ECA Digital enforcement, age-assurance mechanisms; Phase 3 — rule-making procedure (Portaria 16/2021); Phase 4 — good-practice rules, consent, credit-protection basis. The ANPD's published ECA Digital timetable adds dated milestones: definitive age-assurance guidance and Stage II monitoring priorities from August 2026, an adaptation window to November 2026, updated inspection and sanctions regulations (revising Res. 1/2021 and Res. 4/2023) from November 2026, and enforcement action from January 2027 — confirm each has actually issued before relying on it. Track via [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Key obligations for security/GRC teams

1. **Confirm applicability and tier** — Art. 3 tests, Art. 4 exclusions, and whether the small-agent regime (Res. 2/2022) applies; document the high-risk screening because it also drives RIPD expectations. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Appoint and publish the encarregado** by formal act, give them resources, autonomy and access to leadership, screen for conflicts of interest, and keep the website contact current — missing DPO information is the ANPD's current mass-monitoring theme.
3. **Map legal bases per processing activity** in the records of processing (Art. 37), with documented legitimate-interest assessments and separate treatment of sensitive and children's data.
4. **Build the 3-business-day incident playbook**: relevance-risk triage against the six Art. 5 criteria, the 12-item ANPD form content, the DPO filing route with proof of appointment, the data-subject notice template, the 20-business-day supplement, and the 5-year incident register that also captures non-notified incidents. Wire it into [../../workflows/incident-regulatory-response.md](../../workflows/incident-regulatory-response.md).
5. **Run RIPDs for high-risk processing** on the Art. 38 minimum content, and be ready to produce them, the records and the incident report on ANPD demand (Res. 15/2024, Art. 8).
6. **Fix transfers**: inventory cross-border flows, rely on EU/EEA adequacy where applicable, and confirm every remaining contractual transfer uses the unaltered Annex II SCCs (migration deadline passed August 2025); BCRs and specific clauses need prior ANPD approval. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../workflows/vendor-onboarding.md](../../workflows/vendor-onboarding.md).
7. **Contract operators** to process on instruction, report incidents without undue delay and hand over what the controller needs to file; verify compliance (Art. 39).
8. **Implement and evidence a privacy governance programme** (Art. 50 §2) — it is worth −20% on any fine and is a precondition for BCRs; align policies via [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).
9. **Handle data-subject requests** within the statutory clocks (immediate simplified access; 15 days for the full declaration) and record automated-decision review requests; watch the pending rights regulation.
10. **Report to the board** on incident-register trends, request SLAs, transfer-mechanism coverage and ANPD interactions; cooperation is the single biggest determinant of whether a matter becomes a sanctioning process. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **GDPR:** structurally parallel (bases, rights, DPO, records, transfers) but with material differences: ten legal bases including credit protection; a 3-business-day incident clock running to both the regulator and data subjects versus 72 hours to the authority and "without undue delay" to data subjects only where risk is high; a 15-day access deadline versus one month; a R$ 50 million per-infraction fine cap versus 4% of worldwide turnover; no mandatory DPIA trigger yet. Since January 2026 both directions are covered by adequacy, so EU–Brazil intra-group flows no longer need SCCs — but the ANPD decision expressly excludes transfers made solely for public security, defence, State security or criminal prosecution, and the EU decision reaches only recipients subject to the LGPD, which excludes the same purposes. See [gdpr.md](gdpr.md).
- **Other jurisdictions:** the summary row for Brazil in [other-jurisdictions.md](other-jurisdictions.md) is superseded by this pack for detail.
- **ECA Digital (Law 15.211/2025):** adds age assurance, parental supervision and advertising rules for products likely accessed by minors, with the ANPD as enforcer; LGPD Art. 14 consent rules continue to apply alongside it.
- **Sectoral overlays:** Res. 15/2024 preserves shorter or different incident deadlines set in sector-specific legislation, so map those per sector; Art. 52 §2 preserves consumer-law (CDC) sanctions; the LGPD itself amended the Marco Civil da Internet (Law 12.965/2014), whose internet-rights provisions continue to apply alongside it.
- **AI:** Art. 20 automated-decision review and the ANPD's Phase 1 "artificial intelligence" regulatory item are the current hooks. See [eu-ai-act.md](eu-ai-act.md) for the comparator regime and [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).
- **Security frameworks:** Arts. 46–49 are outcome-based; the ANPD has not yet issued minimum technical standards (agenda Phase 1), so ISO 27001 / NIST CSF control sets remain the practical evidence base.

## Primary sources

- Lei nº 13.709/2018 (LGPD), consolidated text with amendment annotations — Planalto: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm (legal text)
- Lei nº 13.853/2019 (created the ANPD) — Planalto: https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/lei/l13853.htm (legal text)
- Lei nº 14.460/2022 (ANPD as special-regime autarchy) — Planalto: https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/L14460.htm (legal text)
- Lei nº 15.352/2026 (ANPD as regulatory agency; ECA Digital commencement) — Planalto: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/L15352.htm (legal text)
- Emenda Constitucional nº 115/2022 — Planalto: https://www.planalto.gov.br/ccivil_03/constituicao/Emendas/Emc/emc115.htm (legal text)
- ANPD normative acts index (all resolutions, status) — https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd (regulator page)
- Res. CD/ANPD 2/2022 (small agents) — https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022 (regulation)
- Res. CD/ANPD 4/2023 (dosimetry and application of administrative sanctions) — DOU: https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-4-de-24-de-fevereiro-de-2023-466146077 (regulation; the numeric appendices are not rendered in the DOU HTML)
- Res. CD/ANPD 15/2024 (security-incident communication) — DOU: https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-15-de-24-de-abril-de-2024-556243024 (regulation); ANPD incident page and FAQ: https://www.gov.br/anpd/pt-br/assuntos/comunicacao-de-incidentes-de-seguranca-cis (regulator guidance)
- Res. CD/ANPD 18/2024 (DPO) — DOU: https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-18-de-16-de-julho-de-2024-572632074 (regulation)
- Res. CD/ANPD 19/2024 (international transfers, SCCs) — https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024 (regulation); ANPD transfer page: https://www.gov.br/anpd/pt-br/assuntos/assuntos-internacionais/transferencia-internacional-de-dados (regulator guidance)
- Res. CD/ANPD 32/2026 (EU adequacy) — DOU: https://www.in.gov.br/web/dou/-/resolucao-n-32-de-26-de-janeiro-de-2026-683334547 (regulation); official English version: https://www.gov.br/anpd/pt-br/centrais-de-conteudo/outros-documentos-e-publicacoes-institucionais/resolucao-no-32-decisao-de-adequacao-uniao-europeia-em-lingua-inglesa.pdf/@@display-file/file
- Commission Implementing Decision (EU) 2026/179 of 26 January 2026 (Brazil adequacy under GDPR Art. 45) — https://eur-lex.europa.eu/eli/dec_impl/2026/179/oj (legal text)
- Res. 23/2024 and Res. CD/ANPD 31/2025 (regulatory agenda 2025–2026) — https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-no-23-de-9-de-dezembro-de-2024 and DOU: https://www.in.gov.br/web/dou/-/resolucao-cd/anpd-n-31-de-22-de-dezembro-de-2025-677950080 (regulator acts)
- ANPD enforcement pages — https://www.gov.br/anpd/pt-br/assuntos/fiscalizacao and https://www.gov.br/anpd/pt-br/assuntos/fiscalizacao-2/saiba-como_fiscalizamos/atividades-fiscalizatorias/ (regulator pages; process lists); sanctions page: https://www.gov.br/anpd/pt-br/acesso-a-informacao/sancoes-administrativas
- Lei nº 15.211/2025 (ECA Digital) — Planalto: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15211.htm (legal text); ANPD ECA Digital page with the implementation timetable: https://www.gov.br/anpd/pt-br/assuntos/eca-digital (regulator guidance)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
