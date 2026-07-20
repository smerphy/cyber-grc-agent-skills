# NIST Cybersecurity Framework (CSF) 2.0

## At a glance

| Attribute | Detail |
|---|---|
| Owner / publisher | US National Institute of Standards and Technology (NIST) |
| Current version | CSF 2.0, published February 26, 2024 (supersedes CSF 1.1, 2018) |
| Structure | 6 Functions → 22 Categories → 106 Subcategories |
| Certifiable? | No. CSF is a voluntary framework, not a certifiable standard. No accredited certification scheme exists; "CSF-aligned" claims are self-attestations |
| Scope | All organizations, all sectors, all sizes (1.1 was framed around critical infrastructure; 2.0 explicitly targets everyone) |
| Typical use | Risk-based program structuring, board/executive communication, maturity baselining via tiers, gap assessment via current-vs-target profiles, common language for crosswalking other frameworks |
| Cost | Free (public document) |

## The six functions

CSF 2.0 organizes cybersecurity outcomes into six functions. Govern is new in 2.0 and sits at the center, informing how the other five are implemented.

| Function | ID | Intent |
|---|---|---|
| Govern | GV | Establish and monitor cybersecurity risk management strategy, expectations, and policy |
| Identify | ID | Understand assets, suppliers, and risks to prioritize effort |
| Protect | PR | Safeguards to manage cybersecurity risk |
| Detect | DE | Find and analyze possible cybersecurity attacks and compromises |
| Respond | RS | Take action regarding detected incidents |
| Recover | RC | Restore assets and operations affected by incidents |

Functions are outcomes, not a sequential lifecycle: Govern, Identify, Protect run continuously; Detect, Respond, Recover are exercised as events occur.

## Categories

The 22 categories with their identifiers. Subcategories (106 total) hang off these as `XX.YY-nn` (e.g., GV.SC-06, ID.AM-01).

### Govern (GV) — 6 categories

| ID | Category |
|---|---|
| GV.OC | Organizational Context |
| GV.RM | Risk Management Strategy |
| GV.RR | Roles, Responsibilities, and Authorities |
| GV.PO | Policy |
| GV.OV | Oversight |
| GV.SC | Cybersecurity Supply Chain Risk Management |

### Identify (ID) — 3 categories

| ID | Category |
|---|---|
| ID.AM | Asset Management |
| ID.RA | Risk Assessment |
| ID.IM | Improvement |

Note: ID.IM (Improvement) consolidates improvement outcomes that were scattered across functions in 1.1 — lessons learned from incidents, tests, and exercises feed here.

### Protect (PR) — 5 categories

| ID | Category |
|---|---|
| PR.AA | Identity Management, Authentication, and Access Control |
| PR.AT | Awareness and Training |
| PR.DS | Data Security |
| PR.PS | Platform Security |
| PR.IR | Technology Infrastructure Resilience |

PR.PS (Platform Security) absorbs much of 1.1's PR.IP (Information Protection Processes) and PR.MA (Maintenance): configuration management, software/hardware maintenance, secure development.

### Detect (DE) — 2 categories

| ID | Category |
|---|---|
| DE.CM | Continuous Monitoring |
| DE.AE | Adverse Event Analysis |

### Respond (RS) — 4 categories

| ID | Category |
|---|---|
| RS.MA | Incident Management |
| RS.AN | Incident Analysis |
| RS.CO | Incident Response Reporting and Communication |
| RS.MI | Incident Mitigation |

### Recover (RC) — 2 categories

| ID | Category |
|---|---|
| RC.RP | Incident Recovery Plan Execution |
| RC.CO | Incident Recovery Communication |

## Tiers

Tiers characterize the rigor of an organization's cybersecurity risk governance and management practices. They apply to the program as a whole (often assessed per-function), not to individual subcategories. Tiers are NOT a maturity model in the CMMI sense, and NIST is explicit that Tier 4 is not the universal goal — the right tier is a risk/cost decision.

| Tier | Name | Characterization |
|---|---|---|
| 1 | Partial | Ad hoc, reactive; limited risk awareness; irregular practices |
| 2 | Risk Informed | Management approves practices; risk awareness exists but org-wide policy and process are inconsistent |
| 3 | Repeatable | Formal, approved policy; practices regularly updated from risk changes; org-wide consistency |
| 4 | Adaptive | Practices adapt from lessons learned and predictive indicators; cybersecurity embedded in organizational culture and decision-making |

