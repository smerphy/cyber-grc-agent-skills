# NIST Secure Software Development Framework (NIST SP 800-218) and software supply chain attestation

## At a glance

| Attribute | Detail |
|---|---|
| Publication / citation | NIST SP 800-218, *Secure Software Development Framework (SSDF) Version 1.1* (February 2022, 36 pages). Supersedes NIST CSWP 13 (23 April 2020) |
| Publisher | NIST Information Technology Laboratory, Computer Security Division. Free of charge, not subject to US copyright |
| Status (September 2026) | v1.1 remains the current **final** version. SP 800-218r1 initial public draft (SSDF **Version 1.2**) published 17 December 2025; comment period closed 30 January 2026. EO 14306 required a final within 120 days of that preliminary update (mid-April 2026); no final v1.2 is published as of September 2026 |
| Structure | 4 practice groups (PO, PS, PW, RV) → 19 practices → 42 tasks, each with notional implementation examples and informative references |
| Who it covers | Voluntary for any software producer. Federal leverage ran through EO 14028 §4(e) and OMB M-22-18/M-23-16 — both memoranda **rescinded by OMB M-26-05 on 23 January 2026** |
| Certifiable? | No certification scheme. Evidence model = producer self-attestation (CISA common form), optional 3PAO assessment, plus retained artifacts |
| AI companion | SP 800-218A (July 2024), *Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile* |
| Federal attestation form | CISA Secure Software Development Attestation Form, Version 1.0 — OMB control #1670-0052, approved under the Paperwork Reduction Act on 8 March 2024, expires 31 March 2027. Submitted through CISA's online form or by email to the acquiring agency |
| Related but distinct | SP 800-161 (organization-level C-SCRM), CISA SBOM minimum elements (transparency artifact), EU Cyber Resilience Act (legally binding product requirements) |

## What it is

SSDF is a vocabulary of high-level secure-development **outcomes**, not an SDLC methodology and not a control catalogue. It started as NIST Cybersecurity White Paper 13 (April 2020) and was reissued as SP 800-218 v1.1 in February 2022 in response to Section 4 of Executive Order 14028, *Improving the Nation's Cybersecurity*, after a June 2021 NIST workshop that drew more than 150 position papers. Because it is model-agnostic, the same practice set can be layered onto waterfall, agile or DevOps pipelines — and used by acquirers as common language with suppliers.

Each practice is defined by four elements: the practice name and identifier; one or more **tasks**; **notional implementation examples** (explicitly non-mandatory and non-exhaustive); and **informative references** mapping the task to established practice documents. SSDF's reference set is unusually broad: BSA Framework for Secure Software, BSIMM, CNCF Software Supply Chain Best Practices, IEC 62443, ISO/IEC 27034, ISO/IEC 29147 (vulnerability disclosure), ISO/IEC 30111 (vulnerability handling), Microsoft SDL, NIST CSF, NTIA SBOM minimum elements, OWASP ASVS / MASVS / SAMM / SCVS, PCI Secure SLC, SAFECode guidance, and NIST SP 800-53, SP 800-160, SP 800-161, SP 800-181 and SP 800-216.

The publication deliberately sets no thresholds. Terms such as "sensitive data", "qualified person" and "well-secured", and the names of environments (development, build, staging, integration, test, production, distribution), are left for the adopting organization to define — SSDF states that enumerating your environments is a prerequisite to securing them and to preventing lateral movement between them.

## Who it covers / scope

SSDF itself imposes no obligations: it is guidance that non-governmental organizations may use voluntarily. Its compliance weight came from procurement.

Under the (now rescinded) M-22-18 / M-23-16 regime, software required a producer self-attestation if **any** of these applied: developed after 14 September 2022; developed earlier but changed by a **major version** change after that date; or delivered as continuous changes (SaaS, CI/CD). Excluded from attestation collection: software developed by federal agencies; open-source software obtained freely and directly by an agency; third-party open-source and proprietary **components** incorporated into an end product; and software that is freely obtained and publicly available. Attestations were collected from the producer of the software **end product** only — the end-product producer was treated as best positioned to manage component risk. These tests are now historical for federal buyers, but they remain in force inside existing contracts and are still the cleanest published scope test for private-sector supplier programs.

