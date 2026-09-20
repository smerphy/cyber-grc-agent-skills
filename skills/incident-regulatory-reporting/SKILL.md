---
name: incident-regulatory-reporting
description: >-
  Determines which regulatory notification obligations a security incident triggers, computes
  concrete deadlines from each regime's legally defined trigger point, and drafts the required
  notifications (GDPR Art. 33/34, NIS2, HIPAA, SEC 8-K Item 1.05, DORA, state AG notices).
  Use when a user reports a breach, incident, or data compromise and asks "who do we have to
  notify," "do we need to report this," or "draft the regulator notification."
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Turn an incident description into a defensible regulatory response: a decision table of which reporting regimes are triggered and why, a deadline schedule computed from each regime's own trigger point, draft notifications containing each regime's required content elements, and a documentation trail for notify and no-notify decisions alike. The single most common failure in incident reporting is running every deadline off one clock — this skill forces the trigger point to be identified per regime before any deadline is computed.

## When to use

- A security incident, data breach, ransomware event, or significant service outage has occurred (or is strongly suspected) and the user needs to know what must be reported, to whom, and by when.
- The user asks to draft a supervisory authority notification, data subject communication, HHS/OCR report, SEC 8-K Item 1.05, NIS2 early warning, or state attorney general notice.
- A previously reported incident needs a supplement, intermediate report, or final report.
- The user wants to document a decision NOT to notify (which most regimes require documenting anyway).

**Do not use for:**
- Determining which regimes apply to the organization in general (pre-incident) — use [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md); its output (an applicability register) is the ideal input to this skill.
- Technical incident response (containment, forensics, eradication) — out of scope; this skill consumes IR facts, it does not produce them.
- Assessing privacy risk of a planned processing activity — use [../dpia-privacy-assessment/SKILL.md](../dpia-privacy-assessment/SKILL.md).
- Contractual notifications to customers, insurers, or partners — flag them (step 4) but the drafting procedure here covers regulators and legally mandated notices.

## Inputs to gather

Ask for these before starting. Mark anything unknown as **UNKNOWN** and carry it forward explicitly — do not silently assume.

1. **Incident facts:** what happened (unauthorized access, exfiltration, ransomware/encryption, loss of availability, misdirection), affected systems and services, current containment status.
2. **Timeline:** when the incident started (if known), when it was **detected**, when the organization **became aware** it was a personal data breach / significant incident (may differ from detection), timezone. For listed companies: whether a materiality determination has been made and when.
3. **Data involved:** categories (personal data, special categories/sensitive data, health data (PHI), payment card data, credentials, trade secrets, none), approximate record and data-subject counts, whether data was encrypted and whether keys were compromised.
4. **People affected:** data subject types (customers, employees, patients, minors) and their countries/states of residence.
5. **Organization profile:** sector, jurisdictions of establishment, regulated statuses (NIS2 essential/important entity, DORA financial entity, HIPAA covered entity or business associate, US-listed issuer, GLBA financial institution, NYDFS covered entity, state data-broker registration), existing applicability register if one exists.
6. **Role in the data:** controller vs processor (GDPR), covered entity vs business associate (HIPAA), direct obligor vs contractual pass-through — this changes who notifies whom.
7. **Prior notifications:** anything already sent (to regulators, individuals, law enforcement) and when.

## Procedure

1. **Characterize the incident.** Write a one-paragraph incident characterization covering: incident type, data types and volumes, data subject categories and jurisdictions, sector-specific data (PHI, cardholder data), service impact (availability/integrity matter for NIS2 and DORA even with zero data loss), and preliminary materiality indicators for listed companies. This paragraph anchors every regime determination.

