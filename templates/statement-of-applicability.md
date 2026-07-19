# Statement of Applicability (SoA) — ISO/IEC 27001:2022

**How to use:** The SoA is a required ISO 27001 document (clause 6.1.3): it lists the Annex A controls, states for each whether it is applicable, justifies inclusions **and** exclusions, and records implementation status. Populate one row for each of the 93 Annex A controls — the five example rows below show the expected quality across the four themes, including one justified exclusion; do not submit an SoA with blanket "best practice" justifications. Control catalog and themes: [../context/frameworks/iso-27001-2022.md](../context/frameworks/iso-27001-2022.md). Certification preparation: [../skills/iso27001-readiness/SKILL.md](../skills/iso27001-readiness/SKILL.md).

Rules that auditors check:
- Every applicable control's justification must trace to a **risk assessment result, a legal/regulatory/contractual obligation, or a business requirement** — name it, with an ID.
- Exclusions must be justified by absence of the risk or activity, and must remain consistent with the ISMS scope statement. An exclusion contradicted by reality (e.g., excluding outsourced development while a contractor writes code) is a nonconformity.
- Controls beyond Annex A (e.g., from other frameworks) may be added; Annex A is a reference set to check against, not a ceiling.
- Version the SoA and re-issue after each risk assessment cycle or scope change.

## Header

| Field | Value |
|---|---|
| Organization / ISMS scope reference | [Scope statement doc ID and version — the SoA only makes sense against a defined scope] |
| Risk assessment reference | [Risk assessment report ID, date, and methodology reference — see [../skills/risk-assessment/SKILL.md](../skills/risk-assessment/SKILL.md)] |
| Risk treatment plan reference | [Doc ID — the SoA and RTP must reconcile] |
| SoA version / date | [e.g., 3.0 / YYYY-MM-DD] |
| Approved by | [Role — typically ISMS owner or steering committee] |
| Implementation status values | Implemented / Partially implemented / Planned (with date) / Not implemented |

## Control applicability table

*93 rows total: organizational controls 5.1-5.37, people controls 6.1-6.8, physical controls 7.1-7.14, technological controls 8.1-8.34. Example rows:*

| Control ID | Control title | Applicable | Justification for inclusion/exclusion | Implementation status | Evidence ref |
|---|---|---|---|---|---|
| 5.1 | Policies for information security | Y | Required to direct the ISMS; addresses governance risk R-021 (inconsistent security practice across units); supports contractual security commitments in enterprise MSAs | Implemented | POL-001 policy set; approval minutes ISSC-2026-02; annual review log |
| 5.23 | Information security for use of cloud services | Y | Core delivery model — all production workloads on IaaS/SaaS; treats risks R-002 (SaaS provider breach) and R-017 (cloud misconfiguration); required by customer contracts mandating cloud governance | Partially implemented — cloud service onboarding standard live; exit-strategy documentation planned 2026-10 | CLD-STD-01; vendor register; CSPM reports |
| 6.3 | Information security awareness, education and training | Y | Treats risk R-001 (ransomware via phishing — see risk register); legal driver: staff-training expectations under multiple applicable regimes | Implemented | LMS completion reports (>96% FY26); phishing simulation results; onboarding curriculum |
| 7.10 | Storage media | Y | Laptops and backup media in scope hold confidential data; treats risk R-009 (data loss via lost/discarded media); disposal obligations under data protection law | Implemented | Media handling standard OPS-STD-04; disposal certificates; encryption compliance report |
| 8.16 | Monitoring activities | Y | Detection capability required by risk treatment for R-001 and R-003; contractual 24x7 monitoring commitment to two enterprise customers | Partially implemented — SIEM coverage complete for Tier-1; Tier-2 log sources onboarding through 2026-09 | SIEM coverage matrix; SOC runbook; alert-handling metrics |
| 8.30 | Outsourced development | **N** | **Excluded:** all software development within ISMS scope is performed by directly employed staff; no development is outsourced and no such engagement is planned. Consistent with scope statement §2.3. Trigger for re-inclusion: any contract engaging external parties for development. | N/A | Reviewed against supplier register 2026-06 — no development suppliers |

*...continue for all remaining Annex A controls.*

## Reconciliation checks (before approval)

- [ ] Every risk treatment in the RTP that relies on a control maps to an applicable SoA row, and vice versa for "Planned" entries
- [ ] No exclusion conflicts with the scope statement, supplier register, or asset inventory
- [ ] Evidence refs resolve to real, current artifacts (spot-check 10%)
- [ ] Version incremented and prior version archived

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
