# NIST SP 800-171 / SP 800-172 and the CMMC Program (protecting Controlled Unclassified Information)

## At a glance

| Attribute | Detail |
|---|---|
| Publications | NIST SP 800-171r3 (May 2024) and SP 800-171Ar3 (May 2024, assessment procedures); SP 800-172r3 and SP 800-172Ar3 (May 2026, enhanced requirements for APT-exposed programs) |
| Regulatory hook | 32 CFR part 170 — DoD Cybersecurity Maturity Model Certification (CMMC) Program, 89 FR 83092, published 15 Oct 2024, effective 16 Dec 2024. Contract clauses: DFARS 252.204-7012 / -7019 / -7020 / -7021 and FAR 52.204-21 |
| Baseline actually enforced | **NIST SP 800-171 Rev. 2** (Feb 2020, updates to 28 Jan 2021) — withdrawn by NIST on 14 May 2024 yet incorporated by reference at 32 CFR 170.2(a)(9); assessed using SP 800-171A **Jun2018** objectives (170.2(a)(10)) |
| Structure (Rev. 3) | 17 requirement families, 97 security requirements, with organization-defined parameters (ODPs) |
| Who is covered | DoD contract and subcontract awardees at all tiers that process, store or transmit Federal Contract Information (FCI) or CUI on contractor information systems (32 CFR 170.3(a)); not federal systems operated on behalf of the Government (170.3(b)) |
| CMMC levels | L1: 15 requirements from FAR 52.204-21(b)(1)(i)–(xv), annual self-assessment. L2: 110 requirements from SP 800-171 R2, self-assessment or C3PAO certification. L3: 24 requirements selected from SP 800-172 Feb2021 with DoD ODPs, assessed by DCMA DIBCAC |
| Certifiable? | Yes — C3PAO certification (L2) or DIBCAC certification (L3), valid three years, plus annual affirmation by a named Affirming Official in SPRS |
| Enforcement | Contract eligibility — the contractor must have and maintain a current CMMC status at the required level for the life of the contract and affirm annually (DFARS 252.204-7021(d)); DoD may reassess where there are indications of compliance issues (252.204-7021(c)); civil False Claims Act exposure for false affirmations *(verify)* |
| Status, Sept 2026 | Phase 1 live since 10 Nov 2025; the Phase 2 transition to third-party assessment, due 10 Nov 2026, was **suspended on 13 July 2026** pending a 60-day CIO review |

## What it is

Two distinct things that practitioners routinely conflate. **SP 800-171** is a NIST publication: a tailored subset of the SP 800-53B moderate baseline, expressing what a *nonfederal* organization must do to protect the confidentiality of CUI it holds on behalf of a federal agency. It is guidance, not law, until an agency puts it into a contract. **CMMC** is the DoD's verification program (32 CFR part 170) that turns the 800-171 requirements — plus a slice of SP 800-172 — into an assessed, certified, contractually enforceable condition of award.

The design assumption stated in SP 800-171r3 §2.1 is that CUI carries the same value inside or outside government and, per 32 CFR part 2002, is categorized at no less than the FIPS 199 **moderate** confidentiality impact value. Requirements were derived by tailoring out SP 800-53 controls that are primarily a federal-government responsibility, are not directly related to confidentiality, or are adequately addressed by other controls. Availability-focused families (Contingency Planning) are excluded, except CP-09/CP-09(08) for backup confidentiality; PII Processing and Transparency is excluded because PII is itself a CUI category; Program Management is excluded as baseline-independent.

CUI itself is defined by the government-wide program at 32 CFR part 2002 and the NARA **CUI Registry**, which organizes categories into 20 organizational index groupings (Defense, Export Control, Privacy, Critical Infrastructure, Procurement and Acquisition, and so on). Knowing which registry category applies determines which law or agency policy drives handling and marking — 800-171 only supplies the confidentiality control set.

## Who it covers / scope

