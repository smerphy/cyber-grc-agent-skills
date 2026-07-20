---
name: bcdr-readiness
description: >-
  Builds and assesses business continuity and disaster recovery readiness
  against ISO 22301 and resilience regulations such as DORA and NIS2 — scoping,
  business impact analysis, RTO/RPO gap analysis against demonstrated recovery,
  plan structure, exercise programs, and restore-test verification. Use when a
  user says "BCP", "DRP", "business continuity", "disaster recovery", "BIA",
  "RTO", "RPO", "failover exercise", or asks whether the
  organization could actually recover from a major outage.
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Establish — or honestly assess — the organization's ability to keep critical business services running and recover them after disruption. The procedure runs from scoping and business impact analysis through recovery-capability gap analysis, plan architecture, a progressive exercise program, and verified backup/restore controls, ending in a readiness report leadership can act on.

The through-line: **declared objectives mean nothing until recovery has been demonstrated.** A binder of plans with untested RTOs is documentation, not readiness, and this skill treats the difference as the main finding to surface. Every conclusion in the readiness report must cite evidence — a test result, an incident timeline, a signed BIA — or be labeled as undemonstrated.

## When to use

- The organization needs a BC/DR program built, refreshed, or independently assessed — for ISO 22301 alignment or certification (see [../../context/frameworks/iso-22301.md](../../context/frameworks/iso-22301.md)), regulatory drivers, customer contractual commitments, or board assurance after a near-miss.
- A resilience regulation applies: DORA digital operational resilience for EU financial entities ([../../context/regulations/dora.md](../../context/regulations/dora.md)), NIS2 business continuity and crisis management measures ([../../context/regulations/nis2.md](../../context/regulations/nis2.md)), or UK FCA/PRA operational resilience rules (important business services, impact tolerances, scenario testing).
- The BIA is stale (older than the last major system or org change), or RTOs were set by IT without business sign-off.
- An exercise, audit, or real incident exposed a recovery gap and someone must turn it into a remediation program rather than a one-off fix.
- **Not for:**
  - Structuring a formal clause-by-clause certification gap assessment — use [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md) with ISO 22301 as the target. This skill supplies the subject-matter judgment; that one supplies the assessment mechanics.
  - Live incident handling and regulator notification during an actual disruption — use [../incident-regulatory-reporting/SKILL.md](../incident-regulatory-reporting/SKILL.md).
  - Enterprise risk analysis feeding the risk register — use [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md); this skill consumes its output as continuity threat scenarios and returns capability gaps to it as risks.

## Inputs to gather

Ask for these before starting; do not guess:

1. **Scope**: products/services, sites, legal entities, and in-scope technology estates; any carve-outs and why.
2. **Regulatory and contractual drivers**: DORA, NIS2, FCA/PRA, sector rules; customer contracts with availability, RTO, or DR-test commitments (these often bind harder than regulation).
3. **Existing artifacts**:
   - Current BIA and BCP/DRP/crisis-management documents.
   - Exercise reports and after-action reviews from the last 2 years.
   - Backup policy, DR architecture diagrams, backup and restore logs.
   - Contracts with recovery commitments, both customer-facing and vendor-facing.
4. **Declared objectives**: RTO/RPO/MTPD per process or service, and who signed them off.
5. **Evidence of demonstrated recovery**: restore-test logs, failover exercise results, actual incident recovery timelines. Absence of evidence is itself a key input — record it.
6. **Dependency data**: critical third parties and their contractual recovery commitments, single points of failure (people, sites, systems), and the CMDB or service map if one exists.
7. **Ownership**: who owns BC (often risk/resilience) vs DR (often IT) vs crisis management (often exec/comms) — fragmented ownership is a common root cause of gaps.

## Procedure

1. **Scope the program and pin the drivers.**
   - Define in-scope products, sites, and legal entities; record carve-outs with reasons.
   - List every driver with its specific demand:
     - ISO 22301 — BCMS clause requirements and intended certification scope.
     - DORA — ICT business continuity, response and recovery, and digital operational resilience testing for EU financial entities.
     - NIS2 — business continuity, backup management, disaster recovery, and crisis management measures for in-scope entities.
     - FCA/PRA operational resilience — important business services, impact tolerances, severe-but-plausible scenario testing.
     - Customer contracts — availability commitments, RTO promises, DR-test and audit clauses.
   - Drivers set the floor for exercise frequency and evidence retention; verify current regulatory specifics against the official texts.
   - Where multiple regimes overlap, build once against the strictest and map outward rather than running parallel programs.
