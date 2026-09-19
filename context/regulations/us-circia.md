# Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA, 6 U.S.C. §§ 681–681g)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | CIRCIA — Division Y of the Consolidated Appropriations Act, 2022 (Pub. L. 117-103, signed 15 March 2022); codified at 6 U.S.C. §§ 681–681g (Homeland Security Act §§ 2240–2246), as amended by Pub. L. 117-263 (Dec. 2022) |
| Implementing rule | Proposed 6 CFR Part 226 (RIN 1670-AA04, docket CISA-2022-0010). NPRM published 4 April 2024 at 89 FR 23644; **no final rule published in the Federal Register as of 18 September 2026** |
| Regulator | Cybersecurity and Infrastructure Security Agency (CISA), within DHS; Sector Risk Management Agencies receive shared reports |
| Status | Statute in force, but the reporting duties "take effect on the dates prescribed in the final rule" (§ 681b(a)(7)) — until the final rule's effective date, no entity is required to submit CIRCIA reports; CISA solicits voluntary reports |
| Who is covered | "Covered entities": entities in one of the 16 critical infrastructure sectors (PPD-21) that meet the definition CISA sets in the final rule. NPRM proposed: any entity in a sector exceeding the SBA small business size standard, plus entities meeting any of 16 sector-based criteria — ~316,000 entities estimated |
| Core clocks (statute) | Covered cyber incident: **≤72 hours** after the entity reasonably believes it occurred. Ransom payment: **≤24 hours** after payment made. Supplemental reports: "promptly" (NPRM: within 24 hours of the trigger) until the incident is concluded and fully mitigated and resolved |
| Data preservation | Statutory duty; NPRM proposes ≥2 years from the last required report, in original format |
| Enforcement | No civil money penalty in the statute. Request for information → administrative subpoena (≥72 h after RFI) → DOJ civil action / contempt; NPRM adds referral for suspension and debarment and for federal-contract enforcement; false statements fall under 18 U.S.C. § 1001 |
| Protections for reporters | FOIA and state open-records exemption, no privilege waiver, no ex parte rule, no cause of action for a conforming report, evidentiary/discovery bar for the report itself, bar on regulators using CIRCIA-only information to enforce against the reporter (§ 681e) |
| Relationship to neighbours | Sits alongside SEC 8-K Item 1.05, HIPAA, banking 36-hour rule, NYDFS Part 500, TSA/Coast Guard/NERC/FCC sector rules; a "substantially similar reporting" exception applies only once CISA has a published agreement with the other agency |

## What it is

CIRCIA is the first cross-sector US federal statute requiring private critical-infrastructure operators to report substantial cyber incidents and ransomware payments to the federal government. Congress enacted it in March 2022 in the wake of the 2021 Colonial Pipeline attack, folding it into the FY2022 appropriations act. Unlike the SEC disclosure rules (public, investor-facing) or HIPAA (individual-facing), CIRCIA reporting is confidential and operational: CISA receives reports to build cross-sector situational awareness, disseminate anonymized indicators and defensive measures, share with Sector Risk Management Agencies within 24 hours (§ 681a(a)(10)), and publish quarterly aggregated trend reports (§ 681a(a)(8)).

The statute is deliberately skeletal. It fixes the two headline clocks and the enforcement and protection architecture, but delegates the definitions of "covered entity" and "covered cyber incident," report contents, preservation periods, supplemental-report timing and exception procedures to a CISA rulemaking (§ 681b(b)–(c)). Congress required the NPRM within 24 months of enactment and a final rule within 18 months of the NPRM. CISA met the first deadline (4 April 2024) and missed the second (4 October 2025). As of September 2026 the rule remains at final-rule stage, with CISA publicly committed to streamlining the requirements in response to comments seeking reduced scope and burden — so every specific below that is labelled "NPRM" is a proposal, not law, and may change materially.

## Who it covers / Scope