Private-sector adopters typically use SSDF for three jobs: structuring an internal secure-SDLC program; setting supplier expectations in software procurement; and demonstrating a recognized baseline to customers and regulators that do not name a specific standard.

## Structure and requirements

| Group | Practices | Active tasks | Emphasis |
|---|---|---|---|
| **PO** — Prepare the Organization | PO.1–PO.5 (5) | 13 | People, process, technology readiness: requirements, roles, toolchains, security-check criteria, secure development environments |
| **PS** — Protect the Software | PS.1–PS.3 (3) | 4 | Protect all forms of code from tampering; release-integrity verification; archive and protect each release |
| **PW** — Produce Well-Secured Software | PW.1, PW.2, PW.4–PW.9 (8) | 16 | Design, design review, reuse, secure coding, build configuration, code review/analysis, executable testing, secure defaults |
| **RV** — Respond to Vulnerabilities | RV.1–RV.3 (3) | 9 | Ongoing identification, risk-based remediation, root-cause analysis feeding process change |

| ID | Practice |
|---|---|
| PO.1 | Define Security Requirements for Software Development |
| PO.2 | Implement Roles and Responsibilities |
| PO.3 | Implement Supporting Toolchains |
| PO.4 | Define and Use Criteria for Software Security Checks |
| PO.5 | Implement and Maintain Secure Environments for Software Development |
| PS.1 | Protect All Forms of Code from Unauthorized Access and Tampering |
| PS.2 | Provide a Mechanism for Verifying Software Release Integrity |
| PS.3 | Archive and Protect Each Software Release |
| PW.1 | Design Software to Meet Security Requirements and Mitigate Security Risks |
| PW.2 | Review the Software Design to Verify Compliance with Security Requirements and Risk Information |
| PW.4 | Reuse Existing, Well-Secured Software When Feasible Instead of Duplicating Functionality |
| PW.5 | Create Source Code by Adhering to Secure Coding Practices |
| PW.6 | Configure the Compilation, Interpreter, and Build Processes to Improve Executable Security |
| PW.7 | Review and/or Analyze Human-Readable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements |
| PW.8 | Test Executable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements |
| PW.9 | Configure Software to Have Secure Settings by Default |
| RV.1 | Identify and Confirm Vulnerabilities on an Ongoing Basis |
| RV.2 | Assess, Prioritize, and Remediate Vulnerabilities |
| RV.3 | Analyze Vulnerabilities to Identify Their Root Causes |

**Retired identifiers.** v1.1 keeps placeholder rows rather than renumbering: PW.3 was merged into PW.4; PW.3.1 moved to PO.1.3; PW.3.2 moved to PW.4.4; PW.4.3 moved to PW.1.3; PW.4.5 moved to PW.4.1 and PW.4.4; PW.5.2 became an example under PW.5.1. Never renumber SSDF identifiers in a mapping — downstream attestation and contract references depend on them.

**SP 800-218A (July 2024)** is a *Community Profile*, not a new framework: it reuses the SSDF structure, tags each task as unchanged, "Modified from SSDF 1.1" or "Not part of SSDF 1.1", assigns a High/Medium/Low priority, and adds AI-specific recommendations, considerations and notes. New tasks include PO.5.3 (continuous monitoring of development environments), PS.1.2 (protect training, testing, fine-tuning data), PS.1.3 (protect model weights), and a repurposed PW.3 practice on confirming the integrity of training, testing, fine-tuning and aligning data, with PW.3.3 covering adversarial samples. It was written to support EO 14110 §4.1(a); **EO 14110 was revoked by EO 14148 on 20 January 2025**, but SP 800-218A remains a published NIST document and is the most usable AI-SDLC control set available.

