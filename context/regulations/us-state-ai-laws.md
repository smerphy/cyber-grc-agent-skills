# US State and Local AI Laws (Colorado ADMT Act, Texas TRAIGA, California ADMT/SB 53/AB 2013, Utah, Illinois, NYC Local Law 144)

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | Colorado C.R.S. 6-1-1701 et seq. (SB 24-205 as repealed and reenacted by SB 26-189; HB 26-1263 chatbots); Texas Bus. & Com. Code chs. 551–554 (HB 149, TRAIGA); California 11 CCR §§ 7001 et seq. (CPPA ADMT / risk-assessment / cybersecurity-audit regulations), Bus. & Prof. Code § 22757.10 et seq. (SB 53, TFAIA), Civil Code §§ 3110–3111 (AB 2013), Civil Rights Council FEHA regulations on automated-decision systems; Utah Code Title 13 chs. 72 and 75 (SB 149 of 2024, SB 226 of 2025); Illinois P.A. 103-0804 (HB 3773) (verify); NYC Admin. Code §§ 20-870–872 and 6 RCNY § 5-300 et seq. (Local Law 144 of 2021) |
| Regulators | State attorneys general (Colorado, Texas, California for SB 53); California Privacy Protection Agency (ADMT/audit regs); California Office of Emergency Services (SB 53 incident intake); Utah Division of Consumer Protection; NYC Department of Consumer and Worker Protection (DCWP) |
| Status (Sep 2026) | Texas TRAIGA in force since 1 Jan 2026; CPPA regs effective 1 Jan 2026 with ADMT compliance by 1 Jan 2027; Colorado ADMT Act effective 1 Jan 2027 (rules in formal rulemaking, comments to 26 Oct 2026); NYC LL 144 enforced since 5 Jul 2023; Utah in force (chapter 72 sunsets 1 Jul 2027 unless extended) |
| Who is covered | Developers and deployers of systems used in *consequential* / *significant* decisions (education, employment, housing, credit, insurance, health care, government services); frontier-model developers (SB 53); generative-AI developers (AB 2013); employers using AI in hiring (Illinois, NYC, California FEHA regs); anyone doing business in Texas (TRAIGA) |
| Model | No federal AI statute; a patchwork of state consumer-protection style laws with AG enforcement, cure periods, and safe harbours for recognised risk frameworks (NIST AI RMF, ISO/IEC 42001) |
| Penalties | Texas: $10,000–$12,000 (curable) / $80,000–$200,000 (uncurable) / $2,000–$40,000 per day continuing; SB 53: up to $1,000,000 per violation; Colorado: Colorado Consumer Protection Act remedies; Utah: up to $2,500 per violation; NYC: $500 first, $500–$1,500 subsequent |
| Private right of action | None created by Colorado, Texas, or SB 53 (SB 53 adds whistleblower actions); existing discrimination and consumer-protection claims survive |
| Federal overlay | Senate struck the proposed 10-year state-law moratorium from H.R. 1 on 1 Jul 2025 (99–1); Executive Order 14365 (11 Dec 2025) directs an AI Litigation Task Force to challenge "onerous" state AI laws and seeks preemptive federal legislation |
| Closest analogue | EU AI Act high-risk deployer duties (notice, human oversight, impact assessment) — see [eu-ai-act.md](eu-ai-act.md) |

## What it is

The United States has no comprehensive federal AI statute. Since 2023 states and cities have filled the gap with three families of law: (1) **algorithmic-discrimination / automated-decision laws** that impose documentation, notice, human-review and correction duties on developers and deployers of AI used in consequential decisions (Colorado, California CPPA regulations, NYC LL 144, Illinois, California FEHA regulations); (2) **transparency and safety laws** aimed at model developers (California SB 53 frontier frameworks and incident reporting; AB 2013 training-data disclosure); and (3) **disclosure and prohibited-use laws** modelled on consumer protection (Texas TRAIGA, Utah AI Policy Act).

Colorado illustrates the volatility: SB 24-205 (signed 17 May 2024) was the first comprehensive "high-risk AI" statute, with a 1 February 2026 start; SB 25B-004 (signed 28 Aug 2025) pushed that to 30 June 2026; SB 26-189 (signed 14 May 2026) then repealed and reenacted the whole part as an "automated decision-making technology" (ADMT) law effective 1 January 2027, dropping the reasonable-care / impact-assessment architecture in favour of documentation, notice, correction and human-review duties. Treat every state entry below as a moving target and re-verify before relying on it.

