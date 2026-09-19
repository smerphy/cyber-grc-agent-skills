# NIST Privacy Framework (PF 1.0, with the PF 1.1 update in draft)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument / citation | *NIST Privacy Framework: A Tool for Improving Privacy through Enterprise Risk Management, Version 1.0* — NIST Cybersecurity White Paper (CSWP) 10, 16 January 2020. Update: *NIST Privacy Framework 1.1*, CSWP 40 Initial Public Draft (IPD), 14 April 2025 |
| Publisher | US National Institute of Standards and Technology (NIST), Information Technology Laboratory / Applied Cybersecurity Division |
| Legal status | Voluntary. The document states it "does not have the force and effect of law" and is not meant to bind the public. No US federal or state law mandates it by name in any source fetched for this pack |
| Current version | 1.0 remains the only final version. 1.1 IPD public comment closed 13 June 2025; NIST's project page (updated 1 April 2026) lists the final 1.1 as "coming soon"; the CSRC publication list still shows only the IPD (checked September 2026) |
| Who it is for | Any organization, any size, sector, technology, law or jurisdiction; any role in the data processing ecosystem (controller/processor-type roles included) |
| Structure | Three components: **Core** (Functions → Categories → Subcategories), **Profiles** (Current / Target; 1.1 adds Organizational and Community Profiles), **Implementation Tiers** (1–4). PF 1.0 Core: 5 Functions, 18 Categories, 100 Subcategories. PF 1.1 IPD Core: 5 Functions, 20 Categories, ~102 active Subcategories (with numbering gaps) |
| Certifiable? | No. No NIST certification, accreditation or conformance scheme; use is self-assessed via Profiles and Tiers |
| Penalties | None — not a legal instrument. Relevance to enforcement is indirect (evidence of a reasonable privacy program; crosswalks to laws) |
| Relationship to neighbours | Modeled on and designed to be used with the NIST Cybersecurity Framework (CSF); 1.1 realigns to CSF 2.0. Points to SP 800-53 for privacy controls, NIST IR 8062 / PRAM for privacy engineering and risk assessment, and (in 1.1) the AI RMF 1.0 for AI risk |

## What it is

The Privacy Framework (PF) is NIST's voluntary, outcome-based tool for managing privacy risk as an enterprise risk, developed through an open stakeholder process launched by the Department of Commerce in September 2018 and published as Version 1.0 on 16 January 2020. It deliberately mirrors the CSF so that cybersecurity and privacy programs can share one vocabulary and one Profile/Tier mechanism, and it is "agnostic to any particular technology, sector, law, or jurisdiction": it describes *what* privacy outcomes an organization should achieve, not *how* or *which law* requires them. Laws, standards and control catalogs are attached through crosswalks ("informative references") rather than baked in.

Its core conceptual move is to separate **privacy risk** from cybersecurity risk. Cybersecurity risk arises from loss of confidentiality, integrity or availability; privacy risk arises from **data processing itself** — any "data action" (collection, retention, logging, generation, transformation, use, disclosure, sharing, transmission, disposal) that could create a problem for individuals, from dignity harms (embarrassment, stigma) to discrimination, economic loss or physical harm. The two overlap in "cybersecurity-related privacy events" (breaches), which is where the PF's Protect-P Function and the CSF's Detect/Respond/Recover Functions meet. Privacy risk is defined as the likelihood that individuals will experience problems resulting from data processing, and the impact should they occur.

The **1.1 update** (IPD, April 2025) is described by NIST as a "modest" revision: targeted restructuring of the Core to track CSF 2.0 (notably a much larger Govern-P Function), a new Section 1.2.2 on artificial intelligence and privacy risk management, and relocation of most "how to use" guidance from the PDF to the NIST website. It does not change the three-component architecture or the Tier definitions' names.

## Who it covers / Scope

- **No applicability test.** Adoption is a choice. The PF applies to whatever an organization scopes into its Profile: an enterprise, a business unit, a product line or a single system/service.
- **Any ecosystem role.** The Core is not assigned by role; an organization uses Profiles to pick the Functions, Categories and Subcategories relevant to its role(s) (which may be legally codified, e.g., controller vs processor, or derived from industry designations). Multiple Profiles may be built for different roles, systems, products, services or categories of individuals.
- **Digital and non-digital data.** Privacy events are considered across the full data life cycle from collection to disposal, "whether in digital or non-digital form".
- **Federal use.** The PF cross-references SP 800-37 Rev. 2 (RMF "Prepare" step) and SP 800-53 (Rev. 4 in PF 1.0, Rev. 5 in the 1.1 IPD), so US federal agencies and their contractors typically use it as the program layer above the mandatory 800-53 privacy controls. See [nist-800-53.md](nist-800-53.md).
- **Not a compliance instrument.** NIST's crosswalk page states explicitly that implementing the mapped PF outcomes does not mean the provisions of the source law or standard have been met.

