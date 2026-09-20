# ISO 31000:2018 and ISO/IEC 27005:2022 — risk management and information security risk management

## At a glance

| Attribute | Detail |
|---|---|
| Documents covered | **ISO 31000:2018** *Risk management — Guidelines* (second edition, 2018-02) and **ISO/IEC 27005:2022** *Information security, cybersecurity and privacy protection — Guidance on managing information security risks* (fourth edition, 2022-10) |
| Publishers / committees | ISO/TC 262 *Risk management* (ISO 31000, ISO 31073, ISO 31022, ISO 31030, ISO/TS 31050); IEC TC 56 *Dependability* with ISO/TC 262 for IEC 31010 (double-logo standard); ISO/IEC JTC 1/SC 27 for ISO/IEC 27005 |
| Nature | **Guidance, not requirements.** Neither document contains auditable "shall" clauses; both are written as guidelines |
| Certifiable? | **No.** Certification in this family is against ISO/IEC 27001:2022, whose clauses 6.1.2, 6.1.3, 8.2 and 8.3 carry the mandatory risk requirements |
| Who it applies to | ISO 31000: any organization, any activity, "not industry or sector specific" (Clause 1). ISO/IEC 27005: "all organizations, regardless of type, size or sector" (Clause 1) |
| ISO 31000 structure | Clause 4 Principles (8 principles) → Clause 5 Framework (5.1–5.7) → Clause 6 Process (6.1–6.7) |
| ISO/IEC 27005 structure | Clauses 5–10 (risk management, context, assessment, treatment, operation, leveraging ISMS processes) + one informative Annex A of example techniques |
| Vocabulary | ISO 31073:2022 *Risk management — Vocabulary* (first edition, 2022-02, ISO/TC 262). Definitions in both ISO 31073 and ISO/IEC 27005 are attributed `[SOURCE: ISO Guide 73:2009, …]` |
| Techniques catalogue | IEC 31010:2019 (second edition; replaced the 2009 first edition), Annex A categorization + Annex B descriptions in ten technique families |
| Cost | All texts are paid ISO/IEC publications; only cover, foreword, contents and opening clauses are available as publisher previews |

## What it is

**ISO 31000:2018** is the generic, sector-neutral umbrella standard for managing risk. It states the purpose of risk management as "the creation and protection of value" and organizes the discipline into three components — principles, framework and process (Figure 1). It defines risk as the "effect of uncertainty on objectives", explicitly two-sided: an effect "can be positive, negative or both, and can address, create or result in opportunities and threats" (3.1). The second edition cancelled and replaced ISO 31000:2009 and shifted emphasis onto integration into governance and decision-making, leadership accountability, and the iterative nature of the process.

**ISO/IEC 27005:2022** is the information-security-specific companion. Its Introduction states that it gives guidance on implementing the information security risk requirements of ISO/IEC 27001, on the actions that address risks (ISO/IEC 27001:2022, 6.1 and Clause 8), and on implementing ISO 31000's risk management guidance in the information security context; it supplements ISO/IEC 27003. The fourth edition cancelled and replaced ISO/IEC 27005:2018 and, per its foreword, (a) aligned all guidance text with ISO/IEC 27001:2022 and ISO 31000:2018, (b) aligned terminology with ISO 31000:2018, (c) adjusted the clause structure to the layout of ISO/IEC 27001:2022, (d) introduced risk scenario concepts, (e) contrasted the **event-based** approach with the **asset-based** approach to risk identification, and (f) restructured the former annexes into a single annex.

Together they form the layer the certifiable standards assume but do not supply: ISO/IEC 27001 tells you that you *shall* have a risk assessment and treatment process producing consistent results; ISO 31000 supplies the governance frame; ISO/IEC 27005 supplies the method; IEC 31010 supplies the techniques.

## Who it covers / Scope

