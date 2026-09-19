# South Korea Personal Information Protection Act (PIPA) and information security law

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Personal Information Protection Act (PIPA), Act No. 10465 of 29 March 2011; consolidated English text as amended by Act No. 19234 (14 March 2023) and Act No. 20897 (1 April 2025). Enforcement Decree: Presidential Decree No. 23169, consolidated through Decree No. 35343 (25 February 2025). A further amending act (reported as Act No. 21445, promulgated 10 March 2026) applies from 11 September 2026 — details in Timeline |
| Regulator | Personal Information Protection Commission (PIPC) — independent central authority since the 2020 consolidation. Korea Internet and Security Agency (KISA) is the designated "specialized institution" for breach reports (Decree Art. 40(3)). Financial Services Commission (FSC) supervises the Credit Information Act and Electronic Financial Transactions Act; Ministry of Science and ICT (MSIT) administers the Network Act |
| Who is covered | Every "personal information controller" — public institutions, companies, organisations and individuals operating personal information files (Art. 2). Outsourcees are bound mutatis mutandis (Art. 26(8)). No establishment test: foreign controllers processing Koreans' data are in scope, and those above thresholds must appoint a domestic agent (Art. 31-2) |
| Structure | Single omnibus statute (Arts. 1–76 plus many inserted "-n" articles): principles and PIPC; lawful processing; safe management; data-subject rights; dispute mediation and class actions; enforcement; criminal penalties and administrative fines. The 2023 amendment deleted the separate chapter for online service providers, unifying online and offline rules |
| Breach clock | Notify data subjects within 72 hours of becoming aware (Decree Art. 39(1)); report to PIPC/KISA within 72 hours where ≥1,000 data subjects, sensitive or unique-identifier data, or illegal external access are involved (Decree Art. 40(1)) |
| Penalties | Penalty surcharge up to 3% of total sales, calculated net of sales unrelated to the violation (Art. 64-2(1)–(2)); administrative fines up to KRW 50 million (Art. 75); criminal penalties up to 10 years / KRW 100 million (Art. 70); civil damages up to five times actual loss (Art. 39(3)); a 10%-of-total-revenue tier applies from 11 September 2026 (see Enforcement) |
| Certifiable? | Yes — ISMS-P (Personal Information & Information Security Management System) under Art. 32-2, three-year validity, annual follow-up audit; voluntary today, mandatory for designated controllers from 1 July 2027 (reported) |
| EU adequacy | Commission Implementing Decision (EU) 2022/254 of 17 December 2021; first review concluded 23 July 2026 (COM(2026) 384) with adequacy maintained |
| Neighbouring regimes | Network Act (ISMS certification, CISO, 24-hour cyber-incident reporting to MSIT/KISA); Credit Information Use and Protection Act (FSC, personal credit information); Electronic Financial Transactions Act (FSC, e-finance security and CISO) |

## What it is

PIPA is Korea's general data protection statute, enacted in 2011 to replace a sector-by-sector patchwork. Two structural reforms define the current regime. The 2020 "Data 3 Laws" amendment (Act No. 16930, 4 February 2020) moved the online-service-provider privacy rules from the Network Act into PIPA, made the PIPC the sole competent authority, and introduced pseudonymized information (Arts. 28-2 to 28-5). The 2023 amendment (Act No. 19234, in force 15 September 2023) then removed the remaining online/offline distinction, rebuilt the cross-border transfer regime (Arts. 28-8 to 28-11), rewrote breach notification (Art. 34), created rights against automated decisions (Art. 37-2, in force 15 March 2024) and data portability (Art. 35-2), and replaced the old "related sales" fine base with a surcharge of up to 3% of total sales (Art. 64-2).

