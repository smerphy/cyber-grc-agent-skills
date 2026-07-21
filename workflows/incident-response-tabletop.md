# Workflow: Incident Response Tabletop Exercise

```yaml
name: incident-response-tabletop
description: >-
  Design and run a tabletop that tests decisions, not slide-reading: objectives
  drawn from the current risk register, decision-forcing injects including the
  regulatory-notification call under time pressure, executive participation,
  structured observation, hot-wash, and findings tracked to verified plan updates.
skills_used:
  - risk-assessment
  - incident-regulatory-reporting
  - bcdr-readiness
  - grc-metrics-reporting
typical_duration: 4-6 weeks design-to-report; the exercise itself is 2-4 hours
roles:
  - grc-analyst
  - risk-manager
  - compliance-officer
```

## Trigger

- The annual (or regulator/customer-driven) exercise calendar slot for incident response.
- A material change that invalidates current muscle memory: new IR plan or leadership, major architecture shift, a merger, or a near-miss that exposed decision confusion.
- A real incident handled badly — exercise the specific failure within a quarter, while the appetite to fix it exists.

## Prerequisites

- A current, approved incident response plan with named roles — a tabletop for a plan that does not exist is a drafting workshop, run that first.
- A current risk register (see [risk-assessment](../skills/risk-assessment/SKILL.md)); the exercise should test risks the organization claims matter.
- Executive calendar commitment secured 4-6 weeks out — crisis roles must be played by the people who hold them, not delegates.
- A facilitator who is not a player, and a scribe who is not the facilitator.

## Steps

### 1. Objectives and scope from the risk register — risk-manager

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (register as input)
- **Inputs:** current risk register top-risk shortlist; prior exercise and incident lessons-learned; audit findings on IR.
- **Actions:** pick the scenario domain from the register — if ransomware and third-party compromise are your stated top risks, exercise one of those, not a generic "hacker" story. Write 3-5 testable objectives as decisions to observe ("does the team reach a notify/no-notify position within the session", "is severity escalated to the executive tier per the plan's criteria"), not activities ("discuss roles"). Define scope: which teams play, what is simulated, what is out of bounds.
- **Outputs:** objectives statement; scope; scenario domain with register cross-reference.

### 2. Scenario design with injects — grc-analyst, reviewed by compliance-officer

- **Skill:** [incident-regulatory-reporting](../skills/incident-regulatory-reporting/SKILL.md); inject craft per [bcdr-readiness](../skills/bcdr-readiness/SKILL.md) (exercise ladder step and its exercise-program reference)
- **Inputs:** objectives; realistic technical detail from engineering; [breach notification timelines](../context/crosswalks/breach-notification-timelines.md).
- **Actions:** build a timeline of 6-12 injects that force decisions under incomplete information — each inject should make someone choose something, escalate, or communicate; an inject that only informs is scenery. Include the regulatory-notification decision under time pressure: an inject establishing probable personal-data or service impact, so players must determine which regimes are plausibly triggered, when each clock starts (awareness/discovery/determination differ by regime — this is where teams get it wrong), and who owns the call. Add ambiguity on purpose (conflicting forensics, a journalist inquiry, a key responder on leave). Script expected-response notes per inject so observers can score against the plan.
- **Outputs:** master scenario events list with inject timings and expected responses; facilitator pack.
- **Decision gate:** dry-run the scenario with the facilitator and one technical reviewer. Injects that players can dismiss as unrealistic kill the exercise in the room — fix them now.

### 3. Participants and logistics — grc-analyst

- **Inputs:** scope; IR plan role assignments.
- **Actions:** invite the people who hold the roles: incident commander, technical leads, legal/privacy, communications, HR if insider-relevant — and the executives who would approve ransom positions, public statements, and notification decisions. A delegate-attended exercise proves only that delegates can manage a crisis. Brief players on format and the no-fault ground rule (the exercise tests the plan, not the people); do not pre-share injects. Position observers with structured capture sheets keyed to the step 1 objectives.
- **Outputs:** confirmed roster with role mapping; observer assignments; logistics confirmed.

### 4. Facilitation and observation capture — risk-manager facilitates; grc-analyst leads observation

