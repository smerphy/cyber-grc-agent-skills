# DORA — Digital Operational Resilience Act (EU 2022/2554)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Regulation (EU) 2022/2554 — directly applicable, no national transposition needed |
| Entered into force | 16 January 2023 |
| Applied from | 17 January 2025 |
| Who is covered | ~20 categories of financial entities plus ICT third-party service providers (via contractual pass-through and, for critical providers, direct ESA oversight) |
| Structure | Five pillars: ICT risk management, incident management/reporting, resilience testing, third-party risk, information sharing |
| Detail layer | RTS/ITS technical standards adopted by the Commission on ESA drafts — much operational detail (incident thresholds, report timelines, register format, TLPT mechanics) lives there, not in the level-1 text |
| Testing | Digital operational resilience testing program; threat-led penetration testing (TLPT) at least every 3 years for designated entities |
| Supervisors | National financial supervisors; the three ESAs (EBA, ESMA, EIOPA); Lead Overseer regime for critical ICT third-party providers |
| Lex specialis | Displaces NIS2's ICT risk-management and incident-reporting provisions for in-scope financial entities |

## What it is

DORA harmonizes how the EU financial sector manages ICT risk. Before DORA, operational-resilience expectations were scattered across sectoral guidelines (EBA outsourcing and ICT guidelines, EIOPA/ESMA equivalents); DORA consolidates them into one directly applicable regulation with a common vocabulary, common incident taxonomy, and — uniquely — a direct EU oversight regime for the largest technology providers to the financial sector.

**Proportionality** runs through the whole act: measures scale with the entity's size, risk profile, and the nature/complexity of services. Microenterprises and certain small entities apply a **simplified ICT risk-management framework** (Art. 16); some entity types are excluded outright under Art. 2(3) (check the exclusion list — it includes, e.g., certain small IORPs and insurance intermediaries).

## Scope

In-scope **financial entities** (Art. 2) span roughly 20 categories, including:

- Credit institutions (banks)
- Payment institutions and account information service providers
- Electronic money institutions
- Investment firms
- Crypto-asset service providers and issuers of asset-referenced tokens (MiCA-linked)
- Central securities depositories; central counterparties; trading venues; trade repositories
- Managers of alternative investment funds; UCITS management companies
- Data reporting service providers
- Insurance and reinsurance undertakings; insurance, reinsurance and ancillary insurance intermediaries
- Institutions for occupational retirement provision (IORPs)
- Credit rating agencies; administrators of critical benchmarks
- Crowdfunding service providers; securitisation repositories

**ICT third-party service providers** are pulled in two ways: indirectly, through mandatory contractual provisions and register/concentration requirements imposed on their financial-entity customers; and directly, if designated a **critical ICT third-party provider (CTPP)** subject to ESA oversight (see Pillar 4).

## The five pillars

### 1. ICT risk-management framework (Arts. 5–16)

- **Management body owns it** (Art. 5): defines, approves, oversees, and is accountable for the framework; members must maintain sufficient ICT-risk knowledge, including through regular training.
- A documented, comprehensive framework (Art. 6) reviewed at least annually and on major incidents, covering identification, protection and prevention, detection, response and recovery, backup and restoration, learning and evolving, and communication.
- Requirements track a full lifecycle: asset and dependency identification, protection measures, anomaly detection, business continuity and disaster recovery with tested plans and RTOs/RPOs, backup policies, post-incident reviews, crisis communication.
- An RTS specifies the detailed content of both the full and the simplified framework.

### 2. ICT-related incident management, classification and reporting (Arts. 17–23)

- Maintain an incident management **process** to detect, manage, and notify ICT-related incidents; record all incidents and significant cyber threats.
- **Classify** incidents against harmonized criteria (clients/counterparties affected, duration, geographic spread, data losses, criticality of services, economic impact). A Commission Delegated Regulation (RTS on incident classification) sets the materiality thresholds that make an incident **major**.
- **Report major incidents** to the competent authority in three stages:

| Report | Purpose |
|---|---|
| Initial notification | Rapid alert shortly after the incident is classified as major |
| Intermediate report | Status update once regular activities recover or on relevant status change; further updates on request |
| Final report | Root-cause analysis after completion, with actual impact figures |

  The **exact deadlines (in hours/days) for each stage are set by RTS/ITS, not the level-1 regulation** — verify the current technical standard and your competent authority's portal before committing timelines to a playbook. Plan for an initial notification window measured in hours from classification, an intermediate report on the order of days, and a final report on the order of one month.
- Significant **cyber threats** may be reported voluntarily; clients must be informed where a major incident affects their financial interests.
- See [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).

### 3. Digital operational resilience testing (Arts. 24–27)

- All in-scope entities (except microenterprises) run a risk-based **testing program**: vulnerability assessments and scans, open-source analyses, network security assessments, gap analyses, physical security reviews, scenario-based tests, compatibility/performance testing, penetration testing.
- ICT tools and systems supporting critical or important functions: tested at least **yearly**.
- **TLPT (threat-led penetration testing)**: entities designated by their authority (based on impact, systemic character, and ICT risk profile) must run intelligence-led red-team tests on live production systems covering critical or important functions at least **every 3 years**. The TLPT RTS aligns with the TIBER-EU framework; critical ICT providers supporting the tested functions must participate (pooled testing possible). Testers and threat-intelligence providers must meet independence and certification requirements; external testers are mandatory in defined cases.
- See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md) for how DORA testing evidence feeds a broader assurance program.