The statute is only the top layer. Operational specifics — the 72-hour clocks, CPO qualification thresholds, safety-measure content, domestic-agent thresholds, portability commencement — sit in the Enforcement Decree and in PIPC notifications, and those are what change most often. The PIPA sits alongside three sectoral security laws that a Korean-facing security programme will meet in practice: the Network Act (Act on Promotion of Information and Communications Network Utilization and Information Protection), the Credit Information Use and Protection Act, and the Electronic Financial Transactions Act (EFTA). PIPA governs processing "except as otherwise provided in other statutes" (Art. 6(1)), so those sectoral rules displace it where they speak.

## Who it covers / Scope

| Test | Rule |
|---|---|
| Material scope | "Personal information" = information on a living individual that identifies them directly or when easily combined with other information; pseudonymized information is personal information; fully anonymized information is outside the Act (Art. 58-2) |
| Personal scope | Any personal information controller, public or private, of any size; micro-enterprises are exempt only from the duty to designate a CPO (Art. 31(1) proviso; Decree Art. 32(1)), in which case the owner or representative is the CPO by law (Art. 31(2)) |
| Processors ("outsourcees") | Entrustment must be in a written document stating purpose limits and safeguards; the entruster must disclose, train and supervise; re-entrustment needs the entruster's consent; the outsourcee is deemed the controller's employee for damages and is directly bound by the listed articles (Art. 26) |
| Extraterritorial reach | No territorial limiter in the Act. A controller with no address or place of business in Korea must designate a written domestic agent for complaints, breach notification/reporting and PIPC document requests where previous-year total sales are ≥ KRW 1 trillion, ≥1 million domestic data subjects are held on average over the preceding three months, or the PIPC so resolves (Art. 31-2; Decree Art. 32-3). From the 2025 amendment, a Korean subsidiary or controlled affiliate must be chosen as the agent where one exists (Art. 31-2(2)) |
| Partial exemptions | Art. 58 excludes Arts. 15–57 for listed categories (e.g., statistical processing by public institutions) while keeping the Art. 3 principles, Art. 4 rights and Art. 58(4) minimum duties |
| Financial sector | Personal credit information is governed by the Credit Information Act, supervised by the FSC; the EU adequacy decision expressly excludes FSC-supervised credit-information processing from its coverage (Decision 2022/254 Art. 1(2)(c)) |

## Core obligations

### Lawful processing and special categories

| Article | Requirement |
|---|---|
| Art. 15 | Seven grounds for collection and use: consent; statute; public-institution duties; contract performance at the data subject's request; imminent danger to life/body/property; manifestly superior legitimate interest; urgent public safety/health. Consent notices must state purpose, items, retention period and the right to refuse (Art. 15(2)); compatible further use is allowed subject to safeguards such as encryption (Art. 15(3)) |
| Arts. 17–19 | Provision to third parties on similar grounds; restrictions on repurposing (Art. 18) and on recipients' use (Art. 19) |
| Art. 22-2 | Children under 14: legal-representative consent, verification of that consent, and plain-language notices |
| Art. 23 | Sensitive information (ideology, belief, union/party membership, political opinion, health, sex life and Decree categories) only with separate consent or statutory basis; mandatory Art. 29 safeguards |
| Arts. 24, 24-2 | Unique identifiers (resident registration numbers etc.) only with separate consent or statute, with encryption mandated (Art. 24(3)); RRN processing needs a specific statutory basis; PIPC inspects encryption compliance at larger controllers (Art. 24(4)) |
| Arts. 28-2 to 28-5 | Pseudonymized information may be processed without consent for statistics, scientific research and public-interest archiving; combination across controllers only through designated expert agencies; re-identification prohibited |
| Art. 28-8 | Cross-border transfer (provision, entrusted processing or storage abroad) only with separate consent; a statute or treaty; contract-necessity entrustment/storage disclosed in the privacy policy or notified; recipient certification recognised by the PIPC (e.g., ISMS-P-based) plus safeguards; or PIPC recognition that the destination country's regime is substantially equivalent. Contract terms contrary to the Act are void; the PIPC may order transfers suspended (Art. 28-9) |

### Safe management and governance

