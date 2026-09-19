# UK Product Security and Telecommunications Infrastructure Act 2022, Part 1 (PSTI product security regime)

## At a glance

| Attribute | Detail |
|---|---|
| Instruments | **Part 1 of the Product Security and Telecommunications Infrastructure Act 2022 (c. 46)** (ss. 1–56) plus the **PSTI (Security Requirements for Relevant Connectable Products) Regulations 2023 (SI 2023/1007)**, as amended by SI 2025/211 (in force 25 February 2025) and SI 2025/1267 (in force 4 December 2025). Part 2 of the Act (Electronic Communications Code) is unrelated telecoms law |
| Publisher / regulator | Department for Science, Innovation and Technology (DSIT) owns policy and makes the regulations; the **Office for Product Safety and Standards (OPSS)**, part of the Department for Business and Trade, enforces on behalf of the Secretary of State under an MoU with DSIT |
| Status and key dates | Act: Royal Assent December 2022. Regime live **29 April 2024** (Part 1 fully commenced by SI 2023/469 reg. 3; 2023 Regulations in force the same day). Extends to England and Wales, Scotland and Northern Ireland (vehicle exceptions are Great Britain only) |
| Who is covered | **Manufacturers, importers and distributors** ("relevant persons", s. 7) of **relevant connectable products** (s. 4) that are, or will be, **UK consumer connectable products** (s. 54); UK authorised representatives of non-UK manufacturers (s. 51) |
| Structure | Act Ch. 1 definitions and powers; Ch. 2 duties (manufacturers ss. 8–12, authorised representatives s. 13, importers ss. 14–20, distributors ss. 21–25); Ch. 3 enforcement (ss. 26–52); Ch. 4 guidance and interpretation. Regulations: Sch. 1 three security requirements; Sch. 2 deemed compliance; Sch. 2A deemed compliance for the statement of compliance; Sch. 3 excepted products; Sch. 4 statement of compliance content |
| Security requirements | (1) no universal default or easily guessable passwords; (2) published information on how to report security issues and when reporters get acknowledgement and status updates; (3) published minimum security update period ("defined support period") with an end date (Regs Sch. 1) |
| Conformity model | Manufacturer self-declaration: a **statement of compliance** must accompany every product (s. 9); no CE/UKCA-style marking, no notified body. Deemed compliance via ETSI EN 303 645 provisions, ISO/IEC 29147:2018, or (from 4 December 2025) a valid Japan JC-STAR STAR-1 or Singapore Cybersecurity Labelling Scheme label |
| Penalties | Monetary penalty up to the greater of **GBP 10 million or 4 % of qualifying worldwide revenue** per breach (s. 38), plus a daily penalty of up to **GBP 20,000** for continuing breaches (s. 36(5)); compliance, stop and recall notices; forfeiture; public naming; failure to comply with an enforcement notice is a criminal offence (s. 32) |
| Relationship to neighbours | UK counterpart to the EU Cyber Resilience Act (Regulation (EU) 2024/2847) and the RED cybersecurity delegated act (Delegated Regulation (EU) 2022/30); built on the UK Code of Practice for Consumer IoT Security (October 2018) and ETSI EN 303 645 |

## What it is

Part 1 of the PSTI Act is the UK's first statutory product-cybersecurity regime. It converts the top three principles of the 2018 Code of Practice for Consumer IoT Security into legal duties on the whole supply chain for consumer "smart" products: no default passwords, a working route for reporting vulnerabilities, and transparency about how long a product will receive security updates. The Act is a framework: it defines the products and persons in scope, the duty structure and the enforcement toolkit, and leaves the substantive security requirements to regulations (s. 1). The 2023 Regulations supply those requirements and lift them almost verbatim from ETSI EN 303 645 provisions 5.1-1, 5.1-2, 5.2-1 and 5.3-13.

The regime deliberately stops short of the EU CRA's full lifecycle model. There is no minimum support period, no vulnerability-handling or secure-development requirement beyond publishing a disclosure route, no obligation to report exploited vulnerabilities or incidents to the regulator, and no third-party conformity assessment. What it does have is a hard, well-resourced enforcement regime modelled on UK product-safety law: OPSS can serve notices, fine, recall, seize and name-and-shame, and directors can be personally liable for offences (s. 52).

