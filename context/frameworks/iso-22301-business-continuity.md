# ISO 22301:2019 — Security and resilience — Business continuity management systems — Requirements

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | ISO 22301:2019, second edition, dated 2019-10 (national bodies record availability from 30 October 2019); cancels and replaces ISO 22301:2012 |
| Publisher / committee | ISO, Technical Committee ISO/TC 292 *Security and resilience* |
| Amendment in force | ISO 22301:2019/Amd 1:2024, *Climate action changes*, effective 23 February 2024 |
| Normative reference | ISO 22300 *Security and resilience — Vocabulary* (undated reference, so the current edition applies: ISO 22300:2025, published 6 November 2025) |
| Structure | Harmonized management-system structure: Clauses 1–3 (scope, references, terms, not auditable) plus Clauses 4–10 containing the requirements; discipline-specific business continuity requirements sit almost entirely in Clause 8 |
| Who it covers | Voluntary and generic: all types and sizes of organization, or parts of one; extent of application depends on operating environment and complexity |
| Certifiable? | Yes. Conformity can be shown by self-determination and self-declaration, confirmation by an interested party such as a customer, external confirmation of the self-declaration, or third-party certification/registration |
| Adoption scale | ISO Survey 2024 (latest published as of September 2026): 4,595 valid ISO 22301 certificates across 11,387 sites, against 96,709 for ISO/IEC 27001 — a small but regulated-sector-weighted population |
| Auditor competence | ISO/IEC TS 17021-6:2014 sets competence requirements for bodies auditing and certifying BCMS |
| Under revision | ISO/CD 22301 (third edition project, ISO/TC 292) reached stage 30.60 with the comment/vote period closing 10 May 2026 |

## What it is

ISO 22301 is the certifiable requirements standard for a **business continuity management system (BCMS)**. Its stated scope is a management system to "protect against, reduce the likelihood of the occurrence of, prepare for, respond to and recover from disruptions when they arise," so that the organization can keep delivering products and services at an acceptable predefined capacity during a disruption. It is deliberately outcome-based: it fixes the management-system machinery and the analytical steps, not the recovery technology.

The 2019 second edition was a clarification exercise, not an expansion. ISO's own summary of the changes is explicit: the evolved ISO requirements for management system standards were applied, requirements were **clarified with no new requirements added**, discipline-specific business continuity requirements were consolidated almost entirely into Clause 8, Clause 8 was restructured, and several business continuity terms were modified. The Introduction places the standard on a Plan-Do-Check-Act cycle and states that this keeps it consistent with ISO 9001, ISO 14001, ISO/IEC 20000-1, ISO/IEC 27001 and ISO 28000 — which is why a BCMS is normally run as an extension of an existing ISMS rather than a parallel system.

ISO 22301 is the anchor of a wider family. The requirements live in 22301; almost all the "how" lives in companion guidance that is not certifiable but that auditors and regulators routinely treat as good practice.

## Scope and applicability

- **Voluntary standard, not law.** Applicability is a business decision, except where a contract, a tender, or a regulator effectively imports it (common in financial services, telecoms, health, defence supply chains, and public procurement).
- **Generic by design.** The requirements are stated to be applicable to all organizations "or parts thereof, regardless of type, size and nature." There is no size threshold and no sector carve-out.
- **Scope is the organization's own choice, but must be justified.** Clause 4.3 covers determining the scope of the BCMS, with 4.3.2 addressing the scope statement itself; certification is granted against that declared scope, which is why a certificate covering one data centre or one service line says much less than its holder usually implies. Always read the scope statement on a counterparty's certificate.
- **No Annex A.** Unlike ISO/IEC 27001, ISO 22301 has no normative control annex and no Statement of Applicability, so there is nothing to "exclude". Every requirement in Clauses 4–10 applies.
- **Climate-change context is now mandatory input.** Under Amendment 1:2024, applied across the harmonized structure following the ISO/IAF joint communiqué of 22 February 2024, Clause 4.1 requires the organization to determine whether climate change is a relevant issue, and a note to Clause 4.2 records that interested parties can have climate-related requirements.

