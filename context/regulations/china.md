# China: PIPL, DSL, and CSL

China regulates data through three interlocking statutes rather than one omnibus law: the **Cybersecurity Law (CSL, 2017)** governs networks and critical information infrastructure; the **Data Security Law (DSL, 2021)** governs all data — personal or not — through a national classification scheme; the **Personal Information Protection Law (PIPL, 2021)** is the GDPR-analogue for personal information. A dense layer of implementing measures, national standards (GB/T series), and Cyberspace Administration of China (CAC) provisions fills in the operational detail — and changes faster than the statutes. Treat the triad as one compliance program, not three.

## At a glance

| Item | Detail |
|---|---|
| Jurisdiction | Mainland China (Hong Kong, Macau, Taiwan have separate regimes); PIPL reaches processing outside China to provide products/services to, or analyze/assess the behavior of, natural persons in China |
| In force since | CSL 2017-06-01; DSL 2021-09-01; PIPL 2021-11-01 |
| Regulators | CAC (lead coordinator, cross-border transfers, enforcement); Ministry of Public Security (MLPS, cybercrime); MIIT (telecom/industrial data); sector regulators (PBOC/NFRA finance, NHC health, etc.) |
| Max penalties | PIPL: up to RMB 50M or 5% of the preceding year's turnover for grave violations, plus business suspension/shutdown, app removal, and personal fines (up to RMB 1M) and disqualification for responsible individuals. DSL and CSL carry separate penalty ladders |
| Who's covered | CSL: "network operators" (effectively any organization operating IT systems in China) plus designated CIIOs; DSL: all data processing in China (extraterritorial where activities harm China's national security/public interest); PIPL: personal information processors (controller-equivalent) in China and abroad per the reach above |
| Private right of action | Yes — PIPL Art. 69 civil claims with a reversed burden of proof (processor must prove no fault); public-interest litigation by procuratorates and consumer associations is an active channel |

## The three laws and how they divide the field

### CSL — networks, CIIOs, MLPS

- Applies to **network operators** broadly: security protection duties, incident response plans, real-name requirements, cooperation with authorities.
- **CIIO designation.** Operators of critical information infrastructure — energy, transport, water, finance, public services, e-government, defense-related, and other systems whose incapacitation would seriously harm national security or public welfare — are designated by sector "protection departments" under the 2021 CII Security Protection Regulations. Designation is not always public; many companies learn of it by notification.
- CIIO status triggers: domestic storage (localization), mandatory CAC security assessment for any cross-border transfer, national-security review of network product/service procurement, and enhanced protection obligations.
- **MLPS 2.0** (Multi-Level Protection Scheme): grade systems 1–5 by the harm a compromise would cause, file the grading with the Ministry of Public Security (level 2+), implement the corresponding GB/T 22239 control baseline, and undergo periodic expert evaluation (annual at level 3+, where most systems handling important data or large-volume personal information land). MLPS is the closest thing China has to a mandatory baseline security framework, and Chinese enterprise customers routinely ask for MLPS evidence.

### DSL — data classification and national security

- All data is classified in a national catalog system:
  - **General data** — default tier.
  - **Important data** — data that, if tampered with, destroyed, leaked, or illegally used, may endanger national security, economic operation, social stability, or public health and safety. Catalogs are issued sector by sector and region by region and remain incomplete; automotive, industrial, and mapping/geographic data have concrete rules, many sectors do not.
  - **National core data** — the top tier, relating to national security and the lifeline of the economy; strictest controls and heaviest penalties.
- Processors of important data must: designate a responsible person and management body, conduct periodic risk assessments and file reports with regulators, and obtain a CAC security assessment before any transfer abroad.
- **Blocking provision (DSL Art. 36; mirrored in PIPL Art. 41):** providing data stored in China to foreign judicial or law-enforcement authorities without Chinese government approval is prohibited. Route foreign discovery requests, subpoenas, and regulator demands through legal counsel before responding.

### PIPL — personal information

- GDPR-family structure: lawful bases, data subject rights (access, copy, correction, deletion, portability in defined cases, explanation of automated decisions), vendor ("entrusted party") contracts, joint processing arrangements.
- Designated **personal information protection officer** required for processors above a CAC-set volume threshold; extraterritorial processors must establish a dedicated entity or appoint a representative in China and file its contact details.

## PIPL: where it diverges from GDPR