- **Contractual trigger.** CMMC requirements apply to DoD solicitations and contracts under which a contractor or subcontractor will process, store or transmit FCI or CUI on unclassified contractor systems, including commercial-item acquisitions above the micro-purchase threshold, but **excluding** acquisitions exclusively for commercially available off-the-shelf (COTS) items (170.3(c)).
- **Flow-down.** Primes must comply and must flow requirements down at all tiers. A subcontractor that will handle only FCI needs Level 1 (Self); one that will handle CUI needs the level the prime's contract dictates (170.23).
- **Level selection is the government's call.** DoD program managers and requiring activities choose the CMMC Status based on mission criticality, technology type, threat of loss and exploitation impact (170.5(b)). Level 3 is reserved for "the most critical programs and technologies".
- **Assessment scope is asset-driven, not enterprise-wide.** Level 1 covers systems that handle FCI. Level 2 scoping (170.19(c)) sorts assets into CUI Assets, Security Protection Assets, Contractor Risk Managed Assets, Specialized Assets and Out-of-Scope Assets, each with different documentation and assessment treatment. Specialized Assets — IoT, IIoT, OT, government-furnished equipment, Restricted Information Systems, test equipment — are out of scope entirely at Level 1.
- **Cloud and external providers.** A CSP that processes, stores or transmits CUI must be FedRAMP Moderate (or higher) Authorized, or meet FedRAMP Moderate–equivalent requirements per DoD policy (170.19(c)(2), and DFARS 252.204-7012(b)(2)(ii)(D)). External Service Providers are scoped by whether they handle CUI and/or Security Protection Data.
- **Waivers and variances.** Waiver of CMMC requirements is possible only at Service/Component Acquisition Executive level (170.5(d)) and is *currently unavailable* during the Phase 2 suspension. Separately, DFARS 7012(b)(2)(ii)(B) allows a written request to vary from an 800-171 requirement, adjudicated by the DoD CIO; an adjudicated variance carried in the SSP is scored MET (170.24(c)(2)(i)).

## Structure and requirements

### SP 800-171 Rev. 3 — 97 requirements across 17 families

| § | Family | Reqs | § | Family | Reqs |
|---|---|---|---|---|---|
| 3.1 | Access Control | 16 | 3.10 | Physical Protection | 5 |
| 3.2 | Awareness and Training | 2 | 3.11 | Risk Assessment | 3 |
| 3.3 | Audit and Accountability | 8 | 3.12 | Security Assessment and Monitoring | 4 |
| 3.4 | Configuration Management | 10 | 3.13 | System and Communications Protection | 10 |
| 3.5 | Identification and Authentication | 8 | 3.14 | System and Information Integrity | 5 |
| 3.6 | Incident Response | 5 | 3.15 | Planning | 3 |
| 3.7 | Maintenance | 3 | 3.16 | System and Services Acquisition | 3 |
| 3.8 | Media Protection | 7 | 3.17 | Supply Chain Risk Management | 3 |
| 3.9 | Personnel Security | 2 | | **Total** | **97** |

Rev. 3 renumbers requirements to a zero-padded form (`03.01.01` Account Management, `03.17.01` Supply Chain Risk Management Plan) and marks 33 requirement identifiers as withdrawn. Planning, System and Services Acquisition and Supply Chain Risk Management are families that Rev. 2 did not contain. Rev. 3 carries no counterpart to the Rev. 2 "NFO" (non-federal organization expected) control listing.

**ODPs are the headline change.** Rev. 3 embeds `[Assignment: organization-defined …]` and selection operations throughout (Appendix D lists them). Where a federal agency or consortium does not set a value, the nonfederal organization must assign one, and that value becomes part of the requirement. Practically: an SSP that leaves ODPs blank is not assessable.

### SP 800-172r3 — enhanced requirements (May 2026)

