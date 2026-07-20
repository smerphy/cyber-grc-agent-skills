# FedRAMP — U.S. Federal Cloud Authorization

## At a glance

| Attribute | Detail |
|---|---|
| Owner | U.S. General Services Administration (GSA) runs the FedRAMP Program Management Office (PMO) |
| Full name | Federal Risk and Authorization Management Program |
| Statutory footing | FedRAMP Authorization Act (enacted December 2022 as part of the FY2023 NDAA, codified at 44 U.S.C. § 3607 et seq.); originally an OMB policy program (2011 memo) |
| Control basis | NIST SP 800-53 Rev. 5 baselines with FedRAMP overlays: Low, Moderate, High, plus LI-SaaS |
| Structure | Authorization of a specific **cloud service offering (CSO)** at a specific impact level — not of a company |
| Certifiable? | Yes in effect — "FedRAMP Authorized" status on the FedRAMP Marketplace, backed by an agency ATO |
| Assessor | Independent Third Party Assessment Organization (3PAO), accredited via A2LA |
| Who needs it | Cloud providers selling to U.S. federal agencies; agencies must use authorized offerings for federal data in the cloud |
| Cost/licensing | Program documents free; the authorization itself is a substantial multi-hundred-thousand-dollar, multi-quarter effort |

## What FedRAMP is

FedRAMP is the U.S. government's "do once, use many times" security authorization program for cloud. A cloud service offering is assessed once against a FedRAMP baseline by an independent 3PAO, authorized by a federal agency, and the resulting package is reused by any other agency instead of each agency re-assessing from scratch. The FedRAMP Authorization Act (2022) put the program on a statutory basis, established the FedRAMP Board, and created a presumption that agencies will rely on existing FedRAMP authorizations.

Two things practitioners routinely get wrong:

- FedRAMP authorizes a **specific offering at a specific boundary** — "Acme Corp is FedRAMP authorized" is meaningless; "Acme GovCloud Platform, Moderate, authorized via agency X" is a real claim. Always check the Marketplace listing for the exact service and impact level.
- FedRAMP is **not a certificate a vendor can buy**: it requires a federal agency customer willing to issue an Authority to Operate (ATO). No agency demand, no authorization.

## Baselines

FedRAMP baselines start from the SP 800-53 Rev. 5 Low/Moderate/High baselines (see [nist-800-53.md](./nist-800-53.md)), then add controls, mandate organization-defined parameter (ODP) values, and attach program requirements (continuous monitoring, scanning, reporting):

| Baseline | Based on | Typical use |
|---|---|---|
| **LI-SaaS** (Low Impact SaaS, "FedRAMP Tailored") | Reduced subset of the Low baseline | Low-risk SaaS handling no PII beyond login; streamlined documentation |
| **Low** | 800-53 Low + overlay | Publicly releasable / low-impact federal data |
| **Moderate** | 800-53 Moderate + overlay | The workhorse — the large majority of authorizations; CUI-class data. Also the reference point for DFARS "FedRAMP Moderate equivalent" cloud requirements (see [nist-800-171-cmmc.md](./nist-800-171-cmmc.md)) |
| **High** | 800-53 High + overlay | Law enforcement, emergency services, health, financial — high-impact unclassified data |

Control counts per baseline changed when FedRAMP moved from Rev. 4 to Rev. 5 baselines (2023); quote counts from the current published baseline documents rather than memory. FedRAMP-mandated ODP values are non-negotiable — a gap assessment against a FedRAMP baseline must use FedRAMP's parameter values, not the organization's preferred ones.

## Authorization paths

- **Agency authorization** — the standard path: a sponsoring federal agency works with the CSP and 3PAO, reviews the package, and issues an ATO; the PMO reviews and lists the offering as Authorized for government-wide reuse.
- **JAB P-ATO (historic)** — the Joint Authorization Board (DoD, DHS, GSA CIOs) formerly issued provisional ATOs for high-demand offerings. The FedRAMP Authorization Act replaced the JAB with a **FedRAMP Board**, and the program has since moved away from the JAB path; packages previously under the JAB were transitioned to program oversight. Treat any "JAB" language in older documentation as legacy.
- **FedRAMP 20x** — announced in 2025, a modernization effort aiming at machine-readable evidence, automated validation, and a faster, less document-centric authorization model, piloted initially for low-baseline cloud-native SaaS. This is **actively evolving** — the paths, phases, and requirements have changed repeatedly; verify the current state on fedramp.gov before advising a vendor on which route to take.

Agencies can also grant a single-agency ATO outside FedRAMP in narrow cases, but OMB policy and the Act push federal cloud usage through FedRAMP.

## Key artifacts

The authorization package is the deliverable set; these acronyms come up constantly:

| Artifact | What it is |
|---|---|
| **SSP** (System Security Plan) | The core document: boundary description, data flows, and per-control implementation statements with ODP values. Hundreds of pages at Moderate; increasingly OSCAL machine-readable. |
| **SAP** (Security Assessment Plan) | The 3PAO's test plan — scope, methodology, sampling, schedule. |
| **SAR** (Security Assessment Report) | The 3PAO's findings: what was tested, what passed, risks identified with severity. |
| **POA&M** (Plan of Action and Milestones) | The living register of open findings and remediation milestones — maintained monthly forever, not just at authorization. |
| **ConMon deliverables** | Continuous monitoring: **monthly** vulnerability scans (OS, web, database, container as applicable), POA&M updates, and inventory; **annual** 3PAO assessment of a control subset; significant change requests before major changes; incident reporting per FedRAMP/US-CERT requirements. |