| Article | Requirement |
|---|---|
| Art. 29; Decree Art. 30 | Technical, managerial and physical safeguards: internal management plan; access-authority standards and authentication; intrusion detection/blocking and — for controllers with ≥1 million average daily users — internet blocking for handler terminals; one-way password hashing, encryption of RRNs and other notified data at rest and in transit; access-log retention and tamper protection; anti-malware; physical controls. Detailed standards are set by PIPC notification (Decree Art. 30(3)) |
| Art. 30 | Privacy policy: content and disclosure; the PIPC evaluates policies and may recommend improvements (Art. 30-2) |
| Art. 31; Decree Art. 32 | Chief Privacy Officer (CPO) with statutory duties (protection plan, regular surveys, complaints, internal controls, training, file management) and inspection powers; controllers must guarantee independence — access to information, regular reporting to the representative or board, adequate resources (Decree Art. 32(6)). Since 15 March 2024, controllers with annual sales ≥ KRW 150 billion that process sensitive/unique-identifier data of ≥50,000 or any personal information of ≥1 million data subjects, large universities, tertiary hospitals and public-system operators must appoint a CPO meeting Decree Appendix 1 qualification requirements (experience criteria — verify current appendix) |
| Art. 32-2; Decree Art. 34-2 | ISMS-P certification: PIPC certifies compliance of the management system, rights guarantees and safety measures; valid 3 years; follow-up management at least annually; revocable. Unified with the Network Act ISMS on 7 November 2018; criteria per the PIPC page: 16 management-system + 64 protection-measure + 22 personal-data-lifecycle items (law-firm sources cite 101 with 21 lifecycle items — verify current notice); certification bodies KISA and the Financial Security Institute |
| Art. 33 | Privacy impact assessment mandatory for public institutions operating files above Decree thresholds, via PIPC-designated assessment institutions; private controllers "shall proactively endeavour" to conduct PIAs (Art. 33(11)) |
| Art. 34-2 | Exposed personal information (unique identifiers, account and card data) must be kept off public networks and erased or blocked at PIPC/KISA request |

### Breach notification and reporting (Art. 34; Decree Arts. 39–40)

| Duty | Trigger | Deadline | Content / notes |
|---|---|---|---|
| Notify data subjects | Awareness of loss, theft or divulgence | Within 72 hours; may follow "without delay" after urgent containment or force majeure; partial notice first if facts unconfirmed (Decree Art. 39(2)); website posting for ≥30 days where contacts unknown (Decree Art. 39(3)) | Items divulged; when and how; mitigation steps for data subjects; controller countermeasures and remedies; help desk (Art. 34(1)) |
| Report to PIPC or KISA | ≥1,000 data subjects; any sensitive or unique-identifier data; or illegal external access to processing systems/handler equipment | Within 72 hours (Decree Art. 40(1)); staged reporting permitted (Art. 40(2)) | Same content as the notice; report may be omitted where the leak path is confirmed and data recovered/deleted so that risk is substantially reduced |
| Sanction for failure | — | — | Administrative fine up to KRW 30 million for failing to notify or report (Art. 75(2)17–18); the SK Telecom decision paired a KRW 9.6 million fine with the KRW 134.8 billion surcharge |

From 11 September 2026 the notification duty reportedly extends to forgery, alteration and damage and triggers on a reasonable possibility of a breach rather than confirmed divulgence (law-firm summaries of the 2026 amendment — verify against the promulgated text). Track the clock in the [incident notification log](../../templates/incident-regulatory-notification-log.md) and the [breach-notification crosswalk](../crosswalks/breach-notification-timelines.md).

### Data-subject rights

