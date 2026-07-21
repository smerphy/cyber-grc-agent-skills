# Workflow: Cloud Migration Security Review

```yaml
name: cloud-migration-review
description: >-
  Security review of a workload or estate move to cloud: scoping and data
  classification, regulatory constraints (residency, sector rules, transfers),
  provider assurance review treating the CSP as a Tier 1 vendor, shared-
  responsibility control mapping to find which controls transfer, which become
  the provider's, and which die, risk acceptance for residual gaps, and a
  cutover go/no-go.
skills_used:
  - regulatory-applicability
  - control-mapping
  - third-party-risk-assessment
  - risk-assessment
  - exception-management
typical_duration: 4-10 weeks depending on estate size; single-workload moves in 2-3 weeks
roles:
  - grc-analyst
  - risk-manager
  - compliance-officer
  - greybeard
```

## Trigger

- A migration program, workload move, or data-center exit to a cloud provider is approved or seriously planned — trigger **before the provider contract is signed**, while assurance findings can still shape terms.
- An existing cloud footprint materially expands (new regulated data categories, new regions, move from IaaS to provider-managed services) — re-run from step 2 for the delta.
- Discovery that a workload already moved without review — run retroactively; the unreviewed period is a finding.

## Prerequisites

- An inventory of the workloads in scope with their data classifications, or the commitment to build one in step 1 — an unclassified estate cannot be migration-reviewed.
- The organization's current control library or adopted framework baseline, with its framework mappings.
- The organization's applicability register (from [regulatory-applicability](../skills/regulatory-applicability/SKILL.md)); build one first if absent.
- A named migration owner and a target architecture description (landing zone, identity model, network design) at least in draft.

## Steps

### 1. Scoping and data classification — grc-analyst, with the migration owner

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (context and asset criticality)
- **Inputs:** migration plan; asset and data inventories.
- **Actions:** fix the boundary in writing: which workloads, data stores, and integrations move, in what waves, to which provider services and regions. Classify the data actually in each workload — inspect, do not trust the label the application had in 2019. Record criticality, recovery expectations, and dependencies that stay on-premises; the hybrid seams are where migrations break.
- **Outputs:** scoped, classified migration inventory with wave assignments.

### 2. Regulatory constraints — compliance-officer, with grc-analyst

- **Skill:** [regulatory-applicability](../skills/regulatory-applicability/SKILL.md) (migration-scoped pass)
- **Inputs:** applicability register; classified inventory; target regions and provider services.
- **Actions:** derive the constraints the target architecture must satisfy per regime: data residency and localization limits, cross-border transfer mechanisms for personal data (see [GDPR](../context/regulations/gdpr.md) Chapter V requirements — verify current transfer-mechanism validity against official guidance), sector rules such as [DORA](../context/regulations/dora.md) ICT third-party and outsourcing expectations for financial entities, and any regulator notification or approval duties for material outsourcing — several sectors have them; verify against the applicable rulebook before scheduling cutover. Express each constraint as a testable architecture requirement (region pinning, key custody, exit plan), not a legal citation.
- **Outputs:** regulatory constraints list bound to workloads and regions.
- **Decision gate:** any workload whose constraints the target provider/region cannot satisfy is removed from scope or re-planned now — not discovered at cutover.

### 3. Provider assurance review — grc-analyst; greybeard reviews architecture claims

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md)
- **Inputs:** provider audit reports and certifications, contract and DPA drafts, service documentation.
- **Actions:** the CSP is a Tier 1 (critical) vendor — assess it like one. Review the SOC 2 / ISO 27001 evidence for the *specific services and regions* being consumed, not the provider's brand: check scope, period, exceptions, and subservice carve-outs, and extract the complementary user entity controls — on a cloud platform, the CUEC list is effectively your side of the shared-responsibility model in audit language. Confirm contract terms: breach notification SLA compatible with your regulatory clocks, audit/assurance rights, subprocessor notification, data return and deletion, exit assistance. Concentration risk (one provider under everything) goes to the risk register, not a footnote.
- **Outputs:** provider assessment report; contract requirements list; CUEC extract.

### 4. Shared-responsibility control mapping — grc-analyst; greybeard validates the deltas