Remediation clocks apply to scan findings by severity (high findings on the order of 30 days, moderate 90, low 180 — verify current ConMon guidance). Failing ConMon is how authorized offerings lose their status.

## The 3PAO

A 3PAO is an assessment firm accredited (via A2LA under ISO/IEC 17020) to perform FedRAMP assessments. The 3PAO writes the SAP, performs testing including penetration testing, and issues the SAR — it attests, it does not authorize. Independence rules apply: the 3PAO cannot assess a package it helped build. Roughly analogous roles elsewhere: C3PAO in CMMC, QSA in PCI DSS ([pci-dss-4.md](./pci-dss-4.md)), external assessor firms in HITRUST ([hitrust-csf.md](./hitrust-csf.md)).

## Marketplace statuses

The FedRAMP Marketplace (marketplace.fedramp.gov) lists offerings by status:

- **Ready** — a 3PAO has completed a Readiness Assessment Report (RAR) and the PMO deems the offering ready to pursue authorization. Time-limited; not an authorization.
- **In Process** — actively working toward authorization with an agency sponsor.
- **Authorized** — holds an ATO; the package is reusable government-wide.

In third-party risk reviews, verify the status, impact level, authorization date, and service boundary directly on the Marketplace — vendors routinely blur "in process" and "authorized," and blur which of their products is actually in the boundary. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).

## StateRAMP / GovRAMP

A separate nonprofit program (launched as StateRAMP, later rebranded GovRAMP) applies the same 800-53-based model to U.S. **state and local government** procurement, with its own PMO and marketplace. It accepts FedRAMP reciprocity in many cases. If a vendor sells to states, universities, or municipalities, it may be asked for StateRAMP/GovRAMP rather than (or in addition to) FedRAMP — verify current program naming and reciprocity rules, which have been in flux.

## Should a SaaS vendor pursue FedRAMP? (practical guidance)

Questions to work through before committing — this decision is a business case, not a security one:

1. **Is there real federal demand?** You need an agency sponsor to get authorized. "Federal would be a nice market someday" does not justify the spend; a signed-intent agency or a channel partner with federal contracts might.
2. **Total cost is dominated by engineering, not paperwork.** Typical drivers: a separated federal boundary (often a dedicated environment, e.g., AWS GovCloud), FIPS 140-validated cryptography everywhere, U.S. personnel/support constraints for some customers, vulnerability management at ConMon cadence, and headcount to feed monthly ConMon indefinitely. All-in first-year costs commonly run well into six figures; treat vendor-quoted shortcuts skeptically.
3. **Timeline is quarters, not weeks** — readiness, remediation, 3PAO assessment, and agency review commonly total 12–18+ months on the traditional path. FedRAMP 20x aims to compress this; verify current reality.
4. **Alternatives and stepping stones:** inheriting from an authorized IaaS/PaaS reduces (but does not eliminate) scope; LI-SaaS is cheaper where it fits; DoD customers layer DoD SRG impact levels (IL2/IL4/IL5) on top of FedRAMP — a further requirement, not an alternative.
5. **Once in, you cannot coast:** ConMon is a permanent operating cost, and a lapsed POA&M discipline puts the ATO at risk.

## Using this in assessments

- **As evidence in vendor reviews:** a FedRAMP Moderate/High authorization is among the strongest third-party security signals available — a 3PAO-tested 800-53 control set with ongoing monitoring. But confirm the *service you are buying* is inside the authorized boundary, and remember commercial (non-federal) environments of the same vendor are often a different, unassessed stack.
- **Gap assessments toward FedRAMP:** fix the target baseline and boundary first, use FedRAMP's ODP values and templates, and assess at the control-enhancement level. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md) and [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
- **Reuse of the work:** a FedRAMP Moderate implementation substantially covers 800-171 (see [nist-800-171-cmmc.md](./nist-800-171-cmmc.md)), maps well into SOC 2 and ISO 27001 ([soc2-tsc.md](./soc2-tsc.md), [iso-27001-2022.md](./iso-27001-2022.md)) via [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md), and generates audit-ready evidence habits ([../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md)).
- **Common pitfalls:** treating FedRAMP as a company-level certificate; scoping the boundary after writing the SSP instead of before; assuming inherited controls from the IaaS need no customer-side implementation statement; ignoring ConMon staffing in the business case; quoting Rev. 4-era control counts against Rev. 5 baselines.

## References

- Related frameworks: [nist-800-53.md](./nist-800-53.md) (control basis), [nist-800-171-cmmc.md](./nist-800-171-cmmc.md) (CUI and DFARS equivalency), [soc2-tsc.md](./soc2-tsc.md), [iso-27001-2022.md](./iso-27001-2022.md)
- Crosswalk: [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md)
- Skills: [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md), [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md), [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md)

## Primary sources

- [FedRAMP official site (baselines, templates, marketplace, 20x updates)](https://www.fedramp.gov)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
