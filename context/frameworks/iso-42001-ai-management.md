# ISO/IEC 42001:2023 — Artificial Intelligence Management System (AIMS)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | ISO/IEC 42001:2023, *Information technology — Artificial intelligence — Management system*, first edition (edition 1.0; still listed as published by the co-publisher) |
| Publisher / committee | ISO and IEC jointly; prepared by ISO/IEC JTC 1/SC 42 (Artificial intelligence). ICS 35.020, 03.100.70 |
| Published | 18 December 2023 — the first certifiable international AI management system standard |
| Structure | Harmonized structure (HS) clauses 4–10 + Annex A (normative, reference control objectives and controls) + Annex B (normative, implementation guidance for AI controls) + Annex C (informative, AI-related organizational objectives and risk sources) + Annex D (informative, use across domains or sectors) |
| Annex A size | 9 control objectives (A.2–A.10); 38 controls — the count matches the 38 distinct controls enumerated in NIST's AI RMF-to-ISO/IEC 42001 crosswalk, but Annex A itself is paywalled *(verify)* |
| Who it covers | Any organization, of any size, type or nature, that **provides or uses** products or services utilizing AI systems |
| Certifiable? | Yes — third-party certification against clauses 4–10; certification bodies are governed by ISO/IEC 42006:2025 (published 7 July 2025), which supplements ISO/IEC 17021-1 |
| Normative reference | ISO/IEC 22989:2022 (AI concepts and terminology) supplies the vocabulary |
| Distinguishing requirements | **AI system impact assessment** (clauses 6.1.4 and 8.4) and a **Statement of Applicability** for Annex A — the impact assessment looks outward, at effects on individuals, groups and societies |
| Cost | Paywalled; full text purchased from ISO/IEC or a national member body. Free previews cover foreword, contents, scope, terms and part of clause 4 |
| Relationship to EU AI Act | Supports but does not satisfy Art. 17 quality management system. The first harmonised European standard for that purpose, **EN 18286:2026**, was published in July 2026 |

## What it is

ISO/IEC 42001 is a management system standard (MSS), not a technical AI standard. It specifies requirements for establishing, implementing, maintaining and continually improving an AI management system "within the context of an organization," and it is deliberately built on the same harmonized structure — identical clause numbers, titles and core definitions — used by ISO/IEC 27001, ISO 9001 and the rest of the MSS family. The standard's own Introduction makes that reuse explicit: the common approach "facilitates implementation and consistency with other management system standards, e.g. related to quality, safety, security and privacy." In practice that means an organization with a working ISMS already owns most of clauses 4, 5, 7, 9 and 10 and is adding AI-specific content to clauses 6 and 8 plus a new control set.

What makes it AI-specific is the object of control. The Introduction names three characteristics that justify management beyond classical IT: automated decision-making that can be non-transparent and non-explainable; systems derived from data and machine learning rather than human-coded logic; and continuously-learning systems that change behaviour during use. Clause 4.1 requires the organization to determine **its role** with respect to each AI system — AI provider, AI producer, AI customer, AI partner, AI subject, or relevant authority — because role determines which requirements and controls apply and how far. The standard also avoids prescribing management processes: it expects the organization to combine "generally accepted frameworks, other International Standards and its own experience" for risk management, life cycle management and data quality.

The standard sits in a family. ISO/IEC 23894:2023 (published 6 February 2023) gives AI risk-management guidance built on the ISO 31000 process; ISO/IEC 42005:2025 (published 28 May 2025) gives guidance for AI system impact assessments and includes an informative Annex A on use with ISO/IEC 42001, Annex B on use with ISO/IEC 23894, a harms-and-benefits taxonomy (Annex C), guidance on aligning with other assessments (Annex D) and an example assessment template (Annex E). ISO/IEC 42006:2025 governs the auditors. Supporting standards include ISO/IEC 22989 (concepts and terminology), ISO/IEC 38507 (governance implications of AI use by organizations) and ISO/IEC 5338:2023 (AI system life cycle processes) *(titles of the latter two taken from national-adoption catalogue listings, not from ISO)*.

