# ISO/IEC 27701 — Privacy Information Management Systems (PIMS)

## At a glance

| Attribute | Detail |
|---|---|
| Full title (current edition) | *Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance* |
| Owner / publisher | ISO/IEC JTC 1/SC 27, prepared in collaboration with CEN/CLC/JTC 13 under the Vienna Agreement; published jointly by ISO and IEC |
| Current version | **ISO/IEC 27701:2025, second edition, 2025-10** (published 14 October 2025). Cancels and replaces ISO/IEC 27701:2019, which it technically revises |
| Headline change | Redrafted as a **stand-alone management system standard**. The only normative reference is ISO/IEC 29100 — ISO/IEC 27001 and 27002 are no longer normative references |
| Structure | Harmonized management system clauses 4–10, clause 11 (guide to the annexes), Annex A (normative controls for PII controllers and PII processors), Annex B (normative implementation guidance) and informative Annexes C–F |
| Who it covers | PII controllers and PII processors of any type or size — public and private companies, government entities, not-for-profits |
| Certifiable? | Yes. Accredited third-party certification; audit and certification requirements are set by **ISO/IEC 27706:2025**, which replaces ISO/IEC TS 27006-2:2021 |
| Transition (UKAS plan) | Accreditation bodies to have transitioned certification bodies by **31 October 2027**; certification bodies to have transitioned all certified clients by **31 October 2028** |
| European adoption | Published in Europe as **EN ISO/IEC 27701:2025** and adopted by CEN/CENELEC members nationally — BSI publishes it as BS EN ISO/IEC 27701:2025 |
| Regulatory status | **Not** an approved GDPR Art. 42 certification mechanism or European Data Protection Seal. Useful accountability evidence, not a legal presumption of conformity |
| Cost | Paid standard — purchase from ISO/IEC or a national member body. Full text is paywalled; only the front matter (foreword, introduction, scope, first terms) is publicly previewable |

## What it is

ISO/IEC 27701 is the international standard for a **privacy information management system (PIMS)** — the management-system wrapper around how an organization processes personally identifiable information (PII). It provides the governance machinery (context, leadership, privacy risk assessment and treatment, competence, documented information, monitoring, internal audit, management review, corrective action) plus a normative control set split by the organization's role as PII controller, PII processor, or both.

The 2019 first edition was explicitly *not* a standalone standard. Its scope read: a PIMS "in the form of an extension to ISO/IEC 27001 and ISO/IEC 27002," applicable to organizations "processing PII within an ISMS." Clause 5 mapped PIMS requirements onto each ISO/IEC 27001:2013 requirement clause; clause 6 onto each ISO/IEC 27002:2013 control; clauses 7 and 8 added controller- and processor-specific guidance. Certification therefore required a certified ISMS underneath. Note that the 2019 edition's normative references were *dated* to ISO/IEC 27001:2013 and 27002:2013 — a persistent friction point once the 2022 editions landed.

The 2025 second edition removes that dependency. Its foreword states the single main change plainly: "the document has been redrafted as a stand-alone management system standard." Its Introduction (0.2) still positions the PIMS to "align or integrate … with other management system standards, and in particular with the information security management system specified in ISO/IEC 27001" — integration is now a choice, not a precondition. Practically, this opens certification to privacy-mature organizations that never pursued ISO/IEC 27001, and lets a controller certify a privacy program whose scope differs from its ISMS scope.

## Who it covers / Scope

- **Applicability test is role-based, not sector- or size-based.** Clause 1 covers PII controllers (including joint controllers) and PII processors (including those using subcontracted processors and those acting as subcontractors to processors), of all types and sizes, public and private.
- **No statutory trigger.** ISO/IEC 27701 is a voluntary standard: nothing compels adoption. It is pulled in by customer contracts, tender requirements, group policy, or a decision to make accountability auditable.
- **Scope is defined by the organization** under clause 4.3 (determining the scope of the PIMS), in the same way ISO/IEC 27001 clause 4.3 works. Scope statements that exclude material processing activities are the most common cause of a certificate being worth less than it appears — read the scope on any vendor certificate before accepting it. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
- **Terminology is ISO, not GDPR.** ISO/IEC 29100 terms apply: *PII* (not "personal data"), *PII principal* (not "data subject"), *PII controller* / *PII processor*. Annex D maps the standard to the GDPR, but the vocabularies are not interchangeable in legal drafting.
- **No extraterritoriality question** — a standard, not a law. Its reach is contractual.

## Structure and requirements

### Management system clauses (2025 edition)

