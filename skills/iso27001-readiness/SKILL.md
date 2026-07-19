---
name: iso27001-readiness
description: >-
  Prepares an organization for ISO/IEC 27001:2022 certification: defining a defensible ISMS
  scope, meeting clause 4-10 requirements (risk assessment, treatment, internal audit,
  management review), producing the Statement of Applicability across all 93 Annex A controls,
  assembling mandatory documented information, and passing stage 1 and stage 2 audits. Use when
  a user says "ISO 27001 prep", "get certified", "build an ISMS", "SoA", or "stage 1 audit".
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Take an organization from no ISMS (or an informal one) to ready for an ISO/IEC 27001:2022 certification audit: scoped, risk-assessed, documented, internally audited, and management-reviewed, with a complete Statement of Applicability. Output is a readiness plan and the core ISMS artifacts — certification itself requires an accredited certification body.

## When to use

- Preparing for first ISO/IEC 27001:2022 certification, or transitioning an ISMS from 27001:2013.
- Fixing nonconformities from a failed or rocky stage 1/stage 2.
- Building or overhauling the Statement of Applicability.
- A customer or tender requires ISO 27001 certification.
- **Not for:** a maturity gap analysis against ISO without certification intent — use [framework-gap-assessment](../framework-gap-assessment/SKILL.md). SOC 2 — use [soc2-readiness](../soc2-readiness/SKILL.md) (run it after this one for the delta; the control overlap is large). Running the risk assessment methodology itself in depth — use [risk-assessment](../risk-assessment/SKILL.md). Executing the internal audit's control tests — use [control-testing](../control-testing/SKILL.md).

## Inputs to gather

1. **Certification driver and deadline** — which contract/market requires the certificate and by when. Work backward: stage 2 must finish before the deadline, stage 1 typically 4-8 weeks before stage 2, internal audit and management review before stage 1.
2. **Candidate scope** — legal entities, sites, products/services, and supporting functions under consideration.
3. **Existing artifacts** — policies, risk registers, asset inventories, prior audits or certifications (SOC 2 evidence reuses well).
4. **Organizational context** — interested parties (customers, regulators, owners) and applicable legal/regulatory requirements (feeds clause 4 and A.5.31; check [regulatory-applicability](../regulatory-applicability/SKILL.md)).
5. **Resourcing** — who owns the ISMS day-to-day, and whether an independent internal auditor (person or firm) is available.

## Procedure

### 1. Define the ISMS scope (clause 4)

Document context: external/internal issues (4.1), interested parties and their requirements (4.2), then the scope (4.3) — a mandatory document stating what is in and, by implication, what is out, considering interfaces and dependencies with out-of-scope and third-party services.

A **defensibly narrow scope** is legitimate and common — e.g., "the ISMS supporting the development, delivery, and operation of the X platform from the Dublin and remote engineering organization" — provided:

- It covers the service the certification driver actually cares about. A certificate scoped to "corporate IT helpdesk" is worthless to a customer buying the SaaS product; customers read the scope statement on the certificate.
- Boundaries are real: in-scope systems and people must be separable in practice (own asset inventory, access domains, processes). If the whole company shares one IdP, one laptop fleet, and one engineering org, scoping out "corporate" is hard to defend at stage 2.
- Dependencies crossing the boundary are treated like suppliers: identified at interfaces, risk-assessed, and controlled (internal SLAs, A.5.19-A.5.23 logic applied internally).

Decision point: small orgs (<~150 people) usually certify the whole organization — the overhead of defending a boundary exceeds the savings. Narrow scope pays off in large orgs where one business unit needs the certificate.

### 2. Walk clauses 4-10 (the certifiable requirements)

Annex A gets the attention; clauses 4-10 get the nonconformities. All clauses are mandatory — no exclusions. Build/verify each:

| Clause | Requirement | Readiness action |
|---|---|---|
| 4 Context | Issues, interested parties, scope, ISMS establishment | Context analysis + scope document (step 1) |
| 5 Leadership | Top management commitment, information security policy (5.2), roles/responsibilities (5.3) | Policy approved by top management; ISMS roles assigned in writing; leadership able to speak to the ISMS at audit — auditors interview executives |
| 6 Planning | Risk assessment process (6.1.2), risk treatment process + SoA (6.1.3), security objectives (6.2), planning of changes (6.3) | Define and run the methodology (step 3); measurable objectives with owners and dates |
| 7 Support | Resources, competence (7.2), awareness (7.3), communication, documented information control (7.5) | Competence records; awareness program with evidence; document control (versioning, approval, availability) |
| 8 Operation | Operational planning, running the risk assessment (8.2) and treatment (8.3) at planned intervals and on significant change | Executed risk assessment with dated results; treatment plan in motion |
| 9 Performance evaluation | Monitoring and measurement (9.1), internal audit (9.2), management review (9.3) | Metrics defined and collected ([grc-metrics-reporting](../grc-metrics-reporting/SKILL.md)); steps 6 and clause-9.3 review below |
| 10 Improvement | Continual improvement (10.1), nonconformity and corrective action (10.2) | Nonconformity log with root-cause analysis and corrective actions — auditors want to see the loop working, not an empty log |

Management review (9.3) must cover the standard's required inputs — status of prior actions, changes in context, ISMS performance feedback (nonconformities, monitoring results, audit results, objectives fulfillment), interested-party feedback, risk assessment results, treatment plan status, improvement opportunities — and produce recorded decisions. Hold at least one real, minuted review before stage 1.

### 3. Risk assessment and treatment (6.1.2, 6.1.3, 8.2, 8.3)

1. Define the methodology: risk criteria (acceptance criteria and assessment criteria), how risks are identified (the 2022 standard does not mandate asset-threat-vulnerability decomposition — scenario-based is acceptable), analysis scales, and risk owners. Method detail: [risk-assessment](../risk-assessment/SKILL.md) and [../../context/risk-scoring.md](../../context/risk-scoring.md).
2. Execute it over the scope; record results (mandatory documented information).
3. Select treatment for each risk (modify/retain/avoid/share); for modified risks, determine necessary controls, then **compare against Annex A** to verify nothing necessary was overlooked — Annex A is a completeness check, not a starting menu.
4. Produce the risk treatment plan and obtain risk owners' approval of the plan and acceptance of residual risks (explicit 6.1.3 requirements auditors check).
5. Route deliberate acceptances of above-appetite risk through [exception-management](../exception-management/SKILL.md).

### 4. Produce the Statement of Applicability (6.1.3 d)

The SoA lists **all 93 Annex A controls** (ISO/IEC 27002:2022 set — 4 themes: A.5 Organizational ×37, A.6 People ×8, A.7 Physical ×14, A.8 Technological ×34) and for each: applicable or excluded, justification **both ways** (inclusion justified by risk treatment, legal/contractual requirement, or business practice; exclusion justified by why the risk/scenario does not apply), and implementation status. Necessary controls not in Annex A (from other frameworks) are added too.

Use the template at [../../templates/statement-of-applicability.md](../../templates/statement-of-applicability.md). Justification patterns, defensible exclusions, and SoA-related nonconformities: [references/soa-guide.md](references/soa-guide.md). Version the SoA and keep it consistent with the risk treatment plan and the policy suite — auditors cross-check all three.

### 5. Assemble mandatory documented information

Verify every item the standard explicitly requires exists, is controlled per 7.5, and is current. Full list with clause references: [references/mandatory-documents.md](references/mandatory-documents.md). Draft missing policies with [policy-authoring](../policy-authoring/SKILL.md); refresh stale ones with [policy-review](../policy-review/SKILL.md). Do not gold-plate: documentation beyond what the standard requires and the org can operate becomes a nonconformity generator ("says here you do X monthly — show me").

### 6. Internal audit before stage 1 (9.2)

Non-negotiable sequencing: a full internal audit — covering clauses 4-10 and the applicable Annex A controls per the SoA — plus a management review that considers its results must be complete before stage 1. Requirements: an audit programme, defined criteria/scope per audit, auditor objectivity and impartiality (someone who does not operate the controls; a small org may hire it out or cross-audit), reported results, and nonconformities entering the 10.2 corrective action loop. An internal audit that found zero nonconformities reads as ineffective to certification auditors — depth beats cleanliness. Use [audit-preparation](../audit-preparation/SKILL.md) for logistics and [control-testing](../control-testing/SKILL.md) for test design.

### 7. Stage 1 vs stage 2 — know what each tests