## Who it covers / Scope

- **Applicability is self-declared, not triggered by law.** Clause 1 states the document "is applicable to any organization, regardless of size, type and nature, that provides or uses products or services that utilize AI systems." There is no threshold, no sector test and no extraterritorial hook — adoption is voluntary, and scope is whatever the organization sets under clause 4.3.
- **Scope must be documented** (4.3) and must cover the organization's activities with respect to the requirements on the AI management system, leadership, planning, support, operation, performance evaluation, improvement, controls and objectives. A scope narrowed to one product line is legitimate; a certificate then only evidences that scope, which is the single most important thing to read on someone else's certificate.
- **Role, not size, drives depth.** Organizations that only *use* third-party AI can justify excluding much of the development-oriented Annex A content; providers and producers cannot.
- **Climate change is an explicit context input** (4.1): the organization "shall determine whether climate change is a relevant issue," and interested parties can have climate-related requirements (4.2 Note) — both sit in the published 2023 text.

## Structure and requirements

| Clause | Requirement content |
|---|---|
| 4 Context | 4.1 external/internal issues, intended purpose of AI systems and the organization's roles; 4.2 interested parties and their requirements; 4.3 documented AIMS scope; 4.4 establish, implement, maintain, continually improve and document the AIMS |
| 5 Leadership | 5.1 top-management commitment; 5.2 documented **AI policy**; 5.3 roles, responsibilities and authorities |
| 6 Planning | 6.1.1 actions to address risks and opportunities; **6.1.2 AI risk assessment**; **6.1.3 AI risk treatment** (drives the Statement of Applicability); **6.1.4 AI system impact assessment**; 6.2 AI objectives and planning to achieve them; 6.3 planning of changes |
| 7 Support | 7.1 resources; 7.2 competence; 7.3 awareness; 7.4 communication; 7.5 documented information (creation, update, control) |
| 8 Operation | 8.1 operational planning and control; 8.2 AI risk assessment (performed); 8.3 AI risk treatment (implemented); 8.4 AI system impact assessment (performed) |
| 9 Performance evaluation | 9.1 monitoring, measurement, analysis, evaluation; 9.2 internal audit and internal audit programme; 9.3 management review — inputs and results specified |
| 10 Improvement | 10.1 continual improvement; 10.2 nonconformity and corrective action |

**Key defined terms** (clause 3) that change how auditors read the system:

- *AI system impact assessment* (3.24): "formal, documented process by which the impacts on individuals, groups of individuals, or both, and societies are identified, evaluated and addressed" — note that the object is impacts on **others**, not risk to the organization.
- *Statement of applicability* (3.26): "documentation of all necessary controls and justification for inclusion or exclusion of controls." Note 1 confirms an organization "may not require all controls listed in Annex A or may even exceed the list … with additional controls established by the organization itself"; Note 2 requires all identified risks and their controls to be reflected in the SoA.
- *Governing body* (3.22, from ISO/IEC 38500) sits alongside *top management* (3.3) — the standard anticipates board-level accountability distinct from executive management.

**Annex A control objectives** — the reference set an organization accepts or excludes in its SoA. The themes below track the Annex B control titles enumerated in NIST's crosswalk to ISO/IEC 42001; the exact Annex A objective wording sits in the paywalled text *(verify)*:

| Objective | Theme |
|---|---|
| A.2 | Policies related to AI |
| A.3 | Internal organization (roles, responsibilities, reporting of concerns) |
| A.4 | Resources for AI systems (data, tooling, compute, human resources) |
| A.5 | Assessing impacts of AI systems |
| A.6 | AI system life cycle (objectives, requirements, design, development, verification, deployment, operation, monitoring, documentation, event logging) |
| A.7 | Data for AI systems (acquisition, quality, provenance, preparation) |
| A.8 | Information for interested parties of AI systems |
| A.9 | Use of AI systems (processes and objectives for responsible use, intended use) |
| A.10 | Third-party and customer relationships |