## Assessment, certification and evidence

There is no SSDF certification. Evidence is produced in three layers:

| Layer | What it is | Notes |
|---|---|---|
| Self-attestation | CISA Secure Software Development Attestation Form, Version 1.0 (OMB PRA approval 8 March 2024) | Signed by the CEO or a designee who is an employee with authority to bind the corporation. Company-wide, single-product, or multi-product scope. Binding for future versions until the producer notifies agencies that practices no longer conform. The form warns that willfully providing false or misleading information may violate 18 U.S.C. §1001 |
| Third-party assessment | A FedRAMP-certified 3PAO, or a 3PAO approved in writing by an agency official, evaluates conformance to all elements of the form | The producer then need not sign; the assessment is attached and must not be posted publicly |
| Artifacts | Evidence generated by the SDLC itself (build logs, provenance, scan results, SBOMs) | M-22-18-era practice; retained by the producer, requested by the acquirer |

The common form attests to four practice statements, mapped in its appendix to EO 14028 §4(e) subsections and SSDF tasks:

| # | Attestation | EO 14028 | SSDF tasks |
|---|---|---|---|
| 1 | Software developed and built in secure environments: separated/protected environments; logging, monitoring and auditing of trust relationships; MFA and conditional access; documenting and minimizing undue-risk software; encrypting sensitive data such as credentials; defensive practices including continuous monitoring and incident response | 4e(i)(A)–(F) | PO.3.2, PO.3.3, PO.5.1, PO.5.2 |
| 2 | Good-faith effort to maintain trusted source code supply chains using automated tools or comparable processes for internal code and third-party components | 4e(iii) | PO.1.1, PO.3.1, PO.3.2, PO.5.1, PO.5.2, PS.1.1, PS.2.1, PS.3.1, PW.4.1, PW.4.4, PW.7.1, PW.8.1, RV.1.1 |
| 3 | Maintain provenance for internal code and third-party components to the greatest extent feasible | 4e(vi) | PO.1.3, PO.3.2, PO.5.1, PO.5.2, PS.3.1, PS.3.2, PW.4.1, PW.4.4, RV.1.1, RV.1.2 |
| 4 | Automated vulnerability checking run on an ongoing basis and before each product, version or update release; a policy or process to address discovered vulnerabilities before release; and an operating vulnerability disclosure program that addresses reports within its stated timelines | 4e(iv) | PO.4.1, PO.4.2, PS.1.1, PW.2.1, PW.4.4, PW.5.1, PW.6.1, PW.6.2, PW.7.1, PW.7.2, PW.8.2, PW.9.1, PW.9.2, RV.1.1–RV.1.3, RV.2.1, RV.2.2, RV.3.3 |

Where a producer cannot attest, the historical alternative was a POA&M submitted to the agency, with the agency required to request an extension or waiver from OMB; an invalid POA&M or a missing extension request obliged the agency to discontinue use. The published burden estimate for the form is 3 hours 20 minutes per response — a useful reality check on how much assurance a signature actually buys.

## Timeline and status

