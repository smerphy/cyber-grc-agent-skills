# Children's Online Privacy Protection Act (COPPA) and the amended COPPA Rule (15 U.S.C. §§ 6501–6506; 16 CFR Part 312)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Children's Online Privacy Protection Act of 1998 (Pub. L. 105–277, div. C, title XIII), codified at 15 U.S.C. §§ 6501–6506; implemented by the FTC's COPPA Rule, 16 CFR Part 312 |
| Regulator | Federal Trade Commission (FTC), enforcing under the FTC Act; state attorneys general may sue as parens patriae (§ 6504); banking, credit-union, aviation, agriculture regulators enforce for their own institutions (§ 6505(b)) |
| Status and key dates | Statute enacted 21 Oct 1998; original Rule issued 3 Nov 1999, effective 21 Apr 2000; amended 2013 (78 FR 4008, 17 Jan 2013); amended again by final rule at 90 FR 16918 (22 Apr 2025), **effective 23 Jun 2025, general compliance date 22 Apr 2026** (now in force) |
| Who is covered | Commercial "operators" of websites/online services (incl. apps, connected toys) that are **directed to children under 13**, or that have **actual knowledge** they collect personal information from a child under 13; non-profits exempt from FTC Act § 5 are outside scope |
| Core model | Notice + verifiable parental consent (VPC) before collection, use or disclosure; parental review/deletion rights; data-minimisation bar on conditioning participation; reasonable security; retention limits |
| 2025 additions | Separate VPC for third-party disclosure (targeted advertising); biometric and government identifiers added to personal information; new "mixed audience" definition; written information security program; written data-retention policy; safe-harbor transparency and reporting |
| Penalties | Rule violations treated as violations of an FTC trade-regulation rule; civil penalties up to **$53,088 per violation** (16 CFR § 1.98, 2025 inflation adjustment still in effect Sept 2026); injunctive orders, deletion, mandated privacy programs and independent audits |
| Breach notification | **None** — COPPA has no breach-reporting clock; state breach statutes and FTC Act § 5 apply instead |
| Safe harbour | FTC-approved self-regulatory programs (§ 6503; 16 CFR § 312.11): members deemed compliant if they follow approved guidelines; six programs approved as of Sept 2026 |
| Neighbours | Federal floor with express preemption of inconsistent state law (§ 6502(d)); state "kids codes" (California, Maryland) and proposed federal COPPA 2.0 / KIDS Act extend protection to teens |

## What it is

COPPA is the only US federal privacy statute aimed squarely at children online. Congress enacted it in 1998 and directed the FTC to write implementing regulations within a year (§ 6502(b)); the Commission issued the COPPA Rule on 3 November 1999, effective 21 April 2000. The Rule is the operative text: it defines "child" (under 13), "operator", "personal information", "website or online service directed to children" and "verifiable parental consent", and sets the notice, consent, access, minimisation, security and retention duties that the statute only sketches. A violation of the Rule is treated as a violation of an FTC rule defining an unfair or deceptive practice (§ 6502(c); 16 CFR § 312.9), which is what unlocks civil penalties.

The Rule was overhauled in 2013 (establishing the "mixed audience" category, treating screen names as online contact information, and clarifying that a child-directed operator is strictly liable when a third party collects personal information through its service while the third party is liable only with actual knowledge) and again in the **2025 final rule** (proposed January 2024 at 89 FR 2034; adopted by a 5–0 vote on 16 January 2025; published 22 April 2025). The 2025 amendments respond to ad-tech monetisation of children's data, biometrics and age-assurance technology. The FTC dropped two proposals — limits on push notifications to children and specific ed-tech/school provisions — while stating it remains concerned about engagement-driven design. Its 2026 posture pairs the amended Rule with a February 2026 policy statement encouraging age-verification technology.

## Who it covers / Scope

