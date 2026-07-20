# Example: Incident Notification Decision Table

**Persona:** compliance-officer · **Skill:** [incident-regulatory-reporting](../skills/incident-regulatory-reporting/SKILL.md) · **Context loaded:** [breach-notification-timelines](../context/crosswalks/breach-notification-timelines.md), [gdpr](../context/regulations/gdpr.md), [nis2](../context/regulations/nis2.md), [sec-cyber-disclosure](../context/regulations/sec-cyber-disclosure.md)

All entities and events are fictional.

---

## User input

> We have an active incident. What do we need to file, where, and by when?
>
> - Company: Meridian Fleet Systems — SaaS fleet-management platform. Dutch operating subsidiary (Rotterdam) serves EU logistics customers; US parent is NASDAQ-listed.
> - Incident: ransomware on the EU production environment. Detected **Tue 14 July 2026, 06:40 UTC** by the SOC; forensics confirmed **data exfiltration at 18:15 UTC the same day**.
> - Data confirmed exfiltrated: ~48,000 driver profiles (names, license numbers, GPS trip history) — drivers are employees of ~200 EU logistics customers. ~1,900 of the drivers are California residents via one US customer.
> - We are a data **processor** for customer driver data; controller for our own ~300 employees (HR data not affected per current forensics).
> - The platform is down for 11 EU customers, including two large road-haulage groups.
> - Revenue impact unclear; incident response cost estimate $2–4M. No ransom paid. Insurer not yet notified.

## Agent output (deliverable)

### Role determination — controls everything downstream

Meridian NL is a **processor** for the exfiltrated driver data. GDPR Art. 33(2) applies: Meridian must notify each affected **controller** (the ~200 customers) *without undue delay* — the customers own the 72-hour supervisory filings and any driver notifications. Meridian's own Art. 33(1) duty would arise only for data it controls (employee data — currently not affected; re-run this table if forensics changes that).

As a fleet-management platform for road transport, Meridian NL plausibly falls in NIS2 Annex I (transport-supporting digital services) or as a digital provider — **entity classification unresolved**, treated as in-scope pending counsel confirmation (flagged, not assumed).

### Notification decision table

| # | Regime | Triggered? | Rationale | Clock start (event + timestamp) | Deadline | Recipient | Status |
|---|---|---|---|---|---|---|---|
| 1 | GDPR Art. 33(2) — processor duty | **Yes** | Personal data breach affecting customer-controlled data | Awareness of breach: 14 Jul 06:40 UTC | **Without undue delay — target ≤24h: 15 Jul 06:40 UTC** | All ~200 affected controllers, per DPA notice clauses (many specify 24–48h — pull the DPAs) | DRAFTING |
| 2 | GDPR Art. 33(1) — own controller duty | No (monitor) | Employee data not affected per current forensics | — | Re-assess on any forensic change | Dutch AP | MONITORING |
| 3 | NIS2 Art. 23 | **Yes (provisional)** | Significant incident: service outage for 11 customers + malicious cause; entity classification pending | Awareness: 14 Jul 06:40 UTC | **Early warning: 15 Jul 06:40 UTC · notification: 17 Jul 06:40 UTC · final: 14 Aug** | Dutch CSIRT (NCSC-NL) per NL transposition — confirm portal | EARLY WARNING DRAFTED |
| 4 | SEC 8-K Item 1.05 (US parent) | **Undetermined — process triggered** | Materiality determination required without unreasonable delay; outage + exfil + $2–4M cost vs. company financials | Materiality determination (pending — committee convened 14 Jul) | **4 business days from determination** | SEC EDGAR | MATERIALITY ANALYSIS OPEN |
| 5 | CCPA / Cal. Civ. Code §1798.82 | No direct duty (processor path) | Meridian is a service provider; duty to notify the **customer** (data owner), who notifies CA residents/AG | Discovery: 14 Jul | Without unreasonable delay (contract may specify) | Affected US customer | INCLUDED IN #1 BATCH |
| 6 | Insurer (cyber policy) | **Yes — contractual** | Policy requires prompt notice; costs may not be covered before notice | Detection: 14 Jul | Per policy "prompt" — same day | Carrier + broker | **OVERDUE — do now** |
| 7 | Customer contracts (SLA/security schedules) | **Yes** | Most B2B security schedules have 24–48h incident notice independent of GDPR | Detection: 14 Jul | Per contract — assume 24h worst case: 15 Jul 06:40 UTC | Customer security contacts | DRAFTING (with #1) |

### Immediate actions (ordered)

1. **Insurer notice today** — it is already the tightest constraint and gates cost recovery.
2. **Controller notification batch by 15 Jul 06:40 UTC** — one processor notice per Art. 33(2) content norms (nature, categories, approximate numbers, measures taken, contact point), so controllers can meet their own 72-hour clocks, which are already running if their awareness is imputed from ours — flag this to them explicitly.
3. **NIS2 early warning by 15 Jul 06:40 UTC** — thin by design: suspected malicious cause, cross-border impact (11 customers, multiple member states). Do not wait for full forensics.
4. **SEC materiality determination** — document the committee's analysis and date; the 4-business-day clock starts at determination, but slow-walking the determination is itself a violation pattern the SEC has called out.
5. Open the **decision log** now (per [decision-log-format](../skills/incident-regulatory-reporting/references/decision-log-format.md)): every notify/no-notify call above with rationale and timestamp, including the Art. 33(1) "not triggered" decision — GDPR Art. 33(5) requires documenting breaches regardless of notification.

### Flags for counsel

- NIS2 entity classification (and whether NL transposition specifics alter the deadlines/portal).
- Whether any driver license numbers qualify as government identifiers under specific US state laws with independent service-provider duties.
- EU employee works-council notification duties in affected customer jurisdictions (customer-side, but expect questions).

---

*This is analysis support, not legal advice. Deadlines computed from the timestamps supplied; all filings need counsel review before submission.*