## Structure and requirements

### The Core

Functions are labelled with a "-P" suffix to distinguish them from CSF Functions. Categories are `XX.YY-P`, Subcategories `XX.YY-Pn`.

| Function | ID | Purpose | PF 1.0 Categories | PF 1.1 IPD Categories |
|---|---|---|---|---|
| Identify-P | ID-P | Understand the data processing, the individuals and the organizational context that give rise to privacy risk | ID.IM-P Inventory and Mapping; ID.BE-P Business Environment; ID.RA-P Risk Assessment; ID.DE-P Data Processing Ecosystem Risk Management | ID.IM-P; ID.BE-P; ID.RA-P (ID.DE-P moved to Govern-P as GV.DE-P) |
| Govern-P | GV-P | Governance structure, privacy values and policies, risk strategy, training, monitoring | GV.PO-P Governance Policies, Processes, and Procedures; GV.RM-P Risk Management Strategy; GV.AT-P Awareness and Training; GV.MT-P Monitoring and Review | GV.PO-P; GV.RM-P; **GV.OV-P Oversight** (new); **GV.RR-P Roles, Responsibilities, and Authorities** (new); GV.DE-P Data Processing Ecosystem Risk Management (relocated); GV.AT-P; GV.MT-P |
| Control-P | CT-P | Enable organizations and individuals to manage data with sufficient granularity | CT.PO-P Data Processing Policies, Processes, and Procedures; CT.DM-P Data Processing Management; CT.DP-P Disassociated Processing | Unchanged: CT.PO-P; CT.DM-P; CT.DP-P |
| Communicate-P | CM-P | Reliable understanding and dialogue about data processing and privacy risk | CM.PO-P Communication Policies, Processes, and Procedures; CM.AW-P Data Processing Awareness | Unchanged: CM.PO-P; CM.AW-P |
| Protect-P | PR-P | Safeguards against cybersecurity-related privacy events (the CSF-adapted Function) | PR.PO-P Data Protection Policies, Processes, and Procedures; PR.AC-P Identity Management, Authentication, and Access Control; PR.DS-P Data Security; PR.MA-P Maintenance; PR.PT-P Protective Technology | PR.PO-P; **PR.AA-P** Identity Management, Authentication, and Access Control (replaces PR.AC-P); PR.DS-P; **PR.PS-P Platform Security** and **PR.IR-P Technology Infrastructure Resilience** (absorb withdrawn PR.MA-P and PR.PT-P, mirroring CSF 2.0) |

Representative Subcategory outcomes (wording from the official Core tables; PF 1.0 identifiers unless noted):