| Date | Event |
|---|---|
| 23 April 2020 | NIST CSWP 13 publishes the original SSDF |
| 12 May 2021 | EO 14028 §4(e) directs NIST guidance on secure software development |
| February 2022 | SP 800-218 v1.1 published (19 practices, 42 tasks) |
| 14 September 2022 | OMB M-22-18 requires agencies to obtain producer self-attestation against SSDF-derived practices |
| 9 June 2023 | OMB M-23-16 extends deadlines: critical software 3 months, all covered software 6 months after PRA approval of CISA's common form |
| 8 March 2024 | OMB approves CISA's Secure Software Development Attestation Common Form under the PRA (control #1670-0052, expires 31 March 2027); CISA publishes Version 1.0 that month |
| July 2024 | SP 800-218A finalized (generative AI and dual-use foundation models Community Profile) |
| 16 January 2025 | EO 14144 adds FAR-amendment, machine-readable attestation and CISA validation directives |
| 20 January 2025 | EO 14148 revokes EO 14110 (30 October 2023), the authority behind SP 800-218A |
| 6 June 2025 (FR 11 June 2025) | **EO 14306** strikes EO 14144 §2(a)–(b) — the FAR amendment and CISA attestation-validation program — and re-tasks NIST: NCCoE consortium by 1 Aug 2025, SP 800-53 patch-deployment guidance by 2 Sep 2025, preliminary SSDF update by 1 Dec 2025, final version within 120 days of that preliminary publication |
| 17 December 2025 | SP 800-218r1 ipd (SSDF v1.2) published; comments closed 30 January 2026 |
| 23 January 2026 | **OMB M-26-05** rescinds M-22-18 and M-23-16, faulting M-22-18 for "unproven and burdensome software accounting processes"; agencies move to risk-based, agency-tailored software and hardware assurance |
| 24 March 2026 | NCCoE publishes a live draft, *Secure Software Development, Security, and Operations (DevSecOps) Practices*, demonstrating SSDF implementation; comments closed 24 April 2026 |
| 16 April 2026 | EO 14306's 120-day deadline for a **final** updated SSDF passes with no final published |
| 29 July 2026 | CISA, NSA, FBI and international partners publish **2026 Minimum Elements for an SBOM**, replacing the 2021 NTIA minimum elements |
| 11 September 2026 | EU Cyber Resilience Act vulnerability and incident **reporting** obligations become applicable |

**SSDF v1.2 (draft) changes.** Two new practices: **PO.6** (Define and Implement a Continuous Process Improvement Plan, tasks PO.6.1–PO.6.3) and **PS.4** (Ensure Software Updates Are Robust and Reliable, tasks PS.4.1–PS.4.4). RV.1.2 and RV.3.3 wording updated; examples added or reworded across PO.1, PO.2, PW.1, PW.4, PW.5, PW.8, PW.9, RV.1 and RV.2; SP 800-53 and SP 800-161 references refreshed throughout the table; the EO 14028 reference and the v1.1 Appendix A EO 14028 mapping removed. The draft totals 21 practices and 49 active tasks. Treat the numbering as provisional until the final is published.

**What M-26-05 leaves standing.** Agencies must still maintain a complete software and hardware inventory and develop assurance policies matched to their risk determinations. Agencies **may** still use the attestation form, **may** require an SBOM on request (for cloud platforms, an SBOM of the runtime production environment), and are pointed to SP 800-218 and its appendices, CISA's SBOM minimum elements (the memorandum cites the August 2025 draft, since finalized as the 2026 edition), and CISA's HBOM framework (September 2023). Existing contract clauses citing M-22-18 do not self-rescind — check them individually.

**2026 SBOM minimum elements.** New elements include SBOM Author Signature, SBOM Data Format Name/Version, SBOM Generation Context, SBOM Tool Name/Version, SBOM Version, Component Hash Value, Component Hash Algorithm and Component License. Major updates cover SBOM Author, Component Identifiers, Component Producer, Component Version, Accommodation of Updates, Coverage, Explicitly Identifying Unknown Information and Machine-Processable Data; the 2021 Access Controls element is removed and folded into Distribution and Delivery. A separate *SBOM for AI – Minimum Elements* was issued by CISA and G7 partners in May 2026.

## Key obligations for security/GRC teams

