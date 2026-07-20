# Canada: PIPEDA, Quebec Law 25, and Sector Rules

## At a glance

| Attribute | Detail |
|---|---|
| Jurisdiction | Canada (federal + provincial layers) |
| Core instruments | PIPEDA (federal, 2000); provincial private-sector acts deemed substantially similar: Quebec (as overhauled by Law 25), Alberta PIPA, BC PIPA |
| Regulators | Office of the Privacy Commissioner of Canada (OPC); Quebec CAI; Alberta and BC OIPCs; OSFI for federally regulated financial institutions |
| Breach notification | PIPEDA: report to the OPC and notify individuals **as soon as feasible** where a breach creates a **real risk of significant harm (RROSH)**; mandatory breach **record-keeping for 24 months** for ALL breaches; Quebec: notify CAI and affected persons where risk of **serious injury** |
| Max penalties | PIPEDA: fines up to C$100,000 per knowing violation of breach duties; Quebec Law 25: administrative penalties up to C$10M or 2% of worldwide turnover, penal fines up to C$25M or 4% (greater of) |
| Reform status | CPPA/AIDA (Bill C-27) **died on the order paper** when Parliament was prorogued in January 2025; successor federal reform unconfirmed — verify current status |

## The federal layer: PIPEDA

PIPEDA governs collection, use, and disclosure of personal information in the course of **commercial activity**, plus employee data of federally regulated employers (banks, telecoms, transport). It is principles-based, built on ten fair-information principles (accountability, consent, limiting collection/use, safeguards, openness, access...). Where a province has a substantially similar act (Quebec, Alberta, BC), the provincial law applies to intra-provincial matters, with PIPEDA covering interprovincial and international flows — most national programs simply build to the strictest applicable layer.

### Breach regime (since November 2018)

- **Trigger:** a breach of security safeguards creating a **real risk of significant harm** — assessed on data sensitivity and probability of misuse. "Significant harm" is defined broadly (humiliation, financial loss, identity theft, credit impacts, property damage).
- **Duties:** report to the **OPC** and notify **affected individuals** *as soon as feasible*; notify other organizations (e.g., credit bureaus) that can mitigate; and — the most-missed duty — **keep records of every breach**, RROSH or not, for **24 months**, producible to the OPC on request.
- **Sanctions:** knowingly failing to report, notify, or keep records is an offence (fines to C$100,000 per violation). The OPC's practical lever is investigation, findings, and compliance agreements; PIPEDA lacks GDPR-scale fining power — that gap drove the (stalled) CPPA reform.

## Quebec Law 25 — the strictest layer

Quebec's Law 25 (formerly Bill 64) phased in from September 2022 to September 2024 and is now the high-water mark in Canada:

- **Governance:** a **person in charge of protection of personal information** (privacy officer — by default the CEO, delegable, with title and contact published); internal policies and practices published in plain language.
- **Privacy impact assessments** required for information-system projects involving personal information, and **before communicating personal information outside Quebec** — the transfer PIA must conclude the destination provides "adequate protection" per the CAI's factors.
- **Breach:** where a **confidentiality incident** presents a **risk of serious injury**, notify the **CAI** and affected persons promptly, and keep an incident register (producible to the CAI).
- **Consent:** granular, purpose-specific; sensitive information requires express consent; privacy-by-default for public-facing technology settings.
- **Individual rights:** including de-indexation and (phased 2024) **data portability**.
- **Biometrics:** systems verifying/confirming identity via biometrics must be declared to the **CAI no later than 60 days before** deployment (per the related IT framework act — verify mechanics).
- **Automated decisions:** individuals must be informed of exclusively automated decisions and can demand review.
- **Penalties:** administrative monetary penalties to **C$10M or 2%** of worldwide turnover; penal provisions to **C$25M or 4%** (greater of) — GDPR-scale exposure, unique in Canada, plus a private right of action with minimum statutory damages for intentional/gross-fault injuries.

## Sector and other layers

- **OSFI B-13** (Technology and Cyber Risk Management, effective January 2024) binds federally regulated financial institutions: governance, technology operations, cyber security expectations — paired with OSFI's incident-reporting advisory requiring notice of **technology/cyber incidents within 24 hours** of determining materiality (verify current advisory). Conceptually parallel to DORA-lite; see [./dora.md](./dora.md) for the EU analogue.
- **Health:** provincial health-information acts (Ontario PHIPA, Alberta HIA, etc.) govern custodians and their service providers with their own breach duties.
- **Anti-spam (CASL):** consent-based regime for commercial electronic messages and software installation, with significant AMPs — operationally adjacent to the marketing-consent stack.
- **Public sector:** the federal Privacy Act and provincial FOI/privacy statutes (not covered here).

## Reform watch

The **CPPA** (Consumer Privacy Protection Act) and **AIDA** (AI and Data Act), bundled in Bill C-27, would have replaced PIPEDA's Part 1 with a fining regime (up to 5% of global revenue) and created a federal AI law. The bill **died with prorogation in January 2025**. Directionally, any successor is expected to revisit the same ground (stronger OPC powers, AMPs, AI rules) — track via [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md) and verify status before advising.

## Key obligations for security/GRC teams

1. **Build to Quebec:** if Quebec residents' data is in scope, Law 25 sets the bar (officer, PIAs incl. transfer PIAs, register, consent granularity, penalties). A PIPEDA-only posture is under-scoped for national operations.
2. **Breach machinery with two triggers:** RROSH (PIPEDA) and serious-injury (Quebec) assessments documented per incident, dual-recipient notifications, and the **24-month all-breach record** — auditors and the OPC ask for the register, not just the notified cases. Use [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and log in [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) terms.
3. **Transfer PIAs for Quebec-origin flows** out of the province — including to the rest of Canada and the US; contract clauses documenting adequate protection.
4. **Financial institutions:** map B-13 expectations to the control set and wire the 24-hour OSFI notification into IR.
5. **Consent and CASL hygiene:** express-consent capture for sensitive data and marketing, unsubscribe mechanics, and proof-of-consent records.
6. **Biometric deployments in Quebec:** CAI declaration lead time (60 days) built into project plans.

## Interplay

- **GDPR** ([./gdpr.md](./gdpr.md)): Canada (PIPEDA scope) holds an EU adequacy decision (reaffirmed in the 2024 review — verify), easing EU→Canada flows. Law 25 borrows GDPR mechanics (PIAs, penalties, portability); PIPEDA remains principles-based and lighter.
- **US state laws** ([./us-state-privacy.md](./us-state-privacy.md)): cross-border North American programs typically run a merged rights-request and breach process; note Canada's RROSH standard differs from US per-state PI-element triggers.

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