SP 800-172r3 supersedes the Feb 2021 edition and is issued with a companion assessment publication, SP 800-172Ar3. They are selected *by the federal agency*, apply only to systems tied to a critical program or high value asset, and — unlike 800-171 — address integrity and availability alongside confidentiality. There is no expectation that all enhanced requirements will be selected. **CMMC Level 3 still points at the Feb 2021 edition**, not r3.

### CMMC levels as codified

| Level | Source of requirements | Assessment | Cycle | POA&M allowed? |
|---|---|---|---|---|
| Level 1 (Self) | FAR 52.204-21(b)(1)(i)–(xv) — 15 basic safeguards for FCI | Self-assessment, results in SPRS | Annual | No (170.21(a)(1)) |
| Level 2 (Self) | NIST SP 800-171 R2 — 110 requirements | Self-assessment, results in SPRS | Every 3 years | Yes, conditionally |
| Level 2 (C3PAO) | Same 110 requirements | Certification by an authorized/accredited C3PAO; results to CMMC eMASS → SPRS | Every 3 years | Yes, conditionally |
| Level 3 (DIBCAC) | 24 requirements selected from SP 800-172 Feb2021 with DoD ODPs (170.14(c)(4)) | DCMA DIBCAC; requires a *Final* Level 2 (C3PAO) status first | Every 3 years (plus the L2 cycle) | Yes, conditionally |

Higher statuses subsume lower ones for the same scope. Level 3 requires annual affirmation of *both* the Level 2 (C3PAO) and Level 3 statuses.

## Assessment, certification and evidence

