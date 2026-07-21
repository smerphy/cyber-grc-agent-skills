# Workflow: Security Exception Lifecycle

```yaml
name: exception-lifecycle
description: >-
  Full life of a policy/control exception: validated intake with business
  justification, residual risk scoring, compensating controls, risk-proportionate
  approval, time-bounded register entry, monitoring during the term, disciplined
  expiry handling, and portfolio-level exception reporting to governance.
skills_used:
  - exception-management
  - risk-assessment
  - grc-metrics-reporting
typical_duration: 5-10 business days intake-to-decision; lifecycle runs the exception term (max 12 months per cycle)
roles:
  - grc-analyst
  - risk-manager
  - compliance-officer
```

## Trigger

- A team cannot or will not meet a specific policy, standard, or control requirement and requests a deviation ("we need TLS 1.0 for a legacy client", "this server can't run EDR").
- Monitoring, audit, or [control testing](../skills/control-testing/SKILL.md) discovers a deviation already live in production — run the workflow from discovery; the unmanaged period is recorded, never backdated.
- An existing exception reaches its review date — enter at step 6.

## Prerequisites

- A citable policy/standard framework — you cannot except a requirement nobody can name. Requirement defects route to [policy-review](../skills/policy-review/SKILL.md), not the exception queue.
- Risk scoring methodology and appetite thresholds (see [risk scoring](../context/risk-scoring.md)); an approval authority matrix, or willingness to adopt the default in [exception-management](../skills/exception-management/SKILL.md).
- An exception register as system of record, cross-referenced to the risk register.
- The intake form: [exception request template](../templates/exception-request.md).

## Steps

### 1. Intake and validation — grc-analyst

- **Skill:** [exception-management](../skills/exception-management/SKILL.md) (validate step)
- **Inputs:** completed [exception request](../templates/exception-request.md): requirement cited, named scope, business justification, requested duration, exit plan, proposed compensating controls.
- **Actions:** confirm the deviation targets a specific citable requirement; route out what does not belong (legal/regulatory obligations escalate to legal — internal waivers cannot authorize breaking the law; policy defects go to policy-review). Return incomplete requests listing the missing items. Check for duplication: the same requirement waived across many assets is one scoped exception and a bigger risk conversation, not twenty small ones.
- **Outputs:** validated request, or return/rejection with reasons.
- **Decision gate:** "inconvenient" is not a justification and "indefinite" is not a duration. No exit plan means it is not temporary — challenge before proceeding.

### 2. Risk scoring and compensating controls — grc-analyst, reviewed by risk-manager

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (analysis step); [exception-management](../skills/exception-management/SKILL.md)
- **Inputs:** validated request; org risk matrix and appetite; existing exceptions on the same asset or requirement.
- **Actions:** write the deviation as an event-based risk statement, score inherent risk (no compensation) and residual risk (compensating controls operating), with written rationale for both. Test compensating controls honestly: do they address the same threat as the waived control, and is there operating evidence? A weaker control on a different threat is not compensation. Assess aggregation — this exception plus existing ones may create a combined exposure larger than any single request looks.
- **Outputs:** scored assessment with recommendation.
- **Decision gate:** residual risk at/above the compensation threshold (default Medium) with no evidenced compensating controls → return the request. Do not route unmitigated Medium+ deviations for approval.

### 3. Risk-proportionate approval — risk-manager routes; approvers per authority matrix

- **Skill:** [exception-management](../skills/exception-management/SKILL.md) (approval routing step)
- **Inputs:** assessment; approval authority matrix.
- **Actions:** route by residual risk: Low → security/GRC manager + business owner; Medium → CISO (or delegate) + BU leader; High → CISO + executive risk owner with risk-committee visibility; Critical/above appetite → executive risk committee, where the default answer is no. Enforce no self-approval: the requester, the risk owner, and anyone in the requesting chain below the required level cannot approve. Escalate one level for regulated data, crown-jewel assets, or certified scope (ISO 27001 / SOC 2 boundaries — flag to the readiness owners; these surface in audits). Record the decision verbatim with names, roles, dates, and conditions.
- **Outputs:** approval, approval-with-conditions, or rejection — all three are valid, recorded outcomes.
- **Decision gate:** rejected requests end here: the team remediates or escalates through management, not through re-submission with softer adjectives.

### 4. Time-bounding and registration — grc-analyst

