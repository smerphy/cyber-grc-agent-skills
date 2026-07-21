# Workflow: BC/DR Exercise Cycle

```yaml
name: bcdr-exercise-cycle
description: >-
  Standing program of continuity and recovery exercises: an annual calendar
  scaled by BIA criticality, design across the escalation ladder from walkthrough
  to full restore test, execution with measured RTO/RPO against declared targets,
  gap findings and remediation tracking, and readiness metrics to governance.
skills_used:
  - bcdr-readiness
  - risk-assessment
  - exception-management
  - grc-metrics-reporting
typical_duration: rolling 12-month calendar; individual exercises half a day (walkthrough) to multi-day (full restore test)
roles:
  - risk-manager
  - grc-analyst
  - internal-auditor
```

## Trigger

- The annual planning point for the rolling exercise calendar (commonly aligned to the BIA refresh).
- A major change forcing off-cycle re-testing of affected plans: platform migration, new data center or cloud region, acquisition, or a key-vendor swap — change-driven tests, not just calendar ones.
- A real disruption or near-miss that revealed a recovery gap; exercise the fix once implemented.

## Prerequisites

- A current, business-signed BIA with RTO/RPO/MTPD per critical process (see [bcdr-readiness](../skills/bcdr-readiness/SKILL.md)); unsigned numbers are drafts and cannot anchor pass/fail.
- Distinct BCP (business-owned), DRP (IT-owned), and crisis management (exec-owned) plans to exercise.
- Regulatory and contractual floors identified: resilience-testing expectations under DORA-type regimes for financial entities, NIS2-style continuity measures, and customer contracts with DR-test clauses often set minimum frequency and evidence retention — verify the specific obligations against the official texts and contracts.
- Budget and change-window agreements for functional and full-scale tests — these compete with delivery work and lose without pre-commitment.

## Steps

### 1. Annual calendar scaled by criticality — risk-manager

- **Skill:** [bcdr-readiness](../skills/bcdr-readiness/SKILL.md) (exercise ladder step)
- **Inputs:** BIA criticality tiers; each plan's current ladder position; last cycle's results; regulatory/contractual floors.
- **Actions:** build the rolling 12-month calendar: highest-criticality processes get the most demanding rung they are ready for, every in-scope plan gets at least a walkthrough, and regulatory floors set minimums, not targets. Sequence up the ladder — walkthrough → tabletop → functional failover → full restore test — and never skip rungs: a full failover of a plan that has not survived a tabletop wastes an expensive change window. Reserve slack for change-driven re-tests.
- **Outputs:** approved exercise calendar with scope, rung, date, and owner per exercise.
- **Decision gate:** if any critical process has never had an at-scale restore demonstrated, its restore test is scheduled first and everything downstream is contingent — that is the program's headline until closed.

### 2. Exercise design — grc-analyst with plan owners

- **Skill:** [bcdr-readiness](../skills/bcdr-readiness/SKILL.md) (exercise-program reference for scenarios, injects, evidence expectations)
- **Inputs:** calendar entry; plan documents; declared RTO/RPO for in-scope processes; known weak points from prior cycles.
- **Actions:** design per rung. Walkthrough: verify currency, completeness, role assignments. Tabletop: timed scenario with decision-forcing injects — stress known weak points (ransomware with backup encryption, regional cloud outage, key-vendor failure), and put executives personally in crisis-management exercises. Functional/full-scale: define success criteria numerically before the test — target restore time, target data-loss window, integrity checks on restored data — plus rollback criteria and an isolated environment for ransomware-assumption restores so the test cannot reinfect production. Every technical test is instrumented to produce timing evidence.
- **Outputs:** exercise plan with scenario, injects, measured success criteria, safety/rollback conditions.

### 3. Execution with measurement — plan owners execute; grc-analyst records; internal-auditor observes high-stakes tests

- **Skill:** [bcdr-readiness](../skills/bcdr-readiness/SKILL.md) (restore verification step); formal evidence via [control-testing](../skills/control-testing/SKILL.md)
- **Inputs:** exercise plan; declared targets.
- **Actions:** run the exercise and measure honestly: elapsed wall-clock time from declared start to verified service restoration (not "restore command completed"), achieved restore point versus RPO, and integrity verification of restored data — corrupt restores pass job-status checks. Record deviations from the runbook as they happen; improvisation that saved the test is a documentation finding. No mid-test rescoping to protect the result: an aborted or assisted test is recorded as such. Restore tests are documented as formal control tests with workpapers.
- **Outputs:** timed results, evidence artifacts (logs, screenshots, workpapers), deviation log.

