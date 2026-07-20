# CIS Critical Security Controls v8 / v8.1

## At a glance

| Attribute | Detail |
|---|---|
| Owner / publisher | Center for Internet Security (CIS) — community-developed, consensus-based |
| Current version | v8 (May 2021); v8.1 (June 2024) — an iterative refresh, not a restructure |
| Structure | 18 Controls → 153 Safeguards (v8 called them Safeguards; pre-v8 "sub-controls") |
| Prioritization | 3 Implementation Groups: IG1 ⊂ IG2 ⊂ IG3 |
| Certifiable? | No formal certification scheme. Self-assessment (commonly via CIS CSAT tool) or third-party attestation by agreement |
| Typical use | Prioritized technical baseline for small/mid organizations, "where do we start" roadmaps, ransomware-defense benchmarking, measurable hygiene metrics |
| Cost | Free (registration required for download) |
| Related but distinct | **CIS Benchmarks** = per-technology hardening guides (OS, cloud, DB). The Controls are the program-level framework; Benchmarks operationalize Controls 4/12-style hardening per platform |

## The 18 controls

| # | Control | Focus |
|---|---|---|
| 1 | Inventory and Control of Enterprise Assets | Know every device (end-user, network, IoT, servers; on-prem, cloud, remote) |
| 2 | Inventory and Control of Software Assets | Authorized software only; unauthorized software found and removed |
| 3 | Data Protection | Data inventory, classification, handling, retention, disposal, encryption |
| 4 | Secure Configuration of Enterprise Assets and Software | Hardening baselines for devices, OS, software, network devices |
| 5 | Account Management | Inventory and manage accounts incl. admin and service accounts |
| 6 | Access Control Management | Grant/revoke processes, MFA, least privilege, role-based access |
| 7 | Continuous Vulnerability Management | Scan, prioritize, remediate on a defined cadence |
| 8 | Audit Log Management | Collect, retain, protect, and review logs |
| 9 | Email and Web Browser Protections | DNS filtering, attachment controls, browser/plugin management |
| 10 | Malware Defenses | Anti-malware deployment, behavior-based detection |
| 11 | Data Recovery | Automated backups, protected/isolated copies, tested restoration |
| 12 | Network Infrastructure Management | Secure network architecture and up-to-date network devices |
| 13 | Network Monitoring and Defense | Detection, traffic filtering, segmentation enforcement, NIDS/HIDS |
| 14 | Security Awareness and Skills Training | Program covering phishing, data handling, incident recognition |
| 15 | Service Provider Management | Inventory, classify, assess, and monitor third parties holding data |
| 16 | Application Software Security | Secure SDLC, dependency management, appsec testing |
| 17 | Incident Response Management | IR plan, roles, contacts, exercises, post-incident review |
| 18 | Penetration Testing | Periodic external/internal pen tests; findings drive remediation |

Ordering is deliberately prioritized: Controls 1-2 (asset and software inventory) are first because everything else depends on knowing what you have.

## Safeguards

Each control decomposes into **safeguards** — 153 in total across v8/v8.1 — each a single, specific, measurable action, numbered `control.safeguard` (e.g., 1.1 "Establish and Maintain Detailed Enterprise Asset Inventory", 5.2 relates to unique passwords, 6.4 to MFA for remote access — verify exact titles against the current CIS publication before quoting them in deliverables).

Each safeguard is tagged with:

- **Asset class** it applies to (devices, software, data, users, network, documentation; v8.1 adds refinements — see below)
- **Security function** (v8: Identify/Protect/Detect/Respond/Recover; v8.1 adds **Govern**, aligning with NIST CSF 2.0)
- **Implementation Group(s)** it belongs to

## Implementation Groups (IGs)

IGs are the framework's prioritization scheme — cumulative subsets of the 153 safeguards. Each IG includes all safeguards of the ones below it.

| IG | Safeguards | Cumulative | Intended profile |
|---|---|---|---|
| IG1 | 56 | 56 | "Essential cyber hygiene." Small orgs, limited IT/security expertise, primarily commodity-threat exposure. CIS positions IG1 as the minimum standard of care for every enterprise |
| IG2 | +74 | 130 | Organizations with dedicated IT/security staff, multiple departments, moderate regulatory exposure |
| IG3 | +23 | 153 | Mature organizations, sensitive data at scale, targeted-attack exposure; includes the most expert-dependent safeguards (e.g., much of Control 18) |