## Who it covers / Scope

| Law | Applicability test | Key exclusions |
|---|---|---|
| Colorado ADMT Act (SB 26-189) | Developers of *covered ADMT* (technology processing personal data that generates predictions, recommendations, scores etc. used to *materially influence* a consequential decision) marketed or contracted for that use; deployers using covered ADMT in a consequential decision affecting a Colorado consumer, employee or job applicant | Anti-malware, anti-virus and similar listed technologies; incidental, trivial or clerical uses; insurers subject to C.R.S. 10-3-1104.9 deemed compliant; HIPAA covered entities carved out of §§ 6-1-1701–1706 (conditions apply); routine academic administration |
| Texas TRAIGA | Any person who promotes, advertises or conducts business in Texas, produces a product or service used by Texas residents, or develops or deploys an AI system in Texas (§ 551.002). "Consumer" = Texas resident acting in an individual or household context, not employment or commercial | Insurance entities subject to unfair-discrimination insurance law and federally insured financial institutions complying with banking law (§ 552.056); no penalties for systems not yet deployed (§ 552.105(f)) |
| California CPPA regs | CCPA "businesses" using ADMT (technology that replaces or substantially replaces human decision-making) for a *significant decision*: financial or lending services, housing, education, employment or independent-contracting opportunities or compensation, health care (§ 7001(ddd)) | Housing decisions based solely on vacancy or payment receipt; opt-out exceptions under § 7221 (e.g., security/fraud, human-appeal alternatives — check conditions) |
| California SB 53 | *Frontier developer* = trained a model using more than 10^26 integer or floating-point operations; *large frontier developer* = frontier developer with affiliates' annual gross revenue above $500,000,000 | Smaller frontier developers owe only transparency reports and incident reports, not the full framework |
| California AB 2013 | Developers of generative AI systems or services (or substantial modifications) released on or after 1 Jan 2022 and made available to Californians | Systems whose sole purpose is security and integrity; other listed exemptions |
| Utah (ch. 72 / ch. 75) | Persons using generative AI in consumer transactions; persons providing services in *regulated occupations* (licensed by the Department of Commerce) | Safe harbour where the generative AI itself clearly and conspicuously discloses its nature at the outset |
| NYC LL 144 | Employers and employment agencies using an *automated employment decision tool* (AEDT) to substantially assist or replace discretionary decisions for candidates or employees in NYC | Tools that do not substantially assist or replace the decision |
| Illinois P.A. 103-0804 | Employers using AI in recruitment, hiring, promotion, discipline, discharge and other terms of employment (verify) | — |

## Core obligations

### Colorado ADMT Act (C.R.S. 6-1-1701 to 6-1-1709, effective 1 Jan 2027)

| Section | Duty |
|---|---|
| 6-1-1702 Developer documentation | From 1 Jan 2027, give each deployer: intended and known harmful uses; categories of training data (incl. personal data) to the extent known; known limitations and circumstances in which the ADMT should not be used; instructions for use, monitoring and meaningful human review; information the deployer needs for its own disclosures. Notify deployers of material updates within a reasonable time (public release notes plus direct notice suffice). Retain compliance records (version identifiers, changelogs, update notices) for at least 3 years |
| 6-1-1703 Deployer records | Retain records demonstrating compliance for at least 3 years after the consequential decision |
| 6-1-1704 Deployer disclosures | Clear and conspicuous notice before using covered ADMT in a consequential decision (public posting option); post-adverse-outcome disclosure of the ADMT's role (bill summary: within 30 days); AG must adopt rules on content of post-adverse disclosures by 1 Jan 2027; a notice that complies with the federal adverse-action laws specified in 6-1-1704(6) may carry a brief statement that covered ADMT was used |
| 6-1-1705 Consumer rights | On request after an adverse outcome: instructions to obtain and correct factually incorrect or materially inaccurate personal data (specified Colorado Privacy Act exceptions do not limit this correction right) and an opportunity for meaningful human review and reconsideration "to the extent commercially reasonable" |
| 6-1-1707 Liability allocation | Fault allocated between developer and deployer; no joint and several liability; compliance with 6-1-1702 is relevant to developer fault |
| HB 26-1263 Chatbot Safety Act | Operators of conversational AI services must estimate user age, disclose AI nature, protect minors (no engagement rewards, sexual content, or simulated emotional dependence), run suicide/self-harm protocols, file an annual AG report, and not present outputs as licensed professional services; effective 1 Jan 2027 |

