# NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management (A CSF 2.0 Community Profile)

## At a glance

| Attribute | Detail |
|---|---|
| Citation | NIST Special Publication 800-61r3; DOI 10.6028/NIST.SP.800-61r3 |
| Publisher | NIST, Computer Security Division, Information Technology Laboratory (authors: Nelson, Rekhi, Souppaya, Scarfone) |
| Status & key dates | Approved by the NIST Editorial Review Board 2025-03-25; published April 2025. Supersedes SP 800-61 Rev. 2 (06 Aug 2012), *Computer Security Incident Handling Guide* |
| Legal force | Developed under NIST's FISMA 2014 (44 U.S.C. § 3551 et seq.) responsibilities; guidance, not a binding control standard. Explicitly available to non-government organizations on a voluntary basis; not subject to US copyright |
| Structure | Executive summary + 3 sections + References + Appendices A–C. The substance is a **CSF 2.0 Community Profile** in two tables: Table 2 (Preparation and Lessons Learned — Govern/Identify/Protect) and Table 3 (Incident Response — Detect/Respond/Recover) |
| Unit of guidance | One row per CSF 2.0 Function, Category and Subcategory, each carrying a priority (High/Medium/Low) and zero or more items tagged **R** (recommendation), **C** (consideration) or **N** (note) |
| Certifiable? | No. No certification, attestation or scoring scheme exists for SP 800-61. It is used as design input and as an audit-defensible reference for IR programme design |
| Assessment model | Self-assessment against the Profile's priorities; evidence comes from plans, playbooks, exercise records, incident tickets and after-action reports |
| Relationship to neighbours | Sits on top of [NIST CSF 2.0](nist-csf-2.md); implementation controls live in [SP 800-53](nist-800-53.md) (IR family) and are reachable from CSF outcomes via NIST's Cybersecurity and Privacy Reference Tool (CPRT). International analogue: the ISO/IEC 27035 series |
| Cost | Free download from NIST |

## What it is

SP 800-61r3 is a **full rewrite**, not an update. Rev. 2 (2012) was a practitioner's handbook organised around a four-phase life cycle and packed with operational detail (attack-vector taxonomy, functional/informational impact and recoverability rating tables, handler checklists). Rev. 3 discards that framing. Its change log states that NIST performed a complete rewrite to remove outdated material and content covered more deeply elsewhere, shifted the focus from *how to handle an incident* to *how to carry incident-response considerations through the whole cybersecurity risk-management programme*, reorganised the contents as a CSF 2.0 Community Profile, and moved most hyperlinks to a maintained SP 800-61 project website.

The rationale is stated in Section 2.1: when Rev. 2 was written, incidents were relatively rare and narrow, and response usually finished within a day or two, so it was realistic to treat incident response as a separate activity run by a separate team on a circular life cycle. Today incidents are frequent, broader and more damaging, recovery often takes weeks or months, and lessons should be shared as soon as they are identified rather than parked until recovery ends. Incident response is therefore presented as a continuous part of cybersecurity risk management rather than an episodic process.

A **Community Profile** is a published baseline of CSF outcomes addressing shared interests across a group of organisations (see NIST CSWP 32 on creating Community Profiles, and [CSF profiles and companion resources](nist-csf-profiles-and-companion-resources.md)). Rev. 3's Profile is deliberately generic — intended for most organisations regardless of sector or size — and NIST notes that narrower versions (federal agencies, small business, education) could be derived from it. The priorities are described as a starting point that adopters are expected to customise.

## Who it covers / Scope