| Test | Detail (16 CFR § 312.2 unless noted) |
|---|---|
| Child | Individual under 13. Teens are outside COPPA (FTC FAQ H.9) — the gap the state kids codes and COPPA 2.0 target |
| Operator | Any person operating a commercial website or online service in interstate/foreign commerce who collects or maintains personal information from users, or on whose behalf it is collected (agents/service providers; or where the operator **benefits by allowing another person to collect** personal information directly from users). Non-profits exempt from FTC Act § 5 are excluded |
| Directed to children (para. 1) | Totality test: subject matter, visual content, animated characters, child-oriented activities and incentives, music, age of models, child celebrities, language, advertising; plus **empirical evidence of audience composition and intended audience** — marketing plans, representations to consumers or third parties, user reviews, and the age of users on similar services (the last four were added in 2025) |
| Directed to children (para. 2) | A service is **deemed** child-directed when it has actual knowledge it collects personal information directly from users of another child-directed service (third-party ad networks, SDKs, plug-ins) |
| Mixed audience (new definition, 2025) | Child-directed under para. 1 but children are **not the primary audience**, and no personal information (beyond § 312.5(c) exceptions) is collected before age-screening or another reasonably calculated means of determining age; screening must be **neutral** — no default age, no encouragement to falsify. Not deemed child-directed for visitors not identified as under 13 |
| Actual knowledge | General-audience services are covered only when they have actual knowledge a user is under 13; the Rule does not require age-gating, and a neutral age screen may be relied on even if users lie (FTC FAQ B.5); knowledge acquired later triggers the Rule from that point |
| Collection | Requesting/prompting submission; enabling public posting (unless reasonable measures delete all or virtually all personal information pre-publication); **passive tracking** |
| Personal information (11 categories) | Name; physical address; online contact information; screen/user name functioning as contact information; telephone number; **government-issued identifier** (SSN, state ID, birth certificate, passport — 2025); **persistent identifier** (cookie ID, IP address, device serial/ID); photo, video or audio containing a child's image or voice; geolocation to street and city; **biometric identifier** usable for automated/semi-automated recognition (fingerprints, handprints, retina/iris, genetic data incl. DNA, voiceprints, gait, facial templates/faceprints — 2025); any information combined with an identifier |
| Support for internal operations | Persistent-identifier collection without consent is allowed only for: maintaining/analysing the service, network communications, authentication/personalisation, **contextual** advertising and frequency capping, security/integrity, legal compliance, fulfilling a child's request — and never to contact an individual, behaviourally advertise or build a profile |
| Extraterritorial reach | Applies to foreign operators serving US children (the Cognosphere/HoYoverse action targeted a Singapore parent); foreign-based services directed to US children should assume coverage |
| Schools | A school may consent as the parent's agent only for the educational context; the operator must give the school the same direct notice and honour review/deletion; FERPA and state student-privacy laws run alongside (FTC FAQ N.1–N.2) |

## Core obligations