## Structure and requirements

| Clause | Title | What it requires |
|---|---|---|
| 4.1–4.2 | Context; needs and expectations of interested parties | External/internal issues (now including a climate-change determination); interested parties and, at 4.2.2, legal and regulatory requirements |
| 4.3–4.4 | Scope of the BCMS; the BCMS itself | Determine and state the BCMS scope (4.3.1 general, 4.3.2 scope of the BCMS); establish, implement, maintain and continually improve the system |
| 5.1–5.3 | Leadership and commitment; policy; roles | Top-management commitment; a business continuity policy that is established and communicated (5.2.1, 5.2.2); assigned roles, responsibilities and authorities |
| 6.1–6.3 | Planning | Risks and opportunities (6.1.1 determining, 6.1.2 addressing); business continuity objectives, with 6.2.1 establishing them and 6.2.2 determining them; planning changes to the BCMS (6.3) |
| 7.1–7.5 | Support | Resources; competence; awareness; communication; documented information, including creation/update and control (7.5.1–7.5.3) |
| 8.1 | Operational planning and control | Plan, implement and control the processes needed to meet the requirements |
| 8.2 | Business impact analysis and risk assessment | 8.2.2 BIA and 8.2.3 risk assessment, run as a paired analytical step feeding strategy selection |
| 8.3 | Business continuity strategies and solutions | Identification (8.3.2), selection (8.3.3), resource requirements (8.3.4) and implementation of solutions (8.3.5) |
| 8.4 | Business continuity plans and procedures | Response structure (8.4.2), warning and communication (8.4.3), business continuity plans (8.4.4), recovery (8.4.5) |
| 8.5 | Exercise programme | A programme of exercises, not a single annual test |
| 8.6 | Evaluation of business continuity documentation and capabilities | Periodic evaluation of the documentation and of the capability itself |
| 9.1–9.3 | Performance evaluation | Monitoring, measurement, analysis and evaluation; internal audit and audit programme (9.2.1–9.2.2); management review with defined inputs and outputs (9.3.1–9.3.3) |
| 10.1–10.2 | Improvement | Nonconformity and corrective action; continual improvement |

**Verbal forms matter in audit.** ISO 22301 states that "shall" indicates a requirement, "should" a recommendation, "may" a permission and "can" a possibility. Only "shall" statements in Clauses 4–10 can generate a nonconformity; guidance in ISO 22313 and the technical specifications cannot.

**The BIA is the load-bearing step.** ISO/TS 22317:2021 lists the outcomes the BIA process is expected to produce, and these are the artefacts an auditor will look for: endorsement or modification of the BCMS scope; identification of legal, regulatory and contractual obligations; evaluation of impact over time as the justification for priorities; estimation of the **maximum tolerable period of disruption (MTPD)**; MTPD and **recovery time objective (RTO)** for the prioritized activities; the resources needed to perform prioritized activities, with RTOs and applicable **recovery point objectives (RPOs)**; dependencies including suppliers and partners; and interdependencies between prioritized activities. ISO/TS 22317 also sequences the work: set RTOs for activities (5.5.4) before defining the prioritized activities (5.5.5), then identify resources and dependencies (5.6), and obtain top-management approval of the results (5.8).

## The ISO 223xx / 27031 family

