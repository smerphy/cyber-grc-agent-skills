# COBIT 2019

## At a glance

| Attribute | Detail |
|---|---|
| Owner / publisher | ISACA (Information Systems Audit and Control Association) |
| Current version | COBIT 2019 (released late 2018/2019, superseding COBIT 5); check ISACA for focus-area publications issued since |
| Structure | 40 governance and management objectives: 5 governance (EDM01–EDM05) + 35 management across four domains (APO, BAI, DSS, MEA) |
| Scope | Enterprise governance of information and technology (I&T) — **not** a security control catalog |
| Certifiable? | No organizational certification. Individual credentials exist (COBIT Foundation and related ISACA certificates); organizational use is self-directed or assessed via capability/maturity reviews |
| Typical use | IT governance operating models, IT audit universes, board-level IT oversight and reporting, capability assessments, SOX ITGC heritage scoping |
| Cost | Core framework publications free to ISACA members / purchasable otherwise — verify current access model |

COBIT is the odd one out in this directory: it governs *how IT is directed and managed*, not *which security controls exist*. GRC and audit teams meet it constantly anyway, because it defines the process universe most IT audit functions and ITGC programs descend from.

## Governance vs management — the core split

COBIT 2019's defining distinction:

- **Governance** (board/owner level): evaluate stakeholder needs, direct through prioritization and decision-making, monitor performance and compliance — the EDM (Evaluate, Direct, Monitor) objectives.
- **Management** (executive/operational level): plan, build, run, and monitor activities in line with the direction set by governance.

| Domain | Prefix | Objectives | Theme |
|---|---|---|---|
| Evaluate, Direct and Monitor | EDM | EDM01–EDM05 | Governance proper: framework setting, benefits delivery, risk optimization, resource optimization, stakeholder engagement |
| Align, Plan and Organize | APO | APO01–APO14 | Strategy, architecture, portfolio, budgets, HR, relationships, agreements, quality, **risk (APO12)**, **security (APO13)**, data |
| Build, Acquire and Implement | BAI | BAI01–BAI11 | Programs/projects, requirements, solution build, availability/capacity, organizational change, IT change, acceptance, knowledge, assets, configuration |
| Deliver, Service and Support | DSS | DSS01–DSS06 | Operations, service requests/incidents, problems, continuity, **security services (DSS05)**, business process controls |
| Monitor, Evaluate and Assess | MEA | MEA01–MEA04 | Performance monitoring, internal control system, compliance with external requirements, assurance |

40 objectives total (5 + 14 + 11 + 6 + 4). Exact objective titles are stable but verify wording against the ISACA "Governance and Management Objectives" publication before quoting — several were renamed from their COBIT 5 process equivalents.

Security-relevant anchor points: **APO12 (Managed Risk)**, **APO13 (Managed Security)**, and **DSS05 (Managed Security Services)** are where an ISMS or security program plugs into the COBIT process model; **MEA03/MEA04** are where regulatory compliance and assurance activity plug in.

## Design factors and the goals cascade

COBIT 2019 replaced one-size-fits-all adoption with a tailoring method:

- **Goals cascade:** stakeholder needs → enterprise goals → alignment goals (renamed from COBIT 5's "IT-related goals") → governance/management objectives. Used to justify *why* a given objective matters and to trace board concerns down to processes — useful scaffolding for audit-planning rationale.
- **Design factors:** a defined set of tailoring inputs — enterprise strategy, enterprise goals, risk profile, current I&T issues, threat landscape, compliance requirements, role of IT, sourcing model, implementation methods, technology adoption strategy, enterprise size (ISACA lists eleven; verify the exact enumeration). Applying them through the "Designing an I&T Governance Solution" guide yields a prioritized subset of the 40 objectives with target capability levels, rather than treating all 40 as equally applicable.

For assessors, the design factors are a defensible way to answer "why didn't you assess everything?" — the same role Implementation Groups play in CIS or scoping plays in ISO 27001.

## Components of a governance system

Each objective is described through seven **components** (COBIT 5 called them "enablers"):

1. Processes (with practices and activities — the most used component)
2. Organizational structures (who decides; suggested RACI-style charts per objective)
3. Principles, policies and frameworks
4. Information (inputs/outputs between practices)
5. Culture, ethics and behavior
6. People, skills and competencies
7. Services, infrastructure and applications

Practical takeaway: COBIT explicitly reminds you that a "process gap" may actually be a structure, skills, or culture gap — a framing worth borrowing in any root-cause analysis, even outside COBIT engagements.

## Capability levels

COBIT 2019 uses a CMMI-derived capability scheme, scored 0–5 per process (via the process activities, each associated with a capability level):

| Level | Meaning (abbreviated) |
|---|---|
| 0 | Incomplete — process not implemented or fails its purpose |
| 1 | Performed — achieves its purpose, largely ad hoc |
| 2 | Managed — planned, monitored, adjusted |
| 3 | Established — defined, organization-wide process |
| 4 | Predictable — quantitatively measured |
| 5 | Optimizing — continuously improved |

This replaced COBIT 5's ISO/IEC 15504-based assessment model. Scores are per-objective, and the design phase sets *target* levels — most organizations legitimately target level 2–3 for most objectives; a blanket target of 5 is a red flag in any COBIT-based roadmap. ISACA also describes maturity at the focus-area level distinct from per-process capability — verify terminology before writing assessment criteria around it.

## How it complements ISO 27001 / NIST CSF

COBIT is a **governance wrapper**; ISO 27001/27002, NIST CSF, and CIS are **security program and control catalogs**. They answer different questions:

| Question | Best-fit framework |
|---|---|
| How does the board direct and monitor IT (including security) investment and risk? | COBIT (EDM domain) |
| What should the security management system contain? | [ISO 27001](iso-27001-2022.md) |
| What security outcomes/functions should the program cover? | [NIST CSF](nist-csf-2.md) |
| Which technical safeguards first? | [CIS Controls](cis-controls-v8.md) |

Common stack: COBIT for enterprise I&T governance and the audit universe; ISO 27001 or CSF for the security program inside it (hanging off APO12/APO13/DSS05); CIS or [800-53](nist-800-53.md) at the control layer. ISACA publishes an Information Security focus-area publication elaborating the security lens over COBIT — verify its current edition. Mapping COBIT objectives to security controls is coarse; use it for coverage narrative, not control-level evidence. See [control-mapping](../../skills/control-mapping/SKILL.md).

## Where GRC teams meet COBIT

- **IT audit universes.** Most internal-audit IT risk universes are COBIT-derived (often still recognizably COBIT 4.1/5 process lists). Knowing the domain structure lets you read an audit plan and spot coverage holes quickly.
- **SOX ITGC heritage.** The classic ITGC domains — access to programs and data, program changes, program development, computer operations — were popularized through COBIT-based SOX guidance in the mid-2000s. Modern ITGC scoping still echoes APO/BAI/DSS structure; see [sox-itgc.md](../regulations/sox-itgc.md).
- **Board IT governance reporting.** EDM objectives plus the goals cascade give a ready-made structure for "how do we know IT is governed" board papers, and capability levels give a defensible scale for trend reporting — see [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).
- **External assurance and regulator dialogues.** In some jurisdictions and sectors, regulators and external auditors frame IT governance expectations in COBIT terms; being able to translate your ISO/CSF program into COBIT objectives shortens those conversations.

## Relationship to ISACA certifications and audit practice

COBIT is ISACA's house framework, so it permeates ISACA's credential ecosystem: CISA (audit), CRISC (risk), CGEIT (governance of enterprise IT), and CISM (security management) exam content and ISACA audit programs reference it, and ISACA publishes COBIT-based audit/assurance programs practitioners reuse as workpaper skeletons. Expect COBIT vocabulary ("control objective," capability levels, EDM/APO/BAI/DSS/MEA) from anyone ISACA-trained — which is a large share of the IT audit population.

## Using this in assessments

- **Don't run COBIT as a control gap assessment.** Assess capability of prioritized objectives against design-phase targets; a 40-objective, all-targets-level-5 gap list is a methodology error, not a finding. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).
- **Use it to assess governance, not controls.** When the engagement question is "is security *governed* well" (board oversight, risk appetite, investment decisions), EDM01–EDM05 + APO12/APO13 + MEA01–MEA04 is the right lens; when the question is "are controls operating," go to ISO/CIS/800-53 and [control-testing](../../skills/control-testing/SKILL.md).
- **Evidence for capability levels** is process evidence — charters, RACI, meeting minutes, KPIs, improvement records — not technical artifacts. Set expectations with the client accordingly.
- **Translate, don't duplicate.** If an ISO 27001 ISMS exists, map its clauses/Annex A themes into the relevant COBIT objectives for the governance narrative rather than building a parallel assessment; see [iso27001-readiness](../../skills/iso27001-readiness/SKILL.md).
- **Watch for version drift:** many "COBIT" artifacts in the field are COBIT 5 or even 4.1 vintage. Confirm which version an audit universe or client maturity model actually descends from before comparing results.

Related skills: [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md), [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md), [audit-preparation](../../skills/audit-preparation/SKILL.md), [risk-assessment](../../skills/risk-assessment/SKILL.md).

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