**Statutory test (§ 681(4)):** a covered entity is "an entity in a critical infrastructure sector, as defined in Presidential Policy Directive 21, that satisfies the definition established by the Director in the final rule." The 16 sectors: Chemical; Commercial Facilities; Communications; Critical Manufacturing; Dams; Defense Industrial Base; Emergency Services; Energy; Financial Services; Food and Agriculture; Government Facilities; Healthcare and Public Health; Information Technology; Nuclear Reactors, Materials and Waste; Transportation Systems; Water and Wastewater. CISA must describe covered entities using three factors (§ 681b(c)(1)): consequences of disruption to national/economic security or public health and safety; likelihood of being targeted, including by foreign states; and the extent to which compromise would enable disruption of critical infrastructure.

**NPRM proposal (proposed § 226.2)** — an entity in a critical infrastructure sector is covered if it meets *either* limb:

| Limb | Test |
|---|---|
| Size-based | Exceeds the SBA small business size standard for its NAICS code (13 CFR Part 121), by employee count or annual revenue |
| Sector-based (any one, regardless of the sector the entity self-identifies with) | CFATS-covered chemical facilities; wire/radio communications providers (incl. telecom carriers, submarine cable licensees); critical manufacturing (primary metals, machinery, electrical equipment, transportation equipment); DoD contractors and subcontractors subject to DFARS 252.204-7012 incident reporting; emergency services to a population ≥50,000; bulk electric/distribution entities subject to NERC CIP reporting or DOE form OE-417; listed financial services entities; education agencies with ≥1,000 students and certain higher-education institutions; election ICT manufacturers and managed-service providers; hospitals with ≥100 beds and critical access hospitals; IT entities (federal IT suppliers, vendors of software with privileged/trust-critical components, OT OEMs/vendors/integrators, DNS operations); NRC-licensed nuclear reactors and fuel-cycle facilities; TSA-regulated transportation entities (pipelines, rail, aviation, transit); MTSA-regulated vessels and facilities; community water systems and POTWs serving >3,300 people |

Practical consequences of the proposal: the size limb sweeps in most mid-size and large businesses in any of the 16 sectors; the sector limb reaches small entities in high-consequence niches (a critical access hospital, a water utility serving 4,000 people, a small vendor of privileged software components). CISA's own RIA counted 316,244 covered entities, 310,855 of them "small" under the Regulatory Flexibility Act. The February 2026 town-hall notice named the size-based limb, the sector criteria and the treatment of MSPs/CSPs as the principal candidates for revision.

**Statutory exemptions:** federal agencies already reporting under FISMA (proposed § 226.4(c)); DNS multistakeholder functions (ICANN, IANA — § 681b(a)(5)(C); NPRM adds ARIN and recognized root-server operators); and reports made to another federal agency under a CISA "CIRCIA Agreement" (see Core obligations). State, local, tribal and territorial government entities can be covered entities but are excluded from the RFI/subpoena enforcement machinery (§ 681d(f)).

## Core obligations

### Reportable events

| Term | Statute | NPRM proposal (proposed § 226.1) |
|---|---|---|
| Covered cyber incident | A "substantial cyber incident" experienced by a covered entity, as defined in the final rule. Minimum floor (§ 681b(c)(2)): substantial loss of CIA of a system, or serious impact on safety/resiliency of OT; disruption of business or industrial operations (incl. DoS, ransomware, zero-day); or unauthorized access/disruption via compromise of a cloud, managed-service or third-party hosting provider, or a supply-chain compromise. Must exclude good-faith activity at the owner's request (e.g., pen tests) and the mere *threat* of disruption as extortion | Any one of four prongs suffices: (1) substantial loss of confidentiality, integrity or availability of an information system or network; (2) serious impact on safety and resiliency of operational systems and processes; (3) disruption of ability to engage in business or industrial operations or deliver goods or services; (4) unauthorized access facilitated by a CSP/MSP/hosting-provider compromise or supply-chain compromise. Impact must have *actually* occurred (CISA rejected "potential" impact). Excludes lawfully authorized government activity, owner-requested activity, and extortion threats |
| Ransom payment | Transmission of money, property or assets (incl. virtual currency) delivered as ransom in connection with a ransomware attack (§ 681(8)) | Reportable even when the underlying attack is not a covered cyber incident, and when a third party pays on the entity's behalf. Excludes demands that are not genuine |

