# Notification Content Requirements per Regime

Required content elements and skeleton drafts for the major breach/incident notification regimes. Use each regime's checklist to verify a draft is complete before it goes to review; use the skeletons as starting text, replacing every `[bracketed]` field. Fields that cannot yet be filled truthfully must be marked `[UNKNOWN — will supplement]` (only where the regime permits phased reporting) — never invented.

Trigger points and deadlines are covered in the main skill and in `../../../context/crosswalks/breach-notification-timelines.md`; this file covers **what goes in the document**.

---

## 1. GDPR Art. 33 — Notification to the supervisory authority

**Recipient:** Competent supervisory authority — for cross-border processing, the lead SA of the main establishment (one-stop-shop). Most SAs provide a web form; the content below maps onto every SA form.

**Required content (Art. 33(3)):**

| # | Element | Notes |
|---|---|---|
| a | Nature of the breach, including where possible: categories and approximate number of data subjects, and categories and approximate number of personal data records | Approximations are acceptable; ranges are fine |
| b | Name and contact details of the DPO or other contact point | |
| c | Likely consequences of the breach | For data subjects, not the company |
| d | Measures taken or proposed to address the breach, including, where appropriate, measures to mitigate possible adverse effects | Containment + mitigation |
| — | If notification is after 72 hours: reasons for the delay (Art. 33(1)) | Mandatory for late filings |

Phased notification is expressly permitted (Art. 33(4)) — say so in the draft when using it.

**Skeleton:**

> **Personal data breach notification under Article 33 GDPR**
> Controller: [legal entity, address, registration no.] | Contact/DPO: [name, email, phone]
> Cross-border processing: [yes/no; lead SA basis if yes]
>
> **1. Nature of the breach.** On [date/time, TZ] we became aware of [confidentiality/integrity/availability breach: description]. The breach began on or about [date] and was contained on [date / ongoing]. Categories of data subjects affected: [customers/employees/...], approximately [N / range]. Categories of personal data: [list; note any Art. 9 special categories], approximately [N] records. [Encryption status of the data.]
> **2. Likely consequences.** [Identity theft / fraud / loss of confidentiality / discrimination risk / etc., tied to the data types.]
> **3. Measures taken and proposed.** [Containment actions with dates; forensic engagement; credential resets; mitigation offered to data subjects; planned remediation.]
> **4. Data subject communication.** [Notified on date / planned by date / assessed as not high-risk — rationale summary.]
> **5. Further information.** This is an initial notification under Art. 33(4); we will supplement without undue delay as [open items] are resolved. [If late: reasons for delay.]

---

## 2. GDPR Art. 34 — Communication to data subjects

Required only where the breach is **likely to result in a high risk** to rights and freedoms. Exceptions (Art. 34(3)): (a) appropriate protection measures were applied to the affected data (notably encryption rendering it unintelligible); (b) subsequent measures ensure the high risk is no longer likely to materialize; (c) disproportionate effort — then a public communication or similar equally effective measure.

**Required content:** clear and plain language description of the nature of the breach, plus at least Art. 33(3)(b), (c), (d): contact point, likely consequences, measures taken/proposed.

**Skeleton (plain language — no legalese, no minimizing):**

> **What happened.** On [date] we discovered that [plain description]. Your [data types] were involved.
> **What this means for you.** [Concrete risks: phishing, fraud, credential reuse.]
> **What we are doing.** [Actions taken; protections offered — credit monitoring, forced password reset.]
> **What you can do.** [Specific steps: change reused passwords, watch statements, fraud alerts.]
> **Contact.** [DPO/contact channel]. You also have the right to lodge a complaint with [supervisory authority].

---

## 3. NIS2 Art. 23 — Significant incident reporting (three documents)

**Recipient:** The CSIRT or competent authority designated by the member state of the entity. Reporting a significant incident is a sequence, not a single filing:

| Document | Deadline (from awareness unless noted) | Required content |
|---|---|---|
| **Early warning** | 24 hours | Whether the incident is suspected of being caused by unlawful or malicious acts; whether it could have cross-border impact |
| **Incident notification** | 72 hours | Updates the early warning; initial assessment of the incident including its severity and impact; indicators of compromise where available |
| **Intermediate report** | On request of the authority/CSIRT | Relevant status updates |
| **Final report** | 1 month after the incident notification | Detailed description including severity and impact; type of threat or root cause likely to have triggered it; applied and ongoing mitigation measures; cross-border impact where applicable. If the incident is still ongoing at the 1-month mark: progress report then, final report within 1 month of handling the incident |

Where the significant incident affects recipients of the entity's services, the entity must also inform those recipients without undue delay of the incident and, where relevant, of measures they can take in response (and, for significant cyber threats, of the threat).

**Early warning skeleton:**

