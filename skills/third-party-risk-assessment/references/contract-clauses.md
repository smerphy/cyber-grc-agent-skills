# Vendor Contract Security and Privacy Clause Checklist

Contract terms are the only vendor controls you actually own. Assessment findings without contractual teeth evaporate at renewal. Use this checklist to build the security schedule (or exhibit/addendum) before signature; the "fallback" column gives the realistic negotiated position when the vendor's paper wins. Tier guidance: Tier 1 = all clauses; Tier 2 = all except those marked optional; Tier 3 = core set (marked ●); Tier 4 = standard terms only.

Legal drafts the words; security defines the requirements. Bring this list to the first redline, not the last.

## 1. Breach and incident notification ●

- **Notification SLA**: vendor notifies you of a confirmed security incident affecting your data or service within a defined period — target **24 hours**, accept 48-72h; reject "without undue delay" alone (undefined) and reject clocks that start at "completed investigation".
- **Clock trigger**: define the trigger as *awareness/confirmation of an incident*, not conclusion of forensics. Distinguish "incident" (confirmed) from "event" (noise) so the vendor can't hide behind either extreme.
- **Content**: nature of incident, data/systems affected, individuals/records affected (or best estimate), actions taken, vendor contact. Continuing duty to update.
- **Why the hours matter**: your own regulatory clocks (GDPR Art. 33 72-hour supervisory notification; HIPAA; state breach laws; NIS2 24-hour early warning where applicable) run against *your* awareness — a vendor allowed 30 days to tell you consumes your entire compliance window. See `../../../context/crosswalks/breach-notification-timelines.md`.
- **Cooperation**: vendor provides reasonable assistance for your regulatory notifications and investigations at no or defined cost; you control communications about your data.
- **Suspected-compromise of credentials/keys**: immediate notification and rotation cooperation.

## 2. Audit and assessment rights ●

- Right to assess annually and after any security incident: at minimum a questionnaire + evidence review; for Tier 1, on-site or live-session audit right (accept "at customer's cost, reasonable notice, once per year, no disruption" qualifiers).
- **Attestation delivery**: vendor provides its then-current SOC 2 Type II (or ISO 27001 certificate + SoA) annually without request, plus bridge letters on request. Make lapse of attestation a notifiable event.
- Right to review penetration test attestations annually.
- Regulator access: where your regulator requires it (financial services under DORA/GLBA-adjacent oversight, healthcare), the vendor cooperates with regulator examinations. See `../../../context/regulations/dora.md` for the contractual requirements DORA imposes for ICT services supporting critical or important functions.

## 3. Subprocessors and flow-down ●

- Current subprocessor list as an annex or referenced URL; **advance notice** of additions/changes (30 days typical) with a right to object; for Tier 1, approval rather than mere notice where negotiable.
- **Flow-down**: vendor imposes materially equivalent security and privacy obligations on subprocessors and remains fully liable for their performance. Without flow-down, every other clause stops at the first outsourcing boundary.
- No transfer of your data to subprocessors outside agreed regions without the transfer mechanisms in the DPA.

## 4. Data handling, return, and deletion ●

- **Data use limitation**: your data used solely to provide the contracted service; no use for vendor product improvement, model training, or analytics beyond de-identified/aggregated forms you have expressly permitted (define "de-identified"; name AI/ML training explicitly — silence is consent in practice).
- **Location**: storage and processing regions specified; changes are notifiable.
- **Encryption**: in transit (current TLS) and at rest; key management described; customer-managed keys optional for Tier 1.
- **Return and deletion**: on termination or request — export in a usable format within a defined window, then deletion of all copies (including backups on their rotation schedule, stated maximum) within a defined period (30-90 days typical), with **written certification of deletion**. Fallback: deletion certificate excluding backup media with a committed backup-expiry maximum.
- **Retention limits** during the contract where regulatory rules apply to the data.

## 5. Security program requirements