| Standard | Title | Status |
|---|---|---|
| ISO 22300:2025 | Security and resilience — Vocabulary | Published 6 November 2025; replaces ISO 22300:2021 |
| ISO 22313:2020 | Guidance on the use of ISO 22301 | Published 20 February 2020; clause-by-clause companion |
| ISO/TS 22317:2021 | Guidelines for business impact analysis | Published 17 November 2021 |
| ISO/TS 22318:2021 | Guidelines for supply chain continuity management | Published 1 December 2021 |
| ISO/TS 22331:2018 | Guidelines for business continuity strategy | Published 25 September 2018 |
| ISO/TS 22332:2021 | Guidelines for developing business continuity plans and procedures | Published 28 May 2021 |
| ISO 22316:2017 | Organizational resilience — Principles and attributes | Published 29 March 2017 |
| ISO 22336:2024 | Organizational resilience — Guidelines for resilience policy and strategy | Published 9 October 2024 |
| ISO 22361:2022 | Crisis management — Guidelines | Published 19 October 2022 |
| ISO 22398:2013 | Guidelines for exercises | Published 13 September 2013; underpins the Clause 8.5 exercise programme |
| ISO/IEC 27031:2025 | Cybersecurity — ICT readiness for business continuity | Published 16 May 2025; replaces the 2011 edition |

**ISO/IEC 27031:2025** is the ICT-facing bridge. Its scope sets out the framework for ICT readiness for business continuity (IRBC) and names the three objectives it serves: **minimum business continuity objective (MBCO)**, **RPO** and **RTO** as part of ICT business continuity planning. It is the standard to cite when the question is how technology recovery capability is derived from, and proven against, business-level continuity requirements.

Outside ISO, the **BCI Good Practice Guidelines Edition 7.0** structures the discipline as six Professional Practices — two management and four technical: PP1 Establishing a Business Continuity Management System, PP2 Embracing Business Continuity, PP3 Analysis, PP4 Solutions Design, PP5 Enabling Solutions, PP6 Validation. It is a methodology, not a conformity standard; use it to build the programme and ISO 22301 to audit it.

## Assessment, certification and evidence

- **Four routes to demonstrating conformity** are recognized in the standard itself: self-determination and self-declaration; confirmation by parties with an interest in the organization, such as customers; external confirmation of the self-declaration; or certification/registration by an external body. Choose deliberately — certification is the expensive option and is only worth it where a customer, tender or supervisor asks for the certificate.
- **Auditor competence** is governed by ISO/IEC TS 17021-6:2014. Certification-body audit cycles (initial certification, surveillance, recertification) follow ISO/IEC 17021-1 (verify the current cycle rules with the certification body before planning an audit calendar).
- **Certificate population is small.** ISO Survey 2024 — the latest published as of September 2026 — recorded 4,595 valid certificates and 11,387 sites, compiled for the first time from IAF CertSearch data contributed by 76 accreditation bodies and more than 2,400 certification bodies. Expect many counterparties to have a BCMS but no certificate.
- **The accreditation layer changed hands in 2026.** The International Accreditation Forum ceased operations on 1 January 2026; Global Accreditation Cooperation Incorporated (Global ACI) began operating that day and has assumed the former roles of IAF and ILAC. CertSearch remains the public register for checking that a counterparty's certificate is accredited and current.
- **Evidence that consistently carries an audit**: the documented scope statement; the business continuity policy and evidence of its communication (5.2.2); a current BIA with top-management sign-off and derived MTPD/RTO/RPO per prioritized activity; documented strategy selection with a resource rationale (8.3.3–8.3.4); the plans themselves with response structure and warning/communication arrangements; a multi-year exercise programme with after-action reports and tracked corrective actions (8.5, 10.1); internal audit programme records (9.2.2); and management review inputs and outputs (9.3.2–9.3.3). See [control-testing](../../skills/control-testing/SKILL.md) and [audit-preparation](../../skills/audit-preparation/SKILL.md).
- **The two most common findings** are a BIA that was never re-approved after a reorganization, and an exercise programme that tests the plan but never tests the recovery capability, which Clause 8.6 requires to be evaluated separately from the documentation.

## Timeline and status