Government has signalled that the regime is a baseline that will grow. The Regulations require a statutory review within five years of 29 April 2024 (reg. 10), the exceptions list has already been extended once (vehicles, 2025), and mutual-recognition routes with Japan and Singapore were added in December 2025.

## Who it covers / Scope

**Product test (ss. 4–5).** A *relevant connectable product* is either an **internet-connectable product** (capable of connecting to the internet using an Internet Protocol suite protocol, s. 5(1)–(2)) or a **network-connectable product** (sends and receives data by electrical or electromagnetic transmission, is not internet-connectable, and either connects directly to an internet-connectable product over IP, or connects directly to two or more products at once over a non-IP protocol and can connect to an internet-connectable product over such a protocol, s. 5(3)–(5)). Wireless input peripherals of a computer are pulled in by s. 5(7). The product must not be an *excepted product* (s. 6, Regs Sch. 3).

**Market test (s. 54).** Duties bite when the product is a *UK consumer connectable product*: made available to consumers in the UK (or to non-consumer customers where identical products are made available to consumers) and not previously supplied to any customer. "Consumer" means an individual acting wholly or mainly outside their business (s. 56). Returned, recalled or manufacturer-reconditioned units are treated as not previously supplied (s. 54(5)–(7)), so refurbished-as-new stock is in scope; ordinary second-hand resale is not. "Supply" is supply in the course of business, including gifts, prizes, hire-purchase and installation into a building (s. 55).

**Persons (s. 7).** *Manufacturer* = anyone who makes, or has made, a product and markets it under their own name or trade mark, **including own-brand labellers**. *Importer* = anyone who imports into the UK and is not a manufacturer. *Distributor* = anyone else who makes the product available in the UK (retailers, resellers). Installers acting under a works contract are not distributors if identical products are also sold to consumers by other means (s. 7(6)). Non-UK manufacturers may appoint a UK **authorised representative** who takes on the statement-of-compliance, compliance-failure and record-keeping duties without relieving the manufacturer of liability (s. 51).

**Excepted products (Regs Sch. 3, as amended by SI 2025/211):**

| Exception | Condition |
|---|---|
| Northern Ireland supply | Products covered by Windsor Framework Annex 2 legislation containing a free-movement article (EU product law applies instead) |
| EV charge points | Charge points within the Electric Vehicles (Smart Charge Points) Regulations 2021 |
| Medical devices | Products within the Medical Devices Regulations 2002, **except** a connectable product on which regulated medical software is merely installed or operable |
| Smart meters | Supplied or installed by gas/electricity licence holders and assured under the NCSC Commercial Product Assurance scheme (or successor) |
| Computers | Desktops, laptops and tablets **without** cellular connectivity, unless designed exclusively for children under 14. Smartphones and cellular tablets are in scope |
| Vehicles (GB only, from 25 February 2025) | Products within Regulation (EU) 2018/858 (motor vehicles and trailers, including systems, components and separate technical units), (EU) 168/2013 (two/three-wheelers and quadricycles) or (EU) 167/2013 (agricultural and forestry vehicles) |

**Extraterritorial reach.** Location of the manufacturer is irrelevant: the trigger is intending, or being aware or "ought to be aware", that the product will be a UK consumer connectable product (ss. 8, 14, 21). Overseas manufacturers selling into the UK are directly bound; their UK importers and distributors carry parallel duties and cannot lawfully supply a non-compliant product.

## Core obligations

### The three security requirements (Regs Sch. 1)

| # | Requirement | What it requires | Notes / edge cases |
|---|---|---|---|
| 1 | Passwords (para. 1) | Passwords in any state other than factory default must be **unique per product** or **user-defined**. Unique passwords must not be based on incremental counters, publicly available information, or product identifiers such as serial numbers (unless via an encryption or keyed-hash method accepted as good industry practice), nor otherwise guessable | Applies to hardware, pre-installed software and software that must be installed for the intended purpose. Excludes cryptographic keys, non-IP pairing PINs and API keys. "Good industry practice" is judged against a skilled and experienced cryptographer |
| 2 | Security-issue reporting (para. 2) | Publish **at least one point of contact** for reporting security issues, and state **when the reporter will receive an acknowledgement and status updates** until resolution | Information must be accessible, clear, transparent, available without prior request, in English, free, and without demanding the reporter's personal data. Covers associated software too, except for smartphones and cellular tablets |
| 3 | Minimum security update period (para. 3) | Publish the **defined support period** (a minimum period expressed with an **end date**). If extended, publish the new period as soon as practicable. The requirement is **not met if the period is later shortened** | Must be understandable without technical knowledge and, where the manufacturer's own website carries an invitation to purchase, given equal prominence to the price and product information required by the Consumer Protection from Unfair Trading Regulations 2008. Applies only to components capable of receiving security updates; no minimum length is prescribed |