- **Findings are MET / NOT MET / N/A.** Evidence must be final, not draft — working papers, drafts and unapproved policies are explicitly unacceptable (170.24(b)(1)). Enduring exceptions and temporary deficiencies documented with mitigations or operational plans of action are scored MET.
- **Level 2 scoring.** Maximum 110. Each NOT MET requirement subtracts 5, 3 or 1 points by severity; the score can go negative. Two requirements score partially: MFA (IA.L2-3.5.3) loses 3 points if implemented only for remote and privileged users, 5 if not at all; CUI encryption (SC.L2-3.13.11) loses 3 if encryption is not FIPS-validated, 5 if absent.
- **No SSP, no assessment.** Absence of a current System Security Plan (CA.L2-3.12.4) yields a finding that the assessment could not be completed, and non-compliance with DFARS 252.204-7012.
- **POA&M gate.** Conditional status requires score ÷ total ≥ 0.8, no POA&M item worth more than 1 point (except the FIPS-validation case at 3), and none of six named requirements on the POA&M: AC.L2-3.1.20, AC.L2-3.1.22, CA.L2-3.12.4, PE.L2-3.10.3, PE.L2-3.10.4, PE.L2-3.10.5. Level 3 bars seven, including the 24/7 SOC (IR.L3-3.6.1e) and the incident-response team (IR.L3-3.6.2e).
- **180 days.** A POA&M closeout assessment must confirm remediation within 180 days of the Conditional CMMC Status Date, or the Conditional status expires (170.21(b)) — and with it the current CMMC status that DFARS 252.204-7021(d) requires the contractor to maintain.
- **Affirmations.** An Affirming Official — a senior representative with authority to bind the organization — submits an affirmation in SPRS on achieving Conditional status, on Final status, annually thereafter, and after POA&M closeout (170.22).
- **Pre-CMMC assessment track persists.** DFARS 252.204-7019/-7020 still require a current (≤ 3 years) Basic, Medium or High NIST SP 800-171 DoD Assessment with summary-level scores posted in SPRS as a condition of award; Medium and High assessments are government-conducted and carry a rebuttal step before posting.
- **Ecosystem.** One Accreditation Body accredits C3PAOs against ISO/IEC 17020:2012; the CAICO certifies assessors and instructors against ISO/IEC 17024:2012 (170.8–170.13). See [iso-27001-2022.md](iso-27001-2022.md) for how conformity-assessment vocabulary differs from certification to a management-system standard.

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| Feb 2020 (upd. Jan 2021) | SP 800-171 Rev. 2 published — the baseline still contractually enforced |
| 14 May 2024 | NIST withdraws Rev. 2; SP 800-171r3 and SP 800-171Ar3 published (May 2024) |
| 2024 *(deviation number and date unverified)* | A DoD class deviation to DFARS 252.204-7012 keeps Rev. 2 as the standard against which the defense industrial base is assessed until Rev. 3 is brought in by rulemaking (Department CMMC FAQ Rev. 2.3, July 2026); the Rev. 2 lock for CMMC itself is verified independently at 32 CFR 170.2(a)(9) |
| 15 Oct 2024 / 16 Dec 2024 | CMMC Program final rule published (89 FR 83092) / effective — 32 CFR part 170 |
| 15 Jan 2025 | FAR CUI proposed rule (FAR case 2017-016), 90 FR 4278; comments closed 17 Mar 2025 |
| Apr 2025 | DoD memorandum sets the DoD organization-defined parameters for SP 800-171 Rev. 3: contractors may implement Rev. 3 early but must use those ODPs, and assessments continue against Rev. 2 until the deviation is superseded (Department CMMC FAQ Rev. 2.3) |
| 10 Sep 2025 / 10 Nov 2025 | DFARS acquisition final rule (DFARS case 2019-D041, 90 FR 43560) published / effective, adding 252.204-7021 and starting **Phase 1** |
| 13 May 2026 | SP 800-172r3 published, superseding the Feb 2021 edition, together with SP 800-172Ar3 |
| 23 Jun 2026 | Revised FAR CUI text re-proposed inside the FAR overhaul (FAR case 2026-001, 91 FR 37550), superseding the 2017-016 text: a standard form conveying CUI requirements, a new clause at FAR 52.240-7, and a CUI incident report due **72 hours** from discovery; comments closed 23 Jul 2026 — still a proposal |
| 13 Jul 2026 | DoW CIO suspends the phased schedule, including the Nov 2026 Phase 2 transition; only Level 1 (Self) and Level 2 (Self) may be designated; C3PAO and DIBCAC designations must be removed from live solicitations by amendment and from existing contracts by modification; no waivers during the review |
| 20 Jul 2026 / 14 Aug 2026 | Department request for information to inform the CMMC Reform Task Force issued / comments closed; the Task Force was asked for actionable reform recommendations within 60 days |
| Sept 2026 | The 60-day review period has run, but no post-review guidance, rule change or Task Force outcome had been published on the Department's CMMC page at the time of writing *(verify)* |
| Pending | The Department states it will incorporate SP 800-171 Rev. 3 through future rulemaking; no proposed or final rule doing so has been published |

Nothing in the suspension relieves the underlying obligations: DFARS 252.204-7012, SP 800-171 Rev. 2 implementation, SPRS score posting and annual affirmation all remain in force, and the Department states it will continue to enforce the baseline through Level 1/Level 2 self-assessment and selected government-led assessments.

## Key obligations for security/GRC teams

