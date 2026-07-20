# India: Digital Personal Data Protection Act (DPDP Act)

## At a glance

| Attribute | Detail |
|---|---|
| Jurisdiction | India |
| Instrument | Digital Personal Data Protection Act, 2023 (assented August 2023); operationalized by the DPDP Rules (draft January 2025; finalization/notification and phased commencement ran through 2025–2026 — **verify current status**, obligations bite as rules commence) |
| Regulator | Data Protection Board of India (adjudicatory body; government retains significant rule-making and exemption powers) |
| Who's covered | Processing of **digital** personal data in India, and processing outside India in connection with offering goods or services to data principals in India |
| Breach notification | Duty to notify the Board **and every affected data principal**; form and timelines set by the Rules (draft rules: prompt notice to affected individuals and detailed report to the Board within 72 hours — verify final text) |
| Max penalties | Schedule-based caps per breach category — up to **INR 250 crore** (~USD 30M) for failure to take reasonable security safeguards; INR 200 crore for breach-notification failures (verify amounts against the final schedule) |

## Structure and terminology

The Act is deliberately short and principles-light compared to GDPR. Its own vocabulary:

- **Data principal** — the individual (GDPR: data subject)
- **Data fiduciary** — determines purpose and means (GDPR: controller)
- **Data processor** — processes on the fiduciary's behalf
- **Significant data fiduciary (SDF)** — a class designated by the government (by volume/sensitivity of data, risk to sovereignty, electoral democracy, etc.) carrying enhanced obligations

There is **no special-categories regime** and no distinction between sensitive and ordinary personal data (a departure from both GDPR and India's earlier drafts) — the same rules apply to all digital personal data, with children's data as the main carve-out.

## Lawful grounds

Processing requires either **consent** (free, specific, informed, unconditional, unambiguous, clear affirmative action, purpose-limited) or a **"certain legitimate use"** — a closed statutory list including: data voluntarily provided by the principal for a specified purpose, state functions and subsidies, medical emergencies, employment-related purposes, and legal obligations. There is no open-ended legitimate-interests basis; if a use case fits neither consent nor the list, it is not lawful.

**Consent managers** — a distinctive Indian construct: registered intermediaries through which principals can give, manage, and withdraw consent across fiduciaries (an interoperable consent layer echoing India's account-aggregator model). Registration requirements and mechanics live in the Rules — verify operational status.

## Breach notification

The Act imposes a dual duty on **any** personal data breach (no risk-of-harm threshold in the statute itself): notify the **Board** and **each affected data principal**, in the form and manner prescribed by the Rules. The draft Rules prescribed a two-track approach — prompt notification to affected principals (plain-language description, consequences, mitigation, contact) and a report to the Board with specified detail **within 72 hours** (extendable on request) — **verify the final Rules** before committing runbook deadlines. The absence of a statutory harm threshold means triage discipline matters: assume notifiable by default and document any position to the contrary with counsel. See [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).

## Significant data fiduciary obligations

SDFs must appoint a **Data Protection Officer based in India** (reporting to the board of directors), engage an **independent data auditor** for periodic audits, and conduct **periodic Data Protection Impact Assessments** — plus additional measures the Rules specify (draft rules added algorithmic due-diligence and, for certain data, localization-style restrictions on transfer of specified categories — verify). If designated an SDF, expect audit-grade evidence expectations comparable to a certification regime; run readiness with [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md) and [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).

## Children's data

For data principals under **18** (India's threshold is high by global standards): **verifiable parental consent** before processing, and prohibitions on **tracking, behavioural monitoring, and targeted advertising** directed at children. The government may exempt classes of fiduciaries or lower the age for defined purposes via the Rules (draft rules set out verification mechanisms and exemptions — verify). Products with any Indian minor exposure need age-assurance design, not just a terms-of-service line.

## Cross-border transfers

The Act takes a **permissive-by-default** approach: transfers are allowed to any country **not on a government-notified negative list** (none may be notified yet — verify). Two overlays matter: (1) **sectoral rules survive** — RBI payment-data localization, insurance and telecom rules continue to apply regardless of the DPDP posture; (2) Rules-based restrictions for SDFs on specified data categories. Maintain a transfer inventory with the sectoral overlay flagged per flow.

## Enforcement

The **Data Protection Board** inquires into breaches and non-compliance and imposes the schedule-based monetary penalties; appeals lie to the TDSAT (telecom appellate tribunal). There is no compensation right for principals in the Act itself, and — notably — principals owe **duties** (no false grievances, no impersonation) with small penalties. Government exemption powers (state instrumentalities, startups, research) are broad; scope determinations should be revisited as notifications land.

## Key obligations for security/GRC teams

1. **Track Rules commencement** — the Act's obligations activate in phases tied to the Rules; maintain a commencement tracker feeding [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).
2. **Consent infrastructure:** itemized notices (multi-language: the Act requires notice availability in English plus scheduled Indian languages), withdrawal parity ("as easy as giving"), and consent records.
3. **Reasonable security safeguards** — the highest penalty attaches here; the draft Rules enumerate minimums (encryption, access control, logging with retention, backups — verify final list). Map to the existing control set with [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).
4. **Breach runbook** with the assume-notifiable default, dual-recipient flow, and the 72-hour Board report drafted against the final Rules.
5. **SDF watch:** monitor designation criteria; if plausibly in scope, stand up the India-resident DPO, auditor relationship, and DPIA cadence before designation forces it.
6. **Erasure and retention:** data must be erased when consent is withdrawn or the purpose is served (draft rules added time-bound retention limits for large platforms — verify); retention schedules need India-specific rows.

## Interplay

- **GDPR** ([./gdpr.md](./gdpr.md)): DPDP is leaner — no special categories, no legitimate interests, no portability right, no DPIA except for SDFs, fewer principal rights (access, correction, erasure, grievance, nomination). A GDPR program over-complies on most axes but still needs India-specific work: the 18-year children's threshold, consent-manager interoperability, notice languages, and the dual breach notification.
- **IT Act / CERT-In directions:** CERT-In's 2022 directions (6-hour incident reporting for specified incident types to CERT-In, log retention, VPN/cloud provider record-keeping) operate **independently** of the DPDP Act and remain in force — a security incident in India can trigger both CERT-In and DPDP clocks. Verify current directions.
- **Sector regulators:** RBI (payments localization, outsourcing, cyber security framework for banks), IRDAI, SEBI cyber rules continue to apply alongside.

## Primary sources

- [MeitY (DPDP Act and Rules texts)](https://www.meity.gov.in)
- [CERT-In (2022 directions, incident reporting)](https://www.cert-in.org.in)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