- **No applicability test, no thresholds, no exemptions** — these are voluntary guidance documents. Obligation arises only by reference: from ISO/IEC 27001 certification, from a contract, or from a regulator that requires a documented risk-management framework (see Interplay).
- ISO 31000 Clause 1: guidelines for managing risk faced by organizations, customizable to any organization and context, usable "throughout the life of the organization" and applicable "to any activity, including decision-making at all levels". It has **no normative references**.
- ISO/IEC 27005 Clause 1: assists organizations to fulfil ISO/IEC 27001 requirements concerning actions to address information security risks and to perform risk assessment and treatment activities. Its only normative reference is ISO/IEC 27000.
- Intended users named in the ISO/IEC 27005 Introduction: organizations establishing or improving an ISMS per ISO/IEC 27001, and persons performing or involved in information security risk management (ISMS professionals, risk owners, other interested parties).
- Nothing in either document can be "complied with" in an audit sense. Statements of conformity are made against ISO/IEC 27001 — see [iso-27001-2022.md](iso-27001-2022.md).

## Structure and requirements

### ISO 31000:2018 — the eight principles (Clause 4)

| # | Principle | Official gloss (condensed) |
|---|---|---|
| a | Integrated | Risk management is an integral part of all organizational activities |
| b | Structured and comprehensive | A structured, comprehensive approach contributes to consistent and comparable results |
| c | Customized | Framework and process are customized and proportionate to the organization's external and internal context related to its objectives |
| d | Inclusive | Appropriate and timely involvement of stakeholders lets their knowledge, views and perceptions be considered |
| e | Dynamic | Risks emerge, change and disappear as context changes; risk management anticipates, detects, acknowledges and responds in a timely manner |
| f | Best available information | Inputs are historical, current and forward-looking; limitations and uncertainties are made explicit; information is timely, clear and available |
| g | Human and cultural factors | Human behaviour and culture significantly influence all aspects at every level and stage |
| h | Continual improvement | Risk management is continually improved through learning and experience |

### ISO 31000:2018 — framework (Clause 5) and process (Clause 6)

| Clause | Title | Substance |
|---|---|---|
| 5.2 | Leadership and commitment | Top management and oversight bodies customize and implement the framework, issue a risk management statement or policy, allocate resources, assign authority/responsibility/accountability. **"Top management is accountable for managing risk while oversight bodies are accountable for overseeing risk management."** Includes establishing "the amount and type of risk that may or may not be taken" to guide risk criteria |
| 5.3 | Integration | Risk is managed in every part of the structure; "everyone in an organization has responsibility for managing risk" |
| 5.4 | Design | 5.4.1 understanding the organization and its context; 5.4.2 articulating risk management commitment; 5.4.3 assigning roles, authorities, responsibilities and accountabilities; 5.4.4 allocating resources; 5.4.5 establishing communication and consultation |
| 5.5–5.7 | Implementation, Evaluation, Improvement | Implement the framework; evaluate it against its purpose and plans; 5.7.1 adapting and 5.7.2 continually improving |
| 6.2 | Communication and consultation | Runs alongside the whole process, not a stage of it |
| 6.3 | Scope, context and criteria | 6.3.2 defining the scope; 6.3.3 external and internal context; 6.3.4 defining risk criteria |
| 6.4 | Risk assessment | 6.4.2 risk identification; 6.4.3 risk analysis; 6.4.4 risk evaluation |
| 6.5 | Risk treatment | 6.5.2 selection of treatment options; 6.5.3 preparing and implementing risk treatment plans |
| 6.6 / 6.7 | Monitoring and review / Recording and reporting | The two activities most often skipped, and the two that generate the audit evidence |

### ISO/IEC 27005:2022 — clause map

