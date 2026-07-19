# Writing a Defensible Statement of Applicability

The Statement of Applicability (SoA) is required by ISO/IEC 27001:2022 clause 6.1.3 d). It is the document auditors use to plan stage 2 testing, the document customers request most after the certificate, and the most common source of avoidable nonconformities. This guide covers structure, justification writing (both directions), defensible exclusions, and the failure patterns seen at stage 1 and stage 2.

Template: [../../../templates/statement-of-applicability.md](../../../templates/statement-of-applicability.md).

## What the SoA must contain

For each of the 93 Annex A controls (27002:2022 set — A.5 Organizational ×37, A.6 People ×8, A.7 Physical ×14, A.8 Technological ×34), plus any necessary controls not in Annex A:

1. **Applicability** — applicable or excluded.
2. **Justification for inclusion** — *why* the control is necessary. Valid sources: risk treatment (control mitigates identified risks — cite risk IDs), legal/regulatory/contractual obligation (cite the requirement), or established business practice/policy the organization commits to.
3. **Justification for exclusion** — why the control is not necessary: the risk scenario it addresses does not exist in the scoped environment.
4. **Implementation status** — implemented / partially implemented / planned (with date). "Applicable, not implemented" is legitimate pre-certification if the treatment plan covers it; at stage 2 an applicable-but-absent control with no credible plan is a nonconformity.

Recommended extra columns that cost little and pay off at audit: linked risk IDs, implementing policy/procedure reference, control owner, and evidence pointer. Version the SoA, date it, and record approval — auditors check that the SoA in front of them is the current one and matches the risk treatment plan.

Controls from other frameworks (SOC 2 commitments, PCI DSS requirements, NIST SP 800-53 obligations under a contract) that the risk treatment determined necessary belong in the SoA's additional-controls section — the SoA describes the organization's actual control set, with Annex A as its completeness backstop.

## Writing inclusion justifications

Weak SoAs justify inclusion with "best practice" on all 93 rows. That tells the auditor the risk assessment and the SoA are disconnected — a finding waiting to happen. Write justifications that trace:

**Bad:** "A.8.13 Information backup — Applicable. Industry best practice."

**Good:** "A.8.13 Information backup — Applicable. Treats R-014 (loss of customer data through ransomware or operator error) and R-021 (single-region storage failure); contractual RPO of 24h in enterprise MSA §7. Implemented: automated daily snapshots, 35-day retention, quarterly restore tests. Owner: Head of Infrastructure. Evidence: backup policy v2.1, restore test log."

**Bad:** "A.6.1 Screening — Applicable. Required by ISO 27001."

(Annex A controls are not "required by ISO 27001" — only the controls the risk treatment determines necessary are. This wording signals misunderstanding of 6.1.3.)

**Good:** "A.6.1 Screening — Applicable. Treats R-030 (insider access to customer data by personnel with falsified credentials); customer contract security exhibits require background checks for staff with production access. Implemented via HR pre-employment screening procedure, proportionate to role and local law."

A pattern is acceptable for genuinely universal controls: "Treats baseline risks R-001/R-002 (unauthorized access to information assets) applicable to all in-scope systems" — as long as those risk IDs exist and the register supports them.

## Writing exclusion justifications

An exclusion says: the scenario this control addresses cannot materialize in the scoped environment. It must survive an auditor walking the floor. Rules:

- Justify with **absence of the activity or asset**, never with cost, effort, or "low risk." "Too expensive" means the risk exists and is being accepted — that is a risk-acceptance decision (clause 6.1.3, routed through risk owners), and the control is *applicable*, treatment "retain," not excluded.
- Check the exclusion against the whole scope, including remote workers, contractors, and dev/test environments.
- Expect the auditor to test the premise: excluding A.7.4 (physical security monitoring) because "we have no premises" fails the moment the auditor learns of the storage unit with old laptops.

### Defensible exclusion examples

