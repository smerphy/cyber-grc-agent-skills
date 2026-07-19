# NERC CIP (Critical Infrastructure Protection)

## At a glance

| Attribute | Detail |
|---|---|
| Owner / publisher | North American Electric Reliability Corporation (NERC), the FERC-certified Electric Reliability Organization (ERO) for North America |
| Legal force | **Mandatory and enforceable** for registered entities. In the US, backed by FERC under Federal Power Act §215 (Energy Policy Act of 2005); Canadian provinces adopt/adapt the standards through their own regulators (Mexico participation is narrower — verify current status) |
| Current version | Standards are versioned individually (e.g., CIP-003-9, CIP-005-7) and change on rolling FERC-approval cycles — always confirm the currently effective version of each standard, not "NERC CIP" as a whole |
| Structure | A family of CIP Reliability Standards (CIP-002 through CIP-014 core set, plus newer additions such as CIP-015), each with numbered Requirements (R1, R2, …) and detailed requirement parts/attachments |
| Certifiable? | Not a certification. Compliance is monitored and enforced by Regional Entities under the ERO Compliance Monitoring and Enforcement Program (CMEP): audits, spot checks, self-certifications, self-reports, complaints |
| Typical use | Bulk electric system (BES) cyber/physical security programs at utilities, generation and transmission operators; OT/ICS security benchmarking; supply-chain requirements flowing down to vendors |
| Penalties | Civil monetary penalties in the US can reach on the order of $1M+ per violation per day (statutory maximum, inflation-adjusted upward over time — verify the current figure); actual penalties are risk-based and most violations settle far below the cap |

## Who is covered

NERC CIP applies to **registered entities** — organizations registered with NERC/their Regional Entity for functions affecting the bulk electric system, such as balancing authorities, reliability coordinators, transmission owners/operators, generator owners/operators, and certain distribution providers. Registration (in the NERC Compliance Registry) is what triggers applicability; an unregistered vendor or a distribution-only utility below thresholds is not directly subject, though CIP-013 pushes obligations into the supply chain contractually.

Key applicability nuances:

- Scope is the **bulk electric system** (roughly, higher-voltage generation and transmission per the BES definition) — most pure distribution assets fall outside, subject to defined inclusion criteria. Verify against the current NERC BES definition; the boundary is technical and litigated.
- Canadian adoption varies **by province** (some adopt standards essentially as-is with jurisdictional edits, on their own timelines) — confirm the provincial instrument for any Canadian entity.
- Cloud and third-party hosting for in-scope systems has historically been constrained by how requirements are worded; NERC has active work modernizing this — treat "can we put it in the cloud" as a current-rules question, not a settled one.

## CIP-002: categorization drives everything