### 4. Gap analysis against declared targets — risk-manager

- **Skill:** [bcdr-readiness](../skills/bcdr-readiness/SKILL.md) (gap analysis step); [risk-assessment](../skills/risk-assessment/SKILL.md) for register intake
- **Inputs:** measured results; declared RTO/RPO/MTPD; BIA dependency map.
- **Actions:** compare demonstrated capability to declared objectives per process. A declared RTO without a demonstrated recovery is a hypothesis, not a capability — never-tested rates red ("unknown"), not amber. Where demonstrated recovery misses the declared target, raise a gap finding and route it into the risk register with owner and deadline; where the miss is structural (a 4-hour RTO on a backup-restore architecture), present the business choice explicitly: fund the capability or formally relax the objective with the process owner's signature. Check third-party dependencies too — a fast internal restore behind a vendor with a 24-hour commitment is still a gap.
- **Outputs:** updated capability heat map (declared vs demonstrated, evidence cited); gap findings in the risk register.
- **Decision gate:** any critical process rated red goes to the risk owner within days of the exercise, not in the annual report.

### 5. Remediation tracking and accepted gaps — grc-analyst tracks; risk-manager escalates

- **Skill:** [exception-management](../skills/exception-management/SKILL.md) for formally accepted gaps
- **Inputs:** gap findings with owners and deadlines; remediation plans.
- **Actions:** track each finding to closure, and closure means re-demonstration — a gap is closed by a passing re-test, not by a ticket marked done. Schedule the re-test into the calendar (step 1 slack). Where the business decides to live with a gap (cost of closing exceeds appetite), record it as a formal, time-bound risk acceptance with the approval authority the risk level requires — never a quietly stale finding. Slipped remediation dates escalate through the risk register, not through the BC coordinator's patience.
- **Outputs:** remediation tracker; re-test schedule; formally recorded acceptances.

### 6. Readiness metrics to governance — grc-analyst prepares; risk-manager presents

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md)
- **Inputs:** heat map; calendar completion status; findings aging; acceptance register.
- **Actions:** report the readiness picture at least annually, with quarterly pulse metrics: exercise calendar completion rate, percentage of critical processes with in-cycle demonstrated recovery, RTO/RPO attainment (demonstrated vs declared), findings open past deadline, and evidence age — stale evidence downgrades ratings automatically. Present gaps in business terms (hours of payroll outage, not replication topology). For regulated entities, package exercise evidence to the applicable testing expectations — regimes like DORA carry programmatic resilience-testing requirements whose specifics should be verified against the official text. A clean streak of problem-free exercises is reported as a design concern, not an achievement.
- **Outputs:** readiness report and heat map to governance; minuted decisions on funding or objective changes; next cycle's calendar inputs.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Rolling exercise calendar | 1 | BC/DR program plan |
| Exercise plans with success criteria | 2 | Exercise file |
| Timed results and workpapers | 3 | Exercise file (audit evidence) |
| Capability heat map + gap findings | 4 | Readiness report; risk register |
| Remediation tracker + acceptances | 5 | Risk register; exception register |
| Readiness report and metrics | 6 | Governance pack |

## Failure modes

- **Paper confidence.** Declared RTOs presented to the board as capabilities when they have never been demonstrated. Step 4's rule — undemonstrated is red — is the antidote; unknown is never amber.
- **Ladder skipping.** Jumping to an expensive full failover for a plan that has not survived a tabletop, burning the year's change window on discovering the contact list is stale.
- **The pet system.** Testing the same well-behaved application every year while the ugly legacy dependencies go untouched. Rotate coverage so it accumulates across the estate.
- **Success-engineered tests.** Pre-staged data, the vendor's best engineer on standby, scope trimmed mid-test — the result measures the choreography, not the capability. Record assists and aborts as what they are.
- **Findings without re-tests.** Remediation tickets closed on assertion, gap re-appears in next year's exercise. Closure requires a passing re-demonstration, scheduled in the calendar.
- **Calendar-only testing.** Annual tests on schedule while a platform migration silently invalidates the DRP mid-year. Material change triggers a re-test of affected plans, not a note for next year.
- **Quiet objective erosion.** Missed targets "fixed" by relaxing the RTO without the business owner's signature. Objective changes are business decisions made explicitly in step 4, or they are just gap-hiding.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
