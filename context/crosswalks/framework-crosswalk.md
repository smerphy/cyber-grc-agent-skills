# Framework Crosswalk (Domain Level)

A navigation aid mapping ~15 common security domains across six frameworks: ISO/IEC 27001:2022 Annex A (control numbering per ISO/IEC 27002:2022), NIST CSF 2.0, CIS Controls v8/v8.1, SOC 2 Trust Services Criteria (2017, revised 2022 points of focus), NIST SP 800-53 Rev. 5 control families, and PCI DSS v4.0.1 requirements.

## How to use this crosswalk — read first

- **Domain granularity only.** Cells point to the control *area* most relevant to each domain, not clause-by-clause equivalence. Two frameworks landing in the same row does NOT mean their controls are interchangeable or that satisfying one satisfies the other.
- **Not compliance evidence.** Never present this table to an auditor or regulator as a mapping deliverable. For defensible mappings, use official sources: the CIS Controls Mappings (published by CIS for ISO 27001, CSF, PCI DSS, and others), NIST's OLIR / Informative References program (available via NIST's Cybersecurity and Privacy Reference Tool), AICPA's SOC 2 mapping publications, and the PCI SSC's own mapping documents. Then validate against your actual control implementations — see [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).
- **Frameworks slice domains differently.** ISO puts secure development under "Technological" controls; CIS has no physical security control; SOC 2 merges logical and physical access into CC6; PCI scopes everything to the cardholder data environment. Expect one-to-many and many-to-one relationships in every row.
- **Abbreviated identifiers.** ISO cells cite Annex A controls (e.g., A.5.15). CSF cells cite categories (e.g., PR.AA) or specific subcategories where a domain maps narrowly. CIS cells cite control numbers 1–18. SOC 2 cells cite common criteria series (CC1–CC9) and category criteria (A, C, PI, P). 800-53 cells cite two-letter families. PCI cells cite requirements 1–12.

Framework detail lives in the per-framework context files — link there rather than restating:
[ISO 27001:2022](../frameworks/iso-27001-2022.md) · [NIST CSF 2.0](../frameworks/nist-csf-2.md) · [CIS v8](../frameworks/cis-controls-v8.md) · [SOC 2 TSC](../frameworks/soc2-tsc.md) · [NIST 800-53](../frameworks/nist-800-53.md) · [PCI DSS v4](../frameworks/pci-dss-4.md)

## Table 1 — ISO 27001 Annex A · NIST CSF 2.0 · CIS Controls v8

| Domain | ISO 27001:2022 Annex A | NIST CSF 2.0 | CIS v8 |
|---|---|---|---|
| Governance & risk management | A.5.1–A.5.8 (+ ISMS clauses 4–10) | GV (all categories), ID.RA, ID.IM | No dedicated control; policy/process expectations embedded per safeguard (v8.1 adds governance emphasis) |
| Asset management | A.5.9–A.5.11 (+ A.5.12–A.5.13 classification) | ID.AM | 1 (enterprise assets), 2 (software) |
| Access control & identity | A.5.15–A.5.18, A.8.2–A.8.5, A.8.18 | PR.AA | 5 (accounts), 6 (access) |
| Cryptography & data protection | A.8.24; A.5.12–A.5.14, A.8.10–A.8.12 | PR.DS | 3 (data protection) |
| Physical & environmental | A.7.1–A.7.14 | PR.AA-06 (physical access); PR.IR (partial) | Not covered |
| Operations security (config, change, malware) | A.8.1, A.8.6–A.8.7, A.8.9, A.8.19, A.8.32, A.5.37 | PR.PS | 4 (secure config), 9 (email/browser), 10 (malware) |
| Network security | A.8.20–A.8.23 | PR.IR-01 (+ PR.DS-02 in transit) | 12 (network infrastructure), 13 (network monitoring/defense) |
| Secure development | A.8.25–A.8.31, A.8.33 | PR.PS-06 | 16 (application software security) |
| Supplier / third-party management | A.5.19–A.5.23 | GV.SC | 15 (service provider management) |
| Incident management | A.5.24–A.5.28, A.6.8 | DE.AE, RS (all), RC (partial) | 17 (incident response management) |
| Continuity & resilience | A.5.29–A.5.30, A.8.13–A.8.14 | RC.RP, RC.CO, PR.IR-03/-04 | 11 (data recovery) |
| Compliance, audit & assurance | A.5.31–A.5.36, A.8.34 | GV.OC-03, GV.OV | No dedicated control |
| HR / people security & awareness | A.6.1–A.6.7 | PR.AT, GV.RR-04 | 14 (awareness & skills training) |
| Logging & monitoring | A.8.15–A.8.17 | DE.CM, DE.AE | 8 (audit logs), 13 (network monitoring) |
| Vulnerability & threat management | A.8.8, A.5.7 (threat intel) | ID.RA-01 (+ ID.RA generally) | 7 (vulnerability management), 18 (penetration testing) |

## Table 2 — SOC 2 TSC · NIST 800-53 r5 · PCI DSS v4

