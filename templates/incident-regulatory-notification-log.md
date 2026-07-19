# Incident Regulatory Notification Log

**How to use:** Open this log the moment an incident is confirmed or strongly suspected — several regimes start their clocks at *awareness* or *detection*, not at the end of the investigation. Section 1 is the decision table: assess **every** potentially applicable regime, including the ones you conclude are not triggered — the documented no-notify rationale is your defense later. Section 2 records the reasoning behind each decision at the time it was made. Deadlines and trigger definitions per regime: [../context/crosswalks/breach-notification-timelines.md](../context/crosswalks/breach-notification-timelines.md). Full assessment procedure and drafting guidance: [../skills/incident-regulatory-reporting/SKILL.md](../skills/incident-regulatory-reporting/SKILL.md). Which regimes even apply to your organization: [../skills/regulatory-applicability/SKILL.md](../skills/regulatory-applicability/SKILL.md).

## Incident header

| Field | Value |
|---|---|
| Incident ID / name | [INC-YYYY-NNN] |
| Incident summary | [One paragraph: what happened, systems and data affected, current status] |
| Detection timestamp (UTC) | [YYYY-MM-DD HH:MM] |
| Confirmation timestamp (UTC) | [When the incident was confirmed — record the basis, since regime clocks anchor differently] |
| Personal data involved? | [Y/N/TBD — categories, subject counts, jurisdictions of subjects] |
| Log owner | [Role — typically legal/privacy counsel or incident commander's regulatory lead] |
| Last updated | [Timestamp — update on every change; this log will be evidence] |

## 1. Regime decision table

*One row per potentially applicable regime — regulators, contractual counterparties, and individuals. Populate the "clock start event" with the regime's own trigger definition, not a generic one. Status values: Assessing / Not triggered / Triggered - preparing / Filed / Follow-up due / Closed.*

| Regime | Triggered? | Rationale (brief — full reasoning in §2) | Clock start event and timestamp (UTC) | Deadline | Recipient | Status | Filed timestamp | Follow-ups due |
|---|---|---|---|---|---|---|---|---|
| GDPR Art. 33 (supervisory authority) | Y | Personal data breach; risk to rights and freedoms of EU subjects not unlikely (D-01) | Awareness: 2026-07-14 09:20 | 72h → 2026-07-17 09:20 | [Lead supervisory authority] | Filed | 2026-07-16 15:41 | Supplementary report with final subject count when forensics completes (phased notification noted in filing) |
| GDPR Art. 34 (data subjects) | Assessing | High-risk threshold not yet determined; depends on confirmation of exfiltration (D-02) | Same awareness point | Without undue delay if triggered | Affected individuals | Assessing | — | Decision due 2026-07-18 |
| NIS2 (if in scope as essential/important entity) | [Y/N] | [Significant incident per Art. 23 criteria?] | [Awareness timestamp] | 24h early warning; 72h incident notification; 1 month final report | [National CSIRT / competent authority] | | | [Intermediate report if requested; final report at 1 month] |
| SEC 8-K Item 1.05 (US-listed) | [Y/N] | [Material to a reasonable investor? Record the materiality determination process and date — the four-business-day clock runs from the **materiality determination**, not discovery] | [Materiality determination date] | 4 business days from determination | EDGAR filing | | | [Amended 8-K if prior filing details become materially inaccurate] |
| US state breach laws | [Y/N] | [Residents' data by state; thresholds and AG-notification triggers vary — see [../context/regulations/us-state-privacy.md](../context/regulations/us-state-privacy.md)] | [Per state definition] | [Per state] | [Individuals; state AGs where thresholds met] | | | |
| Sector regime ([HIPAA](../context/regulations/hipaa.md) / [GLBA-FTC](../context/regulations/glba-ftc-safeguards.md) / [DORA](../context/regulations/dora.md) / other) | [Y/N] | [Covered entity/data? Classification thresholds?] | | | | | | |
| Contractual notifications (customers, cyber insurer, partners) | [Y/N] | [DPA and MSA clauses often run at 24-72h from confirmation — inventory them now] | [Per contract] | [Per contract — earliest first] | [Counterparty list] | | | |
| Law enforcement (non-mandatory) | [Y/N] | [Voluntary report; may support delay provisions in some regimes] | — | — | | | | |

*Delete inapplicable rows only after recording why they are inapplicable in Section 2.*

## 2. Decision log (notify / no-notify rationale)

*One entry per decision, written at the time of the decision with the information then available. Never edit an entry after the fact — append a superseding entry instead. This is the section a regulator or court reads.*

| Decision ID | Timestamp (UTC) | Regime | Decision | Rationale and information relied on | Decided by |
|---|---|---|---|---|---|
| D-01 | 2026-07-15 17:30 | GDPR Art. 33 | Notify | Exfiltration of a directory containing names, emails, and hashed passwords of ~40,000 EU customers confirmed via egress logs. Risk to rights and freedoms cannot be assessed as unlikely (credential-stuffing exposure). Notification filed within 72h of awareness with information available; phased approach declared for pending forensics. | DPO + external counsel |
| D-02 | [pending] | GDPR Art. 34 | [pending] | [High-risk assessment: password hash algorithm strength, evidence of cracking, mitigations offered (forced reset completed 2026-07-15 22:00) — mitigation may take individual notification out of scope if it renders the risk no longer likely to materialize; decision and basis to be recorded here] | DPO |
| D-03 | [example - no-notify] | [State X breach law] | Do not notify | [No residents of State X in affected dataset per residency analysis of 2026-07-16; analysis retained as attachment A-04] | Counsel |

## 3. Attachments and evidence index

| Ref | Item |
|---|---|
| A-01 | Filed Art. 33 notification (as submitted) and authority acknowledgment |
| A-02 | Materiality/risk assessment memos supporting each decision |
| A-03 | Contract notification clause inventory with deadlines |
| A-04 | [Analyses relied on in decision log entries] |

## 4. Closure checklist

- [ ] All triggered regimes: final reports/supplements filed and acknowledged
- [ ] All no-notify decisions documented with retained supporting analysis
- [ ] Follow-up obligations calendared with owners
- [ ] Log and attachments archived per retention schedule; fed into post-incident review
- [ ] Risk register updated ([risk-register.csv](risk-register.csv)) and lessons fed to [../skills/incident-regulatory-reporting/SKILL.md](../skills/incident-regulatory-reporting/SKILL.md) playbook updates

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
