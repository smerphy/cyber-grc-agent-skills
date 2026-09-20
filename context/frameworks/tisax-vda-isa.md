# VDA ISA and TISAX (automotive information security assessment and exchange)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | **VDA ISA** — the "Information Security Assessment" criteria catalogue (an Excel workbook); **TISAX** — "Trusted Information Security Assessment Exchange", the assessment and result-exchange scheme built on it |
| Publisher / governance | Catalogue authored and maintained by the **ENX Working Group ISA** (authorship taken over from the VDA in 2019) and officially published by the **VDA**. TISAX is operated and governed by **ENX Association** (non-profit under the French Law of 1901, reg. no. w923004198; offices Boulogne-Billancourt and Frankfurt am Main) |
| Current catalogue | **ISA 6.0.3** — workbook cover reads "Version: 6.0.3"; ISA 6 announced 16 October 2023, mandatory for TISAX assessments **ordered from 1 April 2024** |
| Next catalogue | **VDA ISA2027**, published **1 July 2026**; applies to assessments **ordered from 1 January 2027**. Final date to open an initial assessment under ISA 6 is **March 2027** |
| Release cycle | From ISA2027, **year-based versioning and an annual cycle**: published in summer, effective 1 January of the named year (ISA2028 due summer 2027) |
| Structure | Three criteria catalogues — Information Security (ch. 1–7), Prototype Protection (ch. 8), Data Protection (ch. 9). ISA 6.0.3: 46 / 22 / 12 control questions. ISA2027: 46 / 20 / 12 |
| Scoring | Maturity levels **0–5**; **target maturity level 3** for every control question; maximum result score 3.0 with cut-back averaging |
| Certifiable? | No certificate. Third-party **assessment** by an ENX-approved audit provider produces **TISAX labels**, valid **three years**, held only in the ENX portal and disclosed to partners through publication or bilateral sharing that the participant controls |
| Licence / cost | Catalogue is free under **Creative Commons Attribution-NoDerivatives 4.0** (© ENX Association), with an added grant to distribute clearly marked derivatives. ENX charges a participation fee based on the locations in registered scopes; the assessment itself is priced competitively by the audit provider |
| Scale | ENX reported **more than 21,000 assessed locations** and **more than 5,000 active users** of TISAX assessment results, from more than ten vehicle manufacturers plus thousands of suppliers (July 2026); a joint ENX/Auto-ISAC statement of March 2026 cited more than 20,000 assessed sites across 90 countries |

## What it is

TISAX answers a supply-chain problem, not a legal one. Automotive OEMs and tier-1 suppliers share design data, prototypes and personal data with thousands of partners, and before TISAX each customer ran its own supplier security audit against its own catalogue. The VDA working group condensed those expectations into one questionnaire — the ISA — and ENX added the missing half: an approved-auditor regime plus a portal where one assessment result can be shared with many customers. First participants registered on 28 June 2016.

Two things follow from that design. First, **TISAX is contractual, not statutory** — nobody is legally obliged to hold a label; you need one because a customer's purchasing process demands it. Second, **results are private by default**: the ENX portal is an exchange mechanism under the assessed company's control, and publication or sharing, once granted, cannot be revoked.

The ISA began as an automotive reading of ISO/IEC 27001 — TISAX started in 2016 on ISA 2.1 — but from ISA 5 onward ENX positions it as an independent industry standard that retains mappings to, rather than derivation from, other standards. Every control question carries a "Reference to other standards" cell (ISO/IEC 27001:2022 and, in ISA 6, also :2013; ISA/IEC 62443; NIST CSF 1.1 in ISA 6, NIST CSF 2.0 in ISA2027) and a "Reference to implementation guidance" cell pointing to BSI-Standard 200-2, the BSI IT-Grundschutz Compendium and NIST SP 800-53 Rev. 5. ISA 6 explicitly extended the scope of "IT systems" to **operational technology (OT)**, mapping to ISA/IEC 62443-2.

## Who it covers / Scope