CIP-002 requires entities to identify and categorize **BES Cyber Systems** by the impact their compromise would have on the BES, using bright-line criteria (in the standard's attachment):

| Impact level | Rough profile | Consequence |
|---|---|---|
| High | Large control centers (e.g., those controlling major transmission/generation footprints) | Full weight of the CIP requirement set |
| Medium | Larger generation facilities, significant transmission stations/substations, certain control centers — per specific MW/kV bright-line criteria in the standard | Most requirements, with some relaxations vs high |
| Low | All other BES Cyber Systems | Reduced, policy/plan-level obligations (largely via CIP-003) |

The requirement applicability tables in every other CIP standard key off this categorization (often further refined by connectivity attributes such as external routable connectivity). Consequence: **the categorization exercise is the highest-stakes control in the whole regime** — an under-categorized asset silently voids downstream compliance. Do not quote specific MW/kV thresholds from memory; verify against the current CIP-002 attachment.

## The standard family (title level)

Titles paraphrased; verify exact titles and effective versions on the NERC standards site.

| Standard | Subject |
|---|---|
| CIP-002 | BES Cyber System categorization (high/medium/low impact) |
| CIP-003 | Security management controls — policies, delegated authority; carries most low-impact obligations |
| CIP-004 | Personnel & training — risk assessments (background checks), training, access management/revocation |
| CIP-005 | Electronic Security Perimeter(s) — network boundaries, remote access controls |
| CIP-006 | Physical security of BES Cyber Systems — physical security plans, access controls, monitoring |
| CIP-007 | System security management — ports/services, patching, malware, logging, credentials |
| CIP-008 | Incident reporting and response planning — including mandatory reporting of incidents (and attempts) to E-ISAC/authorities within defined timeframes |
| CIP-009 | Recovery plans for BES Cyber Systems — backup, restoration, plan testing |
| CIP-010 | Configuration change management and vulnerability assessments — baselines, change authorization, periodic assessments |
| CIP-011 | Information protection — identifying and protecting BES Cyber System Information (BCSI) |
| CIP-012 | Protecting communications between control centers |
| CIP-013 | Supply chain cyber risk management — procurement plans, vendor risk controls for in-scope systems |
| CIP-014 | Physical security of critical transmission stations/substations and control centers (risk assessment + protection plans; driven by the 2013 Metcalf substation attack) |
| CIP-015 | Internal network security monitoring (INSM) inside the electronic security perimeter — **recent addition**; approved and being phased in during the mid-2020s. Verify current approval status, applicability (initially high/certain medium impact), and enforcement dates before relying on it |

Each standard decomposes into Requirements and requirement parts with per-impact-level applicability, measures (acceptable evidence), and violation risk factors / violation severity levels used in enforcement.

## Enforcement and audit regime

- **Regional Entities** (currently six: MRO, NPCC, ReliabilityFirst, SERC, Texas RE, WECC — verify, the roster has consolidated over time) execute the CMEP: scheduled compliance audits (historically on multi-year cycles for entities with high/medium-impact systems), spot checks, and investigation of self-reports and complaints.
- **Violations** are processed with risk-based disposition: minimal-risk issues may be resolved as compliance exceptions or via find-fix-track style treatment; serious violations proceed to settlements/penalties filed with FERC (US). Repeat findings and weak internal compliance programs aggravate penalties; strong self-identification and remediation mitigate them.
- **Self-reporting is structurally rewarded.** Mature CIP programs run internal controls that detect and self-report their own noncompliance — a posture voluntary-framework programs rarely build.
- **Evidence retention** obligations are explicit (retention periods are defined per standard — commonly the current audit period; verify per requirement), and auditors expect evidence for *every day* of the compliance period, not point-in-time samples.

## Why it's different from voluntary frameworks

- **Zero-defect, per-day exposure.** Under ISO 27001 a missed patch cycle is a nonconformity; under CIP a missed obligation can be a violation accruing per day, with monetary exposure. This drives a documentation-heavy, "if it isn't evidenced, it didn't happen" culture — and explains why CIP programs feel legalistic compared to ISO/CSF programs.
- **Requirements are the ceiling of the auditable scope, not a maturity aspiration.** Entities are audited against the literal requirement text; good-faith security work outside the text earns no compliance credit, and "compliant" is not the same as "secure" (a standard criticism of the regime).
- **Change is slow and formal.** Standards go through NERC's ANSI-accredited drafting/ballot process plus FERC approval, so requirements lag threats by years — the INSM standard (CIP-015) post-dates the supply-chain and living-off-the-land campaigns that motivated it.
- **No scoping discretion.** You do not choose your scope as with an ISO certification boundary; the BES definition and CIP-002 bright lines choose it for you.

Treat CIP like other mandatory regimes in this library ([SOX ITGC](../regulations/sox-itgc.md), [DORA](../regulations/dora.md), [NIS2](../regulations/nis2.md)) rather than like the voluntary catalogs — applicability analysis first, requirement-literal compliance second, security-program alignment third. For applicability questions see [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md).

## Using this in assessments

- **Start from the CIP-002 asset list and categorization rationale.** Every downstream conclusion inherits its quality. Sample the bright-line analysis, not just the resulting list.
- **Assess per requirement part per impact level**, using the standard's own applicability tables — a generic "CIP-007 gap" is meaningless without stating which systems and which requirement parts.
- **Evidence over assertion, aggressively.** For each sampled requirement, expect dated artifacts covering the full period (e.g., patch evaluation records on the defined cadence, access revocation within required timeframes). Interview answers alone would fail a Regional Entity audit and should fail yours. See [control-testing](../../skills/control-testing/SKILL.md) and [audit-preparation](../../skills/audit-preparation/SKILL.md).
- **Map, don't merge, with corporate frameworks.** Utilities typically run NIST CSF or ISO enterprise-wide with CIP as a compliance overlay on the OT estate; NERC/industry mappings to [NIST CSF](nist-csf-2.md) and [800-53](nist-800-53.md) exist but are coverage aids, not compliance substitutes. See [control-mapping](../../skills/control-mapping/SKILL.md).
- **Supply chain reviews:** CIP-013 makes vendor security plans auditable — procurement language, vendor notifications of incidents/vulnerabilities, software integrity verification. Vendor assessments for CIP entities should test those specific flow-downs; see [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
- **Incident obligations:** CIP-008 reporting (including attempted compromises) runs alongside other regimes an entity may face; keep it in the reporting matrix — see [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md).
- **Track pending standards** (INSM rollout, cloud-use modernization, evolving low-impact requirements) in horizon scanning — enforcement dates arrive on fixed schedules and drive multi-year projects; see [regulatory-horizon-scanning](../../skills/regulatory-horizon-scanning/SKILL.md).

Related skills: [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md), [audit-preparation](../../skills/audit-preparation/SKILL.md), [control-testing](../../skills/control-testing/SKILL.md), [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md).

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
