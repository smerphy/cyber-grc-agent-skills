# NIST SP 800-161 Rev. 1 — Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations (C-SCRM)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument / citation | NIST Special Publication 800-161 Revision 1, "Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations" (NIST SP 800-161r1-upd1, DOI 10.6028/NIST.SP.800-161r1-upd1) |
| Publisher | US National Institute of Standards and Technology (NIST), Computer Security Division; published under NIST's FISMA (44 U.S.C. § 3551 et seq.) authority |
| Status and key dates | Rev. 1 final 5 May 2022; errata "update 1" incorporated 1 November 2024 (change log in Appendix K). Supersedes the 2015 original. No Rev. 2 draft announced on the NIST C-SCRM project page as of September 2026 |
| Who is covered | Mandatory for US federal executive agencies (non-national-security systems) via FISMA/OMB Circular A-130 and the FASCSA "consistent with NIST guidance" mandate; voluntary for everyone else — but widely flowed down to federal contractors and used as the de-facto C-SCRM reference by private-sector programs |
| Structure | Body: Ch. 1 Introduction, Ch. 2 Integration of C-SCRM into enterprise-wide risk management (three-level model), Ch. 3 Critical success factors (acquisition, information sharing, training, key practices, metrics, dedicated resources). Appendices A–K: control overlay (A/B), Risk Exposure Framework (C), templates (D), FASCSA agency guidance (E), EO 14028 software supply chain pointer (F), C-SCRM in the Frame/Assess/Respond/Monitor process (G), glossary/acronyms/resources (H–J), revision history (K) |
| Control layer | An **enhanced overlay** of SP 800-53 Rev. 5: C-SCRM-relevant controls from all 20 Rev. 5 families with supplemental C-SCRM guidance, plus four additions — AT-3(6), CM-8(10), MA-8, SR-13 |
| Certifiable? | No. Self-assessment against the C-SCRM baseline (Appendix B, Table 6) and control assessment via SP 800-53A. Federal agencies are measured through FISMA/OMB reporting; contractors through contract flow-down |
| Penalties / enforcement | None intrinsic. Enforcement comes from the surrounding legal regime: FASCSA exclusion/removal orders (41 U.S.C. §§ 1323, 4713), Section 889 contract prohibitions (FAR 52.204-25), agency procurement decisions, and the False Claims Act exposure that attaches to contractual attestations |
| Relationship to neighbours | Elaborates CSF 2.0 Govern > GV.SC (10 subcategories); SP 800-53 Rev. 5 SR family is the control anchor; SP 800-37 RMF is the system-level process; SP 800-218 SSDF and EO 14028 cover the software-producer side; SP 800-18 Rev. 2 (June 2026) defines the system-level C-SCRM plan; SP 1326 (July 2026) is the due-diligence quick-start |

## What it is

SP 800-161 is NIST's foundational guidance on managing cybersecurity risk that enters an enterprise through what it buys, integrates and depends on: hardware, software, cloud and other services, and the developers, integrators and logistics providers behind them. The risks it targets are counterfeit and tampered components, malicious code inserted upstream, poor development and manufacturing practice, theft, and loss of visibility into how acquired technology is built and supported. NIST has run a C-SCRM program since 2008; on NIST's own account the SECURE Technology Act (FASCSA, 2018) and the FASC rule gave it specific authority to develop C-SCRM guidelines, and Executive Order 14028 (May 2021) added the software supply chain tasking that Appendix F answers. The 2015 original of SP 800-161 was rewritten as Revision 1 in 2022.

Rev. 1 does three things: it integrates C-SCRM into the SP 800-39 multilevel risk-management model (enterprise, mission/business, operational) rather than treating it as a procurement checklist; it provides a control overlay on SP 800-53 Rev. 5 so that C-SCRM can be assessed with the same RMF machinery as any other control set; and it ships practical artefacts — templates for the C-SCRM strategy and implementation plan, policy, system plan and risk assessment, an example implementation-maturity model, a threat-scenario method, and federal-specific guidance for FASCSA risk assessments. The November 2024 errata update did not change the structure; its substantive edits added RA-3(1) and PM-30 to the baseline and flow-down set, revised RA-3/RA-5 vulnerability language, added definitions for "vulnerability report" and "vulnerability advisory report" (aligned to ISO/IEC 29147), replaced CSF 1.1 references with CSF 2.0, and revised the online Appendix F content on SBOM capabilities and OMB M-22-18 software attestations.

## Who it covers / Scope

