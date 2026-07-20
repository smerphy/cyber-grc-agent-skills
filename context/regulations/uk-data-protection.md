# United Kingdom: Data Protection and Cybersecurity Regime

## At a glance

| Attribute | Detail |
|---|---|
| Core privacy laws | UK GDPR + Data Protection Act 2018 (DPA 2018), as amended by the Data (Use and Access) Act 2025 (DUAA) |
| Cookies/marketing | Privacy and Electronic Communications Regulations 2003 (PECR) — UK implementation of the ePrivacy Directive |
| Cybersecurity laws | NIS Regulations 2018; Telecommunications (Security) Act 2021; Cyber Security and Resilience Bill pending as of mid-2026 (verify status) |
| Financial sector | FCA/PRA operational resilience rules (SYSC 15A / PRA SS1/21); critical third parties regime under FSMA 2023 |
| Regulators | ICO (privacy, PECR, NIS for digital providers); Ofcom (telecoms security); FCA/PRA (financial); sector authorities for NIS OES |
| Breach notification | 72 hours to the ICO (UK GDPR Art. 33); individuals without undue delay if high risk (Art. 34) |
| Maximum fines | UK GDPR: £17.5M or 4% of worldwide annual turnover; lower tier £8.7M or 2%; NIS Regulations: up to £17M; TSA 2021: up to 10% of relevant turnover |
| EU relationship | UK holds EU adequacy (renewed/extended in 2025 following the DUAA — verify current status and expiry) |

## Structure of the privacy regime

Post-Brexit, the UK retained the GDPR as domestic law — the **UK GDPR** — read together with the **DPA 2018**, which supplies exemptions, ICO powers, criminal offences, and separate regimes for law-enforcement and intelligence processing. Substantively, the UK GDPR mirrors the EU GDPR: lawful bases, transparency, data-subject rights, accountability, DPIAs, DPO requirements, processor contracts, and the 72-hour breach clock. An EU-GDPR-compliant program is ~95% of a UK-compliant one; the differences live in transfers, PECR, and the DUAA amendments below.

**Extraterritorial reach** mirrors the EU model: the UK GDPR applies to organizations outside the UK offering goods or services to, or monitoring the behaviour of, individuals in the UK. Non-UK controllers/processors in scope must appoint a **UK representative** (subject to DUAA-era reform proposals — verify whether the representative requirement still stands).