> **NIS2 early warning** — [entity name, sector/Annex classification, member state, entity registration/ID where required]
> Incident summary: [one paragraph — what, when detected/aware, affected services].
> Suspected unlawful or malicious cause: [yes/no/unknown — basis].
> Possible cross-border impact: [yes/no/unknown — which member states/services].
> Contact: [24/7 contact]. Incident notification to follow within 72 hours of awareness.

For the 72-hour incident notification, extend with: severity assessment [user impact, duration, geographic spread, service disruption], impact on service delivery, IoCs [hashes, IPs, TTPs — attach where sharing is safe], and containment status.

---

## 4. DORA — Major ICT-related incident reporting

**Recipient:** The financial entity's competent authority, using the harmonized reporting templates. Sequence: **initial notification** (within 4 hours of classifying the incident as major, and no later than 24 hours from awareness), **intermediate report** (within 72 hours of the initial notification, and when status changes materially), **final report** (within one month of the latest intermediate report). Classification against the majority criteria (clients/counterparties affected, duration, geographic spread, data losses, criticality of services, economic impact) must be documented — it is the trigger.

Content per the reporting ITS templates: entity identification, incident classification results against each criterion, affected services and members states, impact quantification (clients, transactions, amounts), root cause (final report), and remediation. Draft against the current template fields — do not freehand a DORA report. See `../../../context/regulations/dora.md`.

---

## 5. HIPAA Breach Notification Rule (45 CFR 164.400–414)

**Roles matter:** a **covered entity** notifies individuals, HHS, and (sometimes) media. A **business associate** notifies the covered entity (without unreasonable delay, no later than 60 days from discovery; contracts commonly require faster) — the CE then handles individual/HHS notice.

| Notice | When | Required content |
|---|---|---|
| **Individuals** (164.404) | Without unreasonable delay, no later than 60 calendar days from discovery | See element list below; first-class mail (or email if agreed); substitute notice (website posting 90 days + media or toll-free number) if contact info insufficient for 10+ individuals |
| **HHS Secretary** (164.408) | ≥500 individuals: contemporaneously with individual notice (within the 60 days). <500: annual submission within 60 days after calendar year end | HHS breach portal fields |
| **Media** (164.406) | More than 500 residents of a single state or jurisdiction: prominent media outlet in that state/jurisdiction, same 60-day clock | Same content as individual notice |

**Individual notice content (164.404(c)):** (1) brief description of what happened, including dates of breach and of discovery if known; (2) types of unsecured PHI involved (e.g., name, SSN, DOB, diagnosis); (3) steps individuals should take to protect themselves; (4) what the entity is doing to investigate, mitigate, and prevent recurrence; (5) contact procedures — must include a toll-free number, email, website, or postal address.

Remember the threshold analysis: acquisition/access/use/disclosure of unsecured PHI is **presumed** a breach unless a documented four-factor risk assessment demonstrates low probability of compromise (nature/extent of PHI, unauthorized person, whether actually acquired or viewed, extent of mitigation). Put that assessment in the decision log, not the notice.

---

## 6. SEC Form 8-K Item 1.05 — Material cybersecurity incident

**Who:** US-listed registrants (domestic filers). Foreign private issuers report comparable events on Form 6-K. **Deadline:** four business days from the registrant's determination that the incident is material — the determination itself must be made without unreasonable delay after discovery. Limited delay only via Attorney General national-security/public-safety determination.

**Required disclosure:** the material aspects of the **nature, scope, and timing** of the incident, and the **material impact or reasonably likely material impact** on the registrant, including its financial condition and results of operations. Specific technical detail (vulnerability specifics, IR playbook detail) is **not** required and should not be volunteered if it would impede response or remediation. If required information is undetermined or unavailable at filing, state that, and file an amended 8-K within four business days of the information becoming available.

**Skeleton:**

> **Item 1.05 Material Cybersecurity Incidents.**
> On [date], [Registrant] identified [nature — e.g., unauthorized access to portions of its IT environment]. [Scope: systems/data/operations affected at the level of business function, not host names.] [Timing: when the activity is believed to have begun and when it was identified/contained.]
> [Impact:] The incident has [materially affected / is reasonably likely to materially affect] the Registrant's [operations/financial condition] as follows: [known and reasonably likely impacts — operational disruption, remediation costs, revenue effects, legal exposure — quantified where determinable].
> [If applicable:] As of the date of this filing, the Registrant has not yet determined [specific items]; the Registrant will amend this Item 1.05 to disclose such information within four business days after it is determined or becomes available.

Materiality is a total-mix, reasonable-investor judgment made by management with counsel — present quantitative and qualitative factors; do not decide it in the draft.

---

## 7. US state breach notification (individuals + attorneys general)