CISA's guidance on the **"reasonably believes" trigger** (NPRM preamble): no fixed definition; it is a lower bar than confirmation; preliminary triage to rule out benign causes is expected to take "hours, not days" and to happen at subject-matter-expert level, not at executive sign-off. A covered entity is one that meets the applicability test at *any* point during an incident's lifecycle, so an incident discovered years after initial compromise is still reportable if ongoing.

### Reports and clocks

| Report | Trigger and deadline | Source |
|---|---|---|
| Covered Cyber Incident Report | ≤72 hours after the entity reasonably believes a covered cyber incident occurred; CISA may not require earlier | § 681b(a)(1); proposed § 226.5(a) |
| Ransom Payment Report | ≤24 hours after the ransom payment is made (NPRM: "disbursed"); applies even if the attack is not a covered cyber incident | § 681b(a)(2); proposed § 226.5(b) |
| Joint Covered Cyber Incident and Ransom Payment Report | Optional single report when payment is made within the 72-hour incident window; due ≤72 hours after reasonable belief | § 681b(a)(5)(A); proposed § 226.5(c) |
| Supplemental Report | "Promptly" when substantial new or different information becomes available, or a ransom payment is made after the initial report (then ≤24 hours after disbursement); continues until the entity notifies CISA the incident is concluded and fully mitigated and resolved. NPRM interprets "promptly" as within 24 hours of the triggering event | § 681b(a)(3); proposed §§ 226.3(d), 226.5(d) |
| Optional closure notice | Supplemental report stating the incident has concluded and been fully mitigated and resolved — this stops the supplemental-report duty | Proposed § 226.3(d)(2) |

Manner and form: a web-based form on CISA's site or another Director-approved channel (§ 681b(c)(8)(A); proposed § 226.6). Required contents track § 681b(c)(4)–(5): affected systems and their function, description of the compromise, date range, operational impact, vulnerabilities and TTPs, threat-actor identifiers, categories of information accessed, entity identifiers (legal name, state of incorporation, trade names) and contact details; for ransom payments also the demand, payment date, amount, currency type, and payment instructions/wallet address. **Third parties** (incident-response firms, insurers, service providers, ISAOs, law firms) may submit on the entity's behalf, but the duty stays with the covered entity; a third party that knowingly makes a ransom payment for a covered entity must advise it of its reporting duty (§ 681b(d)).

### Data and records preservation (§ 681b(a)(4); proposed § 226.13)

Preservation starts at the earlier of reasonable belief or ransom disbursement and runs **at least two years from the most recent required report**, restarting with each supplemental report. Proposed categories: communications with the threat actor, indicators of compromise, relevant logs, malware samples and forensic artifacts, network data (NetFlow, PCAP), initial-access and TTP evidence, system/patch/configuration information, exfiltration evidence, all ransom-payment records, and any internal or third-party forensic reports. Records must be kept in original format, readily retrievable, and reasonably safeguarded; the entity need not create records it does not already hold.

### Exceptions — the "substantially similar reporting" route (§ 681b(a)(5)(B); proposed § 226.4(a))

A covered entity that must already report substantially similar information to another federal agency within a substantially similar timeframe is excused from CIRCIA reporting **only once CISA and that agency have a published CIRCIA Agreement and sharing mechanism** (§ 681g(a)). The NPRM makes the covered entity responsible for confirming that a listed agreement covers both it and the specific report type, requires field-level functional equivalence, and keeps the supplemental-report duty alive unless the agreement covers it. "Substantially similar timeframe" means the other agency can pass the report to CISA by the CIRCIA deadline. Under § 681g(a) every federal agency that receives an incident report must forward it to CISA within 24 hours once the final rule is effective. No CIRCIA Agreements can be relied on until CISA publishes them; do not assume SEC, HHS, banking-agency or TSA reporting discharges CIRCIA.

### Information handling and protections (§ 681e; proposed § 226.18)

