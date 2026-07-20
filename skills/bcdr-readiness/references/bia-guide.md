# BIA Guide — Method, Scoring, and RTO/RPO/MTPD Derivation

Business impact analysis method for Step 2 of the BCDR readiness skill: process inventory, impact-over-time scoring, objective derivation with a worked example, dependency capture, and the failure modes that make BIAs worthless.

## What the BIA is for

The BIA answers one question per business process: **how fast does disruption become intolerable, and how much data loss is survivable?** Everything else — recovery strategy, DR architecture spend, exercise priority — derives from those answers. The BIA is a business exercise that consumes technical input, not a technical exercise that gets business review at the end.

## Method

### 1. Build the process inventory

- Enumerate business processes per function (order-to-cash, payroll, customer onboarding, claims handling, production line X), not systems. Target 20–60 processes for a mid-size organization; hundreds means the granularity is wrong.
- For each process record: owner (named person), function, description, peak periods (month-end, open-enrollment, Black Friday — impact is time-of-year dependent), and the products/services it supports.
- Where FCA/PRA-style operational resilience rules apply, map processes up to **important business services** (the customer-facing service whose disruption causes harm) — regulators anchor on services, not internal processes.

### 2. Score impact over time

For each process, score the impact of total disruption at fixed time horizons — typically **4 hours, 24 hours, 3 days, 1 week, 1 month** — across impact categories:

- Financial (direct loss, penalties, lost revenue)
- Customer/service (harm, churn, SLA breach)
- Legal/regulatory (missed statutory deadlines, reportable events)
- Reputational
- Health & safety (where relevant — score it first; it dominates)

Use the same impact scale anchors as the enterprise risk register (see the risk-scoring context pack) so a "3" means the same thing in both documents. Score each horizon independently; the point of the exercise is finding where the curve steepens.

### 3. Derive the objectives

- **MTPD** (maximum tolerable period of disruption): the horizon at which impact reaches the intolerable threshold defined with leadership (e.g., first "4"/severe score). This is a business fact, not a preference.
- **RTO** (recovery time objective): target time to restore the process to an acceptable level. Set RTO comfortably inside MTPD — a common rule of thumb is 50–80% of MTPD — to leave margin for detection, decision, and overrun; record the margin chosen and why.
- **RPO** (recovery point objective): maximum tolerable data loss, in time. Derived from re-entry feasibility: can the process reconstruct lost transactions from other sources (email trails, counterparty records, paper), and at what cost? If reconstruction is impossible, RPO approaches zero and the architecture bill follows.
- **Minimum service level during disruption**: what "acceptable level" means concretely (e.g., "process priority payments manually at 20% throughput") — this defines what the BCP workaround must deliver.

### 4. Get business-owner sign-off

The named process owner signs the impact scores and the derived RTO/RPO/MTPD. Unsigned numbers are drafts. Sign-off forces the conversation that gives the numbers meaning: "you scored 4 hours as intolerable — that implies a hot-standby cost of roughly X; still intolerable?" Iterate until the owner accepts both the number and its cost implication.

### 5. Capture dependencies

For each critical process (those with the tightest MTPDs), map what it needs to run:

- **People**: teams, minimum headcount, key-person single points of failure, cross-training status.
- **Technology**: applications, data stores, integrations, and — critically — the *upstream* systems each application needs (identity provider, DNS, network, secrets manager: the dependencies that make "restore order" a hard problem).
- **Sites**: buildings, physical equipment, work-from-anywhere feasibility per role.
- **Third parties**: vendors and their contractual recovery commitments. A 4-hour process RTO resting on a vendor with a 24-hour contractual RTO is a gap; record it in the capability gap analysis, and feed the vendor into third-party risk review.

Record dependency RTOs implied by the process RTO: every system on the critical path inherits an RTO at least as tight as the process it serves.

## Worked example — payments processing

Process: outbound customer payments (payroll-adjacent B2B payment runs). Owner: Head of Treasury Operations. Peak: month-end.

Impact-over-time (scale 1 negligible – 4 severe):

| Horizon | Financial | Customer | Legal/Reg | Reputation | Notes |
|---|---|---|---|---|---|
| 4h | 1 | 1 | 1 | 1 | Same-day runs can be delayed intra-day |
| 24h | 2 | 2 | 2 | 2 | Miss same-day settlement; manual workaround for priority payments |
| 3 days | 3 | 3 | 3 | 3 | Contractual late-payment penalties; counterparty escalation |
| 1 week | 4 | 4 | 4 | 3 | Regulatory reporting obligations missed; material harm |

Derivation:

- **MTPD = 5 business days** (impact reaches severe between day 3 and 1 week; leadership set the intolerable line at 5 days, worse at month-end — noted as a peak-period tightening to 3 days).
- **RTO = 48h** (well inside MTPD; margin covers detection and decision time; month-end runs demand a documented manual priority-payment workaround inside 24h — that workaround is the BCP's job).
- **RPO = 4h** (payment instructions can be reconstructed from the ERP and bank confirmations, but reconciliation cost beyond ~4h of lost transactions was judged intolerable by the owner).
- **Minimum service level**: priority payments (payroll, regulatory, top-20 counterparties) processed manually via banking portal at up to 50 payments/day.
- Dependencies: treasury team (min 2 trained approvers — currently 2, key-person risk flagged), payments application → ERP → identity provider → HSM/signing service (all inherit ≤48h RTO), bank portal (third party, contractual availability 99.9% but no DR commitment in contract — gap logged), office not required (remote-capable).

Sign-off: Head of Treasury Operations, 2026-05-14.

## Common failures

1. **IT-led BIAs without business input.** IT guesses impact, sets RTOs to match current architecture, and the BIA becomes a mirror of what exists instead of a statement of what the business needs. Detectable by: RTOs that exactly equal current capability, and no business signatures.
2. **Everything-is-critical inflation.** Every owner claims a 4-hour RTO because criticality feels like status and nobody is shown the cost. Fix: present the cost curve per RTO tier and force ranking ("you may place two processes in tier 1"). If more than ~20% of processes land in the top tier, the tiers are not doing their job.
3. **Scoring the process at its quietest.** Payroll disruption scored in mid-month, retail scored in February. Always score at peak, and note peak windows.
4. **Confusing RTO with MTPD** — publishing MTPD as the recovery target leaves zero margin for detection and decision; recovery that starts late then breaches tolerance by design.
5. **RPO set without a re-entry analysis.** "RPO = 24h because backups are nightly" is capability masquerading as requirement — the same inversion as failure 1.
6. **Dependencies stop at the application layer.** The restore-order problem lives in the layer below: identity, DNS, network, secrets, backup infrastructure itself. If the BIA's dependency map omits them, the DRP's restore sequence will be discovered live, mid-disaster.
7. **One-and-done.** A BIA older than the last reorg, major system migration, or acquisition describes a company that no longer exists. Refresh annually and on major change.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