Annex B is **normative** and gives per-control implementation guidance (pages 21–45 of the standard — roughly half the document); treat it as part of the requirement set, not as commentary. Annex C lists potential AI-related organizational objectives and risk sources and is a good starting inventory for a first AI risk register. Annex D addresses use of the AIMS across domains or sectors and integration with other management systems.

## Assessment, certification and evidence

- **Certification is against clauses 4–10.** Annex A controls are not individually mandatory; the auditable artefact is the SoA justifying inclusion and exclusion. See [statement-of-applicability.md](../../templates/statement-of-applicability.md).
- **ISO/IEC 42006:2025** (first edition, published 7 July 2025) sets additional requirements to ISO/IEC 17021-1 for AIMS certification bodies: impartiality and conflicts of interest (5.2), liability and financing (5.3), generic and specific technical competence for personnel (7.1.2, 7.1.3), demonstration of knowledge and experience (7.2.2), AIMS certification documents (8.2.2), access to the organization's documentation (8.4.2), audit stages and surveillance/re-certification (9.3–9.6), and a **normative Annex A on audit time** with worked examples in Annex B and a certification-document template in Annex C. Its practical effect is to constrain how little audit time a certification body may sell.
- **Accreditation matured through 2025–2026.** UKAS granted BSI the first UK accreditation for ISO/IEC 42001 certification on **15 January 2026**, following a pilot programme; on its August 2026 update UKAS records the pilot as concluded, applications open and AIMS assessments running through its normal route, with ISO/IEC 42006:2025 supplying the additional competence requirements alongside ISO/IEC 17021-1. Transition deadlines for existing accreditations are set by each accreditation body and were not confirmed in this review *(verify with the relevant body)*.
- **Certificate quality check:** read the scope statement, the accreditation mark and the accreditation body, the certificate dates, and — where the client will share it — the SoA. An unaccredited certificate to ISO/IEC 42001 carries materially less assurance than an accredited one, and the gap was wide before 2026.
- **Evidence an auditor will expect:** AI system inventory with roles per system; AI policy approved by top management; AI risk assessment and treatment records; AI system impact assessments (6.1.4/8.4) with records for each in-scope system; SoA; competence and awareness records; internal audit programme and reports; management review minutes with the specified inputs; nonconformity and corrective action log. See [audit-preparation](../../skills/audit-preparation/SKILL.md) and [control-testing](../../skills/control-testing/SKILL.md).
- **No official certificate population exists.** No ISO Survey figure for ISO/IEC 42001 could be confirmed in this review (the ISO site blocks scripted access), so any global count of certified organizations should be treated as an unofficial compilation *(verify before citing)*.

## Timeline and status

| Date | Event |
|---|---|
| 6 Feb 2023 | ISO/IEC 23894:2023 published (AI risk management guidance) |
| 18 Dec 2023 | **ISO/IEC 42001:2023 published**, first edition |
| 2025 | UKAS opens an AIMS accreditation pilot programme (programme page published 6 February 2025) |
| 28 May 2025 | ISO/IEC 42005:2025 published (AI system impact assessment) |
| 7 Jul 2025 | ISO/IEC 42006:2025 published (requirements for AIMS audit and certification bodies) |
| 15 Jan 2026 | UKAS grants the first UK accreditation for ISO/IEC 42001 certification (to BSI) |
| Mar–Apr 2026 | National adoptions of **EN ISO/IEC 42001:2026** — the European adoption of the identical ISO/IEC text — appear in CEN member catalogues (e.g. BS, March 2026; UNE, April 2026) *(distributor listing only — verify with a CEN member body)* |
| Jul 2026 | **EN 18286:2026**, *Artificial intelligence — Quality management system for EU AI Act regulatory purposes*, published as the first AI Act harmonised standard (CEN-CENELEC announcement posted 31 July 2026) |
| As of Sep 2026 | ISO/IEC 42001:2023, ISO/IEC 42005:2025 and ISO/IEC 42006:2025 are all still listed as published first editions, with no revision or amendment; Regulation (EU) 2024/1689 has no consolidated version on EUR-Lex. No citation of EN 18286:2026 in the Official Journal — the step that creates presumption of conformity under AI Act Art. 40(1) — could be confirmed in this review *(verify)* |

