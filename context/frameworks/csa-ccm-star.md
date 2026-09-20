# Cloud Security Alliance — Cloud Controls Matrix (CCM), CAIQ, STAR and the AI Controls Matrix (AICM)

## At a glance

| Attribute | Detail |
|---|---|
| Publisher | Cloud Security Alliance (CSA) — member-driven, consensus research organization; CCM is maintained by the CCM Working Group |
| Current cloud framework | **CCM v4.1**, released 27 January 2026, succeeding v4.0.13 — **207 controls across 17 domains** (11 controls added, one Identity and Access Management control removed). Predecessors: v4.0, 21 January 2021, 197 controls / 17 domains; v3.0.1, 133 controls / 16 domains |
| Companion questionnaire | **CAIQ v4.1 — 283 yes/no questions** with justification fields; one control commonly maps to several questions. Lite variants: CCM-Lite 96 controls (a subset of the 207), CAIQ-Lite 138 questions across the 17 domains |
| AI framework | **AICM v1.1 — 247 control objectives across 18 domains**, including a Model Security (MDS) domain of 13 AI-specific controls (v1.0, 9 July 2025: 243 controls); companion **AI-CAIQ v1.1 — 320 questions** |
| Assurance program | **STAR** (Security, Trust, Assurance and Risk): public, free-to-search STAR Registry, which CSA describes as carrying over 3,400 assessments; **Level 1** self-assessment and **Level 2** third-party audit. CSA's current levels page presents only Levels 1 and 2 — there is no live "Level 3 / STAR Continuous" tier |
| Certifiable? | Not on its own. STAR Level 2 rides on **ISO/IEC 27001** (STAR Certification) or a **SOC 2** engagement (STAR Attestation); C-STAR rides on Chinese national standards |
| Cost | CCM, CAIQ, guidelines and mappings are free downloads; STAR Level 1 self-assessment is complimentary; Valid-AI-ted scoring is USD 595 (free for CSA corporate members); Level 2 is priced by the audit firm |
| Typical use | Cloud provider due diligence, CSP-side transparency, cloud control baseline layered on ISO 27001/SOC 2, and (via AICM) AI-vendor assurance |
| Relationship to neighbours | CCM is a *cloud-specific control set plus a shared-responsibility model*; it is normally mapped onto, not substituted for, ISO/IEC 27001, SOC 2 TSC, NIST 800-53 or PCI DSS |

## What it is

The Cloud Controls Matrix is CSA's cloud-specific control framework: a spreadsheet-native catalogue of control specifications organized by domain, each carrying a control ID, a control specification, shared-responsibility metadata, implementation and auditing guidance, and pre-built mappings to mainstream standards (currently the v4.0.13 mapping set). It exists because generic control catalogues do not answer the question cloud buyers actually have — *which party implements this control, and how do I get evidence for it from someone else's infrastructure*.

The CCM is paired with the **Consensus Assessments Initiative Questionnaire (CAIQ)**, which turns the control set into a supplier questionnaire, and with the **STAR** program, which publishes the answers (Level 1) or third-party audit outcomes (Level 2) in a free public registry. That registry is the practical payoff: for most major cloud and SaaS providers, a STAR entry is available without an NDA, which shortens vendor due diligence considerably.

Since July 2025 CSA has extended the same pattern to AI. The **AI Controls Matrix (AICM)** reuses the CCM's structure and mapping methodology for cloud-hosted AI systems, and **STAR for AI** (launched 23 October 2025) provides the registry and assurance path, with Level 2 built on ISO/IEC 42001 certification.

## Who it covers / Scope

- **Not a law and not binding.** CCM/CAIQ/STAR apply where a contract, a customer questionnaire, a procurement policy, or an internal standard calls for them. There is no regulator and no penalty regime.
- **Two audiences, by design.** The CCM distinguishes the **Cloud Service Provider (CSP)** and the **Cloud Service Customer (CSC)**. Every control carries a Shared Security Responsibility Model (SSRM) designation: **CSP-owned**, **CSC-owned**, **shared (CSP and CSC independently responsible)**, or **shared (dependent)**, plus a *typical control applicability and ownership* view across IaaS / PaaS / SaaS.
- **Service-model sensitivity is the point.** The same control ID lands on the provider in SaaS and on the customer in IaaS. Assessments that ignore the SSRM column produce findings against the wrong party.
- **Size.** CCM-Lite / CAIQ-Lite exist specifically so that SMEs and startups can answer a defensible subset rather than abandon a 283-question workbook.
- **AICM scope.** AICM assigns controls across five roles: Model Provider (MP), Orchestrated Service Provider (OSP), Application Provider (AP), AI Customer (AIC) and Cloud Service Provider (CSP) — useful when a single AI feature involves four organizations.