| Clause | Title | Notable content |
|---|---|---|
| 4 | Context of the organization | 4.1 context, 4.2 interested parties, 4.3 PIMS scope, 4.4 the PIMS itself |
| 5 | Leadership | 5.1 leadership and commitment, 5.2 **privacy policy**, 5.3 roles, responsibilities and authorities |
| 6 | Planning | 6.1.1 general, **6.1.2 privacy risk assessment**, **6.1.3 privacy risk treatment**, 6.2 privacy objectives, 6.3 planning of changes |
| 7 | Support | Resources, competence, awareness, communication, documented information (7.5.1–7.5.3) |
| 8 | Operation | 8.1 operational planning and control, 8.2 privacy risk assessment, 8.3 privacy risk treatment |
| 9 | Performance evaluation | 9.1 monitoring/measurement, 9.2 internal audit (incl. 9.2.2 audit programme), 9.3 management review with specified inputs (9.3.2) and results (9.3.3) |
| 10 | Improvement | 10.1 continual improvement, 10.2 nonconformity and corrective action |
| 11 | Further information on annexes | Bridge clause explaining how the annexes are used |

The harmonized structure carries in the Annex SL change on **climate change considerations** in clause 4 (context and interested parties) — UKAS lists "introduced climate change considerations" among the main changes — mirroring Amendment 1:2024 to ISO/IEC 27001:2022, see [iso-27001-2022.md](iso-27001-2022.md).

### Annexes (2025 edition)

| Annex | Status | Content |
|---|---|---|
| A | Normative | PIMS reference control objectives and controls **for PII controllers and PII processors** — consolidated into one annex (2019 kept controllers in Annex A and processors in Annex B) |
| B | Normative | Implementation guidance for PII controllers and PII processors, numbered to mirror Annex A |
| C | Informative | Mapping to ISO/IEC 29100 |
| D | Informative | Mapping to the EU General Data Protection Regulation |
| E | Informative | Mapping to ISO/IEC 27018 and ISO/IEC 29151 |
| F | Informative | Correspondence with ISO/IEC 27701:2019 — the transition workbook |

BSI — the UK member body that publishes BS EN ISO/IEC 27701:2025 — describes the 2025 Annex A as restructured to align with ISO/IEC 27002:2022 and as containing **34 controller controls, 21 processor controls and 31 controls shared by both roles**. Those figures come from BSI's published key-changes page, not from the paywalled standard itself; confirm them against the purchased text before writing a control count into a scope or an applicability statement (verify).

### Control families (verified against the 2019 edition)

The 2019 edition's controller and processor control sets used the same four families, and the 2025 consolidation retains that shape (verify against Annex A):