### Deemed compliance (Regs Sch. 2 and 2A)

| Requirement | Route A (standards) | Routes B and C (labels, since 4 December 2025) |
|---|---|---|
| Passwords | ETSI EN 303 645 provisions 5.1-1 and, where relevant, 5.1-2 | Valid, unexpired Japan JC-STAR STAR-1 conformance label (IPA, JST-CR-01-01-2024R1, December 2024) **or** a valid label at any level of the Singapore Cybersecurity Labelling Scheme (CSA, CCC SP-151-2 v1.4, April 2025) |
| Security-issue reporting | ETSI EN 303 645 provision 5.2-1, **or** ISO/IEC 29147:2018 paras 6.2.2, 6.2.5 and 6.5 plus publication of the reporting mechanism and acknowledgement/update timelines | Same labels |
| Update period | ETSI EN 303 645 provision 5.3-13, read with the Regulations' definition of defined support period and publication conditions | Same labels |
| Statement of compliance (s. 9(2)) | None | Same labels deem the SoC requirement met (Sch. 2A) |

The Regulations cite **ETSI EN 303 645 V2.1.1 (June 2020)**; ETSI's current edition is **V3.1.3 (September 2024)**, which keeps the same provision numbering for 5.1-1, 5.1-2, 5.2-1 and 5.3-13. EN 303 645 groups its provisions into 13 security topics (5.1 no universal default passwords through 5.13 validate input data) plus data-protection provisions, and ETSI TS 103 701 is the companion conformance-assessment specification. PSTI mandates only the three topics above; a full EN 303 645 assessment is the natural evidence base for the statement of compliance and positions a product for the EU CRA. Note that the statement of compliance must record the identification number, version and date of any standard relied on (Sch. 4 para. 1(2)).

### Statement of compliance (SoC)

- Every in-scope product must be **accompanied** by an SoC or a regulation-prescribed summary before it is made available in the UK (s. 9 manufacturer, s. 15 importer, s. 22 distributor). OPSS guidance confirms the "document" need not be physical; digital accompaniment is acceptable, but each business must satisfy itself the SoC genuinely accompanies the product.
- **Minimum content (Regs Sch. 4):** product type and batch; name and address of each manufacturer and any authorised representative; declaration that the SoC is prepared by or for the manufacturer; declaration that the manufacturer has complied with the Sch. 1 requirements or the Sch. 2 deemed-compliance conditions (naming standard number, version and date where used); the defined support period as correct at first supply; signature, name and function of signatory; place and date of issue.
- **Retention:** manufacturers (reg. 8) and importers (reg. 9) keep a copy for the **longer of 10 years from issue or the defined support period**.
- Where deemed compliance via a label applies, importers and distributors must instead satisfy themselves the label conditions are met (ss. 15(5), 22(3)).

### Compliance-failure duties (Act Ch. 2)

| Actor | Duty to investigate | Duty to act and notify | Records |
|---|---|---|---|
| Manufacturer (ss. 10–12) | On being informed of a possible compliance failure, take all reasonable steps to investigate | As soon as practicable: stop making the product available and remedy the failure. **As soon as possible** notify the enforcement authority, other manufacturers, and importers/distributors supplied (and customers where regulations specify; none yet made) with details, known risks and remediation steps taken | Record every investigation and compliance failure; **retain 10 years** |
| Authorised representative (s. 13) | — | Contact the manufacturer as soon as possible, then notify the enforcement authority | Shares manufacturer record duty if delegated (s. 51) |
| Importer (ss. 16–20) | Investigate own or manufacturer failures on being informed | Must not supply a product it knows or believes is non-compliant. Remedy own failures and notify the enforcement authority; for manufacturer failures, contact the manufacturer, prevent further supply if remedy unlikely, and notify the enforcement authority and downstream distributors | Record own and known manufacturer investigations; **retain 10 years** |
| Distributor (ss. 23–25) | — | Must not supply a product it knows or believes is non-compliant. Remedy own failures and notify the enforcement authority; for manufacturer failures, contact the manufacturer (or upstream supplier), prevent further supply if remedy unlikely, and notify the enforcement authority and downstream recipients | No express record duty |