- **No statutory applicability test.** Scope is driven by customer requirements: an OEM or supplier tells you which *assessment objectives* (labels) you must achieve. Participants are far from all manufacturers: the registration form's industry list runs from IT services, telecommunications and software development through consulting, marketing, agency, printing, photography and translation services, vehicle testing, simulation and prototype construction, development and CAx services, production, contract manufacturing, shop floor and logistics, to dealerships, financial services, insurance and claims settlement.
- **Scope = locations, not legal entity.** A participant registers one or more *assessment scopes*, each a set of physical locations plus assessment objectives. The **standard scope description (version 2.0)** is fixed text that cannot be edited; ENX states it is the right choice for well over 99% of participants, and other participants only accept results based on it. Custom extended and full custom scopes exist but are not generally accepted.
- **ISMS scope vs assessment scope differ from ISO/IEC 27001.** Under ISO/IEC 27001 the audit scope must equal the ISMS scope; under TISAX the assessment scope is predefined and may be *smaller* than the ISMS scope, but must sit inside it.
- **Simplified Group Assessment (SGA)** is available for participants with at least three locations in a scope and a centrally organised, highly developed ISMS; both ISA 6.0.3 and ISA2027 carry a dedicated "Additional requirements for Simplified Group Assessments (SGA)" column. Higher initial effort, lower marginal cost per location. An SGA uses the ISA version of the initial assessment, as do scope extensions.
- All locations in one scope share the same assessment objectives, one report, one expiry date — and one failure point: if one location fails, the scope fails.

## Structure and requirements

### The three criteria catalogues

| Catalogue | Chapters | Control questions (ISA 6.0.3 → ISA2027) | Covers |
|---|---|---|---|
| Information Security | 1 IS Policies and Organization; 2 Human Resources; 3 Physical Security; 4 Identity and Access Management; 5 IT Security/Cyber Security; 6 Supplier Relationships; 7 Compliance | 46 → 46 | The ISMS itself: policies, organisation, asset management, IS risk management, internal assessments, incident and crisis management, cryptography, operations security, secure acquisition and development, supplier relationships, legal compliance |
| Prototype Protection | 8 (ISA 6: 8.1 Physical and Environmental Security, 8.2 Organizational Requirements, 8.3 Handling of vehicles/components/parts, 8.4 Trial vehicles, 8.5 Events and shootings) | 22 → 20 | Perimeter and building security, sight protection, intrusion monitoring, visitor management, client segregation, NDAs, subcontractors, camouflage, transports, test drives, film and photo shoots |
| Data Protection | 9.1 Policies; 9.2 Organization; 9.3 Processing directory; 9.4 DPIA; 9.5 Data transfers; 9.6 Requests and incidents; 9.7 Human Resources; 9.8 Instructions | 12 → 12 | GDPR **Article 28** processor duties, plus special categories under **Article 9** for the "Special data" objective |

Each control question carries an **Objective** and four requirement tiers — *Requirements (must)*, *Requirements (should)*, *Additional requirements for high protection needs*, *Additional requirements for very high protection needs* — plus a separate column of additional requirements for Simplified Group Assessments. You fulfil every tier up to the protection need implied by your assessment objective — and you must satisfy the requirement in the spirit of the Objective column, not merely to the letter.

### Maturity levels and pass thresholds

| Level | Name | Principle |
|---|---|---|
| 0 | Incomplete | No process, not followed, or unsuitable for the objective |
| 1 | Performed | Undocumented or informal process, some evidence it achieves its objective |
| 2 | Managed | Process achieves objectives; documentation and implementation evidence exist |
| 3 | Established | Standard process integrated into the overall system; dependencies documented; sustained use over an extended period |
| 4 | Predictable | Effectiveness continually monitored via key figures with defined limit values |
| 5 | Optimizing | Continual improvement actively advanced by dedicated resources |

- **Target maturity level is 3 for every question**; the maximum result score is 3.0 (lower if questions are n.a.).
- Scores above target are **cut back** to 3 before averaging, so strength in one control cannot offset a gap in another.
- Formal limits on the gap between your result score and the maximum score: more than **10% below → "minor non-conform"**; more than **30% below → "major non-conform"**.

### Assessment objectives (= TISAX labels) and assessment levels

| # | Objective / label | Catalogue(s) | AL |
|---|---|---|---|
| 1 | Info high | Information Security | AL 2 |
| 2 | Info very high | Information Security | AL 3 |
| 3 | Confidential | Information Security | AL 2 |
| 4 | Strictly confidential | Information Security | AL 3 |
| 5 | High availability | Information Security | AL 2 |
| 6 | Very high availability | Information Security | AL 3 |
| 7 | Proto parts | Prototype Protection | AL 3 |
| 8 | Proto vehicles | Prototype Protection | AL 3 |
| 9 | Test vehicles | Prototype Protection | AL 2 |
| 10 | Proto events | Prototype Protection | AL 2 |
| 11 | Data (GDPR Art. 28 processor) | Information Security + Data Protection | AL 2 |
| 12 | Special data (adds GDPR Art. 9) | Information Security + Data Protection | AL 3 |