| Population | Basis | Practical effect |
|---|---|---|
| US federal executive agencies (non-national-security systems) | FISMA; OMB Circular A-130; 41 U.S.C. § 1326(a) requires each agency head to assess and respond to supply chain risk from "covered articles" consistent with standards, guidelines and practices the FASC identifies under § 1323(a)(1) — i.e., NIST's | Must implement; Appendix E supplies the FASCSA-specific assessment factors, severity schema and record content |
| Federal prime contractors and sub-tier contractors | Contract clauses; Appendix B flags "flow down" controls that primes should push to sub-tiers | Obligations are only as strong as the contract language; SP 800-161 is the source acquirers cite when writing that language |
| Non-federal organizations | Voluntary; NIST states the publication "may be used by nongovernmental organizations on a voluntary basis" | Used as the reference design for a C-SCRM program and as the elaboration of CSF 2.0 GV.SC; regulators in other regimes (NIS2, DORA) do not cite it, but its practices map cleanly onto their supply-chain measures |
| Cloud service providers | Sec. 1.3: external system service providers include CSPs, and the publication does not replace federal cloud security guidance | Federal agencies should apply FedRAMP guidelines first, then this publication for the processes and controls FedRAMP does not address; treat CSPs as suppliers under the SR/SA controls |
| Audience (Sec. 1.2) | AOs, CIOs, CISOs, privacy officials; system developers and integrators; acquisition and contracting officers; logistics/disposition staff; auditors, IGs and assessors; commercial suppliers | Section 1.4 defines reader profiles that route each audience to the relevant chapters |

Scope spans the entire SDLC (Sec. 1.5): research and development, design, manufacturing, acquisition, delivery, integration, operations and maintenance, and disposal, for ICT and OT products and services. Appendix A draws controls from the high-, moderate- and low-impact levels of SP 800-53 Rev. 5, and NIST is explicit (Sec. 1.1) that the guidance is not one-size-fits-all: the controls are a starting point from which items may be removed, added or specialised.

## Structure and requirements

### The three-level model (Sec. 2.3)

| Level | Owner | Key C-SCRM outputs |
|---|---|---|
| Level 1 — Enterprise | Executive leadership, C-SCRM PMO | C-SCRM strategy, policy and implementation plan; governance structure; risk appetite and tolerance; enterprise risk framing |
| Level 2 — Mission and business process | Mission/business owners, program managers | Mid-level C-SCRM strategies, policies and implementation plans tailored to the mission; common control baselines; mission-level risk assessments |
| Level 3 — Operational | System owners, engineers, ISSOs | System-level C-SCRM plan with tailored controls; feeds and mirrors RMF steps (SP 800-37); informed by Level 1–2 outputs |

Every Appendix A control carries a Level(s) designation (1, 2, 3) so that control selection happens at the right layer. A **C-SCRM PMO** (Sec. 2.3.5) — or a risk function in smaller organizations — sits at Level 1 or 2 and must be cross-disciplinary (security, acquisition, legal, engineering, supply/logistics).

### Risk-management process (Appendix G) and Risk Exposure Framework (Appendix C)

- C-SCRM activities are mapped onto the SP 800-39 steps **Frame → Assess → Respond → Monitor**, iterative rather than sequential, with a criticality analysis, threat analysis, vulnerability analysis and impact analysis feeding likelihood/impact determination (Fig. 13).
- Appendix C's Risk Exposure Framework documents **threat scenarios** (ordered sets of threat events tied to a threat source) and uses them to derive a risk determination and response; NIST points to the CISA ICT SCRM Task Force Threat Scenarios Report v3 (August 2021) for additional scenarios.
- Appendix D.4's risk-assessment template follows five analyses: information gathering and scoping (Table 26, "Information gathering and scoping analysis"; NIST released a fillable "SCRM Assessment Scoping Questionnaire" version of it on 2 December 2025), threat, vulnerability, impact, risk response.

### Key practices and implementation model (Sec. 3.4, Table 3)

| Tier | Representative practices |
|---|---|
| Foundational | C-SCRM PMO and leadership support; policies across levels; defined governance and roles; dedicated resources; integration into acquisition/procurement policy; FIPS 199 impact levels; defined C-SCRM control baseline; supplier management program; C-SCRM inside incident management; processes to ensure suppliers disclose vulnerabilities |
| Sustaining | Threat-informed program; third-party assessments, site visits and formal certification; formal supplier monitoring; defined risk appetite/tolerances; formal information sharing (e.g., with the FASC); regular executive/risk-committee reporting; training; C-SCRM in SDLC and contracts; suppliers in IR/DR/contingency planning; collaboration to improve supplier practice; defined and reported metrics |
| Enhancing | Process automation; quantitative risk analysis; predictive and adaptive strategies; community of practice |