The repealed SB 24-205 architecture (reasonable care to avoid algorithmic discrimination, annual impact assessments and within 90 days of substantial modification, AG notice within 90 days of discovering discrimination, exemption for deployers under 50 FTE, ISO/IEC 42001 / NIST AI RMF affirmative defence) never took effect; do not build programmes on it.

### Texas TRAIGA (Bus. & Com. Code ch. 552, effective 1 Jan 2026)

| Section | Duty or prohibition |
|---|---|
| 552.051 | Governmental agencies must disclose AI interaction to consumers before or at the time of interaction; health-care providers must disclose AI use no later than first service (emergencies: as soon as reasonably possible); disclosure must be clear, plain-language, no dark patterns |
| 552.052 | No developing or deploying AI intentionally aimed at inciting self-harm, harm to others, or crime |
| 552.053 / 552.054 | Governmental entities may not use AI for social scoring or for biometric identification from scraped images that infringes rights |
| 552.055 / 552.056 | No AI developed or deployed with the sole intent to infringe constitutional rights, or with intent to unlawfully discriminate against a protected class — disparate impact alone does not prove intent |
| 552.057 | No AI with the sole intent of producing child sexual abuse material or unlawful deepfakes, or child-impersonating sexual chat |
| 552.003 | Preempts local AI ordinances |
| ch. 553 | Regulatory sandbox programme; participation for not more than 36 months |
| § 503.001 amendment | Biometric-identifier law does not reach training or storage of biometrics for AI development unless the system is used to uniquely identify an individual |

### California

| Instrument | Duty |
|---|---|
| CPPA ADMT regs (§§ 7200–7222) | Pre-use notice, opt-out and access rights for ADMT used in significant decisions; existing uses must comply by 1 Jan 2027, new uses on first use |
| CPPA risk assessments (§§ 7150–7157) | Required before selling/sharing PI, processing sensitive PI, using ADMT for a significant decision, automated inference about workers/applicants/students, or profiling in sensitive locations; review at least every 3 years; update within 45 days of a material change; processing already under way must be assessed by 31 Dec 2027; retain for the life of the processing or 5 years, whichever is later; submit the required risk-assessment information to the Agency by 1 Apr 2028 for 2026–2027 assessments, then by 1 Apr annually |
| CPPA cybersecurity audits (§§ 7120–7124) | Businesses deriving 50%+ revenue from selling/sharing PI, or meeting the CCPA revenue threshold and processing PI of 250,000+ consumers/households or sensitive PI of 50,000+ consumers, need an independent annual audit; first report due 1 Apr 2028 (2026 revenue > $100M), 1 Apr 2029 ($50M–$100M) or 1 Apr 2030 (< $50M); executive certification to the Agency by 1 Apr each year |
| SB 53 TFAIA (§ 22757.12–.13) | Large frontier developers publish a *frontier AI framework* covering catastrophic-risk thresholds, mitigations, third-party assessment, cybersecurity of unreleased model weights, incident response and governance; review annually; publish material modifications with justification within 30 days; transmit summaries of internal catastrophic-risk assessments to OES every 3 months. All frontier developers publish a transparency report before or at deployment and report *critical safety incidents* to OES within 15 days of discovery (24 hours to an appropriate authority where there is imminent risk of death or serious injury). Catastrophic risk = more than 50 deaths/serious injuries or more than $1,000,000,000 in property damage from a single incident. Whistleblower protections in Labor Code § 1107 et seq. |
| AB 2013 (Civil Code § 3111) | By 1 Jan 2026 and before each release, post training-data documentation: dataset sources/owners, purpose, number and types of data points, IP status, licensing, personal information, cleaning/processing, collection period, first-use dates, synthetic data |
| Civil Rights Council FEHA regs | Employment regulations addressing automated-decision systems (and proxies) across selection, pre-employment inquiries, criminal-history, medical-inquiry and age provisions of 2 CCR § 11008 et seq.; approved by OAL and filed 27 Jun 2025, effective 1 Oct 2025 |