| Date | Event |
|---|---|
| 15 May 2012 | ISO 22301:2012 first edition published |
| October 2019 | ISO 22301:2019 second edition published (national records show 30 October 2019); technical revision, clarifications only |
| 20 February 2020 | ISO 22313:2020 guidance published against the 2019 edition |
| 22 February 2024 | ISO/IAF joint communiqué on climate-change amendments to management system standards |
| 23 February 2024 | ISO 22301:2019/Amd 1:2024 (Climate action changes) effective; existing certificates remained valid and auditors assess the added requirements at the next audit |
| 16 May 2025 | ISO/IEC 27031:2025 published, replacing the 2011 edition |
| September 2025 | ISO Survey 2024 results published, first edition sourced from IAF CertSearch |
| 6 November 2025 | ISO 22300:2025 vocabulary published, replacing the 2021 edition; feeds ISO 22301 through its undated normative reference |
| 1 January 2026 | International Accreditation Forum ceased operations; Global Accreditation Cooperation Incorporated (Global ACI) began operating and assumed the former IAF and ILAC roles, CertSearch included |
| 10 May 2026 | ISO/CD 22301 comment and voting period closed; the third-edition project sits at stage 30.60 under ISO/TC 292 |
| As of September 2026 | ISO 22301:2019 plus Amd 1:2024 remains the certifiable edition. No publication date for the third edition is confirmed; plan for a transition period to be announced after the draft advances, and do not defer BCMS work in anticipation of it |

## Key obligations for security/GRC teams

1. **Decide whether certification is actually required**, or whether a self-declared BCMS aligned to ISO 22301 satisfies the driver (customer contract, tender, supervisor expectation). Run the decision through [certification-readiness](../../workflows/certification-readiness.md).
2. **Set the BCMS scope in writing and keep it honest** (Clause 4.3.2). Scope drives certificate value, audit cost and, in vendor diligence, whether a counterparty's certificate covers the service you buy.
3. **Run the BIA and the risk assessment as one paired exercise** (8.2.2 and 8.2.3), reusing the enterprise risk methodology rather than inventing a second one. See [risk-assessment](../../skills/risk-assessment/SKILL.md) and [risk-scoring](../risk-scoring.md).
4. **Derive MTPD, RTO and RPO per prioritized activity, and get top management to approve them.** Unapproved recovery objectives are the root cause of most failed continuity investments and most audit findings.
5. **Map ICT recovery capability to those objectives** using ISO/IEC 27031:2025 (MBCO, RPO, RTO) and the ISO/IEC 27001 Annex A controls 5.29, 5.30, 8.13 and 8.14, so the technology plan is traceable to a business requirement. See [iso-27001-2022.md](iso-27001-2022.md).
6. **Build an exercise programme, not an annual test** (8.5), spanning plan walkthroughs, technical failover, crisis-communication and scenario exercises; track every action to closure under [exception-management](../../skills/exception-management/SKILL.md) where remediation will not land before the next audit.
7. **Evaluate documentation and capability separately** (8.6) and feed both into internal audit (9.2) and management review (9.3), with the inputs and outputs the clause enumerates.
8. **Extend continuity requirements into the supply chain** using ISO/TS 22318:2021 — supplier RTOs, dependency mapping, and exit or alternative-source arrangements as contract terms, not questionnaire answers. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
9. **Report a small, stable metric set to the board**: prioritized activities with approved and met RTOs, exercise coverage and pass rate, open corrective actions past due, and supplier coverage of critical dependencies. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).
10. **Reconcile the BCMS against the regulatory continuity obligations that already bind the organization** before building anything new — most of the work is usually already required by one of the regimes below. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).

## Interplay