| Article | Right |
|---|---|
| Arts. 35–37 | Access, correction/erasure, suspension of processing |
| Art. 35-2 | Portability: request transmission to self or to designated recipients, limited to consent- or contract-based data processed by computer; scope and commencement set by Decree, with sector-by-sector technical rollout still expanding in 2026 |
| Art. 37-2 | Automated decisions (including AI systems) with significant effect: right to object and to demand explanation; controller must not apply the decision or must re-process with human involvement unless a compelling reason exists; criteria and procedures must be disclosed. In force 15 March 2024 |
| Arts. 39, 39-2, 51 | Reversed burden of proof on fault; punitive damages up to 5x actual loss for intentional or negligent breaches; statutory damages up to KRW 3 million without proof of loss; injunctive class actions by qualified consumer groups after failed collective mediation |

## Enforcement and penalties

| Instrument | Ceiling / basis | Notes |
|---|---|---|
| Penalty surcharge (Art. 64-2) | Up to 3% of total sales, calculated on gross sales net of sales unrelated to the violation; up to KRW 2 billion where no sales or sales cannot be calculated | Grounds include unlawful collection/provision, children's data, sensitive/unique identifiers, failure to supervise outsourcees, re-identification, unlawful cross-border transfer, and any loss/theft/divulgence/forgery/alteration/damage unless all Art. 29 safeguards were in place |
| 10% tier (from 11 September 2026) | Up to 10% of total revenue | Reported conditions: intentional or grossly negligent repeat violation within three years; intentional or grossly negligent conduct affecting ≥10 million data subjects; breach after non-compliance with a PIPC corrective order. Reductions available for documented privacy investment except for intent/gross negligence (new Art. 64-2(6), per law-firm summaries — verify) |
| Administrative fines (Art. 75) | KRW 50m / 30m / 20m / 10m tiers | Breach notice/report failures and automated-decision failures sit in the KRW 30m tier; missing privacy policy or CPO in the KRW 10m tier |
| Criminal (Arts. 70–73) | Up to 10 years or KRW 100m (Art. 70, e.g., fraudulent acquisition and onward provision for profit); up to 5 years or KRW 50m (Art. 71, e.g., provision without consent) | Corporate joint liability (Art. 74); confiscation (Art. 74-2) |
| Corrective powers | Corrective orders (Art. 64), publication of results (Art. 66), suspension of cross-border transfers (Art. 28-9), preliminary fact-finding inspections (Art. 63-2) | The PIPC publishes its decisions and names sanctioned entities |

Benchmark decisions (amounts as reported in Korean press and PIPC releases):

| Date | Entity | Sanction | Findings |
|---|---|---|---|
| 28 Aug 2025 | SK Telecom | KRW 134.8 billion surcharge + KRW 9.6 million fine; corrective orders | HSS breach exposing 25 data categories of 23.2 million subscribers; flat network with internal management servers reachable from the internet; 26.1 million SIM authentication keys stored in plaintext; ignored IDS logs and a 2016 patch; CPO remit confined to IT services. Largest PIPA penalty at the time (industry had expected mid-KRW 300 billion under the 3% cap); revocation suit filed in the Seoul Administrative Court, January 2026 |
| 10 Jun 2026 | Coupang (and subsidiary CFS) | KRW 624.681 billion surcharge + KRW 16.8 million fine; CFS KRW 248 million | 33.22 million members and 4.34 million non-members exposed via an ex-employee's alternative authentication path; unrevoked signing keys, weak access control, missed anomalous logins, late notification, CPO excluded from the investigation, five months of web logs deleted despite a preservation order; separate KRW 201.1 billion component for non-consensual tracking of 11.17 million users |
| 29 Jul 2026 | KT | KRW 53.979 billion surcharge + KRW 7.2 million fine; criminal referral for obstruction | Rogue femtocells built from certificates extracted from lost devices; 16,647 subscribers' data and KRW 240 million in fraudulent micropayments; separate undisclosed 2024 malware infection of 38 servers |
| Earlier | Google KRW 69.2bn and Meta KRW 30.8bn (2022, behavioural advertising without consent); Kakao KRW 15.1bn (2024, open-chat leak) | | Pre-3%-cap era; shows the trajectory that the 2026 10% tier extends |

The PIPC also sanctioned GS Retail and three other businesses over data breaches on 3 September 2026, so enforcement cadence is monthly, not annual.