1. **Fix the baseline version in writing.** Assess against SP 800-218 v1.1 (19 practices / 42 tasks) and track v1.2 as a watch item; do not mix draft and final identifiers in one assessment. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).
2. **Map SSDF tasks to existing controls** rather than standing up a parallel program — SSDF's own informative references already point at SP 800-53, CSF, ISO 27034/29147/30111 and OWASP. See [control-mapping](../../skills/control-mapping/SKILL.md), [nist-800-53.md](nist-800-53.md), [nist-csf-2.md](nist-csf-2.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
3. **Enumerate and segregate build environments (PO.5).** Development, build, test and distribution environments, MFA and conditional access, credential encryption, and logged/audited trust relationships are the single largest attestation exposure.
4. **Stand up provenance and SBOM generation (PS.3, PW.4, RV.1).** Align output to the 2026 CISA minimum elements, not the 2021 NTIA list, and decide now who signs the SBOM.
5. **Operate a vulnerability disclosure program with published timelines (RV.1–RV.3)** and feed root-cause analysis back into PO.1 requirements. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
6. **Re-read your federal contracts.** M-26-05 rescinded the mandate, not the clauses. Inventory every contract citing M-22-18, M-23-16 or the attestation form and decide whether to keep, renegotiate or retire the commitment. Track divergences as formal exceptions ([exception-management](../../skills/exception-management/SKILL.md)).
7. **Do not let self-attestation substitute for diligence in your own supplier program.** Ask for the attestation *and* the artifacts behind statements 2–4. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
8. **For AI model development, apply SP 800-218A** as the SDLC layer beneath your AI governance program — data and model-weight protection (PS.1.2, PS.1.3) have no equivalent in v1.1. See [ai-governance](../../skills/ai-governance/SKILL.md), and pair it with the NIST AI Risk Management Framework at the governance layer.
9. **Evidence the practices as controls you can test**: build-pipeline access reviews, signed-artifact verification, dependency-scan coverage, release-gate exceptions. See [control-testing](../../skills/control-testing/SKILL.md).
10. **Keep a horizon item open** on SSDF v1.2 finalization and on any successor federal acquisition language. See [regulatory-horizon-scanning](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

- **EU Cyber Resilience Act.** The CRA makes much of SSDF's PS/PW/RV content legally binding for products with digital elements sold in the EU — Annex I essential requirements plus vulnerability-handling duties, an SBOM covering at least top-level dependencies, and hard clocks: 24-hour early-warning notification of an actively exploited vulnerability, a 72-hour vulnerability notification, and a final report. Reporting obligations apply from 11 September 2026; the bulk of the Regulation from 11 December 2027. SSDF conformance is a strong head start but is **not** CRA conformity. See [../regulations/eu-cyber-resilience-act.md](../regulations/eu-cyber-resilience-act.md).
- **NIST SP 800-161 (C-SCRM).** SSDF is producer-side and product-scoped; 800-161 is acquirer-side and organization-scoped. Most SSDF tasks carry 800-161 informative references, so run them together rather than sequentially. See [nist-800-161-cscrm.md](nist-800-161-cscrm.md).
- **NIST CSF 2.0 and SP 800-53.** SSDF v1.1 carries per-task references to SP 800-53 (chiefly the SA and SR families) and to CSF **1.1** subcategory identifiers (ID.GV-3, ID.SC-1/-3, PR.AC-4, PR.DS-6, PR.IP-1/-3, DE.CM and others) — re-express them against CSF 2.0 before use. Use CSF for program framing and SSDF for the SDLC layer beneath it. See [nist-csf-2.md](nist-csf-2.md) and [nist-800-53.md](nist-800-53.md).
- **CIS Controls v8.1.** Control 16 (Application Software Security) is the closest CIS analogue and is a reasonable IG2 entry point for teams not ready for full SSDF coverage. See [cis-controls-v8.md](cis-controls-v8.md).
- **PCI DSS v4.x and the PCI Software Security Framework.** PCI Secure SLC is a named SSDF informative reference, cited at task level throughout the v1.1 table; PCI DSS's secure-development and vulnerability-management requirements cover overlapping ground for cardholder-data environments. See [pci-dss-4.md](pci-dss-4.md).
- **SOC 2 and ISO/IEC 27001.** Neither certifies secure development specifically, but SSDF evidence supports SOC 2 change-management criteria and ISO 27001 Annex A application-security and secure-development controls. See [soc2-tsc.md](soc2-tsc.md) and [iso-27001-2022.md](iso-27001-2022.md).
- **SLSA, OWASP SAMM and BSIMM** are complementary measurement models rather than competitors: SLSA grades build-pipeline integrity (PS.2/PW.6 territory), SAMM and BSIMM measure program maturity. SAMM and BSIMM are named informative references in SSDF v1.1; SLSA appears in neither SSDF v1.1 nor the v1.2 draft.

## Primary sources

- NIST SP 800-218 v1.1 (full text, PDF): https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf
- NIST CSRC publication record for SP 800-218 (February 2022; supersedes CSWP 13, 23 April 2020): https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SSDF project publications list (current status of every SSDF document): https://csrc.nist.gov/Projects/ssdf/publications
- NIST SP 800-218r1 ipd, SSDF v1.2 draft (full text, PDF): https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218r1.ipd.pdf
- NIST CSRC draft record for SP 800-218 Rev. 1 (published 17 December 2025, comments closed 30 January 2026): https://csrc.nist.gov/pubs/sp/800/218/r1/ipd
- NIST SP 800-218A, generative AI and dual-use foundation model Community Profile (full text, PDF): https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf
- NIST SSDF project news feed: https://csrc.nist.gov/projects/ssdf/news
- NCCoE DevSecOps Practices live draft record (24 March 2026): https://csrc.nist.gov/pubs/other/2026/03/24/devsecops-practices/iprd
- Executive Order 14306 (signed 6 June 2025), 90 FR 24723 (legal text, govinfo): https://www.govinfo.gov/content/pkg/FR-2025-06-11/html/2025-10804.htm
- Executive Order 14144 (signed 16 January 2025), 90 FR 6755 (legal text, govinfo): https://www.govinfo.gov/content/pkg/FR-2025-01-17/html/2025-01470.htm
- Executive Order 14148 (20 January 2025), revoking EO 14110, 90 FR 8237 (legal text, govinfo): https://www.govinfo.gov/content/pkg/FR-2025-01-28/html/2025-01901.htm
- OMB M-26-05, *Adopting a Risk-based Approach to Software and Hardware Security* (23 January 2026): https://www.whitehouse.gov/wp-content/uploads/2026/01/M-26-05-Adopting-a-Risk-based-Approach-to-Software-and-Hardware-Security.pdf
- OMB M-22-18 (14 September 2022): https://bidenwhitehouse.archives.gov/wp-content/uploads/2022/09/M-22-18.pdf
- OMB M-23-16, update to M-22-18 (9 June 2023): https://bidenwhitehouse.archives.gov/wp-content/uploads/2023/06/M-23-16-Update-to-M-22-18-Enhancing-Software-Security.pdf
- CISA Secure Software Development Attestation Form and instructions (PDF): https://www.cisa.gov/sites/default/files/2024-04/Self_Attestation_Common_Form_FINAL_508c.pdf — cisa.gov returns 403 to scripted access; the form text above was read from an identical copy of the same PDF
- OMB Paperwork Reduction Act history for control #1670-0052, the attestation common form (approval concluded 8 March 2024): https://www.reginfo.gov/public/do/PRAOMBHistory?ombControlNumber=1670-0052
- CISA and partners, *2026 Minimum Elements for a Software Bill of Materials (SBOM)* (29 July 2026, PDF): https://www.cisa.gov/sites/default/files/2026-07/2026_cisa_sbom_minimum_elements_508c.pdf
- CISA resource page for the 2026 SBOM minimum elements: https://www.cisa.gov/resources-tools/resources/2026-minimum-elements-software-bill-materials-sbom
- Regulation (EU) 2024/2847 (Cyber Resilience Act) — Art. 14 clocks, Annex I Part II(1) SBOM duty, Art. 71 application dates (legal text, EUR-Lex): https://eur-lex.europa.eu/eli/reg/2024/2847/oj

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