- Maintain a written information security program aligned to a named framework (ISO/IEC 27001, NIST CSF 2.0, or SOC 2 TSC) — see `../../../context/crosswalks/framework-crosswalk.md` for equivalence arguments when the vendor uses a different one than you asked for.
- Named minimums for Tier 1-2: MFA for vendor personnel access to systems holding your data; least-privilege and joiner/mover/leaver process; vulnerability management with remediation targets; logging and monitoring; secure development practices; background checks where lawful; security awareness training.
- **No degradation** clause: security measures may evolve but not materially degrade during the term.

## 6. Privacy / DPA (where personal data is processed) ●

- Full data processing agreement with GDPR Art. 28 processor terms where in scope: processing on documented instructions, confidentiality, security measures, subprocessor conditions, data subject request assistance, breach notification assistance, deletion/return, audit contribution. See `../../../context/regulations/gdpr.md`.
- International transfer mechanism where applicable (adequacy, SCCs plus transfer risk assessment).
- US state law service-provider/processor terms where in scope (e.g., CCPA/CPRA "service provider" restrictions on sale/sharing) — see `../../../context/regulations/us-state-privacy.md`.
- HIPAA Business Associate Agreement where PHI is involved — see `../../../context/regulations/hipaa.md`.

## 7. Availability and resilience (criticality-driven)

- SLA with defined uptime measurement, exclusions reviewed (beware maintenance windows that swallow the SLA), and service credits (understand credits are a discount, not a remedy — pair with termination right for chronic failure).
- **RTO/RPO commitments** for Tier 1 availability-driven vendors; annual DR test with results available on request.
- Business continuity plan maintained and tested; notification of activation.
- **Exit assistance**: transition support for a defined period at defined rates; data export capability tested before you need it.

## 8. Insurance

- Cyber liability insurance at a floor appropriate to exposure (commonly $1M-$5M for mid-market engagements; scale to records held and contract value), covering breach response, third-party liability, and regulatory defense where insurable.
- Certificate of insurance on request, annually; notice of material reduction or cancellation.
- Insurance is a recovery backstop, not a control — never trade a security requirement for a bigger policy.

## 9. Liability and remedies

- Review the **liability cap** against breach scenarios: standard caps (12 months' fees) are absurd for a vendor holding millions of records. Negotiate a **super-cap** (elevated or uncapped tier) for breaches of confidentiality/security/privacy obligations. This is usually the hardest-fought clause; bring the data-volume math to legal.
- Termination rights: for material security breach, for lapsed attestation/certification uncured, for chronic SLA failure, and (regulated sectors) for regulator direction.
- Indemnity for third-party claims arising from vendor's security/privacy failures, where negotiable.

## 10. Miscellaneous but load-bearing

- **Notice contact**: security notices go to a monitored security address, not the procurement contact who left last year. Keep it current on both sides.
- Publicity restriction: vendor may not name you or describe the incident publicly without consent.
- Order of precedence: security schedule and DPA prevail over conflicting terms in the main agreement and any vendor "policy incorporated by reference" that they can change unilaterally. Reject unilateral-amendment-by-URL for security terms.
- Assignment/change of control: notification, and for Tier 1, termination right on acquisition by an unacceptable party.

## Negotiation reality check

| Clause | Usually winnable | Common vendor pushback | Minimum acceptable (Tier 1) |
|--------|-----------------|------------------------|------------------------------|
| Breach notice SLA | 48-72h; 24h with leverage | "Without undue delay" | 72h hard, clock at confirmation |
| Audit rights | Evidence + attestation delivery | On-site refused | Annual SOC 2 delivery + incident-triggered assessment |
| Subprocessor | Notice + objection | Approval refused | 30-day notice, objection with termination-as-remedy |
| Deletion certificate | Yes | Backup carve-out | Certificate + stated backup expiry max |
| Super-cap | Sometimes | Flat 12-month cap | 2-3x cap for security/privacy breaches |
| No AI-training on data | Yes (increasingly standard) | "Aggregated/de-identified" loophole | Express prohibition incl. derived models |

Track clause outcomes per vendor. "Contractual requirement rejected by vendor" is a residual risk: register it via `../../risk-assessment/SKILL.md` or accept it via `../../exception-management/SKILL.md` — never let it die in the redline history.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
