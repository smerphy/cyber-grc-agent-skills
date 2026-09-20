# CISA Cross-Sector Cybersecurity Performance Goals (CPGs) and Secure by Design

## At a glance

| Attribute | Detail |
|---|---|
| Publisher | Cybersecurity and Infrastructure Security Agency (CISA), US Department of Homeland Security. Issued under CISA's technical-assistance authority at 6 U.S.C. §652 |
| Current edition | *Cross-Sector Cybersecurity Performance Goals* **Version 2.0**, cover-dated **December 2025** (resource page publication date 11 December 2025). Supersedes v1.0.1 (21 March 2023); first release October 2022 |
| Origin | Directed by the July 2021 National Security Memorandum on Improving Cybersecurity for Critical Infrastructure Control Systems; developed with NIST |
| Structure (CPG 2.0) | **34 goals** across the six NIST CSF 2.0 functions — Govern 5, Identify 5, Protect 19, Detect 2, Respond 2, Recover 1 |
| Legal status | **Voluntary.** "CISA has no plans to audit entities based on the performance goals." Not a maturity model, not a risk-management programme, not comprehensive — explicitly "a floor, not a ceiling" |
| Who it is for | All 16 critical infrastructure sectors, IT and OT, with small and medium organisations as the priority audience |
| Assessment model | Self-assessment against the CPG Worksheet / CPG Checklist, also carried inside the CPG assessment module of CISA's free Cyber Security Evaluation Tool (CSET). **No certification scheme** |
| Revision cycle | Targeted 24–36 months; sector-specific goals (SSGs) layered on top per sector |
| Companion line of effort | **Secure by Design** — supplier-side guidance (2023 joint whitepaper, 2024 Pledge, Product Security Bad Practices, Secure by Demand) plus the KEV catalog. Also voluntary, except where a binding operational directive applies to federal civilian agencies |
| Related but distinct | NIST CSF 2.0 (the programme frame the CPGs map into), CIS Controls IG1 (a comparable prioritised hygiene baseline), CIRCIA (mandatory reporting) |

## What it is

The CPGs are a prioritised subset of IT and OT cybersecurity practices that CISA selected from observed adversary tactics, techniques and procedures, on three criteria: demonstrated risk-reduction value against commonly observed cross-sector threats; clear, actionable and easily definable; and reasonably straightforward and not cost-prohibitive for small and medium entities. CISA's worked example of the criteria is instructive — "ensuring that none of an organization's internet-facing systems have any known exploited vulnerabilities" qualifies; "implement zero trust" does not, because the target audience cannot yet execute it.

CPG 2.0 (December 2025) is the first substantive rewrite since 2023. It adds a **Govern** function to mirror NIST CSF 2.0, merges the previously separate OT-only goals into a single universal goal set (on the reasoning that modern estates blur IT, IoT and OT), adds four goals covering programme management, managed service provider risk, least privilege and incident communication, and deletes three low-adoption goals whose outcomes were absorbed elsewhere. Every security practice maps to a NIST CSF 2.0 subcategory, with secondary references to SP 800-53 Rev. 5 and SP 800-82 Rev. 3; the CPGs deliberately do **not** cover every subcategory.

**Secure by Design** is the demand- and supply-side counterpart: instead of telling operators what to do, it tells manufacturers what to ship and buyers what to insist on. It comprises the joint whitepaper *Shifting the Balance of Cybersecurity Risk* (April 2023, revised 25 October 2023, co-sealed by CISA and 17 US and international partners), the Secure by Design Pledge (launched 8 May 2024), *Product Security Bad Practices* (October 2024; v2 17 January 2025), and two *Secure by Demand* procurement guides. None of it is binding on manufacturers; its leverage is procurement language, buyer questionnaires and reputational transparency.

## Who it covers / scope