### 4. ICT third-party risk management (Arts. 28–44)

- **Strategy and principle-level requirements** (Art. 28): third-party ICT risk managed as integral part of the framework; proportionality; assessment before contracting (including concentration risk and sub-outsourcing chains); exit strategies for critical or important functions.
- **Register of information** (Art. 28(3)): a structured register of *all* contractual arrangements with ICT third-party providers, distinguishing those supporting critical or important functions, in the format fixed by ITS. Authorities collect these registers annually — the register is the practical backbone of DORA third-party compliance and feeds CTPP designation.
- **Key contractual provisions** (Art. 30) — minimum contract content for all ICT service contracts includes: clear service descriptions; data-processing locations (regions/countries) and notice of changes; availability, authenticity, integrity and confidentiality provisions for data; access, recovery and return of data on insolvency or termination; service-level descriptions; incident assistance; cooperation with competent authorities; termination rights and minimum notice. For contracts supporting **critical or important functions**, additionally: full SLAs with performance targets; reporting obligations including incident notification; participation in the entity's security awareness and resilience training; unrestricted rights of access, inspection and audit (for the entity and its authorities); exit strategies with adequate transition periods; TLPT participation.
- **CTPP oversight regime** (Arts. 31–44): the ESAs designate critical ICT third-party providers (major cloud, software, and data providers to the sector) based on systemic impact, importance of dependent entities, and substitutability. Each CTPP gets a **Lead Overseer** (one of EBA/ESMA/EIOPA) with powers to request information, conduct investigations and inspections, and issue recommendations; non-cooperation can attract periodic penalty payments (up to 1% of average daily worldwide turnover, daily, for up to six months). Authorities can, as a last resort, require financial entities to suspend or terminate use of a provider. Non-EU CTPPs must establish an EU subsidiary. First designations were made in 2025.
- See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).

### 5. Information sharing (Art. 45)

Voluntary exchange of cyber threat information and intelligence among financial entities within trusted communities, protected where conducted under the article's conditions; participation (join/leave) is notified to authorities.

## The RTS/ITS layer

DORA is a two-tier regime. The regulation sets principles; the operational detail sits in Regulatory Technical Standards (RTS) and Implementing Technical Standards (ITS) drafted by the ESAs and adopted as Commission delegated/implementing regulations, covering at least: the ICT risk-management framework (full and simplified), incident classification criteria and materiality thresholds, incident report content, format and timelines, the register-of-information template, the sub-outsourcing/critical-function contractual policy, TLPT execution, and oversight harmonization. **Any DORA compliance artifact — incident playbook, contract checklist, register — must cite the applicable RTS/ITS version, and those texts are the ones to re-verify over time.**

## Key obligations for security/GRC teams

1. **Confirm entity category and proportionality tier** (full vs simplified framework, microenterprise carve-outs, TLPT designation status). See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Map the ICT risk-management framework** onto the existing control set (ISO 27001, NIST CSF 2.0) and gap-assess — DORA's identification/protection/detection/response-recovery/learning structure aligns naturally with CSF functions. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md) and [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md).
3. **Inventory critical or important functions** and the ICT assets and providers supporting them — this designation drives testing frequency, contract clauses, exit plans, and TLPT scope.
4. **Build and maintain the register of information** in the ITS format; reconcile it against procurement and accounts-payable data at least annually before regulator submission.
5. **Remediate contracts** against the Art. 30 checklist; prioritize critical-or-important-function providers; track gaps as formal exceptions ([../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md)).
6. **Wire major-incident classification into incident response**: classification criteria embedded in severity triage, pre-approved report templates for initial/intermediate/final stages, authority portals and contacts pre-mapped.
7. **Run the testing program** with evidence: annual testing of critical-function systems, full remediation tracking, and — if designated — a TLPT cycle with certified testers.
8. **Board reporting**: management-body accountability plus training expectations mirror NIS2 Art. 20; report ICT risk, major incidents, testing results, and third-party concentration to the board. See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **NIS2:** DORA is *lex specialis* for financial entities — where both apply, DORA's ICT risk-management and reporting provisions prevail over the corresponding NIS2 provisions. A financial group with non-financial subsidiaries (e.g., an ICT service company inside the group) may still face NIS2 for those subsidiaries. See [nis2.md](nis2.md).
- **GDPR:** a major ICT incident involving personal data triggers DORA reporting to the financial supervisor *and* GDPR Art. 33 notification to the data protection authority within 72 hours — different regulators, different content, parallel clocks. Art. 30 data-location and confidentiality clauses overlap with GDPR Art. 28 processor terms; negotiate them together. See [gdpr.md](gdpr.md).
- **EBA/EIOPA/ESMA outsourcing guidelines:** DORA supersedes much of their ICT content, but the guidelines persist for non-ICT outsourcing; register designs should serve both.
- **CTPP oversight vs customer diligence:** ESA oversight of a critical provider does **not** discharge the financial entity's own third-party risk obligations — the entity remains fully responsible for its use of the provider.
- **EU AI Act:** AI systems used by financial entities (credit scoring, insurance pricing are Annex III high-risk use cases) add AI Act obligations on top of DORA's ICT risk controls; see [eu-ai-act.md](eu-ai-act.md).

## Primary sources

- [Regulation (EU) 2022/2554 (DORA) — official text on EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