All 50 states, DC, and US territories have breach notification laws. They differ on: definition of covered "personal information" (some include usernames+passwords, biometrics, medical or health insurance info), the harm threshold (some allow no-notify where no reasonable likelihood of harm — usually requiring a documented determination), deadlines (many say "most expedient time possible and without unreasonable delay"; a substantial minority impose fixed outer limits, commonly 30–60 days), AG/regulator copies (often triggered at 500 or 1,000 residents), and content mandates (a few states prescribe or prohibit specific content — some prohibit stating breach specifics like number of affected residents; some require specific credit-agency language or complimentary credit monitoring for SSN breaches). See `../../../context/regulations/us-state-privacy.md`.

**Efficient drafting pattern:** build one **master individual notice** with the union of common elements, then a **state-variance table**: State | Resident count | Deadline | AG copy required (threshold) | Content deltas from master | Credit-monitoring obligation | Status.

**Master individual notice elements:** what happened and when; what information was involved; what the organization is doing; what the individual can do (fraud alerts, security freezes, credit reports — several states require the credit bureau and FTC contact details); complimentary services offered; contact information; date of the notice.

**AG notices** typically require: entity identity, nature of breach, number of state residents affected, timing (breach, discovery, notice), copy of the individual notice, and remediation/services offered. Several AGs have online portals; some publish the submissions — write accordingly.

---

## 8. GLBA / FTC Safeguards Rule — notification event reporting

Non-bank financial institutions under the FTC Safeguards Rule must report to the **FTC** a **notification event** — acquisition of unencrypted customer information of **500 or more consumers** without authorization — **within 30 days of discovery**, via the FTC's online form. Content: name and contact of the institution, description of the types of information involved, date or date range of the event if determinable, number of consumers affected, general description of the event, and whether a law-enforcement official has requested delay of public disclosure (with contact details). Note: the FTC publishes these reports. This is regulator notice only — consumer notice obligations still come from state law (and, where applicable, the Interagency Guidance for banking institutions).

**Adjacent regimes to check for financial-sector incidents:**
- **Federal banking agencies (OCC/Fed/FDIC) incident rule:** banking organizations notify their primary federal regulator within **36 hours** of determining a notification incident occurred (materially disrupts operations, business lines, or sector stability); no prescribed content form — a call or email to the point of contact suffices. Bank **service providers** must notify affected banking customers of qualifying disruptions.
- **NYDFS 23 NYCRR 500.17:** covered entities notify the superintendent within **72 hours** of determining a reportable cybersecurity event; notice of extortion payments within 24 hours of payment and a written explanation within 30 days.

---

## 9. Non-US regimes — quick content pointers

Full applicability detail lives in `../../../context/regulations/other-jurisdictions.md`; content essentials when drafting:

- **UK GDPR:** mirrors Art. 33/34 — ICO notification within 72 hours of awareness where risk is likely; same four content elements; ICO web form.
- **Canada (PIPEDA):** report to the OPC and notify affected individuals **as soon as feasible** where the breach creates a **real risk of significant harm**; keep records of **all** breaches for 24 months. Report content: circumstances, day/period, personal information involved, affected count (estimate), mitigation, notification status.
- **Australia (Privacy Act NDB scheme):** notify OAIC and individuals for **eligible data breaches** (likely serious harm) as soon as practicable after the assessment (assessment within 30 days of suspicion). APRA-regulated entities: CPS 234 requires notifying APRA within **72 hours** of an information security incident meeting the rule's criteria.
- **Brazil (LGPD):** communicate to the ANPD and data subjects incidents likely to cause relevant risk or damage; ANPD guidance sets the expected timeframe and content — verify current guidance before drafting.
- **Singapore (PDPA):** notify the PDPC within **3 calendar days** of assessing a breach as notifiable (significant harm or significant scale — 500+ individuals); notify individuals where significant harm is likely.
- **Japan (APPI):** report to the PPC (prompt initial report, detailed report within the prescribed period) and notify individuals for defined categories of leakage (sensitive data, financial harm risk, ill-intent, or 1,000+ individuals).
- **India (DPDP Act):** intimate the Data Protection Board and each affected data principal of any personal data breach in the prescribed form and manner; CERT-In separately requires reporting of specified cyber incidents within **6 hours** of noticing — check both tracks.

---

## Cross-regime drafting rules

1. **One fact base, many documents.** Maintain a single source-of-truth fact sheet (timeline, counts, data types, actions) and derive every notification from it. Inconsistent numbers across filings are a regulator's first finding.
2. **Counts:** use the same counting basis everywhere (individuals vs records vs accounts) and label it.
3. **Do not admit legal conclusions.** State facts ("unauthorized access to X occurred"), not conclusions ("we were negligent," "we violated"). Route drafts through counsel where privilege matters.
4. **Version every draft** with date-time and author; regulators may ask what you knew when.
5. **Language:** file in the language the authority requires; data subject notices in the language of the audience.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