2. **Run or refresh the BIA.**
   - Inventory business processes (not systems), score impact over time at fixed horizons, and derive **RTO, RPO, and MTPD per critical process — with business-owner sign-off, not IT's guess**. Unsigned numbers are drafts.
   - Score impact at the process's peak period (month-end, payroll week, seasonal spikes), not its quietest — impact is time-of-year dependent, and the BIA must say when the numbers tighten.
   - Map dependencies for each critical process across all four categories: people (key-person risk, minimum headcount), technology (applications *and* the layer below them — identity, DNS, network, secrets), sites, and third parties (with their contractual recovery commitments).
   - Every system on a critical path inherits an RTO at least as tight as the process it serves — record these derived RTOs; they drive the DR architecture bill.
   - Full method, worked example, and the classic failure modes (IT-led BIAs, everything-is-critical inflation): [references/bia-guide.md](references/bia-guide.md).
   - Use the impact scales from [../../context/risk-scoring.md](../../context/risk-scoring.md) so BIA impact ratings and the enterprise risk register speak the same language.
3. **Gap the recovery capability against declared objectives.** For each critical process compare:
   - Declared RTO vs **demonstrated** restore/failover time — from timed tests or real incident timelines, never from architecture diagrams. This is the classic gap: a 4-hour declared RTO against a restore that has only ever been done in 14 hours, or never.
   - Declared RPO vs actual backup frequency, replication lag, and last verified restore point.
   - MTPD vs realistic worst-case outage duration for the dependency that fails hardest (usually a third party or a regional event).
   - Third-party contractual recovery commitments vs the process RTOs that depend on them — a 4-hour process RTO resting on a vendor with a 24-hour contractual RTO is a gap even if internal systems are fast.
   - Where no demonstration exists, the gap is "unknown capability" — treat unknown as red, not amber.
   - **Decision point:** if the organization has **never restored from backup at scale**, stop. That is the finding. Do not proceed to polishing plan documents while the foundational capability is undemonstrated — recommend a scoped restore test as the immediate next action and report everything downstream as contingent on its result.
4. **Define strategies and plans with a clean split.** Three artifact families, distinct owners and audiences:
   - **BCP** (business-owned): how the business keeps operating degraded — manual workarounds, alternate sites, people cover, customer communication, and the minimum service levels the BIA defined.
   - **DRP** (IT-owned): how technology is recovered — restore order, runbooks, failover procedures, dependency sequencing, and the credentials/tooling needed when primary systems (including the password manager and chat) are down.
   - **Crisis management plan** (exec-owned): activation and escalation criteria, decision authority, internal/external communications, regulator notification interfaces (hand off to [../incident-regulatory-reporting/SKILL.md](../incident-regulatory-reporting/SKILL.md) for the notification clocks).
   - All three plans need out-of-band access: printed or offline copies, contact trees, and communication channels that survive the loss of the primary identity provider and chat platform.
   - Strategy choices (active-active, warm standby, backup-restore, reciprocal/vendor DR) must trace to the BIA numbers: a 4-hour RTO is incompatible with a tape-restore strategy; say so where it happens, with the cost of closing the gap and the alternative of relaxing the objective — that is a business decision, so present both.
5. **Build the exercise ladder.**
   - Progress each plan up the ladder; do not skip rungs (a full failover test of a plan that has never survived a tabletop wastes an expensive slot):
     - Walkthrough — proves the plan is current, complete, and roles are assigned.
     - Tabletop — proves decision-making, escalation, and communications under a timed scenario.
     - Functional/component test — real technical action on a bounded scope, producing timing data.
     - Full-scale test — end-to-end recovery of a critical service, ideally with business users transacting on the recovered environment.
   - Set frequency by process criticality tier with the regulatory floor as minimum; re-test affected plans after major changes, not just on the calendar.
   - Design scenarios that stress known weak points — ransomware with backup encryption, regional cloud outage, key-vendor failure — and write injects that force real decisions under incomplete information.
   - Executives personally participate in crisis-management exercises — a delegate-attended crisis exercise proves only that the delegates can manage a crisis.
   - **Exercises that find problems are successes; a clean exercise report streak is a design smell, and regulators and auditors increasingly read it that way.**
   - Scenario library, inject design, after-action format, and evidence expectations: [references/exercise-program.md](references/exercise-program.md).
6. **Verify backup/restore controls with real restore tests.**
   - Backup job success logs are not evidence of recoverability — restores are.
   - Test restore of representative systems and data at realistic scale, timed, from the actual media/tier that would be used in a disaster.
   - Include at least one restore from immutable/offline copies under a ransomware assumption (primary backups presumed compromised).
   - Verify integrity of the restored data, not just job completion — corrupt restores pass job-status checks.
   - Rotate the sampled systems each cycle so coverage accumulates instead of re-testing the easiest system annually.
   - Restore into an isolated environment when testing under a ransomware assumption, so the test itself cannot reintroduce compromised artifacts into production.
   - Run these as formal control tests with workpapers via [../control-testing/SKILL.md](../control-testing/SKILL.md), and check coverage against the resilience and backup controls in [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md) (redundancy, backup, ICT readiness for business continuity).