NIST's position: reach a base level of maturity in the Foundational practices before investing in the rest.

### Control overlay (Appendix A/B)

- Structure: SP 800-53 Rev. 5 controls with C-SCRM relevance, organized by the 20 Rev. 5 families (AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC, SI, SR), each with supplemental C-SCRM guidance and level designations. Controls not listed are deemed not directly applicable.
- Appendix B, Table 6 marks each control as **C-SCRM Baseline** (Rev. 5 low-baseline controls are treated as C-SCRM-relevant, plus additions) and/or **Flow Down** (prime → sub-tier), by level. Update 1 added RA-3(1) and PM-30 to both sets.
- Additions not in SP 800-53 Rev. 5: **AT-3(6)** Role-Based Training | Counterintelligence Training; **CM-8(10)** System Component Inventory | SBOMs for Open Source Projects; **MA-8** Maintenance Monitoring and Information Sharing; **SR-13** Supplier Inventory (tier-one supplier inventory with procurement identifiers, reviewed at an enterprise-defined frequency).
- The SR family as used in the overlay (SR-1 to SR-12 from Rev. 5, SR-13 new):

| Control | Title | Control | Title |
|---|---|---|---|
| SR-1 | Policy and Procedures | SR-8 | Notification Agreements |
| SR-2 | Supply Chain Risk Management Plan | SR-9 | Tamper Resistance and Detection |
| SR-3 | Supply Chain Controls and Processes | SR-10 | Inspection of Systems or Components |
| SR-4 | Provenance | SR-11 | Component Authenticity |
| SR-5 | Acquisition Strategies, Tools, and Methods | SR-12 | Component Disposal |
| SR-6 | Supplier Assessments and Reviews | SR-13 | Supplier Inventory (new in SP 800-161) |
| SR-7 | Supply Chain Operations Security | | |

See [nist-800-53.md](nist-800-53.md) for the parent catalog.

### Templates (Appendix D)

| Template | Level | Contents |
|---|---|---|
| D.1 C-SCRM Strategy and Implementation Plan | 1 (tailored at 2) | Purpose; authority and compliance; strategic objectives; implementation plan and progress tracking; roles; definitions; revision |
| D.2 C-SCRM Policy | 1–2 | Authority; description; policy statements; roles; definitions; revision |
| D.3 C-SCRM Plan (system) | 3 | System identifier, description, FIPS 199 categorization, operational status, diagrams/inventory/life-cycle, interconnections, control details, roles, contingencies, related laws, approval, attachments, life-cycle linkage. SP 800-18 Rev. 2 (June 2026) publishes a C-SCRM Plan example outline alongside its security and privacy plan outlines |
| D.4 C-SCRM Risk Assessment | any | Authority; description; scoping (Table 26); threat, vulnerability, impact and risk-response analyses; roles |

### Federal software supply chain layer (Appendix F, online)

Appendix F points to NIST's EO 14028 web content rather than printing it, so it can be updated independently. EO 14028 Sec. 4(e) elements that flow into acquirer requirements include automated vulnerability checking, provenance and component controls, providing an **SBOM** to purchasers, a vulnerability disclosure program, and attesting to conformity with secure development practices; the SSDF (SP 800-218) is the practice reference (SP 800-218r1 / SSDF 1.2 initial public draft released 17 December 2025). EO 14306 (6 June 2025) amended EO 14144 and directed NIST to update SP 800-53 on secure and reliable deployment of patches and updates by 2 September 2025 (delivered as SP 800-53 Release 5.2.0 on 27 August 2025, adding SA-15(13), SA-24 and SI-2(7)) and to publish a preliminary SSDF update by 1 December 2025 with a final version within 120 days of that preliminary. The preliminary update appeared on 17 December 2025; no final SSDF 1.2 had been published as of September 2026.

## Assessment, certification and evidence