2. **Sweep applicable regimes.** Work through [../../context/crosswalks/breach-notification-timelines.md](../../context/crosswalks/breach-notification-timelines.md) regime by regime. For each, answer: (a) does the regime apply to this organization at all, (b) does this incident meet the regime's notification threshold? Cover at minimum: [GDPR](../../context/regulations/gdpr.md) / [UK GDPR and PECR](../../context/regulations/uk-data-protection.md), [NIS2](../../context/regulations/nis2.md) (national transpositions diverge on reporting channels — see [eu-nis2-implementing-and-transposition.md](../../context/regulations/eu-nis2-implementing-and-transposition.md)) and the [UK NIS Regulations](../../context/regulations/uk-nis-cyber-security-resilience.md), [DORA](../../context/regulations/dora.md), [HIPAA](../../context/regulations/hipaa.md) and the [FTC Health Breach Notification Rule](../../context/regulations/us-ftc-act-health-breach-rule.md), [SEC Item 1.05](../../context/regulations/sec-cyber-disclosure.md) and [Reg S-P / Reg SCI](../../context/regulations/us-sec-reg-sp-reg-sci.md), [US state breach laws](../../context/regulations/us-state-breach-notification-laws.md) (per affected-resident state), [GLBA/FTC Safeguards](../../context/regulations/glba-ftc-safeguards.md), sector regulators ([NYDFS](../../context/regulations/us-nydfs-part-500.md), the [federal banking 36-hour rule](../../context/regulations/us-banking-incident-notification-third-party.md), [state insurance regulators](../../context/regulations/us-naic-insurance-data-security.md), [NERC CIP](../../context/regulations/nerc-cip.md), [TSA](../../context/regulations/us-tsa-transportation-cyber.md), [FDA](../../context/regulations/us-fda-medical-device-cybersecurity.md)), product-side duties ([EU Cyber Resilience Act Art. 14](../../context/regulations/eu-cyber-resilience-act.md), which has applied to manufacturers since 11 September 2026), [CIRCIA](../../context/regulations/us-circia.md) (statute in force, but the reporting duties bind only from the effective date of CISA's final rule — confirm current status before promising or skipping a filing), and non-US regimes for any jurisdiction with affected data subjects (per-country packs in References; [other-jurisdictions.md](../../context/regulations/other-jurisdictions.md) for the rest). An incident with no personal data can still trigger NIS2, DORA, SEC, and the banking rules — never stop the sweep because "no PII was involved."