- **Skill:** [exception-management](../skills/exception-management/SKILL.md) (duration and recording steps)
- **Inputs:** approved exception with conditions.
- **Actions:** set duration to the shortest period consistent with the exit plan — max 12 months, 6 or less for high-risk — and a review date before expiry (typically 30 days prior, 60 for high-risk). Tie expiry to the exit-plan milestone where possible. Enter the exception in the register per the fixed schema with an ID; cross-reference Medium+ residuals into the risk register as accepted risks. Notify control owners and monitoring teams so the deviation stops resurfacing as an unknown finding while staying visible in compliance reporting.
- **Outputs:** register entry with effective/review/expiry dates; risk register cross-reference.

### 5. Monitoring during the term — grc-analyst

- **Skill:** [exception-management](../skills/exception-management/SKILL.md); compensating-control evidence via [control-testing](../skills/control-testing/SKILL.md)
- **Inputs:** active register entries; approval conditions; exit-plan milestones.
- **Actions:** an approved exception is a live risk position, not a filed document. Verify compensating controls keep operating (evidence, not assertion — reuse control testing results); track exit-plan progress and any approval conditions (e.g., monthly vendor-migration status); watch for scope creep — new assets riding an existing exception need re-assessment, not a quiet append. A failed compensating control voids the residual score: re-score and re-route immediately.
- **Outputs:** monitoring evidence attached to the register entry; scope-change or control-failure escalations.

### 6. Expiry handling — risk-manager decides; grc-analyst prepares

- **Skill:** [exception-management](../skills/exception-management/SKILL.md) (re-certification flow)
- **Inputs:** exceptions at review date; monitoring evidence; current threat landscape.
- **Actions:** at each review date, three outcomes only: **renew** — a full re-approval at the level the re-scored risk requires, with fresh justification and evidence, never a rubber stamp; **close** — remediated or decommissioned, with closure evidence recorded; or **lapse to violation** — expired without action is an open policy violation reported as non-compliance, not a grace period. No exit-plan progress on two consecutive reviews → escalate one authority level; the exception is functioning as permanent.
- **Outputs:** renewed, closed, or expired-violation status with evidence.
- **Decision gate:** silent renewal is the failure mode this step exists to prevent. Renewal without the required approver's fresh signature does not happen.

### 7. Portfolio reporting — grc-analyst, presented by compliance-officer

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md)
- **Inputs:** full exception register; risk register cross-references.
- **Actions:** report register health quarterly (monthly for high-risk items): exception load (open count by risk level), count and percentage past review date (target: zero), aging distribution, serial renewals, expired-violation count, and concentration by requirement — many exceptions against one control means fix the control or the policy, and route that to [policy-review](../skills/policy-review/SKILL.md). Feed the exception-load KRI into board reporting.
- **Outputs:** exception portfolio report; policy-defect and escalation actions with owners.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Validated request (or documented return) | 1 | Exception register (requested status) |
| Risk assessment with residual score | 2 | Exception register entry |
| Approval decision with names and conditions | 3 | Exception register (audit evidence) |
| Time-bounded register entry | 4 | Exception register + risk register |
| Monitoring evidence | 5 | Exception register attachments |
| Renewal / closure / violation status | 6 | Exception register + compliance reporting |
| Portfolio report | 7 | Governance pack; board KRIs |

## Failure modes

- **Silent renewal.** Expiry arrives, nobody decides, the exception rolls forward by inertia. Step 6 makes renewal a full re-approval and expiry-without-action a reported violation — there is no fourth outcome.
- **Self-approval by proximity.** The requesting director "approves" their own team's exception because the matrix was never enforced. The requester's chain below the required authority level can never approve.
- **Compensating-control theater.** Controls promised at approval, never implemented, never checked. Step 5 requires operating evidence during the term; a dead compensating control invalidates the approval it enabled.
- **Exception-as-backlog.** Teams use exceptions to defer remediation indefinitely — same justification, third renewal. Two reviews with no exit-plan progress force escalation; serial renewals are a step 7 metric.
- **Register-risk disconnect.** Exceptions live in one list, risks in another, and governance sees neither whole. Medium+ exceptions must cross-reference the risk register or they are hidden risk acceptances.
- **Scope creep on a valid ticket.** An exception approved for two servers quietly covers twenty. Named-asset scope at intake plus scope checks in step 5 keep the approval matched to the exposure.
- **Waiving the law.** Processing an exception against a regulatory obligation as if it were internal policy. Regulators do not accept your waivers — step 1 routes these to legal, full stop.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