### Utah, Illinois, New York City

| Instrument | Duty |
|---|---|
| Utah ch. 75 (SB 226, effective 7 May 2025) | Disclose generative-AI use on a clear and unambiguous request; regulated occupations must prominently disclose (verbally at the start of a verbal interaction, in writing before a written one) for *high-risk AI interactions* involving sensitive information such as health, financial or biometric data; safe harbour for systems that self-disclose at the outset. Ch. 72 (SB 149, effective 1 May 2024) created the Office of AI Policy and a regulatory learning laboratory; sunset extended to 1 Jul 2027 |
| Illinois P.A. 103-0804 (HB 3773) | Amends the Illinois Human Rights Act to bar employers from using AI that has a discriminatory effect on protected classes in employment decisions, bars use of zip codes as a proxy, and requires notice to employees of AI use; effective 1 Jan 2026 (verify — official text not retrievable at time of writing) |
| NYC LL 144 (enforced from 5 Jul 2023) | No AEDT use unless an independent auditor completed a **bias audit within one year** of use, computing selection-rate impact ratios by sex, race/ethnicity and intersectional categories (categories under 2% may be excluded with justification); historical data required, test data only if historical data is insufficient; publish a summary of results; give candidates and employees notice at least **10 business days** before use |

## Enforcement and penalties

| Regime | Enforcer and mechanics | Penalties |
|---|---|---|
| Colorado | AG exclusively, via the Colorado Consumer Protection Act (violation = deceptive trade practice, C.R.S. 6-1-105(1)(uuuu)); 60-day cure where the AG deems cure possible — waived for knowing or repeated violations; cure provision repealed 1 Jan 2030; AG SMART Act reporting from Jan 2028; no new private right of action | CCPA civil penalties and injunctive relief (statute does not set AI-specific amounts) |
| Texas | AG exclusively; online complaint portal (due by 1 Sep 2026); civil investigative demands; written notice and 60-day cure with a written cure statement; rebuttable presumption of reasonable care; defences where a third party misused the system or the violation was found through red-teaming/feedback or, if substantially compliant with the NIST AI RMF Generative AI Profile or another recognised framework, an internal review | $10,000–$12,000 per curable violation or breach of a cure statement; $80,000–$200,000 per uncurable violation; $2,000–$40,000 per day continuing; licensing agencies may add sanctions up to $100,000 on AG recommendation |
| California SB 53 | AG civil action only | Large frontier developers: up to $1,000,000 per violation, scaled to severity, for failing to publish/transmit required documents, false statements, unreported incidents, or breaching the developer's own framework |
| California CPPA regs / AB 2013 | CPPA administrative enforcement and AG under the CCPA; AB 2013 via the Civil Code (no dedicated penalty section seen) | CCPA penalty schedule — see [us-state-privacy.md](us-state-privacy.md) |
| Utah | Division of Consumer Protection; administrative fines and court actions; AG for order violations | Up to $2,500 per violation; up to $5,000 per violation of an administrative or court order |
| NYC | DCWP complaint-driven enforcement | Not more than $500 for a first violation (and each additional violation the same day); $500–$1,500 for each subsequent violation |

## Timeline and status