| Clause | Title | Notes |
|---|---|---|
| 5.1 / 5.2 | Risk management process / cycles | Process is iterative with two named decision points; 5.2 splits maintenance into a **strategic cycle** (long interval or on major context change) and an **operational cycle** (shorter, scenario-level review and update) |
| 6.1–6.3 | Context establishment | 6.1 organizational considerations (mapped to ISO/IEC 27001:2022, 4.1); 6.2 identifying basic requirements of interested parties; 6.3 applying risk assessment |
| 6.4 | Establishing and maintaining risk criteria | 6.4.2 **risk acceptance criteria**; 6.4.3 **criteria for performing risk assessments** — the same two criteria sets ISO/IEC 27001 6.1.2 a) requires |
| 6.5 | Choosing an appropriate method | Method selection is an explicit, documented decision, not a default |
| 7.2 | Identifying risks | 7.2.1 identifying and describing information security risks (event-based vs asset-based); 7.2.2 identifying risk owners |
| 7.3 | Analysing risks | 7.3.2 assessing potential consequences; 7.3.3 assessing likelihood; 7.3.4 determining the levels of risk |
| 7.4 | Evaluating risks | 7.4.1 comparing results with the risk criteria; 7.4.2 prioritizing analysed risks for treatment |
| 8.2–8.3 | Treatment options and controls | 8.2 selecting treatment options; 8.3 determining **all** controls necessary to implement them |
| 8.4–8.5 | Reconciliation with ISO/IEC 27001 | 8.4 comparing the determined controls with those in ISO/IEC 27001:2022, Annex A; 8.5 producing a Statement of Applicability |
| 8.6 | Risk treatment plan | 8.6.1 formulation; 8.6.2 approval by risk owners; 8.6.3 acceptance of residual risks |
| 9.1 / 9.2 | Operation | Performing the information security risk assessment process and the risk treatment process — the counterparts of the ISO/IEC 27001:2022 clauses 8.2 and 8.3 of the same titles |
| 10 | Leveraging related ISMS processes | 10.1 context; 10.2 leadership and commitment; 10.3 communication and consultation; 10.4 documented information (10.4.2 about processes, 10.4.3 about results); 10.5 monitoring and review (10.5.2 factors influencing risks); 10.6 management review; 10.7 corrective action; 10.8 continual improvement |
| Annex A | Informative | "Examples of techniques in support of the risk assessment process" — the single annex that replaced the 2018 edition's several annexes |

Every activity in Clauses 7–10 (outside general subclauses) is written to a fixed five-part template: **Input → Action → Trigger → Output → Guidance.** The "Trigger" element is the underused one: it is where re-assessment conditions (change in the organization, plan, or external context) are defined, which is what turns an annual assessment into a live one.

### Risk treatment options

ISO/IEC 27005 3.2.7 lists treatment as: avoiding the risk by not starting or continuing the activity; taking or increasing risk to pursue an opportunity; removing the risk source; changing the likelihood; changing the consequences; sharing the risk with other parties (including contracts and risk financing); and retaining the risk by informed decision. **Note 2 excludes "taking or increasing risk to pursue an opportunity" from information security risk treatment**, while allowing it in general risk management — a real difference between the 31000 and 27005 worlds. Risk sharing (3.2.9) notes that legal or regulatory requirements can limit, prohibit or mandate sharing and that "risk transfer is a form of risk sharing"; risk retention (3.2.10) is defined as *temporary* acceptance.

### Terminology that auditors hold you to

| Term | Definition (ISO/IEC 27005:2022 Clause 3 / ISO 31073:2022) |
|---|---|
| Risk | Effect of uncertainty on objectives (ISO 31000 3.1; 27005 restricts the two-sided note to "positive or negative" and adds information-security notes) |
| Risk criteria | Terms of reference against which the significance of a risk is evaluated; based on objectives and external/internal context; can derive from standards, laws and policies |
| Risk owner | Person or entity with the **accountability and authority** to manage a risk |
| Risk scenario | Sequence or combination of events leading from the initial cause to the unwanted consequence |
| Risk acceptance | Informed decision to take a particular risk; can occur without treatment; accepted risks remain subject to monitoring and review |
| Risk evaluation | Comparing risk analysis results with risk criteria to decide whether the risk and/or its significance is acceptable or tolerable |

More terms: [../glossary.md](../glossary.md). Scoring mechanics and the ordinal-arithmetic traps that break "consistent, valid and comparable results": [../risk-scoring.md](../risk-scoring.md).

## Assessment, certification and evidence

