# Incident Notification Decision Log Format

How to document notify and no-notify decisions so they survive regulatory scrutiny, litigation discovery, and an auditor two years later. A notification you sent proves itself; a notification you decided **not** to send is defensible only through the record you made at the time. This file defines that record.

## Why a decision log is mandatory, not optional

- **GDPR Art. 33(5)** requires the controller to document **any** personal data breach — "comprising the facts relating to the personal data breach, its effects and the remedial action taken" — expressly so the supervisory authority can verify compliance with Art. 33. This applies to every personal data breach, including those assessed as unlikely to result in risk and therefore not notified.
- **HIPAA** places the burden of proof on the covered entity/business associate: an impermissible use or disclosure of unsecured PHI is presumed a breach unless a documented four-factor risk assessment demonstrates a low probability that the PHI was compromised. No documentation, no defense.
- **State breach laws** with harm thresholds generally expect (and several require) a written determination, sometimes retained for a fixed period or filed with the AG.
- **SEC:** the reasonableness and timing of the materiality determination is itself examinable — registrants need contemporaneous records showing the determination was made "without unreasonable delay" and on what factors.
- **PIPEDA** requires records of all breaches of security safeguards (24-month retention) regardless of whether the real-risk-of-significant-harm threshold was met.

## Log structure

Keep one decision log per incident, one entry per regime-level decision (a single incident produces many entries). Append-only: corrections are new entries referencing the old one, never edits. Store alongside the notification log (`../../../templates/incident-regulatory-notification-log.md`).

### Entry template

```
Entry ID:            [INC-2026-014-D07]
Incident ref:        [INC-2026-014]
Regime / obligation: [e.g., GDPR Art. 33 SA notification | GDPR Art. 34 data subject
                      communication | HIPAA individual notice | CA Civ. Code breach notice |
                      NIS2 significant-incident reporting | SEC 8-K Item 1.05]
Decision:            [NOTIFY | DO NOT NOTIFY | DEFER — pending facts | SUPERSEDED by entry #]
Decision date-time:  [2026-07-15 14:30 CEST]
Decision maker(s):   [name, role — who had authority to make this call]
Advisors consulted:  [counsel, DPO, forensics — or "none"]

Trigger point analysis:
  Legal trigger for this regime:  [awareness / discovery / materiality determination /
                                   classification as major]
  Did/when did the trigger occur: [timestamp + basis, or "not yet — condition"]
  Deadline if triggered:          [computed date-time]

Facts relied on (as known at decision time):
  [Bullet list: data types, counts, encryption status, exfiltration evidence,
   affected jurisdictions, threat actor behavior. Cite sources — forensic report
   version/date, log analysis, vendor statement. State what was UNKNOWN.]

Threshold analysis:
  [The regime's test applied to the facts. Examples:
   - GDPR Art. 33: is the breach "unlikely to result in a risk to the rights and
     freedoms of natural persons"? Factors: data types, ease of identification,
     severity of consequences, volume, special categories, mitigations (encryption
     with uncompromised keys), data subject vulnerability.
   - GDPR Art. 34: is high risk likely? If not notifying individuals despite SA
     notification, state which Art. 34(3) exception applies, if any, or why risk
     is not "high."
   - HIPAA four factors: (1) nature/extent of PHI incl. identifiers and
     re-identification likelihood; (2) the unauthorized person who used/received;
     (3) whether PHI was actually acquired or viewed; (4) extent of mitigation.
     Conclusion: probability of compromise LOW / NOT LOW.
   - SEC: quantitative and qualitative materiality factors considered; total-mix
     judgment; who made the determination and when the determination process began.
   - State harm threshold: statute's standard quoted, applied.]

Conclusion & rationale: [2-6 sentences. The reasoning, not just the result.]
Dissent / open questions: [any disagreement or flagged uncertainty — recording it
                           helps, not hurts, if the decision was reasonable]
Re-evaluation trigger:  [what new fact reopens this decision — e.g., "evidence of
                         exfiltration," "key compromise confirmed," "count exceeds
                         500 CA residents"]
Re-evaluated on:        [dates of each re-check, even if unchanged]
Attachments:            [forensic report refs, counsel memo refs (note privilege),
                         draft notifications, authority correspondence]
```