- **ISO/IEC 27001:2022** — the natural host system. Annex A control 5.29 (information security during disruption), 5.30 (ICT readiness for business continuity), 8.13 (information backup) and 8.14 (redundancy of information processing facilities) are the ISMS hooks; ISO 22301 supplies the BIA, strategy and exercise machinery behind them, and the shared harmonized structure lets one internal audit and one management review serve both. See [iso-27001-2022.md](iso-27001-2022.md) and [iso27001-readiness](../../skills/iso27001-readiness/SKILL.md).
- **DORA (EU financial entities)** — Art. 11 requires a comprehensive ICT business continuity policy, documented plans and procedures, independent internal audit review of ICT response and recovery plans for entities other than microenterprises, a business impact analysis of exposures to severe business disruptions using quantitative and qualitative criteria and scenario analysis, **testing of ICT business continuity and response/recovery plans at least yearly** and on substantive changes to systems supporting critical or important functions, a crisis management function, and readily accessible records of activities before and during disruption events. Art. 12(6) requires RTOs and RPOs to be set per function with regard to criticality and market-efficiency impact. An ISO 22301 BCMS maps well onto Art. 11 but does not by itself discharge it. See [dora.md](../regulations/dora.md).
- **NIS2** — Art. 21(2)(c) lists "business continuity, such as backup management and disaster recovery, and crisis management" among the minimum risk-management measures for essential and important entities. ISO 22301 plus ISO 22361 is the cleanest evidence story for that point. See [nis2.md](../regulations/nis2.md).
- **EU CER Directive** — Art. 13(1)(d) requires critical entities to take measures to recover from incidents, "duly considering business continuity measures and the identification of alternative supply chains," in order to resume the essential service. Physical and organizational resilience sit alongside the ICT-focused NIS2 duties. See [eu-cer-directive.md](../regulations/eu-cer-directive.md).
- **UK operational resilience (FCA PS21/3 and the PRA equivalent)** — a different unit of analysis. Firms identify important business services and set **impact tolerances** (the maximum tolerable disruption to a service, viewed from the harm caused), rather than activity-level RTOs. Rules came into force 31 March 2022, and by no later than 31 March 2025 firms had to have completed mapping and testing sufficient to show they can remain within impact tolerances. A BCMS supplies much of the evidence but not the impact-tolerance construct. See [uk-financial-operational-resilience.md](../regulations/uk-financial-operational-resilience.md).
- **HIPAA Security Rule** — 45 CFR 164.308(a)(7) requires a contingency plan with a data backup plan, disaster recovery plan and emergency mode operation plan (all Required), plus testing and revision procedures and applications and data criticality analysis (both Addressable). The criticality analysis is a BIA in all but name. See [hipaa.md](../regulations/hipaa.md).
- **NIST CSF 2.0** — the RECOVER (RC) function, with the categories Incident Recovery Plan Execution (RC.RP) and Incident Recovery Communication (RC.CO), is the CSF-side anchor; CSF gives outcome language for reporting, ISO 22301 gives the auditable system. See [nist-csf-2.md](nist-csf-2.md). For the US federal counterpart to ICT contingency planning, NIST SP 800-34 Rev. 1 (published May 2010) is still widely cited, but its CSRC catalogue entry now carries a self-referential withdrawal/supersession banner and offers no download, so confirm its status before citing it as authoritative.
- **APRA CPS 230 (Australia)** — the Australian prudential operational-risk and service-continuity regime; read it alongside this pack rather than assuming an ISO 22301 BCMS satisfies it. See [australia-apra-cps-234-230.md](../regulations/australia-apra-cps-234-230.md).
- **CIS Controls v8/v8.1** — Control 11 (Data Recovery) is the technical hygiene layer under a BCMS; tested, isolated backups are what turn a recovery plan into a recovery capability. See [cis-controls-v8.md](cis-controls-v8.md).

## Primary sources