| Family | Controller controls (2019) | Processor controls (2019) |
|---|---|---|
| Conditions for collection and processing | 8 (purpose, lawful basis, consent mechanics, privacy impact assessment, processor contracts, joint controllers, records of processing) | 6 (customer agreement, organization's own purposes, marketing/advertising use, infringing instruction, customer obligations, records) |
| Obligations to PII principals | 10 (determining/providing information, consent withdrawal, objection, access/correction/erasure, informing third parties, copy of PII, request handling, automated decision making) | 1 (assist the controller in meeting its obligations) |
| Privacy by design and privacy by default | 9 (limit collection, limit processing, accuracy, minimization objectives, de-identification and deletion, temporary files, retention, disposal, transmission controls) | 3 (temporary files; return/transfer/disposal of PII; transmission controls) |
| PII sharing, transfer and disclosure | 4 (basis for cross-border transfer, permitted destinations, records of transfer, records of disclosure to third parties) | 8 (transfer basis, permitted destinations, disclosure records, notification of disclosure requests, legally binding disclosures, subcontractor disclosure, engagement, change of subcontractor) |
| **Total** | **31** | **18** |

The processor set is deliberately thin on principal-facing duties and thick on subcontracting and disclosure — mirroring the controller/processor split in [gdpr.md](../regulations/gdpr.md) Arts. 28–29.

## Assessment, certification and evidence

- **Audit standard:** ISO/IEC 27706:2025, published alongside the 2025 edition on 14 October 2025, is the dedicated standard for bodies auditing and certifying a PIMS. On UKAS's summary it establishes a certifiable framework for PIMS certification bodies, defines competence requirements for PIMS auditors, technical experts and certification decision-makers, strengthens impartiality, independence and governance expectations, and sets audit-duration and scope-determination criteria tailored to controller and processor roles. It is a full International Standard replacing the earlier technical specification ISO/IEC TS 27006-2:2021.
- **Accreditation chain:** national accreditation body (e.g. UKAS, ANAB) → certification body → certified organization. A "27701 certificate" from a body with no accreditation to ISO/IEC 27706 is a marketing artifact; check the accreditation mark and scope.
- **Certificate cycle:** the usual ISO/IEC 17021-1 three-year cycle (stage 1 + stage 2 initial audit, annual surveillance, recertification) applies (verify the body's specific programme).
- **Integrated audits:** where an ISMS exists, the PIMS audit is normally combined with the ISO/IEC 27001 audit. Evidence overlaps heavily — risk methodology, internal audit programme, management review, corrective actions, supplier controls. See [audit-preparation](../../skills/audit-preparation/SKILL.md) and [certification-readiness](../../workflows/certification-readiness.md).
- **Applicability statement:** as with ISO/IEC 27001, expect to justify inclusion and exclusion of Annex A controls by role (controller-only organizations have no obligation against processor controls, and vice versa). Reuse [statement-of-applicability.md](../../templates/statement-of-applicability.md).
- **Standing evidence set:** PII inventory / records of processing, lawful-basis register, consent records, privacy impact assessments, retention and deletion schedules, processor and sub-processor contracts and registers, cross-border transfer bases, PII-principal request logs and SLAs, breach records, privacy training records.

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| August 2019 | ISO/IEC 27701:2019 published — first edition, titled as an extension to ISO/IEC 27001 and ISO/IEC 27002 for privacy information management |
| 2021 | ISO/IEC TS 27006-2:2021 — technical specification for PIMS audit and certification bodies (superseded in 2025) |
| **14 October 2025** | **ISO/IEC 27701:2025 (2nd ed.) and ISO/IEC 27706:2025 published**; European adoption as EN ISO/IEC 27701:2025 follows |
| 1 January 2026 | IAF ceases operations; its functions pass to Global Accreditation Cooperation Incorporated, which commences full operations the same day |
| 18 March 2026 | UKAS publishes its PIMS transition technical bulletin (revision 1 issued 18 August 2026, consolidating gap-analysis forms F659/F660 into a single F659) |
| 1 May 2026 | UKAS assessment of certification bodies against the new standards commences |
| December 2026 | Deadline for UKAS-accredited certification bodies to submit their documented gap analysis |
| 31 October 2027 | UKAS to have transitioned all accredited certification bodies |
| **31 October 2028** | Certification bodies to have transitioned all certified clients; 2019-based certificates cease to be current after this point |

No amendment or corrigendum to ISO/IEC 27701:2025 is reflected in the publisher's preview or in UKAS's August 2026 revision of the transition bulletin, which still cites the standard as published on 14 October 2025. Transition dates are set per accreditation body in line with the consensus of the IAF ICT and Data Security (ICTDS) working group; the dates above are UKAS's published plan — confirm the equivalent plan for your certification body's accreditation body, noting that the International Accreditation Forum ceased operations on 1 January 2026 and its functions passed to Global Accreditation Cooperation Incorporated on that date.

## Key obligations for security/GRC teams

1. **Decide the role(s) first** — controller, processor, joint controller, sub-processor — per processing activity. The role determines which Annex A table applies and is the single most consequential scoping decision. See [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md).
2. **Decide the edition and the integration model.** New programmes should go straight to the 2025 edition as a standalone or ISMS-integrated PIMS; existing 2019 certificate holders should plan the transition audit into a surveillance or recertification slot well before the October 2028 cut-off, using informative Annex F as the gap map.
3. **Build a real PII inventory and records of processing.** Nearly every Annex A control depends on knowing what PII exists, why, on what basis, where it flows and for how long it is kept.
4. **Stand up privacy risk assessment as a distinct discipline** (clauses 6.1.2/6.1.3 and 8.2/8.3). It is not the information security risk assessment with "privacy" appended — impact is on PII principals, not only on the organization. Wire privacy impact assessments to the same process. See [dpia-privacy-assessment](../../skills/dpia-privacy-assessment/SKILL.md) and [dpia-template.md](../../templates/dpia-template.md).
5. **Instrument PII-principal rights end to end** — intake, identity verification, fulfilment, logging, statutory clocks — and measure them; the controller family "Obligations to PII principals" is the largest and the most frequently under-evidenced.
6. **Push controller/processor terms into the supply chain**: processor contracts, sub-processor authorization and change notification, disclosure-request handling, return/deletion at exit. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
7. **Document cross-border transfer bases per destination** and keep transfer and disclosure records; this is where the standard and the transfer rules in [eu-gdpr-international-transfers.md](../regulations/eu-gdpr-international-transfers.md) meet.
8. **Map once, certify many.** Build the crosswalk from the PIMS control set to ISO/IEC 27001 Annex A, SOC 2 privacy criteria and the applicable statutes rather than running parallel programmes. See [control-mapping](../../skills/control-mapping/SKILL.md), [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).

## Interplay

- **ISO/IEC 27001:2022** — no longer a prerequisite, but still the natural host. Shared clauses 4–10 mean one management system, two certificates, one audit programme. See [iso-27001-2022.md](iso-27001-2022.md) and [iso27001-readiness](../../skills/iso27001-readiness/SKILL.md).
- **GDPR** — Annex D maps the standard to the GDPR. Arts. 24(3), 25(3), 28(5) and 32(3) allow adherence to an **approved** Art. 42 certification mechanism to be used as an element in demonstrating compliance or sufficient guarantees; ISO/IEC 27701 is not such a mechanism, so a certificate is ordinary accountability evidence rather than a statutory element. An Art. 42 certification is issued against criteria approved by the competent supervisory authority or the Board (Art. 42(5)), by bodies accredited under Art. 43 by that authority and/or the national accreditation body under EN-ISO/IEC 17065/2012 plus supervisory-authority requirements, for a maximum of three years, renewable (Art. 42(7)). The European Data Protection Seal is Europrivacy — first approved by the EDPB on 10 October 2022 (Opinion 28/2022), with updated criteria approved on 16 April 2026 (Opinion 14/2026) and recognized the same day as a transfer tool under Arts. 42 and 46 (Opinion 15/2026). Never present a 27701 certificate as GDPR certification. See [gdpr.md](../regulations/gdpr.md).
- **ISO/IEC 29100** — the normative reference supplying the privacy framework, terminology and principles; Annex C maps to it. ISO/IEC 29134 (privacy impact assessment guidance) and ISO/IEC 29151 (PII protection code of practice) sit alongside it; Annex E maps to 29151 and to **ISO/IEC 27018** (PII in public clouds acting as PII processors).
- **NIST Privacy Framework** — a parallel, non-certifiable US-origin programme framework. Use the Privacy Framework for structuring and communicating a programme, 27701 when a certificate is the deliverable; contributor crosswalks between them exist but are not validated. See [nist-privacy-framework.md](nist-privacy-framework.md).
- **SOC 2** — the AICPA privacy and confidentiality criteria answer the same buyer question in North American markets; many organizations run SOC 2 for US customers and 27701 for EU/UK/APAC. See [soc2-tsc.md](soc2-tsc.md).
- **National privacy statutes** — the PIMS is the delivery vehicle, the statute sets the substance. Obligations, clocks and penalties come from [gdpr.md](../regulations/gdpr.md), [uk-data-protection.md](../regulations/uk-data-protection.md), [us-state-privacy.md](../regulations/us-state-privacy.md), [brazil-lgpd.md](../regulations/brazil-lgpd.md) and their siblings — not from the standard.
- **AI systems** — privacy risk assessment under clauses 6.1.2/8.2 is the natural hook for PII used in training and inference; pair with the AI governance duties in [eu-ai-act.md](../regulations/eu-ai-act.md).

## Primary sources

- ISO/IEC 27701:2025 official publisher preview (cover page, foreword, introduction, scope, normative references, full table of contents) — fetched: https://cdn.standards.iteh.ai/samples/iso/iso-iec-27701-2025/999f0b4e27d84804be12758c821cc34e/iso-iec-27701-2025.pdf
- ISO/IEC 27701:2019 official publisher preview (cover page, scope, normative references, full table of contents including the clause 7 and 8 control lists) — fetched: https://cdn.standards.iteh.ai/samples/71670/8a8bcac5d3614f63bf02ab5d6cc0c07c/ISO-IEC-27701-2019.pdf
- ISO Online Browsing Platform and ISO catalogue — publisher entries for ISO/IEC 27701:2025 and ISO/IEC 27706:2025; **not fetchable** (iso.org returns 403 to scripted access) and both full texts are paywalled: https://www.iso.org/obp/ui/
- UKAS technical bulletin, *Transition Arrangements for Privacy Information Management Systems (PIMS)*, revision 1 of 18 August 2026 (replacing the 18 March 2026 original) — accreditation-body guidance and the source of the publication date and transition milestones, fetched: https://www.ukas.com/resources/technical-bulletins/transition-arrangements-for-pims/
- Regulation (EU) 2016/679 (GDPR), Arts. 24(3), 25(3), 28(5), 32(3), 42 and 43 — official legal text, fetched: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- EDPB press release of 16 April 2026 and the underlying Opinion 14/2026 on the Europrivacy certification criteria — regulator source, fetched: https://www.edpb.europa.eu/news/news/2026/edpb-brings-clarity-data-processing-scientific-research-speeds-finalisation_en and https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-142026-on-the-europrivacy-certification-criteria_en
- International Accreditation Forum legacy site, confirming IAF ceased operations on 1 January 2026 and the succession to Global Accreditation Cooperation Incorporated — fetched: https://iaf.nu/ and https://globalaccreditationcooperationincorporated.org/
- BSI, *ISO/IEC 27701:2025 — Key Changes and Guidance* — national member body and publisher of BS EN ISO/IEC 27701:2025; the only fetchable source for the 2025 Annex A control counts and for the EN adoption, so both are marked for confirmation above, fetched: https://www.bsigroup.com/en-GB/products-and-services/standards-services/iso-iec-27701-key-changes-and-guidance/

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
