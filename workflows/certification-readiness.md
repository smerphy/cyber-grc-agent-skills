# Workflow: Certification Readiness (SOC 2 / ISO 27001 from Zero)

```yaml
name: certification-readiness
description: >-
  Taking an organization from no formal certification to a SOC 2 report or ISO
  27001 certificate: choose the right target, fix scope, run a gap assessment,
  execute the remediation program, operate controls through the evidence
  period, run an internal audit or dry run, and support the external audit.
skills_used:
  - soc2-readiness
  - iso27001-readiness
  - framework-gap-assessment
  - audit-preparation
  - control-testing
typical_duration: 9-18 months from decision to report/certificate (SOC 2 Type I achievable faster; Type II and ISO require months of operating history)
roles:
  - compliance-officer
  - grc-analyst
  - internal-auditor
  - risk-manager
```

## Trigger

- Customer contracts or sales pipeline demand third-party assurance ("do you have SOC 2 / ISO 27001?").
- Market entry, investor diligence, or regulatory positioning requires demonstrable security certification.

## Prerequisites

- Executive sponsor with budget authority — certification is a program, not a project, and it changes how teams work.
- A realistic deadline driver (which deal, which renewal, by when) — it decides Type I vs Type II sequencing and how hard scope gets cut.
- Someone accountable for the program day-to-day (compliance-officer or a dedicated lead).

## Steps

### 1. Choose the certification — compliance-officer with sales/leadership

- **Skills:** [soc2-readiness](../skills/soc2-readiness/SKILL.md) and [iso27001-readiness](../skills/iso27001-readiness/SKILL.md) (positioning sections)
- **Inputs:** who is asking (US enterprise buyers → usually SOC 2; EU/international buyers, regulators, tenders → usually ISO 27001; many orgs eventually need both), deadline, budget.
- **Actions:** decide the target and sequencing. SOC 2: choose Trust Services Criteria in scope (Security is mandatory baseline; add Availability/Confidentiality/Processing Integrity/Privacy only if customers demand — each adds cost; see [SOC 2 TSC](../context/frameworks/soc2-tsc.md)) and Type I vs Type II strategy (Type I is point-in-time design assurance; Type II covers operating effectiveness over a period, commonly 3-12 months — many orgs do Type I first, then a Type II). ISO 27001: certification audit is stage 1 + stage 2, then annual surveillance and recertification every three years; the ISMS clauses (4-10) are mandatory regardless of which [Annex A controls](../context/frameworks/iso-27001-2022.md) apply. If both are eventually needed, design controls once against a common set (see [framework crosswalk](../context/crosswalks/framework-crosswalk.md)).
- **Outputs:** decision memo: target, TSC/standard scope, Type I/II or stage plan, target dates.
- **Decision gate:** leadership signs the memo including the resourcing implication. No signature, no program.

### 2. Scope definition — compliance-officer with grc-analyst

- **Skills:** [soc2-readiness](../skills/soc2-readiness/SKILL.md) / [iso27001-readiness](../skills/iso27001-readiness/SKILL.md) (scoping)
- **Inputs:** decision memo; system architecture; org chart; customer expectations of what "covered" means.
- **Actions:** define the audit boundary: for SOC 2, the system description (services, infrastructure, software, people, data); for ISO 27001, the ISMS scope statement (locations, org units, services, interfaces and dependencies). Cut scope to what customers actually buy — but not so narrow the report is useless to them; a scope excluding the production platform convinces no one. Identify subservice organizations/outsourced dependencies and whether they are carved out or included.
- **Outputs:** written scope/system description v1; in-scope asset and team list.

### 3. Gap assessment — grc-analyst, reviewed by internal-auditor

