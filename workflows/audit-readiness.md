# Workflow: Audit Readiness

```yaml
name: audit-readiness
description: >-
  Preparation program for an upcoming external audit or assessment (SOC 2, ISO
  27001 surveillance, internal audit, customer audit, regulator exam): confirm
  scope, inventory and map controls, dry-run evidence collection, pre-test weak
  controls, run a remediation sprint, prepare control owners, and support
  fieldwork.
skills_used:
  - audit-preparation
  - control-testing
  - control-mapping
  - policy-review
typical_duration: 8-12 weeks before fieldwork; compressible to 4 with prior audit history
roles:
  - internal-auditor
  - grc-analyst
  - compliance-officer
```

## Trigger

- An external audit is scheduled: SOC 2 examination, ISO 27001 certification/surveillance/recertification, customer right-to-audit exercise, or regulator examination.
- Fieldwork date confirmed at least 4 weeks out (below that, run steps 1, 3, and 6 only and accept the risk on the rest).

## Prerequisites

- Audit engagement details: audit type, criteria/standard, period covered (point-in-time vs period-of-time — a SOC 2 Type II covers a period; see [SOC 2 TSC](../context/frameworks/soc2-tsc.md)), auditor firm, and prior-year report with findings if this is a repeat. The criteria pack for the target sits in [../context/frameworks/](../context/frameworks/) — among them [SOC 1 / ISAE 3402](../context/frameworks/soc1-isae3402-soc-reports.md) where the engagement covers controls relevant to financial reporting rather than security, and the [FFIEC IT Examination Handbook](../context/frameworks/ffiec-it-examination-handbook.md) for a US banking examination; for a regulator exam under a specific regime, the regime's pack in [../context/regulations/](../context/regulations/) supplies the criteria.
- Control inventory or statement of applicability for the audited framework.
- Named control owners for every in-scope control.
- An evidence repository location the whole team will actually use.

## Steps

### 1. Scope confirmation — internal-auditor with compliance-officer

- **Skill:** [audit-preparation](../skills/audit-preparation/SKILL.md)
- **Inputs:** engagement letter, criteria, prior report, system description or SoA.
- **Actions:** confirm in writing with the auditor: systems/entities/locations in scope, audit period, criteria version, sampling expectations, and fieldwork logistics. Reconcile scope against what changed since the last audit (new systems, deprecated controls, org changes) — scope surprises during fieldwork are the most expensive kind.
- **Outputs:** confirmed scope memo; audit calendar working back from fieldwork with owners per milestone.
- **Decision gate:** if scope disputes exist (auditor assumes a system is in scope that the team excluded), resolve them now with the auditor, not in week one of fieldwork.

### 2. Control inventory and mapping — grc-analyst

- **Skill:** [control-mapping](../skills/control-mapping/SKILL.md)
- **Inputs:** control inventory; audit criteria; prior request lists (PBC lists).
- **Actions:** map every criterion/requirement to the specific controls that satisfy it and the owner of each. Identify criteria with no mapped control (design gap — escalate immediately) and controls mapped to nothing (drop from audit scope discussion). Where the organization runs multiple frameworks, reuse the [framework crosswalk](../context/crosswalks/framework-crosswalk.md) rather than remapping from scratch.
- **Outputs:** criterion-to-control-to-owner matrix; design-gap list.

### 3. Evidence dry run — grc-analyst, owners produce

- **Skill:** [audit-preparation](../skills/audit-preparation/SKILL.md) (evidence readiness step)
- **Inputs:** matrix from step 2; prior PBC list or a predicted one.
- **Actions:** issue a mock PBC request to control owners with real deadlines. For each control, collect one sample of the evidence the auditor will request and check it for the classic defects: wrong period, missing timestamps/system identifiers, screenshots without context, exported reports nobody can regenerate, and evidence that reveals the control was not operating for part of the period. Populate the evidence repository with a per-control index.
- **Outputs:** evidence gap list (missing, defective, or unretrievable evidence); populated repository skeleton.
- **Decision gate:** any control whose owner cannot produce evidence within the mock deadline is flagged red and routed to steps 4-5.

### 4. Control pre-testing — internal-auditor