| Domain | SOC 2 TSC | 800-53 r5 families | PCI DSS v4 |
|---|---|---|---|
| Governance & risk management | CC1, CC2, CC3, CC5 | PM, PL, RA, CA | Req 12 |
| Asset management | CC6.1 (partial); no dedicated criterion | CM (CM-8), MP, PM-5 | Req 12.5 (scope/asset inventory), Req 9 (media) |
| Access control & identity | CC6.1–CC6.3 | AC, IA | Req 7, 8 |
| Cryptography & data protection | CC6.1, C-series (confidentiality) | SC (SC-12/13/28), MP | Req 3, 4 |
| Physical & environmental | CC6.4–CC6.5 | PE | Req 9 |
| Operations security (config, change, malware) | CC6.8, CC7.1, CC8.1 | CM, SI (SI-3), MA | Req 2, 5, 6.5 (change control) |
| Network security | CC6.6–CC6.7 | SC (SC-7), AC-4 | Req 1, 4 |
| Secure development | CC8.1 | SA, SI (input validation etc.), CM | Req 6 |
| Supplier / third-party management | CC9.2 | SR, SA-9 | Req 12.8–12.9 (TPSPs) |
| Incident management | CC7.3–CC7.5 | IR | Req 12.10 |
| Continuity & resilience | A1.1–A1.3 (availability), CC9.1 | CP | Not directly addressed |
| Compliance, audit & assurance | CC4.1–CC4.2 | CA, AU (records), PM | Req 12 (12.1 policy, 12.4 compliance program) |
| HR / people security & awareness | CC1.4–CC1.5 | PS, AT | Req 12.6 (awareness), 12.7 (screening) |
| Logging & monitoring | CC7.2 (+ CC7.1) | AU, SI-4 | Req 10 |
| Vulnerability & threat management | CC7.1 | RA (RA-5), SI-2 | Req 6.3 (patching), Req 11 (scans/pen tests) |

## Domain notes and known friction points

- **Governance.** CSF 2.0 elevated governance to its own function (GV) — the strongest governance articulation of the six. ISO covers it partly in Annex A (A.5.1–A.5.8) but mostly in the management-system clauses 4–10, which Annex A crosswalks miss. CIS v8 and PCI treat governance thinly (PCI concentrates it in Requirement 12). When assessing governance maturity, do not rely on a CIS- or PCI-anchored control set alone.
- **Asset management.** SOC 2 has no dedicated inventory criterion; auditors typically test inventories under CC6.1's identification of protected information assets. PCI v4 made scope/asset inventory explicit (12.5.1).
- **Access control.** The cleanest row in the crosswalk — every framework has a substantial, testable access domain. Fine-grained differences remain large (e.g., PCI Req 8 MFA specifics vs. ISO A.8.5's outcome-level "secure authentication").
- **Physical security.** CIS v8 deliberately excludes it. If CIS is your primary framework, source physical controls from ISO A.7 or 800-53 PE.
- **Continuity.** SOC 2 covers it only if Availability is in scope; PCI barely addresses it (incident response plan aside). ISO 27001 covers ICT readiness (A.5.30) but full BCM lives in ISO 22301.
- **Logging vs. monitoring vs. detection.** Frameworks split these differently: CIS separates log management (8) from network defense (13); CSF splits continuous monitoring (DE.CM) from event analysis (DE.AE); PCI folds both into Req 10 plus testing in Req 11. Map at safeguard level before claiming coverage.
- **Vulnerability management.** ISO has a single control (A.8.8); PCI is the most prescriptive (defined scan cadence, ASV scans, pen testing under Req 11). A "compliant" ISO program can be far weaker than a compliant PCI one in this domain — granularity differs by an order of magnitude.

## Beyond the core six

The crosswalk tables above cover the six frameworks most organizations anchor on. The repository also carries packs for frameworks that largely *inherit* or *repackage* the core six — map them by locating their parent rather than extending the tables:

| Framework | Maps through | Note |
|---|---|---|
| [SP 800-171 / CMMC](../frameworks/nist-800-171-cmmc.md) | NIST 800-53 families | 800-171 derives from 800-53; use the 800-53 column, then narrow to CUI scope |
| [FedRAMP](../frameworks/fedramp.md) | NIST 800-53 baselines | 800-53 r5 plus FedRAMP-specific parameters — the 800-53 column applies directly |
| [HITRUST CSF](../frameworks/hitrust-csf.md) | Harmonizes many sources | Ships its own authoritative-source mappings; prefer those over this table |
| [CSA CCM v4](../frameworks/csa-ccm.md) | ISO 27001 / 800-53 | Cloud-specific domains (IPY, SEF) have no clean single parent; map at safeguard level |
| [COBIT 2019](../frameworks/cobit-2019.md) | Governance row mostly | IT governance wrapper, not a security control catalog — expect thin coverage below the governance row |
| [NERC CIP](../frameworks/nerc-cip.md) | Domain rows individually | Sector-mandatory; its own asset-categorization logic (CIP-002) drives everything |
| [ISO 22301](../frameworks/iso-22301.md) | Continuity row | Full BCMS behind the continuity row's ISO A.5.29–A.5.30 cells |
| [ISO 27701](../frameworks/iso-27701.md) | ISO 27001 extension | Adds privacy (PIMS) controls on the 27001 machinery |
| [ISO 42001](../frameworks/iso-42001.md) / [NIST AI RMF](../frameworks/nist-ai-rmf.md) | Governance + new AI domains | AI-specific obligations mostly sit outside these security domains — see [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md) |
| [Essential Eight](../frameworks/essential-eight.md) | CIS v8 subset areas | Eight prioritized mitigations, closest to CIS safeguards; no governance layer |
| [Cyber Essentials](../frameworks/cyber-essentials.md) | Access, network, ops rows | Five baseline technical themes only |
| [TISAX](../frameworks/tisax.md) | ISO 27001 heritage | VDA ISA catalogue follows 27001/27002 structure with automotive additions |

## Related

- [../crosswalks/breach-notification-timelines.md](breach-notification-timelines.md) — regulatory deadline matrix
- [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md) — using this crosswalk in a gap assessment
- [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md) — producing defensible control-level mappings

## Primary sources

- [CIS Controls mappings (official CIS mapping downloads)](https://www.cisecurity.org/controls)
- [NIST OLIR / informative references program](https://csrc.nist.gov/projects/olir)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