In 2.0, tier definitions cover two dimensions: cybersecurity risk **governance** and cybersecurity risk **management** (including third-party considerations).

## Profiles

A **profile** is a selection of CSF outcomes tailored to an organization's mission, risk appetite, and resources.

- **Current profile** — outcomes the organization achieves today, and to what degree.
- **Target profile** — outcomes it aims to achieve, prioritized by risk.
- The gap between current and target profiles is the core CSF assessment output and drives the remediation roadmap. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).
- **Community profiles** — baseline target profiles published for a sector, technology, or threat context (e.g., sector bodies and NIST publish profiles for specific industries and use cases). Organizations adopt a community profile as a starting target and tailor it.

## Informative references

Each subcategory can be linked to **informative references**: mappings to specific controls in other sources (ISO/IEC 27001, NIST SP 800-53, CIS Controls, COBIT, etc.). In 2.0 these live outside the core document in NIST's online **Cybersecurity and Privacy Reference Tool (CPRT)** so mappings can be updated without republishing the framework. NIST also publishes **implementation examples** — concrete, non-exhaustive action statements per subcategory — as a separate online resource.

Practical implication: CSF is a natural "hub" taxonomy for control mapping. Map your control set to CSF subcategories once, then leverage published mappings to reach other frameworks. See [control-mapping](../../skills/control-mapping/SKILL.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).

## Changes from CSF 1.1

| Change | Detail |
|---|---|
| Govern function added | Governance outcomes (strategy, roles, policy, oversight) elevated from scattered 1.1 categories into a sixth function at the framework's center |
| Supply chain elevated | Cybersecurity supply chain risk management moved into Govern as GV.SC with expanded outcomes, reflecting post-SolarWinds emphasis |
| Scope broadened | Title dropped "for Improving Critical Infrastructure Cybersecurity"; explicitly for all organizations |
| Structure consolidated | 1.1's 5 functions / 23 categories / 108 subcategories became 6 / 22 / 106; several 1.1 categories merged (e.g., PR.IP dissolved into PR.PS, ID.IM, and others) |
| References externalized | Informative references and implementation examples moved to online CPRT for living updates |
| Profiles formalized | Clearer current/target profile methodology; community profiles introduced as a named concept |

When updating an assessment performed against 1.1, do not assume subcategory IDs carried over — many were renumbered or moved (NIST publishes a 1.1-to-2.0 transition mapping in the CPRT).

## Using this in assessments

- **Choose the assessment unit deliberately.** CSF subcategories are outcome statements, not controls. Assess "to what degree is this outcome achieved and how do we know," not "is this control implemented." Evidence lives in your actual control set — map it first.
- **Rate with a defined scale.** CSF prescribes no scoring scale. Common practice: a 0-4 or 1-5 achievement scale per subcategory, rolled up to category level for reporting. Define the scale and anchor descriptions before scoring, or results are not comparable across assessors or years. See [risk scoring pitfalls](../../context/risk-scoring.md).
- **Do not conflate tiers with subcategory scores.** Tiers describe governance/management rigor across the program; a program can be Tier 3 while individual subcategories score low. Report them separately.
- **Set the target profile before scoring the current one** where politically feasible — otherwise targets drift toward current state.
- **Govern findings usually have the highest leverage.** Weak GV.RM or GV.OV outcomes explain systemic weaknesses elsewhere; lead executive reporting with them.
- **Regulatory tie-ins:** CSF is referenced or accepted as a baseline in several regimes (e.g., US state safe-harbor statutes, FTC expectations, sector guidance). It does not by itself satisfy prescriptive regimes like [PCI DSS](pci-dss-4.md) or certifiable ones like [ISO 27001](iso-27001-2022.md).

Related skills: [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md), [control-mapping](../../skills/control-mapping/SKILL.md), [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).

## Primary sources

- [NIST CSF 2.0 (CSWP 29), official PDF](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)
- [NIST Cybersecurity Framework program page (tools, profiles, informative references)](https://www.nist.gov/cyberframework)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
