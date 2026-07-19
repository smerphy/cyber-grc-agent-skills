# Other Jurisdictions: UK, Australia, Canada, Singapore, Brazil, China, Japan, India

Concise practitioner summaries for regimes outside the EU/US deep-dive files. For the EU, see [gdpr.md](gdpr.md), [nis2.md](nis2.md), [dora.md](dora.md), [eu-ai-act.md](eu-ai-act.md); for the US, see [us-state-privacy.md](us-state-privacy.md), [hipaa.md](hipaa.md), [glba-ftc-safeguards.md](glba-ftc-safeguards.md), [sec-cyber-disclosure.md](sec-cyber-disclosure.md). Deadline comparisons across all regimes: [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).

## At a glance

| Jurisdiction | Core law(s) | Regulator | Headline breach clock |
|---|---|---|---|
| UK | UK GDPR + DPA 2018; NIS Regulations 2018 | ICO (privacy/NIS for digital); sector authorities | 72 hours to ICO |
| Australia | Privacy Act 1988 (NDB scheme); APRA CPS 234; SOCI Act | OAIC; APRA; Dept. Home Affairs/ACSC | 30-day assessment then notify ASAP; APRA 72h; SOCI 12h/72h |
| Canada | PIPEDA; Quebec Law 25 | OPC (federal); CAI (Quebec) | "As soon as feasible" on real risk of significant harm |
| Singapore | PDPA; MAS TRM/notices; Cybersecurity Act | PDPC; MAS; CSA | 3 days to PDPC after determining notifiable; MAS 1 hour |
| Brazil | LGPD | ANPD | 3 business days to ANPD (2024 regulation) |
| China | PIPL + DSL + CSL | CAC (lead) | Prompt notification; localization + transfer approvals |
| Japan | APPI | PPC | Prompt initial report; final within 30 days (60 if malicious) |
| India | DPDP Act 2023; CERT-In directions | Data Protection Board; CERT-In (MeitY) | CERT-In 6 hours; DPDP rules: notify without delay, details to Board within 72h |

## United Kingdom