## Timeline and status

| Date | Event |
|---|---|
| 29 Mar 2011 | PIPA enacted (Act No. 10465); in force six months later |
| 4 Feb 2020 | "Data 3 Laws" amendment (Act No. 16930): online-provider rules folded into PIPA; PIPC becomes sole regulator; pseudonymization introduced; in force six months after promulgation |
| 17 Dec 2021 | EU adequacy decision (EU) 2022/254 adopted; Supplementary Rules (PIPC Notification 2021-5) in Annex I, government assurances in Annex II |
| 14 Mar 2023 | Act No. 19234 promulgated; general provisions in force 15 Sep 2023; Arts. 11-2, 31 (CPO), 35-3, 37-2 (automated decisions), 39-7 in force 15 Mar 2024; Art. 35-2 (portability) commenced by Decree within two years thereafter |
| 12 Sep 2023 | Enforcement Decree wholly rewrites breach notification (Arts. 39–40, 72-hour clocks) and adds cross-border certification/recognition procedures (Arts. 29-8 to 29-10) |
| 12 Mar 2024 | Decree No. 34309: CPO qualification thresholds and independence guarantees (Art. 32), in force 15 Mar 2024; public-system operator rules from 15 Sep 2024 |
| 1 Apr 2025 | Act No. 20897: domestic agent must be an in-country subsidiary/affiliate where one exists; controller must train and inspect the agent; in force six months after promulgation |
| 16 Sep 2025 | Korea's reciprocal adequacy recognition of the EU under Art. 28-8(1)5 enters into force (joint Commission–PIPC statement of that date, cited in the Commission's 2026 review report; PIPC release of 24 July 2026) |
| 10 Mar 2026 | Amending act (reported as Act No. 21445) promulgated: 10%-of-total-revenue surcharge tier; CEO/representative designated ultimate responsible person; board approval and PIPC reporting of CPO appointments for designated controllers; wider breach-notification trigger; investment-based fine reductions. In force 11 Sep 2026; mandatory ISMS-P provisions from 1 Jul 2027. Draft Decree on revenue calculation and reductions published 16 Mar 2026 |
| 31 Mar 2026 | Network Act amendment promulgated (passed 12 Mar 2026), in force 1 Oct 2026: statutory 24-hour incident reporting, director-level CISO reporting to the board, administrative fines up to 3% of revenue for repeated incidents, information-security level assessment from 1 Apr 2027 (law-firm summaries — verify against text) |
| 10 Apr 2026 | MSIT and PIPC announce ISMS/ISMS-P overhaul: three tiers (enhanced/standard/simplified), on-site technical audits including penetration testing, preliminary audit gate on CISO/CPO authority, asset identification, encryption and patching, post-certification monitoring and revocation; rollout expected from 2027 via Decree and notices |
| 23 Jul 2026 | Commission report COM(2026) 384 concludes first adequacy review: Korea remains adequate; Supplementary Rules 2, 4 and part of 5 to be revoked as now embedded in PIPA; review cycle to move from three to four years; PIPC encouraged to run random compliance checks |
| 27 Aug 2026 | National Assembly passes a further PIPA amendment bill on personal data use for AI development (PIPC release); promulgation and commencement to be confirmed (verify) |

Status as of September 2026: the 2023 regime is fully in force; the 2026 amendment has just commenced (11 September 2026) with implementing Decree provisions still being finalised; ISMS-P mandate and the Network Act security-level assessment are pending 2027 milestones.

## Key obligations for security/GRC teams

