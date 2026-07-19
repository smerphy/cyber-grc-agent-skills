# Workflow: New Regulation Impact Assessment

```yaml
name: new-regulation-impact-assessment
description: >-
  End-to-end response when horizon scanning flags a new or amended regulation:
  determine applicability, extract obligations, assess gaps against current
  controls, plan remediation, update policies, and brief leadership.
skills_used:
  - regulatory-horizon-scanning
  - regulatory-applicability
  - control-mapping
  - framework-gap-assessment
  - policy-authoring
  - grc-metrics-reporting
typical_duration: 4-8 weeks elapsed; 5-15 working days of effort depending on regulation breadth
roles:
  - compliance-officer
  - grc-analyst
  - risk-manager
```

## Trigger

- A [regulatory horizon scan](../skills/regulatory-horizon-scanning/SKILL.md) flags a new regulation, amendment, or enforcement-priority shift rated medium impact or higher.
- Legal counsel, a regulator, a customer contract, or an industry body notifies the organization of a new obligation.
- Business expansion (new market, new product line, new data category) brings a known regulation into scope for the first time.

## Prerequisites

- Current control inventory or statement of applicability (any format; a spreadsheet is fine).
- Entity facts: legal entities, jurisdictions of establishment and operation, sector classifications, headcount/revenue, data categories processed, customer base geography.
- A named accountable owner (typically the compliance officer) and a decision forum that can accept residual risk or fund remediation.

## Steps

### 1. Confirm the signal — compliance-officer

- **Skill:** [regulatory-horizon-scanning](../skills/regulatory-horizon-scanning/SKILL.md)
- **Inputs:** the scan alert; official source text (act, directive, final rule, guidance).
- **Actions:** verify against the official publication, not secondary commentary. Record: instrument name, issuing authority, publication date, entry-into-force date, and any phased application dates. Classify as new obligation / amendment / guidance / enforcement signal.
- **Outputs:** confirmed regulation record with dates and source citation.
- **Decision gate:** if the instrument is draft-stage with no fixed dates, park it on the horizon watchlist with a re-review date and stop here. Proceed only for adopted text or drafts with high adoption probability and near-term dates.

### 2. Applicability determination — compliance-officer, supported by grc-analyst

- **Skill:** [regulatory-applicability](../skills/regulatory-applicability/SKILL.md)
- **Inputs:** confirmed regulation record; entity facts from prerequisites.
- **Actions:** walk the regulation's scope tests (entity type, sector, thresholds, territorial scope, data or activity triggers) per legal entity. Where scope is genuinely ambiguous, document the ambiguity and escalate to legal counsel rather than guessing.
- **Outputs:** applicability memo per entity: in scope / out of scope / ambiguous-pending-counsel, with the specific scope provision cited for each conclusion.
- **Decision gate:** if all entities are out of scope, record the memo (it is audit evidence of diligence), set a re-check trigger for business changes, and close the workflow.

### 3. Obligations extraction — grc-analyst

- **Skill:** [regulatory-applicability](../skills/regulatory-applicability/SKILL.md) (obligation decomposition step)
- **Inputs:** applicability memo; official regulation text.
- **Actions:** decompose the regulation into discrete, testable obligations — one row per requirement, with citation, obliged entity, deadline, and required evidence. Separate one-time obligations (registration, notification of a representative) from continuous ones (security measures, reporting, record-keeping).
- **Outputs:** obligations register (typically 15-80 rows for a substantial regulation).

### 4. Map obligations to existing controls — grc-analyst

- **Skill:** [control-mapping](../skills/control-mapping/SKILL.md)
- **Inputs:** obligations register; current control inventory; existing framework mappings (see [framework crosswalk](../context/crosswalks/framework-crosswalk.md)).
- **Actions:** for each obligation, identify existing controls that fully, partially, or nowhere satisfy it. Reuse existing mappings — a mature ISO 27001 or NIST CSF 2.0 program will already cover much of any security-flavored regulation; the delta is usually in reporting, governance, and documentation obligations.
- **Outputs:** obligation-to-control map with coverage rating (full / partial / none) per obligation.