- **No legitimate-interests basis.** PIPL's lawful bases (Art. 13) are consent, contract necessity, HR management under labor rules and lawful policies, statutory duties, public health/emergencies, news reporting/public-interest supervision within reason, and lawfully self-disclosed or otherwise lawfully published data. Marketing, analytics, and most secondary uses therefore ride on consent — consent does far more work than under GDPR.
- **Separate consent is its own tier.** Beyond ordinary consent, a distinct, specific, unbundled affirmation — not buried in a general privacy-notice acceptance — is required for:
  - providing personal information to another processor;
  - public disclosure;
  - processing **sensitive personal information**;
  - cross-border transfers;
  - use of images/identification data collected by public-area equipment for purposes beyond public security.
- **Sensitive personal information (Arts. 28–32):** information that, if leaked or misused, could easily harm dignity or personal/property safety — biometrics, religious beliefs, specific identity, medical/health, financial accounts, location tracking, and any personal information of minors under 14. Requires a specific purpose, sufficient necessity, separate consent, enhanced notice, and a prior impact assessment. Minors' data additionally needs guardian consent and dedicated processing rules.
- **PIPIA — personal information protection impact assessment (Arts. 55–56).** Mandatory before:
  - processing sensitive personal information;
  - automated decision-making using personal information;
  - entrusting processing to a vendor, providing personal information to another processor, or public disclosure;
  - cross-border transfers;
  - other activities with major impact on individuals.
  Content parallels a DPIA: legality/necessity of purpose and means, risks to individuals, effectiveness of protective measures. Reports must be retained at least three years. The PIPIA is the single most-reused artifact in a China program — build one template and trigger list, and reuse it as the filing artifact for the standard-contract transfer route.
- **Automated decision-making (Art. 24):** decisions must be transparent and fair, without unreasonable differential treatment on price or terms ("big data price discrimination"); push marketing via automated decision-making needs a non-personalized option or a convenient way to refuse.

## Breach and incident duties

- **PIPL Art. 57:** where a leak, tampering, or loss of personal information occurs or may occur, the processor must **immediately take remedial measures and notify** the performing regulator and affected individuals. Notice content: affected categories, causes, possible harm, remedial measures taken, mitigation steps individuals can take, and contact information.
- Individual notice may be waived where the measures taken can effectively avoid harm — but the regulator can order notification anyway.
- **Timelines sit in measures, not the statute.** The statute says "immediately"; concrete hour-counts appear in implementing instruments — the Network Data Security Management Regulations and national cyber incident-reporting measures have pushed reporting for serious incidents toward very short windows (on the order of hours). These instruments have been in flux; verify the currently effective reporting rules and sector overlays (e.g., financial regulators) before committing hard numbers to a playbook.
- **CSL/DSL overlays:** network operators must maintain incident response plans and report incidents threatening network security; important-data incidents carry their own reporting duties. A single intrusion can trigger PIPL, DSL important-data, and CSL/MLPS reporting simultaneously.

## Cross-border transfers and localization

Three legal routes for exporting personal information from mainland China (PIPL Art. 38 plus CAC measures):

| Route | When required/used | Mechanics |
|---|---|---|
| CAC security assessment | Mandatory for CIIOs (any personal information), important data (always), and processors above volume thresholds | Government review of purpose, scope, necessity, and destination risk; approvals are time-limited and transfer-specific |
| Standard contract filing | Default route for mid-volume transfers below assessment thresholds | Execute the CAC standard contractual clauses with the overseas recipient, conduct a PIPIA, file both with the provincial CAC |
| Certification | Mainly intra-group arrangements and some extraterritorial processors | Personal information protection certification by an accredited body |

- The **March 2024 Provisions on Promoting and Regulating Cross-Border Data Flows** materially eased the regime: exemptions for transfers necessary to perform a contract with the individual (cross-border e-commerce, travel, payments, visa processing), necessary cross-border HR management, emergencies, and low-volume transfers below revised thresholds; raised volume thresholds before the security-assessment route becomes mandatory; and **Free Trade Zone "negative lists"** under which data not on a zone's list can flow freely from that zone.
- The specific headcount thresholds vary by scenario (sensitive vs. non-sensitive personal information, cumulative counts over a look-back period) and have shifted with these provisions — verify current thresholds and any applicable FTZ negative list before designing data flows; do not hardcode numbers from secondary sources.
- **Localization:** CIIOs must store personal information and important data collected/generated in China domestically (CSL Art. 37); important data generally cannot leave China without a security assessment regardless of who holds it. **Remote access from outside China to data stored in China is treated as a transfer** — global SaaS admin consoles, follow-the-sun support, and centralized HR systems all count.

## Enforcement pattern