1. **Confirm applicability and the domestic-agent trigger** (KRW 1 trillion sales or 1 million Korean data subjects) and whether Network Act, Credit Information Act or EFTA layers also apply. See [regulatory-applicability](../../skills/regulatory-applicability/SKILL.md).
2. **Build the 72-hour dual clock into incident response**: subject notice and PIPC/KISA report in parallel, staged reporting when facts are incomplete, and — for Network Act providers — the separate 24-hour cyber-incident report to MSIT/KISA. See [incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md) and the [incident response workflow](../../workflows/incident-regulatory-response.md).
3. **Appoint a qualified, independent CPO** with board reporting lines; from September 2026 expect board approval and PIPC registration for designated controllers, and executive-level accountability. Evidence the reporting cadence in [board reporting](../../skills/grc-metrics-reporting/SKILL.md).
4. **Map Decree Art. 30 safeguards to the control set** — access authority, intrusion detection, encryption of authentication data and identifiers, tamper-proof access logs, anti-malware, network separation for large controllers. The SK Telecom, Coupang and KT decisions turned on exactly these controls. See [framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md) and [ISO 27001](../frameworks/iso-27001-2022.md).
5. **Govern outsourcing under Art. 26**: written entrustment terms, public disclosure of outsourcees, consent for sub-entrustment, documented training and inspection; PIPA treats supervisory neglect as a surcharge ground. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md).
6. **Document a cross-border transfer basis per flow** (consent, contract-necessity disclosure, recognised certification, or PIPC country recognition) and keep Art. 28-8(2) notices current; note the EU is recognised, but most other destinations still rely on consent or contract-necessity. See [dpia-privacy-assessment](../../skills/dpia-privacy-assessment/SKILL.md).
7. **Inventory automated decision-making** and publish criteria and procedures; wire objection and explanation handling into the rights process. See [ai-governance](../../skills/ai-governance/SKILL.md).
8. **Plan for ISMS-P** if you are a telecom carrier, identity-verification provider, public-system operator or large controller — the 2027 mandate and the new technical audit model make paper compliance untenable. See [iso27001-readiness](../../skills/iso27001-readiness/SKILL.md) for reuse of an existing ISMS.
9. **Track the 2026 Decree and notice changes** (surcharge calculation, reductions, CPO reporting, ISMS-P tiers). See [regulatory-horizon-scanning](../../skills/regulatory-horizon-scanning/SKILL.md).

## Interplay

- **Network Act** (Act No. 21066 consolidated text): mandatory ISMS certification for telecom operators, major online service providers, data-centre operators and any provider with previous-year sales/tax revenue ≥ KRW 150 billion, ICT-service sales ≥ KRW 10 billion or ≥1 million average daily users (Art. 47(2)); three-year validity with annual follow-up (Art. 47(5), (8)); CISO designation reported to MSIT, no concurrent roles at large providers (Art. 45-3); "immediate" cyber-incident reporting to MSIT/KISA with Decree-set timing (Art. 48-3) — reported as 24 hours from awareness under the Decree change effective 14 August 2024 (law-firm summary; verify Decree Art. 58-2), with fines up to KRW 30 million for non-reporting (Art. 76(1)6-6). A report already made under another statute (e.g., PIPA Art. 34) is deemed to satisfy Art. 48-3(1), but PIPA contains no reciprocal deeming rule, so the PIPC/KISA 72-hour report must still be filed.
- **Credit Information Act** (Act No. 21646 consolidated text): FSC-supervised security measures for credit information systems (Art. 19); leak notice to credit data subjects "without delay" and report to the FSC above Decree thresholds (Art. 39-4); penalty surcharge up to 3% of total sales, capped at KRW 5 billion for Art. 19(1) security failures (Art. 42-2); the PIPC exercises those powers over commercial (non-financial) enterprises (Art. 45-3). Three-year record-keeping of collection/use events (Art. 20(2)).
- **Electronic Financial Transactions Act** (Act No. 21205 consolidated text): duty of safety under FSC standards (Art. 21), annual IT-sector plan signed by the representative (Art. 21(4)), executive-level CISO without concurrent IT duties at larger firms (Art. 21-2), vulnerability analysis (Art. 21-3), notification of infringement incidents to the FSC without delay (Art. 21-5), penalty surcharge up to KRW 5 billion for misuse of transaction information (Art. 46). A financial-sector incident can therefore trigger PIPA, Credit Information Act and EFTA reports to two regulators.
- **GDPR**: adequacy makes EU-to-Korea transfers lawful without SCCs for PIPA-covered recipients, subject to the Supplementary Rules (purpose of transfer = purpose of collection; one-month transparency notice to EU data subjects; onward-transfer limits) and excluding FSC-supervised credit-information processing. Korea-to-EU transfers rely on PIPC recognition of the EU since September 2025. PIPA's 72-hour subject notice is stricter than GDPR Art. 34's "without undue delay"; its punitive damages and class actions have no GDPR analogue. See [gdpr.md](gdpr.md).
- **EU AI Act**: Art. 37-2 is a rights-based control on automated decisions, not a product-safety regime; organisations deploying high-risk AI in both markets need both. See [eu-ai-act.md](eu-ai-act.md).
- **NIS2/DORA**: Korean telecom and financial security duties (Network Act, EFTA) parallel NIS2 and DORA in structure — CISO, testing, incident clocks — but differ on hours and recipients; see [nis2.md](nis2.md), [dora.md](dora.md) and the [breach-notification crosswalk](../crosswalks/breach-notification-timelines.md). Other APAC regimes are summarised in [other-jurisdictions.md](other-jurisdictions.md).