- **CPGs:** any critical infrastructure owner or operator, of any size, in any of the 16 sectors — and, in practice, any organisation looking for a defensible "minimum reasonable practice" baseline. Adoption is voluntary and unenforced by CISA; the practical pull comes from state and sector regulators, insurers, and grant or funding conditions that reference the CPGs.
- **Sector-Specific Goals (SSGs):** additional voluntary practices developed by sector risk management agencies with CISA for a given sector, announced 26 July 2023 and released per sector since.
- **Secure by Design / Bad Practices:** software manufacturers producing on-premises software, cloud services and SaaS used to support critical infrastructure or national critical functions. The Bad Practices document is expressly "non-binding" and "imposes no requirement".
- **Binding element:** only the KEV-linked binding operational directives bite, and only on Federal Civilian Executive Branch agencies; BOD 26-04 excludes statutorily defined national security systems and certain Department of War and Intelligence Community systems. See [us-fisma-federal-cyber.md](../regulations/us-fisma-federal-cyber.md).

## Structure and requirements

### Anatomy of a CPG 2.0 goal

| Field | Content |
|---|---|
| Outcome | The result the goal is meant to enable |
| Recommended action | Example approaches, including OT-specific variants where relevant |
| Risk addressed | The organisational risks made less likely or less impactful |
| Scope | Who or what is responsible / where the goal applies (e.g. "organization-wide", "all organizational assets, to include those that face the internet") |
| NIST CSF 2.0 reference(s) | Subcategory identifiers (e.g. GV.OV-03; ID.RA-01, ID.RA-06, ID.RA-08; RS.CO-03; RC.RP-01) |
| Additional NIST references | SP 800-53 Rev. 5 and SP 800-82 Rev. 3 control identifiers |
| Support resources | CISA services and guidance (KEV catalog, Cyber Hygiene Services, ICS recommended practices, IR playbooks) |
| Cost / Impact / Ease of implementation | Three prioritisation ratings (see below) |

### Goals by function (CPG 2.0)

| Function | Goals | Coverage |
|---|---|---|
| 1 Govern | 5 | Cybersecurity responsibilities; cybersecurity oversight and programme management; incident response plans; supply-chain incident reporting and vulnerability disclosure; managed service provider risk |
| 2 Identify | 5 | Asset management; mitigate known vulnerabilities; independent validation of controls; vulnerability disclosure/reporting process; documented network topology |
| 3 Protect | 19 | Default passwords; password strength; unique credentials; revoking departing-staff credentials; failed-login monitoring; MFA; separate privileged accounts; least privilege; network segmentation; security training; strong encryption; email security; disable autorun/macros; change management; backups and tested restoration; hardware/software approval; log collection and storage; prohibit unauthorised devices; secure internet-facing devices |
| 4 Detect | 2 | Malicious code detection; identify adverse events |
| 5 Respond | 2 | Incident communication procedures; incident reporting procedures |
| 6 Recover | 1 | Execute the incident recovery plan and complete post-incident analysis |

Goal letters were renumbered in 2.0, so v1.0.1 references in old policies and assessments no longer resolve — the report carries a full v1.0.1→2.0 mapping table. One caution on titles: the report's change log calls the new goal 1.B "Proactive Program Management", but the goal pages in the same report and CISA's online CPG 2.0 catalogue both title it "Manage Cybersecurity Oversight" (1.A is "Establish Cybersecurity Responsibilities"). Quote the goal pages, not the change log.

### Prioritisation ratings

| Rating | Low / Simple | Moderate | High / Complex |
|---|---|---|---|
| Cost (implement, maintain, dispose) | <5% of annual security budget | 5–15% of annual security budget | >15% of annual security budget |
| Impact (harm prevented) | Prevents limited adverse effects — mission still supportable | Prevents serious adverse effects — some mission functions lost | Prevents severe or catastrophic effects — mission unsupportable |
| Ease of implementation | A few months, minimal technical expertise | 4–8 months, moderate expertise or management involvement | ~A year or longer, significant expertise and coordination |