- "Confidential" and "Strictly confidential" were introduced with the ISA 6 release and selectable **from 1 April 2024**; "Info high" / "Info very high" were selectable only until 31 March 2024. Since **1 January 2025**, *Test vehicles* and *Proto events* are AL 2 rather than AL 3.
- **Label hierarchy** (a superset label automatically confers its subsets): Info high ⊃ Confidential, High availability; Info very high ⊃ Strictly confidential, Very high availability; Strictly confidential ⊃ Confidential; Very high availability ⊃ High availability; Special data ⊃ Data. New subset labels are assigned retroactively.
- **AL 1** — auditor only checks a self-assessment exists; not used in TISAX. **AL 2** — plausibility check of the self-assessment, evidence review, interview with the person in charge of information security, usually by web conference; on-site inspection at the participant's request. **AL 2.5** (informal) — a full *remote* verification, formally recorded as AL 2 but methodologically upgradeable to AL 3. **AL 3** — comprehensive on-site verification: documents and evidence, planned and unplanned interviews, observation of local conditions and process execution. A video-supported remote substitute for AL 3 on-site activities must be recorded as a minor non-conformity and closed out by a follow-up assessment.
- Higher assessment levels satisfy requests for lower ones. Because AL 2 depends on a *plausible* self-assessment, ENX notes internal effort can be higher at AL 2 than at AL 3.

## Assessment, certification and evidence

**Process.** Register participant and scope in the ENX portal → complete the ISA self-assessment → select an ENX-approved audit provider → initial assessment (opening meeting, assessment procedure, closing meeting, report) → optional corrective action plan (CAP) assessment → follow-up assessment(s) → share results.

**Two clocks both start at the closing meeting of the initial assessment:** the **maximum three-year** label validity, and a **nine-month window** to resolve all non-conformities. Miss the nine months and no labels are issued — you start a new initial assessment.

**Findings** are graded per requirement: *major non-conformity* (significant immediate risk, or doubt about overall ISMS effectiveness — needs immediate compensating measures), *minor non-conformity* (isolated or sporadic deficits — corrective action without undue delay), *observation* (no present risk but may create one), *room for improvement*. Overall result is **conform / minor non-conform / major non-conform**. Unaddressed non-conformities always produce "major non-conform"; only an approved CAP moves the result to "minor non-conform".

**Corrective action plans** must state the finding, root cause, corrective actions, implementation date, and compensating measures for critical risks. Implementation periods run from the day the initial assessment concluded and may not exceed **three months without justification, six months without justification plus evidence, or nine months at all**.

**Temporary labels** follow a CAP assessment report rated "minor non-conform"; they are functionally equal to permanent labels but expire with the longest corrective-action implementation period, up to nine months after the initial assessment's closing meeting.

**Report and selective sharing.** The report has five sections of increasing detail — A Assessment Related Information, B Summarized Results, C Assessment result summary (per chapter and catalogue), D Maturity Levels of VDA ISA, E Detailed Assessment Results — and sharing is **cumulative up to a chosen section**, so the participant decides how much detail each partner sees. Selective sharing with a named participant offers six options (A; A + Labels; then B, C, D and E added in turn) and is possible even when the overall result is non-conform. Publishing to the whole exchange platform is limited to A, A + Labels, or A + Labels + B, and only if the overall result is "conform"; ENX recommends "A + Labels" for both. Results usually appear on the exchange platform 5–10 business days after the report is issued. Publication and sharing are **permanent and cannot be revoked**. Labels themselves are visible only in the ENX portal and are not recorded in the report.

**Renewal** is a full re-run every three years against the ISA version current when the assessment is ordered: register a **new** scope (reusing existing location and contact records) before approaching an audit provider. ENX recommends starting the renewal at least one year before the labels expire.

