---
name: exception-management
description: >-
  Processes security policy and control exception requests (risk acceptances, waivers,
  deviations): validates the request, assesses residual risk, routes to the correct
  approval authority by risk level, sets expiry and review dates, records the exception,
  and defines re-certification. Use when asked to "request an exception", "accept this
  risk", "waive a control", "extend an exception", or "review the exception register".
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

# Security Exception Management

## Purpose

Turn ad-hoc "we can't comply" situations into governed, time-boxed, risk-assessed exceptions with the right approver on record. A disciplined exception process keeps the policy framework credible: deviations are visible, owned, compensated, and expiring — never silent or permanent. This skill handles the full lifecycle: intake, assessment, approval routing, registration, and re-certification.

## When to use

- A team requests deviation from a security policy, standard, or mandated control ("we need to keep TLS 1.0 for a legacy client", "this server can't run EDR").
- A risk owner wants to formally accept a residual risk that stems from non-compliance with an internal requirement.
- An existing exception approaches expiry and needs re-certification or closure.
- Auditors or leadership request an exception register review (aging, concentration, expired items).

**When NOT to use:**

- The risk does not arise from deviating against a defined policy/control requirement — general risk acceptance belongs in [risk-assessment](../risk-assessment/SKILL.md) treatment step.
- The requirement itself is wrong or obsolete — route to [policy-review](../policy-review/SKILL.md) to fix the policy instead of piling exceptions onto it.
- The deviation is from an external legal/regulatory obligation — regulators do not accept internal waivers; assess exposure via [regulatory-applicability](../regulatory-applicability/SKILL.md) and escalate to legal. An internal exception can never authorize breaking the law.
- A finding remediation needs more time but the control will be met — that is a remediation-plan extension, not an exception, unless the org's process treats overdue findings as exceptions.

## Hard rules (non-negotiable)

1. **No indefinite exceptions.** Every exception has an expiry date. Maximum initial term 12 months; 6 months or less for high-risk. "Permanent" business conditions get re-certified on schedule anyway — conditions change.
2. **No self-approval.** The requester, the exception's risk owner, and anyone in the requesting reporting line below the required authority level cannot approve. The control owner (e.g., CISO org) provides the risk assessment but the business risk owner's chain provides acceptance — one party cannot play both roles.
3. **Compensating controls are mandatory above the defined risk threshold** (default: any residual risk of Medium or higher). An exception without compensating controls at that level is returned, not approved.
4. **No retroactive silence.** If the deviation already exists in production, the exception is logged from discovery date and the period of unmanaged deviation is noted — do not backdate approval.
5. **Expired means non-compliant.** An expired exception is not a grace period; it is an open policy violation and is reported as such until renewed or remediated.

## Inputs to gather

1. **The requirement being deviated from** — exact policy/standard clause or control ID, and the framework mappings behind it (feeds impact on certifications; see [control-mapping](../control-mapping/SKILL.md)).
2. **Scope** — systems, data classifications, user populations, locations affected. Named assets, not "some servers".
3. **Business justification** — why compliance is not feasible now: technical constraint, vendor limitation, cost, timeline. "Inconvenient" is not a justification.
4. **Requested duration and exit plan** — how long, and what will change to end the need (remediation project, decommission date, vendor fix ETA). No exit plan → challenge whether this is really temporary.
5. **Proposed compensating controls** — what reduces the risk in the meantime, with evidence they are (or will be) operating.
6. **Risk context** — organization's risk matrix and appetite thresholds (reuse the scales from [risk-assessment](../risk-assessment/SKILL.md); methodology in [risk scoring](../../context/risk-scoring.md)), plus the org's approval authority matrix if one exists.
7. **Prior history** — previous exceptions for the same requirement or asset (serial renewal is a red flag), related incidents or findings.

Use [templates/exception-request.md](../../templates/exception-request.md) as the intake form.

## Procedure

### 1. Validate the request

1. Confirm the deviation targets a specific, citable requirement. If the requester cannot name the control, identify it for them or reject as unscoped.
2. Check the "When NOT to use" routing: legal/regulatory obligation → escalate, do not process. Policy defect → policy-review. Not actually a deviation → close.
3. Verify completeness against the intake inputs above. Return incomplete requests with the specific missing items — do not assess partial requests.
4. Check for duplication/aggregation: same requirement waived for many assets should be one exception with a defined scope (and a bigger risk conversation), not twenty small ones that individually look harmless.
5. Check whether the governing regime defines its own deviation mechanism — a [NERC CIP](../../context/regulations/nerc-cip.md) Technical Feasibility Exception, a [CMMC](../../context/frameworks/nist-800-171-cmmc.md) plan of action with its closeout clock, a [FedRAMP](../../context/frameworks/fedramp.md) accepted weakness, a compensating control the CISO must approve in writing under [NYDFS Part 500](../../context/regulations/us-nydfs-part-500.md). Where one exists, run it as well as the internal register; the internal record alone does not satisfy the regime.