- **No certification scheme.** Assessment is control-based: select the C-SCRM baseline (Table 6) tailored by level, then assess with SP 800-53A methods; results feed the system authorization package under the RMF. See [control-testing](../../skills/control-testing/SKILL.md) and the [control test workpaper](../../templates/control-test-workpaper.md).
- **Evidence set that auditors and FASCSA reviewers expect:** enterprise C-SCRM strategy/policy with approval; supplier inventory (SR-13) reconciled to procurement; criticality analysis for systems and components; documented supplier assessments and reviews (SR-6) with due-diligence records (SP 1326 components: FOCI, provenance, resilience, foundational cyber practices, supply chain tiers); contract clauses and flow-down evidence (SA-4, SR-3, SR-5, SR-8); provenance and authenticity checks (SR-4, SR-10, SR-11); incident and vulnerability notification agreements; disposal records (SR-12); metrics reported to executives (Sec. 3.5.1).
- **Federal agencies (Appendix E):** supply chain risk assessments for covered articles must document baseline risk factors, apply the risk severity schema, and keep an assessment record in the content format E.3 describes, so that agency-level assessments align with FASC-level actions.
- **FASCSA order evidence (FAR subpart 4.23, clauses 52.204-28/-29/-30):** contractors must search SAM for applicable FASCSA orders, represent and disclose against them, and — on identifying a covered article or source subject to an order — report within **3 business days**, with further mitigation detail within **10 business days**.
- **Section 889 / FAR 52.204-25 evidence:** representations that no covered telecommunications or video surveillance equipment (Huawei, ZTE, Hytera, Hikvision, Dahua and affiliates) is provided (prohibition from 13 August 2019) or used by the contractor (from 13 August 2020); discovery during performance must be reported to the contracting officer within **one business day**, with mitigation detail within **10 business days**.

## Timeline and status

| Date | Event |
|---|---|
| 2015 | SP 800-161 original published |
| 21 Dec 2018 | SECURE Technology Act; Title II = FASCSA, creating the FASC (41 U.S.C. §§ 1321–1328) and agency authorities (§ 4713) |
| 13 Aug 2019 / 13 Aug 2020 | Section 889(a)(1)(A) then (a)(1)(B) prohibitions take effect (FAR 52.204-25) |
| 12 May 2021 | EO 14028, Sec. 4 tasks NIST on software supply chain security |
| 10 May 2021 / 28 Oct 2021 | First and second public drafts of Rev. 1 |
| 26 Aug 2021 (effective 27 Sep 2021) | FASC final rule, 86 FR 47581, 41 CFR Parts 201 and 201-1: FASC operation, information sharing, exclusion/removal order procedures |
| 5 May 2022 | SP 800-161 Rev. 1 final |
| 23 Dec 2022 | FY2023 NDAA extends the FASCSA subchapter's sunset to 31 December 2033 (41 U.S.C. § 1328) |
| 5 Oct 2023 (effective 4 Dec 2023) | FAR final rule implementing FASCSA orders, 88 FR 69503 (FAR Case 2020-011): new FAR subpart 4.23 and clauses 52.204-28, -29, -30 |
| 26 Feb 2024 | NIST CSF 2.0 elevates supply chain to Govern (GV.SC) |
| 21 Oct 2024 | SP 1305, CSF 2.0 quick-start guide for C-SCRM |
| 30 Oct 2024 | SP 1326 due-diligence quick-start guide, initial public draft |
| 1 Nov 2024 | Rev. 1 errata update 1 (Appendix K) |
| 6 Jun 2025 | EO 14306 amends EO 14144: SSDF update and SP 800-53 patching guidance tasking |
| 27 Aug 2025 | SP 800-53 Release 5.2.0 adds patch/update deployment controls in answer to that tasking |
| 2 Dec 2025 | Fillable SCRM Assessment Scoping Questionnaire (Table 26) released |
| 17 Dec 2025 | SP 800-218r1 (SSDF 1.2) initial public draft |
| 30 Jun 2026 | SP 800-18 Rev. 2 final — system security, privacy and C-SCRM plans as one set of "system plans" |
| 8 Jul 2026 | SP 1326 final |
| Sep 2026 | Status: Rev. 1 upd1 is current; no Rev. 2 draft is listed on the NIST C-SCRM project pages. SSDF 1.2 remains an initial public draft, past the EO 14306 deadline. The FAR Council's "Revolutionary FAR Overhaul" proposed rules (2026) reopen FAR Part 4, which carries the Section 889 and FASCSA subparts — pending. Watch the EO 14028 online Appendix F, the final SSDF 1.2 and FASC order activity via [regulatory-horizon-scanning](../../skills/regulatory-horizon-scanning/SKILL.md) |

## Key obligations for security/GRC teams