1. **Establish what you actually hold.** Separate FCI from CUI, and map each CUI item to its NARA registry category — the category, not the contract, drives marking and dissemination limits. Feeds [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md).
2. **Fix the enclave boundary before assessing.** Categorize every asset into the Level 2 categories and record CUI Assets, Security Protection Assets and Specialized Assets in the inventory, SSP and network diagram; scope decisions drive cost more than any control does.
3. **Maintain a current, ODP-complete SSP.** It is both the scoping artifact and the pass/fail gate; stale plans stop an assessment. Use [policy-authoring](../../skills/policy-authoring/SKILL.md) and [audit-preparation](../../skills/audit-preparation/SKILL.md).
4. **Run the score as a managed metric.** Track the 110-point Level 2 score, the 5/3/1 weightings and the 0.8 conditional threshold; report trend, not snapshots. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).
5. **Treat the 180-day POA&M clock as a hard project deadline**, and confirm no barred requirement sits on the plan. Manage entries through [exception-management](../../skills/exception-management/SKILL.md) and the [exception request template](../../templates/exception-request.md).
6. **Wire the 72-hour DFARS 7012 incident clock into the IR plan** — report at dibnet.dod.mil, obtain a DoD-approved medium assurance certificate *in advance*, preserve system images and packet capture for 90 days, and submit isolated malicious software to DC3. See [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md).
7. **Assess the supply chain both ways.** Flow requirements down at the correct level and evidence them upward; Rev. 3 adds a Supply Chain Risk Management family. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md) and [nist-800-161-cscrm.md](nist-800-161-cscrm.md).
8. **Verify cloud claims.** Require FedRAMP Moderate authorization or documented Moderate-equivalency evidence for any CSP touching CUI — a vendor's assertion is not evidence. See [fedramp.md](fedramp.md).
9. **Name and brief the Affirming Official.** Annual affirmation is a personal attestation of continuing compliance made into a government system; treat drift between assessment and affirmation as a governance failure.
10. **Plan for two baselines.** Build control documentation so Rev. 2 requirement IDs and Rev. 3 requirement IDs both resolve; use [control-mapping](../../skills/control-mapping/SKILL.md) and run the delta as a [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md).

## Interplay

- **SP 800-53 / FISMA.** 800-171 is a tailored derivative of the SP 800-53B moderate baseline — see [nist-800-53.md](nist-800-53.md). Where a contractor operates a system *on behalf of* the government, 800-171 does not apply; FISMA and full 800-53 do ([us-fisma-federal-cyber.md](../regulations/us-fisma-federal-cyber.md)).
- **NIST CSF 2.0** organizes the program; 800-171 supplies the requirement set. Mixing them in one deliverable without a crosswalk produces double counting — see [nist-csf-2.md](nist-csf-2.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).
- **CIS Controls v8** map usefully to 800-171 for implementation-level evidence in smaller suppliers ([cis-controls-v8.md](cis-controls-v8.md)).
- **CIRCIA** will impose separate covered-cyber-incident reporting on critical infrastructure entities; a defense supplier may owe both DFARS 7012 and CIRCIA reports on one event — see [us-circia.md](../regulations/us-circia.md) and the [breach notification timelines crosswalk](../crosswalks/breach-notification-timelines.md).
- **ISO/IEC 27001** certification does not satisfy CMMC and vice versa: different scope constructs, different assessment bodies, different evidence standard ([iso-27001-2022.md](iso-27001-2022.md)).
- **Other agencies' CUI regimes** ([IRS Publication 1075](../regulations/us-irs-pub-1075.md), [CJIS](../regulations/us-cjis-security-policy.md)) set their own control requirements for federal data held outside government; check the controlling authority for each data type rather than assuming one assessment covers all.

## Primary sources