| Section | Obligation | Practical specifics |
|---|---|---|
| § 312.4(a)–(c) Direct notice | Reasonable efforts to deliver direct notice to the parent before collection, and on any **material change** to consented practices | Must state the items collected, uses, the identities or **specific categories of third parties** and purposes of disclosure, that the parent can consent to collection/use **without** consenting to third-party disclosure (unless integral to the service), the consent method, and deletion of contact details if consent is not given in a reasonable time |
| § 312.4(d) Online notice | Prominent, clearly labelled link on the home/landing page and at every collection point (and on the children's area of a general-audience site) | Names and contact details of **all operators** collecting through the service (one may be designated to respond); collection, use and disclosure practices incl. third-party identities/categories; the **written data-retention policy** (2025); internal-operations use of persistent identifiers; audio-file handling; parental review/deletion procedures |
| § 312.5(a) Consent | VPC before any collection, use or disclosure, and for material changes. **Separate VPC is required for disclosure to third parties** (targeted advertising, data sharing) unless disclosure is integral to the service (2025) | Consent to collection/use cannot be bundled with consent to disclosure; conditioning participation on disclosure consent has long been barred by FTC position |
| § 312.5(b) VPC methods | Method must be reasonably calculated, in light of available technology, to ensure the consenter is the parent | Enumerated: signed form (mail/fax/scan); payment-card transaction with per-transaction notification; toll-free call or video-conference with trained staff; government-ID check against databases with prompt deletion; **knowledge-based authentication** with dynamic multiple-choice questions (2025); **photo-ID plus facial-recognition match** confirmed by trained personnel, images promptly deleted (2025); and, only for operators that do **not** disclose, email-plus or **text-message-plus** confirmation (2025). Safe-harbor programs may approve additional methods for members (§ 312.5(b)(3)); anyone may petition the FTC (§ 312.12, 120-day determination) |
| § 312.5(c) Exceptions | Nine no-consent cases | Collecting contact details solely to seek consent (delete if not obtained in reasonable time); one-time response; multiple responses with parental notice; child-safety; security/liability/judicial process/law enforcement; persistent identifier solely for internal operations; audio files deleted immediately after fulfilling a request; para.-2 operators recognising a previously registered non-child user |
| § 312.6 Parental rights | On request: description of categories collected; the right at any time to refuse further use/collection and **direct deletion**; a means to review the information | Verify the requester is the parent; process must not be unduly burdensome; good-faith disclosure to a verified parent is immunised; service may be terminated if the parent refuses consent |
| § 312.7 Minimisation | May not condition a child's participation in a game, prize or activity on disclosing more information than reasonably necessary | Data-minimisation is an independent obligation, not merely a consent question |
| § 312.8 Security | Reasonable procedures for confidentiality, security and integrity; at minimum a **written information security program** proportionate to sensitivity, size and complexity (2025) | Program must: designate coordinating employee(s); identify and **at least annually** reassess internal/external risks; design safeguards scaled to volume, sensitivity and likelihood of compromise; regularly test and monitor; **at least annually** evaluate and modify. Before letting other operators/service providers/third parties collect or hold children's data, take reasonable steps to confirm capability **and obtain written assurances** |
| § 312.10 Retention and deletion | Retain only as long as reasonably necessary for the specific purpose; **no indefinite retention**; delete with reasonable measures against unauthorised access; maintain a **written data-retention policy** stating purposes, business need and a **timeframe for deletion**, published in the online notice (2025) | Retention schedules and deletion evidence become audit artefacts |
| § 312.11 Safe harbor programs | Approved programs must ensure protections equal to §§ 312.2–312.8 and 312.10, run a mandatory independent assessment of each member **at least annually**, and impose discipline | 2025 transparency duties: public list of members and certified services by 21 Jul 2025, updated every six months; annual report to the FTC from 22 Oct 2025 (members, departures, complaints, assessment results, discipline, approved consent methods); proposed guideline modifications by 22 Oct 2025; three-yearly capability reports from 22 Apr 2028; records kept ≥ 3 years. Approved programs (Sept 2026): CARU, ESRB, iKeepSafe, kidSAFE, PRIVO, TRUSTe |

## Enforcement and penalties

- **Mechanism.** Rule violations are enforced as trade-regulation-rule violations under the FTC Act (§ 6502(c), § 6505(d); 16 CFR § 312.9). Civil-penalty complaints are filed by the Department of Justice on FTC referral in federal court; the FTC also uses administrative orders for related FTC Act § 5 counts (dark patterns, unfair defaults).
- **Penalty ceiling.** Up to **$53,088 per violation** under 16 CFR § 1.98 (adjusted 17 Jan 2025; still the operative figure in the September 2026 eCFR). The FTC's FAQ lists the factors it weighs: egregiousness, prior violations, number of children, amount and type of data, use, third-party sharing, company size; the FAQ notes outcomes have ranged from no penalty to millions of dollars.
- **State enforcement.** State AGs may sue as parens patriae for injunctions, compliance, damages/restitution, after notice to the FTC (§ 6504). No private right of action in the statute.
- **Preemption.** § 6502(d) bars state or local liability inconsistent with COPPA's treatment of covered activities — the fault line in litigation over state kids codes.
- **Safe-harbor credit.** The FTC weighs a member's participation history, remediation and program discipline when deciding whether to investigate (§ 312.11(h)).

| Action | Date | Outcome |
|---|---|---|
| Epic Games (Fortnite) | Dec 2022 | **$275M** COPPA civil penalty (largest for any FTC rule at the time) plus $245M refunds for dark patterns; child-directed finding despite "general audience" positioning; voice/text chat off by default for minors; deletion of unlawfully collected data; comprehensive privacy program with independent audits |
| Cognosphere / HoYoverse (Genshin Impact) | Jan 2025 | **$20M**; collection from known under-13 users without VPC; loot-box sales to under-16s barred without parental consent; Singapore parent named |
| Disney (YouTube channels) | Sept 2025 (order approved Dec 2025) | **$10M**; mislabelling child-directed videos as not "Made for Kids" enabled targeted-ad data collection via the platform; mandated video-review/audience-designation program; confirms FTC FAQ position that whoever posts child-directed content on a platform is an operator if personal information is collected on its behalf |

## Timeline and status

| Date | Event |
|---|---|
| 21 Oct 1998 | COPPA enacted (Pub. L. 105–277) |
| 3 Nov 1999 / 21 Apr 2000 | Original COPPA Rule issued / effective (64 FR 59888) |
| 17 Jan 2013 | 2013 amendments published (78 FR 4008) |
| 11 Jan 2024 | NPRM for current amendments (89 FR 2034) |
| 16 Jan 2025 | Commission votes 5–0 to adopt final rule |
| 22 Apr 2025 | Final rule published, 90 FR 16918 |
| 23 Jun 2025 | Amended Rule effective (60 days after publication); during the transition operators could comply with either the pre-2025 or the revised Rule |
| 21 Jul 2025 | Safe-harbor programs must publish member lists (§ 312.11(d)(4)) |
| 22 Oct 2025 | First annual safe-harbor report and proposed guideline modifications due (§ 312.11(d)(1), (g)) |
| 25 Feb 2026 | FTC COPPA policy statement: no enforcement against general- or mixed-audience operators that collect personal information **solely** to determine age without prior VPC, provided the data is used only for age determination, retained no longer than necessary and promptly deleted, and shared only with third parties vetted and bound by written assurances |
| 5 Mar 2026 | Senate passes S. 836, COPPA 2.0 (Children and Teens' Online Privacy Protection Act) — reported to extend protection to under-17s and ban targeted advertising to minors (verify against enrolled text; secondary sources; House action pending) |
| **22 Apr 2026** | **General compliance date** for the amended Rule — enforcement of the new requirements available from this date |
| 29 Jun 2026 | House passes H.R. 7757, KIDS Act (267–117), consolidating a House version of KOSA, COPPA 2.0 and other bills; drops KOSA's "duty of care"; Senate sponsors have rejected the House text — **no federal teen-privacy law enacted as of Sept 2026** |
| 22 Apr 2028 | First three-yearly safe-harbor capability report (§ 312.11(f)) |

State analogues (as of Sept 2026): **California Age-Appropriate Design Code Act** (Cal. Civ. Code § 1798.99.31 and related sections) — after the Ninth Circuit's 12 Mar 2026 *NetChoice v. Bonta* opinion the age-estimation requirement (§ 1798.99.31(a)(5)) and the statute's valid remainder may be enforced, while the DPIA/risk-mitigation requirement, the data-use restrictions (§ 1798.99.31(b)(1)–(4)) and the dark-patterns bar (§ 1798.99.31(b)(7)) remain enjoined pending remand (secondary source). **Maryland Kids Code** (Ch. 461 of 2024, Com. Law §§ 14–4601 et seq.) — in effect 1 Oct 2024; covers for-profit entities offering online products reasonably likely to be accessed by children **under 18**; DPIAs required by 1 Apr 2026 for existing products and before offering new ones; violations are unfair, abusive or deceptive trade practices under the Maryland Consumer Protection Act; facially challenged in *NetChoice v. Brown* (D. Md.) with no injunction in effect (verify). Comprehensive state privacy laws add opt-in rules for known-child data — see [us-state-privacy.md](us-state-privacy.md).

## Key obligations for security/GRC teams

1. **Classify every property and SDK**: child-directed, mixed-audience, or general-audience with actual-knowledge procedures; document the § 312.2 factor analysis and audience evidence, and re-run it when content, marketing or user demographics change. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Split the consent flow**: separate, unbundled VPC for third-party disclosure/targeted advertising; verify no persistent-identifier use exceeds "support for internal operations"; audit ad-tech and analytics SDK configurations against the contextual-only rule.
3. **Stand up the § 312.8 written information security program** — named coordinator, annual risk assessment, scaled safeguards, testing/monitoring, annual program review — and map it to existing ISO 27001 or NIST CSF 2.0 controls rather than building a parallel program. See [../../skills/risk-assessment/SKILL.md](../../skills/risk-assessment/SKILL.md), [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md).
4. **Write and publish the § 312.10 retention policy** with purpose, business need and deletion timeframe per data element; automate deletion and retain evidence. See [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).
5. **Vendor assurance**: before any service provider or third party collects or holds children's data, document capability due diligence and obtain **written assurances**; add COPPA clauses and internal-operations restrictions to contracts. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../templates/vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md).
6. **Age-assurance design**: neutral age screens; if using age-verification technology, meet the Feb 2026 policy-statement conditions (sole purpose, prompt deletion, vetted third parties) so the verification data itself does not create a COPPA violation.
7. **Parental rights operations**: verified review, refusal and deletion requests with SLAs; test the process — obstructive deletion handling was an Epic Games finding. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
8. **Run a children's-data DPIA** for new features (biometrics, voice, geolocation, chat) and, where Maryland or California applies, the statutory DPIA. See [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md) and [../../templates/dpia-template.md](../../templates/dpia-template.md).
9. **Horizon-scan** COPPA 2.0 / KIDS Act and state kids-code litigation quarterly; both would raise the protected age to teens and change ad rules. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).
10. **Safe-harbor decision**: weigh membership (annual independent assessment, enforcement credit under § 312.11(h)) against cost; membership now appears on public lists and in FTC reporting.

## Interplay

- **FTC Act § 5**: COPPA cases are routinely paired with unfairness/deception counts (dark patterns, unsafe defaults, misrepresented labelling), which reach teens and adults outside COPPA's under-13 scope.
- **GLBA Safeguards Rule**: the § 312.8 program mirrors the Safeguards Rule's structure (designated individual, written risk assessment, testing, periodic review); one program can satisfy both where a financial institution serves children. See [glba-ftc-safeguards.md](glba-ftc-safeguards.md).
- **State privacy laws and kids codes**: comprehensive state laws treat known-child data as sensitive data requiring opt-in consent; Maryland's and California's codes reach under-18s and add design and DPIA duties — see [us-state-privacy.md](us-state-privacy.md). Preemption under § 6502(d) is contested but unresolved.
- **Breach notification**: COPPA is silent; children's data breaches are governed by state breach statutes and FTC Act § 5 — see [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
- **GDPR / UK GDPR**: EU and UK regimes set their own child-consent ages and design duties (the UK's Age Appropriate Design Code and the children's higher-protection matters introduced by the Data (Use and Access) Act 2025) — a global product needs one children's-data architecture with jurisdiction-specific age thresholds. See [gdpr.md](gdpr.md) and [uk-data-protection.md](uk-data-protection.md).
- **EU Digital Services Act**: platform duties on protection of minors (a named systemic-risk category, with Commission guidelines of July 2025) complement COPPA's consent model for services also offered in the EU. See [eu-digital-services-act.md](eu-digital-services-act.md).
- **HIPAA / FERPA**: health apps for children and ed-tech may be inside HIPAA or FERPA as well; COPPA's school-consent path does not displace FERPA. See [hipaa.md](hipaa.md).

## Primary sources

- 15 U.S.C. Chapter 91 (§§ 6501–6506), 2023 edition, GPO govinfo — legal text (statute).
- 16 CFR Part 312, eCFR current text (as of 1 Sept 2026) — legal text (Rule as amended).
- Federal Register, Children's Online Privacy Protection Rule, final rule, 90 FR 16918 (22 Apr 2025), Doc. 2025-05904 — legal text and preamble (dates, rationale).
- 16 CFR § 1.98, eCFR — civil penalty schedule (90 FR 5581, 17 Jan 2025).
- FTC, "Complying with COPPA: Frequently Asked Questions" — regulator guidance.
- FTC press release, "FTC Finalizes Changes to Children's Privacy Rule…" (16 Jan 2025) — regulator guidance.
- FTC press release, "FTC Issues COPPA Policy Statement to Incentivize the Use of Age Verification Technologies…" (25 Feb 2026) — regulator guidance.
- FTC, COPPA Safe Harbor Program page — regulator guidance (approved programs).
- FTC press releases: Epic Games (19 Dec 2022), Cognosphere/HoYoverse (17 Jan 2025), Disney (2 Sept 2025) — enforcement records.
- Maryland General Assembly, HB 603 (2024) legislation page and Chapter 461 enrolled text — legal text (state analogue).
- Secondary (used only for pending legislation and litigation status): GovTrack pages for S. 836 and H.R. 7757; IAPP analysis of the KIDS Act (July 2026); Cooley client alert on *NetChoice v. Bonta* (30 Mar 2026). Congress.gov could not be fetched.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
