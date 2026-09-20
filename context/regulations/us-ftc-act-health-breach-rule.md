# US FTC Data-Security Enforcement — Section 5 of the FTC Act (15 U.S.C. § 45) and the Health Breach Notification Rule (16 CFR Part 318)

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | Section 5 of the Federal Trade Commission Act, 15 U.S.C. § 45 (unfair or deceptive acts or practices — "UDAP"); Health Breach Notification Rule ("HBNR"), 16 CFR Part 318, implementing § 13407 of the American Recovery and Reinvestment Act of 2009 (authority: 42 U.S.C. §§ 17937 and 17953) |
| Regulator | Federal Trade Commission (FTC), Bureau of Consumer Protection; civil-penalty suits filed by the Department of Justice on the FTC's behalf; state attorneys general joined the Premom HBNR matter |
| Status and key dates | Section 5: in force since 1914, unfairness test codified at § 45(n). HBNR: original rule 74 FR 42962 (25 Aug 2009), applies to breaches discovered on or after 24 Sep 2009 (16 CFR 318.8); amended rule 89 FR 47028 (30 May 2024), effective **29 July 2024**; FTC rescinded its 2021 health-app policy statement on 9 Sep 2026 as superseded by the 2024 amendments |
| Who is covered | Section 5: essentially every business "in or affecting commerce" except banks, savings and loan institutions, federal credit unions, common carriers, air carriers and packers/stockyards (§ 45(a)(2)). HBNR: non-HIPAA vendors of personal health records (PHRs), PHR related entities and their third party service providers, foreign or domestic, holding data on US citizens or residents |
| Core requirements | Section 5: no deceptive security/privacy claims; no "unfair" security failures (substantial, unavoidable, unoffset consumer injury). HBNR: notify individuals, the FTC and (≥500 residents of a state) the media of any unauthorized acquisition — including unauthorized disclosure — of unsecured PHR identifiable health information |
| Breach clocks | HBNR: without unreasonable delay and no later than **60 calendar days** after discovery (individuals, media, service-provider-to-vendor notice); FTC notice at the same time for ≥500 individuals, or an annual log within 60 days of year-end for <500 |
| Penalties | No civil penalty for a first-time Section 5(a) violation; consent or litigated order, then up to **$53,088 per violation** (16 CFR 1.98, adjusted 17 Jan 2025 and held at that level for 2026) for order violations under § 45(l). HBNR violations are Section 18 rule violations: **up to $53,088 per violation** from the first offense (§ 45(m)(1)(A)) |
| Order model | 20-year consent orders mandating a written information security program, board reporting, annual risk assessment, MFA, testing, biennial independent assessments, annual executive certification and incident reports to the FTC |
| Certifiable? | No. Compliance is evidenced by a reasonable, documented security program and truthful representations; FTC business guidance ("Start with Security", HBNR compliance guide) is the practical yardstick |
| Neighbours | GLBA Safeguards Rule (16 CFR Part 314) for non-bank financial institutions — see [glba-ftc-safeguards.md](glba-ftc-safeguards.md); HHS Breach Notification Rule for HIPAA entities — see [hipaa.md](hipaa.md); COPPA; state UDAP, breach-notification and consumer-health-data laws |

## What it is

Section 5 is the United States' general-purpose consumer-protection statute. It has no security clause: the FTC reads "deceptive" to reach false or unsubstantiated statements about privacy and security (privacy policies, "bank-level encryption", Privacy Shield/HIPAA seals) and "unfair" to reach security programs so inadequate that they cause substantial, unavoidable consumer injury. The unfairness test, adopted in the Commission's 1980 Policy Statement on Unfairness and codified at § 45(n), requires injury that is (1) substantial, (2) not reasonably avoidable by consumers and (3) not outweighed by countervailing benefits to consumers or competition; public policy may inform but not drive the finding. Two appellate decisions frame the doctrine: in *FTC v. Wyndham* (3d Cir., 24 Aug 2015) the Third Circuit affirmed the denial of Wyndham's motion to dismiss the FTC's unfairness complaint over lax security, while *LabMD v. FTC* (11th Cir., 6 Jun 2018) vacated a litigated Commission order because it directed a general "reasonable" program rather than the cessation of a specific unfair act — the reason modern consent orders list concrete controls.