- NIST SP 800-171r3, *Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations* (May 2024) — https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-171r3.pdf (publication, fetched)
- NIST SP 800-171A Rev. 3 publication page (May 2024) — https://csrc.nist.gov/pubs/sp/800/171/a/r3/final (publisher page, fetched)
- NIST SP 800-171 Rev. 2 publication page, showing withdrawal on 14 May 2024 — https://csrc.nist.gov/pubs/sp/800/171/r2/upd1/final (publisher page, fetched)
- NIST SP 800-172 Rev. 3 publication page (May 2026) — https://csrc.nist.gov/pubs/sp/800/172/r3/final (publisher page, fetched)
- NIST "Protecting Controlled Unclassified Information" project page, recent updates — https://csrc.nist.gov/projects/protecting-controlled-unclassified-information (publisher page, fetched)
- 32 CFR part 170, CMMC Program (current text) — https://www.ecfr.gov/current/title-32/subtitle-A/chapter-I/subchapter-D/part-170 (legal text, fetched)
- DFARS 252.204-7012 (current text, MAY 2024 clause date) — https://www.ecfr.gov/current/title-48/chapter-2/subchapter-H/part-252/subpart-252.2/section-252.204-7012 (legal text, fetched); DFARS 252.204-7019 and -7020 (NOV 2023) and 252.204-7021 (NOV 2025) at the sibling section URLs, e.g. https://www.ecfr.gov/current/title-48/chapter-2/subchapter-H/part-252/subpart-252.2/section-252.204-7021 (legal text, fetched)
- FAR 52.204-21, Basic Safeguarding of Covered Contractor Information Systems — https://www.ecfr.gov/current/title-48/chapter-1/subchapter-H/part-52/subpart-52.2/section-52.204-21 (legal text, fetched)
- CMMC Program final rule metadata, 89 FR 83092 (15 Oct 2024, effective 16 Dec 2024) — https://www.federalregister.gov/documents/2024/10/15/2024-22905/cybersecurity-maturity-model-certification-cmmc-program (legal text, fetched via API)
- DFARS final rule, DFARS case 2019-D041, 90 FR 43560 (10 Sep 2025, effective 10 Nov 2025) — https://www.federalregister.gov/documents/2025/09/10/2025-17359/defense-federal-acquisition-regulation-supplement-assessing-contractor-implementation-of (legal text, fetched via API)
- FAR CUI proposed rule, 90 FR 4278 (15 Jan 2025) — https://www.federalregister.gov/documents/2025/01/15/2024-30437/federal-acquisition-regulation-controlled-unclassified-information (legal text, fetched via API)
- FAR overhaul proposed rule carrying revised CUI text, 91 FR 37550 (23 Jun 2026) — https://www.federalregister.gov/documents/2026/06/23/2026-12559/federal-acquisition-regulation-revolutionary-federal-acquisition-regulation-overhaul-parts-1-2-4-33 (legal text, fetched via API)
- Department of War CIO, *Implementing the Suspension of CMMC Phase II* — attachment cleared for open publication 13 Jul 2026 — https://dowcio.war.gov/Portals/0/Documents/Library/ImplementingSuspensionCMMC-PhaseII.pdf (regulator guidance, fetched; the covering CIO memorandum at the same library is a scanned image and could not be read as text)
- Department of War CIO CMMC program page, stating the 13 Jul 2026 suspension of the Phase 2 transition originally set for 10 Nov 2026 — https://dowcio.war.gov/CMMC/ (regulator page, fetched)
- CMMC Program Frequently Asked Questions, Revision 2.3 (July 2026) — source for the DFARS 252.204-7012 class deviation holding assessments at Rev. 2, the intent to bring in Rev. 3 by rulemaking, and the April 2025 DoD ODP memorandum — https://dowcio.war.gov/Portals/0/Documents/CMMC/FAQsv6.pdf (regulator guidance, fetched)
- SBA Office of Advocacy alert on the CMMC Reform Task Force request for information (20 Jul 2026) — https://advocacy.sba.gov/2026/07/20/dow-requests-information-for-cmmc-reform-task-force/ (government secondary, fetched)
- NARA CUI Registry, category list — https://www.archives.gov/cui/registry/category-list (regulator guidance, fetched)
- 32 CFR part 2002, Controlled Unclassified Information — https://www.ecfr.gov/current/title-32/subtitle-B/chapter-XX/part-2002 (legal text, fetched)
- **Not fetched:** the NIST SP 800-171 DoD Assessment Methodology v1.2.1 (cited in 32 CFR 170.4 and linked from DFARS 252.204-7019/-7020 at https://www.acq.osd.mil/asda/dpc/cp/cyber/docs/safeguarding/NIST-SP-800-171-Assessment-Methodology-Version-1.2.1-6.24.2020.pdf), the April 2025 DoD ODP memorandum (dodcio.defense.gov) and the Department press release announcing the class deviation (war.gov) — those hosts refused scripted access. Confirm the deviation number and date, and the Basic/Medium/High scoring detail, directly.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