CISA states these ratings apply primarily to **IT** infrastructure and do not necessarily extend to OT or other non-IT environments. CPG 2.0 replaced v1.0.1's "Complexity" with "Ease of Implementation" and published the rating logic to make assessments repeatable. Where a goal is not implemented — especially a high-cost one — CISA recommends documenting a cost-benefit analysis covering productivity loss, response effort and replacement costs.

### Sector-Specific Goals

| Sector | Status (September 2026) |
|---|---|
| Information Technology | Released 7 January 2025 — 18 goals (11 software development process, 7 product design) |
| Chemical | Released 7 January 2025 — 3 goals (lifecycle security integration, eliminating unnecessary network components, mobile device management) |
| Energy (electric distribution and distributed energy resources) | Listed as available, but CISA links out to the NARUC/DOE-CESER *Cybersecurity Baselines* (February 2024) rather than a CISA-published SSG document |
| Healthcare and Public Health | Published by HHS as the HPH Cybersecurity Performance Goals, not by CISA (hphcyber.hhs.gov) |
| Financial Services | Still listed as "coming soon (Winter 2025)" on CISA's CPG page as of September 2026 |

### The Secure by Design line of effort

| Artefact | Date | Substance |
|---|---|---|
| *Shifting the Balance of Cybersecurity Risk* | April 2023; revised 25 October 2023 | Three principles: take ownership of customer security outcomes; embrace radical transparency and accountability; lead from the top. The 25 October 2023 revision is co-sealed by CISA and 17 US and international partners |
| Secure by Design Pledge | Launched 8 May 2024 with 68 signatories; over 200 as of September 2026 | Seven goals — MFA, default passwords, reducing entire classes of vulnerability, security patches, vulnerability disclosure policy, CVEs, evidence of intrusions. Each asks the manufacturer to "demonstrate actions taken to measurably increase…" **within one year of signing**. CISA "does not enforce nor verify adherence to the pledge"; signatories self-publish progress reports |
| *Product Security Bad Practices* | October 2024; v2 17 January 2025 | Three categories — Product Properties (8), Security Features (2), Organizational Processes and Policies (3). Named dates: publish a memory-safety roadmap by end of 2025 (not applicable to products with announced end-of-support before 1 Jan 2030); MFA expectations not applicable to products with end-of-support before 1 Jan 2028; on publication of a new KEV, issue a free patch "no longer than 30 days from the date of which a patch for the component containing the KEV is made available" |
| *Secure by Demand Guide* | 6 August 2024 (CISA, FBI) | Buyer-side questions across authentication, eliminating vulnerability classes, intrusion evidence/logging, supply chain and SBOM, vulnerability disclosure |
| *Secure by Demand: Priority Considerations for OT Owners and Operators* | 13 January 2025 (with NSA, FBI, EPA, TSA and seven international partners) | Procurement considerations for OT digital products |
| *2026 Minimum Elements for a Software Bill of Materials (SBOM)* | 29 July 2026 (CISA with NSA, FBI and international partners) | Final guidance that updates and replaces the 2021 NTIA SBOM minimum elements, after an August 2025 draft and public comment. The SBOM questions in the Secure by Demand guides should now be written against it |

### KEV catalog and the directives behind it

The Known Exploited Vulnerabilities catalog lists vulnerabilities meeting three criteria: an assigned CVE ID, reliable evidence of active exploitation in the wild, and clear remediation action. It held **1,716 entries as of 19 September 2026**. CISA tells non-federal organisations to use it "as an input to their vulnerability management prioritization framework" — the Identify function's "mitigate known vulnerabilities" goal is written against it.

| Directive | Date | Effect |
|---|---|---|
| BOD 22-01 | 3 November 2021 | Required FCEB agencies to remediate KEV entries — 6 months for CVEs assigned before 2021, 2 weeks for all others; status reported through the CDM federal dashboard |
| BOD 26-04, *Prioritizing Security Updates Based on Risk* | 10 June 2026 | Revokes BOD 22-01 and BOD 19-02. Risk-based remediation matrix keyed to asset exposure, KEV status, exploit automation and technical impact; windows run 3 days plus forensic triage (publicly exposed + KEV + automatable + total technical impact), then 6, 14, 21, 30, 60, 90 and 180 days by combination, down to "fix on system upgrade" where the asset is neither publicly exposed nor carrying a KEV. Phased implementation: immediate policy and reporting updates, 60 days for vulnerability-process updates, 180 days for remediation to the table and for tagging publicly accessible assets |