3. **Identify the trigger point per regime — before computing any deadline.** This is the step most often done wrong. The clock starts at a legally defined moment that differs by regime:

   | Regime | Clock starts at | Not at |
   |---|---|---|
   | GDPR Art. 33 | Controller **becomes aware** — reasonable certainty a personal data breach occurred | First alert; forensic confirmation of full scope |
   | GDPR (processor role) | Processor awareness → notify controller **without undue delay** (no 72h grace) | Controller's awareness |
   | NIS2 Art. 23 | **Becoming aware** of the significant incident | Incident start; root-cause confirmation |
   | HIPAA | **Discovery** — known, or would have been known with reasonable diligence (workforce/agent knowledge is imputed) | Completion of the four-factor risk assessment |
   | SEC 8-K Item 1.05 | **Materiality determination** (which must itself be made without unreasonable delay) | Discovery or detection |
   | DORA | **Classification as major** (initial notice also bounded from awareness) | Detection |
   | US state laws | Typically **discovery/determination** that a breach of the state's defined data occurred; some states run from determination that notification is required | Uniform national clock — check each state |
   | FTC Safeguards Rule | **Discovery** of a notification event (≥500 consumers, unencrypted) | — |
   | Federal banking 36h rule | **Determination** that a notification incident occurred | Detection |
   | NYDFS Part 500 | **Determination** that a cybersecurity incident occurred (72h); the extortion payment itself (24h) | Detection; completion of the investigation |
   | EU Cyber Resilience Act Art. 14 (manufacturers) | Becoming **aware** of an actively exploited vulnerability or a severe incident affecting product security | Availability of a fix |
   | CIRCIA (once CISA's final rule is in effect) | Reasonable belief that a covered cyber incident occurred (72h); the ransom payment itself (24h) | Detection — and no duty at all before the final rule's effective date |

   Record the actual date-time of each trigger point for each triggered regime, with timezone. If a trigger point has not yet occurred (e.g., materiality not yet determined), record the deadline as **conditional** and state the condition.

4. **Build the notification decision table.** One row per regime swept (including regimes assessed and NOT triggered — the no-notify rationale is part of the deliverable). Columns: Regime | Triggered? (Yes / No / TBD) | Rationale | Trigger point + timestamp | Deadline (computed) | Recipient | Required content ref | Status. Add rows for contractual notifications identified (cyber insurer, key customers with breach clauses, card brands/acquirer for cardholder data) marked as contractual, not regulatory.

5. **Compute concrete deadlines.** From each trigger timestamp, compute the actual calendar date-time due, respecting each regime's counting rules: NIS2 24h/72h/1-month run in clock hours from awareness; GDPR 72 hours in clock hours from awareness (weekends count); SEC four **business days** from the materiality determination; HIPAA 60 **calendar days** from discovery (individuals and, for 500+ breaches, HHS); state deadlines per statute. Sort the resulting schedule chronologically — the output must show the next deadline first. Where a deadline has already passed, say so plainly and note the regime's late-notification handling (GDPR Art. 33(1) requires reasons for delay to accompany a late notification).

6. **Draft the notifications.** For each triggered regime, draft using the skeletons and required-content checklists in [references/notification-content-requirements.md](references/notification-content-requirements.md). Key regime shapes:
   - **GDPR Art. 33(3):** nature of the breach (categories and approximate numbers of data subjects and records), DPO/contact point, likely consequences, measures taken or proposed. Phased notification under Art. 33(4) is permitted — draft the initial notification with what is known and mark UNKNOWN fields for supplement.
   - **GDPR Art. 34:** separate plain-language communication to data subjects if high risk — assess and document this determination even if the answer is no.
   - **NIS2:** three distinct documents — 24h early warning (suspected unlawful/malicious cause, cross-border impact), 72h incident notification (initial assessment of severity and impact, indicators of compromise), 1-month final report (or progress report if ongoing).
   - **HIPAA:** individual notice content per 45 CFR 164.404(c); HHS portal submission; media notice if more than 500 residents of one state/jurisdiction; business associates notify the covered entity, not HHS.
   - **SEC 8-K Item 1.05:** material aspects of nature, scope, and timing, and material impact or reasonably likely material impact on the registrant — not technical detail that would impede response.
   - **State AG / individual notices:** per-state content and AG-copy requirements; draft one master individual notice and a state-variance table rather than 50 separate letters.
   Never fabricate facts to fill a required field — use "under investigation; will supplement" where accurate, and only where the regime permits phased reporting.

7. **Record notify AND no-notify decisions.** For every regime marked "No," write a dated rationale entry using [references/decision-log-format.md](references/decision-log-format.md). For GDPR specifically, Art. 33(5) requires internal documentation of **all** personal data breaches — facts, effects, remedial action — regardless of whether notified. Log entries in [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).

8. **Track supplements and final reports.** Open a follow-up schedule: GDPR Art. 33(4) supplements as facts firm up; NIS2 final report at 1 month from the incident notification; DORA intermediate and final reports; SEC 8-K amendment if previously undetermined/unavailable information becomes available; state-law supplements where numbers change. A notification obligation is not closed until its final report is filed and the decision log is complete.

9. **Escalate what this skill cannot decide.** Materiality (SEC) is a legal/management judgment — present the factors, do not decide it. Law-enforcement delay requests, litigation privilege, and cross-border conflicts go to counsel. Flag these explicitly in the output.

## Output format

Deliver four artifacts in one document:

**1. Incident characterization** (one paragraph, per step 1).

**2. Notification decision table** — worked example (ransomware with exfiltration at a mid-size EU/US SaaS provider, detected 2026-07-14 09:00 CEST, awareness of personal data breach 2026-07-14 16:00 CEST, ~40,000 EU customer records, 3,200 California residents, company is NIS2 important entity, not US-listed):

| Regime | Triggered? | Rationale | Trigger point (timestamp) | Deadline | Recipient | Status |
|---|---|---|---|---|---|---|
| GDPR Art. 33 | Yes | Personal data breach, risk to data subjects not unlikely | Awareness 2026-07-14 16:00 CEST | 2026-07-17 16:00 CEST (72h) | Lead SA (per main establishment) | Draft ready |
| GDPR Art. 34 | TBD | High-risk assessment pending (credentials involved?) | Awareness 2026-07-14 16:00 CEST | Without undue delay if high risk | Data subjects | Assessing |
| NIS2 early warning | Yes | Significant incident, important entity, malicious cause suspected | Awareness 2026-07-14 16:00 CEST | 2026-07-15 16:00 CEST (24h) | National CSIRT/competent authority | **OVERDUE if not sent — send now with delay noted** |
| NIS2 incident notification | Yes | Follows early warning | Awareness 2026-07-14 16:00 CEST | 2026-07-17 16:00 CEST (72h) | Same | Drafting |
| NIS2 final report | Yes | Follows incident notification | Incident notification date | +1 month | Same | Scheduled |
| CA breach law + AG notice | Yes | >500 CA residents, unencrypted personal information | Discovery 2026-07-14 | Most expedient time, without unreasonable delay; AG copy at >500 residents | Individuals; CA AG | Drafting |
| SEC 8-K Item 1.05 | No | Not an SEC registrant | — | — | — | Logged (no-notify) |
| HIPAA | No | No PHI; org is neither CE nor BA | — | — | — | Logged (no-notify) |
| Cyber insurer (contractual) | Yes | Policy requires prompt notice | Detection 2026-07-14 09:00 | Per policy | Carrier | Sent 2026-07-14 |

**3. Deadline schedule** — chronological list of every open deadline with date-time, timezone, and owner.

**4. Draft notifications** — one per triggered regime, each headed by regime, recipient, deadline, and completeness status (fields marked UNKNOWN listed at top), body per [references/notification-content-requirements.md](references/notification-content-requirements.md).

Plus: decision log entries per [references/decision-log-format.md](references/decision-log-format.md) and a follow-up schedule (step 8).

## Quality checklist

- [ ] Every regime in the sweep has an explicit Yes/No/TBD with rationale — no regime silently skipped.
- [ ] Every deadline is computed from that regime's own trigger point, and the trigger point timestamp (with timezone) is stated in the table.
- [ ] SEC deadline (if applicable) runs from materiality determination, not detection; the materiality decision itself is flagged to management/counsel, not made by the analyst.
- [ ] Business-day vs calendar-day vs clock-hour counting applied correctly per regime.
- [ ] Passed deadlines are called out, not hidden, with the regime's late-filing handling noted.
- [ ] Every draft notification contains all required content elements for its regime, and every unknown field is marked for supplement rather than fabricated.
- [ ] GDPR Art. 34 data subject communication was assessed and documented even if not triggered.
- [ ] No-notify decisions are logged with rationale and date (GDPR Art. 33(5) documentation exists for any personal data breach).
- [ ] Processor/business-associate role checked — where the org is a processor or BA, notifications route to the controller/covered entity and contract deadlines are checked.
- [ ] Follow-up schedule exists for all supplements, intermediate reports, and final reports.
- [ ] Contractual notifications (insurer, customers, card brands) identified and marked as contractual, not conflated with regulatory duties.

## References

- [references/notification-content-requirements.md](references/notification-content-requirements.md) — required content elements per regime with skeleton drafts.
- [references/decision-log-format.md](references/decision-log-format.md) — defensible notify/no-notify documentation, including GDPR Art. 33(5) internal record.
- [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md) — running log template.
- [../../context/crosswalks/breach-notification-timelines.md](../../context/crosswalks/breach-notification-timelines.md) — deadline matrix across regimes.
- **EU and UK reporting duties:** [gdpr.md](../../context/regulations/gdpr.md) · [eu-eprivacy.md](../../context/regulations/eu-eprivacy.md) · [nis2.md](../../context/regulations/nis2.md) · [eu-nis2-implementing-and-transposition.md](../../context/regulations/eu-nis2-implementing-and-transposition.md) · [dora.md](../../context/regulations/dora.md) · [eu-dora-technical-standards.md](../../context/regulations/eu-dora-technical-standards.md) · [eu-cyber-resilience-act.md](../../context/regulations/eu-cyber-resilience-act.md) · [eu-digital-services-act.md](../../context/regulations/eu-digital-services-act.md) · [eu-ehds.md](../../context/regulations/eu-ehds.md) · [uk-data-protection.md](../../context/regulations/uk-data-protection.md) · [uk-nis-cyber-security-resilience.md](../../context/regulations/uk-nis-cyber-security-resilience.md) · [uk-financial-operational-resilience.md](../../context/regulations/uk-financial-operational-resilience.md) · [switzerland-fadp-isa.md](../../context/regulations/switzerland-fadp-isa.md)
- **US federal and sector reporting duties:** [hipaa.md](../../context/regulations/hipaa.md) · [us-ftc-act-health-breach-rule.md](../../context/regulations/us-ftc-act-health-breach-rule.md) · [glba-ftc-safeguards.md](../../context/regulations/glba-ftc-safeguards.md) · [sec-cyber-disclosure.md](../../context/regulations/sec-cyber-disclosure.md) · [us-sec-reg-sp-reg-sci.md](../../context/regulations/us-sec-reg-sp-reg-sci.md) · [us-banking-incident-notification-third-party.md](../../context/regulations/us-banking-incident-notification-third-party.md) · [us-nydfs-part-500.md](../../context/regulations/us-nydfs-part-500.md) · [us-naic-insurance-data-security.md](../../context/regulations/us-naic-insurance-data-security.md) · [us-circia.md](../../context/regulations/us-circia.md) · [us-fisma-federal-cyber.md](../../context/regulations/us-fisma-federal-cyber.md) · [nerc-cip.md](../../context/regulations/nerc-cip.md) · [us-tsa-transportation-cyber.md](../../context/regulations/us-tsa-transportation-cyber.md) · [us-fda-medical-device-cybersecurity.md](../../context/regulations/us-fda-medical-device-cybersecurity.md) · [us-cjis-security-policy.md](../../context/regulations/us-cjis-security-policy.md) · [us-irs-pub-1075.md](../../context/regulations/us-irs-pub-1075.md)
- **US state reporting duties:** [us-state-breach-notification-laws.md](../../context/regulations/us-state-breach-notification-laws.md) · [us-state-privacy.md](../../context/regulations/us-state-privacy.md) · [us-biometric-privacy-laws.md](../../context/regulations/us-biometric-privacy-laws.md)
- **Asia-Pacific reporting duties:** [china-pipl-dsl-csl.md](../../context/regulations/china-pipl-dsl-csl.md) · [japan-appi-cyber.md](../../context/regulations/japan-appi-cyber.md) · [south-korea-pipa.md](../../context/regulations/south-korea-pipa.md) · [india-dpdp-cert-in.md](../../context/regulations/india-dpdp-cert-in.md) · [singapore-pdpa-cybersecurity.md](../../context/regulations/singapore-pdpa-cybersecurity.md) · [southeast-asia-privacy-regimes.md](../../context/regulations/southeast-asia-privacy-regimes.md) · [hong-kong-pdpo-critical-infrastructure.md](../../context/regulations/hong-kong-pdpo-critical-infrastructure.md) · [australia-privacy-act.md](../../context/regulations/australia-privacy-act.md) · [australia-apra-cps-234-230.md](../../context/regulations/australia-apra-cps-234-230.md) · [australia-soci-cyber-security-act.md](../../context/regulations/australia-soci-cyber-security-act.md) · [new-zealand-privacy-act.md](../../context/regulations/new-zealand-privacy-act.md)
- **Americas, Middle East, Africa reporting duties:** [canada-pipeda-law-25.md](../../context/regulations/canada-pipeda-law-25.md) · [brazil-lgpd.md](../../context/regulations/brazil-lgpd.md) · [latin-america-privacy-regimes.md](../../context/regulations/latin-america-privacy-regimes.md) · [israel-privacy-protection-law.md](../../context/regulations/israel-privacy-protection-law.md) · [saudi-arabia-pdpl-nca.md](../../context/regulations/saudi-arabia-pdpl-nca.md) · [uae-data-protection-cyber.md](../../context/regulations/uae-data-protection-cyber.md) · [south-africa-popia.md](../../context/regulations/south-africa-popia.md) · [africa-privacy-regimes.md](../../context/regulations/africa-privacy-regimes.md) · [other-jurisdictions.md](../../context/regulations/other-jurisdictions.md)
- **Incident-handling method and continuity:** [nist-800-61-incident-handling.md](../../context/frameworks/nist-800-61-incident-handling.md) · [iso-22301-business-continuity.md](../../context/frameworks/iso-22301-business-continuity.md) · [pci-dss-4.md](../../context/frameworks/pci-dss-4.md)
- [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md) — establish which regimes apply before an incident happens.
- [../dpia-privacy-assessment/SKILL.md](../dpia-privacy-assessment/SKILL.md) — privacy risk assessment methodology reused in the Art. 34 high-risk determination.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