The FTC's February 2026 RANSOMWARE Act report to Congress counts **more than 90 data-security enforcement actions** with favourable outcomes to date. Because the agency cannot obtain civil penalties for a first Section 5 violation and, since *AMG Capital v. FTC* (22 Apr 2021), cannot obtain restitution under § 13(b), most cases settle into long-running consent orders; monetary relief comes from § 19 (15 U.S.C. § 57b) redress suits, from civil penalties for violations of rules treated as Section 18 rules (the HBNR is one) and from order violations.

The HBNR is the FTC's one health-specific rule. Congress created it in 2009 to cover the personal-health-record market that HIPAA misses; the 2024 amendments rewrote its definitions so that health, fitness, fertility, sleep, mental-health and diet apps and connected devices are squarely covered, and made an unauthorized *disclosure* (for example, sending user health data to an advertising SDK) a reportable "breach of security". The FTC's first two HBNR actions — GoodRx (2023) and Premom (2023) — were advertising-pixel/SDK cases, not hacks.

## Who it covers / Scope

**Section 5.** Any "person, partnership, or corporation" acting in or affecting commerce, except the entities carved out in § 45(a)(2) (banks, savings and loan institutions, federal credit unions, common carriers under the Acts to regulate commerce, air carriers, and persons subject to the Packers and Stockyards Act). § 45(a)(4) extends UDAP jurisdiction to foreign-commerce conduct that causes reasonably foreseeable injury within the United States or involves material conduct in the United States — so a non-US app or hosting provider serving US users is reachable.

**HBNR (16 CFR 318.1–318.2).** Applies "irrespective of any jurisdictional tests in the FTC Act" to foreign and domestic entities that maintain information of US citizens or residents and are one of:

| Role | Definition (16 CFR 318.2) | Typical examples |
|---|---|---|
| Vendor of personal health records | Offers or maintains a PHR — an electronic record of PHR identifiable health information that has the *technical capacity* to draw information from multiple sources and is managed, shared and controlled by or primarily for the individual | Health, fitness, diet, fertility, sleep and mental-health apps; wearables that sync with user inputs; prescription-discount platforms (GoodRx) |
| PHR related entity | Offers products or services through the online service of a vendor of PHR or of a HIPAA entity offering PHRs, **or** accesses unsecured PHR identifiable health information in a PHR or sends such information to one | Device makers sending data into apps; integrations and plug-ins |
| Third party service provider | Provides services to a vendor or PHR related entity and accesses, maintains, stores, uses or discloses unsecured PHR identifiable health information as a result | Hosting, analytics, billing, customer-support and data-storage vendors |

Key definitional levers after the 2024 amendments:

- **PHR identifiable health information** is information relating to health condition, care or payment that identifies (or could reasonably identify) the individual and is created or received by a "covered health care provider", health plan, employer or clearinghouse — and "covered health care provider" now includes **any entity furnishing "health care services or supplies"**, defined as *any online service* (website, app, connected device) with mechanisms to track diseases, conditions, diagnoses, treatment, medications, vital signs, symptoms, bodily functions, fitness, fertility, sexual health, sleep, mental health, genetic information or diet. Information provided by the individual themselves counts.
- **Multiple sources**: the definition turns on *technical capacity*, and the FTC's compliance guidance treats an app that takes user input *and* can sync with a fitness tracker, or pull data through an API, as drawing on multiple sources.
- **Unsecured** means not protected by the technologies in HHS's guidance under 42 U.S.C. § 17932(h)(2) — in practice, not encrypted or destroyed. A lost laptop holding only encrypted PHRs is not a reportable breach. Paper-only breaches are outside the rule.
- **Exclusions**: HIPAA covered entities, and any entity *to the extent* it acts as a HIPAA business associate. An organisation can be a business associate for one product and a PHR vendor for another, in which case both the HHS and FTC rules apply to the respective data sets.

## Core obligations

### Section 5 — what enforcement treats as required