- ISO 22301:2019 official preview (title page, foreword with the 2019 change summary, full Clause 1–10 contents listing, Introduction 0.1–0.5, Clause 1 Scope, Clauses 2–3 terms) — https://cdn.standards.iteh.ai/samples/75106/d11801a9bab045a88d59cd321519ecf1/ISO-22301-2019.pdf (fetched; ISO-published preview extract, full standard paywalled)
- ISO 22313:2020 official preview (contents, Clause 4 body) — https://cdn.standards.iteh.ai/samples/75107/8a8dea23287c465e97d89f0ec0f1c240/ISO-22313-2020.pdf (fetched)
- ISO/TS 22317:2021 official preview (contents, BIA outcomes list) — https://cdn.standards.iteh.ai/samples/79000/1c0f02d98ec647a8b1661e6c949a4bc2/ISO-TS-22317-2021.pdf (fetched)
- ISO/IEC 27002:2022 official preview (control titles 5.29, 5.30, 8.13, 8.14) — https://cdn.standards.iteh.ai/samples/75652/f9b90f856c0d4c3dbef74cf67374d1c5/ISO-IEC-27002-2022.pdf (fetched)
- ISO catalogue entries, publication dates, scopes and standard histories via the Estonian Centre for Standardisation (ISO member body) — https://www.evs.ee/en/iso-22301-2019 , /iso-22301-2019-amd-1-2024 , /iso-22313-2020 , /iso-ts-22317-2021 , /iso-ts-22318-2021 , /iso-ts-22331-2018 , /iso-ts-22332-2021 , /iso-22316-2017 , /iso-22336-2024 , /iso-22361-2022 , /iso-22398-2013 , /iso-22300-2021 , /iso-22300-2025 , /iso-iec-27031-2025 , /iso-iec-ts-17021-6-2014 (all fetched). iso.org itself returned 403 to scripted access and could not be fetched.
- ISO/CD 22301 project record (stage 30.60, close of voting 10 May 2026, owner ISO/TC 292), ISO projects database via the Institute for Standardization of Serbia — https://iss.rs/en/project/show/iso:proj:93606 (fetched)
- ISO Survey 2024 results (certificate and site counts) — https://www.globalstd.com/wp-content/uploads/2025/10/Infografia-ISO-Survey-2024_EN.pdf and https://isbl.eu/wp-content/uploads/2025/10/ISO-SURVEY-2024.pdf (both fetched; secondary reproductions of ISO's survey, cross-checked against each other, because iso.org was unreachable)
- Regulation (EU) 2022/2554 (DORA), Arts. 11 and 12 — official consolidated text — https://eur-lex.europa.eu/eli/reg/2022/2554/oj (fetched)
- Directive (EU) 2022/2555 (NIS2), Art. 21(2)(c) — official text — https://eur-lex.europa.eu/eli/dir/2022/2555/oj (fetched)
- Directive (EU) 2022/2557 (CER), Art. 13(1)(d) — official text — https://eur-lex.europa.eu/eli/dir/2022/2557/oj (fetched)
- FCA PS21/3 *Building operational resilience*, regulator page with the 31 March 2022 and 31 March 2025 dates — https://www.fca.org.uk/publications/policy-statements/ps21-3-building-operational-resilience (fetched)
- 45 CFR 164.308 (HIPAA Security Rule administrative safeguards, contingency plan standard) — https://www.ecfr.gov/current/title-45/section-164.308 (fetched)
- NIST CSF 2.0, RECOVER function and RC.RP/RC.CO categories — https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf (fetched)
- NIST SP 800-34 Rev. 1 catalogue entry — https://csrc.nist.gov/pubs/sp/800/34/r1/final (fetched; the entry shows a withdrawal/supersession banner that is self-referential on its face and no downloadable document)
- IAF cessation notice and successor body — https://iaf.nu/en/news/ (fetched; legacy IAF site) and https://global-aci.org/ (fetched; Global Accreditation Cooperation Incorporated)
- BCI Good Practice Guidelines Edition 7.0, Professional Practices PP1–PP6 — https://www.thebci.org/certification-training/good-practice-guidelines.html (fetched)
- Climate-change amendment wording added to Clauses 4.1 and 4.2 and the ISO/IAF joint communiqué date — https://www.qualityaustria.com/en/news/climate-change-becomes-the-focus-of-management-system-standards/ (fetched; accredited certification body, used as a secondary source because the ISO and IAF pages were unreachable)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