Assessment guidance:

- **Pick the IG first, then assess.** Scoring a 50-person company against all 153 safeguards produces a demoralizing and misleading gap list. IG1 is the honest baseline for most SMEs.
- Fifteen of the 18 controls have at least one IG1 safeguard; Controls 13 (Network Monitoring and Defense), 16 (Application Software Security), and 18 (Penetration Testing) have none and start at IG2 — small orgs are not expected to run those programs as baseline hygiene.
- CIS publishes analyses showing IG1 safeguards defend against the majority of common attack techniques (mapped via MITRE ATT&CK in the CIS Community Defense Model) — useful evidence when justifying an IG1-first roadmap to leadership.

## v8.1 changes (June 2024)

v8.1 is a minor revision — same 18 controls, same 153 safeguards, same IG allocations. Changes:

- **Governance alignment:** added Govern to the security-function taxonomy to align with NIST CSF 2.0's Govern function; safeguards with governance character (policy/process establishment, documentation) are tagged accordingly.
- **New/clarified asset classes** and an expanded glossary for more consistent interpretation (e.g., clearer treatment of documentation as an asset class).
- **Clarified safeguard descriptions** — wording cleanups, no new obligations.

Practical impact: assessments performed against v8 remain valid; update taxonomy tags rather than re-assessing.

## Mapping ecosystem

CIS maintains and publishes official mappings from the Controls to other frameworks — one of the richest free mapping sets available:

- NIST CSF (2.0 and 1.1) — see [nist-csf-2.md](nist-csf-2.md)
- ISO/IEC 27001/27002:2022 — see [iso-27001-2022.md](iso-27001-2022.md)
- NIST SP 800-53 Rev. 5 and 800-171 — see [nist-800-53.md](nist-800-53.md)
- PCI DSS v4.x — see [pci-dss-4.md](pci-dss-4.md)
- MITRE ATT&CK (via the Community Defense Model)
- Various regulatory regimes (e.g., HIPAA Security Rule crosswalks published by CIS and third parties)

Mappings are directional and lossy: a CIS safeguard mapping to an ISO control does not mean implementing one satisfies the other — granularity differs (safeguards are narrower than most ISO controls, broader than most 800-53 control enhancements). Use mappings for coverage analysis, not equivalence claims. See [control-mapping](../../skills/control-mapping/SKILL.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).

## Using this in assessments

- **Scoring model:** common practice is per-safeguard status (not implemented / partially / implemented / automated) with policy-defined vs. actually-enforced tracked separately. The CIS CSAT tool scores policy, implementation, automation, and reporting dimensions per safeguard.
- **CIS shines where prescriptive beats abstract.** Use CIS when the audience is IT operations needing a concrete to-do list; use CSF or ISO when the audience is executives or auditors needing program structure. Many programs run both: ISO/CSF as the frame, CIS safeguards as the implementation-level evidence layer.
- **Ransomware/incident readiness reviews:** Controls 1, 2, 4, 5, 6, 7, 8, 10, 11, 17 form the core defensive set; Control 11 (tested, isolated backups) is the single most common fatal gap.
- **Regulatory leverage:** several US state safe-harbor statutes recognize the CIS Controls as a qualifying framework for breach-litigation affirmative defense (alongside NIST CSF and ISO 27001) — check the specific statute; see [us-state-privacy.md](../regulations/us-state-privacy.md).
- **Vendor assessments:** asking a small vendor for their IG1 self-assessment yields far more signal than sending them a 300-question ISO-derived questionnaire. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
- **Metrics:** safeguard implementation percentage by IG and by control is a clean, board-friendly hygiene metric — but pair it with outcome metrics (patch latency, inventory coverage) to avoid checkbox drift. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).

Related skills: [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md), [control-testing](../../skills/control-testing/SKILL.md), [control-mapping](../../skills/control-mapping/SKILL.md).

## Primary sources

- [CIS Critical Security Controls — official download and mappings](https://www.cisecurity.org/controls)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
