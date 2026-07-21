# Workflow: Continuous Control Assurance Cycle

```yaml
name: control-assurance-cycle
description: >-
  The standing cycle that keeps control assurance current: a risk-based annual
  test plan executed in quarterly waves, a refreshed control inventory and
  framework mappings so one test attests many, failures routed to remediation
  or governed exception, retesting, and pass-rate and aging metrics feeding
  the reporting program.
skills_used:
  - control-mapping
  - control-testing
  - exception-management
  - grc-metrics-reporting
typical_duration: annual cycle in quarterly waves; plan build 2-3 weeks, each wave 4-6 weeks
roles:
  - grc-analyst
  - risk-manager
  - compliance-officer
```

## Trigger

- Annually: build next year's test plan before the current cycle's final wave closes.
- Quarterly: each wave starts on the calendar, not on demand.
- Off-cycle: a material control change, incident, or new certification scope inserts controls into the next wave.

This is a standing management-assurance program, not an audit. An [internal audit engagement](internal-audit-engagement.md) is a one-off, independent examination that concludes and reports; this cycle is continuous, run by the second line, and exists so that audits and certifications find a tested estate rather than a surprise. It does not replace internal audit's independent opinion — and internal audit may rely on it only after evaluating it.

## Prerequisites

- A control inventory with owners, frequency, automation class, and criticality rating per control. No inventory means the first wave is building one.
- The organization's risk matrix and criticality definitions (see [risk-scoring](../context/risk-scoring.md)).
- Frameworks in scope declared (certification scopes, regulatory baselines, contractual commitments).
- A results repository that survives staff turnover: workpapers, plan, and metrics in one place.

## Steps

### 1. Build the risk-based test plan — grc-analyst drafts; risk-manager approves

- **Skill:** [control-testing](../skills/control-testing/SKILL.md) (frequency baselines and method selection)
- **Inputs:** control inventory, prior-cycle results, risk register, audit and certification calendar.
- **Actions:** set test frequency by criticality, not uniformly: key controls (mitigating high risks, in certified scope, or SOX-relevant) tested every cycle; medium criticality on a 2-year rotation; low criticality on a 3-year rotation or design-review only. Prior failures and recently remediated controls jump to the next wave regardless of rotation. Sequence waves so controls feeding an external audit are tested before its fieldwork, and spread owner workload — one team should not carry an entire wave. Record method and planned sample size per control up front.
- **Outputs:** approved annual plan: control, wave, method, sample, tester.
- **Decision gate:** risk-manager signs off that coverage matches the risk profile — every high-criticality control has a slot this cycle, and untested-for-2+-years controls are visible as a listed residual risk, not an accident.

### 2. Refresh inventory and mappings — grc-analyst

- **Skill:** [control-mapping](../skills/control-mapping/SKILL.md)
- **Inputs:** control inventory, framework mappings, change records since last refresh (new systems, reorgs, decommissions).
- **Actions:** reconcile the inventory against reality before testing it: retire controls whose systems are gone, add controls for new systems, reconfirm owners after reorgs. Refresh control-to-framework mappings — element-level, partial-coverage aware — so each test result rolls up to every framework the control serves ("test once, attest many"). Flag mappings invalidated by framework version changes; the [framework crosswalk](../context/crosswalks/framework-crosswalk.md) narrows the field but does not replace control-level mapping.
- **Outputs:** current inventory; refreshed mapping table with residue lists.
- **Decision gate:** framework requirements with no mapped control are design gaps — route to remediation planning immediately; do not wait for a wave to "test" a control that does not exist.

### 3. Execute the wave — grc-analyst tests; owners provide populations

- **Skill:** [control-testing](../skills/control-testing/SKILL.md)
- **Inputs:** wave slice of the plan; population sources.
- **Actions:** for each control: confirm design still holds (a one-instance walkthrough — designs drift between cycles), then test operating effectiveness: system-generated population with completeness check, samples at the frequency baseline spread across the period, owner never selecting items. Document in workpapers per [control-test-workpaper](../templates/control-test-workpaper.md) to the re-performance standard — external auditors who may rely on this work will hold it to theirs. Conclude per control: effective / operating ineffectively / design deficiency.
- **Outputs:** workpapers and conclusions for every wave control; exception list.