- **Stage 1 (documentation/readiness review, often partly remote):** auditor reviews scope, SoA, risk methodology and results, mandatory documents, and confirms internal audit + management review happened; assesses readiness for stage 2 and flags "areas of concern." Expect findings; fix them before stage 2 (typically 4-8 weeks later).
- **Stage 2 (certification audit, on site/interviews):** auditor tests implementation and effectiveness — interviews staff and leadership, samples evidence and records, walks controls declared in the SoA. Outcome: minor nonconformities (certificate granted subject to corrective action plans) or major nonconformities (certificate withheld until corrected and verified). Majors typically arise from a broken mandatory process (no internal audit, risk assessment not performed, SoA contradicting reality), not from a single weak technical control.

Ensure evidence spans a real operating period: certification bodies expect the ISMS to have operated long enough to generate records — roughly 3 months of operation is a common practical minimum before stage 2.

### 8. Plan the surveillance and recertification cycle

The certificate runs on a 3-year cycle: surveillance audits (reduced scope, sampled) in years 1 and 2, full recertification in year 3. Surveillance reliably checks: internal audit and management review performed since last visit, corrective actions on prior findings closed, changes to scope/risks/SoA handled, continued top-management engagement. Calendarize the annual rhythm now — risk assessment review, internal audit, management review, SoA/policy refresh — so surveillance is routine, not a scramble. Track regulatory changes affecting A.5.31 obligations via [regulatory-horizon-scanning](../regulatory-horizon-scanning/SKILL.md).

## Output format

Deliver an **ISO 27001 Readiness Package**:

1. **Scope statement** (draft 4.3 document) with boundary rationale and interface/dependency register.
2. **Clause 4-10 conformity checklist** — per requirement: conforms / gap / evidence pointer.
3. **Risk assessment summary** — methodology reference, top risks, treatment decisions, residual-risk acceptances.
4. **Statement of Applicability** — all 93 controls per the template.
5. **Documented information register** — mandatory items with status (exists/current/missing) per [references/mandatory-documents.md](references/mandatory-documents.md).
6. **Remediation plan and timeline** — gaps with owners/dates, then: internal audit → management review → stage 1 → corrective window → stage 2.

Worked example (conformity checklist excerpt):

| Req | Requirement | Status | Evidence / gap |
|---|---|---|---|
| 5.2 | Information security policy established, communicated | Conforms | Policy v3.1, CEO-approved 2026-04, on intranet, acknowledgment 97% |
| 6.1.3 | Risk treatment plan; risk owner approval + residual acceptance | Gap | Plan exists; residual risk acceptance not recorded — add sign-off field, obtain by 2026-08-15 |
| 9.2 | Internal audit conducted | Gap | Not yet performed — external auditor engaged, fieldwork w/c 2026-09-07 |

## Quality checklist

- [ ] Scope statement documented; every cross-boundary dependency identified and risk-treated; scope wording is what the certificate should say.
- [ ] Every clause 4-10 requirement mapped to evidence or an owned, dated gap.
- [ ] Risk assessment executed within the last 12 months with recorded results; risk owners approved the treatment plan and accepted residual risks.
- [ ] SoA covers all 93 Annex A controls; every exclusion justified; no SoA/risk-treatment/policy contradictions.
- [ ] All mandatory documented information exists and is version-controlled per 7.5.
- [ ] Internal audit (clauses + Annex A per SoA) and management review with all required inputs completed before stage 1; nonconformities in the 10.2 loop.
- [ ] ≥3 months of ISMS operating records available before stage 2.
- [ ] 3-year surveillance/recert calendar drafted.
- [ ] Deliverable states certification requires an accredited certification body.

## References

- [references/mandatory-documents.md](references/mandatory-documents.md) — documented information required by the standard, with clause references.
- [references/soa-guide.md](references/soa-guide.md) — defensible SoA justifications, exclusion examples, common stage 1/2 nonconformities.
- [../../templates/statement-of-applicability.md](../../templates/statement-of-applicability.md) — SoA template.
- [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md) — standard overview, Annex A themes.
- [../../context/risk-scoring.md](../../context/risk-scoring.md) — risk analysis methods.
- [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md) — risk assessment execution.
- [../audit-preparation/SKILL.md](../audit-preparation/SKILL.md) — internal and external audit logistics.
- [../soc2-readiness/SKILL.md](../soc2-readiness/SKILL.md) — parallel attestation track.
- [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md) — legal register inputs (A.5.31).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