1. **Decide the mandate.** Federal agency or contractor → SP 800-161 is binding through FISMA/FASCSA or contract; otherwise adopt it as the reference architecture for CSF 2.0 GV.SC. See [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md).
2. **Stand up governance at Level 1**: C-SCRM strategy and implementation plan, policy, PMO or named risk function, risk appetite — use the Appendix D templates and the repository's [policy-authoring](../../skills/policy-authoring/SKILL.md) skill and [policy template](../../templates/policy-template.md).
3. **Build and maintain the supplier inventory (SR-13)** and a criticality-ranked view of suppliers, products and services; reconcile against procurement and accounts-payable data.
4. **Run supplier due diligence and assessments (SR-6, SP 1326)** before contracting and on a monitoring cadence; capture FOCI, provenance, resilience and foundational cyber practices. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md), the [vendor security questionnaire](../../templates/vendor-security-questionnaire.md) and the [vendor onboarding workflow](../../workflows/vendor-onboarding.md).
5. **Write C-SCRM requirements into contracts (SA-4, SR-3, SR-5, SR-8)**: flow-down controls, notification agreements for incidents and vulnerabilities, SBOM and attestation where software is acquired, right to assess, Section 889 representations where federal money is involved.
6. **Integrate supply chain scenarios into risk assessment and the risk register** using the Appendix C threat-scenario method; see [risk-assessment](../../skills/risk-assessment/SKILL.md) and [risk-scoring](../risk-scoring.md).
7. **Wire suppliers into incident response**: notification agreements, supplier participation in IR/DR/contingency exercises (Sustaining practice), and a path from supplier-originated incidents into regulatory reporting — see [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md).
8. **Gap-assess against the Appendix B baseline** by level and map results to CSF 2.0 GV.SC and other frameworks in use; see [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md) and [control-mapping](../../skills/control-mapping/SKILL.md).
9. **Report C-SCRM metrics to executives** (Sec. 3.5.1) — supplier coverage, assessment currency, open supplier findings, SBOM coverage; see [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **NIST CSF 2.0:** GV.SC-01 to GV.SC-10 are the outcome statements (program established; supplier roles; integration into ERM; suppliers known and prioritised by criticality; requirements in contracts; pre-contract due diligence; risks monitored across the relationship; suppliers in incident planning; life-cycle performance monitoring; post-termination provisions). SP 800-161 is the "how"; CSF 2.0 is the "what". See [nist-csf-2.md](nist-csf-2.md).
- **SP 800-53 Rev. 5 / RMF:** the SR family and SA controls are the anchor; SP 800-161 adds guidance, levels and four new items. A system's C-SCRM plan is now one of the three "system plans" in SP 800-18 Rev. 2. See [nist-800-53.md](nist-800-53.md).
- **FASCSA, the FASC rule and the FAR:** § 1323 gives the FASC power to recommend exclusion and removal orders (a named source gets 30 days after receipt of notice to submit information and argument in opposition); § 4713 lets agency heads take covered procurement actions, with congressional notice within 7 calendar days and confidentiality until a determination is made; § 1326 puts the assessment duty on each agency consistent with NIST guidance; the subchapter sunsets on 31 December 2033 (§ 1328). FAR subpart 4.23 and clauses 52.204-28/-29/-30 push issued orders into solicitations and contracts. Appendix E is the bridge between agency assessments and FASC action.
- **Section 889 (FAR 52.204-25):** a hard prohibition list rather than a risk-management practice; treat it as a screening control inside supplier due diligence.
- **EU NIS2:** Art. 21(2)(d) requires "supply chain security, including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers"; Art. 21(3) requires entities to weigh supplier-specific vulnerabilities, product quality and secure development practices and to take into account the results of Art. 22 Union-level coordinated security risk assessments of critical supply chains. SP 800-161's supplier assessment, contract and monitoring practices are a ready evidence base for those measures. See [nis2.md](../regulations/nis2.md).
- **EU DORA:** Arts. 28–30 impose a register of information, pre-contract assessment, concentration-risk analysis and mandatory contract clauses for ICT third-party providers, with direct oversight of critical providers. SR-13 supplier inventory ≈ DORA register at a lower level of prescription; SR-8 notification agreements ≈ Art. 30 incident-assistance clauses. See [dora.md](../regulations/dora.md).
- **ISO/IEC 27001:2022:** the Annex A organizational controls on supplier relationships and on use of cloud services, and ISO/IEC 27036 (SP 800-161's reference list cites ISO/IEC 27036-2:2014 on supplier-relationship requirements, and ISO/IEC 29147:2018 for the vulnerability-disclosure definitions added in update 1) cover the same ground with less operational detail; ISO 28000 (cited as ISO 28000:2007 in the Appendix D.1 strategy template) addresses security management for the supply chain. Current ISO editions were not verified here — the catalogue and full texts are paywalled and blocked to scripted access (verify). See [iso-27001-2022.md](iso-27001-2022.md).
- **CISA ICT SCRM Task Force:** public-private body whose Threat Scenarios Report v3 (August 2021) SP 800-161 cites in Appendix C as the source of additional threat scenarios and threat lists, and as the basis for Scenario 1. The task force's other deliverables were not checked here — cisa.gov blocks scripted access.
- **SOC 2 / vendor attestations:** SOC 2 reports and ISO certificates are Sustaining-tier evidence inputs to SR-6 supplier assessments, not substitutes for them. See [soc2-tsc.md](soc2-tsc.md).
- **Crosswalks:** [framework-crosswalk.md](../crosswalks/framework-crosswalk.md).

## Primary sources

- NIST SP 800-161r1-upd1 full text (publisher document, PDF): https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-161r1-upd1.pdf
- NIST CSRC publication page for SP 800-161 Rev. 1 (dates, supplemental material, Table 26 questionnaire): https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final
- NIST C-SCRM project page and news feed (2024–2026 developments): https://csrc.nist.gov/projects/cyber-supply-chain-risk-management and https://csrc.nist.gov/Projects/cyber-supply-chain-risk-management/news
- NIST SP 800-18 Rev. 2, SP 1326 and SP 1305 publication pages: https://csrc.nist.gov/pubs/sp/800/18/r2/final ; https://csrc.nist.gov/pubs/sp/1326/final ; https://csrc.nist.gov/pubs/sp/1305/final
- NIST CSF 2.0 (CSWP 29), GV.SC subcategories: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
- NIST SP 800-53 Rev. 5 publication page: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- 41 U.S.C. §§ 1323, 1326, 1328, 4713 (legal text, via Cornell LII): https://www.law.cornell.edu/uscode/text/41/1323 ; /1326 ; /1328 ; /4713
- FASC final rule, 86 FR 47581 (26 Aug 2021, effective 27 Sep 2021), 41 CFR Parts 201 and 201-1 (legal text, govinfo PDF): https://www.govinfo.gov/content/pkg/FR-2021-08-26/pdf/2021-17532.pdf
- FAR 52.204-25 (Section 889 clause, legal text, eCFR): https://www.ecfr.gov/current/title-48/chapter-1/subchapter-H/part-52/subpart-52.2/section-52.204-25
- FAR subpart 4.23, Federal Acquisition Security Council (legal text, eCFR): https://www.ecfr.gov/current/title-48/chapter-1/subchapter-A/part-4/subpart-4.23
- FAR final rule implementing FASCSA orders, 88 FR 69503 (5 Oct 2023, effective 4 Dec 2023; legal text, govinfo): https://www.govinfo.gov/content/pkg/FR-2023-10-05/pdf/2023-21320.pdf
- EO 14028 (12 May 2021), 86 FR 26633 (legal text, govinfo PDF): https://www.govinfo.gov/content/pkg/FR-2021-05-17/pdf/2021-10460.pdf
- EO 14306 (signed 6 June 2025), 90 FR 24723 (legal text, govinfo): https://www.govinfo.gov/content/pkg/FR-2025-06-11/html/2025-10804.htm
- FAR Council proposed rule, "Revolutionary Federal Acquisition Regulation Overhaul Parts 1, 2, 4, 33, 39, 40, and 53", 91 FR 37550 (23 June 2026): https://www.federalregister.gov/documents/2026/06/23/2026-12559/federal-acquisition-regulation-revolutionary-federal-acquisition-regulation-overhaul-parts-1-2-4-33
- NIS2, Directive (EU) 2022/2555, Arts. 21–22 (legal text, EUR-Lex): https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- CISA ICT SCRM Task Force Threat Scenarios Report v3 (August 2021), cited by SP 800-161 Appendix C: https://www.cisa.gov/sites/default/files/publications/ict-scrm-task-force-threat-scenarios-report-v3.pdf — could not be fetched (cisa.gov returns 403 to scripted access); content above is taken from SP 800-161's own citation of it
- Not fetched: ISO/IEC 27036, ISO/IEC 29147 and ISO 28000 catalogue entries and texts (iso.org returns 403; the standards are paywalled)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