## Key obligations for security/GRC teams

1. **Inventory AI systems and assign a role per system** (provider, producer, customer, partner) before scoping anything — clause 4.1 role determination drives the applicability of nearly everything else. Use [ai-system-intake](../../workflows/ai-system-intake.md).
2. **Write the AI policy once and link it to the existing policy stack** (information security, privacy, procurement, HR, ethics). Clause 5.2 requires it; [policy-authoring](../../skills/policy-authoring/SKILL.md) covers structure.
3. **Stand up an AI risk assessment method** that is distinct from, but feeds, the enterprise risk register — clauses 6.1.2/6.1.3 and 8.2/8.3. ISO/IEC 23894 supplies the process shape. See [risk-assessment](../../skills/risk-assessment/SKILL.md).
4. **Build an AI system impact assessment process** covering impacts on individuals, groups and societies (3.24, 6.1.4, 8.4), with defined triggers, thresholds and approval. ISO/IEC 42005:2025 Annexes A and E give the process and a template. Run it alongside, not instead of, a DPIA — see [dpia-privacy-assessment](../../skills/dpia-privacy-assessment/SKILL.md).
5. **Produce and maintain the Statement of Applicability** with a written justification for every Annex A inclusion and exclusion, traceable to identified risks (3.26 Note 2).
6. **Extend third-party due diligence to AI suppliers and to customers of your AI** (Annex A.10): model and data provenance, evaluation results, incident and change notification, permitted-use terms, and the split of responsibilities across the life cycle. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
7. **Integrate rather than duplicate.** Map AIMS clauses onto the ISMS: one internal audit programme, one management review, one corrective-action process, one documented-information control. See [iso27001-readiness](../../skills/iso27001-readiness/SKILL.md) and [control-mapping](../../skills/control-mapping/SKILL.md).
8. **Give the governing body something to govern** (3.22, 9.3): AI inventory movement, impact assessments completed and overdue, AI risk acceptances, incidents and model-behaviour deviations, supplier concentration. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).
9. **Gap-assess before committing to a certification date** — the AI system impact assessment and Annex A.6/A.7 life-cycle and data controls are where organizations with a mature ISMS still fail. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).
10. **Track the standards layer as a live dependency**: EN 18286, its relationship to AI Act Art. 17, and any Official Journal citation change what an AI Act provider must do. See [ai-governance](../../skills/ai-governance/SKILL.md).

## Interplay

- **EU AI Act.** ISO/IEC 42001 is a governance management system; AI Act Art. 17 requires a provider of a high-risk AI system to operate a quality management system covering thirteen enumerated aspects (a)–(m), including a regulatory-compliance strategy, design and development control, test and validation procedures, data management, the Art. 9 risk management system, post-market monitoring (Art. 72), serious-incident reporting (Art. 73), record-keeping, resource management and an accountability framework. A 42001 AIMS is a credible host for those aspects but is **not** equivalent: only a harmonised standard cited in the Official Journal confers presumption of conformity (Art. 40(1)), which is EN 18286:2026's role. Art. 17(2) scales implementation to provider size; Art. 17(3) lets sectoral QMS obligations absorb the aspects; Art. 17(4) deems the obligation met for financial institutions complying with internal-governance rules under Union financial services law, except points (g), (h) and (i). See [eu-ai-act.md](../regulations/eu-ai-act.md).
- **ISO/IEC 27001:2022.** Same harmonized structure, so clauses 4, 5, 7, 9 and 10 can be operated jointly and audited together. The control sets are complementary, not overlapping: Annex A of 27001 protects information; Annex A of 42001 governs AI behaviour, data suitability, transparency and human oversight. Security of AI systems is still an ISMS problem. See [iso-27001-2022.md](iso-27001-2022.md).
- **GDPR.** An AI system impact assessment and a DPIA answer different questions — societal and group impact versus risk to data subjects' rights from processing — and neither substitutes for the other, though ISO/IEC 42005 Annex D addresses aligning them. Where AI processes personal data, expect to run both and cross-reference. See [gdpr.md](../regulations/gdpr.md).
- **NIST AI RMF.** A voluntary, non-certifiable framework (Govern/Map/Measure/Manage) that the 42001 text itself cites when describing AI roles (clause 4.1, NOTE 1), and for which NIST publishes a clause-by-clause crosswalk to ISO/IEC 42001. The two are complementary: the NIST framework gives outcome language and profiles, ISO/IEC 42001 gives an auditable management system. Organizations serving both US federal and EU markets commonly map one to the other rather than choosing.
- **SOC 2.** A SOC 2 examination produces an auditor's report on a service organization's controls over a period; ISO/IEC 42001 produces a certificate that a management system conforms. Different assurance objects, different audiences — buyers routinely ask for both, and neither covers the other. See [soc2-tsc.md](soc2-tsc.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).