**Governance.** ENX approves audit providers, maintains the audit-provider criteria framework ("TISAX ACAR" — audit provider criteria and assessment requirements) and monitors implementation and result quality; the TISAX Committee is the advisory board that decides on audit-provider approval and is the escalation instance for disputes between a participant and its audit provider over the interpretation of the VDA ISA. An audit provider that has consulted for you can no longer assess you. You may mention that you are pursuing TISAX, but you may not publish the assessment result itself.

## Timeline and status

Status as of September 2026. ISA 6.0.3 is the catalogue in force for every assessment ordered up to 31 December 2026; ISA2027 is published but not yet effective. Participant Handbook 2.8 (13 March 2025) is still the current edition, and ENX had announced no further ISA or TISAX change between 7 August 2026 and today. Nothing here is pending legislative approval — the scheme is contractual, so the only "pending" items are the ISA2027 changeover on 1 January 2027, the ISA 6 cut-off in March 2027 and the ISA2028 release expected in summer 2027.

| Date | Event |
|---|---|
| 28 June 2016 | First TISAX participants register |
| 2019 | ENX Working Group ISA takes over authorship of the catalogue from the VDA |
| 16 October 2023 | ISA 6 (version 6.0.1) published; redline against ISA 5.1.0 dated 15 October 2023 |
| 1 April 2024 | ISA 6 mandatory for all TISAX assessments ordered from this date; "Confidential"/"Strictly confidential" labels replace "Info high"/"Info very high" as selectable objectives |
| 25 April 2024 | ISA 6.0.3 (English) published on the ENX download centre |
| 1 January 2025 | Test vehicles and Proto events move from AL 3 to AL 2 |
| 13 March 2025 | TISAX Participant Handbook v2.8 — still the current edition in September 2026 |
| 29 June 2025 | ENX WG ISA "NIS2 fulfilment through TISAX" coverage analysis published (announced 2 July 2025) |
| 9 December 2025 | ENX reports over 20,000 assessed locations holding valid labels (expanded 18 February 2026) |
| 17 March 2026 | ENX and Auto-ISAC sign a memorandum of understanding on automotive supply-chain cyber risk |
| 1 July 2026 | **VDA ISA2027 published** (workbook cover "Version: 2027", dated 2026-07-01); new year-based versioning and annual release cycle announced |
| 7 August 2026 | ISA2027 webinar series and ISA6.0→ISA2027 redline document released |
| 1 January 2027 | ISA2027 applies to all assessments **ordered** from this date (scope registration date is irrelevant) |
| March 2027 | Last date to **open** an initial assessment under ISA 6 (kick-off date is irrelevant) |
| Summer 2027 | ISA2028 expected, effective for assessments ordered in 2028 |

**What ISA2027 changes.** Year-based versioning; NIST CSF mappings updated from 1.1 to **2.0**, ISO/IEC 27001:2022 mappings refined, ISA/IEC 62443 mappings clarified and pinned to 62443-2-1, **ISO/IEC 27001:2013 references removed**. A formal definition of the phrase "The following aspects are considered" — each listed aspect must be consciously considered and the rationale explainable at assessment. Broader definition of "Project"; clearer separation of events and incidents; managers and organisational leaders named as a dedicated target group for awareness and training. **Supply chain security is strengthened**: organisations with high protection needs must document, review and monitor supplier compliance and evidence including on significant supplier or supply-chain changes; at very high protection needs suppliers are expected to demonstrate adequate security through a TISAX label, an equivalent third-party assessment, or an appropriate supplier audit. **Prototype Protection is restructured** from five control groups into two domains — 8.1 Organizational Requirements (13 questions) and 8.2 Physical and Environmental Security (7) — dropping the old 8.3–8.5, with new controls on traceability and lifecycle tracking of protected vehicles, components and parts, and on their disposal, recycling or return. Annual releases do **not** shorten label validity — three years is unchanged, and organisations will normally skip ISA generations between reassessments.

## Key obligations for security/GRC teams