- **Didi (2022):** RMB 8.026 billion fine (roughly 4–5% of revenue) under CSL, DSL, and PIPL for large-scale excessive collection and processing violations, plus RMB 1M personal fines on the CEO and president. The case followed a cybersecurity review triggered by Didi's US IPO and established that listing abroad while holding large China data sets invites scrutiny.
- Routine enforcement runs through **app-focused sweeps**: batch orders against apps for excessive permission requests, missing privacy notices, and consent failures, escalating from rectification orders to app-store removal.
- **Cybersecurity review** powers (CIIO procurement of network products/services; data-processing activities affecting national security, including foreign listings by large data processors) can suspend business activity — often a sharper deterrent than fines.
- Public-interest litigation plus the Art. 69 reversed burden of proof give the civil channel real teeth in consumer-facing cases.

## Program shape for multinationals

A workable sequencing for a multinational building China compliance:

1. **Scope** — confirm PIPL/DSL/CSL applicability (China entity, China users, China-hosted systems, China employees) using a structured applicability analysis ([../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md)).
2. **Inventory and classify** — data mapping with China-specific tags: personal vs. sensitive personal information, important-data screening, storage location, and every cross-border access path.
3. **Legalize the flows** — select and execute transfer routes per flow; remediate or ring-fence flows that cannot be legalized (common outcome: a segregated China instance for HR or CRM data).
4. **Certify the systems** — MLPS grading and evaluation for China-hosted systems; align control evidence with the GB/T 22239 baseline.
5. **Operationalize** — separate-consent UX, PIPIA pipeline, incident tree, foreign-request gate, and the appointed roles. Chinese-language notices and regulator filings are required; budget for local counsel on filings.

## Key obligations for security/GRC teams

1. **Map China-touching data flows first.** What is collected or generated in China, where it is stored, and who accesses it from abroad (support teams, global SaaS, HR/CRM systems) — remote access counts as a transfer. This map determines which transfer route, if any, you need.
2. **Determine CIIO exposure and MLPS grading.** Check with sector regulators/local counsel whether any system could be designated CII; file MLPS grading for level 2+ systems and complete level-appropriate evaluation.
3. **Screen for important data** against published sectoral/regional catalogs; where catalogs are silent, document the screening rationale. A positive finding means: responsible person, periodic filed risk assessments, no export without CAC assessment.
4. **Operationalize separate consent** — distinct UI affirmations for sensitive data, third-party sharing, public disclosure, and cross-border transfer. A bundled "I agree" fails. Keep consent records retrievable per individual.
5. **Run the PIPIA pipeline** against the Art. 55 trigger list; retain reports 3+ years.
6. **Pick and maintain a transfer route per flow** (assessment, standard contract filing, certification, or a 2024 exemption/FTZ negative list), with an annual re-check — thresholds and exemptions have moved and may move again.
7. **Build the incident playbook for "immediate":** remedial-measures-first sequencing, regulator and individual notice templates in Chinese, and one escalation tree covering PIPL, DSL important-data, CSL/MLPS, and sector-regulator reporting. See [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
8. **Gate foreign government data demands.** Put a legal-review checkpoint in front of e-discovery, subpoenas, and foreign-regulator requests touching China-stored data (DSL Art. 36 / PIPL Art. 41).
9. **Appoint the required roles:** personal information protection officer (above threshold), important-data responsible person, and a China representative/entity for extraterritorial processors; report contact details to the regulator.
10. **Localize vendor diligence:** entrusted-processing agreements with PIPL-required terms, MLPS status of China-hosted infrastructure providers, and sub-entrustment controls — see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).

## Interplay

- **Versus [GDPR](./gdpr.md):** PIPL borrows the structure — lawful bases, rights, impact assessments, extraterritoriality, turnover-based fines — but diverges where it matters operationally:
  - no legitimate-interests basis (consent does far more work);
  - the separate-consent tier with prescribed triggers;
  - national-security framing throughout, with the DSL classification layer sitting on top of all data, not just personal data;
  - government-approval or government-filed transfer routes instead of self-assessed SCCs, plus hard localization for CIIOs and important data;
  - the blocking provision on foreign law-enforcement disclosure, which has no GDPR equivalent (GDPR Art. 48 is a softer analogue).
  A GDPR program is a useful chassis but is not sufficient — the classification and transfer layers need China-specific build-out.
- GDPR and PIPL can apply to the same processing (an EU company serving China users, or vice versa); apply the stricter rule per element. China holds no EU adequacy decision — EU-to-China transfers need SCCs plus a transfer impact assessment, while China-to-anywhere transfers need a PIPL route.
- Sector overlays (PBOC/NFRA financial data rules, health, automotive, mapping) add localization and reporting on top of the triad.
- Regional program parallels: [japan.md](japan.md), [south-korea.md](south-korea.md), [singapore.md](singapore.md), [india-dpdp.md](india-dpdp.md).

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