- **Skill:** [framework-gap-assessment](../skills/framework-gap-assessment/SKILL.md)
- **Inputs:** scope; target criteria (TSC CC-series or ISO 27001 clauses 4-10 plus Annex A per [ISO 27002:2022's 93 controls in 4 themes](../context/frameworks/iso-27001-2022.md)); current practices and documents.
- **Actions:** assess current state against every requirement: exists-and-evidenced / exists-unevidenced / partial / absent. For ISO, cover the management-system clauses (context, leadership, risk assessment/treatment, objectives, competence, internal audit, management review) — first-timers systematically underestimate these relative to technical controls. Estimate remediation effort per gap.
- **Outputs:** gap report with effort ratings; draft Statement of Applicability (ISO) or control list mapped to TSC (SOC 2).

### 4. Remediation program — grc-analyst coordinates; control owners execute; risk-manager on risk-driven design

- **Skills:** [soc2-readiness](../skills/soc2-readiness/SKILL.md) / [iso27001-readiness](../skills/iso27001-readiness/SKILL.md); [policy-authoring](../skills/policy-authoring/SKILL.md) for the document set; [risk-assessment](../skills/risk-assessment/SKILL.md) for ISO's mandatory risk assessment
- **Inputs:** gap report; target audit date worked backward: the evidence period must start after remediation completes.
- **Actions:** run gaps as a tracked program with owners and dates. Typical workstreams: governance documents (policies, risk methodology, SoA), access management, change management, vendor management, logging/monitoring, incident response, HR security (onboarding/offboarding, training), business continuity. Design every control with its evidence in mind — a control that generates no artifact will fail the audit no matter how well it operates. For ISO, complete the risk assessment and risk treatment plan; they drive the SoA and are themselves audited.
- **Outputs:** implemented controls; approved document set; final SoA/system description.
- **Decision gate:** declare "controls operational" only when each control has run once with evidence captured. This date starts the Type II evidence period / ISO operating history — declaring it prematurely poisons the whole period.

### 5. Evidence period operation — control owners; grc-analyst monitors

- **Skills:** [soc2-readiness](../skills/soc2-readiness/SKILL.md) / [iso27001-readiness](../skills/iso27001-readiness/SKILL.md) (operate phase)
- **Inputs:** operational control set; evidence calendar (which control produces what artifact at what cadence).
- **Actions:** operate everything for the chosen period. The grc-analyst runs a monthly evidence health check: sample each recurring control's artifacts, catch missed executions within the month (a quarterly access review skipped in month two is recoverable in month three; discovered at audit it is an exception). Log control changes and incidents during the period — auditors ask.
- **Outputs:** populated evidence repository; monthly health-check log.

### 6. Internal audit / dry run — internal-auditor (must be independent of control operation)

- **Skills:** [control-testing](../skills/control-testing/SKILL.md); [audit-preparation](../skills/audit-preparation/SKILL.md)
- **Inputs:** evidence repository; criteria; scope.
- **Actions:** for ISO 27001 this is the mandatory internal audit plus management review — schedule both before stage 1 and record them properly (they are among the most-cited nonconformities for first-timers). For SOC 2 it is a dry run: test controls the way the auditor will, sample real periods, write up exceptions. Remediate what is fixable; for what is not fixable in time, prepare honest management responses.
- **Outputs:** internal audit report / dry-run results; corrective actions; management review minutes (ISO).
- **Decision gate:** go/no-go on the external audit date. Postponing beats paying for a failed stage 2 or a report full of exceptions — but distinguish "material design failures" (postpone) from "a handful of operating exceptions" (proceed; clean reports are rare and buyers tolerate well-managed exceptions).

### 7. External audit support — internal-auditor coordinates; run as [audit-readiness](audit-readiness.md)

- **Skill:** [audit-preparation](../skills/audit-preparation/SKILL.md)
- **Inputs:** auditor selection (accredited certification body for ISO; licensed CPA firm for SOC 2); PBC lists; interview schedule.
- **Actions:** execute the fieldwork-support pattern from the [audit-readiness workflow](audit-readiness.md): single point of contact, request log, evidence review before delivery, daily stand-ups, early management responses. For ISO, expect stage 1 (documentation/readiness) findings to be fixed before stage 2. After the report/certificate: plan the ongoing cycle — SOC 2 reports are annual; ISO surveillance is annual with recertification in year three. Certification is a subscription, not a trophy.
- **Outputs:** SOC 2 report or ISO 27001 certificate; findings log; next-cycle calendar.

## Outputs summary

| Output | Step |
|--------|------|
| Certification decision memo | 1 |
| Scope statement / system description | 2 |
| Gap report + draft SoA/control map | 3 |
| Implemented controls + document set | 4 |
| Evidence repository + health-check log | 5 |
| Internal audit / dry-run report | 6 |
| Report or certificate + next-cycle plan | 7 |

## Failure modes

- **Buying a policy pack.** Purchasing templates, renaming them, and calling step 4 done. Auditors interview owners; controls that exist only on paper collapse in the first conversation.
- **Evidence-period false start.** Starting the Type II window before controls actually operate, guaranteeing period-opening exceptions. Enforce the step 4 gate.
- **Scope gerrymandering.** A scope so narrow the report excludes what customers buy — the deal-blocking questions return anyway, now with a credibility cost.
- **ISO as a controls checklist.** Implementing Annex A controls while neglecting clauses 4-10; stage 1 fails on missing internal audit, management review, or risk treatment linkage.
- **Tool-will-save-us.** Compliance automation platforms help collect evidence; they do not design controls, own risk, or answer auditor interviews. Budget for humans.
- **Post-certificate collapse.** Everyone exhales after the report; controls stop; year-two surveillance or the next Type II period becomes a crisis. Step 7's next-cycle calendar and the [policy lifecycle](policy-lifecycle.md) and [annual risk assessment](annual-risk-assessment.md) workflows are the sustain mechanism.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