| Date | Event |
|---|---|
| 11 Dec 2021 / 1 Jan 2023 / 5 Jul 2023 | NYC LL 144 enacted / effective / DCWP enforcement begins (DCWP final rule effective 5 Jul 2023) |
| 1 May 2024 | Utah AI Policy Act (SB 149) effective |
| 17 May 2024 | Colorado SB 24-205 signed (original start 1 Feb 2026) |
| 28 Sep 2024 | California AB 2013 signed (Ch. 817) |
| 7 May 2025 | Utah SB 226 effective; AI Policy Act sunset moved to 1 Jul 2027 |
| 1 Jul 2025 | US Senate adopts S.Amdt. 2814 (99–1) striking the state-AI-law moratorium from H.R. 1 |
| 24 Jul / 22 Sep 2025 | CPPA Board adopts ADMT, risk-assessment and cybersecurity-audit regulations / OAL approves; effective 1 Jan 2026 |
| 28 Aug 2025 | Colorado SB 25B-004 signed, delaying SB 24-205 to 30 Jun 2026 |
| 29 Sep 2025 | California SB 53 (TFAIA) signed (Ch. 138); operative 1 Jan 2026 under California's default commencement rule (verify) |
| 1 Oct 2025 | California Civil Rights Council ADS employment regulations effective |
| 11 Dec 2025 | Executive Order 14365 "Ensuring a National Policy Framework for Artificial Intelligence" |
| 1 Jan 2026 | Texas TRAIGA effective; AB 2013 documentation deadline; Illinois P.A. 103-0804 effective (verify) |
| 14 May 2026 | Colorado SB 26-189 signed — repeals and reenacts Part 17 as the ADMT Act |
| 2 Jun 2026 | Executive Order 14409 "Promoting Advanced Artificial Intelligence Innovation and Security" (content not reviewed here) |
| 11 Aug 2026 | Colorado AG files proposed ADMT and Chatbot Safety rules; written comments accepted to 26 Oct 2026, revised draft by 23 Sep 2026 |
| 1 Sep 2026 | Texas AG complaint mechanism due online |
| 1 Jan 2027 | Colorado ADMT Act and Chatbot Safety Act apply; CPPA ADMT compliance deadline; Colorado AG rules due; SB 53 OES annual incident reporting begins |
| 31 Dec 2027 / 1 Apr 2028 | CPPA: legacy risk assessments completed / first risk-assessment submissions and first cybersecurity-audit reports (largest businesses) |
| 1 Jan 2030 | Colorado cure-period provision repealed |

Pending: Connecticut and Maryland have debated comprehensive algorithmic-discrimination bills in 2024–2026 sessions; no enacted comprehensive statute was confirmed in this review (verify). EO 14365 tasked Commerce with identifying "onerous" state laws, the FCC with a possible preemptive disclosure standard, and the FTC with a policy statement; watch for litigation against Colorado and California and for a federal preemption bill.

## Key obligations for security/GRC teams

1. **Inventory AI used in consequential/significant decisions** (hiring, credit, housing, insurance, health, education, government benefits) and classify each system by state footprint and role (developer vs deployer). See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md) and [../../workflows/ai-system-intake.md](../../workflows/ai-system-intake.md).
2. **Build one intake/assessment record per system** that satisfies the CPPA risk assessment (§ 7152), Colorado deployer records (3 years), NYC bias-audit evidence and EU AI Act FRIA where relevant — do not run four parallel assessments. See [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md) and [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).
3. **Demand developer documentation in contracts**: Colorado 6-1-1702 content, model/dataset cards, update notices, AB 2013 training-data summaries, and audit cooperation for NYC bias audits. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
4. **Stand up notice, correction, human-review and opt-out workflows** with clocks: NYC 10 business days pre-use; Colorado post-adverse disclosure and human review; CPPA pre-use notice, opt-out and access.
5. **Adopt a recognised AI risk framework** (NIST AI RMF and its Generative AI Profile, ISO/IEC 42001): Texas makes substantial compliance a defence, and Colorado's AG rulemaking and enforcement discretion will weigh it. See [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).
6. **Wire SB 53 incident clocks into incident response** if you train frontier models: 15 days to OES, 24 hours to authorities for imminent physical danger; protect unreleased model weights as a named control objective. See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
7. **Plan CPPA cybersecurity-audit readiness** now: scope the audit to the 2027 period, appoint an independent auditor, and prepare the executive certification. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
8. **Track legislative and rulemaking change monthly** — Colorado rules, EO 14365 follow-on actions and federal preemption bills can change obligations within a quarter. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md) and [../../workflows/new-regulation-impact-assessment.md](../../workflows/new-regulation-impact-assessment.md).

## Interplay