| Control | Exclusion justification | Holds only if… |
|---|---|---|
| A.6.7 Remote working | Not excludable for most orgs post-2020 — listed here as a warning: excluding it while any employee works from home is a classic stage 2 finding | Truly no remote work, enforced technically |
| A.7.x (subset of physical controls, e.g., A.7.8 equipment siting, A.7.12 cabling security) | Fully remote organization with no premises; all infrastructure is cloud IaaS whose physical controls are the provider's, verified via provider certifications under A.5.19-A.5.22 | No office, no server room, no self-managed racks; provider assurance reviews actually happen. Note: A.7 controls covering endpoints and home working (e.g., A.7.9 assets off-premises, A.7.7 clear desk/screen as policy) usually remain applicable |
| A.8.30 Outsourced development | All development performed by in-scope employees; no development is outsourced | No agencies, no outsourced feature teams; individual contractors managed under A.6 personnel controls are inside the boundary — document that reasoning |
| A.5.16-A.5.18 identity/access (exclusion attempt) | Not excludable in any real organization — every org has identities and access to manage | — |
| A.8.14 Redundancy of information processing facilities | No availability commitments; service is an internal batch tool with tolerance for multi-day outage, per risk assessment R-xx | No customer SLA exists anywhere; risk owners accepted availability risk on record |

Exclusions should be few. A first-time SoA for a cloud SaaS company typically excludes somewhere between zero and a handful of controls (mostly physical/outsourced-development items). Ten or more exclusions is a signal to re-check scope definition or risk assessment coverage.

## Common SoA-related nonconformities at stage 1 and stage 2

| Nonconformity | Stage seen | Root cause | Prevention |
|---|---|---|---|
| SoA missing controls (not all 93 addressed; org used the 2013 list of 114 or a vendor's abbreviated list) | Stage 1 | Stale template | Rebuild from the 27002:2022 control set; map any 2013-era ISMS through the standard's transition mapping |
| No justification for exclusions, or "N/A" as justification | Stage 1 | Treating the SoA as a checkbox | Write scenario-absence justifications per above |
| Inclusion justifications not traceable to risk assessment, legal register, or policy | Stage 1-2 | SoA written before/without the risk assessment | Generate the SoA *from* the risk treatment exercise; add risk ID column |
| SoA contradicts reality: control marked implemented, not operating (e.g., "A.8.13 implemented," no restore test ever run) | Stage 2 — often major | Aspirational SoA | Evidence pointer per row; verify each during internal audit |
| SoA contradicts other documents: policy mandates a control the SoA excludes, or risk treatment plan lists a control the SoA omits | Stage 1-2 | No cross-checking | Reconcile SoA ↔ risk treatment plan ↔ policy suite before internal audit |
| SoA not current: organization changed (new product, new site, moved to cloud) but SoA predates the change | Surveillance/stage 2 | No trigger to update | Tie SoA review to clause 6.3 change planning and the annual risk assessment |
| Exclusion justified by cost or "risk accepted" | Stage 1 | Category confusion | Move to applicable + treatment "retain" with risk-owner acceptance record |
| No approval/version control on the SoA | Stage 1 | 7.5 not applied | Treat the SoA as controlled documented information: owner, version, approval record |
| Additional necessary controls (from contracts/regulation) absent | Stage 2 | Annex A treated as a ceiling | Sweep the legal/contractual register (A.5.31 work, [regulatory-applicability](../../regulatory-applicability/SKILL.md)) for control obligations beyond Annex A |

## Worked rows

| ID | Control | Applicable | Justification | Status | Risks | Reference |
|---|---|---|---|---|---|---|
| A.5.23 | Information security for use of cloud services | Yes | Treats R-008 (misconfigured cloud services exposing customer data), R-019 (cloud provider lock-in/exit risk); DPA obligations to assess subprocessors | Implemented | R-008, R-019 | Cloud security standard v1.4; provider review records |
| A.7.14 | Secure disposal or re-use of equipment | Yes | Treats R-027 (data recovery from disposed laptops); contractual data-destruction commitments | Implemented | R-027 | Asset disposal procedure; destruction certificates |
| A.8.30 | Outsourced development | No | All software development performed by employees within ISMS scope; no development activities are outsourced to external organizations. Individual contractors are onboarded under the same personnel and access controls as employees (A.6.1-A.6.6, A.5.16-A.5.18) | — | — | HR/contractor policy |
| A.7.4 | Physical security monitoring | No | Organization operates no physical premises; all personnel are remote and all processing occurs in cloud provider facilities. Provider physical monitoring verified annually via its certifications under supplier management (A.5.22) | — | — | Supplier review record: IaaS provider |

## Maintenance rhythm

Re-approve the SoA at least annually and on significant change (new products, architecture shifts, new legal obligations, M&A). Practical trigger set: annual risk assessment refresh, any change routed through clause 6.3 planning, and any new contract whose security exhibit adds control obligations. Keep prior versions — surveillance auditors ask what changed and why.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