| Theory | What the FTC pleads | Illustrative matters |
|---|---|---|
| Deception | Security or privacy representations that are false or unsubstantiated: "appropriate safeguards", "award-winning security", HIPAA or Privacy Shield compliance seals, promises never to share health data with advertisers, promised breach-notice timing | GoodRx (HIPAA seal, ad sharing), GoDaddy (security claims, Privacy Shield), Blackbaud (safeguards promise, misleading breach notice), Illuminate (promised notification timing) |
| Unfairness | Failure to implement reasonable security causing or likely to cause substantial injury: no MFA, shared credentials, credentials in code repositories, no network monitoring, no segmentation, unpatched known vulnerabilities, weak or default passwords, plaintext or weak-hash storage, ignoring vendor vulnerability warnings, no incident-response process, indefinite data retention | Wyndham, LabMD, Drizly, Chegg, Blackbaud, GoDaddy, Illusory Systems (Nomad) |
| Rule violations (§ 45(m)) | HBNR (16 CFR 318.7 treats every violation as a Section 18 rule violation) — civil penalties available from the first violation | GoodRx ($1.5M), Premom ($100K) |

### Standard consent-order security programme (GoDaddy Decision and Order, finalised 21 May 2025 — representative of 2022–2026 orders)

| Provision | Requirement |
|---|---|
| Programme | Within 90 days, establish, implement and maintain a documented comprehensive information security programme protecting security, confidentiality and integrity of covered information |
| Governance | Provide the written programme and material evaluations to the board (or a committee, or a senior officer if no board) at least every 12 months and within 120 days of a Covered Incident; designate a qualified employee responsible for the programme |
| Risk assessment | Assess and document internal and external risks at least every 12 months and within 120 days of a Covered Incident |
| Safeguards | Design safeguards proportionate to data volume and sensitivity; MFA for all employees within 180 days (no SMS/phone-call factors), MFA or equivalent offered to customers; encryption, logging, monitoring, segmentation and patching provisions tailored to the complaint |
| Testing | Test and monitor safeguards at least every 12 months and within 120 days of a Covered Incident; vulnerability scanning at least daily; penetration testing at least every 12 months |
| Independent assessment | Initial and then **biennial assessments** by a qualified, objective, independent third-party assessor for **20 years**; assessor documents and findings producible to the FTC on 10 days' request |
| Certification | Annual certification to the FTC by a senior executive with information-security responsibility, listing all Covered Incidents |
| Incident reporting | Report to the FTC within **10 days** of notifying any US federal, state or local entity of a Covered Incident (date, facts, cause, data and individuals affected, remediation, copies of notices) |
| Duration | Order terminates 20 years from issuance (extended by any later complaint alleging violation); each violation exposes the company to a civil penalty of up to $53,088 |

Recurring add-ons: data-minimisation and public retention schedules (Drizly, Chegg, Blackbaud, Illuminate), deletion of unneeded data, consumer access/deletion rights (Chegg), bans on sharing health data for advertising plus affirmative express consent for other sharing (GoodRx, Premom), and — in Drizly — an order that **binds the CEO personally** and follows him to any future business collecting data on more than 25,000 individuals where he is majority owner, CEO or a senior officer with security responsibilities.

### HBNR — breach notification duties (16 CFR 318.3–318.6)

| Element | Requirement |
|---|---|
| Trigger (§ 318.2) | "Breach of security" = acquisition of unsecured PHR identifiable health information in a PHR without the individual's authorization, **including** acquisition resulting from a data breach **or an unauthorized disclosure**. Unauthorized *access* is presumed to be acquisition unless the entity has reliable evidence there was not, or could not reasonably have been, acquisition |
| Discovery (§ 318.3(c)) | First day the breach is known, or reasonably should have been known, to any employee, officer or agent other than the person committing it |
| Individuals (§ 318.3(a)(1), 318.4(a)) | Notify each affected US citizen or resident without unreasonable delay and **no later than 60 calendar days after discovery** — the 60 days is an outer limit, not a target |
| FTC (§ 318.4(b), 318.5(c)) | **≥500 individuals**: notify the FTC via its online Notice of Breach of Health Information **at the same time** as individual notice. **<500**: log and submit annually within 60 calendar days after the end of the calendar year |
| Media (§ 318.3(a)(3)) | If ≥500 residents of a state or jurisdiction are (or are reasonably believed to be) affected, notify prominent media outlets serving it within the same 60-day window — in addition to, not instead of, individual notice |
| Third party service providers (§ 318.3(b)) | Notify the official designated in the contract (else a senior official) at the vendor/PHR related entity, identify each affected customer, and **obtain acknowledgment of receipt**. Vendors and PHR related entities must tell their service providers up front that they are covered by the rule |
| Method (§ 318.5) | Written notice to last known address; email allowed where the individual chose email as primary contact, and must be clear and conspicuous and paired with text, in-app message or banner; next of kin for deceased users; substitute notice (90-day home-page posting or major media, plus a toll-free number live ≥90 days) if contact details for 10+ individuals fail; telephone allowed as an additional urgent channel |
| Content (§ 318.6) | Plain language: what happened (breach and discovery dates; **name or identity of third parties that acquired the data**, or a description if naming poses risk); data types; steps individuals should take; what the entity is doing to investigate, mitigate and prevent recurrence; contact options — at least two of toll-free number, email, website, in-app, postal address |
| Delay and proof (§ 318.4(c)–(d)) | Delay only where a law-enforcement official determines notice would impede a criminal investigation or damage national security (handled as under 45 CFR 164.528(a)(2)). **The burden of proving timely notice, and the necessity of any delay, sits with the entity** |
| Preemption (§ 318.1(b)) | Preempts contradictory state breach laws only; additional, non-contradictory state content requirements still apply and can be folded into a single notice |

