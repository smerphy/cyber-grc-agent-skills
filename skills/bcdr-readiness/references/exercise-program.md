# Exercise Program — Ladder, Scenarios, Injects, and Evidence

Design of the BC/DR exercise program for Step 5 of the BCDR readiness skill: exercise types, the maturity ladder, a scenario library, inject design, after-action format, and what auditors and regulators accept as evidence.

## Exercise types and the ladder

Progress each plan up the ladder; do not skip rungs (a full failover test of a plan that has never survived a tabletop wastes an expensive slot proving the plan is unreadable).

| Rung | Type | What happens | Proves | Typical duration |
|---|---|---|---|---|
| 1 | Walkthrough / plan review | Owner and participants read the plan step by step | Plan is current, complete, roles assigned | 1–2h |
| 2 | Tabletop | Facilitated scenario discussion with timed injects; decisions made verbally | Decision-making, escalation, communications, plan logic under pressure | 2–4h |
| 3 | Functional / component test | Real technical action on a bounded scope: restore one system, fail over one component, activate the alternate site for one team | Demonstrated capability for the component; timing data | 0.5–2 days |
| 4 | Full-scale test | End-to-end failover or recovery of a critical service, ideally with business users transacting on the recovered environment | Demonstrated RTO/RPO for the service; restore-order correctness | 1–3 days |

Frequency by criticality (treat as a floor and tighten where a regulator or contract demands more — verify current DORA/FCA/PRA testing expectations against the official texts):

- **Tier 1 (tightest MTPD)**: tabletop annually + functional test annually + full-scale test every 1–2 years.
- **Tier 2**: tabletop annually + functional test every 1–2 years.
- **Tier 3**: walkthrough/tabletop annually.
- Crisis management plan: exercised annually at minimum, with executives personally participating — a delegate-attended crisis exercise proves the delegates can manage a crisis.
- After any material change (platform migration, new data center/region, acquisition): re-test the affected plan within the next two quarters regardless of calendar.

## Scenario library

Eight scenarios covering the failure modes that break real organizations. Rotate — never run the same scenario twice in a row.

1. **Ransomware with backup encryption.** Attacker has been resident 3 weeks; primary backups are encrypted or deleted; only the immutable/offline tier survives, and it is N days old. Forces: restore from last-resort media, RPO-loss acceptance decision, negotiate-or-rebuild decision, regulator/customer notification (link the incident-reporting skill), and payroll-week timing pressure. The single most valuable scenario — run it before any other cyber scenario.
2. **Regional cloud outage.** Primary cloud region degraded for 18+ hours; status page vague. Forces: the fail-over-or-wait decision with incomplete information, discovery of hidden single-region dependencies (identity, DNS, CI/CD, secrets), and cost/consistency tradeoffs of cross-region failover.
3. **Key-vendor failure.** A critical SaaS or outsourced-operations vendor suffers its own disaster (or insolvency-driven sudden shutdown). Forces: manual workaround activation, contractual-commitment reality check, data egress under duress, substitution timelines.
4. **Primary site loss.** Fire, flood, or access denial at the main office/plant/data center. Forces: people relocation, physical-equipment dependencies, work-from-anywhere gaps for specialist roles.
5. **Mass staff unavailability.** Pandemic wave, severe weather, or industrial action removes 40% of staff including two named key people. Forces: key-person single points of failure, cross-training reality, minimum-headcount assumptions from the BIA.
6. **Data corruption discovered late.** A batch job has been silently corrupting records for 12 days — inside every recent backup. Forces: point-in-time restore selection, corruption-vs-availability tradeoff, reconciliation and re-entry at scale (tests the RPO re-entry analysis honestly).
7. **Extended power/network loss.** Utility failure beyond generator/UPS runtime at a site hosting critical infrastructure. Forces: graceful-shutdown sequencing, restore-order on power return, dependency on fuel/telecom vendors.
8. **Crisis communications meltdown.** Any of the above, plus: the incident is trending publicly, a journalist has a partially wrong story on a deadline, customers are calling, and internal chat is down (it ran on the failed platform). Forces: out-of-band communication channels, holding-statement discipline, spokesperson designation, regulator-vs-media sequencing.

## Inject design

Injects are timed information drops that force decisions. Good injects:

- Arrive on a **realistic clock** (the ransom note before the backup status; the journalist call mid-restore) and via realistic channels (email the actual crisis inbox, don't just narrate).
- Are **incomplete or partially wrong**, like real incident information — teams must decide with uncertainty, and one inject should later be corrected.
- Target **specific decisions**: activate the plan or wait; fail over or hold; pay-or-rebuild posture; notify now with partial facts or wait (tie to real notification clocks); accept N hours of data loss or attempt salvage.
- Include at least one **absent-person inject** ("the DR lead is on a plane for 9 hours") to test deputies and documented handoffs.
- Are scripted in advance with expected actions per inject, so the after-action review can compare expected vs actual instead of relying on facilitator memory.

## After-action format

Produce the after-action report within 10 business days, while memory is fresh. Sections:

1. **Exercise metadata**: scenario, type/rung, date, duration, facilitator, participants and roles, scope, objectives.
2. **Timeline**: injects and actual responses with timestamps; measured times against targets (detection → activation → recovery milestones vs RTO; data currency vs RPO).
3. **What worked** — capabilities demonstrated, with evidence.
4. **Findings** — each with: description, severity, root cause (plan gap / capability gap / knowledge gap / dependency gap), owner, deadline. Route capability findings into the risk register.
5. **Objective results**: met / partially met / not met, per stated exercise objective. It is normal and healthy for some objectives to be "not met".
6. **Plan and program changes**: specific document updates triggered, and next exercise recommendation (repeat this rung vs advance).

Track findings to closure in the same system as audit findings — an after-action report whose actions evaporate is theater.

## Evidence auditors and regulators expect

- A **rolling exercise calendar** (12+ months forward) tied to process criticality tiers, and the record of the last 2–3 years actually executed against it.
- After-action reports **containing findings and closed remediation actions**. Auditors and regulators treat a streak of problem-free exercises as evidence the exercises are too easy, not that the program is mature — an exercise that finds problems and closes them is the strong artifact.
- **Timed results vs declared objectives**: measured restore/failover durations against RTO, measured data currency against RPO, for the critical services — not just "test completed successfully".
- **Restore-test workpapers** for backup evidence (scope, media/tier used, timing, verification of restored-data integrity) — backup job logs alone do not demonstrate recoverability. Run these through the control-testing skill's workpaper format.
- **Scenario coverage** including severe-but-plausible cyber scenarios (ransomware with backup compromise) — resilience regimes such as DORA and the UK operational-resilience rules expect scenario testing at severity, not convenience; verify the applicable regime's current testing requirements (scope, frequency, and any threat-led testing obligations) against the official text.
- **Participation records** showing executives in crisis exercises and business users in full-scale tests.
- Evidence of the **change-triggered re-tests**, not only calendar ones.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
