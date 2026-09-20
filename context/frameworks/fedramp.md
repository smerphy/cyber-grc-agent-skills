# FedRAMP (Federal Risk and Authorization Management Program) and state analogues

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | FedRAMP Authorization Act — Public Law 117-263 (FY23 NDAA), Title LIX, Subtitle C, Sec. 5921, enacted 23 December 2022; codified at 44 U.S.C. §§ 3607–3616 |
| Implementing policy | OMB Memorandum M-24-15 (25 July 2024), issued under 44 U.S.C. § 3614; rescinded and replaced the December 2011 cloud security authorization memorandum |
| Owner / operator | General Services Administration (GSA); FedRAMP Board (not more than 7 senior officials/experts appointed by the OMB Director in consultation with the GSA Administrator, 44 U.S.C. § 3610); Federal Secure Cloud Advisory Committee (§ 3616) |
| Current ruleset | **FedRAMP Consolidated Rules for 2026 ("CR26")** — launched 24 June 2026; optional early adoption from 4 July 2026; **mandatory for all stakeholders 1 January 2027** |
| Structure | 15 rulesets (certification, scope, package, incident, vulnerability, monitoring, change, crypto, assessment…) plus **46 Key Security Indicators (KSIs)** in 10 families for the 20x certification type |
| Grading | **Certification Classes A / B / C / D** replace the FIPS 199 impact labels Low / Moderate / High as FedRAMP's own label, rising from minimal assurance at Class A to significant assurance at Class D. 20x Class D certification is not yet obtainable — FedRAMP lists it as "coming in 2027" and pairs it with the 20x Phase 4 Class D pilot (FY27 Q1–Q2, FedRAMP's own estimate) |
| Certifiable? | Yes — FedRAMP Certification, via **Program Certification** (FedRAMP direct, no agency sponsor; 20x, plus two temporary Rev5 pipelines) or **Agency Certification** (agency sponsor; Rev5 only) |
| Independent assessment | By a **FedRAMP Recognized** independent assessment service (legacy term: 3PAO), accredited under the A2LA Cybersecurity Inspection Body Program to A2LA R311; at least once per year for Classes B/C/D |
| Legal effect | Statutory **presumption of adequacy** (44 U.S.C. § 3613(e)) — a FedRAMP package is presumed adequate for an agency ATO, but does not relieve the agency of its FISMA duties |
| State analogues | **GovRAMP** (renamed from StateRAMP in 2025) and **TX-RAMP** (Texas DIR, Tex. Gov't Code § 2054.0593) — separate programs with reciprocity rules of their own |

## What it is

FedRAMP is the US government's standardized process for assessing cloud products and services used by federal agencies, so that one assessment can be reused across government instead of each agency running its own. It began as a 2011 OMB memorandum, was put on a statutory footing by the FedRAMP Authorization Act in December 2022, and was re-founded in policy terms by OMB M-24-15 in July 2024 — which retired the Joint Authorization Board provisional-ATO model (existing JAB P-ATOs were re-designated) and directed automation, new authorization paths, and wider reuse.

The 2025–2026 **FedRAMP 20x** program carried that direction into practice. It replaced control-by-control paperwork review with **Key Security Indicators** — measurable security outcomes validated by automation — piloted first for Low-impact services (Phase 1, April–September 2025: 26 complete packages between 30 May and 18 August 2025, first pilot authorizations late July 2025) and then for Moderate (Phase 2, 18 November 2025 – March 2026: 14 qualifying submissions, first cohort authorized 6 March 2026). On **24 June 2026** FedRAMP consolidated everything into the **Consolidated Rules for 2026**, ended the pilots, and made 20x a generally available certification path.

CR26 also rewrote FedRAMP's vocabulary. "FedRAMP authorization" became **FedRAMP Certification** (to stop the misreading that it is a government-wide risk acceptance); impact levels became **Certification Classes**; the System Security Plan became the **Certification Package Overview** plus a **Security Decision Record**; "continuous monitoring" became **Ongoing Certification**; and **POA&Ms were eliminated entirely**, replaced by a list of **Accepted Weaknesses**. Anything written against pre-2026 FedRAMP templates should be assumed stale.

## Who it covers / Scope

FedRAMP applies to **cloud computing products and services** (IaaS, PaaS, SaaS) that create, collect, process, store, or maintain federal information on behalf of a federal agency. Per M-24-15, the following are outside scope, subject to exceptions granted by the FedRAMP Director with OMB approval:

1. Systems used only for a single agency's operations, hosted on cloud infrastructure/platform, not offered as a shared service and not operating under a shared responsibility model
2. Social media and communications platforms used under agency social media policy
3. Search engines
4. Widely available services supplying commercially available information that do not collect federal information
5. Ancillary services whose compromise would pose negligible risk (e.g. external measurement or public-feed ingestion)
6. Any other category identified by the FedRAMP Board with the concurrence of the Federal CIO

Scope is a **use-case** determination made by the agency, not a property of the product: the same service can be in scope for one agency use and out of scope for another. FedRAMP deliberately publishes no list of always-out-of-scope services. Note also CR26's framing that a commercial cloud service is normally a *component within* a federal information system, not itself a federal information system, unless built by or operated under contract on behalf of the government.

## Structure and requirements

### Certification Classes (CR26)

| Class | Intended for | Agency presumption of adequacy (FedRAMP's own guidance) |
|---|---|---|
| A | Commercial services with a mature security program entering the federal market; smallest up-front and ongoing commitment | Pilots, configuration/testing, negligible-risk uses such as public information |
| B | The next step up in assurance, for providers scaling commitment as agency interest grows | Most Low-impact agency systems; some Moderate/High with compensating controls |
| C | Providers with an active federal customer base; FedRAMP warns against starting here without an agency contract that requires it | Most Low/Moderate agency systems; some High with compensating controls |
| D | Highest assurance. The 20x Class D pipeline is "coming in 2027"; Rev5 Class D remains available through Agency Certification | Most agency systems regardless of impact level, with appropriate compensating controls |

Classes describe the **level of assurance information the provider commits to supply**, not how secure the service is, and FedRAMP warns explicitly against treating them as one-for-one substitutes for Low/Moderate/High. Agencies still categorize their own system under FIPS 199/200 first.

### Key Security Indicators (20x)

46 KSIs across 10 families, each mapped to related SP 800-53 Rev. 5 controls:

| Family | KSIs | Focus |
|---|---|---|
| KSI-CNA Cloud Native Architecture | 8 | Defined functionality/privileges, enforced intended state, minimized attack surface, logical networking, restricted traffic |
| KSI-SVC Service Configuration | 8 | Automated configuration and secret management, residual-risk prevention, data removal, securing information, integrity validation |
| KSI-IAM Identity and Access Management | 6 | Automated account management, passwordless methods, least privilege, just-in-time authorization, non-user authentication |
| KSI-MLA Monitoring, Logging and Auditing | 5 | Log access authorization, configuration evaluation, event types, SIEM capability, log review |
| KSI-PIY Policy and Inventory | 5 | Inventories, executive support, security investment, security in the SDLC, vulnerability disclosure |
| KSI-CMT Change Management | 4 | Logging changes, redeploy vs modify, change procedures, validation through deployment |
| KSI-RPL Recovery Planning | 4 | Backups aligned to objectives, recovery plan alignment, objective review, tested recovery |
| KSI-INR Incident Response | 3 | After-action reports, IR procedure review, past-incident review |
| KSI-SCR Supply Chain Risk | 2 | Mitigating and monitoring supply chain risk |
| KSI-CED Cybersecurity Education | 1 | Reviewing all training |

**Class A** must address only 7 named KSIs (KSI-CMT-LMC, KSI-CNA-RNT, KSI-CED-RAT, KSI-IAM-AAM, KSI-IAM-APM, KSI-INR-RIR, KSI-SVC-SIN) alongside a short list of mandatory rules. **Classes B and C** must include **all 46** in a FedRAMP independent assessment at least once per year.

### Class A: reuse of an existing framework

Class A is the on-ramp. The provider must hold a completed certification or equivalent from an **approved alternative security framework within the past 12 months** — FedRAMP Rev5 (including FedRAMP Ready) at any historical impact level, **SOC 2 Type II**, or **GovRAMP** at any impact level — and supply the underlying materials (for SOC 2: the complete report, bridge/gap letter, audit engagement documentation, and the schedule for the next report). FedRAMP is explicit that "see the SOC 2 report" is not an acceptable answer; each FedRAMP rule needs its own summary.

### Incident reporting clocks (CR26)

Reportability turns on whether an incident affects, or is likely to affect, the **confidentiality or integrity of federal customer data**. Severity uses a **Potential Agency Impact N-rating (PAIN)** from N1 (minimal customer effect) to N5 (debilitating effect on more than one agency). If the provider does not promptly estimate a rating, **PAIN-5 timeframes apply by default**.

| Report | Class C: PAIN-5/4/3 | Class C: PAIN-2 | Class C: PAIN-1 | Class B: all PAIN ratings |
|---|---|---|---|---|
| Initial Incident Report (IEC-CSO-IIR) | 1 hour | 24 hours | 1 business day | 6 hours (PAIN-5/4/3); 1 business day (PAIN-2/1) |
| Ongoing Incident Reports (IEC-CSO-OIR) | every 6 hours | every 24 hours | every business day | every business day |
| Final Incident Report (IEC-CSO-FIR) | 6 hours | 1 business day | 1 business day | 3 business days |

For Class A, evaluating reportability and the Final Incident Report are mandatory; initial and ongoing reports are recommended.

### Vulnerability detection and response

POA&Ms are gone, replaced by a list of accepted weaknesses (marked and reported as *accepted vulnerabilities* under the Vulnerability Evaluation and Reporting ruleset). Providers must run persistent detection and response, with class-scaled cadences and remediation windows keyed to PAIN plus exploitability and internet reachability:

| Requirement | Class A | Class B | Class C | Class D |
|---|---|---|---|---|
| Verify/validate machine-based information resources | every month (should) | every 7 days | every 3 days | not specified |
| Verify/validate non-machine-based resources | every 3 months (all classes) | every 3 months | every 3 months | every 3 months |
| Mitigate/remediate PAIN-5, likely exploitable + internet-reachable | 4 days | 4 days | 2 days | 12 hours |
| Mitigate/remediate PAIN-3, likely exploitable + internet-reachable | 32 days | 32 days | 16 days | 8 days |

### Ongoing Certification and change

- **Ongoing Certification Report** to all necessary parties **every 3 months**, human-readable, covering the whole period, with a published next-report date and a feedback mechanism.
- **Quarterly Review** — a synchronous session every 3 months: mandatory for Classes C and D, recommended for Class B; scheduled 3–10 business days after the report.
- **Significant Change Notification**: routine recurring changes are exempt; **adaptive** changes notified within **10 business days after** completion; **transformative** changes notified **30 business days before** (initial plans), **10 business days before** (final plans), **5 business days after** finishing and again after verification/validation, with updated documentation published within **30 business days**. 12 months of notifications retained.
- **Cryptographic Module Use**: Class D **must** use modules with active NIST CMVP validations; Class C **should**; Classes A and B **may**. Providers must document the modules used. FIPS 140 is now expected to protect sensitive data rather than presumed necessary for all federal data and metadata.

## Assessment, certification and evidence

- **Independent assessors** must hold and maintain **A2LA Cybersecurity Inspection Body Program** accreditation and comply with **A2LA R311**, pass an annual surveillance assessment (75 days to close nonconformances, otherwise listed in Remediation on the Marketplace) and a full reassessment at least every 2 years.
- **Classes B/C/D** require an independent verification and validation assessment of all applicable FedRAMP rules at least once per year (the first is the "initial assessment", subsequent ones "annual assessments"). Assessment by FedRAMP itself is extremely rare and limited to explicitly prioritized services.
- **Class A** relies on the underlying alternative framework's assessment expectations rather than a separate FedRAMP independent assessment.
- **Evidence model**: verification = evidence that documented measures are implemented; validation = evidence that they are effective. 20x expects automated verification and validation of KSIs, machine-readable schemas, and **metrics trended over time** — not point-in-time artifacts.
- **Package**: Certification Package Overview, Security Decision Record, implementation/validation/assessment information per rule/control/KSI, and a real or example Ongoing Certification Report. Word/Excel templates are being retired in favor of JSON (optionally OSCAL).

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| 23 Dec 2022 | FedRAMP Authorization Act enacted (PL 117-263) |
| 25 Jul 2024 | OMB M-24-15 issued; 2011 memorandum rescinded; JAB P-ATO model retired |
| Mar 2025 | FedRAMP 20x announced |
| Apr–Sep 2025 | 20x Phase 1 (Low pilot); 26 packages; first pilot authorizations late July 2025 |
| 18 Nov 2025 – Mar 2026 | 20x Phase 2 (Moderate pilot); 14 submissions; first cohort authorized 6 March 2026 |
| 24–25 Jun 2026 | Consolidated Rules for 2026 launched; 20x becomes generally available |
| 4 Jul 2026 | CR26 optional early adoption begins |
| 6 Jul 2026 | Marketplace listings open for Initial Implementation providers |
| 28 Jul 2026 | FedRAMP Ready goes legacy — no new Ready submissions |
| 3 Aug 2026 | 20x Class A pipeline opens |
| 10 Aug 2026 | Temporary Rev5 Program Certification pipelines open (Ready Conversion, Lost Sponsor) for Classes B and C; grace period ends 19 Feb 2027 |
| 31 Aug 2026 | 20x Class B and Class C pipelines open |
| 13 Sep 2026 | Latest CR26 release (2026.09.13.02): clarifications, plus the Rev5 package-ruleset default grace date moved from 1 Jan to 1 Jul 2027 |
| 1 Jan 2027 | **CR26 becomes mandatory for all stakeholders**; existing Rev5 certifications must have adopted the new rules |
| 11 Jun 2027 | FedRAMP stops accepting applications for new Rev5 Certifications |
| FY27 Q1–Q2 (FedRAMP est.) | 20x Phase 4 — Class D pilot; the 20x Class D Program Certification pipeline is listed as "coming in 2027" |
| 31 Dec 2028 | Earliest stated end of existing Rev5 Certifications ("remain active until at least") |

Rev5 obligations phase in per ruleset: Addressing FedRAMP Communication from 5 Jan 2026, Secure Configuration Guide from 1 Mar 2026, Marketplace Listing 4 Jul 2026, Vulnerability Detection/Response and Vulnerability Evaluation/Reporting 7 Dec 2026, and the remainder obtainable from 1 Jan 2027 with maintenance dates running to 1 Aug 2027 (Certification Package Overview moved to 1 Jul 2027 in September 2026) and grace periods into February 2028. The 20x rulesets carry the same early dates.

CR26 republishes the Rev5 baselines as per-class control lists drawn from NIST SP 800-53 Rev. 5: a Security Decision Record must cover at least **155 controls for Class B, 322 for Class C and 409 for Class D**. FedRAMP has removed most FedRAMP-defined organizational parameters from those baselines and expects providers to set their own.

## State and defense analogues

| Program | Basis | Levels | Notes |
|---|---|---|---|
| **GovRAMP** (formerly StateRAMP, renamed in 2025 *(verify exact date)*) | Non-profit member program for state, local, tribal and education buyers | Low, Moderate and High impact levels, reached through Security Snapshot, Core, Ready and Authorized/Provisional verification | Baselines built on NIST SP 800-53 Rev. 5; Ready and Authorized verification need an independent assessment by a GovRAMP-approved 3PAO; authorized products are published on a participants list. CR26 accepts a GovRAMP certification at any impact level as the alternative framework for **FedRAMP Class A**, which GovRAMP recorded in July 2026 |
| **TX-RAMP** (Texas DIR) | SB 475 (87th Legislature); Tex. Gov't Code § 2054.0593 — state agencies may only enter or renew cloud contracts that comply, from 1 January 2022 | Level 1 (public/non-confidential or low impact); Level 2 (confidential/regulated data, moderate or high impact) | Reciprocity: FedRAMP Low or StateRAMP Category 1 → Level 1; FedRAMP Moderate or StateRAMP Category 2 → Level 2. Provisional status allows contracting for up to 18 months |
| **DoD Cloud Computing SRG** (DISA) | DoD policy, issued separately from FedRAMP | Impact Levels 2, 4, 5 and 6 *(verify)* | DoD issues its own Provisional Authorization and layers DoD-specific requirements and CNSSI 1253 overlays on the FedRAMP baselines *(verify — DISA's document library needs DoD credentials, so no part of this row could be confirmed against the SRG text itself)* |

## Key obligations for security/GRC teams

1. **Decide whether FedRAMP applies at all** — it is an agency use-case test under M-24-15, not a product property. See [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md) and [../regulations/us-fisma-federal-cyber.md](../regulations/us-fisma-federal-cyber.md).
2. **Pick the class, then the path.** Class A via Program Certification is the normal entry point; Class C or D without an agency contract demanding it is an expensive mistake. Rev5 Agency Certification closes to new applicants on 11 June 2027.
3. **Re-plan any in-flight Rev5 work against the CR26 deadline table.** Existing certifications must adopt the new rules by 1 January 2027; POA&Ms, SSP templates, and monthly-scan-centric continuous monitoring all change. Use [certification-readiness](../../workflows/certification-readiness.md).
4. **Harvest the SOC 2 Type II you already have.** Keep it current within 12 months and map its evidence to the 7 Class A KSIs and mandatory rules. See [soc2-readiness](../../skills/soc2-readiness/SKILL.md) and [soc2-tsc.md](soc2-tsc.md).
5. **Build KSI validation as engineering, not GRC paperwork** — automated collection, drift detection, machine-readable schemas, and metrics trended over time. Map KSIs to the related SP 800-53 Rev. 5 controls you already operate ([nist-800-53.md](nist-800-53.md), [control-mapping](../../skills/control-mapping/SKILL.md)).
6. **Rewire incident response to the PAIN clocks** — a 1-hour initial report at Class C for PAIN-5/4/3, with PAIN-5 as the default when no rating is made. Pre-stage the report schema and the recipient list. See [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
7. **Replace POA&M hygiene with vulnerability detection/response cadences and an Accepted Weaknesses list**, tracked against the class-specific remediation windows. Exceptions belong in [exception-management](../../skills/exception-management/SKILL.md).
8. **Stand up the Ongoing Certification rhythm**: quarterly report, quarterly review, significant-change notifications on their own clocks, and a monitored FedRAMP security inbox. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).
9. **Contract the assessor early** and confirm current A2LA accreditation and FedRAMP Recognition before signing. See [audit-preparation](../../skills/audit-preparation/SKILL.md) and [control-testing](../../skills/control-testing/SKILL.md).
10. **Treat GovRAMP and TX-RAMP as separate programs with their own clocks**, and check reciprocity in both directions before promising a state customer that a federal certification suffices.

## Interplay

- **FISMA / SP 800-53**: FedRAMP does not displace an agency's FISMA duties — the statutory presumption of adequacy covers the assessment materials, not the agency's own responsibility. See [../regulations/us-fisma-federal-cyber.md](../regulations/us-fisma-federal-cyber.md) and [nist-800-53.md](nist-800-53.md).
- **SOC 2**: now a formally recognized input to FedRAMP Class A, which makes the SOC 2 scope boundary and report timing a FedRAMP planning problem rather than a separate exercise. See [soc2-tsc.md](soc2-tsc.md).
- **ISO/IEC 27001**: not an approved alternative framework for Class A, but a useful base for the KSI-PIY and KSI-CED families. See [iso-27001-2022.md](iso-27001-2022.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
- **CMMC / SP 800-171**: a different regime for contractor-held CUI, frequently confused with FedRAMP. A FedRAMP certification does not confer CMMC status. See [nist-800-171-cmmc.md](nist-800-171-cmmc.md).
- **Data-specific federal regimes**: CJIS and IRS Pub. 1075 impose their own cloud conditions on top of FedRAMP for criminal-justice and federal tax information. See [../regulations/us-cjis-security-policy.md](../regulations/us-cjis-security-policy.md) and [../regulations/us-irs-pub-1075.md](../regulations/us-irs-pub-1075.md).
- **Third-party risk**: an agency's use of a certified service still requires its own risk determination, and a provider's certification says nothing about its subservice organizations. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).

## Primary sources

- FedRAMP Authorization Act (Sec. 5921 of PL 117-263), codified at 44 U.S.C. §§ 3607–3616, as reproduced section by section by FedRAMP — https://www.fedramp.gov/2026/authority/law/ (legal text; fetched)
- Public Law 117-263, James M. Inhofe National Defense Authorization Act for FY2023 — https://www.govinfo.gov/app/details/PLAW-117publ263 (legal text; link checked, not separately fetched)
- OMB Memorandum M-24-15, "Modernizing the Federal Risk and Authorization Management Program", 25 July 2024 — https://www.whitehouse.gov/wp-content/uploads/2024/07/M-24-15-Modernizing-the-Federal-Risk-and-Authorization-Management-Program.pdf (OMB policy; link checked) and its scope and rescission text at https://www.fedramp.gov/2026/authority/m-24-15/ (fetched)
- CR26 — Important Dates — https://www.fedramp.gov/2026/timeline/ (publisher rules; fetched)
- CR26 — Changelog, latest release 2026.09.13.02 of 13 September 2026 — https://www.fedramp.gov/2026/changelog/ (publisher rules; fetched)
- CR26 — FedRAMP Definitions — https://www.fedramp.gov/2026/definitions/ (publisher rules; fetched)
- CR26 — What's Changing in 2026 (terminology, POA&M removal, FIPS 140 framing, Rev5 end dates) — https://www.fedramp.gov/2026/providers/updating/changes/ (publisher rules; fetched)
- CR26 — Certification Classes, agency view — https://www.fedramp.gov/2026/agencies/use/classes/ (publisher rules; fetched)
- CR26 — Choosing a Path — https://www.fedramp.gov/2026/providers/start/path/ and Choosing a Class — https://www.fedramp.gov/2026/providers/start/class/ (publisher rules; fetched)
- CR26 — FedRAMP Certification ruleset (20x), including Class A approved alternative frameworks — https://www.fedramp.gov/2026/providers/20x/rules/fedramp-certification/ (publisher rules; fetched)
- CR26 — Incident Evaluation and Communication ruleset (PAIN ratings and reporting clocks) — https://www.fedramp.gov/2026/providers/20x/rules/incident-evaluation-and-communication/ (publisher rules; fetched)
- CR26 — Vulnerability Detection and Response ruleset — https://www.fedramp.gov/2026/providers/20x/rules/vulnerability-detection-and-response/ (publisher rules; fetched)
- CR26 — Collaborative Continuous Monitoring — https://www.fedramp.gov/2026/providers/20x/rules/collaborative-continuous-monitoring/, Significant Change Notification — https://www.fedramp.gov/2026/providers/20x/rules/significant-change-notification/, Cryptographic Module Use — https://www.fedramp.gov/2026/providers/20x/rules/cryptographic-module-use/, Independent Verification and Validation — https://www.fedramp.gov/2026/providers/20x/rules/independent-verification-and-validation/ (publisher rules; each fetched)
- CR26 — Rev5 Certification ruleset, including the per-class SP 800-53 Rev. 5 control lists counted above — https://www.fedramp.gov/2026/providers/rev5/rules/fedramp-certification/ (publisher rules; fetched)
- CR26 — Rev5 ruleset deadlines — https://www.fedramp.gov/2026/providers/updating/deadlines/rev5/ (publisher rules; fetched)
- CR26 — FedRAMP Recognition rules for independent assessors (A2LA accreditation, R311, surveillance) — https://www.fedramp.gov/2026/assessors/rules/fedramp-recognition/ (publisher rules; fetched)
- CR26 — Key Security Indicators reference — https://www.fedramp.gov/2026/reference/20x/b/key-security-indicators/ (publisher rules; fetched)
- FedRAMP 20x program page and phase recaps — https://www.fedramp.gov/20x/ (publisher page; fetched)
- FedRAMP blog, "Propelling Change: FedRAMP Launches Consolidated Rules for 2026", 25 June 2026 — https://www.fedramp.gov/2026-06-25-propelling-change-fedramp-launches-consolidated-rules-for-2026/ (publisher page; fetched)
- GovRAMP — Authorized verification https://govramp.org/authorized, FAQs https://govramp.org/faqs, program changelog https://govramp.org/changelog (publisher pages; fetched — the rename date is not stated on any of them)
- Texas SB 475, 87th Legislature, adding Tex. Gov't Code § 2054.0593 and the 1 January 2022 contract date — https://capitol.texas.gov/tlodocs/87R/billtext/html/SB00475F.HTM (legal text; fetched)
- Texas DIR, TX-RAMP eligibility and requirements (levels, reciprocity, provisional status) — https://dir.texas.gov/information-security/texas-risk-and-authorization-management-program-tx-ramp/tx-ramp-eligibility (regulator guidance; fetched)
- DoD Cloud Computing SRG, DISA document library — https://www.cyber.mil/dccs/ (publisher page; **not fetched** — the document library requires DoD credentials, so the SRG row above is unverified)

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