- **Federal civilian agencies** apply it through FISMA and OMB Circular A-130; it does not automatically bind national security systems, which require separate approval by the relevant policy authorities.
- **Everyone else** uses it voluntarily. It is the de facto reference an auditor, regulator or plaintiff's counsel reaches for when asking whether a US organisation's incident-response programme was reasonable.
- **Subject-matter scope** is *adverse cybersecurity events only*. Rev. 3 defines an **event** as any observable occurrence involving computing assets; an **adverse event** as any event with a negative consequence, whatever the cause; and adopts the FISMA 2014 definition of a **cybersecurity incident**: an occurrence that actually or imminently jeopardises, without lawful authority, the integrity, confidentiality or availability of information or an information system, or constitutes a violation or imminent threat of violation of law, security policies, procedures or acceptable use policies.
- **Deliberately undefined terms.** The publication warns that some terms it uses — "data breach" is its own example — are not defined in the document, and that adopting organisations must define them against their own environment and applicable law. That gap is exactly where regulatory definitions in [breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) have to be bolted on.
- **No thresholds, no clocks.** SP 800-61r3 contains no reporting deadline of its own. Notification timing is pushed out to law, regulation and contract (RS.CO-02.R3/R5).

## Structure and requirements

### Life-cycle model: the old phases mapped to CSF Functions

| Rev. 2 phase | Rev. 3 CSF 2.0 Function(s) |
|---|---|
| Preparation | Govern; Identify (all Categories); Protect |
| Detection & Analysis | Detect; Identify (Improvement Category, ID.IM) |
| Containment, Eradication & Recovery | Respond; Recover; Identify (ID.IM) |
| Post-Incident Activity | Identify (ID.IM) |

Rev. 3's own model is two-level: Govern/Identify/Protect are preparation activities that are *not part of the response itself*, while Detect/Respond/Recover are the response. Continuous improvement (ID.IM) sits between them, fed by lessons from all Functions at all times rather than only after recovery. NIST explicitly says organisations should use whichever life-cycle model suits them — the four-phase model is not prohibited, it is simply no longer NIST's presentation.

### How to read the Profile

- **Priority** — *High*: a core incident-response activity for most organisations. *Medium*: directly supports IR. *Low*: indirectly supports IR. Low priority does not mean the outcome is unnecessary, only that it is outside the direct scope of responding to incidents.
- **Item IDs** — append the item to the CSF ID to get a unique reference, e.g. `GV.OC-03.R1`. Recommendations, considerations and notes at Function or Category level also apply to everything beneath them.
- Because the Profile is keyed to CSF IDs, an organisation that has already mapped its control set to CSF can attach these recommendations to existing controls without a new mapping exercise. See [control-mapping](../../skills/control-mapping/SKILL.md).

### Where the High priorities land

| Function | Elements marked High |
|---|---|
| Govern | GV.PO (Policy) — cybersecurity policies should include an incident response policy |
| Identify | ID.RA-02 (threat intelligence received), ID.RA-05 (threats/vulnerabilities/likelihood/impact inform prioritisation), ID.RA-06 (risk responses chosen and tracked); ID.IM-02 (improvements from tests and exercises), ID.IM-03 (improvements from operational execution), ID.IM-04 (IR and other plans established, maintained, improved) |
| Protect | PR.DS-11 (backups created, protected, maintained and **tested**) — the only High in Protect |
| Detect | Whole DE.CM and DE.AE Categories: DE.CM-01/02/03/06/09 (network, physical, personnel, external-provider and asset monitoring); DE.AE-02/03/04/06/07/08 (analyse adverse events, correlate sources, estimate impact and scope, alert authorised staff and tools, integrate threat intelligence, **declare incidents against defined criteria**) |
| Respond | Whole RS.MA (MA-01 execute plan with third parties on declaration, MA-02 triage and validate, MA-03 categorise and prioritise, MA-04 escalate/elevate, MA-05 apply recovery-initiation criteria); RS.AN-03 (root cause), RS.AN-06 (record actions, preserve integrity and provenance), RS.AN-07 (incident data and metadata collected, integrity and provenance preserved), RS.AN-08 (estimate and validate magnitude); RS.CO-02/03 (notification and information sharing); RS.MI-01 (contain), RS.MI-02 (eradicate) |
| Recover | Whole RC.RP (RP-01 to RP-06, ending with declaring the end of recovery against criteria and completing documentation); RC.CO-03 (stakeholder communication on recovery), RC.CO-04 (public updates via approved methods and messaging) |