### 2. Assess residual risk

1. Write the risk created by the deviation as an event-based statement ("Risk that X due to [absent control] resulting in Z") — see [risk statement patterns](../risk-assessment/references/risk-statement-patterns.md).
2. Score inherent risk of the deviation (no compensating controls) on the org's matrix, then residual risk with the proposed compensating controls operating. Record rationale for both.
3. Evaluate compensating controls honestly: do they address the same threat the original control addresses, and is there evidence they operate? A weaker control on a different threat is not compensation. If residual risk ≥ the compensating-control threshold and none are proposed, stop — return the request (hard rule 3).
4. Note aggregation: does this exception combine with existing ones on the same asset or requirement to create a larger combined exposure? Score the marginal risk in that light.

### 3. Determine approval authority

Route by residual risk level using the org's authority matrix; absent one, apply the default matrix in [exception criteria](references/exception-criteria.md):

- **Low** → security/GRC manager + requesting business owner.
- **Medium** → CISO (or delegate) + business unit leader.
- **High** → CISO + executive risk owner (CIO/COO/CFO as applicable); risk committee visibility.
- **Critical / above appetite** → executive risk committee decision; default answer is no — require remediation or avoidance instead.

**Decision points:** verify no approver fails the self-approval rule; escalate one level if the exception touches regulated data, crown-jewel assets, or an externally certified scope (e.g., systems in an ISO 27001 or SOC 2 boundary — flag to [iso27001-readiness](../iso27001-readiness/SKILL.md) / [soc2-readiness](../soc2-readiness/SKILL.md) owners, since exceptions inside certified scope surface in audits; see [audit-preparation](../audit-preparation/SKILL.md)).

### 4. Set duration, expiry, and review

1. Duration = shortest period consistent with the exit plan, capped per hard rule 1 and the risk-based maximums in [exception criteria](references/exception-criteria.md).
2. Set a review date before expiry (typically 30 days prior; 60 for high-risk) to trigger re-certification or closure without a compliance gap.
3. Tie expiry to the exit plan milestone where possible ("expires at legacy client decommission, no later than 2027-01-31").

### 5. Record the decision

1. Present the assessment to the approver(s) with: risk statement, inherent/residual scores, compensating controls, duration, exit plan, and aggregation notes. Record approval, rejection, or approval-with-conditions verbatim, with names, roles, and dates.
2. Enter the exception in the exception register using the schema below. Assign an ID.
3. Link the exception to the risk register: Medium+ residual exceptions appear as accepted risks with the exception ID cross-referenced.
4. Notify control owners and monitoring teams so the deviation is not repeatedly re-flagged as an unknown finding — but keep it visible in compliance reporting as an approved exception.

### 6. Run the re-certification flow

At each review date:

1. Confirm the business justification still holds and the exit plan progressed. No progress on two consecutive reviews → escalate one authority level; the exception is functioning as permanent.
2. Re-verify compensating controls are operating (evidence, not assertion — reuse [control-testing](../control-testing/SKILL.md) results where available).
3. Re-score residual risk against the current threat landscape; a changed score changes the required authority.
4. Outcome: **renew** (new expiry, re-approval at the required level — renewal is a full re-approval, not a rubber stamp), **close** (remediated or decommissioned; record closure evidence), or **lapse to violation** (expired without action → report as non-compliance to the risk committee).
5. Report register health monthly/quarterly via [grc-metrics-reporting](../grc-metrics-reporting/SKILL.md): open count by risk level, aging, expired count, serial renewals, concentration by requirement (many exceptions against one control = fix the control or the policy).

## Output format

Deliverables: (a) completed assessment and recommendation, (b) exception register entry.

**Exception register entry schema (fixed):**

| Field | Content |
|---|---|
| Exception ID | e.g., EXC-2026-031 |
| Requirement deviated from | Policy/standard clause or control ID |
| Scope | Named assets, data classes, populations |
| Requester / date | Name, role, submission date |
| Business justification | 2–4 sentences |
| Risk statement | Event-based |
| Inherent / residual risk | Scores with rationale |
| Compensating controls | Named, with operating evidence status |
| Approval authority & decision | Names, roles, decision, conditions, date |
| Effective / expiry / review dates | All three explicit |
| Exit plan | Actions, owner, milestone |
| Risk register cross-ref | RSK ID if Medium+ |
| Status | Requested / Approved / Rejected / Active / In review / Renewed / Closed / Expired-violation |

**Worked example (abbreviated):**