## Structure and requirements

### The 17 CCM domains

| ID | Domain | ID | Domain |
|---|---|---|---|
| A&A | Audit and Assurance | IAM | Identity and Access Management |
| AIS | Application and Interface Security | IPY | Interoperability and Portability |
| BCR | Business Continuity Management and Operational Resilience | IVS | Infrastructure and Virtualization Security |
| CCC | Change Control and Configuration Management | LOG | Logging and Monitoring |
| CEK | Cryptography, Encryption and Key Management | SEF | Security Incident Management, E-Discovery and Cloud Forensics |
| DCS | Datacenter Security | STA | Supply Chain Management, Transparency and Accountability |
| DSP | Data Security and Privacy Lifecycle Management | TVM | Threat and Vulnerability Management |
| GRC | Governance, Risk Management and Compliance | UEM | Universal Endpoint Management |
| HRS | Human Resources | | |

LOG was introduced in v4.0; GRC, A&A, UEM and CEK were restructured in the same release. Domain sizes are uneven: in v4.1, CEK carries 21 controls, DSP 19 and DCS 18, against 4 for IPY and 6 for A&A — read the per-domain counts off the workbook rather than assuming an even split.

### What ships in the CCM v4.1 bundle

| Component | What it gives you |
|---|---|
| CCM v4.1 workbook | 207 control specifications with IDs and control text, a *CCM Lite* flag, typical ownership and applicability by IaaS / PaaS / SaaS, architectural and organizational relevance columns, plus implementation-guidelines, auditing-guidelines, mappings, CAIQ and change-log tabs |
| CAIQ v4.1 (STAR Level 1 Security Questionnaire) | 283 questions — the *submittable* form; the combined CCM+CAIQ workbook is reference-only and is rejected by the registry |
| Implementation Guidelines | Vendor-agnostic, explicitly non-exhaustive and non-prescriptive; includes the SSRM rationale per control |
| Auditing Guidelines | Assessment steps for each control, to be tailored to the audit objective |
| Introductory Guidance to CCM | Structure, SSRM model and how to read the columns |
| Code of Practice for Key Metrics + Continuous Audit Metrics Catalog v1.1 | Metric definitions for continuous control monitoring |
| CAIQ v4.0.3 → v4.1 change analysis | Delta document for re-answering an existing questionnaire |
| Machine-readable bundle | Controls, CAIQ, implementation guidelines and mappings in JSON/YAML and **OSCAL** — the hook for compliance automation. It is a separate download, and its artifact page still shows a June 2024 release date, so check the version before wiring it in |

### v4.1 changes (January 2026)

- **11 new control specifications**, added in Datacenter Security (DCS), Logging and Monitoring (LOG), Security Incident Management (SEF), Supply Chain Management (STA) and Threat and Vulnerability Management (TVM); **one Identity and Access Management (IAM) control was removed** — net 197 to 207.
- Minor and major revisions to existing control objectives for depth, coverage and alignment with evolving standards; no change to the 17-domain structure.
- Implementation Guidelines, Auditing Guidelines, CCM-Lite and CAIQ-Lite reissued against v4.1.

### Mappings