### Selected recommendations worth quoting to a steering committee

| CSF ID | Substance |
|---|---|
| GV.OC-03.R1 | Cybersecurity requirements should include **all** requirements related to incident notification, data-breach reporting and other aspects of incident response |
| GV.RM-03.R1 | Incident-related decision-making must be informed by the organisation's other risk types |
| ID.IM-04.R1 | **Synchronise business continuity plans with incident response plans** — incidents undermine business resilience |
| RS.MA.R1/R2 | Incidents must not be handled first-come, first-served; triage, prioritisation, escalation and recovery-initiation decisions should run off a defined set of risk-evaluation factors (examples given: asset criticality, functional impact, data impact, stage of observed activity, threat-actor characterisation, recoverability) |
| RS.MA-02.R2 | Provide a mechanism for **third parties to report incidents to you**, and monitor it seriously |
| RS.CO.N1 | Reporting and communication splits into four distinct activities: incident **coordination**, incident **notification**, **public communication**, and **information sharing** — each with different audiences, triggers and legal exposure |
| RS.CO-02.R3/R4/R5 | Perform notifications in compliance with current incident-notification laws applicable to your sectors, geographies and customer locations; notify affected third parties per regulatory, legal and contractual requirements; notify law enforcement and regulators per plan criteria and management approval. NIST flags that notification law "is an evolving topic, and new laws and regulations are being established frequently" |
| RS.AN-06 | Record investigative actions and preserve the records' integrity and provenance — the evidentiary hook for any later enforcement or litigation |
| RC.RP-06.R1 | Prepare an after-action report documenting the incident, the response and recovery actions taken, and lessons learned (the outcome itself also requires declaring the end of recovery against criteria) |

### Roles, policy and procedures (Section 2.2–2.3)

Rev. 3 names the participating roles explicitly: leadership (funding and high-impact decisions such as shutting down or rebuilding critical services), incident handlers (on staff, on contract such as an outsourced SOC/MSSP, or on call), technology professionals, legal, public affairs/media relations, human resources, physical security and facilities, and asset owners. Third-party handlers are treated as a **shared responsibility model**: the division of responsibilities, information flows, coordination and authority to act must be in the contract, including restrictions (e.g. on the provider sharing sanitised incident data with other customers or unilaterally deactivating services). Provider privileged access and provider compromise are named as risks to address, with NDAs and contract clauses as controls — feed this into [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).

The stated elements of an incident-response **policy** are: management commitment statement; purpose and objectives; scope; definitions of events, incidents, investigations and related terms; roles, responsibilities and authorities (including who may confiscate, disconnect or shut down assets); guidelines for prioritising incidents, estimating severity and initiating recovery; and performance measures. Procedures sit under the policy and plan, should be tested or exercised periodically, and may be formatted as **playbooks**; NIST points to CISA's *Cybersecurity Incident & Vulnerability Response Playbooks* as examples. Use [policy-authoring](../../skills/policy-authoring/SKILL.md) and the [policy template](../../templates/policy-template.md).

## Assessment, certification and evidence

There is nothing to certify against. What holds up in an audit or an enforcement review:

| Evidence | Tied to |
|---|---|
| Approved IR policy containing the seven policy elements above | GV.PO, ID.IM-04 |
| IR plan plus per-scenario playbooks, versioned and reviewed | ID.IM-04.R2/R3/R4 |
| Documented incident-declaration criteria and recovery-initiation criteria, with tickets showing them applied | DE.AE-08, RS.MA-05 |
| Documented risk-evaluation factors and a triage/prioritisation matrix | RS.MA.R2 |
| Exercise and tabletop records with resulting improvement actions tracked to closure | ID.IM-02 (NIST points to SP 800-84 for exercise design) |
| Backup restoration test results | PR.DS-11 |
| After-action reports and lessons-learned records feeding a tracked improvement backlog | ID.IM-03, RC.RP-06 |
| Regulatory notification decision log — including documented no-notify decisions | RS.CO-02, and the [notification log template](../../templates/incident-regulatory-notification-log.md) |
| Contracts and MSSP/CSP responsibility splits for incident handling | Section 2.2 shared-responsibility guidance |