1. **Get the assessment objective from the customer in writing before anything else.** The objective drives catalogue, applicable requirements, assessment level, cost and on-site effort. Where you must choose, ENX recommends objectives implying AL 3 to avoid re-work. See [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md).
2. **Fix scope by location, and keep the standard scope description.** Model the trade-off between one large scope (one expiry, cheaper central assessment, single point of failure) and several. Consider SGA at three or more locations with a centralised ISMS.
3. **Time the order against the ISA calendar.** Assessments ordered in 2026 run on ISA 6; anything ordered from 1 January 2027 runs on ISA2027, and the last ISA 6 initial assessment must be opened by March 2027. Pull renewal forward or push it back deliberately — do not let the boundary decide for you.
4. **Run the self-assessment as a real gap assessment.** Score each question 0–5, cut back to target 3, and drive the result score to the maximum; anything more than 10% below is already "minor non-conform" territory. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md) and [risk-assessment](../../skills/risk-assessment/SKILL.md).
5. **Build the evidence set to the maturity-3 definition** — a standard, integrated process with documented dependencies and proof of sustained use over time, not a policy PDF. At AL 2 the self-assessment must be conclusive and substantiated on its own. See [control-testing](../../skills/control-testing/SKILL.md) and [audit-preparation](../../skills/audit-preparation/SKILL.md).
6. **Pre-plan the corrective action plan.** Root cause, corrective action, implementation date, compensating measures for critical risks; nothing longer than nine months, justification beyond three, justification plus evidence beyond six. Track residual items through [exception-management](../../skills/exception-management/SKILL.md).
7. **Cascade requirements to your own suppliers.** ISA 6 already requires managing security among contractors; ISA2027 tightens documentation, review and evidence duties and expects label-level assurance from suppliers at very high protection needs. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md) and [vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md).
8. **Treat sharing as irreversible.** Decide per partner how far down report sections A–E they see; a share cannot be withdrawn, and publishing to the whole exchange platform stops at section B and requires a "conform" result. Do not publish the assessment result itself outside the rules ENX sets for writing about TISAX publicly.
9. **Diary the two clocks and the renewal.** Three-year validity and the nine-month non-conformity window both start at the initial assessment's closing meeting; register a new scope at least a year before expiry.
10. **Report label status as a board metric** alongside ISMS maturity by chapter — the ISA spider-web view per chapter is directly reusable. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **ISO/IEC 27001:2022** — the closest neighbour and the usual base. ISA maps to Annex A but is not derived from it, and a certificate is **not** a substitute for a label: TISAX requires its own assessment by an ENX-approved provider. The scope rules differ (see above), so an ISO scope statement rarely transfers unchanged. See [iso-27001-2022.md](iso-27001-2022.md) and [iso27001-readiness](../../skills/iso27001-readiness/SKILL.md).
- **GDPR** — the "Data" and "Special data" objectives assess Article 28 processor duties directly (processing records, DPIAs, transfers including third countries, data-subject requests, breach handling, confidentiality obligations, instructions). A label is evidence toward, not a substitute for, controller due diligence. See [gdpr.md](../regulations/gdpr.md), [dpia-privacy-assessment](../../skills/dpia-privacy-assessment/SKILL.md).
- **NIS 2** — ENX's own working-group analysis (2025) concludes an ISA 6-based TISAX assessment addresses the directive's risk-management, incident-response, supply-chain, governance and technical requirements, and that the three-year cycle is appropriate; national **incident-reporting duties to authorities and CSIRTs are explicitly out of scope** and must be handled separately. See [nis2.md](../regulations/nis2.md), [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
- **NIST CSF 2.0 and NIST SP 800-53 Rev. 5** — ISA2027 replaces ISA 6's CSF 1.1 references with CSF 2.0 subcategory mappings throughout, and both versions point to 800-53 Rev. 5 (alongside BSI-Standard 200-2 and the IT-Grundschutz Compendium) as implementation guidance. Useful as the pivot when an automotive supplier also serves US federal or CSF-aligned customers. See [nist-csf-2.md](nist-csf-2.md), [nist-800-53.md](nist-800-53.md), [control-mapping](../../skills/control-mapping/SKILL.md).
- **ISA/IEC 62443** — ISA references 62443 (62443-2-1 in ISA2027) for the OT-facing controls, reflecting ISA 6's extension of IT-system scope to operational technology. Plant and production environments in scope for a TISAX label should be assessed with the 62443 programme in the same pass. See [iec-62443-ot-security.md](iec-62443-ot-security.md).
- **Vehicle cybersecurity (UN R155 / ISO 21434)** — a different object of assessment. ISA covers the *organisation's* information security, prototype protection and processor duties; it does not address vehicle type-approval cybersecurity. ENX operates a separate **ENX VCS** scheme alongside TISAX: an ISO/SAE 21434-based, ISO/PAS 5112-implementing third-party audit of a supplier's vehicle cybersecurity management system (V-CSMS) against the public ENX VCSA criteria catalogue, yielding an ENX VCS Label. It exists because UN R155 requires manufacturers to demonstrate CSMS effectiveness; a TISAX label does not. See [../regulations/automotive-un-r155-iso-21434.md](../regulations/automotive-un-r155-iso-21434.md).
- **SOC 2** — non-overlapping audience: SOC 2 reports serve US customers of service organisations, TISAX labels serve automotive customers in Europe and increasingly worldwide. Evidence sets overlap heavily; the assurance vehicles do not. See [soc2-tsc.md](soc2-tsc.md).
- **Statement of Applicability** — ISA has no participant-level SoA; applicability is fixed by the assessment objective, which determines exactly which requirement columns and catalogues apply. If you run both regimes, keep the ISO SoA as the master and treat ISA questions as a mapped view. See [statement-of-applicability.md](../../templates/statement-of-applicability.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).

## Primary sources

- TISAX Participant Handbook, version 2.8 (2025-03-13), ENX Association — publisher document, the authoritative process reference: https://www.enx.com/handbook/tisax-participant-handbook.html
- VDA ISA2027 catalogue workbook, cover "Version: 2027", dated 2026-07-01, published by the VDA, © ENX Association — publisher document (control questions, chapter structure, maturity-level definitions, standards mappings, licence): https://www.enx.com/isa2027-en.xlsx
- VDA ISA 6.0.3 catalogue workbook, cover "Version: 6.0.3" — publisher document (ISA 6 control questions, chapter structure, change history): https://www.enx.com/isa6-en.xlsx
- ENX news, "10 Years of TISAX – VDA ISA2027 Released", 2026-07-01 — publisher announcement (ISA2027 content changes, versioning, adoption figures): https://www.enx.com/en-US/news/isa2027/
- ENX news, "ISA2027 Webinar Series and Redline Document available", 2026-08-07 — publisher announcement (ISA2027 transition dates): https://www.enx.com/en-US/news/isa2027-redline/
- ENX TISAX download centre — publisher page (ISA version history and effective dates): https://www.enx.com/en-US/TISAX/downloads/
- ENX ISA overview page — publisher page (catalogue governance, annual cycle): https://www.enx.com/en-US/TISAX/isa/
- ENX TISAX overview page — publisher page (process, labels, three-year validity): https://www.enx.com/en-US/TISAX/
- ENX TISAX FAQs — publisher page (roles, governance, TISAX ACAR, registration fees, temporary labels): https://www.enx.com/en-US/TISAX/faqs/
- ENX news, "TISAX and Cybersecurity in Industry – Expert Analysis Confirms NIS2 Coverage", 2025-07-02 — publisher summary of the ENX WG ISA analysis: https://www.enx.com/en-US/news/TISAX-NIS2/
- ENX news, "20000 TISAX Locations", 2025-12-09 — publisher statistic: https://www.enx.com/en-US/news/20000%20TISAX%20locations/
- ENX news, "Auto-ISAC and ENX Association Align to Collaborate...", 2026-03-17 — joint publisher announcement (memorandum of understanding; assessed-site and country figures): https://www.enx.com/en-US/news/Auto-ISAC-ENX-MoU/
- ENX news index — publisher page used to confirm that no ISA or TISAX change was announced between 7 August 2026 and today: https://www.enx.com/en-US/news/
- ENX VCS overview — publisher page (ISO/SAE 21434 and ISO/PAS 5112 basis, ENX VCSA catalogue, ENX VCS Label, UN R155 driver): https://www.enx.com/en-US/VCS/
- Availability note: ENX announced scheduled maintenance taking the website and portal offline from 19 September 2026 02:00 CEST to 21 September 2026 11:00 CEST, with limited service until 23 September. During that window every URL above except the Participant Handbook returned a maintenance page, so those documents — including both ISA workbooks — were read from archived captures taken between November 2024 and September 2026. Re-check them against the live pages once maintenance ends. **Not retrieved in any form:** the TISAX price list, the Simplified Group Assessment addendum, the TISAX Participation General Terms and Conditions, the full "NIS2 fulfilment through TISAX" analysis PDF, the audit-provider directory, and the VDA's own ISA pages. Fee amounts, the number of approved audit providers and the detailed SGA rules are therefore described only qualitatively here and must be checked against ENX before use.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