- **Inputs:** facilitator pack; observation sheets.
- **Actions:** run the timeline, holding time pressure — decisions on the clock, not after leisurely debate; that pressure is the test. Let wrong turns play out long enough to surface consequences before correcting. Capture verbatim: decisions made and by whom, escalations, where the plan was consulted versus improvised, the notification position and its reasoning, and any moment players did not know who owned a call. Note where injects landed flat for the exercise's own lessons.
- **Outputs:** timestamped observation log; decision record.

### 5. Hot-wash — risk-manager facilitates, all players

- **Inputs:** fresh memory; observation log.
- **Actions:** 20-30 minutes immediately after, while candor is high: each player names one thing that worked and one that would have hurt in a real incident; facilitator replays the 2-3 pivotal decision moments and asks whether the plan helped or was bypassed. Capture, do not litigate — analysis comes in step 6. Collect written feedback before the room empties.
- **Outputs:** hot-wash notes; player feedback.

### 6. Lessons-learned report and findings routing — grc-analyst drafts; risk-manager owns

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (register intake for capability gaps)
- **Inputs:** observation log, decision record, hot-wash notes; objectives.
- **Actions:** report against the objectives: met, partially met, or failed, with evidence from the log. Convert observations into findings with a named owner and due date — "communications were confusing" is an anecdote; "no one owned the regulator-notification decision for 40 minutes; owner: General Counsel; fix by: date" is a finding. Route capability gaps into the risk register; route notification-process gaps to the [incident-regulatory-reporting](../skills/incident-regulatory-reporting/SKILL.md) process owner. An exercise that found problems succeeded — a problem-free report is a design smell.
- **Outputs:** lessons-learned report; findings register entries with owners and dates.
- **Decision gate:** every finding has an owner and a date before the report is issued. Unowned findings are filed observations, and filed observations recur in the next real incident.

### 7. Plan updates verified and metrics — grc-analyst; compliance-officer confirms closure

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md)
- **Inputs:** findings register; IR plan and playbooks.
- **Actions:** track each finding to a verified change — an updated plan section, a corrected contact tree, a new decision matrix — and check the fix landed in the published plan, not a draft nobody reads. Re-test material fixes in the next exercise (carry them in as injects). Report to governance: exercise conducted, objectives result, findings open/closed, executive participation — these feed the exercise-program metrics and any regulatory testing-expectation evidence (verify specific regime requirements against the official text).
- **Outputs:** verified plan updates; closure evidence; governance metrics.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Objectives and scope statement | 1 | Exercise file |
| Scenario and facilitator pack | 2 | Exercise file (restricted pre-exercise) |
| Roster and role mapping | 3 | Exercise file |
| Observation log and decision record | 4 | Exercise file (audit evidence) |
| Hot-wash notes | 5 | Exercise file |
| Lessons-learned report + findings | 6 | Findings tracker; risk register |
| Verified plan updates + metrics | 7 | IR plan repository; governance pack |

## Failure modes

- **The briefing disguised as an exercise.** Facilitator walks through slides, players nod, no decision is ever forced. If nobody had to choose anything under pressure, you validated attendance, not response.
- **Executive no-show.** Delegates play the roles that matter, and the first time the real CEO faces a ransom decision is during a real ransom. Book principals first; reschedule the exercise before accepting substitutes.
- **Regulatory clock hand-waving.** Players say "legal will handle notification" and the inject dies. Force the position: which regimes, from what trigger moment, decided by whom — during the session, not as a parking-lot item.
- **Scenario fantasy.** Technically impossible injects let players dismiss the whole exercise. The step 2 dry-run with a technical reviewer is the fix.
- **Grading people instead of the plan.** Players who feel judged perform for the room and hide confusion — which is the exact data you need. No-fault framing, stated up front and honored in the report.
- **Findings to nowhere.** A lessons-learned document filed unread, same gaps next year. Findings get owners, dates, register entries, and verified closure — step 7 is the difference between an exercise program and annual theater.
- **Same scenario, every year.** Ransomware again, because the pack exists. Rotate scenario domains through the register's top risks and carry forward last year's fixes as this year's injects.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