For test design and sampling, see [control-testing](../../skills/control-testing/SKILL.md); for programme gaps, [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).

## Timeline and status

| Date | Event |
|---|---|
| 01 Sep 2006 | SP 800-86, *Guide to Integrating Forensic Techniques into Incident Response* — published, still the current edition |
| 06 Aug 2012 | SP 800-61 Rev. 2 published |
| 22 Jul 2013 | SP 800-83 Rev. 1, malware incident prevention and handling — published, still the current edition |
| 22 Dec 2016 | SP 800-184, *Guide for Cybersecurity Event Recovery* — published, still the current edition |
| 01 Apr 2017 | CISA Federal Incident Notification Guidelines take effect (current edition) |
| Feb 2024 | CSF 2.0 (NIST CSWP 29) published, creating the taxonomy Rev. 3 is built on |
| 25 Mar 2025 | SP 800-61r3 approved by the NIST Editorial Review Board |
| Apr 2025 | **SP 800-61r3 published; Rev. 2 superseded in full** |
| As of Sep 2026 | No errata, supplement or further revision of Rev. 3 identified. The CSRC record still shows "Date Published: April 2025", Rev. 3 as the only final version in the 800-61 series, and Rev. 2 now listed as withdrawn |

Two companions that Rev. 3 cites are themselves unfinished: **SP 800-92r1** (cybersecurity log management planning, initial public draft dated 11 Oct 2023) and **CSWP 32** (guide to creating Community Profiles, initial public draft dated 26 Feb 2024) are both cited in draft form, and both were still listed on CSRC as drafts in September 2026. Check for final versions before citing either as settled guidance. Note also that Rev. 3's reference list does **not** cite SP 800-83 or SP 800-86, even though Rev. 2 pointed to SP 800-83 for malware handling — treat those two as still-current-but-ageing adjuncts rather than as part of the Rev. 3 ecosystem.

**US federal reporting context (separate from SP 800-61, and the part that actually carries deadlines):**

- **CISA Federal Incident Notification Guidelines** (effective 1 April 2017) require federal executive branch civilian agencies to report to CISA **within one hour** of identification by the agency's top-level CSIRT/SOC/IT department, with seven required attributes (functional impact, information impact, recoverability, detection timing, counts of affected systems/records/users, network location, point of contact); reporting by other bodies is voluntary. CISA scores incidents with the National Cyber Incident Scoring System (NCISS), which aligns to the priority levels of the Cyber Incident Severity Schema (Emergency/Black through Baseline — Negligible/White). Functional impact, information impact and recoverability are the same three axes Rev. 2 rated and Rev. 3 dropped. Full federal picture: [FISMA and federal cyber](../regulations/us-fisma-federal-cyber.md).
- **CIRCIA** (Cyber Incident Reporting for Critical Infrastructure Act of 2022): **no final rule had been published in the Federal Register as of 19 September 2026**. CISA's programme page states it continues to work on the final rule, citing multiple funding lapses that impacted rulemaking; town hall meetings announced by Federal Register notices of 13 February 2026 and 26 May 2026 were held 15–18 June 2026. The statutory clocks are 72 hours for a covered cyber incident and 24 hours for a ransom payment, but they do not bite until the final rule's effective date; CISA has announced no target date. Detail in [CIRCIA](../regulations/us-circia.md).

## Key obligations for security/GRC teams

