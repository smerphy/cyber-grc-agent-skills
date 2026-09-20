# SOC 1 (AT-C 320), ISAE 3402 and the rest of the SOC family

## At a glance

| Attribute | Detail |
|---|---|
| Instrument (US) | AT-C section 320, *Reporting on an Examination of Controls at a Service Organization Relevant to User Entities' Internal Control Over Financial Reporting* — source SSAE No. 18; effective for service auditors' reports dated on or after 1 May 2017 |
| Instrument (international) | ISAE 3402, *Assurance Reports on Controls at a Service Organization* (IAASB) — effective for service auditors' assurance reports covering periods ending on or after 15 June 2011; performed together with ISAE 3000 (Revised) |
| Publishers | AICPA Auditing Standards Board / Assurance Services Executive Committee (US); IAASB (international); PCAOB for issuer audits |
| Subject matter | Controls at a service organization **likely to be relevant to user entities' internal control over financial reporting (ICFR)** — not a general security assessment |
| Report types | Type 1 (description + suitability of design, as of a date) and Type 2 (description + design + operating effectiveness, throughout a period, with a description of tests and results) |
| Who performs it | An independent service auditor — under AT-C 320 "a practitioner who reports on controls at a service organization" (.08); under ISAE 3402 a practitioner in a firm applying ISQM 1 and complying with the IESBA Code (paras. 5–6) |
| Certifiable? | No. The deliverable is an opinion in an attestation/assurance report, not a certificate; there is no pass/fail score |
| Distribution | SOC 1 under AT-C 320 carries a mandatory restricted-use alert (.40n for a type 2 report, .41n for a type 1). ISAE 3402 instead requires a statement that the report is intended only for user entities and their auditors (para. 53(e)) |
| Typical period | Type 2 reports "ordinarily" cover a minimum of six months (ISAE 3402 para. A30; PCAOB AS 2601 .53) |
| Sibling reports | SOC 2 and SOC 3 (Trust Services Criteria), SOC for Cybersecurity, SOC for Supply Chain — all examinations under AT-C section 205, not AT-C 320 |

## What it is

A SOC 1 report answers one question: *can the auditor of a company that outsources part of its accounting processing rely on the outsourcer's controls?* The service auditor examines management's description of the service organization's system, the control objectives management (or an outside party) has stated, and the controls designed to achieve them. Under AT-C 320 the objectives are to obtain reasonable assurance that the description fairly presents the system, that the controls were suitably designed, and — for a Type 2 — that they operated effectively throughout the period, and to express an opinion on those matters (AT-C 320 .07).

Because the criteria are **management's own control objectives**, SOC 1 has no fixed control list. Two payroll processors can issue clean SOC 1 reports on entirely different control sets. This is the deepest structural difference from SOC 2, where the criteria are the Trust Services Criteria published by the AICPA — see [soc2-tsc.md](soc2-tsc.md). It also explains why a SOC 1 is weak evidence of security posture: control objectives are chosen for their financial-statement relevance, so encryption, vulnerability management and incident response may be absent by design.

ISAE 3402 is the international analogue, issued by the IAASB and deliberately parallel: same Type 1/Type 2 split, same carve-out/inclusive treatment of subservice organizations, same complementary user entity control concept. It complements ISA 402 in the same way AT-C 320 complements AU-C section 402 (ISAE 3402 para. 1; AT-C 320 .01). Reports are frequently labelled "SOC 1 / ISAE 3402" and issued under both frameworks.

## Who it covers / Scope