- **Nothing to certify.** There is no ISO 31000 or ISO/IEC 27005 certificate for an organization. Claims of "ISO 31000 certified" are a red flag in vendor due diligence — see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
- **The auditable surface is ISO/IEC 27001:2022.** Clause 6.1.2 requires a defined and applied risk assessment process that: a) establishes and maintains risk criteria including risk acceptance criteria and criteria for performing assessments; b) ensures repeated assessments "produce consistent, valid and comparable results"; c) identifies risks associated with loss of confidentiality, integrity and availability within ISMS scope, and identifies risk owners; d) analyses risks (consequences, realistic likelihood, levels of risk); e) evaluates risks against the criteria and prioritizes them for treatment. Clause 6.1.3 requires selecting treatment options, determining **all** necessary controls, comparing them with Annex A so no necessary control is omitted, producing a Statement of Applicability (necessary controls, justification for inclusion, implementation status, justification for any Annex A exclusion), formulating a risk treatment plan, and obtaining **risk owners' approval of the plan and acceptance of the residual risks**. Documented information must be retained about both processes. Clauses 8.2 and 8.3, sitting under Clause 8 *Operation*, carry the same two topics — information security risk assessment and information security risk treatment — into ISMS operation. ISO/IEC 27001:2022 6.1.3 NOTE 4 states the process "aligns with the principles and generic guidelines provided in ISO 31000".
- **Evidence set:** methodology document (naming the chosen method per 27005 6.5), both criteria sets, risk register with owners and rationale, treatment plan, SoA, dated risk-owner approvals and residual-risk acceptances, re-assessment triggers, monitoring records. Templates: [../../templates/risk-register-guide.md](../../templates/risk-register-guide.md), [../../templates/statement-of-applicability.md](../../templates/statement-of-applicability.md). Preparation: [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).
- **Technique selection** comes from IEC 31010:2019, whose Annex B groups techniques into ten families: B.1 eliciting views from stakeholders and experts; B.2 identifying risk; B.3 determining sources, causes and drivers; B.4 analysing controls; B.5 understanding consequences and likelihood; B.6 analysing dependencies and interactions; B.7 providing a measure of risk; B.8 evaluating the significance of risk; B.9 selecting between options; B.10 recording and reporting (including risk registers and the consequence/likelihood matrix). Annex A Table A.3 maps applicability of techniques to the ISO 31000 process.

## Timeline and status (as of September 2026)

| Document | Edition / date | Status |
|---|---|---|
| ISO 31000:2018 | Second edition, 2018-02; cancelled and replaced ISO 31000:2009 | Current; **no revised edition and no amendment** in member-body catalogue records as of September 2026. ISO/TC 262 lists "Development of Framework and Design Specification for the revision of ISO 31000" among its projects in progress, and a committee news item of 19 August 2024 describes a task group weighing an update; no revision appears on the committee's "standards under development" list and no target date is published |
| IEC 31010:2019 | Second edition (2019); cancelled and replaced the 2009 first edition; technical revision (more detail on planning/implementing/verifying technique use, more techniques, ISO 31000 concepts no longer repeated) | Current |
| ISO 31073:2022 | First edition, 2022-02 | Current TC 262 vocabulary standard. Its definitions still cite ISO Guide 73:2009 as source, although Guide 73 itself was withdrawn on 2 November 2023 (ISO member-body catalogue record; the iso.org catalogue page was not retrievable) |
| ISO 31022:2020 | First edition, 2020-05 — legal risk management | Current |
| ISO/TS 31050:2023 | First edition, 2023-10 — managing an emerging risk to enhance resilience | Current Technical Specification |
| ISO/IEC 27005:2022 | Fourth edition, 2022-10; cancelled and replaced ISO/IEC 27005:2018 | Current; no later edition and no amendment in member-body catalogue records as of September 2026 |
| ISO/IEC 23894:2023 | First edition, 2023-02 — AI risk management guidance | Current; the AI-specific analogue built on the ISO 31000 structure |
| ISO/IEC 27001:2022 | Third edition, 2022-10 | The certifiable anchor; amended by ISO/IEC 27001:2022/Amd 1:2024 *Climate action changes* (February 2024) — see [iso-27001-2022.md](iso-27001-2022.md) |

## Key obligations for security/GRC teams