1. **Re-anchor the IR programme on CSF IDs, not the four phases.** If your plan, metrics and audit evidence are labelled Preparation / Detection & Analysis / Containment-Eradication-Recovery / Post-Incident, keep the operational language but map each element to CSF Functions using the Table 1 crosswalk above, so Rev. 3 recommendations and [CSF 2.0](nist-csf-2.md) profiles attach cleanly.
2. **Write down incident-declaration criteria and recovery-initiation criteria** (DE.AE-08, RS.MA-05) and make the incident record show them being applied. These two decision points are where regulatory clocks start and where enforcement reviews concentrate.
3. **Define and publish risk-evaluation factors for triage** (RS.MA.R2). Ban first-come-first-served handling in the policy. Tie severity levels to escalation authority and to the notification decision tree.
4. **Split "reporting" into the four RS.CO activities** — coordination, notification, public communication, information sharing — and give each its own owner, approval path and template. Most notification failures are really coordination failures.
5. **Build the notification obligation register before the incident.** GV.OC-03.R1 requires cybersecurity requirements to include every incident-notification and breach-reporting obligation. Drive it from [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md), the [timelines crosswalk](../crosswalks/breach-notification-timelines.md) and the [incident regulatory response workflow](../../workflows/incident-regulatory-response.md).
6. **Define "data breach" and the other terms Rev. 3 leaves open** in your own policy, aligned to the legal definitions that actually bind you ([GDPR](../regulations/gdpr.md), [HIPAA](../regulations/hipaa.md), [NIS2](../regulations/nis2.md), [DORA](../regulations/dora.md), [SEC disclosure](../regulations/sec-cyber-disclosure.md), [GLBA/FTC Safeguards](../regulations/glba-ftc-safeguards.md)).
7. **Synchronise BC/DR with IR** (ID.IM-04.R1) and prove backups are tested, not just taken (PR.DS-11). Untested restoration remains the most common fatal gap in ransomware readiness — see also Control 11 (Data Recovery) in [CIS Controls v8](cis-controls-v8.md) and [ISO 22301](iso-22301-business-continuity.md).
8. **Contract for third-party incident handling.** Responsibility split, information flows, notification timelines to you, authority to act and limits on unilateral action, plus the provider's own breach-notification duty. Feed into [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
9. **Run exercises and close the loop** (ID.IM-02/03). Track improvement actions from tabletops and real incidents in the same backlog, with dates and owners; unclosed actions are exception candidates — see [exception-management](../../skills/exception-management/SKILL.md).
10. **Report on outcomes, not ticket counts.** Time-to-declare, time-to-contain, percentage of incidents with completed after-action reports, and improvement-action closure rate map directly to High-priority Profile elements. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **[NIST CSF 2.0](nist-csf-2.md)** — Rev. 3 *is* a CSF profile; it adds no outcomes of its own. Adopting it is an overlay on an existing CSF programme, not a parallel framework.
- **[NIST SP 800-53](nist-800-53.md)** — the IR control family (and AU, CP, SI) supplies the implementable controls behind the Profile's outcomes; NIST's CPRT holds the CSF-to-800-53 mapping.
- **ISO/IEC 27035 series** — the international counterpart, and a five-phase process rather than a CSF overlay: Plan and prepare; Detect and report; Assess and decide; Respond; Learn lessons. Current parts: **27035-1:2023** (2nd ed., 2023-02, principles and process — cancels and replaces 27035-1:2016; Annex C cross-references ISO/IEC 27001), **27035-2:2023** (2nd ed., 2023-02, planning and preparing for incident response), **27035-3:2020** (1st ed., 2020-09, ICT incident response operations), **27035-4:2024** (1st ed., 2024-12-02, coordination across multiple organisations). The series positions itself as additional guidance to the incident-management controls in ISO/IEC 27002 — see [iso-27001-2022.md](iso-27001-2022.md). Unlike SP 800-61, these are paywalled.
- **[PCI DSS v4.x](pci-dss-4.md)** and **[SOC 2](soc2-tsc.md)** impose their own testable IR requirements (plan, roles, annual testing, incident communication). SP 800-61r3 is a sensible design source for a single IR programme that satisfies all three, but none of them accept it as evidence on its own.
- **Regulatory reporting** — SP 800-61r3 provides no clocks. Every deadline comes from elsewhere; keep the Profile for programme design and the [breach-notification-timelines crosswalk](../crosswalks/breach-notification-timelines.md) for the deadlines. A single incident routinely runs several clocks at once.
- **CISA guidance** — federal agencies (and anyone imitating federal practice) layer the one-hour CISA notification and the NCISS/Cyber Incident Severity Schema on top of Rev. 3; see [FISMA and federal cyber](../regulations/us-fisma-federal-cyber.md) and, for critical infrastructure, [CIRCIA](../regulations/us-circia.md). If you kept Rev. 2's functional-impact, information-impact and recoverability rating scheme, NCISS is the live equivalent and a reasonable severity model to adopt.