**The ICO** (Information Commissioner's Office) is the single supervisory authority for UK GDPR, PECR, and (for relevant digital service providers) the NIS Regulations. The DUAA restructures it into an **Information Commission** with a board-and-CEO governance model — verify commencement status.

## Data (Use and Access) Act 2025

The DUAA received royal assent on 19 June 2025. It amends — rather than replaces — the UK GDPR, DPA 2018, and PECR. It is an evolution designed to preserve EU adequacy, not a divergence event. Headline reforms (commencement is phased; verify which provisions are in force before relying on them):

- **Recognised legitimate interests:** a new lawful basis for a listed set of processing purposes (e.g., national security, emergencies, crime prevention, safeguarding) without the usual balancing test, plus statutory examples easing ordinary legitimate-interests analysis (direct marketing, intra-group transfers, security of systems).
- **Automated decision-making:** the restrictive Art. 22 model is relaxed for most personal data — significant automated decisions are permitted with safeguards (information, human review, contestation), with the stricter regime retained for special category data.
- **International transfers:** the adequacy-style "data protection test" for Secretary of State regulations and for exporter TRAs becomes a "not materially lower" standard of protection.
- **Data subject requests:** a "reasonable and proportionate search" standard for DSARs and a stop-the-clock mechanism for clarification are codified.
- **PECR changes:** consent exemptions for low-risk purposes (notably first-party statistics/analytics and appearance/functionality cookies, subject to information and opt-out) and — significantly — **PECR fines raised from the legacy £500,000 cap to UK GDPR levels** (£17.5M/4%). Verify commencement of each.
- **Smart data schemes and digital verification services:** frameworks enabling sector data-sharing schemes and certified digital-ID providers.
- **Research provisions:** broadened definitions and consent flexibility for scientific research.

GRC consequence: reassess lawful-basis documentation, DSAR procedures, ADM inventories, and cookie configurations against the amended text as provisions commence — see [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Breach notification

Mirrors the EU: notify the ICO **within 72 hours** of becoming aware of a personal data breach unless it is unlikely to result in a risk to individuals; notify affected individuals **without undue delay** where the risk is high; document all breaches internally regardless of notification. The ICO operates an online reporting portal with a phone route for urgent cases. Telecom providers have a separate, faster PECR breach-notification duty to the ICO (24 hours, per the retained EU rules — verify). A UK-and-EU incident means parallel filings: ICO plus each relevant EU authority — one-stop-shop does not cover the UK. See [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).

## International transfers

- **Inbound from the EU:** the UK benefits from EU adequacy decisions (GDPR and LED), originally granted June 2021 with a four-year sunset. The sunset was extended in 2025 pending the DUAA, and the Commission moved to renew adequacy thereafter — **verify the current decisions' status and expiry date**; loss of adequacy would be a step-change event for EU→UK data flows.
- **Outbound from the UK:** transfers to countries without UK adequacy regulations require a transfer mechanism: the ICO's **International Data Transfer Agreement (IDTA)** or the **UK Addendum** to the EU SCCs (the common choice for organizations already on EU SCCs), plus a **transfer risk assessment (TRA)** — the ICO's TRA tool is more pragmatic than the EDPB's approach, and the DUAA's "not materially lower" test softens it further (verify).
- **UK adequacy regulations** largely track the EU's adequacy list, with additions (e.g., the UK-US Data Bridge as a UK extension to the EU-US Data Privacy Framework).

Dual-regime organizations should run one transfer program with two overlays: EU SCCs + UK Addendum in contracts, and TRA documentation acceptable to both standards.

## PECR (cookies and electronic marketing)

PECR implements the ePrivacy Directive ([./eu-eprivacy.md](./eu-eprivacy.md)) and survives Brexit as free-standing UK law:

- **Cookies/storage-and-access:** consent required for non-essential cookies and similar technologies, to the UK GDPR consent standard; strictly-necessary and transmission exemptions mirror the EU, with DUAA adding low-risk exemptions (analytics, functionality) — verify commencement.
- **Marketing:** opt-in for email/SMS marketing to individual subscribers with the soft-opt-in exception; corporate subscribers (B2B) are treated more permissively than in many EU states; live calls follow TPS/CTPS screening rules.
- **Enforcement:** the ICO actively enforces PECR (marketing fines are its highest-volume enforcement line, historically capped at £500k; DUAA raises the cap to UK GDPR levels — verify). The ICO has also run coordinated cookie-banner compliance sweeps against top UK websites, demanding "reject all" parity.

## NIS Regulations 2018 and the Cyber Security and Resilience Bill

The **NIS Regulations 2018** are the UK's retained implementation of the original 2016 EU NIS Directive. They cover **operators of essential services (OES)** in energy, transport, water, health, and digital infrastructure — designated by sector competent authorities — and **relevant digital service providers (RDSPs)** (online marketplaces, search engines, cloud services) supervised by the ICO. Obligations: appropriate and proportionate security measures (the NCSC **Cyber Assessment Framework (CAF)** is the de facto assessment standard for OES) and incident reporting to the competent authority **without undue delay and within 72 hours**. Penalties reach **£17M**.

The UK did not implement NIS2. Its counterpart is the **Cyber Security and Resilience Bill**, announced in the July 2024 King's Speech and introduced to Parliament in 2025; as of mid-2026 it had not completed passage — **verify current status**. Expected direction (based on government policy statements; verify against the bill text): bringing **managed service providers** and (via secondary legislation) data centres into scope, strengthening incident reporting (a two-stage report with a rapid initial notification, reportedly 24 hours, plus ransomware/ransom-payment reporting proposals), stronger regulator powers and cost-recovery, and delegated powers to update scope without new primary legislation. Organizations in MSP, cloud, and critical-supply roles should gap-assess against the CAF now rather than waiting for commencement — see [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).

## Financial sector: operational resilience and critical third parties

- **FCA/PRA operational resilience regime** (FCA PS21/3, PRA SS1/21; in force March 2022 with full compliance by 31 March 2025): in-scope firms must identify **important business services**, set **impact tolerances** (maximum tolerable disruption), map dependencies (people, processes, technology, facilities, third parties), run severe-but-plausible scenario testing, and demonstrate the ability to remain within tolerances. Board-approved self-assessment required. Conceptually parallel to DORA ([./dora.md](./dora.md)) but principles-based rather than prescriptive; dual-regulated EU/UK firms should build one resilience program mapped to both.
- **Critical third parties (CTP) regime** (FSMA 2023; PS16/24 rules effective January 2025): HM Treasury can designate third parties (notably cloud providers) critical to the sector; designated CTPs face direct FCA/PRA/Bank of England oversight, resilience requirements, and incident-reporting duties — regulation of the vendor, not just the firm.
- Firms also owe **material outsourcing** notifications and operational incident reporting to the FCA/PRA under existing rules (incident-reporting rules were being formalised in the mid-2020s — verify current requirements).

## Telecoms security

The **Telecommunications (Security) Act 2021** and its secondary legislation (Electronic Communications (Security Measures) Regulations 2022 plus a Telecommunications Security Code of Practice) impose tiered, detailed security duties on public telecoms providers — asset management, supply-chain controls (including high-risk-vendor restrictions), privileged access, monitoring, and incident reporting to **Ofcom**. Penalties reach **10% of relevant turnover** (or £100,000/day for continuing failures). Tier deadlines phased through the mid-2020s.

## Key obligations for security/GRC teams

1. **Run UK GDPR as an overlay on the EU program, not a copy**: separate ICO breach-reporting runbook (72h), UK representative check, UK Addendum/IDTA in transfer paperwork, and a DUAA commencement tracker feeding change into lawful-basis records, ADM registers, and DSAR SOPs. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Treat adequacy as a monitored dependency**: EU→UK flows ride on the EU adequacy decisions; log it as a risk with a contingency (SCCs ready to deploy) rather than an assumption.
3. **Cookie and marketing compliance per PECR**, including "reject all" parity and — once commenced — the DUAA's analytics exemption and the raised fine ceiling, which changes PECR risk economics materially.
4. **If an OES/RDSP (or a likely CSRB target — MSPs, data centres):** assess against the NCSC CAF, wire the 72-hour NIS notification into incident response, and track the Cyber Security and Resilience Bill through commencement.
5. **Financial firms:** maintain the operational-resilience self-assessment (important business services, impact tolerances, scenario tests) as living governance, and map third-party dependencies for CTP-regime exposure. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
6. **One incident, many clocks:** a UK breach can trigger ICO (72h), NIS (72h), FCA/PRA notification, Ofcom (telecoms), and parallel EU filings. Pre-map recipients and thresholds — see [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).

## Interplay

- **EU GDPR:** near-identical substance; dual compliance is mostly duplicated filings and transfer paperwork, but divergence is now real and growing via the DUAA — track deltas rather than assuming equivalence. UK-only conduct is outside the EU one-stop-shop and vice versa. See [./gdpr.md](./gdpr.md).
- **ePrivacy Directive:** PECR is the UK sibling; a pan-European cookie program needs the UK as a distinct variant (its exemptions now differ). See [./eu-eprivacy.md](./eu-eprivacy.md).
- **NIS2:** the UK regime lags NIS2 in scope and penalties until the Cyber Security and Resilience Bill lands; groups operating in both jurisdictions should build to NIS2 as the high-water mark and treat UK NIS as a subset. See [./nis2.md](./nis2.md).
- **DORA:** UK operational resilience + CTP regime is the UK's functional equivalent; dual-regulated financial groups should maintain a single mapped control set. See [./dora.md](./dora.md).
- **EU AI Act:** the UK has no AI Act equivalent (a principles-based, regulator-led approach, with targeted legislation repeatedly signalled — verify status); UK AI governance currently hangs off UK GDPR (ADM rules) and sector regulators. See [./eu-ai-act.md](./eu-ai-act.md).

## Primary sources

- [Data Protection Act 2018 — legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2018/12)
- [ICO (UK GDPR guidance, PECR, breach reporting portal)](https://ico.org.uk)
- [NCSC (CAF, security guidance)](https://www.ncsc.gov.uk)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