> **EXC-2026-031** — Deviation from Encryption Standard §4.2 (TLS 1.2+ required) for payment terminal integration with AcquirerLegacy API (2 app servers, cardholder-adjacent zone).
> Justification: acquirer's legacy endpoint supports TLS 1.0 only; vendor migration ETA 2026-Q4.
> Risk: Risk that payment-adjacent traffic is intercepted or downgraded due to permitted TLS 1.0 on the acquirer link, resulting in cardholder data exposure and PCI DSS compliance impact. Inherent: L3 x I4 = 12 (High band). Residual with compensating controls: L2 x I4 = 8 (Medium).
> Compensating controls: dedicated egress-restricted VLAN for the two servers; IDS signature alerting on downgrade attempts; weekly config attestation. Evidence: firewall ruleset review 2026-07-02.
> Approval: CISO (J. Ortiz) + BU Director Payments (M. Chen), approved with condition of monthly vendor-migration status report, 2026-07-10. Effective 2026-07-10; review 2026-11-30; expires at acquirer migration, no later than 2026-12-31. Cross-ref: RSK-2026-022. Status: Active.

## Quality checklist

- [ ] Deviation cites a specific requirement; regulatory-obligation deviations rejected/escalated, not processed.
- [ ] Every exception has an expiry date within the risk-based maximum; zero indefinite exceptions.
- [ ] Approver meets the authority matrix for the residual risk level; no self-approval anywhere in the chain.
- [ ] Compensating controls present and evidenced for all exceptions at/above the threshold; each addresses the same threat as the waived control.
- [ ] Residual risk scored on the org's matrix with written rationale; aggregation with existing exceptions considered.
- [ ] Exit plan with owner and milestone recorded; duration tied to it.
- [ ] Review date set before expiry; re-certification defined as full re-approval.
- [ ] Register entry complete per schema; Medium+ exceptions cross-referenced in the risk register.
- [ ] Pre-existing (already-live) deviations logged from discovery date, not backdated.
- [ ] Exceptions in certified/audited scope flagged to the relevant readiness/audit owners.

## References

- [references/exception-criteria.md](references/exception-criteria.md) — default approval matrix, duration caps, required evidence, escalation paths, example completed record
- [../../templates/exception-request.md](../../templates/exception-request.md) — intake form template
- [../../context/risk-scoring.md](../../context/risk-scoring.md) — scoring methodology for residual risk
- [../../context/glossary.md](../../context/glossary.md) — exception, waiver, risk acceptance, compensating control definitions
- Regime-defined deviation mechanisms: [../../context/regulations/nerc-cip.md](../../context/regulations/nerc-cip.md) — the Technical Feasibility Exception process and its "per system capability" successor; [../../context/frameworks/nist-800-171-cmmc.md](../../context/frameworks/nist-800-171-cmmc.md) — which requirements may never sit on a plan of action, and the closeout clock that ends a conditional status; [../../context/regulations/us-fisma-federal-cyber.md](../../context/regulations/us-fisma-federal-cyber.md) and [../../context/frameworks/nist-rmf-800-37-800-30.md](../../context/frameworks/nist-rmf-800-37-800-30.md) — the remedial-action process and the authorizing official who accepts residual risk by name; [../../context/frameworks/fedramp.md](../../context/frameworks/fedramp.md) — plans of action replaced by an accepted-weaknesses list under the 2026 consolidated rules
- Compensating-control regimes: [../../context/frameworks/pci-dss-4.md](../../context/frameworks/pci-dss-4.md) — compensating controls need a documented business or technical constraint and are not the same thing as the customized approach; [../../context/regulations/us-nydfs-part-500.md](../../context/regulations/us-nydfs-part-500.md) — where the CISO may approve reasonably equivalent or more secure compensating controls in writing, reviewed at least annually; [../../context/frameworks/swift-customer-security-programme.md](../../context/frameworks/swift-customer-security-programme.md) — non-compliance surfaces in an annual attestation counterparties can read
- Escalation and reporting duties an exception can trigger: [../../context/regulations/australia-apra-cps-234-230.md](../../context/regulations/australia-apra-cps-234-230.md) — notification of a material control weakness that cannot be remediated in a timely manner; [../../context/frameworks/hitrust-csf.md](../../context/frameworks/hitrust-csf.md) — corrective action plans tracked inside the assessment platform; [../../context/frameworks/iso-31000-27005-risk-management.md](../../context/frameworks/iso-31000-27005-risk-management.md) — risk acceptance as a treatment option inside a documented risk process
- Related skills: [risk-assessment](../risk-assessment/SKILL.md), [policy-review](../policy-review/SKILL.md), [control-testing](../control-testing/SKILL.md), [control-mapping](../control-mapping/SKILL.md), [audit-preparation](../audit-preparation/SKILL.md), [grc-metrics-reporting](../grc-metrics-reporting/SKILL.md), [regulatory-applicability](../regulatory-applicability/SKILL.md)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