## Primary sources

- NIST SP 800-61r3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile* (April 2025), full text — https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf (publisher document; fetched)
- NIST CSRC publication record for SP 800-61 Rev. 3 (publication date, supersession) — https://csrc.nist.gov/pubs/sp/800/61/r3/final (publisher page; fetched)
- NIST SP 800-61r2, *Computer Security Incident Handling Guide* (August 2012), superseded — https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf (publisher document; fetched, for the legacy life cycle and impact taxonomy)
- NIST CSRC records for SP 800-86 (Aug 2006), SP 800-83 Rev. 1 (Jul 2013) and SP 800-184 (Dec 2016) — https://csrc.nist.gov/pubs/sp/800/86/final, https://csrc.nist.gov/pubs/sp/800/83/r1/final, https://csrc.nist.gov/pubs/sp/800/184/final (publisher pages; fetched)
- NIST Incident Response project page (the maintained SP 800-61 website, CPRT mappings) — https://csrc.nist.gov/projects/incident-response (publisher page; fetched)
- CISA, *Federal Incident Notification Guidelines* (one-hour clock, seven attributes, NCISS and the severity schema, 1 Apr 2017 effective date) — https://www.cisa.gov/federal-incident-notification-guidelines (regulator guidance; page is live but blocks automated retrieval, so the text was read through a rendering proxy)
- CISA, CIRCIA programme page (final-rule status, 72-hour / 24-hour clocks, June 2026 town halls) — https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia (regulator guidance; same access caveat)
- Federal Register, CIRCIA document search (confirms no final rule published as of 19 September 2026; town-hall notices of 13 Feb 2026 and 26 May 2026) — https://www.federalregister.gov/documents/search?conditions%5Bterm%5D=CIRCIA&order=newest (official gazette; fetched)
- ISO/IEC 27035-1:2023 and 27035-2:2023 official previews (edition, date, five-phase process, relationship to ISO/IEC 27002 and 27001) — https://cdn.standards.iteh.ai/samples/78973/38e0e742e02741ba856510f74aa9f23b/ISO-IEC-27035-1-2023.pdf, https://cdn.standards.iteh.ai/samples/78974/58e4871b153f4bb387a4c39d2d5ff4af/ISO-IEC-27035-2-2023.pdf (publisher preview via standards distributor; fetched — full texts are paywalled)
- ISO/IEC 27035-3:2020 official preview — https://cdn.standards.iteh.ai/samples/74033/7a04b26605644f2897ee4bab41ad4a08/ISO-IEC-27035-3-2020.pdf (publisher preview; fetched)
- IEC Webstore record for ISO/IEC 27035-4:2024 (edition 1.0, publication date 2024-12-02, scope) — https://webstore.iec.ch/en/publication/103970 (publisher page; fetched)
- ISO catalogue pages for the 27035 series — https://www.iso.org/standard/78973.html, https://www.iso.org/standard/78974.html, https://www.iso.org/standard/74033.html, https://www.iso.org/standard/80973.html (**could not fetch** — iso.org blocks scripted access; details above taken from the publisher previews and the IEC record instead)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