1. **Write the method down before scoring anything.** ISO/IEC 27005 6.5 makes method choice explicit; ISO/IEC 27001 6.1.2 b) makes repeatability auditable. See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md).
2. **Set both criteria sets separately** — risk acceptance criteria (27005 6.4.2) and criteria for performing assessments (6.4.3). A single "risk appetite" sentence satisfies neither.
3. **Anchor the scales.** "Consistent, valid and comparable results" is the requirement that unanchored High/Medium/Low scoring fails; calibrate against [../risk-scoring.md](../risk-scoring.md).
4. **Name a risk owner with accountability *and* authority** for every register entry (27005 3.1.5, 7.2.2) — not a team mailbox. Register structure: [../../templates/risk-register-guide.md](../../templates/risk-register-guide.md).
5. **Decide event-based or asset-based identification per scope, and say which.** Asset-based inventories scale badly and miss cross-system scenarios; event-based scenario work misses unmanaged assets. Many programs run asset-based for infrastructure scope and event-based for business-service scope.
6. **Run treatment as 27005 8.3 → 8.4 → 8.5:** determine the controls you actually need first, *then* reconcile against ISO/IEC 27001 Annex A, then write the SoA. Deriving controls from Annex A first inverts the standard and produces an SoA no risk decision supports.
7. **Capture residual-risk acceptance as a dated decision by the risk owner** (27005 8.6.2–8.6.3; 27001 6.1.3 f). Where a control is not implemented, route it through [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md) rather than silently accepting.
8. **Define re-assessment triggers, not just an annual date** — use the 27005 "Trigger" element and the 5.2 strategic/operational cycle split; feed regulatory change from [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).
9. **Report risk to the governing body in the framework's own terms:** top management accountable for managing risk, oversight body accountable for overseeing it (ISO 31000 5.2). See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md) and [../../templates/grc-board-report.md](../../templates/grc-board-report.md).
10. **Keep documented information about processes and about results separately** (27005 10.4.2 / 10.4.3) — auditors ask for both and most programs only have the second.

## Interplay

- **ISO/IEC 27001:2022** — the requirements layer; ISO/IEC 27005 is its method layer and 31000 its governance frame. See [iso-27001-2022.md](iso-27001-2022.md) and [../../skills/iso27001-readiness/SKILL.md](../../skills/iso27001-readiness/SKILL.md).
- **NIST lineage** — NIST SP 800-30 Rev. 1, *Guide for Conducting Risk Assessments* (September 2012), and the NIST Risk Management Framework built around it form the parallel US-federal tradition: same decomposition (threat source, threat event, vulnerability, likelihood, impact), different vocabulary and a control-catalogue-first orientation. NIST CSF 2.0's Govern and Identify functions cover much of what ISO 31000 Clause 5 covers — see [nist-csf-2.md](nist-csf-2.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md). The RMF and SP 800-30 in detail: [nist-rmf-800-37-800-30.md](nist-rmf-800-37-800-30.md).
- **FAIR** — quantitative loss-exposure modelling; compatible with, not an alternative to, 27005: FAIR is a technique you plug into 7.3 analysis. See [fair-cyber-risk-quantification.md](fair-cyber-risk-quantification.md) and [../risk-scoring.md](../risk-scoring.md).
- **COSO ERM (*Enterprise Risk Management — Integrating with Strategy and Performance*, 2017)** — the enterprise/financial-reporting lineage, organized into five interrelated components supported by twenty principles (June 2017 executive summary). Where both exist, map cyber risk into the enterprise taxonomy rather than maintaining two disconnected registers; see [coso-internal-control-erm.md](coso-internal-control-erm.md) and [../regulations/sox-itgc.md](../regulations/sox-itgc.md).
- **Regulatory demands for a risk-management framework** — DORA requires financial entities to hold a documented ICT risk-management framework ([../regulations/dora.md](../regulations/dora.md)) and NIS2 requires all-hazards risk-management measures ([../regulations/nis2.md](../regulations/nis2.md)); both are satisfiable with a 27005-shaped process, but neither accepts adherence to the standard as evidence on its own.
- **TC 262 siblings** — ISO 31022:2020 (legal risk) and ISO/TS 31050:2023 (emerging risk) extend the same principles/framework/process spine; ISO/IEC 23894:2023 does the same for AI, useful alongside [iso-42001-ai-management.md](iso-42001-ai-management.md), [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md) and [../regulations/eu-ai-act.md](../regulations/eu-ai-act.md).
- **Control mapping** — ISO/IEC 27005 8.4 is the only place in this family where a control catalogue enters, and only as a completeness check. See [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).

## Primary sources