## Primary sources

- ISO/IEC 42001:2023 official preview (foreword, contents, scope, terms and definitions, clause 4) — https://cdn.standards.iteh.ai/samples/81230/4c1911ebc9a641fcb6ee21aa09c28ad3/ISO-IEC-42001-2023.pdf — publisher preview of the standard text; fetched.
- ISO/IEC 42001:2023 publisher catalogue record (publication date, edition, status, ICS, committee) — https://webstore.iec.ch/en/publication/90574 — co-publisher page; fetched.
- ISO/IEC 42005:2025 publisher catalogue record — https://webstore.iec.ch/en/publication/107659 — fetched.
- ISO/IEC 42005:2025 official preview (contents and annex list) — https://cdn.standards.iteh.ai/samples/iso/iso-iec-42005-2025/08d7e571c9c3429d82aceca0b4746d01/iso-iec-42005-2025.pdf — fetched.
- ISO/IEC 42006:2025 official preview (contents, foreword, annex list) — https://cdn.standards.iteh.ai/samples/iso/iso-iec-42006-2025/6b90be3a546143cfbedae3ffd62ac9e5/iso-iec-42006-2025.pdf — fetched.
- ISO/IEC 42006:2025 publisher catalogue record — https://webstore.iec.ch/en/publication/108460 — fetched.
- ISO/IEC 23894:2023 publisher catalogue record — https://webstore.iec.ch/en/publication/82914 — fetched.
- Regulation (EU) 2024/1689 (AI Act), Arts. 17 and 40 — https://eur-lex.europa.eu/eli/reg/2024/1689/oj — official Official Journal text (CELEX 32024R1689); fetched.
- CEN-CENELEC, "EN 18286 in the Spotlight: Supporting Compliance with the AI Act" (posted 31 July 2026) — https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-07-30-ai-quality-management/ — European standardisation organisation announcement; fetched.
- UKAS, "UKAS grants first accreditation for ISO/IEC 42001" (15 January 2026) — https://www.ukas.com/resources/latest-news/ukas-grants-first-aims-accreditation/ — national accreditation body news; fetched.
- ISO catalogue record for ISO/IEC 42001:2023 — https://www.iso.org/standard/81230.html — **could not be fetched** (iso.org blocks scripted access); catalogue facts were taken from the IEC co-publisher records instead.
- NIST, *NIST AI RMF to ISO/IEC 42001 crosswalk* — https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf — US government mapping that enumerates the Annex A/B control numbers and titles used to cross-check the control counts and objective themes; fetched (it maps the FDIS text).
- UKAS, AI management systems accreditation programme page — https://www.ukas.com/accreditation/about/developing-new-programmes/development-programmes/aims/ — accreditation-body status page (updated August 2026); fetched.
- Standards distributor catalogue listings for EN ISO/IEC 42001:2026 national adoptions and for the titles of ISO/IEC 38507:2022 and ISO/IEC 5338:2023 — https://www.en-standard.eu/search/?q=42001 — **secondary source**, used only because CEN's own catalogue portal and iso.org were unreachable.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