- **Skill:** [control-testing](../skills/control-testing/SKILL.md)
- **Inputs:** red/amber controls from step 3; controls with prior-year findings; controls new this period.
- **Actions:** perform independent test-of-design and test-of-operating-effectiveness on the risk-weighted subset (testing everything is rarely feasible — prioritize prior findings, new controls, and evidence-weak controls). Use the auditor's likely sampling approach. Record results with the same rigor an auditor would: population, sample, attribute tested, result. Where an internal audit function runs the pre-test, it is bound by its own professional standards ([IIA Global Internal Audit Standards](../context/frameworks/iia-global-internal-audit-standards.md)), including on independence from the remediation in step 5.
- **Outputs:** pre-test results with pass/fail per control and root cause for failures.

### 5. Remediation sprint — grc-analyst coordinates; control owners execute

- **Skill:** [audit-preparation](../skills/audit-preparation/SKILL.md); [policy-review](../skills/policy-review/SKILL.md) for documentation defects
- **Inputs:** design gaps (step 2), evidence gaps (step 3), pre-test failures (step 4).
- **Actions:** triage by what can genuinely improve before fieldwork. Operating-effectiveness history cannot be rewritten — for a period-of-time audit, a control that failed for six months will be an exception regardless; focus remediation on (a) fixing the control going forward, (b) documenting the failure and remediation honestly for the auditor, (c) closable items: policy updates via policy-review, missing approvals, access recertifications, evidence packaging. Never fabricate or backdate evidence — an integrity finding ends careers and engagements; a control exception is just a finding.
- **Outputs:** remediation tracker with owner/date/status; management-response drafts for known exceptions.

### 6. Owner preparation — internal-auditor

- **Skill:** [audit-preparation](../skills/audit-preparation/SKILL.md) (interview prep step)
- **Inputs:** matrix, evidence index, known-exception list.
- **Actions:** brief each control owner: what they own, what the auditor will ask, where their evidence lives, and interview discipline (answer what was asked, say "I'll follow up" rather than guessing, never speculate about other teams' controls). Run mock interviews for first-time interviewees and for owners of known-weak controls.
- **Outputs:** briefed owners; interview schedule aligned to auditor plan.

### 7. Fieldwork support — internal-auditor (single point of contact)

- **Skill:** [audit-preparation](../skills/audit-preparation/SKILL.md) (fieldwork step)
- **Inputs:** live auditor requests.
- **Actions:** route every request through one coordinator; log request, owner, due date, and delivery in a request tracker. Review evidence before it goes to the auditor (for responsiveness and accuracy, not sanitization). Hold a short daily stand-up during fieldwork to surface stuck requests and emerging findings early. When the auditor floats a potential finding, get the facts confirmed and the management response drafted while fieldwork is still open — findings are cheapest to contest or contextualize before the draft report.
- **Outputs:** request log; delivered evidence; draft management responses.

## Outputs summary

| Output | Step | Purpose |
|--------|------|---------|
| Scope memo + audit calendar | 1 | Shared plan with auditor |
| Criterion-to-control-owner matrix | 2 | Backbone for evidence and interviews |
| Evidence gap list + repository | 3 | Fieldwork readiness |
| Pre-test results | 4 | Find exceptions before the auditor does |
| Remediation tracker + response drafts | 5 | Reduce and contextualize findings |
| Briefed owners | 6 | Clean interviews |
| Request log | 7 | Controlled, fast fieldwork |

## Failure modes

- **Starting at the PBC list.** Waiting for the auditor's request list to begin preparing means steps 2-5 never happen and fieldwork becomes discovery.
- **Evidence heroics.** One analyst assembling all evidence themselves instead of making owners produce it — the audit passes, the program learns nothing, and next year is identical.
- **Backdating temptation.** Under deadline pressure, someone "recreates" a missing approval. Treat this as a bright line in step 5 and say so out loud to owners.
- **Scope creep in interviews.** Unprepped owners volunteering adjacent systems and problems into scope. Step 6 interview discipline exists for this.
- **Fighting every finding.** Contesting all findings burns auditor goodwill needed for the genuinely wrong ones. Concede the accurate findings with strong management responses; contest the factually wrong ones with evidence.
- **Post-audit amnesia.** Findings remediated to close the report, then the same findings recur next year. Feed results into [control testing](../skills/control-testing/SKILL.md) cadence and the [annual risk assessment](annual-risk-assessment.md) so the fix persists.