CSA builds its mappings into the workbook's *Scope Applicability (Mappings)* tab. Each mapped control carries a gap rating — **no gap / partial gap / full gap** — and an addendum column proposing a compensating control where a gap exists; a mapping is a coverage aid, never an equivalence claim, and the gap rating is a discipline worth copying into your own crosswalks. Across the v4.0.x maintenance releases CSA mapped CCM v4 to CCM v3.0.1, ISO/IEC 27001:2013 and 27002, ISO/IEC 27017:2015, ISO/IEC 27018:2019, AICPA TSC 2017, CIS Controls v8.0, PCI DSS v3.2.1 and v4.0, NIST SP 800-53 Rev. 5, ISO/IEC 27001:2022 and 27002:2022, ISF SOGP 2022, NIST CSF v1.1 and v2.0, and ENX ISA v6.0. **None of these had been re-cut against v4.1 as of September 2026**: the mappings tab of the v4.1 workbook reads "This dataset is not available yet", and CSA said in February 2026 that the v4.0.13 mappings were still being realigned. Separately published artifacts map CCM v4 to FedRAMP and provide a NIST CSF v2.0 cloud community profile based on CCM v4. No official CCM-to-DORA mapping was found on CSA's site as of September 2026.

## Assessment, certification and evidence

| Tier | What it is | Underlying standard | Validity |
|---|---|---|---|
| Level 1 — Self-Assessment | Complimentary CAIQ submission published on the STAR Registry | CCM / CAIQ | Updated annually |
| Level 1 — Valid-AI-ted | Optional automated scoring of a CAIQ v4 submission, with a registry badge; up to 10 scoring attempts | CCM / CAIQ | USD 595; free for CSA corporate members |
| Level 2 — STAR Attestation | SOC 2 engagement performed against AICPA Trust Services criteria **plus** the CCM, by a CPA firm | SOC 2 | Listing expires after one year unless updated |
| Level 2 — STAR Certification | Third-party certification against ISO/IEC 27001 **plus** the CCM, by an approved certification body | ISO/IEC 27001 | Certificates follow normal ISO/IEC 27001 protocol and expire after three years unless updated |
| Level 2 — C-STAR | Greater China variant: GB/T 22080-2008 plus the CCM and 29 related controls drawn from GB/T 22239-2008 and GB/Z 28828-2012 | Chinese national standards | Three years unless updated |

Evidence notes for practitioners:

- **A Level 1 entry is a self-assertion.** Treat it as scoped, dated vendor testimony — useful for triage and for pre-populating a questionnaire, not as assurance. Valid-AI-ted adds consistency scoring, not independent testing.
- **A Level 2 listing does not replace the underlying report.** Still obtain and read the ISO/IEC 27001 certificate plus Statement of Applicability, or the SOC 2 report with its exceptions and complementary user-entity controls.
- **Check freshness and scope** on every registry entry: CAIQ version answered, submission date, and which services the entry covers.

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| 21 Jan 2021 | CCM v4.0 published — new LOG domain, 197 controls (up from 133), 17 domains |
| Dec 2021 | CCM v4 Auditing Guidelines published (maintenance release v4.0.4) |
| 2021–2024 | v4.0.x maintenance releases through v4.0.13 (Nov 2024); mapping set extended (AICPA TSC 2017, CIS v8.0, PCI DSS v3.2.1 and v4.0, NIST SP 800-53 Rev. 5, ISO/IEC 27001 and 27002:2022, ISF SOGP 2022, NIST CSF v1.1 and v2.0, ENX ISA v6.0) |
| 9 Jul 2025 | AICM v1.0 released — 243 control objectives, 18 domains including the new Model Security (MDS) domain (page updated 30 Oct 2025) |
| 23 Oct 2025 | STAR for AI launched: Level 1 (AI-CAIQ self-assessment) available |
| 20 Nov 2025 | STAR for AI Level 2 available — third-party ISO/IEC 42001 certification plus a Valid-AI-ted AI-CAIQ |
| 27 Jan 2026 | **CCM v4.1 and CAIQ v4.1 released**, with CCM-Lite / CAIQ-Lite refresh (CSA's transition blog dates the release to 28 January) |
| 13 Feb 2026 | Introductory Guidance to CCM reissued for v4.1 |
| Mar 2026 | STAR Registry begins accepting both v4.0 and v4.1 submissions for Levels 1 and 2 |
| 22 Jun 2026 | AICM v1.1 — 247 control objectives, 18 domains, AI-CAIQ 320 questions, mappings to BSI AIC4, ISO/IEC 42001:2023, AIUC-1, EU AI Act and NIST AI RMF / AI 600-1 |
| 30 Jun 2026 | AIUC-1 AI-agent trustmark can be added to an existing STAR Registry listing (AIUC-1 certification uses quarterly red-teaming and annual review of operational, legal and technical controls) |
| **Dec 2027** | Last date for STAR Level 1 and Level 2 submissions based on v4.0.x; thereafter v4.1 only |
| **Jan 2028** | CCM v4.0.x and CAIQ v4.0.x withdrawn |

CSA has stated that the CCSK curriculum and exam are unaffected by the v4.1 change for now. The open item as of September 2026 is the mapping portfolio: the v4.1 workbook still ships an empty mappings tab, so cross-framework work has to run off the v4.0.13 mapping set until CSA republishes it.

## Key obligations for security/GRC teams

1. **Decide which side of the SSRM you are on per service** before assessing anything; record CSP-owned vs CSC-owned vs shared for each in-scope control. See [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).
2. **Use the STAR Registry as the first step of vendor due diligence.** Pull the existing Level 1/Level 2 entry before sending your own questionnaire — see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
3. **Replace bespoke cloud questionnaires with CAIQ v4.1 or CAIQ-Lite** so answers are comparable across vendors and reusable by the vendor; align your own [vendor security questionnaire](../../templates/vendor-security-questionnaire.md) to CCM domain IDs.
4. **If you are the provider**, plan the v4.1 re-answer now: the change analysis document exists, and the v4.0.x window closes December 2027. Late migration risks a stale registry entry during a customer's procurement cycle.
5. **Layer CCM onto an existing certification rather than running it standalone** — Level 2 exists precisely because ISO/IEC 27001 or SOC 2 is the audit vehicle. See [../../skills/iso27001-readiness/SKILL.md](../../skills/iso27001-readiness/SKILL.md) and [../../skills/soc2-readiness/SKILL.md](../../skills/soc2-readiness/SKILL.md).
6. **Use the mappings for gap analysis, not for equivalence claims** — and note that the published set is still the v4.0.13 one. Carry CSA's own gap ratings into your crosswalk — [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).
7. **Exploit the OSCAL/JSON bundle** if you run a GRC platform: CCM is one of the few free control catalogues shipped machine-readable, which makes continuous control monitoring cheap to wire up. Pair with the Continuous Audit Metrics Catalog and [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).
8. **For AI vendors, ask for an AICM/AI-CAIQ answer and check the role assignment** (model provider vs orchestrator vs application provider) — otherwise controls land on whoever is easiest to ask. See [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).
9. **Where a CCM control cannot be satisfied because the provider owns it**, record it as an inherited control with the provider's evidence reference, or raise an exception — [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).

## Interplay

- **ISO/IEC 27001:2022** — the audit vehicle for STAR Certification. CCM adds cloud specificity that Annex A leaves generic; the Statement of Applicability remains the ISO artefact. See [iso-27001-2022.md](iso-27001-2022.md). ISO/IEC 27017 (cloud security) and 27018 (cloud PII) overlap heavily with CCM's DCS, IVS and DSP domains and are mapped by CSA.
- **SOC 2** — the audit vehicle for STAR Attestation; CCM controls are tested alongside the Trust Services criteria in one engagement. See [soc2-tsc.md](soc2-tsc.md).
- **NIST CSF 2.0 / SP 800-53 Rev. 5 / CIS Controls v8 / PCI DSS v4** — all officially mapped at v4.0.13; use CCM when the question is cloud shared responsibility and the others when the question is enterprise-wide control coverage. See [nist-csf-2.md](nist-csf-2.md), [nist-800-53.md](nist-800-53.md), [cis-controls-v8.md](cis-controls-v8.md), [pci-dss-4.md](pci-dss-4.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).
- **DORA** — no official CSA mapping from CCM to DORA was published as of September 2026. A provider's STAR entry helps evidence ICT third-party controls but does not discharge DORA's register-of-information, contractual-clause or incident-reporting duties; map through ISO/IEC 27001. See [../regulations/dora.md](../regulations/dora.md).
- **EU AI Act and AI management systems** — AICM maps to the EU AI Act and to ISO/IEC 42001, and STAR for AI Level 2 is built on an ISO/IEC 42001 certificate. AICM is a control catalogue, not a conformity-assessment route under the Act. See [../regulations/eu-ai-act.md](../regulations/eu-ai-act.md).
- **NIS2** — no official CCM→NIS2 mapping was found as of September 2026; map through ISO/IEC 27001 instead. See [../regulations/nis2.md](../regulations/nis2.md).

## Primary sources

- CSA, *Cloud Controls Matrix* research page — https://cloudsecurityalliance.org/research/cloud-controls-matrix (publisher page)
- CSA, *Cloud Controls Matrix and CAIQ v4.1* artifact page — https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4-1 (publisher page)
- CSA blog, *The CSA Cloud Controls Matrix v4.1: Strengthening the Future of Cloud Security*, 2 Dec 2025 — https://cloudsecurityalliance.org/blog/2025/12/02/the-csa-cloud-controls-matrix-v4-1-strengthening-the-future-of-cloud-security (publisher guidance)
- CSA blog, *CCM v4.1 Transition Timeline*, 19 Feb 2026 — https://cloudsecurityalliance.org/blog/2026/02/19/ccm-v4-1-transition-timeline (publisher guidance)
- CSA, *Introductory Guidance to Cloud Controls Matrix (CCM)* — https://cloudsecurityalliance.org/artifacts/introductory-guidance-to-ccm (publisher document page)
- CSA press release, *CCM v4 adds new Log and Monitoring domain*, 21 Jan 2021 — https://cloudsecurityalliance.org/press-releases/2021/01/21/cloud-security-alliance-s-new-cloud-controls-matrix-v4-adds-new-log-and-monitoring-domain-and-more-than-60-new-cloud-security-controls (publisher)
- CSA, *A Checklist for CSA's Cloud Controls Matrix v4* — https://cloudsecurityalliance.org/articles/a-checklist-for-csa-s-cloud-controls-matrix-v4/ (publisher article, used for the domain list)
- CSA, *CCM-Lite and CAIQ-Lite* — https://cloudsecurityalliance.org/artifacts/ccm-lite-and-caiq-lite-v4 (publisher page)
- CSA, *Cloud Controls Matrix and CAIQ v4.0* (the v4.0.13 bundle) — https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4 (publisher page)
- CSA, *CCM Machine Readable Bundle (JSON/YAML/OSCAL)* — https://cloudsecurityalliance.org/artifacts/ccm-machine-readable-bundle-json-yaml-oscal (publisher page)
- CSA, *STAR levels* — https://cloudsecurityalliance.org/star/levels (program terms, fees, validity)
- CSA, *STAR Registry* — https://cloudsecurityalliance.org/star/registry (publisher page)
- CSA, *STAR for AI* — https://cloudsecurityalliance.org/star/ai (publisher page)
- CSA press release, *CSA launches STAR for AI*, 23 Oct 2025 — https://cloudsecurityalliance.org/press-releases/2025/10/23/cloud-security-alliance-launches-star-for-ai-establishing-the-global-framework-for-responsible-and-auditable-artificial-intelligence (publisher)
- CSA, *AI Controls Matrix* v1 and v1.1 artifact pages — https://cloudsecurityalliance.org/artifacts/ai-controls-matrix and https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1 (publisher pages)
- CSA blog, *AI Controls Matrix v1.1*, 14 Jul 2026 — https://cloudsecurityalliance.org/blog/2026/07/14/ai-controls-matrix-v1-1-strengthening-the-foundation-for-trustworthy-ai (publisher)
- CSA press release, *AIUC-1 certification added to the STAR Registry*, 30 Jun 2026 — https://cloudsecurityalliance.org/press-releases/2026/06/30/csa-extends-leadership-into-agentic-ai-with-addition-of-aiuc-1-certification-to-star-registry (publisher)

The CCM v4.1 and CAIQ v4.1 workbooks were downloaded from the artifact page above and used to verify the 207 control IDs, the 283 CAIQ questions, the ownership and applicability columns, the mapping history in the change log and the empty v4.1 mappings tab. The AICM workbook and the individual mapping spreadsheets were not opened; exact control text should be read from the download before quoting.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