- ISO 31000:2018 publisher preview (cover, foreword, contents, Clauses 1–5.3 including the eight principles): `https://cdn.standards.iteh.ai/samples/65694/60673072317a4b96bd36efb910b68926/ISO-31000-2018.pdf` — retrieved.
- ANSI/ASSP/ISO 31000-2018 preview (identical US adoption; foreword, full contents, Clauses 1–3): `https://www.assp.org/docs/default-source/standards-documents/preview/31000_2018_wms_preview.pdf` — retrieved.
- ISO/IEC 27005:2022 publisher preview (cover, foreword incl. list of changes, introduction, Clauses 1–6.1, full contents): `https://cdn.standards.iteh.ai/samples/80585/7bca93ac16fd426a9bc717cadc9284d9/ISO-IEC-27005-2022.pdf` — retrieved.
- ISO/IEC 27001:2022 publisher preview (Clauses 6.1.2, 6.1.3, 6.2, 6.3 and full contents): `https://cdn.standards.iteh.ai/samples/82875/726bcf58250e43d9a666b4d929c8fbdb/ISO-IEC-27001-2022.pdf` — retrieved.
- ANSI/ASSP/ISO/IEC 31010-2019 preview (foreword, changes from the 2009 edition, full contents incl. Annex A/B structure): `https://www.assp.org/docs/default-source/standards-documents/preview/31010_2019_wms_preview.pdf` — retrieved.
- ISO 31073:2022 publisher preview (cover, foreword, introduction, Clause 3 terms): `https://cdn.standards.iteh.ai/samples/79637/fdad1b37b1904a48aa640dd57a7d7619/ISO-31073-2022.pdf` — retrieved.
- ISO 31022:2020, ISO/TS 31050:2023 and ISO/IEC 23894:2023 publisher previews (covers and edition dates): `https://cdn.standards.iteh.ai/samples/69295/e6975e479d6149f0afb157c0d1e87715/ISO-31022-2020.pdf`, `https://cdn.standards.iteh.ai/samples/54224/c9150993cfd84591aed5153965c11cd8/ISO-TS-31050-2023.pdf`, `https://cdn.standards.iteh.ai/samples/77304/cb803ee4e9624430a5db177459158b24/ISO-IEC-23894-2023.pdf` — retrieved.
- ISO/TC 262 committee site, About, Projects and News pages (standards portfolio; revision work in progress on ISO 31000; 19 August 2024 news item on a task group to advance ISO 31000): `https://committee.iso.org/home/tc262`, `https://committee.iso.org/sites/tc262/home/projects.html` and `https://committee.iso.org/sites/tc262/home/news.html` — retrieved (the site carries an ISO disclaimer that it is maintained by a third party).
- NIST SP 800-30 Rev. 1 publication record (title and September 2012 publication date): `https://csrc.nist.gov/pubs/sp/800/30/r1/final` — retrieved.
- COSO, *Enterprise Risk Management — Integrating with Strategy and Performance*, Executive Summary, June 2017 (five components, twenty principles): `https://www.coso.org/guidance-erm` and `https://www.coso.org/_files/ugd/3059fc_61ea5985b03c4293960642fdce408eaa.pdf` — retrieved.
- Catalogue records of an ISO member body (Estonian Centre for Standardisation) used for publication dates, validity and amendment history where iso.org was unreachable — ISO 31000:2018 valid from 14.02.2018; ISO 31073:2022 from 15.02.2022; ISO/IEC 27005:2022 from 25.10.2022; ISO/IEC 27001:2022 from 25.10.2022 with Amd 1:2024 *Climate action changes* from 23.02.2024; EVS-EN IEC 31010:2019 from 02.09.2019; ISO Guide 73:2009 withdrawn from 02.11.2023: `https://www.evs.ee/en/iso-31000-2018`, `https://www.evs.ee/en/iso-iec-27005-2022`, `https://www.evs.ee/en/iso-iec-27001-2022-amd-1-2024` and `https://www.evs.ee/en/iso-guide-73-2009` — retrieved.
- ISO catalogue entries on `https://www.iso.org` (e.g. `standard/65694` for ISO 31000, `standard/80585` for ISO/IEC 27005) and the ISO Online Browsing Platform — **not accessible** (HTTP 403); publisher-side status fields could not be read directly.
- Full normative text of all standards above is paywalled; clause content beyond the preview pages has not been independently verified.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