**Who it covers.** UK GDPR + Data Protection Act 2018 apply to organizations processing personal data of individuals in the UK, with extraterritorial reach mirroring EU GDPR (offering goods/services to, or monitoring, people in the UK). The NIS Regulations 2018 (the UK's retained implementation of the original EU NIS Directive) cover operators of essential services (energy, transport, water, health, digital infrastructure) and relevant digital service providers.

**Core obligations.**
- Substantively parallel to EU GDPR: lawful basis, security of processing, DPIAs, DPO where required, international transfer rules (UK adequacy decisions, the ICO's International Data Transfer Agreement (IDTA) or UK Addendum to EU SCCs).
- Personal data breach: notify the ICO within **72 hours** of awareness unless unlikely to risk individuals' rights; notify individuals without undue delay if high risk. Fines up to **£17.5m or 4% of global annual turnover**.
- NIS Regulations: appropriate and proportionate security measures; incident reporting to the competent authority (sector regulators for OES; ICO for digital service providers), generally within 72 hours of awareness.
- The **Cyber Security and Resilience Bill** — announced to modernize the NIS Regulations (expanding scope to managed service providers, strengthening incident reporting, giving regulators more powers) — is **evolving legislation**; track its passage and final text before relying on specifics. The Data (Use and Access) Act 2025 also adjusted parts of the UK data protection regime; verify current state.
- Sectoral overlays: FCA/PRA operational resilience rules for financial firms (important business services, impact tolerances); NCSC publishes the de facto national security guidance (Cyber Assessment Framework, Cyber Essentials).

**Regulators.** ICO (data protection, DSP incidents); sector competent authorities under NIS; FCA/PRA for financial services; NCSC as technical authority (non-regulatory).

## Australia

**Who it covers.** The Privacy Act 1988 applies to Australian government agencies and private organizations with annual turnover above A$3m (plus some smaller entities, e.g., health providers) — the small-business exemption is under reform review. APRA CPS 234 binds all APRA-regulated entities (banks, insurers, superannuation trustees). The Security of Critical Infrastructure (SOCI) Act 2018 (as amended 2021–22) covers 11 critical infrastructure sectors from energy and water to data storage/processing, food, and higher education.

**Core obligations.**
- **Notifiable Data Breaches (NDB) scheme:** for an "eligible data breach" (unauthorized access/disclosure/loss likely to result in **serious harm** to individuals), notify the OAIC and affected individuals **as soon as practicable**; if it is unclear whether a breach is eligible, complete an assessment within **30 days**. Penalties for serious/repeated privacy interferences: the greater of **A$50m**, 3× the benefit obtained, or 30% of adjusted turnover in the period.
- **APRA CPS 234** (information security): board is ultimately responsible; maintain security capability commensurate with threats; classify information assets; test controls systematically; assess third parties managing your assets; notify APRA within **72 hours** of a material information security incident and within **10 business days** of identifying a material control weakness that cannot be remediated in a timely manner. CPS 230 (operational risk management, effective mid-2025) adds service-provider and operational-resilience requirements on top.
- **SOCI Act:** register critical infrastructure assets; adopt and annually attest a Critical Infrastructure Risk Management Program (CIRMP, including a cyber framework such as ISO 27001, NIST CSF, or the ACSC Essential Eight); mandatory cyber incident reporting to the ACSC — **12 hours** for incidents with significant impact on the asset, **72 hours** for other relevant incidents; government assistance/intervention powers ("step-in") for serious incidents; enhanced obligations for declared Systems of National Significance.

**Regulators.** OAIC (privacy/NDB); APRA (CPS 234/230); Department of Home Affairs and the Cyber and Infrastructure Security Centre, with ACSC as incident recipient (SOCI).

## Canada

**Who it covers.** PIPEDA applies to private-sector organizations handling personal information in commercial activities across Canada, except in provinces with substantially similar laws (Quebec, Alberta, BC) for intra-provincial matters — federal works and cross-border flows remain PIPEDA. Quebec's Law 25 (modernizing the Quebec private-sector act, fully phased in by 2023–24) applies to any enterprise processing Quebec residents' personal information.

**Core obligations.**
- **PIPEDA breach rules (since 2018):** on a breach of security safeguards creating a **real risk of significant harm (RROSH)**, report to the Office of the Privacy Commissioner and notify affected individuals **as soon as feasible**; notify other organizations/government bodies that can mitigate harm; keep records of **all** breaches (RROSH or not) for **24 months**. Knowing failure to report/notify/record is an offence (fines up to C$100,000).
- Security principle: safeguards appropriate to sensitivity (Schedule 1, Principle 7). Federal reform (successor bills to CPPA) remains pending — treat as evolving.
- **Quebec Law 25:** designate a person in charge of personal information protection (default: CEO); conduct privacy impact assessments for projects involving personal information and for transfers outside Quebec; notify the CAI and affected persons of **confidentiality incidents presenting a risk of serious injury**, and keep an incident register; consent and transparency rules stricter than PIPEDA; administrative monetary penalties up to **C$10m or 2% of worldwide turnover**, and penal fines up to **C$25m or 4% of worldwide turnover**; a private right of action exists.

**Regulators.** OPC (federal); Commission d'accès à l'information (CAI) in Quebec; OIPC Alberta/BC for provincial laws (both with their own breach-notification rules — Alberta's is mandatory).

## Singapore

**Who it covers.** The Personal Data Protection Act (PDPA) applies to all private-sector organizations processing personal data in Singapore, regardless of size or location of the organization. Financial institutions additionally answer to MAS; owners of designated Critical Information Infrastructure (CII) fall under the Cybersecurity Act 2018 (amended 2025 to extend to key digital infrastructure and supply-chain aspects — verify current scope).

**Core obligations.**
- **PDPA breach notification (since Feb 2021):** assess suspected breaches expeditiously (PDPC guidance: generally within **30 days**); a breach is notifiable if it (a) is likely to result in **significant harm** (prescribed categories: financial data, identification numbers, health data, etc.) or (b) is of **significant scale** (**500 or more** individuals). Notify the PDPC **within 3 calendar days** of determining a breach is notifiable; notify affected individuals contemporaneously where significant harm is likely (exceptions for law-enforcement requests and remedial-action/technological-protection cases). Financial penalties up to **10% of Singapore annual turnover** (for turnover above S$10m) or S$1m.
- Protection obligation: reasonable security arrangements; appoint a DPO (mandatory).
- **MAS**: Technology Risk Management Guidelines (2021) set supervisory expectations (governance, secure SDLC, cyber ops, third parties); the MAS Notices on Technology Risk Management require regulated FIs to notify MAS **within 1 hour** of discovering a relevant IT security incident or major system malfunction, with a root-cause and impact report within **14 days**; outsourcing/third-party guidelines apply to material arrangements.
- **Cybersecurity Act:** CII owners must comply with codes of practice, conduct audits and risk assessments, report prescribed cybersecurity incidents to the Commissioner of Cybersecurity (CSA) — reporting windows are short (hours, per subsidiary requirements).

**Regulators.** PDPC (personal data); MAS (financial); Cyber Security Agency of Singapore (CSA) for CII.

## Brazil

**Who it covers.** The Lei Geral de Proteção de Dados (LGPD, Law 13,709/2018, in force since 2020) applies to any processing of personal data carried out in Brazil, for offering goods/services to individuals in Brazil, or of data collected in Brazil — extraterritorial reach comparable to GDPR.

**Core obligations.**
- GDPR-family structure: legal bases (ten, including legitimate interest), data subject rights, DPO ("encarregado") appointment expected for most controllers, records of processing, international transfer mechanisms (ANPD-approved SCCs since 2024).
- Security: adopt technical and administrative measures able to protect personal data (Arts. 46–49); ANPD has published minimum-security guidance for small processing agents.
- **Incident notification:** notify the ANPD and affected data subjects of security incidents that may cause **relevant risk or damage** to data subjects. ANPD's incident-reporting regulation (2024) sets the deadline at **3 business days** from knowledge of the incident, with prescribed content and an incident register requirement; late or incomplete filings can be supplemented but attract scrutiny.
- Sanctions: warnings, daily fines, blocking/deletion of data, and fines up to **2% of the group's revenue in Brazil**, capped at **R$50m per infraction**; publicization of the infraction is itself a sanction.

**Regulator.** Autoridade Nacional de Proteção de Dados (ANPD); sectoral overlays from the Central Bank (cyber rules for financial institutions) and others.

## China

**Who it covers.** Three interlocking laws: the Cybersecurity Law (CSL, 2017) — network operators and Critical Information Infrastructure Operators (CIIOs); the Data Security Law (DSL, 2021) — all data processing, with a tiered "important data" / "core data" classification; the Personal Information Protection Law (PIPL, 2021) — personal information processing, with extraterritorial reach (offering products/services to, or analyzing behavior of, individuals in China).

**Core obligations.**
- **Localization and cross-border transfer:** CIIOs, and processors above volume thresholds, must store personal information and important data collected in China domestically; cross-border transfers require one of: a **CAC security assessment** (mandatory for CIIOs, important data, and large-volume transfers), filing of the **CAC standard contract**, or **PIPL certification**. 2024 provisions relaxed thresholds and exempted several routine scenarios (e.g., transfers necessary for a contract with the individual, low-volume transfers, and transfers within Free Trade Zone negative-list regimes) — check current thresholds before designing data flows.
- **Security program:** Multi-Level Protection Scheme (MLPS 2.0) grading and certification of systems; DSL requires data classification, risk monitoring, and remediation; PIPL requires appropriate technical measures, personal information protection impact assessments (PIPIAs) for sensitive processing, cross-border transfers, and automated decision-making, and a designated protection officer/local representative in defined cases.
- **Incidents:** on a personal information breach, take remedial measures and **promptly notify** authorities and affected individuals (individual notice can be waived if measures effectively avoid harm — but regulators can order it). Draft/finalized national incident-reporting measures push severe-incident reporting to very short windows (hours) — verify current status. DSL and CSL add incident reporting for important data and CII events.
- Penalties (PIPL): up to **RMB 50m or 5% of the previous year's turnover** for grave violations, plus personal fines and disqualification for responsible individuals; DSL adds separate penalties, including severe ones for unauthorized provision of data to foreign judicial/law-enforcement bodies (a blocking-statute effect — route foreign data demands through legal counsel).

**Regulators.** Cyberspace Administration of China (CAC, lead); Ministry of Public Security (MLPS); Ministry of Industry and Information Technology; sector regulators.

## Japan

**Who it covers.** The Act on the Protection of Personal Information (APPI) applies to all business operators handling personal information, regardless of size, including foreign operators processing Japanese data subjects' information in connection with offering goods/services in Japan.

**Core obligations.**
- Security control measures proportionate to risk (organizational, human, physical, technical — detailed in PPC guidelines); supervision of employees and contractors.
- **Breach reporting (mandatory since the 2022-effective amendments)** for four incident classes: sensitive ("special care-required") personal information; risk of financial harm (e.g., payment card data); incidents likely involving unlawful intent (cyberattacks); or affecting **more than 1,000 individuals**. Two-stage reporting to the PPC: a **prompt initial report** (PPC guidance: within about 3–5 days of awareness) and a **final report within 30 days** (**60 days** for incidents involving unlawful intent). Affected individuals must also be notified.
- Cross-border transfers: consent, adequacy (the EU and UK hold mutual adequacy with Japan), or safeguards with information provision to the data subject about the destination country's regime; onward-transfer diligence obligations.
- Pseudonymized/anonymized information categories carry distinct, lighter regimes — useful for analytics designs.
- Penalties are modest by global standards (corporate fines up to ¥100m for certain violations; PPC orders and publication are the sharper tools). The APPI undergoes a statutory review every three years — expect incremental change.

**Regulator.** Personal Information Protection Commission (PPC); FSA overlays for financial institutions.

## India

**Who it covers.** The Digital Personal Data Protection (DPDP) Act 2023 applies to processing of digital personal data in India, and abroad where connected to offering goods/services to data principals in India. Implementation arrives through the DPDP Rules (notified 2025, with **phased implementation over roughly the following 18 months**) — treat operative dates as evolving and verify what is currently in force. Separately, CERT-In's 2022 directions under the IT Act apply now to virtually all service providers, intermediaries, and companies operating in India.

**Core obligations.**
- **DPDP Act:** consent-centric regime (consent or defined "legitimate uses"); data fiduciaries must implement **reasonable security safeguards**; notify the **Data Protection Board of India and each affected data principal** of any personal data breach — the Act itself sets **no harm threshold**, making Indian breach notification unusually broad. The Rules prescribe notice to affected individuals without delay and a detailed report to the Board **within 72 hours** (extendable on request). "Significant Data Fiduciaries" (designated by government) face added duties: DPO in India, independent data audits, and periodic DPIAs. Penalties: up to **₹250 crore** (~US$30m) per instance for failure to maintain security safeguards; up to ₹200 crore for breach-notification failures.
- **CERT-In directions (2022):** report specified cyber incidents (a 20-item list including data breaches, ransomware, identity theft, attacks on critical systems) to CERT-In **within 6 hours** of noticing; maintain logs for 180 days within India; sync clocks to NTP servers; VPN/cloud/data-center providers must retain customer records for 5 years. The 6-hour clock is among the world's tightest — build it into IR playbooks for India operations.
- Sectoral overlays: RBI cyber security framework and outsourcing directions for banks/NBFCs (RBI incident reporting within 6 hours), SEBI cybersecurity framework for market participants, IRDAI for insurers.

**Regulators.** Data Protection Board of India (adjudication under DPDP); MeitY/CERT-In (incident reporting); RBI/SEBI/IRDAI sectorally.

## Key obligations for security/GRC teams

1. Determine applicability per jurisdiction by data subjects served, establishment, sector, and infrastructure designation — not by headquarters location (see [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md)).
2. Build a single breach-clock matrix covering every applicable regime; the binding constraint is usually the shortest sectoral clock (MAS 1 hour, CERT-In 6 hours, SOCI 12 hours), not the privacy law (see [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md)).
3. Map data flows for localization and transfer-mechanism obligations (China first, then Quebec/India/Brazil transfer rules) before architecting cross-border systems.
4. Track evolving instruments explicitly: UK Cyber Security and Resilience Bill, Canadian federal privacy reform, India DPDP Rules phase-in, China incident-reporting measures (see [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md)).
5. For financial-sector entities, treat APRA CPS 234, MAS TRM, RBI, and local equivalents as the operative control baselines — they are examined, prescriptive, and carry the shortest reporting windows.
6. Localize IR playbooks: regulator contact points, report templates, and language requirements per jurisdiction, rehearsed in tabletops.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