## Primary sources

- Personal Information Protection Act, English translation (Korea Legislation Research Institute), text as amended by Act No. 20897: https://elaw.klri.re.kr/eng_service/lawViewContent.do?hseq=71740&lang=ENG — legal text
- Enforcement Decree of the PIPA, English translation, Decree No. 35343: https://elaw.klri.re.kr/eng_service/lawViewContent.do?hseq=69668&lang=ENG — legal text
- Act on Promotion of Information and Communications Network Utilization and Information Protection, English translation, Act No. 21066: https://elaw.klri.re.kr/eng_service/lawViewContent.do?hseq=71563&lang=ENG — legal text
- Credit Information Use and Protection Act, English translation, Act No. 21646: https://elaw.klri.re.kr/eng_service/lawViewContent.do?hseq=75061&lang=ENG — legal text
- Electronic Financial Transactions Act, English translation, Act No. 21205: https://elaw.klri.re.kr/eng_service/lawViewContent.do?hseq=72502&lang=ENG — legal text
- Commission Implementing Decision (EU) 2022/254 (Korea adequacy), CELEX 32022D0254 — legal text
- Commission report COM(2026) 384 final, first review of the Korea adequacy decision, 23 July 2026: https://ec.europa.eu/transparency/documents-register/api/files/COM(2026)384_0/090166e530f429d9 — regulator report
- PIPC English site, press-release list and "EU's Adequacy Decision on the Republic of Korea Renewed" (24 July 2026): https://www.pipc.go.kr/eng/ — regulator page (press-release detail pages partly inaccessible to scripted retrieval)
- PIPC ISMS-P overview: https://www.pipc.go.kr/eng/user/lgp/bnp/certification.do — regulator guidance (criteria count and certification bodies)
- Yulchon, "Amendments to the PIPA, its Enforcement Decree and the Network Act" (10 April 2026) and "ISMS/ISMS-P Reform in Korea" (April 2026); Shin & Kim, "South Korea to Overhaul ISMS/ISMS-P" (29 April 2026); Kim & Chang notes on Network Act incident-reporting (2024) and 2026 amendments; DLA Piper Data Protection Laws of the World – Korea (updated 20 March 2026); Hunton and IAPP alerts on the 2026 amendment — secondary sources used for the 2026 amendment specifics (promulgated text not yet available in English)
- Korea Herald (28 Aug 2025, SK Telecom), Korea Times (19 Jan 2026, SK Telecom suit), Seoul Economic Daily (11 Jun 2026, Coupang; 30 Jul 2026, KT) — secondary sources for enforcement figures
- Not fetchable: KISA ISMS-P portal (isms.kisa.or.kr) and Korean-language PIPC press releases

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