"Compliance failure" is a failure to meet a security requirement, not a security incident or a vulnerability as such. Nothing in PSTI requires reporting vulnerabilities or breaches to OPSS; the statutory clock is "as soon as possible" from awareness of a compliance failure, with no fixed hour count. Cross-notification chains are de-duplicated: a person told of a failure by another relevant person need not notify them back, and need not contact the manufacturer or the authority if told they already know (ss. 11(8), 19(10), 25(11)).

## Enforcement and penalties

- **Authority and powers.** The Secretary of State enforces (s. 26); functions are exercised by OPSS. Investigatory powers are those in **Schedule 5 to the Consumer Rights Act 2015** (including information notices, which OPSS can enforce through the courts), with the information-production powers usable for any Part 1 purpose (s. 26(4)).
- **Enforcement notices (ss. 28–33).** *Compliance notice* (remedy a duty within a period, supply evidence); *stop notice* (cease an activity, inform customers of risks); *recall notice* (arrange return of products, available only where other action would be insufficient). A **notice of intent with 10 days for representations** precedes each, except stop and recall notices in urgent cases. Notices may be varied only to be less onerous. Appeals lie to the **First-tier Tribunal** (s. 33). Failure to comply with an enforcement notice is an offence, punishable on summary conviction by a fine (s. 32), with a "took all reasonable steps" defence.
- **Monetary penalties (ss. 36–41).** Civil standard of proof (balance of probabilities). Maximum per breach the **greater of GBP 10 million or 4 % of qualifying worldwide revenue** for the most recent complete accounting period (GBP 10 million if no accounting period), plus a **daily penalty up to GBP 20,000** per day of continuing breach after the payment deadline. One penalty notice per breach; **28-day notice of intent** for representations; payment period at least 28 days; amount must be appropriate and proportionate, taking account of effects and remediation (s. 37). Appeal to the First-tier Tribunal on the decision, amount or period (s. 41). Penalties go to the Consolidated Fund. A penalty can be imposed with or without a prior enforcement notice.
- **Other tools.** Court **forfeiture orders** for non-compliant stock held by relevant persons or returned after a failure (ss. 42–44); power to **inform the public** about a compliance failure (s. 45) and to **publish details** of notices, penalties and forfeitures (s. 46); Secretary of State **recall and destruction** with cost recovery where a recall notice is ignored or cannot be served (s. 47); **compensation** for notices wrongly given (s. 34). **Directors, managers and officers** are personally liable for offences committed with their consent, connivance or neglect (s. 52).
- **OPSS practice (June 2025 enforcement-actions guidance).** Risk-based and proportionate, taking account of the regime's maturity; OPSS publishes every compliance, stop, recall and penalty notice; penalty starting points weigh harm, culpability and market position, then aggravating and mitigating factors; prosecution policy sits in the general OPSS Enforcement Policy.

## Timeline and status

| Date | Event |
|---|---|
| 14 October 2018 | UK Code of Practice for Consumer IoT Security published by DCMS with the NCSC: thirteen voluntary guidelines, the top three of which became the PSTI security requirements |
| June 2020 | ETSI EN 303 645 V2.1.1 published, the version cited in the Regulations |
| December 2022 | PSTI Act 2022 receives Royal Assent; enforcement-delegation power (s. 27) in force at Royal Assent |
| 14 September 2023 | SI 2023/1007 made after affirmative approval by both Houses |
| 29 April 2024 | Part 1 fully commenced (SI 2023/469 reg. 3); Regulations in force; OPSS begins enforcement |
| September 2024 | ETSI EN 303 645 V3.1.3 published (Regulations still cite V2.1.1) |
| 25 February 2025 | SI 2025/211: vehicle exceptions (GB) added to Sch. 3; drafting fix to Sch. 1 para. 3(3) |
| 17 March 2025 | OPSS/DSIT guidance page updated for the vehicle exceptions |
| June 2025 | OPSS publishes "Guidance on enforcement actions and associated rights" for the regime |
| 1 August 2025 | EU RED cybersecurity delegated act (2022/30) applies to radio equipment placed on the EU market |
| 4 December 2025 | SI 2025/1267: Japan JC-STAR STAR-1 and Singapore CLS labels become deemed-compliance routes for the security requirements and the SoC (mutual-recognition policy) |
| 7 April 2026 | Commencement No. 4 (SI 2025/1326) brings Part 2 telecoms-code provisions (ss. 61–64) into force; no effect on Part 1 |
| 11 September 2026 | EU CRA Art. 14 vulnerability and incident reporting applies to products sold in the EU |
| 11 December 2027 | EU CRA applies in full |
| By April 2029 | First statutory review report on the Regulations due within five years of commencement (reg. 10); subsequent reviews at intervals of no more than five years |