## Assessment, certification and evidence

- **No certification exists.** There is no CPG certificate, no accredited assessor scheme, and no Secure by Design conformity assessment. Evidence is self-produced.
- **CPG Worksheet / Checklist:** review and prioritise goals, record current and target state, and communicate trade-offs to non-technical executives. CISA's own method is: self-evaluate, identify and prioritise gaps by cost/impact/ease, invest and execute, then **re-run the worksheet after 12 months**.
- **CSET:** CISA's free Cyber Security Evaluation Tool contains a CPG assessment module. As of September 2026 CISA's CPG page still states that the **CPG 2.0 CSET module and the updated CPG 2.0 Checklist would be available in Q1 2026** — confirm current availability before planning an assessment around it.
- **Credible evidence set** for a CPG claim: the completed worksheet with owner and date per goal, the underlying artefacts (asset inventory extract, MFA coverage report, backup restoration test record, log retention configuration), and a dated remediation plan for gaps. See [control-testing](../../skills/control-testing/SKILL.md) and [audit-preparation](../../skills/audit-preparation/SKILL.md).
- **Supplier-side evidence:** a signed pledge is a commitment, not an attestation — ask for the signatory's published progress report, its vulnerability disclosure policy, CVE issuance practice, and its memory-safety roadmap, and compare against the Bad Practices list. See [vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md).

## Timeline and status

| Date | Event |
|---|---|
| July 2021 | National Security Memorandum directs CISA, with NIST, to develop baseline cybersecurity goals for critical infrastructure |
| October 2022 | Initial CPG release |
| 21 March 2023 | CPG v1.0.1 — reorganised, reordered and renumbered to align with the five NIST CSF functions |
| April 2023 / 25 Oct 2023 | Secure by Design whitepaper published, then revised with international co-sealers |
| 26 July 2023 | Sector-Specific Goals programme announced |
| 8 May 2024 | Secure by Design Pledge launched (68 initial signatories) |
| 6 Aug 2024 / 13 Jan 2025 | Secure by Demand guides (software buyers; OT owners and operators) |
| Oct 2024 / 17 Jan 2025 | Product Security Bad Practices v1 and v2 |
| 7 January 2025 | IT and Chemical Sector-Specific Goals released |
| December 2025 | **CPG 2.0 published** (resource page date 11 December 2025) |
| Q1 2026 (stated) | CPG 2.0 CSET module and updated checklist — still described as forthcoming on CISA's page as of September 2026 |
| 10 June 2026 | BOD 26-04 replaces BOD 22-01 with a risk-based remediation matrix for federal civilian agencies |
| 29 July 2026 | CISA and partners publish the final *2026 Minimum Elements for an SBOM*, replacing the 2021 NTIA elements |
| Next | CPG revision cycle targeted at 24–36 months; Financial Services SSGs outstanding |

## Key obligations for security/GRC teams

