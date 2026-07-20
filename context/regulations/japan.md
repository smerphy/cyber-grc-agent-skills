# Japan: Act on the Protection of Personal Information (APPI)

## At a glance

| Attribute | Detail |
|---|---|
| Jurisdiction | Japan |
| Instrument | Act on the Protection of Personal Information (APPI), Act No. 57 of 2003, substantially amended 2015, 2020 (in force April 2022) and 2021 (public/private consolidation) |
| Regulator | Personal Information Protection Commission (PPC) — independent, centralized |
| Who's covered | Business operators handling personal information; extraterritorial reach to foreign operators handling data of individuals in Japan in connection with offering goods/services |
| Breach reporting | Mandatory since April 2022 for defined incident classes: prompt initial report to the PPC, final report within 30 days (60 days for intentional/malicious causes — verify against PPC guidance); affected individuals must also be notified |
| Max penalties | Corporate fines up to ¥100M for certain violations (e.g., ignoring PPC orders, unlawful database trafficking); PPC guidance, recommendations, and orders are the primary lever |
| EU relationship | Mutual adequacy with the EU since January 2019 (supplementary rules apply to EU-origin data) |

## Key concepts

- **Personal information / personal data / retained personal data.** The Act layers obligations: "personal information" (identifiable information), "personal data" (information in a searchable database), and "retained personal data" (data the operator can disclose/correct — the tier that carries data-subject-facing duties).
- **Special care-required personal information** — race, creed, social status, medical history, criminal record, crime-victim status, and similar categories defined by cabinet order. Requires prior consent to acquire (with narrow exceptions); roughly analogous to GDPR special categories but consent-gated at *acquisition*.
- **Anonymously processed information** (2015 amendment) and **pseudonymously processed information** (2020 amendment) — two distinct de-identification regimes with different obligations and re-identification prohibitions. Pseudonymized data retains more utility but stays regulated; do not treat either as GDPR "anonymous" without analysis.

## Breach reporting

The 2020 amendment made reporting mandatory (from April 2022) for four incident classes:

1. Breaches involving special care-required personal information
2. Breaches likely to cause financial harm (e.g., payment card data)
3. Breaches caused by acts with wrongful intent (unauthorized access, malware, insider theft)
4. Breaches affecting more than 1,000 individuals

Mechanics (verify current PPC rules): a **prompt initial report** to the PPC (PPC guidance indicates within roughly 3–5 days of becoming aware), a **final report within 30 days** (60 days for the wrongful-intent class), and **notification to affected individuals** promptly, unless substitution measures (public notice) apply where individual notice is difficult. The two-stage cadence rewards the same discipline as NIS2-style reporting: an early factual report with follow-up, not silence until investigation completes. See [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).

## Security control measures

APPI requires "necessary and appropriate measures" for security of personal data. The PPC's guidelines decompose this into **organizational, human, physical, and technical** safeguard categories — functionally a lightweight control framework (policies and responsible persons; training and confidentiality duties; physical access and media handling; access control, malware defense, monitoring). Map these against an existing control set with [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md) rather than building a parallel program; an ISO 27001-grade program generally covers the substance.

Operators must also supervise **trustees** (processors/subcontractors) — contractual controls plus ongoing oversight, the practical equivalent of GDPR Art. 28 diligence.

## Cross-border transfers

Providing personal data to a third party in a foreign country requires one of:

- **Consent**, given after the operator provides information about the destination country's data-protection system and the recipient's measures (the 2020 amendment made this information duty explicit);
- Transfer to a country designated as having an **equivalent** system (the EU and UK are designated — verify current list); or
- A recipient with **equivalent safeguards** established (contractual or intra-group mechanisms, APEC CBPR certification), with ongoing monitoring and information duties.

EU-origin data received under the mutual adequacy carries **supplementary rules** (stricter handling of special categories, retention of the EU-origin marking, onward-transfer limits).

## Enforcement and outlook

PPC enforcement typically escalates guidance → recommendation → order, with criminal penalties reserved for order violations and database trafficking. Direct fine amounts are modest by GDPR standards; the operational risk is business disruption and mandatory remediation, plus reputational exposure in a market sensitive to data incidents.

The Act is subject to a **triennial review**. The review cycle running through the mid-2020s has discussed administrative monetary penalties, collective redress, and children's data protections — proposals only; verify current amendment status before advising on future obligations.

## Key obligations for security/GRC teams

1. **Classify Japanese data holdings** into personal data / special care-required / pseudonymized categories — obligations attach differently to each.
2. **Wire the four reportable incident classes** into incident-response triage, with the initial-report clock (days, not weeks) and the 30/60-day final report tracked as deadlines.
3. **Purpose specification and use limitation:** purposes must be specified as concretely as practicable and published or notified; changes beyond reasonable relevance need consent.
4. **Third-party provision records:** transfers to third parties generally require consent or an opt-out filing with the PPC (opt-out route unavailable for special care-required data), and both provider and recipient must keep transfer records — an auditable ledger, not a policy statement.
5. **Trustee supervision** evidence: contracts, security review of subcontractors, periodic checks — fold into [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
6. **Transfer inventory for Japan-origin data** with the mechanism per destination, and the pre-consent information disclosures where consent is the basis.

## Interplay

- **GDPR** ([./gdpr.md](./gdpr.md)): mutual adequacy makes EU↔Japan flows straightforward, but the supplementary rules mean EU-origin data needs tagging and differentiated handling inside Japanese systems. APPI is notification-and-purpose driven where GDPR is lawful-basis driven; a GDPR program needs a consent/notice overlay, not a rebuild.
- **APEC CBPR:** Japan participates; CBPR certification can serve as a transfer mechanism and vendor-assurance signal in APAC.
- **Sector rules:** financial services (FSA guidelines), telecom, and medical sectors carry additional security and secrecy obligations — check sector guidance when scoping.

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