**Pending or evolving (as of September 2026):** no further amendments to Part 1 or the 2023 Regulations were found on legislation.gov.uk beyond those above; no regulations have yet been made under the Act's powers to require customer notification of compliance failures (ss. 11(5), 18(5), 24(5)), to prescribe an SoC summary, or to set group-level revenue rules for penalties (s. 38(6)). Whether DSIT will align the cited ETSI edition with V3.1.3, extend the security requirements toward the CRA baseline, or publish details of OPSS enforcement outcomes under the regime should be checked with [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md).

## Key obligations for security/GRC teams

1. **Classify every product SKU** against ss. 4–5 (internet- or network-connectable), s. 54 (UK consumer market, including refurbished and B2B-identical stock) and the Sch. 3 exceptions; record the determination and the role your entity plays (manufacturer including own-brand, importer, distributor, authorised representative). See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **Engineer out default credentials**: per-unit random passwords or forced user-set passwords at first use, with evidence that unique passwords are not derived from serial numbers, MAC addresses or counters; test the factory-reset path. Map to EN 303 645 5.1-1/5.1-2 via [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).
3. **Publish and run a vulnerability disclosure policy** with a contact point, acknowledgement and status-update timelines, in English, free of charge, no personal data demanded; align it with ISO/IEC 29147:2018 and make sure the intake actually works. Draft with [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md).
4. **Set and publish a defined support period with an end date** per product, prominent alongside price on your own sales pages, and treat it as a commitment: shortening it is a breach. Build the security-update pipeline and patch-release evidence to honour it. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
5. **Produce, ship and retain the statement of compliance** with all Sch. 4 fields, naming any standard, version and date relied on; retain for 10 years or the support period if longer; give importers and distributors a copy so they can lawfully supply. See [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).
6. **Wire compliance-failure handling into incident response**: triage rules for "is this a compliance failure", an "as soon as possible" notification path to OPSS and to the supply chain with the s. 11(6) content, and a 10-year investigation and failure record. Log it in [../../templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md) and see [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
7. **Importers and distributors: gate onboarding on PSTI evidence** (SoC or recognised label, support period, disclosure contact) and contractually require manufacturers to notify compliance failures and provide investigation records. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../workflows/vendor-onboarding.md](../../workflows/vendor-onboarding.md).
8. **Track deemed-compliance choices and gaps as formal exceptions** (for example a legacy product line relying on a Singapore or Japan label, or software components outside the Sch. 1 hardware/software categories) with owners and expiry dates, using [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
9. **Report to the board** on product-portfolio coverage, open compliance failures, support periods approaching expiry and enforcement exposure (up to 4 % of worldwide revenue plus personal officer liability). See [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).

## Interplay

- **EU Cyber Resilience Act (Regulation (EU) 2024/2847).** The CRA covers PSTI's three requirements and far more (Annex I essential requirements, vulnerability handling including a software bill of materials, a support period of at least five years unless the product's expected use is shorter, 24-hour early warning and 72-hour notification of actively exploited vulnerabilities and severe incidents from 11 September 2026, CE marking with mandatory third-party assessment for important class II products and for class I products not applying harmonised standards, fines up to EUR 15 million or 2.5 % of worldwide turnover). A product built to the CRA will satisfy PSTI, but not the reverse; the SoC is not an EU declaration of conformity and UK deemed-compliance labels have no CRA status. UK-established manufacturers selling into the EU need both. See the repository's EU Cyber Resilience Act pack.
- **RED cybersecurity delegated act (Delegated Regulation (EU) 2022/30).** Applies from 1 August 2025 (postponed from 1 August 2024 by Delegated Regulation (EU) 2023/2444) to internet-connected radio equipment, plus childcare, toy and wearable radio equipment processing personal, traffic or location data, and internet-connected equipment handling money or virtual currency. In Northern Ireland, products subject to Windsor Framework Annex 2 EU product legislation with a free-movement article are excepted from PSTI because EU rules apply instead (check whether the RED is the applicable instrument for a given product); Great Britain has no RED-equivalent cyber requirement beyond PSTI. See the repository's EU product security (RED and Machinery) pack.
- **UK GDPR / Data Protection Act 2018.** A vulnerability that exposes personal data triggers the controller's 72-hour breach notification to the ICO independently of any PSTI compliance failure; PSTI's "without personal data" rule for vulnerability reporters also shapes the disclosure form. See [gdpr.md](gdpr.md) and [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).
- **NIS2 / UK cyber-resilience law.** PSTI regulates the *makers* of products; NIS2 and the UK's network-and-information-systems rules regulate the *operators* who use them. Operators procuring consumer-grade connectable devices can use PSTI SoCs and support periods as supply-chain evidence. See [nis2.md](nis2.md).
- **Consumer law.** The support-period publication is tied to the Consumer Protection from Unfair Trading Regulations 2008 "invitation to purchase" concept; misstating it may also be a consumer-protection breach.
- **Standards and certifications.** ETSI EN 303 645 / TS 103 701 assessments, an ISO/IEC 29147-aligned disclosure process, and an ISO/IEC 27001 ISMS covering product security supply the evidence layer; see [../frameworks/iso-27001-2022.md](../frameworks/iso-27001-2022.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
- **Other jurisdictions.** Singapore's CLS (any level) and Japan's JC-STAR STAR-1 are now formally recognised UK routes, and the DSIT explanatory memorandum describes reciprocal accelerated access for PSTI-compliant UK products to those schemes. Other national IoT labelling schemes have no PSTI status. See [other-jurisdictions.md](other-jurisdictions.md).

## Primary sources

- Product Security and Telecommunications Infrastructure Act 2022, Part 1 (legal text, current version): https://www.legislation.gov.uk/ukpga/2022/46/part/1
- PSTI (Security Requirements for Relevant Connectable Products) Regulations 2023, SI 2023/1007 (legal text, as made and as amended): https://www.legislation.gov.uk/uksi/2023/1007
- PSTI (Security Requirements for Relevant Connectable Products) (Amendment) Regulations 2025, SI 2025/211 (legal text): https://www.legislation.gov.uk/uksi/2025/211/made
- PSTI (Security Requirements for Relevant Connectable Products) (Amendment) (No. 2) Regulations 2025, SI 2025/1267 (legal text) and its explanatory memorandum: https://www.legislation.gov.uk/uksi/2025/1267/made
- PSTI Act 2022 (Commencement No. 4, Saving and Transitional Provisions) Regulations 2025, SI 2025/1326 (legal text, Part 2 only): https://www.legislation.gov.uk/uksi/2025/1326/made
- DSIT policy paper, "The UK Product Security and Telecommunications Infrastructure (Product Security) regime" (regulator guidance, updated 2 May 2024): https://www.gov.uk/government/publications/the-uk-product-security-and-telecommunications-infrastructure-product-security-regime
- OPSS/DSIT guidance, "Regulations: consumer connectable product security" (regulator guidance, updated 17 March 2025): https://www.gov.uk/guidance/regulations-consumer-connectable-product-security
- OPSS, "Guidance on enforcement actions and associated rights" for the PSTI regime (regulator guidance, June 2025): https://www.gov.uk/government/publications/opss-enforcement-enforcement-actions/consumer-connectable-product-security-regulations
- ETSI EN 303 645 V3.1.3 (2024-09), Cyber Security for Consumer IoT: Baseline Requirements (publisher document): https://www.etsi.org/deliver/etsi_en/303600_303699/303645/03.01.03_60/en_303645v030103p.pdf
- Regulation (EU) 2024/2847 (Cyber Resilience Act), Art. 71 application dates (legal text): https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- Commission Delegated Regulations (EU) 2022/30 and (EU) 2023/2444 (RED cybersecurity delegated act and its postponement to 1 August 2025) (legal text): https://eur-lex.europa.eu/eli/reg_del/2022/30/oj and https://eur-lex.europa.eu/eli/reg_del/2023/2444/oj
- Not consulted directly: the Hansard debate on the draft (Amendment) (No. 2) Regulations 2025 was unavailable, so the enacted SI text and its explanatory memorandum were used instead. ISO/IEC 29147:2018 is paywalled; only the clause numbers cited in the Regulations are used here.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