- Federal use is limited to cybersecurity purposes, identifying threats/vulnerabilities, and preventing specific threats of death, serious bodily harm, serious economic harm, harm to minors, or prosecuting offenses arising from the reported incident.
- Reports designated by the entity are treated as commercial, financial and proprietary information; exempt from FOIA under 5 U.S.C. § 552(b)(3) and from state/local open-records laws; submission waives no privilege or trade-secret protection; not subject to ex parte rules.
- **No regulatory use:** no federal, state, local or tribal government may use information obtained *solely* through a CIRCIA report to regulate or enforce against the reporter, unless that regulator expressly accepts CISA reports as satisfying its own requirement.
- **Liability shield:** no cause of action lies for submitting a conforming report; the report, and records created solely to prepare it, cannot be received in evidence or discovered in any proceeding — but this does not shield underlying incident records that exist for other reasons.
- Protections extend to voluntary reports (§ 681c) and RFI responses, **not** to subpoena responses. CISA must store reports at FIPS 199 moderate baseline or higher and anonymize victims when sharing outward.

## Enforcement and penalties

| Stage | Mechanism | Source |
|---|---|---|
| 1. Request for information (RFI) | Issued where the Director has reason to believe (public reporting, other government information, CISA analysis) that a covered entity failed to report. Response deadline set by the Director; RFI responses get § 681e protections. Not a final agency action; cannot be appealed | § 681d(b); proposed § 226.14(c) |
| 2. Administrative subpoena | No earlier than 72 hours after the RFI, if no or inadequate response. Nondelegable authority of the Director; electronic subpoenas must carry a cryptographic signature. NPRM: appeal by written notice within 7 calendar days of service; CISA may withdraw | § 681d(c)(1),(3),(4); proposed § 226.14(d) |
| 3. Civil enforcement | Referral to the Attorney General for a district-court action; non-compliance punishable as contempt of court. Liability shield does not apply to this action | § 681d(c)(2); proposed § 226.15 |
| 4. Onward referral | Subpoena-obtained information may be passed to the AG or a regulator for criminal prosecution or regulatory enforcement | § 681d(d) |
| 5. Procurement consequences (NPRM) | Mandatory referral of non-compliance that may warrant action to the DHS Suspension and Debarment Official; discretionary referral to the cognizant contracting official or AG where the failure relates to a federal contract | Proposed §§ 226.16–226.17; § 681b(c)(8)(B)(ii) |
| False statements | Knowingly and willfully false or fraudulent statements in a report, RFI response or subpoena reply are punishable under 18 U.S.C. § 1001 | Proposed § 226.20 |

The statute contains **no civil money penalty**. The Director must weigh the complexity of determining whether an incident was covered and the entity's prior awareness of CISA's procedures before enforcing (§ 681d(e)). SLTT government entities are outside §681d. CISA must publish an annual, anonymized count of RFIs and subpoenas (§ 681d(g)–(i)).

## Timeline and status

| Date | Event |
|---|---|
| 15 Mar 2022 | CIRCIA enacted (Pub. L. 117-103, Div. Y) |
| 12 Sep 2022 | CISA Request for Information (87 FR 55833); ~130 comments and sector listening sessions |
| 23 Dec 2022 | Pub. L. 117-263 amends cross-references (renumbered Homeland Security Act definitions) |
| 19 Sep 2023 | DHS report to Congress, *Harmonization of Cyber Incident Reporting to the Federal Government*, from the Cyber Incident Reporting Council (§ 681f): model definition of a reportable cyber incident and model reporting form, which the NPRM used as its starting point (departing where CIRCIA requires actual rather than potential impact) |
| 4 Apr 2024 | NPRM, 89 FR 23644 (proposed 6 CFR Part 226); comment period extended to 3 Jul 2024 (89 FR 37141); correction 3 Jun 2024 (89 FR 47471); ~300 comments received |
| 4 Sep 2025 | Spring 2025 Unified Agenda released, moving the final rule to May 2026; CISA stated it would use the time to "streamline CIRCIA's requirements" in response to comments seeking reduced scope and burden and better harmonization with other federal regimes |
| 4 Oct 2025 | Statutory final-rule deadline (18 months after NPRM) — missed |
| 13 Feb 2026 | Federal Register notice (91 FR 6794) of virtual town halls (9 Mar–2 Apr 2026) on "refining the scope and burden" of the NPRM; comment period not reopened |
| 14 Feb–30 Apr 2026 | DHS appropriations lapse; town halls not held; CISA cites "multiple funding lapses" as delaying the rulemaking |
| 26 May 2026 | Revised schedule (91 FR 30498): town halls held 15–18 June 2026; transcripts and materials on docket CISA-2022-0010 |
| 14 Aug 2026 | 2026 Unified Agenda and Regulatory Plan (91 FR 53004; 91 FR 52792): rule listed at Final Rule Stage; Regulatory Plan timetable targets a final rule in **September 2026**, and states CISA "is working to address Congressional intent and streamline CIRCIA's requirements" |
| 18 Sep 2026 | No final rule in the Federal Register. When it publishes, expect a 60-day minimum delayed effective date (major rule under the Congressional Review Act), so mandatory reporting is unlikely before late 2026 at the earliest |