7. **Report readiness with a heat map.**
   - One row per critical process: declared objectives, demonstrated capability, gap, and evidence age. Stale evidence (older than the refresh cycle) downgrades the rating.
   - Route capability gaps into the risk register via [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md) with owners and deadlines; feed systemic findings back into strategy (step 4) and the exercise plan (step 5).
   - Set the review cycle: BIA refresh annually and on major change; exercise calendar rolling 12 months; readiness report to leadership at least annually.

## Output format

Deliver a readiness report with, in order:

1. Scope and drivers (regulatory/contractual demands with the specific clause or commitment)
2. BIA summary (critical processes, RTO/RPO/MTPD, sign-off status, dependency highlights)
3. Capability gap analysis (declared vs demonstrated, evidence cited per row)
4. Plan architecture status (BCP/DRP/crisis plan coverage and owners)
5. Exercise program (ladder position per plan, last results, next 12 months)
6. Findings and remediation plan (owner, deadline, risk-register reference)
7. Readiness heat map

Worked example (heat map rows):

| Process | RTO (declared) | Demonstrated | RPO (declared) | Demonstrated | Evidence | Rating |
|---|---|---|---|---|---|---|
| Customer payments | 4h | 6h 20m (failover test 2026-03) | 15m | 15m (replication verified) | Test report EX-2026-03 | Amber — RTO gap, remediation in flight |
| Payroll | 24h | Never tested | 24h | Backups succeed; restore never tested | None | Red — unknown capability |
| Corporate website | 8h | 45m (auto-failover, incident 2026-01) | 1h | 5m | Incident PIR-2026-01 | Green |

Worked example (findings and remediation rows, section 6):

| ID | Finding | Source | Owner | Deadline | Risk ref |
|----|---|---|---|---|---|
| B-04 | Payroll restore never demonstrated; capability unknown | Gap analysis step 3 | IT Ops Director | 2026-10-15 | RR-118 |
| B-07 | Restore order for identity provider undocumented; DRP assumes SSO is up | Tabletop EX-2026-05 | Infrastructure Lead | 2026-09-01 | RR-121 |

Rating rules for the heat map: **Green** = demonstrated capability meets declared objectives with evidence inside the refresh cycle. **Amber** = demonstrated but short of objective, with remediation owned and dated. **Red** = objective breached with no remediation path, or capability unknown (never tested). Unknown is never amber.

## Quality checklist

- [ ] Scope names products, sites, and legal entities; every regulatory and contractual driver is listed with its specific demand
- [ ] Every critical process has RTO/RPO/MTPD signed off by the business owner, not just IT
- [ ] Dependencies mapped across all four categories: people, technology (including the identity/DNS/secrets layer), sites, third parties
- [ ] Third-party recovery commitments compared against the process RTOs that depend on them
- [ ] Gap analysis compares declared objectives to **demonstrated** capability with cited evidence; unknowns rated red
- [ ] If at-scale restore has never been done, it is the headline finding — not buried in an appendix
- [ ] BCP, DRP, and crisis management plans are distinct artifacts with distinct owners; strategies trace to BIA numbers, with cost-vs-objective tradeoffs surfaced as business decisions
- [ ] Exercise ladder defined per plan with frequency tied to criticality and regulatory floor; scenarios include ransomware-with-backup-encryption
- [ ] At least one restore test from immutable/offline copies completed or scheduled, documented as a formal control test with integrity verification
- [ ] Exercise reports record problems found and fixes tracked to closure — no problem-free streaks accepted at face value
- [ ] Findings routed to the risk register with owners and deadlines; BIA and exercise refresh cycle set
- [ ] Readiness ratings degrade automatically when evidence ages past the refresh cycle

## References

- [references/bia-guide.md](references/bia-guide.md) — BIA method, impact-over-time scoring, RTO/RPO/MTPD derivation with worked example, common failures
- [references/exercise-program.md](references/exercise-program.md) — exercise ladder, scenario library, injects, after-action format, evidence expectations
- [../../context/frameworks/iso-22301.md](../../context/frameworks/iso-22301.md) — ISO 22301 BCMS structure and requirements
- [../../context/regulations/dora.md](../../context/regulations/dora.md) — DORA digital operational resilience obligations for financial entities
- [../../context/regulations/nis2.md](../../context/regulations/nis2.md) — NIS2 continuity and crisis-management measures
- [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md) — resilience, redundancy, and backup controls in the ISMS
- [../../context/risk-scoring.md](../../context/risk-scoring.md) — shared impact scales for BIA and risk register
- [../control-testing/SKILL.md](../control-testing/SKILL.md) — formal testing of backup/restore and failover controls
- [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md) — risk-register intake for capability gaps; threat scenarios feeding the BIA
- [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md) — clause-by-clause ISO 22301 certification gap mechanics
- [../incident-regulatory-reporting/SKILL.md](../incident-regulatory-reporting/SKILL.md) — regulator notification during an actual disruption

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