1. **Re-baseline against CPG 2.0 numbering.** Any control mapping, policy cross-reference or assessment that cites v1.0.1 goal letters is now stale; use the report's v1.0.1→2.0 mapping table. See [control-mapping](../../skills/control-mapping/SKILL.md).
2. **Treat the CPGs as a floor, layered under a full framework.** They are not a risk-management programme; run them inside NIST CSF 2.0 or ISO 27001. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md) and [nist-csf-2.md](nist-csf-2.md).
3. **Close the Govern goals first if you have none.** Cybersecurity responsibilities, oversight, incident response plans, supply-chain disclosure and MSP risk are the 2.0 additions most organisations cannot evidence. See [policy-authoring](../../skills/policy-authoring/SKILL.md).
4. **Wire the KEV catalog into vulnerability SLAs** and state the internal clock explicitly; federal-adjacent contracts and OT regulators increasingly assume it. See [risk-assessment](../../skills/risk-assessment/SKILL.md).
5. **Use the cost/impact/ease ratings for the funding conversation**, and record a documented cost-benefit analysis for any goal you consciously decline — that record is your exception artefact. See [exception-management](../../skills/exception-management/SKILL.md) and [exception-request.md](../../templates/exception-request.md).
6. **Add Secure by Design questions to procurement**, drawn from the Secure by Demand guides and Bad Practices list, and validate pledge claims against published progress reports. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md) and [vendor-onboarding.md](../../workflows/vendor-onboarding.md).
7. **Check the sector layer before assuming cross-sector coverage is enough** — IT, Chemical, Energy and (via HHS) healthcare goals add obligations the cross-sector set omits.
8. **Report CPG implementation percentage by function** as a board metric, paired with outcome metrics; re-run the worksheet annually as CISA prescribes. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md) and [grc-board-report.md](../../templates/grc-board-report.md).
9. **Do not describe CPG adoption as compliance.** It is voluntary and unaudited by CISA; say "aligned to" and keep the evidence. See [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md).

## Interplay

- **NIST CSF 2.0** — the CPGs are a prioritised entry point that maps into CSF subcategories; CISA says organisations that have implemented the CSF "will not need to perform additional work to implement the relevant CPGs". See [nist-csf-2.md](nist-csf-2.md).
- **CIS Controls IG1** — the closest analogue: both claim to be the minimum standard of care for smaller organisations, both are voluntary and self-assessed. The CPGs are shorter (34 goals vs 56 IG1 safeguards) and carry OT-specific guidance; IG1 is more granular and more measurable. See [cis-controls-v8.md](cis-controls-v8.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).
- **NIST SP 800-53 and SP 800-82** — each CPG carries control references into both, giving a clean path from hygiene baseline to federal control catalogue and to OT. See [nist-800-53.md](nist-800-53.md) and [iec-62443-ot-security.md](iec-62443-ot-security.md).
- **Secure by Design vs SSDF** — SSDF (SP 800-218) is the practice framework a manufacturer implements; Secure by Design is the outcome and transparency posture it advertises. Attestation obligations live with SSDF, not the pledge. See [nist-ssdf-800-218.md](nist-ssdf-800-218.md).
- **Mandatory reporting regimes** — the CPGs' incident reporting goal is a capability, not a legal clock. Actual clocks come from CIRCIA, sector directives and securities rules. See [us-circia.md](../regulations/us-circia.md), [us-tsa-transportation-cyber.md](../regulations/us-tsa-transportation-cyber.md), [nerc-cip.md](../regulations/nerc-cip.md) and [sec-cyber-disclosure.md](../regulations/sec-cyber-disclosure.md).
- **Product-security law** — the EU Cyber Resilience Act and the UK PSTI regime make in law much of what Secure by Design asks for voluntarily; a manufacturer selling into both markets should run one programme. See [eu-cyber-resilience-act.md](../regulations/eu-cyber-resilience-act.md), [uk-psti-product-security.md](../regulations/uk-psti-product-security.md) and [us-fda-medical-device-cybersecurity.md](../regulations/us-fda-medical-device-cybersecurity.md).
- **Healthcare** — the HHS HPH CPGs, not the CISA set, are the sector reference, and they sit alongside (not inside) the HIPAA Security Rule. See [hipaa.md](../regulations/hipaa.md).

## Primary sources