- **EU AI Act:** Colorado's covered domains and California's significant decisions map closely to Annex III high-risk use cases; EU deployer duties (Art. 26 human oversight, Art. 27 FRIA) and provider documentation largely satisfy the state documentation and human-review duties, but state notice and correction rights are consumer-facing and must be operationalised separately. See [eu-ai-act.md](eu-ai-act.md).
- **State privacy laws:** the CPPA ADMT rules are CCPA regulations — the same business thresholds, consumer-rights machinery and penalty schedule apply; Colorado's correction right leans on the Colorado Privacy Act (C.R.S. 6-1-1306). See [us-state-privacy.md](us-state-privacy.md).
- **Anti-discrimination law:** none of these statutes displaces Title VII, ECOA, FHA, ADA or state civil-rights acts; Illinois and the California FEHA regulations *are* civil-rights law. Texas expressly says disparate impact alone does not prove intent, while NYC's bias audit is entirely disparate-impact based.
- **Sectoral overlays:** Colorado deems insurers under its existing algorithm rule compliant and carves out HIPAA covered entities; Texas defers to insurance and banking regulation; federal adverse-action notices specified in C.R.S. 6-1-1704(6) can carry the Colorado ADMT statement. See [hipaa.md](hipaa.md) and [glba-ftc-safeguards.md](glba-ftc-safeguards.md).
- **Security frameworks:** SB 53 frontier frameworks and CPPA cybersecurity audits are the first US AI-adjacent rules that name cybersecurity controls explicitly; align them with the ISMS ([../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md)) and CSF profiles ([../frameworks/nist-csf-2.md](../frameworks/nist-csf-2.md)).
- **Federal preemption:** EO 14365 cannot itself preempt state law; only litigation outcomes or federal legislation can. Until then, comply with the strictest applicable state rule.

## Primary sources

- Colorado SB 24-205 signed act (legal text): https://leg.colorado.gov/sites/default/files/2024a_205_signed.pdf; bill page: https://leg.colorado.gov/bills/sb24-205
- Colorado SB 25B-004 bill page (delay to 30 Jun 2026): https://leg.colorado.gov/bills/sb25b-004 (signed PDF fetched but image-only)
- Colorado SB 26-189 signed act (legal text): https://leg.colorado.gov/bill_files/116489/download; bill page: https://leg.colorado.gov/bills/sb26-189; HB 26-1263 bill page: https://leg.colorado.gov/bills/HB26-1263
- Colorado AG ADMT and Chatbot Safety rulemaking page and pre-rulemaking considerations (regulator guidance): https://coag.gov/ai/ ; https://coag.gov/app/uploads/2026/06/ADMT-Chatbot-Pre-Rulemaking-Considerations-Document.pdf
- Texas HB 149 enrolled text (legal text): https://capitol.texas.gov/tlodocs/89R/billtext/html/HB00149F.htm
- CPPA regulations page and approved text (regulator page / legal text): https://cppa.ca.gov/regulations/ccpa_updates.html ; https://cppa.ca.gov/regulations/pdf/ccpa_updates_cyber_risk_admt_appr_text.pdf
- California SB 53 chaptered text (legal text): https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53
- California AB 2013 chaptered text (legal text): https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013
- California Civil Rights Council rulemaking actions (regulator page): https://calcivilrights.ca.gov/civilrightscouncil/rulemaking-actions/ (final ADS regulation PDF is image-only; content summarised from the modified text and the council page)
- Utah SB 149 (2024) and SB 226 (2025) enrolled texts (legal text): https://le.utah.gov/~2024/bills/sbillenr/SB0149.pdf ; https://le.utah.gov/~2025/bills/sbillenr/SB0226.pdf
- NYC DCWP AEDT page, final rule and FAQ (regulator guidance): https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page ; https://rules.cityofnewyork.us/wp-content/uploads/2023/04/DCWP-NOA-for-Use-of-Automated-Employment-Decisionmaking-Tools-2.pdf ; https://www.nyc.gov/assets/dca/downloads/pdf/about/DCWP-AEDT-FAQ.pdf ; Local Law 144 legislative record: https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=4344524&GUID=B051915D-A9AC-451E-81F8-6596032FA3F9
- Executive Order 14365 (Federal Register): https://www.federalregister.gov/documents/2025/12/16/2025-23092/ensuring-a-national-policy-framework-for-artificial-intelligence
- US Senate roll-call votes, 119th Congress 1st session (vote 363 on S.Amdt. 2814): https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_1.xml
- Illinois P.A. 103-0804 (HB 3773): https://www.ilga.gov/legislation/publicacts/fulltext.asp?Name=103-0804 — **could not be fetched**; Illinois details above are unverified

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