## The GDPR Art. 33(5) internal breach record

For every personal data breach — notified or not — maintain a record containing at minimum:

1. **Facts:** what happened, when detected, when the controller became aware (and why awareness attached at that moment), cause if known, data and data subjects affected (categories and approximate numbers), systems involved.
2. **Effects:** actual and likely consequences for data subjects.
3. **Remedial action:** containment, recovery, mitigation for data subjects, and preventive measures adopted.
4. **Assessment and decisions:** the risk assessment for Art. 33 (notify SA?) and Art. 34 (notify data subjects?), with reasoning — including "no risk likely" conclusions.
5. **If notified late:** the reasons for the delay recorded at the time.

A breach register (one row per breach, linking to full entries) satisfies the "verifiability" purpose: supervisory authorities ask for the register first. Minimum register columns: ref, date aware, description, data/subject categories and counts, risk conclusion, SA notified (date/ref or "no + rationale ref"), data subjects notified (date or "no + rationale ref"), status.

## Defensibility rules

1. **Contemporaneous or worthless.** Write the entry the day the decision is made. A rationale reconstructed after a regulator inquiry reads as one.
2. **Record the facts *as known at the time*, separately from later facts.** The decision is judged against what was reasonably known then; the log must show that boundary. When new facts change the picture, add a re-evaluation entry — do not rewrite history.
3. **Name the decision maker.** "The team decided" is not a decision record. Escalation paths (who could overrule) should be visible.
4. **Quote the legal test, then apply it.** An entry that never states the regime's threshold cannot show the threshold was applied.
5. **Document DEFER decisions with a follow-up date.** "Waiting for forensics" without a re-check date becomes "we sat on it" in hindsight. GDPR's 72 hours does not pause for forensics — awareness with reasonable certainty starts the clock even with scope unknown.
6. **Handle privilege deliberately.** Facts and decisions belong in the log; legal advice may live in privileged counsel memos referenced but not reproduced. Do not let privilege strategy leave you with *no* discoverable record of the risk assessment GDPR/HIPAA require you to have.
7. **Retention:** keep the log at least as long as the longest applicable limitation/retention period across triggered regimes (PIPEDA: minimum 24 months for breach records; HIPAA documentation: 6 years; GDPR: no fixed period stated — retain per accountability needs).
8. **Consistency check before closing the incident:** every "No" and "TBD" row in the notification decision table must map to a log entry; every notification sent must map to a NOTIFY entry plus the filed document.

## Worked example (abbreviated no-notify entry)

```
Entry ID: INC-2026-009-D02 | Incident: INC-2026-009 | Regime: GDPR Art. 33
Decision: DO NOT NOTIFY SA | Date: 2026-06-03 11:00 CEST
Decision maker: J. Alvarez, DPO (CISO and GC consulted)
Trigger analysis: Awareness 2026-06-02 16:40 CEST (laptop confirmed stolen, contents
  inventoried). 72h deadline if triggered: 2026-06-05 16:40 CEST.
Facts: Laptop stolen from employee vehicle. Contained cached HR records of 212
  employees (names, salaries, IBANs). Full-disk encryption (AES-256) enforced by
  MDM; MDM attestation shows encryption active at last check-in 2026-06-02 09:12.
  Password + TPM-bound key; no evidence credentials compromised. Remote wipe issued.
Threshold analysis: Art. 33(1) exception — breach unlikely to result in risk:
  data rendered unintelligible by state-of-the-art encryption, keys not compromised,
  device wiped on next network contact. Recital 83 / SA encryption guidance considered.
Conclusion: Confidentiality breach occurred but risk to data subjects unlikely;
  no SA notification. Art. 34 communication likewise not required (a fortiori).
  Recorded in Art. 33(5) breach register, ref BR-2026-031.
Re-evaluation trigger: any evidence of pre-theft credential compromise or
  encryption bypass. Re-check: 2026-06-16 — no new facts, decision stands.
```

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