Pending items to watch: the final applicability test (size limb under reconsideration), final incident definition and examples, supplemental-report timing, the CIRCIA reporting form (CISA's January 2025 incident-form information collection expressly covers only non-CIRCIA reporting), and publication of CIRCIA Agreements with other agencies. Track via [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Key obligations for security/GRC teams

1. **Run the applicability test now, twice**: once against the NPRM size limb (SBA size standard for your NAICS code) and once against each sector-based criterion for every legal entity and facility — the sector limb applies regardless of which sector you think you are in. Record the analysis so it can be refreshed against the final rule within days of publication. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Define the "reasonable belief" moment in the incident-response plan**: a named triage role, a bounded triage window measured in hours, and a documented timestamp, since the 72-hour clock starts there, not at executive confirmation. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) and [../../workflows/incident-regulatory-response.md](../../workflows/incident-regulatory-response.md).
3. **Pre-map the four substantial-incident prongs to severity tiers**, including third-party/CSP/MSP compromise as a stand-alone trigger, so the "is this covered?" call does not start from a blank page.
4. **Build the 24-hour ransom-payment path**: whoever can authorize a payment (including cyber insurers and negotiators acting for you) must be contractually obliged to notify the reporting owner immediately; a third party paying on your behalf does not discharge your duty.
5. **Stand up a supplemental-report cadence** — a standing checkpoint in every major incident to ask "is there substantial new or different information?", and a deliberate closure notice to stop the clock. Log every report in [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
6. **Add CIRCIA preservation to the legal-hold procedure**: two years from the last report, original format, covering third-party forensic reports and payment records. Test retrievability as a control ([../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md)).
7. **Do not treat other filings as CIRCIA compliance** until a published CIRCIA Agreement covers your regulator and report type; until then, plan for parallel filings with different clocks (see Interplay).
8. **Mark reports for protection**: designate commercial/financial/proprietary content on submission, keep report-drafting workpapers segregated from ordinary incident records (only the former get the evidentiary bar), and route submissions through counsel. Track any deliberate non-reporting decision as a formal exception ([../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md)).
9. **Brief the board** on the enforcement chain (RFI → subpoena → DOJ → debarment referral) and on the fact that the rule's scope is still moving; see [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **SEC 8-K Item 1.05** — different audience and clock: public disclosure within four business days of a *materiality* determination versus confidential CISA report within 72 hours of *reasonable belief*. A CIRCIA report is FOIA-exempt and cannot itself be used against the filer; an 8-K is public. Sequence them: the CISA report will usually be due first. See [sec-cyber-disclosure.md](sec-cyber-disclosure.md).
- **HIPAA Breach Notification Rule** — 60-day individual/HHS clock on discovery of unsecured PHI; hospitals ≥100 beds and critical access hospitals are named sector-based covered entities in the NPRM, so a ransomware event at a hospital triggers both. See [hipaa.md](hipaa.md).
- **Banking 36-hour rule, NYDFS Part 500 (72 h; 24 h for extortion payments), FTC Safeguards (30 days)** — financial services entities are a named sector criterion; none of these filings substitutes for CIRCIA absent a CIRCIA Agreement. See [glba-ftc-safeguards.md](glba-ftc-safeguards.md) and the NYDFS Part 500 pack (us-nydfs-part-500).
- **Sector regimes (TSA security directives, Coast Guard MTSA cyber rule, NERC CIP, DOE OE-417, FCC outage reporting, NRC)** — the NPRM uses existing obligations under these regimes as sector-based coverage criteria, and they are the most likely candidates for CIRCIA Agreements; § 681g(a) obliges those agencies to forward reports to CISA within 24 hours.
- **State breach laws** — consumer/AG notification runs on separate discovery-based clocks; state regulators also cannot use CIRCIA-only information to enforce. See [us-state-privacy.md](us-state-privacy.md).
- **NIS2 / DORA (EU)** — multinational operators face 24-hour early warnings and 4-hour classification clocks in Europe alongside CIRCIA's 72 hours; design one incident-classification schema that emits all of them. See [nis2.md](nis2.md), [dora.md](dora.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
- **Frameworks** — CIRCIA readiness maps to NIST CSF 2.0 Respond (RS.CO, RS.MA) and Govern outcomes and to CIS Control 17; see [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md) and [../frameworks/cis-controls-v8.md](../frameworks/cis-controls-v8.md).
- **Third-party risk** — CSP/MSP and supply-chain compromises are explicit incident prongs; vendor contracts need incident-notification clauses tight enough to let you meet 72 hours ([../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md)).

## Primary sources

- 6 U.S.C. §§ 681–681g (Office of the Law Revision Counsel, current through 18 Sep 2026) — statutory text: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title6-section681b&num=0&edition=prelim (and sibling sections 681, 681a, 681c–681g)
- Pub. L. 117-103, Consolidated Appropriations Act, 2022 (Division Y = CIRCIA) — govinfo record: https://www.govinfo.gov/app/details/PLAW-117publ103
- CISA NPRM, *CIRCIA Reporting Requirements*, 89 FR 23644 (4 Apr 2024), proposed 6 CFR Part 226 — legal text of the proposal and preamble: https://www.federalregister.gov/documents/2024/04/04/2024-06526/cyber-incident-reporting-for-critical-infrastructure-act-circia-reporting-requirements
- CISA, *CIRCIA Rulemaking; Town Hall Meetings*, 91 FR 6794 (13 Feb 2026) — regulator notice listing topics under reconsideration: https://www.federalregister.gov/documents/2026/02/13/2026-02948/cyber-incident-reporting-for-critical-infrastructure-act-circia-rulemaking-town-hall-meetings
- CISA, *Town Hall Meetings… Revised Schedule*, 91 FR 30498 (26 May 2026): https://www.federalregister.gov/documents/2026/05/26/2026-10417/town-hall-meetings-to-provide-input-on-cyber-incident-reporting-for-critical-infrastructure-act
- Unified Agenda 2026 / Regulatory Plan, RIN 1670-AA04 (14 Aug 2026), 91 FR 53004 and 91 FR 52792 — status and September 2026 target: https://www.federalregister.gov/documents/2026/08/14/2026-16603/introduction-to-the-unified-agenda-of-federal-regulatory-and-deregulatory-actions-2026
- Spring 2025 Unified Agenda entry, RIN 1670-AA04 (May 2026 target; statutory deadline 4 Oct 2025): https://www.reginfo.gov/public/do/eAgendaViewRule?pubId=202504&RIN=1670-AA04
- CISA CIRCIA landing page and FAQs (regulator guidance; voluntary reporting, town-hall record, funding-lapse statement): https://www.cisa.gov/circia
- DHS, *Harmonization of Cyber Incident Reporting to the Federal Government* (19 Sep 2023) — Cyber Incident Reporting Council report; landing page only, PDF not retrievable at time of writing: https://www.dhs.gov/publication/harmonization-cyber-incident-reporting-federal-government
- Secondary (dated confirmation of the May 2026 delay and CISA's public statement): CyberScoop, 8 Sep 2025; Davis Wright Tremaine, 17 Sep 2025; Covington Inside Privacy, Sep 2025; Hunton, 17 Jul 2026 (September 2026 target)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