### 5. Gap assessment — grc-analyst, reviewed by compliance-officer

- **Skill:** [framework-gap-assessment](../skills/framework-gap-assessment/SKILL.md)
- **Inputs:** obligation-to-control map; interviews with control owners for anything rated partial.
- **Actions:** validate coverage claims with evidence, not owner assertion. Rate each gap by remediation effort and by exposure (enforcement likelihood, penalty ceiling, contractual consequence). Distinguish design gaps (control missing) from operating gaps (control exists but not performed or not evidenced).
- **Outputs:** gap report with prioritized gap list and compliance-by-deadline view (which gaps must close before which application date).

### 6. Remediation plan — risk-manager and compliance-officer

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) framing via [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md) for tracking
- **Inputs:** prioritized gap list; regulatory deadlines; budget and resourcing constraints.
- **Actions:** sequence remediation backward from application dates. Assign each gap an owner, target date, and acceptance criterion. Where a gap cannot close before the deadline, route it through [exception management](../skills/exception-management/SKILL.md) as an explicit, time-bound risk acceptance with a named approver.
- **Outputs:** remediation plan; exception records for accepted timing gaps.
- **Decision gate:** plan is not approved until every deadline-critical gap has either a funded remediation task or a signed exception. No silent gaps.

### 7. Policy and procedure updates — grc-analyst

- **Skill:** [policy-authoring](../skills/policy-authoring/SKILL.md)
- **Inputs:** obligations register rows tagged "requires documented policy/procedure"; existing policy set.
- **Actions:** prefer amending existing policies over creating new ones — one obligation rarely deserves a standalone policy. Route amendments through the standard [policy lifecycle](policy-lifecycle.md) approval chain, expedited if a deadline forces it.
- **Outputs:** amended or new policy drafts in approval workflow.

### 8. Leadership brief — compliance-officer

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md)
- **Inputs:** applicability memo, gap report, remediation plan, exception records.
- **Actions:** produce a one-to-two-page board or executive brief: what the regulation is, why we are in scope, key deadlines, top gaps, cost and timeline to comply, residual risk being accepted, and any personal-liability provisions for management (several regimes, including NIS2, attach responsibility to management bodies — flag these explicitly).
- **Outputs:** board brief; recurring status line added to the compliance dashboard until remediation closes.

## Outputs summary

| # | Output | Owner | Feeds into |
|---|--------|-------|------------|
| 1 | Confirmed regulation record | compliance-officer | Horizon watchlist |
| 2 | Applicability memo | compliance-officer | Audit evidence; step 3 |
| 3 | Obligations register | grc-analyst | Steps 4-5; future audits |
| 4 | Obligation-to-control map | grc-analyst | Gap assessment; control inventory |
| 5 | Gap report | grc-analyst | Remediation plan |
| 6 | Remediation plan + exceptions | risk-manager | Program tracking |
| 7 | Policy updates | grc-analyst | Policy lifecycle workflow |
| 8 | Board brief | compliance-officer | Governance record |

## Failure modes

- **Commentary substitution.** Teams assess against a law-firm summary instead of the official text and miss obligations the summary omitted. Always extract from the primary source.
- **Applicability by vibes.** "This is an EU thing, we're US-based, skip it" — extraterritorial scope provisions (GDPR, EU AI Act, NIS2 for suppliers) routinely catch non-EU entities. Run the scope tests formally.
- **Security tunnel vision.** Mapping only the technical-measures articles and ignoring governance, registration, reporting, and record-keeping obligations, which are where most enforcement actually lands.
- **Deadline compression.** Starting the workflow when the application date is announced but deferring work until it is imminent. Sequence backward from the deadline at step 6, not at step 6 minus three months.
- **Orphaned gaps.** Gaps that are neither remediated nor formally accepted. The step 6 decision gate exists precisely to prevent this; enforce it.
- **One-and-done.** Treating the assessment as complete forever. Amendments, delegated acts, and regulator guidance keep arriving — feed the regulation back into the horizon-scanning watchlist with a review cadence.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