### 4. Disposition failures — grc-analyst routes; risk-manager decides contested calls

- **Skill:** [exception-management](../skills/exception-management/SKILL.md)
- **Inputs:** deficiencies from step 3.
- **Actions:** route each deficiency down one of two paths within 10 business days — undispositioned failures are the cycle's silent killer. (a) Remediation: owner, plan, date proportionate to criticality, tracked in the findings register (see [finding-remediation](finding-remediation.md)). (b) Exception: where the control cannot be met, a formal time-bound exception with compensating controls and the approval authority the residual risk requires — never a shrug. Check mappings from step 2 for blast radius: a failed control that serves three frameworks is three exposures, and failures inside certified scope get flagged to the certification owner for pre-disclosure planning.
- **Outputs:** remediation entries or approved exceptions for every failure; zero unrouted deficiencies.
- **Decision gate:** a deficiency that is neither remediable nor acceptable within appetite escalates to the risk committee — the cycle surfaces the decision, it does not bury it.

### 5. Retest remediated controls — grc-analyst

- **Skill:** [control-testing](../skills/control-testing/SKILL.md) (remediation validation)
- **Inputs:** remediation entries reported complete; exception register review dates.
- **Actions:** retest with samples drawn only from the post-remediation period; passing on pre-fix samples proves nothing. A retest failure reopens the finding at escalated visibility — repeat failure is a different conversation than first failure. At exception review dates, re-verify compensating controls with evidence, not assertion.
- **Outputs:** closure verifications; reopened findings where retests failed.

### 6. Report cycle metrics — grc-analyst produces; compliance-officer presents

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md)
- **Inputs:** wave results, findings register, exception register.
- **Actions:** publish per wave: control test pass rate by domain (with n — a 50% rate off two tests is noise), repeat-failure count, plan attainment (tested vs planned), deficiency aging, and exception load past review date. Each metric carries its threshold and defined response, not a bare number. Feed results to the risk register (residual scores citing observed, not assumed, effectiveness), to [audit-readiness](audit-readiness.md) as pre-tested evidence, and into next year's step-1 plan.
- **Outputs:** wave metrics pack; cycle-end annual summary.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Annual test plan | 1 | Assurance repository |
| Refreshed inventory + mappings | 2 | Control inventory / GRC tool |
| Workpapers + conclusions | 3 | Assurance repository |
| Remediation entries / exceptions | 4 | Findings register / exception register |
| Retest verifications | 5 | Assurance repository |
| Metrics pack | 6 | Metrics program |

## Failure modes

- **Flat-rotation testing.** Every control tested with equal rigor on the same cadence, exhausting the team on low-risk controls while key controls get the same shallow pass. Criticality drives frequency and depth; that is the whole point of step 1.
- **Inventory drift.** Testing last year's inventory against this year's estate — retired controls pass trivially, new systems go untested. Step 2 runs every cycle, not every recertification.
- **The unrouted failure.** A control fails, everyone agrees it is bad, nothing enters remediation or exception, and next wave it fails again as a "new" issue. Step 4's 10-day disposition rule exists for this.
- **Exception as remediation graveyard.** Failures that are really unfunded fixes get parked as serially renewed exceptions. Serial renewal without exit-plan progress escalates by rule, not by mood.
- **Retest theater.** Remediation "verified" by re-inspecting the same pre-fix evidence, or by the owner's screenshot. Post-remediation samples only, pulled by the tester.
- **Cycle-audit confusion.** Presenting this management self-assurance as an independent audit opinion — or letting internal audit reflexively rely on it unevaluated. Keep the roles distinct in reporting; both lose credibility when blurred.
- **Metrics without thresholds.** Pass rates reported as wallpaper with no defined response when they drop. A metric nobody acts on is a vanity count.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