- CISA, *Cross-Sector Cybersecurity Performance Goals, Version 2.0*, December 2025 (publisher document, full text) — https://www.cisa.gov/sites/default/files/2025-12/CPG_Report_2.0_508c.pdf
- CISA, CPG resource page (publication date 11 December 2025) — https://www.cisa.gov/resources-tools/resources/cpg-report
- CISA press release, *CISA Unveils Enhanced Cross-Sector Cybersecurity Performance Goals*, 11 December 2025 — https://www.cisa.gov/news-events/news/cisa-unveils-enhanced-cross-sector-cybersecurity-performance-goals
- CISA blog, *Cybersecurity Performance Goals: Sector-Specific Goals*, 26 July 2023 — https://www.cisa.gov/news-events/news/cybersecurity-performance-goals-sector-specific-goals
- CISA, Cross-Sector Cybersecurity Performance Goals programme page (CPG 2.0 key updates, SSG status, CSET Q1 2026 statement) — https://www.cisa.gov/cross-sector-cybersecurity-performance-goals
- CISA, CPG 2.0 goal catalogue — https://www.cisa.gov/cybersecurity-performance-goals-2-0-cpg-2-0
- CISA, CPG frequently asked questions (voluntary status, July 2021 NSM origin) — https://www.cisa.gov/cross-sector-cybersecurity-performance-goals/frequently-asked-questions
- CISA alert, *CISA Releases Updated Cybersecurity Performance Goals*, 21 March 2023 — https://www.cisa.gov/news-events/alerts/2023/03/21/cisa-releases-updated-cybersecurity-performance-goals
- CISA, Secure by Design programme page and Pledge page — https://www.cisa.gov/securebydesign and https://www.cisa.gov/securebydesign/pledge
- CISA, *Shifting the Balance of Cybersecurity Risk* resource page (April 2023, revised 25 October 2023) — https://www.cisa.gov/resources-tools/resources/secure-by-design
- CISA, *CISA Announces Secure by Design Commitments from Leading Technology Providers*, 8 May 2024 — https://www.cisa.gov/news-events/news/cisa-announces-secure-design-commitments-leading-technology-providers
- CISA, Secure by Design Pledge progress reports — https://www.cisa.gov/securebydesign/pledge/progress-reports
- CISA/FBI, *Product Security Bad Practices* v2, 17 January 2025 — https://www.cisa.gov/resources-tools/resources/product-security-bad-practices (PDF at https://www.cisa.gov/sites/default/files/2025-01/joint-guidance-product-security-bad-practices-508c_0.pdf)
- CISA/FBI, *Secure by Demand Guide*, 6 August 2024 — https://www.cisa.gov/resources-tools/resources/secure-demand-guide
- CISA and partners, *Secure by Demand: Priority Considerations for OT Owners and Operators*, 13 January 2025 — https://www.cisa.gov/resources-tools/resources/secure-demand-priority-considerations-operational-technology-owners-and-operators-when-selecting
- CISA, Known Exploited Vulnerabilities Catalog (1,716 entries, 19 September 2026) and the catalog's three inclusion criteria — https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA, BOD 22-01 (3 November 2021, revoked) — https://www.cisa.gov/news-events/directives/bod-22-01-reducing-significant-risk-known-exploited-vulnerabilities
- CISA, BOD 26-04 *Prioritizing Security Updates Based on Risk*, 10 June 2026 — https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- CISA, IT and Chemical Sector-Specific Goals resource pages (7 January 2025) — https://www.cisa.gov/resources-tools/resources/information-technology-it-sector-specific-goals-ssgs and https://www.cisa.gov/resources-tools/resources/chemical-sector-specific-goals-ssgs
- HHS, Healthcare and Public Health Cybersecurity Performance Goals — https://hphcyber.hhs.gov/performance-goals.html (the healthcare SSG source CISA's CPG page links to; the host was unreachable at the time of review, so nothing above rests on it)
- NARUC and US DOE CESER, *Cybersecurity Baselines for Electric Distribution Systems and DER* (the resource CISA's CPG page links to for energy) — https://www.naruc.org/core-sectors/critical-infrastructure-and-cybersecurity/cybersecurity-for-utility-regulators/cybersecurity-baselines/
- CISA and partners, *2026 Minimum Elements for a Software Bill of Materials (SBOM)*, 29 July 2026 — https://www.cisa.gov/resources-tools/resources/2026-minimum-elements-software-bill-materials-sbom

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