- **Service organizations**: any organization or segment of one providing services to user entities that are likely to be relevant to those user entities' ICFR (AT-C 320 .08) — payroll bureaux, claims administrators, transfer agents, custodians, loan servicers, fund administrators, and the financially relevant parts of SaaS platforms (billing, revenue, ledger).
- **Voluntary.** Neither AT-C 320 nor ISAE 3402 is law. Demand is contractual and audit-driven: user auditors need the evidence, so customers put SOC 1 obligations in contracts.
- **Subservice organizations** (a service organization's own providers) are handled by either the **carve-out method** (their control objectives and controls are excluded from the description and from the engagement scope) or the **inclusive method** (both are pulled in). Carve-out is the market norm and shifts the diligence burden back onto the reader.
- **Complementary user entity controls (CUECs)**: controls management assumes the customer will implement and that are necessary to achieve the stated control objectives. AT-C 320 also defines **complementary subservice organization controls (CSOCs)**; ISAE 3402 defines complementary user entity controls but carries no equivalent defined term for subservice-side complementary controls.
- ISAE 3402 applies only to **reasonable assurance attestation** engagements, and only where the service organization is responsible for — or can otherwise assert on — the suitable design of controls (paras. 2–3). Engagements on controls unrelated to financial reporting, and engagements reporting only on whether controls operated as described, fall outside it and are carried out under ISAE 3000 (Revised) (para. 3).

## Structure and requirements

### The SOC family

| Report | Standard | Criteria | Subject | Use |
|---|---|---|---|---|
| SOC 1 | AT-C 320 (US) / ISAE 3402 (intl.) | Management's stated control objectives | Controls relevant to user entities' ICFR | Restricted: service org management, user entities during the period, and their auditors |
| SOC 2 | AT-C 205 | 2017 Trust Services Criteria (revised points of focus, 2022) + 2018 SOC 2 description criteria (revised implementation guidance, 2022) | Security, availability, processing integrity, confidentiality, privacy | Restricted use |
| SOC 3 | AT-C 205 | Trust Services Criteria | Same as SOC 2 but without the system description detail and test results | **General use** — freely distributable |
| SOC for Cybersecurity | AT-C 205 | AICPA description criteria for a cybersecurity risk management program + control criteria | Entity-wide cybersecurity risk management program | Intended for boards, senior management and other stakeholders; confirm the individual report's use restriction (verify) |
| SOC for Supply Chain | AT-C 205 | SOC for Supply Chain description criteria + Trust Services Criteria | Controls in a production, manufacturing or distribution system | For customers and business partners |

### What a SOC 1 report contains

1. **Management's description of the system** — services covered, the period (or date), the control objectives and who specified them, and the related controls.
2. **Management's written assertion** on the description, design and (Type 2) operating effectiveness. The service auditor is required to request it (AT-C 320 .13), which makes SOC 1 an assertion-based examination under AT-C 205.
3. **The service auditor's opinion**, including explicit statements where CUECs or CSOCs are necessary to achieve the stated control objectives (AT-C 320 .40m(iv)–(v)).
4. **The description of tests of controls and results** (Type 2 only). AT-C 320 .40l requires: the controls tested; whether items tested were all or a selection of the population; the nature of tests in enough detail for a user auditor to judge the effect on risk assessments; **any deviations, the extent of testing that found them including the number of items tested, and the number and nature of deviations — even where the service auditor concludes the control objective was still achieved**; and, where internal audit work was used, a description of that work and of the service auditor's procedures over it.
5. **The restricted-use alert** (.40n) and the report date, which may be no earlier than the date sufficient appropriate evidence was obtained, including the prepared description, management's assertion and reviewed documentation (.40q).

Other requirements worth knowing when reading a report: the service auditor must investigate the nature and cause of identified deviations (.32), request written representations that management has disclosed known noncompliance with laws or regulations, uncorrected misstatements and actual, suspected or alleged fraud (.36), and perform subsequent-events procedures (.35).

### SOC 1 (AT-C 320) versus ISAE 3402

| Dimension | AT-C 320 | ISAE 3402 |
|---|---|---|
| Umbrella standards | AT-C 105 and AT-C 205 (AT-C 320 .02) | ISAE 3000 (Revised), IESBA Code, ISQM 1 (paras. 5–6) |
| Effective from | Reports dated on/after 1 May 2017 | Reports covering periods ending on/after 15 June 2011 |
| Assurance level | Reasonable assurance, assertion-based examination | Reasonable assurance attestation only; limited assurance and direct engagements excluded |
| Use restriction | Mandatory restricted-use alert naming management, user entities during the period, and their auditors | Statement that the report and the description of tests are intended only for user entities and their auditors |
| Complementary controls | CUECs and CSOCs both defined | CUECs defined; no equivalent CSOC term |
| Minimum period | Not specified in the standard | Type 2 "ordinarily covers a minimum period of six months" (para. A30); shorter is contemplated where the system has run under six months or controls changed significantly |

## Assessment, certification and evidence

There is no certificate and no score — only an opinion (unqualified, qualified, adverse, or a disclaimer) plus, in a Type 2, the test detail. How the report is consumed:

- **Nonissuer financial-statement audits — AU-C section 402** (sources SAS Nos. 122, 128, 130, 145; effective for audits of periods ending on or after 15 December 2012). When using a Type 1 or Type 2 report to understand design and implementation, the user auditor must evaluate whether the date or period is appropriate, evaluate the sufficiency of the evidence, and determine whether CUECs address the relevant risks of material misstatement and whether the user entity designed and implemented them (.14). To rely on a Type 2 for **operating effectiveness**, the user auditor must additionally evaluate the adequacy of the period covered and the time elapsed since testing, **test the user entity's own CUECs**, and judge whether the service auditor's tests and results are relevant to the assertions (.17).
- **Carve-outs do not disappear.** If the report excludes a subservice organization whose services are relevant to the audit, the user auditor must apply AU-C 402's requirements to that subservice organization as well (.18).
- **Gaps in coverage.** Where the report's date or period falls outside the audited period, the user auditor performs updating procedures and gathers current information from other sources (.A25) — the practical origin of the "bridge letter" or gap letter that service organizations issue for the stub period. Bridge letters are management representations, not assurance; no standard cited here gives them evidential weight of their own.
- **Fraud inquiry.** The user auditor must ask user entity management whether the service organization has reported any fraud, noncompliance with laws and regulations, or uncorrected misstatements affecting the financial statements (.19).
- **Issuer audits — PCAOB AS 2601**, *Consideration of an Entity's Use of a Service Organization*, with integrated ICFR audits directed to AS 2201 Appendix B .B17–.B27. AS 2601 states that to be useful to user auditors a report should **ordinarily cover a minimum reporting period of six months** (.53) and addresses subsequent changes in service organization controls (.57–.59).
- **Reading a report for vendor risk** (deviations, CUECs, carve-outs, scope of the description, opinion modifications) is covered in [soc2-report-review.md](../../skills/third-party-risk-assessment/references/soc2-report-review.md); the same mechanics apply to SOC 1, with control objectives replacing the Trust Services Criteria.

## Timeline and status

*Dated as of September 2026.*

| Date | Event |
|---|---|
| June 2011 | ISAE 3402 effective (reports covering periods ending on or after 15 June 2011) |
| December 2015 | ISAE 3000 (Revised) effective for assurance reports dated on or after 15 December 2015 |
| April 2016 / May 2017 | SSAE No. 18, *Attestation Standards: Clarification and Recodification*, issued; AT-C 320 effective for reports dated on or after 1 May 2017 |
| Oct 2020 – Dec 2020 | SSAE No. 21 (direct examination) and No. 22 (review) issued; AT-C 205 as recodified is effective for assertion-based examination reports dated on or after 15 June 2022 |
| 2022 | 2017 Trust Services Criteria reissued with revised points of focus; 2018 SOC 2 description criteria reissued with revised implementation guidance; current AICPA SOC 2 guide carries a 2022 publication date |
| June 2024 / December 2025 | SSAE No. 23, *Amendments to the Attestation Standards for Consistency With the Issuance of AICPA Standards on Quality Management*, issued June 2024; effective for engagements beginning on or after 15 December 2025. AT-C 320 .04 was revised in April 2026 for the resulting conforming changes |
| Feb – May 2026 | AICPA posts a notice that it is looking into anonymously published allegations about the business practices of a compliance vendor offering SOC services, and publishes ethics staff insights on firm business arrangements with SOC tool providers (13 April 2026); profession media flag fast-turnaround SOC engagements (1 February and 30 April 2026) and AICPA guidance to peer reviewers on SOC 2 risks (14 May 2026) |
| March 2026 | AICPA FAQs on the effect of the use of software tools on SOC 2 examinations (posted 31 March 2026) |
| June 2026 | AT-C 320 .A73 revised for the updated title of the AICPA guide, now *SOC 1 Reporting on an Examination of Controls at a Service Organization Relevant to User Entities' Internal Control Over Financial Reporting* |
| September 2026 | AICPA Technical Questions and Answers section 9561 issued (posted 11 September 2026) on the effect of a service organization's **use of AI** on SOC 1 (AT-C 320) and SOC 2 (AT-C 205) examinations |

No repeal, replacement or restructuring of AT-C 320 or ISAE 3402 is in force as of September 2026; the AT-C codification is current as of August 2026, the IAASB work plan carries no ISAE 3402 revision project, and AS 2601 does not appear on the PCAOB standard-setting or research agenda. Two dated AU-C 402 amendments are pending and sit in the meantime in appendices to other sections: SAS No. 149 (group audits, issued March 2023; amendments in appendix C of AU-C 600), effective for audits of periods ending on or after 15 December 2026, and SAS No. 150 (external confirmations, issued July 2026; amendments in appendix B of AU-C 505), effective for periods ending on or after 15 December 2028.

## Key obligations for security/GRC teams

1. **Decide SOC 1 or SOC 2 on the basis of what the customer's auditor needs.** SOC 1 exists for ICFR reliance; if customers are asking about security posture, a SOC 1 will not answer them. See [soc2-readiness](../../skills/soc2-readiness/SKILL.md).
2. **Write control objectives before controls.** In a SOC 1 the objectives are the criteria — vague objectives produce an unfalsifiable report and, in peer review, a challengeable one. Anchor them to the transaction flows that touch customers' financial statements.
3. **Publish and police your CUECs.** They are the contractual boundary of the report. Every CUEC you state is an obligation you have pushed to the customer, and customers' auditors are required to test them.
4. **Map subservice organizations and decide carve-out or inclusive deliberately**, then inherit accordingly: carved-out providers must be covered by your own vendor programme — see [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md) and [vendor-onboarding.md](../../workflows/vendor-onboarding.md).
5. **Plan the period.** Six months is the working floor for a Type 2 to be useful; align the period end with customers' fiscal year ends and budget for a bridge letter covering the stub period.
6. **Treat deviations as disclosable.** A Type 2 must report deviations and the number of items tested even where the objective was still achieved — so remediate before the period, not during fieldwork, and log unremediated items as exceptions ([exception-management](../../skills/exception-management/SKILL.md)).
7. **Run one evidence programme, many reports.** Access, change, and operations evidence supports SOC 1 ITGCs, SOC 2 CC6–CC8, and SOX 404 testing simultaneously — see [control-testing](../../skills/control-testing/SKILL.md), [audit-preparation](../../skills/audit-preparation/SKILL.md) and [audit-evidence-request-list.md](../../templates/audit-evidence-request-list.md).
8. **Document AI use in scoped processes.** The September 2026 technical Q&A addresses how a service organization's use of AI affects SOC 1 and SOC 2 examinations; expect service auditors to ask what AI does inside financially relevant processing and how it is controlled.
9. **Read inbound reports, do not file them.** Check opinion type, period covered versus your fiscal year, carve-outs, CUECs you must implement, and every deviation — then feed results into the vendor risk register ([vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md)).

## Interplay

- **SOX 404 / ITGC**: a SOC 1 Type 2 over a financially relevant outsourced process is the standard evidence route for management's and the external auditor's ICFR conclusions; it does not eliminate the user entity's own monitoring or CUEC testing. See [sox-itgc.md](../regulations/sox-itgc.md), [coso-internal-control-erm.md](coso-internal-control-erm.md) and [cobit-2019.md](cobit-2019.md).
- **SOC 2**: different standard (AT-C 205), different criteria, different audience. Do not treat a SOC 1 as a security attestation or vice versa; see [soc2-tsc.md](soc2-tsc.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).
- **ISO/IEC 27001**: a certification against a management-system standard, not an opinion on control operation over a period. Complementary, not interchangeable — see [iso-27001-2022.md](iso-27001-2022.md).
- **Cloud and sector schemes built on the same attestation machinery**: the CSA STAR Attestation is a CSA/AICPA collaboration applying Trust Services Criteria together with the Cloud Controls Matrix in a SOC 2 engagement, with listings expiring after one year ([csa-ccm-star.md](csa-ccm-star.md)); Germany's C5, first published in 2016 and, in BSI's words, "completely revised in 2025/26", is audited by public accountants who produce a detailed examination report ([germany-bsi-it-grundschutz-c5.md](germany-bsi-it-grundschutz-c5.md)). Other schemes that consume or resemble SOC reporting include [fedramp.md](fedramp.md) and [hitrust-csf.md](hitrust-csf.md).
- **Supply chain**: SOC for Supply Chain covers production, manufacturing and distribution systems and sits alongside, not inside, ICT supply-chain risk management — see [nist-800-161-cscrm.md](nist-800-161-cscrm.md).
- **Broker-dealers, market infrastructure and regulated financial firms** frequently require SOC 1 coverage of outsourced processing as part of their own control obligations — see [us-sec-reg-sp-reg-sci.md](../regulations/us-sec-reg-sp-reg-sci.md).
- Terminology used above (Type 1/Type 2, CUEC, carve-out, bridge letter) is defined in the [glossary](../glossary.md).

## Primary sources

- AICPA, *U.S. Attestation Standards — AICPA (Clarified) [AT-C]*, codification current as of August 2026 — AT-C 105, AT-C 205 and AT-C 320 full text, plus the SSAE cross-reference table (linked as the AT-C sections PDF): https://www.aicpa-cima.com/resources/download/aicpa-ssaes-currently-effective
- AICPA, *U.S. Auditing Standards — AICPA (Clarified) [AU-C]*, codification current as of August 2026 — AU-C section 402, *Audit Considerations Relating to an Entity Using a Service Organization* (linked as the AU-C sections PDF): https://www.aicpa-cima.com/resources/download/aicpa-statements-on-auditing-standards-currently-effective
- IAASB, *2025 Handbook of International Quality Management, Auditing, Review, Other Assurance, and Related Services Pronouncements, Volume 4* — ISAE 3402, *Assurance Reports on Controls at a Service Organization*, and ISAE 3000 (Revised): https://www.iaasb.org/publications/2025-handbook-international-quality-management-auditing-review-other-assurance-and-related-services
- IAASB work plan and current projects (no ISAE 3402 revision project listed): https://www.iaasb.org/consultations-projects/work-plan
- PCAOB, AS 2601, *Consideration of an Entity's Use of a Service Organization*: https://pcaobus.org/oversight/standards/auditing-standards/details/AS2601
- PCAOB standard-setting and research agenda (no AS 2601 project listed): https://pcaobus.org/oversight/standards/standard-setting-research-projects
- AICPA & CIMA, *System and Organization Controls: SOC Suite of Services* landing page, including the 2026 notice on a compliance vendor's SOC business practices: https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services
- AICPA & CIMA topic pages: SOC 1 https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-1 · SOC 3 https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-3 · SOC for Cybersecurity https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-for-cybersecurity · SOC for Supply Chain https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-soc-for-supply-chain
- AICPA & CIMA publisher page for the *2017 Trust Services Criteria (With Revised Points of Focus – 2022)*: https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022
- AICPA & CIMA publication page for the SOC 2 guide (publication date 2022, updated as of 15 October 2022): https://www.aicpa-cima.com/cpe-learning/publication/soc-2-reporting-on-an-examination-of-controls-at-a-service-organization-relevant-to-security-availability-
- AICPA & CIMA, *TQA section 9561, SOC Examinations: Effect of the Service Organization's Use of AI on SOC 1 and SOC 2 Examinations* (posted 11 September 2026): https://www.aicpa-cima.com/resources/download/tqa-section-9561-soc-examinations-effect-of-the-service-organizations-use-of-ai-on-soc1-and-soc2-examinations
- AICPA & CIMA, *FAQs — Effect of the use of software tools on SOC 2 examinations* (posted 31 March 2026): https://www.aicpa-cima.com/resources/article/faqs-effect-of-the-use-of-software-tools-on-soc-2-r-examinations
- Cloud Security Alliance, STAR programme: https://cloudsecurityalliance.org/star · BSI, *Cloud Computing Compliance Criteria Catalogue (C5)*: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html
- Note: the AICPA criteria, description-criteria, TQA and FAQ **PDFs** sit behind a free-account gate; the publisher pages above (titles, scope summaries and posting dates) were used instead of the PDF text.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