- **Skill:** [control-mapping](../skills/control-mapping/SKILL.md)
- **Inputs:** current control library; provider responsibility documentation per service; CUEC extract.
- **Actions:** map every in-scope control to its target-state disposition: **transfers** (still ours, re-implemented on cloud primitives), **inherited** (becomes the provider's — evidenced only via their assurance reports), **dies** (no longer meaningful — e.g., physical controls for exited data centers), or **new** (cloud-native obligations with no on-prem ancestor: tenant configuration baselines, identity federation, key management custody, egress controls). Responsibility shifts per service model — the same control can be inherited on a managed service and yours on IaaS, so map per service, not per provider. Sweep both directions for residue: target obligations nothing covers, and legacy controls about to be decommissioned while still needed by unmigrated waves.
- **Outputs:** disposition-tagged control map; uncovered-obligation list.

### 5. Target-state gap and risk assessment — grc-analyst scores; risk-manager reviews

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md)
- **Inputs:** uncovered-obligation list; regulatory constraints; provider assessment findings.
- **Actions:** convert material gaps into event-based risk statements and score them on the org matrix ([risk scoring](../context/risk-scoring.md)) — inherent, then residual with the compensating measures actually planned for cutover, not the ones on the roadmap. Pay specific attention to the dual-running window: legacy controls decommissioned before cloud controls demonstrably operate is the classic migration exposure. Assign remediation owners and dates for everything above appetite; entries land in the [risk register](../templates/risk-register.csv).
- **Outputs:** scored gap-risk register with treatment plan per wave.

### 6. Risk acceptance for residual gaps — risk-manager approves; migration owner sponsors

- **Skill:** [exception-management](../skills/exception-management/SKILL.md)
- **Inputs:** above-appetite residuals that will not be closed before cutover.
- **Actions:** each surviving gap gets a formal, time-bound exception using the [exception request](../templates/exception-request.md): named requirement deviated from, compensating controls with evidence they operate, expiry tied to the remediation date, approval authority by risk level — never the migration team approving its own schedule pressure. Gaps against external legal obligations cannot be internally waived; those go back to step 2 for re-planning or to counsel.
- **Outputs:** signed exceptions in the register; rejected acceptances returned as blockers.

### 7. Cutover go/no-go — risk-manager chairs; compliance-officer and greybeard advise

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (appetite comparison at the gate)
- **Inputs:** all prior outputs; wave readiness evidence.
- **Actions:** per wave, verify with evidence — not assertions — that regulatory constraints are implemented, transferring controls operate in the target, CUECs are configured, rollback is demonstrated (a rollback never exercised is a hypothesis), and every open gap is either treated or covered by a signed exception. Decide go / conditional go / no-go and record it. After the final wave, schedule the provider's ongoing monitoring per [vendor-onboarding](vendor-onboarding.md) step 6 and set the post-migration control test cycle.
- **Outputs:** recorded go/no-go decision per wave; post-migration monitoring schedule.
- **Decision gate:** a failed rollback demonstration or an unapproved above-appetite gap is a no-go for that wave. Schedule pressure is not an approval authority.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Classified migration inventory | 1 | Migration file / CMDB |
| Regulatory constraints list | 2 | Applicability register annex |
| Provider assessment + contract requirements | 3 | Vendor file |
| Disposition-tagged control map | 4 | Control library |
| Gap-risk register entries | 5 | Risk register |
| Signed exceptions | 6 | Exception register |
| Go/no-go records + monitoring schedule | 7 | Migration file; vendor inventory |

## Failure modes

- **"The cloud provider handles security."** Shared responsibility read as full transfer. The CUEC extract in step 3 and the disposition map in step 4 exist precisely to enumerate what stayed yours — which, for configuration, identity, and data, is most of it.
- **Contract signed before assurance.** The provider deal closes, then security reviews it; every step 3 contract requirement becomes a favor to ask instead of a term to demand.
- **Lift-and-shift control assumption.** Assuming on-prem controls transfer unchanged. Network controls, backup schemes, and monitoring rarely survive the move intact — that is what the "transfers" tag forces you to verify per control.
- **Residency discovered after migration.** Data localization or transfer constraints found once regulated data is already in a non-compliant region. Step 2's gate exists so this is a planning event, not an incident.
- **Dual-running gap.** Legacy controls switched off at wave 1 while dependent workloads migrate in wave 3. Sequence decommissioning against the wave plan, and test the seams.
- **Carve-out blindness.** Relying on the provider's SOC 2 without noticing the subservice carve-outs and the services outside the report's scope. Assess the services you actually consume.
- **Go-live by momentum.** The cutover date approved months ago outranks the open gaps. The step 7 gate with a no-go option — used at least occasionally — is what keeps the rest of the workflow honest.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