## Enforcement and penalties

| Mechanism | Basis | Practical effect |
|---|---|---|
| Administrative complaint and cease-and-desist order | § 45(b) | Standard route for Section 5 security cases; almost always resolved by a consent agreement published for 30 days' comment, then finalised |
| Federal-court injunction | § 13(b), 15 U.S.C. § 53(b) | TRO, preliminary and permanent injunctions; **no** restitution or disgorgement after *AMG Capital* (2021) |
| Consumer redress | § 19, 15 U.S.C. § 57b | Refunds, rescission, damages after a rule violation or a final litigated order; no punitive damages |
| Civil penalties for rule violations | § 45(m)(1)(A); 16 CFR 318.7 | HBNR and other rules treated as Section 18 rules: up to **$53,088 per violation** with actual or fairly implied knowledge; each day of a continuing violation is a separate violation; court weighs culpability, history, ability to pay and effect on the business |
| Civil penalties for order violations | § 45(l) | Up to **$53,088 per violation**, per day for continuing violations, recovered by DOJ |
| Penalties after a litigated order against another company | § 45(m)(1)(B) | Available where a company had actual knowledge that a practice was already held unfair or deceptive in a litigated (not consent) cease-and-desist order — the statutory footing for the FTC's "Notices of Penalty Offenses" practice |
| Individual liability | Complaint naming officers | Drizly (2022–23) bound the CEO personally with obligations that travel to future employers |

The $53,088 figure is the inflation-adjusted maximum in 16 CFR 1.98 for penalties assessed after 17 Jan 2025 (90 FR 5580); on 15 Sep 2026 the FTC gave notice that amounts stay unchanged for 2026 at the 2025 levels (91 FR 58446), so $53,088 is the figure in the eCFR as of September 2026. Earlier years were $46,517 (2022, 87 FR 1070) and $51,744 (2024, 89 FR 1445) — always check the current § 1.98 table.

**HBNR enforcement record:** GoodRx (1 Feb 2023, N.D. Cal.; first HBNR action; $1.5M penalty; permanent ban on sharing health data for advertising; consent, retention-schedule and privacy-programme terms) and Easy Healthcare/Premom (17 May 2023, N.D. Ill.; $100,000 federal penalty plus $100,000 to Connecticut, DC and Oregon; SDK disclosures to AppsFlyer, Google, Umeng and Jiguang). Both were unauthorized-disclosure cases; neither involved an intrusion, and they remain the only HBNR enforcement actions as of September 2026.

## Timeline and status