| Subcategory | Outcome | GRC use |
|---|---|---|
| ID.IM-P1 | Systems/products/services that process data are inventoried | Record of processing / data inventory |
| ID.IM-P8 (1.1 IPD) | Data processing is mapped — data actions, data elements, component owners/operators, interactions of individuals and third parties | Data map for a DPIA/PIA |
| ID.RA-P3 / P4 | Potential problematic data actions and associated problems are identified; likelihoods and impacts are used to determine and prioritize risk | Privacy risk assessment (PRAM-style) |
| GV.PO-P1 | Organizational privacy values and policies (e.g., conditions on data uses or retention periods, individuals' prerogatives) are established and communicated | Privacy policy set |
| GV.RR-P1 (1.1 IPD) | Organizational leadership is responsible and accountable for privacy risk and fosters a risk-aware, ethical, continually improving culture | Board/executive accountability evidence |
| GV.MT-P1 | Privacy risk is re-evaluated on an ongoing basis and as key factors change (new technologies, legal obligations, data processing, systems) | Continuous review cadence |
| CT.DM-P1–P3 | Data elements can be accessed for review, for transmission or disclosure, for alteration | Data-subject rights handling (access, portability, rectification) |
| CT.DP-P1 / P2 | Data are processed to limit observability and linkability; to limit identification of individuals | De-identification, privacy-enhancing technologies |
| CM.AW-P1 | Mechanisms (notices, reports) for communicating processing purposes, practices, risks and individuals' options are established | Privacy notice program |
| CM.AW-P8 (1.1 IPD) | Individuals are provided with mitigation mechanisms (credit monitoring, consent withdrawal, data alteration or deletion) for impacts of problematic data actions | Breach/harm remediation |
| PR.DS-P1 / P2 | Data-at-rest / data-in-transit are protected | Encryption controls (shared with CSF PR.DS) |

### Profiles

A Profile is a selection of Functions, Categories and Subcategories. A **Current Profile** records outcomes currently achieved (partial achievement may be noted); a **Target Profile** records desired outcomes given business objectives, risk tolerance, legal obligations and ecosystem expectations. Gap = Target minus Current; the gap list becomes the prioritized action plan. Organizations may add their own Functions, Categories or Subcategories. PF 1.1 adds **Organizational Profiles** (the organization's own) and **Community Profiles** (sector, subsector, technology or use-case baselines that others adopt as informative references), in line with CSF 2.0.

### Implementation Tiers

Tiers characterize how an organization views privacy risk and whether its processes and resources are sufficient. They are a progression but not a compulsory one, and Tier selection is informed by the Target Profile, not the reverse; achievement is measured against the Target Profile, not the Tier.

| Tier | Name | Signature characteristics (each Tier is defined across four elements: risk management process; integrated program; data processing ecosystem relationships; workforce) |
|---|---|---|
| 1 | Partial | Ad hoc, reactive practices; limited organizational awareness; no ecosystem risk processes; no specific privacy roles; ad hoc training |
| 2 | Risk Informed | Management-approved practices not yet organization-wide policy; informal information sharing; risk assessment occurs but is not repeatable; named privacy personnel with mixed duties |
| 3 | Repeatable | Practices formally approved as policy and regularly updated; organization-wide approach with defined, implemented and reviewed policies; formal ecosystem mechanisms (written agreements, governance, monitoring); dedicated, skilled privacy personnel and regular training for all |
| 4 | Adaptive | Continuous improvement from privacy events and new risks; privacy risk monitored by senior executives alongside cybersecurity and financial risk; budget driven by risk environment and tolerance; proactive ecosystem contribution |

### Privacy risk management practices (Appendix D)

- **Data maps** (ID.IM-P) are the foundational artifact: data actions, data elements, components, owners/operators and individuals' interactions.
- **Privacy engineering objectives** (adapted from NIST IR 8062): *predictability*, *manageability*, *disassociability* — used alongside the security objectives (confidentiality, integrity, availability). Low scores signal higher privacy risk and the need for deeper assessment.
- **Risk model**: privacy risk = likelihood of a problematic data action × impact; likelihood is a contextual analysis, impact is assessed as costs to individuals then internalized to the organization (non-compliance costs, direct business costs, reputational costs). NIST's Privacy Risk Assessment Methodology (PRAM) supplies worksheets and an illustrative catalog of problematic data actions and problems.
- **Requirements traceability**: privacy requirements derived from the Target Profile are traced to controls (SP 800-53 or other catalogs) and assessed through the SDLC (plan, design, build/buy, deploy, operate, decommission).

### AI and privacy (PF 1.1 IPD, Section 1.2.2)

The draft states the PF can be used to manage privacy risk arising from data processing in AI systems across the AI life cycle: training on data collected without consent or safeguards; inference of personal attributes; privacy attacks such as data reconstruction, prompt injection and membership inference; bias; and generative AI used to create privacy-invasive content. It points to GV.RR-P (AI workforce roles), GV.MT-P (policy review for fast-moving AI risk), and Control-P/Communicate-P (de-identification, user preference mechanisms), and positions the NIST AI RMF 1.0 (AI 100-1) as the companion framework. Notably, the draft **withdrew** the one AI-specific Subcategory (ID.RA-P2) "to keep PF 1.1 Core outcomes technology-neutral" — AI is addressed in narrative and Profiles, not in the Core.

## Assessment, certification and evidence

- **No certification.** There is no accredited scheme, no NIST-recognized assessor, and no "PF-certified" claim that carries formal weight. "Aligned with the NIST Privacy Framework" is a self-attestation; evidence is the Profile pair, the gap analysis and the action plan.
- **Ready, Set, Go** (NIST's program method): *Ready* — use Identify-P and Govern-P to establish context, values, risk tolerance and run privacy risk assessments; *Set* — complete Current and Target Profiles, list gaps, prioritize actions; *Go* — implement, monitor and update Profiles as risk changes.
- **Typical evidence set**: data map and processing inventory; privacy risk assessment records (PRAM worksheets or equivalent); Current/Target Profile workbook (NIST publishes the Core as XLSX/DOCX and in its Cybersecurity and Privacy Reference Tool); Tier self-assessment with rationale; requirements-to-controls traceability; ecosystem Profiles exchanged with suppliers or customers; periodic Current Profile refresh.
- **Informative references** (NIST's official crosswalk repository, updated February 2026) include NIST-authored mappings to the CSF, to SP 800-53 Rev. 5 (joint PF/CSF crosswalk), to the Fair Information Practice Principles and to the AICPA 2017 Trust Services Criteria, plus contributor-submitted crosswalks to GDPR, CCPA/CPRA regulations, VCDPA, LGPD, India's DPDP Act and Rules, ISO/IEC 27701 and the IAPP CIPM body of knowledge. Contributor crosswalks are not NIST-validated: treat them as starting points and re-verify against the current law or standard edition.
- **Buying and third-party decisions**: a Target Profile becomes a prioritized privacy requirement list for procurement; a supplier's Current Profile is its evidence of contractual conformance; residual gaps are managed as accepted risk or mitigations.

## Timeline and status

| Date | Event |
|---|---|
| September 2018 | Department of Commerce launches the collaborative PF development effort |
| September 2019 | Preliminary draft released for comment |
| 16 January 2020 | **PF Version 1.0 published** (CSWP 10) |
| January 2020 onward | Crosswalk / Profile / guideline resource repository opened; annual "birthday" infographics 2021, 2022 |
| 25 January 2024 | NIST announces the 1.1 update and a joint-frameworks Data Governance and Management (DGM) Profile |
| 18 June 2024 | PF 1.1 Concept Paper and DGM Profile Concept Paper published |
| 25–26 June 2024 | "Ready, Set, Update!" public workshop (PF 1.1 + DGM Profile) |
| September 2024 | DGM Profile Working Session 1 |
| 14 April 2025 | **PF 1.1 Initial Public Draft** (CSWP 40 ipd) released; comment period to 13 June 2025 |
| 13 June 2025 | PF 1.1 IPD comment period closed |
| 14 May 2026 | DGM Profile Working Session 2 (mappings); DGM Profile IPD date "TBD" as of the June 2026 page update |
| As of September 2026 | **PF 1.1 final not yet published**: NIST's 1.1 page (updated 1 April 2026) shows "Coming soon"; CSRC lists CSWP 40 only as a draft. PF 1.0 remains the authoritative Core |

Open questions NIST put to reviewers in the IPD (which may change the final text): whether to publish Implementation Examples (possibly built from the NIST Privacy Workforce Taxonomy task statements); whether to renumber Subcategories to remove the gaps created by withdrawals and relocations; and whether to move further content (e.g., appendices) out of the PDF to the website. Programs built on the 1.1 IPD identifiers should expect identifier changes in the final.

## Key obligations for security/GRC teams

The PF imposes no legal obligations; the following are the program actions it structures.

1. **Decide which version to anchor on.** Build or maintain Profiles on PF 1.0 identifiers today and keep the 1.0→1.1 mapping workbook at hand; re-baseline once 1.1 is final. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).
2. **Build the data map and processing inventory first** (ID.IM-P) — it is the prerequisite for every other Function and doubles as the GDPR Art. 30 record and the DPIA description of processing. See [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md) and [../../templates/dpia-template.md](../../templates/dpia-template.md).
3. **Run privacy risk assessments with an explicit model** (ID.RA-P): enumerate problematic data actions, score likelihood and impact to individuals, then internalize to organizational impact; reuse the organization's risk-scoring scale. See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md) and [../risk-scoring.md](../risk-scoring.md).
4. **Set governance and accountability outcomes** (GV.PO-P, GV.RM-P; GV.RR-P and GV.OV-P in 1.1): named executive ownership of privacy risk, privacy values and policies, risk tolerance, board-level reporting. See [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md) and [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).
5. **Use Profiles as the crosswalk hub.** Map legal obligations (GDPR, US state privacy laws, sectoral rules) to Subcategories once, then reuse the Target Profile for gap assessments, audits and vendor questionnaires. See [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md) and [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
6. **Govern the data processing ecosystem** (ID.DE-P / GV.DE-P): exchange Profiles with processors and suppliers, embed privacy requirements in contracts, verify them. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../templates/vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md).
7. **Engineer for Control-P and Communicate-P**: data-subject request handling (CT.DM-P), de-identification/disassociability (CT.DP-P), notices and preference mechanisms (CM.AW-P); trace requirements through the SDLC.
8. **Integrate with the cybersecurity program**: Protect-P outcomes are shared with CSF Protect; breach detection, response and recovery stay in the CSF. Keep one control set and two Profiles. See [nist-csf-2.md](nist-csf-2.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
9. **Fold AI systems into the same Profiles** using the 1.1 IPD guidance and the AI RMF; do not wait for an AI-specific Subcategory — NIST removed it. See [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md) and [../../workflows/ai-system-intake.md](../../workflows/ai-system-intake.md).
10. **Track the 1.1 final and the DGM Profile** as horizon items. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

| Neighbour | Relationship |
|---|---|
| [NIST CSF 2.0](nist-csf-2.md) | Sibling framework with identical mechanics. PF 1.0 tracked CSF 1.1; PF 1.1 IPD tracks CSF 2.0 (six-Function CSF; PF keeps five "-P" Functions and borrows CSF's Detect/Respond/Recover for breaches). Category-level parallels: GV.RR, GV.OV, PR.AA, PR.PS, PR.IR now exist in both. NIST publishes an official PF↔CSF crosswalk |
| [NIST SP 800-53 Rev. 5](nist-800-53.md) | The PF is outcome-level; 800-53 supplies the control catalog (PT family, privacy baseline, privacy-relevant controls throughout). NIST's joint PF/CSF→SP 800-53 Rev. 5 crosswalk is the official bridge; PF 1.0 still cites Rev. 4 in its references |
| NIST IR 8062 and PRAM | Source of the privacy engineering objectives and the problematic-data-action risk model the PF assumes; PRAM worksheets are the de facto assessment method |
| NIST AI RMF 1.0 | Named companion in PF 1.1 IPD for AI risk; NIST is developing joint "NIST Frameworks" Community Profiles (the DGM Profile is the first) — see [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md) and [../regulations/eu-ai-act.md](../regulations/eu-ai-act.md) |
| [GDPR](../regulations/gdpr.md) and [US state privacy laws](../regulations/us-state-privacy.md) | Contributor crosswalks exist in NIST's repository (GDPR, CCPA/CPRA, VCDPA, LGPD, India DPDP). The PF does not define lawful basis, transfer rules or breach clocks; it organizes the program that meets them. DPIA/PIA content maps naturally to ID.IM-P, ID.RA-P and GV.RM-P |
| [ISO/IEC 27001:2022](iso-27001-2022.md) / ISO/IEC 27701 | 27701 is the certifiable privacy information management extension; a contributor crosswalk to the PF exists. Use the PF for program design and 27701 when a certificate is required. Note ISO/IEC 27701 edition currency (verify) before relying on any 27701 mapping |
| [SOC 2 Trust Services Criteria](soc2-tsc.md) | NIST lists a crosswalk to the AICPA 2017 TSC (Privacy category). Useful when a SOC 2 Privacy report is the external assurance vehicle |
| [HIPAA](../regulations/hipaa.md), [GLBA](../regulations/glba-ftc-safeguards.md) | Sectoral US privacy/security rules; no NIST-published PF crosswalk was found on the repository page, so mappings must be built or sourced independently |
| [Framework crosswalk](../crosswalks/framework-crosswalk.md) | Repository-level comparison of security frameworks; the PF sits alongside as the privacy-program layer |

## Primary sources

- NIST Privacy Framework Version 1.0 (CSWP 10), 16 January 2020 — official text (PDF): https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.01162020.pdf
- NIST Privacy Framework 1.1 Initial Public Draft (CSWP 40 ipd), 14 April 2025 — official draft text (PDF): https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.40.ipd.pdf
- CSRC publication record for CSWP 40 ipd (dates, comment period): https://csrc.nist.gov/pubs/cswp/40/nist-privacy-framework-11/ipd
- CSRC CSWP publication list (confirms no final CSWP 40 as of September 2026): https://csrc.nist.gov/publications/cswp
- NIST Privacy Framework program page (publisher page): https://www.nist.gov/privacy-framework
- Privacy Framework 1.1 project page (timeline, "coming soon" status; updated 1 April 2026): https://www.nist.gov/privacy-framework/privacy-framework-version-11
- Using Privacy Framework 1.1 (publisher guidance: informative references, accountability, Ready/Set/Go, SDLC, ecosystem, buying decisions): https://www.nist.gov/privacy-framework/using-privacy-framework-11
- Resource Repository — Crosswalks (publisher page; updated 9 February 2026): https://www.nist.gov/privacy-framework/resource-repository/browse/crosswalks
- Data Governance and Management Profile project page (updated 24 June 2026): https://www.nist.gov/privacy-framework/new-projects/data-governance-and-management-profile
- NIST Privacy Framework Newsroom (publication history): https://www.nist.gov/privacy-framework/newsroom
- Not fetched (404 at time of writing): NIST PF FAQs page and the PF 1.0→1.1 Core mapping page; the mapping content above is taken from Table 2 of the 1.1 IPD itself.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