| Date | Event |
|---|---|
| 26 Sep 1914 | FTC Act enacted (38 Stat. 719); § 45(a)(1) now declares unfair or deceptive acts or practices unlawful |
| 17 Dec 1980 | FTC Policy Statement on Unfairness (three-part test), later codified at § 45(n) |
| 25 Aug 2009 | HBNR final rule published (74 FR 42962; Part 318 text at 74 FR 42980); applies to breaches discovered on or after 24 Sep 2009 |
| 26 Jun 2012 → 24 Aug 2015 | *FTC v. Wyndham*: complaint filed 26 Jun 2012 (case later docketed in D.N.J. as 2:13-cv-01887), motion to dismiss denied 7 Apr 2014, affirmed by the Third Circuit 24 Aug 2015; stipulated order 11 Dec 2015 |
| 29 Jul 2016 → 6 Jun 2018 | *LabMD*: Commission opinion and final order; vacated by the Eleventh Circuit for lack of specificity |
| 22 May 2020 | FTC request for comment on HBNR as part of periodic rule review |
| 22 Apr 2021 | *AMG Capital*: Supreme Court holds § 13(b) does not authorise equitable monetary relief |
| 15 Sep 2021 | FTC Policy Statement on Breaches by Health Apps and Other Connected Devices (asserted HBNR coverage of health apps) |
| 22 Aug 2022 | Trade Regulation Rule on Commercial Surveillance and Data Security — ANPR under Section 18 (87 FR 51273); comment period extended to 21 Nov 2022 (87 FR 63738); public forum 8 Sep 2022 |
| Oct 2022 – Jan 2023 | Drizly (CEO named) and Chegg orders proposed and finalised |
| 1 Feb / 17 May 2023 | GoodRx and Premom — first HBNR civil-penalty actions |
| 9 Jun 2023 | HBNR NPRM (88 FR 37819); comments closed 8 Aug 2023; ~120 comments |
| 26 Apr 2024 | Commission votes 3–2 to finalise HBNR amendments (Holyoak and Ferguson dissenting) |
| 30 May 2024 / 29 Jul 2024 | Amended HBNR published (89 FR 47028) / effective |
| 1 Feb / 20 May 2024 | Blackbaud order proposed / finalised |
| 15 Jan / 21 May 2025 | GoDaddy order proposed / finalised (independent assessor, 20-year term) |
| 17 Jan 2025 | Civil-penalty maximums adjusted to $53,088 (90 FR 5580) |
| 1 Dec 2025 | Illuminate Education proposed order (data-security programme, data minimisation, deletion) |
| 16 Dec 2025 | Illusory Systems (Nomad) proposed order — $186M theft attributed to unreasonable security; company must return recovered funds; still awaiting final Commission approval as of September 2026 |
| 6 Feb 2026 | Second RANSOMWARE Act report: 90+ data-security actions to date |
| 5 Jun 2026 | Illuminate Education order finalised as modified after public comment (10.1M students' data; retention schedule; FTC notice of breaches reported elsewhere) |
| 9 Sep 2026 | FTC rescinds the 2021 health-app policy statement as obsolete because the 2024 rule text itself covers health apps and connected devices — **the rule is unchanged** |
| 15 Sep 2026 | FTC notice: civil-penalty maximums unchanged for 2026; 2025 levels ($53,088) continue to apply (91 FR 58446) |

**Status as of September 2026.** Section 5 enforcement continues under Chairman Andrew Ferguson, with unanimous 2–0 Commission votes on the 2025–2026 security matters (Illusory Systems, Illuminate); the substantive order template (programme, assessor, certification, incident reports) is unchanged from 2022–2024. The 2022 Commercial Surveillance ANPR has produced **no notice of proposed rulemaking**; treat it as dormant and check the FTC's current regulatory agenda before citing it as pending. The amended HBNR is in force, with no further amendment or rulemaking published since 2024 and no change to Part 318 in the eCFR; withdrawal of the 2021 policy statement (part of a wider clear-out of guidance documents) removed a guidance layer, not an obligation. The FTC's "Complying with FTC's Health Breach Notification Rule" guidance (July 2024, penalty figure updated January 2025) is the operative compliance reference.

## Key obligations for security/GRC teams

1. **Classify the organisation against the HBNR roles** (vendor of PHR, PHR related entity, third party service provider) for every consumer-facing health, fitness, fertility, sleep, mental-health or diet product, and separately map which data sets sit under HIPAA business-associate agreements. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Treat advertising and analytics SDKs, pixels and data-sharing as breach vectors.** Inventory every third-party recipient of identifiable health data and confirm affirmative express consent; an unauthorized disclosure is a reportable HBNR breach and a Section 5 deception count if the privacy policy said otherwise. See [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).
3. **Build the 60-day HBNR clock into incident response**, with discovery defined as first knowledge by any employee or agent, the ≥500 simultaneous-FTC-notice rule, media notice by state, the <500 annual log, and evidence for any delay. Pre-draft § 318.6-compliant notices naming third-party recipients. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md), [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md) and [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md).
4. **Flow HBNR terms into vendor contracts**: notify service providers of covered status, designate the breach-notice recipient, require identification of affected customers and written acknowledgment, and set a sub-60-day contractual clock so the vendor's obligation can still be met. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
5. **Substantiate every public security claim** (website, app-store listing, sales decks, seals, Privacy Shield/Data Privacy Framework and HIPAA statements) with evidence; unsupported claims are the most common deception count. Route claims through policy review — see [../../skills/policy-review/SKILL.md](../../skills/policy-review/SKILL.md).
6. **Run the consent-order programme voluntarily as the reasonableness benchmark**: written programme, named owner, annual board reporting, annual risk assessment, MFA without SMS or phone-call factors, daily vulnerability scanning, annual penetration testing, logging/monitoring, segmentation, retention schedule, and tested incident response. Map it to CIS Controls v8 or NIST CSF 2.0 for evidence — see [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md), [../frameworks/cis-controls-v8.md](../frameworks/cis-controls-v8.md), [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md).
7. **Act on vendor and researcher vulnerability warnings** and document closure; ignored warnings (Drizly, Illuminate, Nomad) are the fact pattern the FTC pleads as unfairness. Track deferred fixes as formal exceptions — see [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
8. **Minimise and schedule deletion of personal data**; publish a retention schedule if consumer-facing. Data retained without purpose converts a breach into an unfairness count and is now a standard order term.
9. **Brief executives on personal exposure**: officers who preside over known-deficient security can be named individually (Drizly) and carry obligations to future employers. Include FTC exposure in board risk reporting — see [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).
10. **Watch the docket**: HBNR periodic review, any revival of the Commercial Surveillance rulemaking, and the annual § 1.98 penalty adjustment. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

- **HIPAA / HHS Breach Notification Rule** ([hipaa.md](hipaa.md)): mutually exclusive by role — HIPAA covered entities and business associates (to that extent) are outside the HBNR; the HBNR borrows HIPAA's "unsecured" standard and law-enforcement-delay mechanics. Hybrid companies (business associate for one line, consumer app for another) run both regimes in parallel with different notice recipients.
- **GLBA Safeguards Rule** ([glba-ftc-safeguards.md](glba-ftc-safeguards.md)): the FTC's prescriptive security rule for non-bank financial institutions, with its own 30-day FTC notification for ≥500 consumers. Section 5 applies on top of it; consent-order programme terms mirror Safeguards Rule elements (qualified individual, written risk assessment, MFA, encryption, testing, board reporting).
- **State law** ([us-state-privacy.md](us-state-privacy.md)): all 50 states have breach statutes and many have UDAP "mini-FTC Acts"; the HBNR preempts only contradictory state breach rules, so state content and attorney-general notice requirements stack. State consumer-health-data statutes (for example Washington's My Health My Data Act, noted in hipaa.md) add consent duties the HBNR lacks (verify current provisions); Connecticut, DC and Oregon co-enforced Premom.
- **SEC cyber disclosure** ([sec-cyber-disclosure.md](sec-cyber-disclosure.md)): a public company's Form 8-K materiality determination and an HBNR/Section 5 incident run on separate clocks; a Blackbaud-style understated breach notice is an FTC deception theory and would also be tested under the SEC's disclosure rules.
- **GDPR** ([gdpr.md](gdpr.md)): FTC orders now routinely cite Privacy Shield/Data Privacy Framework misrepresentations; EU users' health data in a US app also falls under the GDPR breach regime (different trigger, recipient and clock — see gdpr.md).
- **Frameworks**: FTC orders do not name a framework, but the assessor must use "procedures and standards generally accepted in the profession"; NIST CSF 2.0, CIS Controls v8 and ISO/IEC 27001 are the usual scaffolds — see [../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md), [../frameworks/cis-controls-v8.md](../frameworks/cis-controls-v8.md), [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md).

## Primary sources

- 15 U.S.C. § 45 (Section 5 of the FTC Act) — legal text (U.S. Code, 2023 edition, govinfo): https://www.govinfo.gov/content/pkg/USCODE-2023-title15/html/USCODE-2023-title15-chap2-subchapI-sec45.htm
- 15 U.S.C. § 53 and § 57b (Sections 13(b) and 19) — legal text (govinfo): https://www.govinfo.gov/content/pkg/USCODE-2023-title15/html/USCODE-2023-title15-chap2-subchapI-sec53.htm and https://www.govinfo.gov/content/pkg/USCODE-2023-title15/html/USCODE-2023-title15-chap2-subchapI-sec57b.htm
- 16 CFR Part 318, Health Breach Notification Rule — legal text (eCFR, current as of September 2026): https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-318
- 16 CFR 1.98, civil-penalty maximums — legal text (eCFR, Part 1 Subpart L): https://www.ecfr.gov/current/title-16/chapter-I/subchapter-A/part-1/subpart-L
- Adjustments to Civil Penalty Amounts, 90 FR 5580 (17 Jan 2025) and Civil Penalty Inflation Adjustments, 91 FR 58446 (15 Sep 2026, amounts unchanged for 2026) — Federal Register: https://www.federalregister.gov/documents/2025/01/17/2025-01361/adjustments-to-civil-penalty-amounts and https://www.federalregister.gov/documents/2026/09/15/2026-18853/civil-penalty-inflation-adjustments
- Health Breach Notification Rule, final rule, 89 FR 47028 (30 May 2024, effective 29 Jul 2024) — Federal Register: https://www.federalregister.gov/documents/2024/05/30/2024-10855/health-breach-notification-rule
- Health Breach Notification Rule NPRM, 88 FR 37819 (9 Jun 2023) — Federal Register: https://www.federalregister.gov/documents/2023/06/09/2023-12148/health-breach-notification-rule
- Trade Regulation Rule on Commercial Surveillance and Data Security, ANPR 87 FR 51273 (22 Aug 2022) and extension 87 FR 63738 (20 Oct 2022) — Federal Register: https://www.federalregister.gov/documents/2022/08/22/2022-17752/trade-regulation-rule-on-commercial-surveillance-and-data-security
- FTC, Health Breach Notification Rule page (rule history, press releases) — regulator page: https://www.ftc.gov/legal-library/browse/rules/health-breach-notification-rule
- FTC, Complying with FTC's Health Breach Notification Rule (July 2024; penalty figure updated Jan 2025) — regulator guidance: https://www.ftc.gov/business-guidance/resources/complying-ftcs-health-breach-notification-rule-0
- FTC, Policy Statement on Unfairness (17 Dec 1980) — regulator policy: https://www.ftc.gov/legal-library/browse/ftc-policy-statement-unfairness
- FTC, "FTC Withdraws Obsolete Policy Statement" (9 Sep 2026, rescinding the 2021 health-app policy statement) — regulator press release: https://www.ftc.gov/news-events/news/press-releases/2026/09/ftc-withdraws-obsolete-policy-statement
- *In re GoDaddy Inc.*, Decision and Order (finalised 21 May 2025) — order text used for the consent-order programme table: https://www.ftc.gov/system/files/ftc_gov/pdf/2023133_godaddy_decisionandorder.pdf
- *FTC v. Wyndham Worldwide Corp.*, FTC case page (complaint 26 Jun 2012; Third Circuit opinion 24 Aug 2015; stipulated order 11 Dec 2015) — regulator case record: https://www.ftc.gov/legal-library/browse/cases-proceedings/1023142-wyndham-worldwide-corporation
- FTC press releases and case pages — regulator records: GoodRx (1 Feb 2023), Easy Healthcare/Premom (17 May 2023), Drizly (24 Oct 2022; final 10 Jan 2023), Chegg (31 Oct 2022; final 27 Jan 2023), Blackbaud (1 Feb 2024; final 20 May 2024), GoDaddy (15 Jan 2025; final 21 May 2025, Decision and Order PDF), Illusory Systems (16 Dec 2025), Illuminate Education (5 Jun 2026), RANSOMWARE Act report (6 Feb 2026), rescission of the 2021 health-app policy statement (9 Sep 2026), LabMD and Wyndham case pages — all under https://www.ftc.gov/
- *LabMD, Inc. v. FTC*, No. 16-16270 (11th Cir. 6 Jun 2018) — court opinion: https://media.ca11.uscourts.gov/opinions/pub/files/201616270.pdf
- *AMG Capital Management v. FTC*, No. 19-508 (U.S. 22 Apr 2021) — court opinion: https://www.supremecourt.gov/opinions/20pdf/19-508_l6gn.pdf
- Not fetched: the Third Circuit's *Wyndham* opinion itself (date and holding taken from the FTC case page) and the GoodRx, Premom, Drizly, Blackbaud, Illusory Systems and Illuminate order documents (terms taken from the FTC press releases and case pages listed above).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
