# Applicability Decision Trees per Major Regime

Structured trigger questions for the regimes most often mis-scoped. Each tree yields **Applies / Does not apply / Needs counsel review**, plus the facts that must be documented in the register rationale. Work every question in order; the first decisive answer ends the tree. Where a question depends on a fact you do not have, the output is not a guess — it is "open fact: [X]" in the register.

Regime substance (obligations, deadlines, penalties) lives in the context files linked per section — this file only answers "in scope or not."

## Index

| Group | Trees |
|---|---|
| [European Union and EEA](#european-union-and-eea) | 1 GDPR · 2 NIS2 · 3 CER Directive · 4 DORA · 5 EU AI Act · 6 Cyber Resilience Act · 7 Data Act · 8 eIDAS 2 · 9 European Health Data Space |
| [United Kingdom](#united-kingdom) | 10 UK NIS / Cyber Security and Resilience · 11 PSTI · 12 Financial operational resilience and critical third parties |
| [United States — financial services](#united-states--financial-services) | 13 SEC reporting and SOX · 14 GLBA and FTC Safeguards · 15 SEC Reg S-P / S-ID / SCI · 16 Banking 36-hour rule · 17 NYDFS Part 500 · 18 NAIC insurance data security |
| [United States — sector, federal-data and contract regimes](#united-states--sector-federal-data-and-contract-regimes) | 19 HIPAA · 20 NERC CIP · 21 TSA surface transportation · 22 FDA cyber devices · 23 CIRCIA · 24 CJIS · 25 IRS Pub 1075 · 26 FedRAMP · 27 Government contracts · 28 CMMC · 29 DOJ bulk data rule · 30 COPPA · 31 FERPA |
| [United States — state regimes](#united-states--state-regimes) | 32 Comprehensive privacy laws · 33 Biometric privacy laws · 34 State AI laws |
| [Asia-Pacific](#asia-pacific) | 35 Australia SOCI and Cyber Security Act · 36 APRA CPS 234/230 · 37 China CSL/DSL/PIPL · 38 India DPDP and CERT-In · 39 Japan APPI · 40 South Korea PIPA · 41 Singapore PDPA and Cybersecurity Act · 42 Hong Kong PDPO and PCICSO |
| [Americas beyond the United States](#americas-beyond-the-united-states) | 43 Canada · 44 Brazil LGPD |
| [Europe beyond the EU, Middle East and Africa](#europe-beyond-the-eu-middle-east-and-africa) | 45 Switzerland FADP and ISA · 46 Saudi Arabia PDPL and NCA · 47 United Arab Emirates · 48 Israel PPL · 49 South Africa POPIA |
| [Cross-sector and product regimes](#cross-sector-and-product-regimes) | 50 PCI DSS · 51 UN R155 / R156 |

Regimes with no tree here are not out of scope by implication — the library holds packs the trees do not cover (for example [`../../../context/regulations/eu-digital-services-act.md`](../../../context/regulations/eu-digital-services-act.md), [`../../../context/regulations/eu-eprivacy.md`](../../../context/regulations/eu-eprivacy.md), [`../../../context/regulations/new-zealand-privacy-act.md`](../../../context/regulations/new-zealand-privacy-act.md), [`../../../context/regulations/latin-america-privacy-regimes.md`](../../../context/regulations/latin-america-privacy-regimes.md), [`../../../context/regulations/southeast-asia-privacy-regimes.md`](../../../context/regulations/southeast-asia-privacy-regimes.md), [`../../../context/regulations/africa-privacy-regimes.md`](../../../context/regulations/africa-privacy-regimes.md) and [`../../../context/regulations/other-jurisdictions.md`](../../../context/regulations/other-jurisdictions.md)). Read the pack and build the test from its scope section.

---

# European Union and EEA

## 1. GDPR — territorial scope (Art. 3)

Context: `../../../context/regulations/gdpr.md`

**Q1. Does any group entity have an establishment in the EU/EEA** (subsidiary, branch, or stable arrangement exercising real activity — an office, local staff, even a single sales representative can suffice), **and is personal data processed in the context of that establishment's activities?**
- Yes → **GDPR applies** under Art. 3(1) to that processing, regardless of where the processing physically occurs or where the data subjects are. Record which entity/establishment.
- No → Q2.

**Q2. Does the organization offer goods or services (paid or free) to data subjects who are in the EU?** Targeting indicators (Recital 23): EU member-state language or currency where different from the org's home market, delivery to the EU, references to EU users/customers, EU top-level domains, marketing aimed at EU audiences. Mere accessibility of a website from the EU is **not** targeting.
- Yes → **GDPR applies** under Art. 3(2)(a) to processing related to that offering. Also test Q4.
- No → Q3.

**Q3. Does the organization monitor the behavior of data subjects as far as their behavior takes place in the EU?** (Tracking cookies with profiling, behavioral advertising, location tracking, fraud-scoring of EU users.)
- Yes → **GDPR applies** under Art. 3(2)(b) to that monitoring. Also test Q4.
- No → **GDPR does not apply.** Re-test trigger: EU market entry, EU analytics/tracking deployment.

**Q4. (If in scope via Art. 3(2) only.)** No EU establishment but caught by targeting/monitoring → an **EU representative** (Art. 27) is required unless the processing is occasional, excludes large-scale special-category/criminal data, and is unlikely to risk rights and freedoms. Representative appointment is a distinct register line item.

**Also record:** controller vs processor role per processing activity (processors are directly caught by Art. 3 too); UK GDPR as a separate row (tree 10's sibling regime — see `../../../context/regulations/uk-data-protection.md`, whose territorial test mirrors Art. 3 with the UK substituted); and, where personal data leaves the EEA, a Chapter V transfer row using `../../../context/regulations/eu-gdpr-international-transfers.md`.

**Counsel flags:** "targeting" edge cases (B2B contacts, employees of EU customers), group structures where an EU entity arguably processes "in the context of" a non-EU parent's activity.

---

## 2. NIS2 — entity classification

Context: `../../../context/regulations/nis2.md`

**Q1. Does the organization provide services or carry out activities in the EU in a sector listed in Annex I or Annex II?**
- Annex I (high criticality): energy; transport; banking; financial market infrastructure; health; drinking water; waste water; digital infrastructure (IXPs, DNS service providers, TLD registries, cloud computing, data centres, CDNs, trust service providers, public electronic communications networks/services); ICT service management (B2B managed service providers and managed security service providers); public administration; space.
- Annex II (other critical): postal and courier; waste management; chemicals (manufacture/production/distribution); food (production/processing/distribution); manufacturing (medical devices, computer/electronic/optical products, electrical equipment, machinery, motor vehicles, other transport equipment); digital providers (online marketplaces, online search engines, social networking platforms); research organizations.
- No → **Not in scope.** Re-test trigger: activity change into a listed sector.
- Yes → Q2.

**Q2. Size-cap test.** Is the entity at least **medium-sized** under the EU SME definition — 50 or more employees, **or** annual turnover (or balance sheet total) above EUR 10 million?
- Yes → in scope; go to Q4 to classify essential vs important.
- No (micro/small) → Q3.

**Q3. Size-independent inclusion.** Small/micro entities are still in scope if they are: qualified trust service providers; TLD name registries or DNS service providers; sole providers in a member state of a service essential to critical societal/economic activity; providers whose disruption could significantly impact public safety, security, or health, or induce systemic risk; critical entities under CER (tree 3); certain public administration entities; providers of public electronic communications networks/services (these are in scope regardless of size, classification by size). Any hit → in scope (member-state identification may be required for some categories). No hit → **Not in scope.**

**Q4. Essential vs important.** Broad rule: **essential** = Annex I sectors at **large** size (250+ employees, or turnover > EUR 50M / balance sheet > EUR 43M), plus the special categories designated essential regardless of size (e.g., qualified trust service providers, TLD registries and DNS providers, sole providers) and entities designated essential by a member state or under CER. **Important** = other in-scope entities (Annex I medium-sized; Annex II regardless of large/medium). Classification changes supervision intensity (ex-ante vs ex-post) and fine caps, not the core Art. 21 measures or Art. 23 reporting duties.

**Q5. Which member state(s)?** Jurisdiction generally follows establishment; for DNS/TLD/cloud/data centre/CDN/managed service/digital providers, main-establishment rules apply and non-EU providers of those services need an EU representative. National transpositions add registration duties and diverge in detail (see `../../../context/regulations/eu-nis2-implementing-and-transposition.md`) → **counsel/local review flag for every multi-state footprint.**

---

## 3. CER Directive — critical entity identification

Context: `../../../context/regulations/eu-cer-directive.md`

CER is a **designation** regime, not a self-identification one: an entity is in scope only once a member state identifies it (Art. 2(1), Art. 6).

**Q1.** Does the entity provide an essential service in one of the Annex's 11 sectors — energy; transport; banking; financial market infrastructure; health; drinking water; waste water; digital infrastructure; public administration; space; production, processing and distribution of food?
- No → **Not in scope.**
- Yes → Q2.

**Q2.** Does it operate, with its critical infrastructure located, on the territory of a member state?
- No → **Not in scope** (CER has no extraterritorial limb; dependencies reach you only through a customer's risk assessment).
- Yes → Q3.

**Q3.** Would an incident have significant disruptive effects on that service or on dependent services, judged against the Art. 7(1) criteria (users, cross-sector dependency, degree and duration of impact, market share, geographic area including isolation, availability of alternatives)? All three criteria of Art. 6(2) are cumulative.
- Plausibly yes → **candidate for identification** — the member state decides. Record "awaiting/subject to national identification"; entity-level Chapter III obligations apply 10 months after notification (Art. 6(3)).
- No → **Not in scope**, re-test on growth in users or market share.

**Q4. Carve-out check.** Entities in banking, financial market infrastructure and digital infrastructure (Annex points 3, 4, 8) are identified, but Art. 11 and Chapters III, IV and VI do not apply to them (Art. 8) — DORA and NIS2 carry the equivalent duties instead. Art. 1(3) disapplies CER where sector-specific EU law imposes at-least-equivalent resilience measures. National-security, public-security, defence and law-enforcement public administration is excluded (Art. 1(5)–(8)).

**Counsel flag:** whether a national transposition has set thresholds that pull the entity in, and whether identification under CER also makes the entity "essential" under NIS2.

---

## 4. DORA — financial entity types

Context: `../../../context/regulations/dora.md`

**Q1. Is the organization one of the financial entity types listed in DORA Art. 2?** Principal list: credit institutions; payment institutions; account information service providers; electronic money institutions; investment firms; crypto-asset service providers and issuers of asset-referenced tokens; central securities depositories; central counterparties; trading venues; trade repositories; managers of alternative investment funds; UCITS management companies; data reporting service providers; insurance and reinsurance undertakings; insurance, reinsurance, and ancillary insurance intermediaries; institutions for occupational retirement provision; credit rating agencies; administrators of critical benchmarks; crowdfunding service providers; securitisation repositories.
- Yes → **DORA applies** to that entity. Note the exclusions/carve-outs (e.g., certain small AIFMs under the AIFMD registration regime, small IORPs, microenterprise intermediaries, and entities excluded from their sectoral directive) and proportionality provisions — verify the specific entity type against Art. 2's exclusion list. **Counsel flag** for borderline license types. Register the applicable RTS/ITS detail separately from `../../../context/regulations/eu-dora-technical-standards.md`.
- No → Q2.

**Q2. Does the organization provide ICT services to EU financial entities** (software, cloud, data analytics, data centres, managed services)?
- Yes → not directly a DORA obligor, but two exposures: (a) **contractual flow-down** — financial entity customers must impose DORA-derived contract terms (Art. 30: audit/access rights, exit strategies, incident support, subcontracting conditions); (b) possible designation as a **critical ICT third-party provider (CTPP)** subject to direct oversight by an ESA-led framework, with fees and remediation powers. Register as "contractual + designation risk," not "applies."
- No → **Not in scope.**

---

## 5. EU AI Act — role and reach

Context: `../../../context/regulations/eu-ai-act.md`

**Q1.** Does the org **place on the EU market or put into service** AI systems (or general-purpose AI models), regardless of where the org is established? → **provider** obligations by risk tier.
**Q2.** Is the org established/located in the EU and **using** AI systems under its authority (other than personal non-professional use)? → **deployer** obligations.
**Q3.** Is the org outside the EU but the **output** of its AI system is used in the EU? → in scope.
**Q4.** Importer/distributor of AI systems into the EU market? → respective obligations.
Any yes → classify each system by tier (prohibited / high-risk per Annex III and product-safety route / transparency-risk / minimal) and add register rows per role. Timeline staggering matters — obligations phase in by tier; see the context file. Hand system-level analysis to `../../ai-governance/SKILL.md`.

---

## 6. EU Cyber Resilience Act — products with digital elements

Context: `../../../context/regulations/eu-cyber-resilience-act.md`

**Q1. Product test (Art. 3(1)).** Does the org make available on the EU market any software or hardware product — or a component placed on the market separately — whose intended or reasonably foreseeable use includes a direct or indirect logical or physical data connection to a device or network? Remote data processing counts only where the manufacturer designs it and the product cannot perform a function without it (Art. 3(2)).
- No → **Not in scope** (a standalone cloud service with no product dependency is generally read as outside the CRA; the provider may still be a NIS2 entity — tree 2).
- Yes → Q2.

**Q2. Exclusion test (Art. 2(2)–(8)).** Is the product covered by the Medical Devices Regulation (EU) 2017/745, the IVDR, vehicle type-approval Regulation (EU) 2019/2144, civil-aviation Regulation (EU) 2018/1139 or marine-equipment Directive 2014/90/EU; an identical spare part; or developed exclusively for national security, defence or classified processing?
- Yes → **Out of scope** for the CRA; test the sectoral regime instead (tree 51 for vehicles, tree 22 for US devices).
- No → Q3.

**Q3. Role test.** Manufacturer (Art. 3(13), no EU establishment needed) · deemed manufacturer through own-branding or **substantial modification** (Arts. 21–22) · authorised representative (Art. 18) · importer (Art. 19) · distributor (Art. 20) · open-source software steward (Arts. 3(14), 24 — no administrative fines under Art. 64(10)). Record every role the group holds; each carries a different obligation set.

**Q4. Free and open-source software.** Only FOSS made available on the market **in the course of a commercial activity** is in scope; non-monetised FOSS and individual contributors to code they do not control are out, and hosting on a repository or package manager is not "making available" (Recitals 18, 20).

**Q5. Conformity route.** Is the product listed in Annex III (important, class I or II) or Annex IV (critical)? Class II, and class I absent applicable harmonised standards, need notified-body assessment; everything else is manufacturer self-assessment (module A).

**Q6. Timing.** Chapter IV (notified bodies) applies from 11 June 2026, Art. 14 reporting from 11 September 2026, the rest from 11 December 2027. Products placed on the market before 11 December 2027 are caught only if substantially modified after that date — **except** Art. 14 reporting, which applies regardless of placement date (Art. 69(2)–(3)).

**Counsel flag:** whether a connected service is a "remote data processing solution", and whether a change is a "substantial modification" that makes the org a manufacturer.

---

## 7. EU Data Act — connected products and data processing services

Context: `../../../context/regulations/eu-data-act.md`

**Q1.** Does the org manufacture a **connected product** (an item that obtains, generates or collects data on its use or environment and can communicate it, whose primary function is not storing or processing data for others — Art. 2(5)) placed on the EU market, or provide a **related service** to EU users? Establishment is irrelevant.
- Yes → Chapter II access and sharing duties apply; go to Q3.
- No → Q2.

**Q2.** Does the org provide a **data processing service** (IaaS, PaaS or SaaS — Art. 2(8)) to customers in the EU?
- Yes → Chapter VI switching and egress duties and Chapter VII international-access safeguards apply. Note switching charges are abolished from 12 January 2027 and Chapter IV reaches certain legacy contracts from 12 September 2027.
- No → is the org a data holder, data recipient, data-space participant or smart-contract vendor under Art. 1(3)? If none → **Not in scope.**

**Q3. SME exemption (Art. 7).** Chapter II duties do not apply to data from products or services of micro and small enterprises, nor to a medium-sized enterprise in its first year of that status, nor for one year after a medium-sized enterprise places a product on the market — unless the enterprise is partnered with or linked to a larger one, or acts as a subcontractor.

**Q4. Representative.** A non-EU entity offering connected products or related services in the EU must designate an EU legal representative (Art. 37(11)–(13)); until it does, every member state's authority may act against it.

**Also record:** content data is outside Chapter II (Art. 1(2)(a)); the GDPR prevails on conflict (Art. 1(5)); DMA gatekeepers cannot be eligible third-party data recipients (Art. 5(3)).

---

## 8. eIDAS 2 — trust services, wallets and relying parties

Context: `../../../context/regulations/eu-eidas2.md`

**Q1.** Does the org, established in the Union, provide a **trust service** on the Art. 3(16) list (certificates, e-signatures, e-seals, time stamps, registered delivery, website authentication, attestations of attributes, archiving, ledgers, remote signature-device management)?
- Yes → **TSP obligations apply**; record qualified vs non-qualified status, because the duty set and the supervisory route differ. Services used exclusively within a closed system under national law or agreement between a defined set of participants are excluded (Art. 2(2)).
- No → Q2.

**Q2.** Does the org provide a **EUDI Wallet** directly by, under mandate from, or recognised by a member state (Art. 5a(2))? → wallet-provider duties, with listed QTSP duties applying mutatis mutandis (Art. 5a(20)).

**Q3.** Does the org intend to **rely on wallets** to provide public or private services by digital interaction (Art. 5b)? → it must register as a relying party in its member state of establishment; an intermediary acting for a relying party is itself deemed one.

**Q4. Mandatory acceptance (Art. 5f).** Is the org a public-sector body requiring eID for online services; a private relying party (other than a micro or small enterprise) required by law or contract to use strong user authentication in transport, energy, banking, financial services, social security, health, drinking water, postal, digital infrastructure, education or telecoms; or a very large online platform under DSA Art. 33? → wallet acceptance becomes mandatory on the user's voluntary request, from 36 months after the wallet implementing acts.

**Q5.** Does the org provide a **web browser**? → Art. 45 recognition of QWACs and display duties; micro and small browser providers are exempt for their first 5 years (Art. 45(1a)).

- No hit on Q1–Q5 → **Not in scope.** Third-country TSPs gain legal equivalence only through a Commission implementing act or EU agreement (Art. 14) → **counsel flag.**

---

## 9. European Health Data Space — health data holders and EHR systems

Context: `../../../context/regulations/eu-ehds.md`

**Q1.** Is the org a **healthcare provider** or employer of health professionals processing health data electronically in the EU? → registration of priority-category data in an EHR system, traceability and connection to the national contact point (Arts. 11–13, 23(5)).

**Q2.** Does the org manufacture, import or distribute an **EHR system** — software (or hardware plus software) letting priority-category health data be stored, intermediated, exported, imported, converted, edited or viewed, intended by the manufacturer for healthcare providers in patient care or for patients accessing their own data (Art. 2(2)(k))? General-purpose software used in healthcare is excluded (Art. 25(2)); in-house systems inside EU health institutions and SaaS offered to EU persons count as "put into service" (Art. 26(2)).
- Yes → manufacturer duties apply. Commission FAQ examples in scope: pharmacy dispensing systems, patient portals, format-conversion layers; out of scope: appointment schedulers, billing systems not processing priority-category data, non-medical wellness apps.

**Q3.** Does the org market a **medical device, IVD or high-risk AI system claiming EHR interoperability** (Art. 27) or a **wellness application claiming it** (Arts. 47–49)? → the Annex II essential requirements and common specifications attach.

**Q4. Health data holder test (Art. 2(2)(t)).** Is the org a natural or legal person, public authority or body in the health or care sector, a developer of products or services for that sector, a wellness-app developer, a health-related researcher or a mortality registry that, as controller, has the right or obligation to process personal electronic health data — or can make non-personal health data available through control of a product's technical design?
- Yes → secondary-use duties. **Processors are not holders** for data they process on a controller's behalf; natural persons (including individual researchers) and **microenterprises are exempt** unless national law extends the duties (Art. 50).
- No → Q5.

**Q5.** Does the org seek access to health data for secondary use as a **health data user** under a data permit (Art. 2(2)(u))? Third-country applicants are eligible only via an authorised HealthData@EU participant or a Commission reciprocity act (Art. 91).

- No hit → **Not in scope.** Processing outside Union law and criminal-law processing by competent authorities are excluded (Art. 1(9)).

---

# United Kingdom

## 10. UK NIS / Cyber Security and Resilience regime

Context: `../../../context/regulations/uk-nis-cyber-security-resilience.md`

**Q1. Operator of essential services (Part 3).** Does the org provide a Schedule 2 essential service in energy, transport, health, drinking water or digital infrastructure that relies on network and information systems **and** meet that service's threshold (illustrative: electricity supply to more than 250,000 final customers; aerodromes above 10 million annual terminal passengers; potable water to at least 200,000 people; DNS resolvers serving at least 500,000 UK IP addresses)?
- Yes → **deemed designated** as an OES; notify the competent authority in writing within three months (reg 8(2), (11)).
- No → Q2 — but note a competent authority may still designate a below-threshold provider under reg 8(3)–(4).

**Q2. Relevant digital service provider (Part 4).** Does the org provide an online marketplace, online search engine or cloud computing service in the UK, with a UK head office or nominated UK representative, and is it **not** a micro or small enterprise (ICO guidance: fewer than 50 staff with turnover and/or balance sheet below EUR 10 million, assessed at group level)?
- Yes → **RDSP in scope**; a non-UK provider must nominate a UK representative within three months (reg 14A).

**Q3. Exclusion.** Telecoms providers subject to sections 105A–105C of the Communications Act 2003 are outside the NIS Regulations (reg 8(1A)).

**Q4. Reform horizon.** The Cyber Security and Resilience Bill is **not yet an Act**. If enacted and commenced, it adds data centres (rated IT load of at least 1 MW, or at least 10 MW for enterprise data centres run solely for the owner's own IT), medium and large managed service providers, large load controllers (at least 300 MW of potential electrical control), and regulator-designated critical suppliers. Register these as "monitor", not "applies", and track through `../../regulatory-horizon-scanning/SKILL.md`.

**Also record:** the UK data-protection row separately (`../../../context/regulations/uk-data-protection.md`) — it is a different test and a different regulator.

---

## 11. UK PSTI — consumer connectable products

Context: `../../../context/regulations/uk-psti-product-security.md`

**Q1. Product test (ss. 4–5).** Is the product **internet-connectable** (able to connect to the internet over an Internet Protocol suite protocol) or **network-connectable** (sends and receives data by electrical or electromagnetic transmission and connects directly to an internet-connectable product, or to two or more products at once over a non-IP protocol)?
- No → **Not in scope.**
- Yes → Q2.

**Q2. Excepted products (Regs Sch. 3).** Is it supplied only in Northern Ireland under Windsor Framework product law; an EV charge point under the 2021 Regulations; a medical device under the Medical Devices Regulations 2002 (unless regulated medical software is merely installed on an otherwise connectable product); a licence-holder smart meter assured under the NCSC Commercial Product Assurance scheme; a desktop, laptop or tablet **without** cellular connectivity (unless designed exclusively for children under 14); or, in Great Britain, a vehicle product under Regulation (EU) 2018/858, 168/2013 or 167/2013?
- Yes → **Out of scope.** Note smartphones and cellular tablets are in scope.
- No → Q3.

**Q3. Market test (s. 54).** Will the product be made available to consumers in the UK (or to non-consumer customers where identical products are made available to consumers) and not previously supplied to any customer? Returned, recalled or manufacturer-reconditioned units count as not previously supplied — refurbished-as-new stock is in scope; ordinary second-hand resale is not.

**Q4. Role (s. 7).** Manufacturer (including own-brand labellers) · importer · distributor. A non-UK manufacturer may appoint a UK authorised representative (s. 51), which does not relieve it of liability.

**Q5. Reach (ss. 8, 14, 21).** The manufacturer's location is irrelevant: the trigger is intending, or being aware or "ought to be aware", that the product will be a UK consumer connectable product → **overseas sellers into the UK are directly bound.**

---

## 12. UK financial operational resilience and critical third parties

Context: `../../../context/regulations/uk-financial-operational-resilience.md`

**Q1. Operational resilience rules (SYSC 15A / PRA Operational Resilience Parts).** Is the firm an enhanced-scope SM&CR firm, bank, building society, PRA-designated investment firm, Solvency II firm, UK RIE, e-money or payment institution, RAISP or consolidated tape provider (FCA), or a UK bank, building society, PRA-designated investment firm, Solvency II firm, the Society of Lloyd's or a managing agent (PRA)?
- Yes → in scope; the impact-tolerance compliance deadline of 31 March 2025 has passed, so treat this as a live obligation, not a project. For PIs and EMIs it bites only on payment/e-money activity (SYSC 15A.1.8R).
- No → Q2. Firms whose registered or head office is outside the UK (SYSC 15A.1.4R) and temporary-permission firms (15A.1.3R) are excluded.

**Q2. Outsourcing and third-party risk.** Is the firm a common-platform firm or otherwise within SYSC 8.1, or a PRA firm within SS2/21 (banks, building societies, PRA-designated investment firms, Solvency II insurers and groups, third-country branches, with parts applying to credit unions and non-directive firms)? → "critical or important" / "material" outsourcing duties apply.

**Q3. Operational incident and material third-party reporting (in force 18 March 2027).** Does the firm hold a Part 4A permission, or is it a PSP, UK RIE, registered trade repository or registered credit rating agency (FCA), or a UK bank, building society, PRA-designated investment firm, UK branch of an overseas bank, UK Solvency II firm, the Society of Lloyd's or a managing agent (PRA)? MTP notification and register duties reach a narrower list, including UK credit unions with at least GBP 50m total assets on the PRA side. Register with the 2027 date; a dual-regulated firm makes one submission.

**Q4. Critical third party (FSMA ss. 312L–312V).** Does the org provide services to authorised persons, PSPs/EMIs or FMI entities such that failure or disruption "could threaten the stability of, or confidence in, the UK financial system"? Designation is HM Treasury's, not self-assessed; the first four CTPs were designated with effect from 13 July 2026.
- Provider, not yet designated → register as "designation risk + contractual flow-down", not "applies".

**Counsel flag:** third-country branch treatment, which differs between the FCA and PRA registers and notification duties.

---

# United States — financial services

## 13. SEC reporting and SOX — listed status

Context: `../../../context/regulations/sec-cyber-disclosure.md`, `../../../context/regulations/sox-itgc.md`

**Q1. Is the organization an SEC registrant** (securities registered under the Exchange Act, or required to file periodic reports)?
- No → SOX and SEC disclosure do not apply. Re-test trigger: IPO preparation (obligations begin with the registration process), US listing, or crossing shareholder-of-record thresholds.
- Yes → Q2.

**Q2. Domestic issuer or foreign private issuer (FPI)?**
- **Domestic:** cyber disclosure via **Form 8-K Item 1.05** (material incidents, four business days from materiality determination) and **Form 10-K Item 106** (Reg S-K: risk management, strategy, governance).
- **FPI:** furnish material incident information on **Form 6-K**; annual report cyber disclosure in **Form 20-F**. Do not put 8-K obligations in an FPI's register.

**Q3. SOX scope.** All registrants: s302 officer certifications and s404(a) management assessment of ICFR — ITGCs over financially relevant systems in scope. **s404(b) auditor attestation** depends on filer category (accelerated and large accelerated filers; exemptions for smaller/emerging companies) → record filer status as a register fact. Newly public companies get transition accommodations → counsel/auditor confirmation.

**Q4. Adjacent:** listed on a non-US exchange → that market's listing rules and disclosure regime instead (register per jurisdiction). Market infrastructure and broker-dealer registrants also test tree 15.

---

## 14. GLBA — "financial institution" test (and FTC Safeguards Rule)

Context: `../../../context/regulations/glba-ftc-safeguards.md`

**Q1. Is the organization significantly engaged in financial activities** (as defined by reference to the Bank Holding Company Act §4(k))? This reaches far beyond banks. FTC-jurisdiction examples: mortgage lenders and brokers, payday and other non-bank lenders, finance companies, auto dealers that extend credit or lease, check cashers, wire transfer / money services businesses, collection agencies, credit counselors, tax preparation firms, investment advisors not required to register with the SEC, and "finders" bringing together buyers and sellers of financial products. Higher-education institutions participating in federal student aid are held to Safeguards Rule compliance.
- No → Not a GLBA financial institution. Re-test trigger: launching lending, payment, or advisory activity.
- Yes → Q2.

**Q2. Does it handle nonpublic personal information of consumers** (individuals obtaining financial products/services for personal/family/household purposes)?
- No (pure B2B financial activity) → GLBA privacy/safeguards obligations largely fall away — counsel flag before concluding.
- Yes → Q3.

**Q3. Which regulator?** Banks/credit unions → prudential regulators' safeguards and the Interagency Guidelines, plus the 36-hour incident notification rule (tree 16, `../../../context/regulations/us-banking-incident-notification-third-party.md`). Broker-dealers/advisers → SEC Regulation S-P (tree 15, `../../../context/regulations/us-sec-reg-sp-reg-sci.md`). Everyone else → **FTC Safeguards Rule**: written ISP, qualified individual, risk assessment, the rule's enumerated safeguards (encryption, MFA, access controls, monitoring/pen-testing, vendor oversight, IR plan, board reporting), and FTC notification of security events affecting **500+ consumers' unencrypted customer information within 30 days of discovery**. Note the rule's limited exemption for institutions maintaining information on fewer than 5,000 consumers (exempts some written-documentation elements, not the safeguards themselves).

**Also:** receiving consumer financial data *from* financial institutions can bind a non-FI via GLBA reuse/redisclosure limits — register as contractual/derived.

---

## 15. SEC Regulation S-P / S-ID / SCI — covered institutions

Context: `../../../context/regulations/us-sec-reg-sp-reg-sci.md`

**Q1. Reg S-P § 248.30 (safeguards, incident response, disposal).** Is the org a broker or dealer (funding portals comply as brokers do), an investment company, an SEC-registered investment adviser, or a transfer agent registered with the SEC or another appropriate regulatory agency?
- Yes → **covered institution**; the 2024 amendments' incident-response and customer-notification duties apply — compliance dates of 3 December 2025 (larger entities) and 3 June 2026 (smaller entities) have both passed.
- No → Q3.

**Q2. Reg S-P privacy provisions (§ 248.1(b)).** Same population plus SEC-registered non-resident firms, limited to nonpublic personal information about individuals obtaining products primarily for personal, family or household purposes. Unregistered foreign firms are excluded; HIPAA is not displaced for health information.

**Q3. Reg S-ID (§ 248.201(a)).** Is the org a broker, dealer or other person registered (or required to be) under the Exchange Act, a registered (or required to be registered) investment company including BDCs and employees' securities companies, or a registered (or required to be registered) investment adviser — **and** does it offer or maintain "covered accounts" (consumer accounts permitting multiple payments or transactions, or any account with reasonably foreseeable identity-theft risk)?
- Both yes → identity-theft prevention programme required.

**Q4. Reg SCI (§ 242.1000).** Is the org an SCI SRO (exchange, registered securities association, registered clearing agency, the MSRB); an SCI ATS meeting the NMS-stock volume thresholds (5% in any single stock and 0.25% overall, or 1% overall, of average daily dollar volume in 4 of the preceding 6 months; 5% for non-NMS equities); a plan processor; an exempt clearing agency subject to ARP; or an SCI competing consolidator (5% of consolidated market-data revenue)?
- Yes → SCI systems and indirect SCI systems in scope; new SCI ATSs and competing consolidators get six months after first meeting a threshold.

**Q5.** FINRA members additionally carry Rule 4370 business-continuity duties, tailorable to size with documented rationale for non-applicable categories.

---

## 16. US banking 36-hour incident notification rule

Context: `../../../context/regulations/us-banking-incident-notification-third-party.md`

**Q1. Banking organization test.** Is the entity a national bank, federal savings association or federal branch/agency of a foreign bank (12 CFR 53); a US bank holding company or S&L holding company, state member bank, US operation of a foreign banking organization, or Edge/agreement corporation (12 CFR 225.300–303); an insured state nonmember bank, insured state savings association or insured state-licensed branch of a foreign bank (12 CFR 304.21–24)?
- Yes → **36-hour notification rule applies**; holding companies are in scope, not only the bank.
- No → Q2.

**Q2. Credit union test.** Federally insured credit union? → 12 CFR 748.1(c), a **72-hour** clock with a broader trigger.

**Q3. Bank service provider test.** Does the org perform **covered services** subject to the Bank Service Company Act (12 U.S.C. 1861–1867) — core processing, cloud and hosting, payment processing and similar?
- Yes → **directly bound** by the service-provider notification duty, owed to each affected banking-organization customer and applying "independent of any contractual provisions", even though the org is not a bank.

**Q4. Exclusions.** Designated financial market utilities are carved out. Non-bank financial institutions (fintechs, lenders, brokers, dealers) are outside the rule — test trees 14 and 15 instead — but may still be *bank service providers* under Q3.

**Q5. Third-party risk overlay.** The 2023 interagency third-party guidance applies to all OCC-, FRB- and FDIC-supervised banking organizations and defines a third-party relationship as *any business arrangement*, including affiliates, fintech partners, referral arrangements and merchant payment processing. A replacement proposal was published 15 September 2026 → **monitor**, do not restate as settled law.

---

## 17. NYDFS Part 500 — covered entity and Class A

Context: `../../../context/regulations/us-nydfs-part-500.md`

**Q1. Covered entity (§500.1(e)).** Is the org (or the individual) licensed, registered, chartered, certified, permitted or accredited — or required to be — under the New York Banking Law, Insurance Law or Financial Services Law? Regulation by another agency does not displace Part 500, and individuals such as insurance producers are covered entities in their own right.
- No → **Not in scope.** Re-test trigger: any New York licensing event.
- Yes → Q2. Note the reach attaches to the DFS authorization, not to New York data: a licensed entity is in scope wherever it is headquartered, and the tests below count worldwide operations.

**Q2. Full exemption (§500.19(b), (e), (g)).** Is the org an employee, agent or wholly owned subsidiary covered by another covered entity's programme; an inactive individual broker with no information systems and no NPI; or one of the listed persons such as an accredited or certified reinsurer or inactive agent?
- Yes → full exemption; no annual notification required.
- No → Q3.

**Q3. Limited exemption (§500.19(a), (c), (d)).** Does the org meet any one of: fewer than 20 employees and independent contractors (entity plus affiliates); less than USD 7.5m gross annual revenue in each of the last three fiscal years (entity worldwide plus affiliates' NY operations); less than USD 15m year-end total assets under GAAP including all affiliates — or is it an entity with no information systems and no NPI, or a captive insurer holding only parent/affiliate NPI?
- Yes → limited exemption from the listed sections, but **still** subject to risk assessment (§500.9), access privileges (§500.7), third-party policy (§500.11), reduced-scope MFA (§500.12(a)), asset inventory and data disposal (§500.13), training (§500.14(a)(3)) and notices (§500.17). File a Notice of Exemption within 30 days of determining eligibility (§500.19(f)); 180 days to comply fully once the org ceases to qualify (§500.19(h)).
- No → Q4.

**Q4. Class A company (§500.1(d)).** At least USD 20m gross annual revenue in each of the last two fiscal years (entity worldwide plus affiliates' NY operations) **and** either more than 2,000 employees averaged over two years or more than USD 1bn gross annual revenue in each of the last two years, counting only affiliates that share information systems, cybersecurity resources or any part of the programme?
- Yes → **Class A**: the heightened obligations apply on top of the full programme.
- No → standard covered entity.

---

## 18. NAIC Insurance Data Security Model Law — licensee

Context: `../../../context/regulations/us-naic-insurance-data-security.md`

The model binds only as enacted, so run this state by state.

**Q1.** Has the state in question enacted the model (or an equivalent insurance data security law)?
- No → **Not applicable in that state**; the comprehensive privacy and breach-notification rows still stand (tree 32 and its always-on list).
- Yes → Q2.

**Q2. Licensee test (§3I).** Is the org licensed, authorized to operate, or registered — or required to be — under that state's insurance laws? This reaches producers and agencies, not only carriers. Excluded: purchasing groups and risk retention groups chartered and licensed in another state, and a licensee acting as an assuming insurer domiciled elsewhere.

**Q3.** Does the org hold **Nonpublic Information** as defined in §3K (business information whose compromise would materially harm the licensee; consumer identifiers combined with SSN, licence/ID number, account or card number, access code or biometric record; or health information other than age or gender)?

**Q4. Small-licensee exception (§9A(1)).** Fewer than 10 employees **including independent contractors** → exempt from §4 (the information security programme) only; §5 investigation and §6 notification duties still apply. Virginia's enactment has no headcount exception.

**Q5. Deeming exceptions.** A HIPAA-covered licensee maintaining a HIPAA security programme is deemed to meet §4 on filing a written certification (§9A(2)); an employee, agent, representative or designee covered by another licensee's programme need not run its own (§9A(3)); in Virginia only, a licensee affiliated with a depository institution complying with the federal Interagency Guidelines is deemed to meet the programme section.

**Q6.** Loss of an exception gives 180 days to comply (§9B).

---

# United States — sector, federal-data and contract regimes

## 19. HIPAA — covered entity and business associate tests

Context: `../../../context/regulations/hipaa.md`

**Q1. Covered entity test.** Is the organization any of:
- a **health plan** (insurers, HMOs, employer group health plans — note: self-insured employer plans make the *plan* a CE, not the employer generally);
- a **healthcare clearinghouse**; or
- a **healthcare provider that transmits health information electronically in connection with a HIPAA standard transaction** (claims, eligibility, enrollment...)? A provider that never bills electronically via standard transactions is not a CE.
- Yes → **HIPAA applies as CE.** Consider hybrid-entity designation if only part of the org performs covered functions → counsel flag.
- No → Q2.

**Q2. Business associate test.** Does the organization **create, receive, maintain, or transmit PHI on behalf of a CE** (or another BA) to perform a covered function or service — claims processing, data analytics, billing, cloud hosting of PHI, IT services touching PHI?
- Yes → **HIPAA applies as BA** (Security Rule directly; Privacy Rule per BAA; Breach Notification duty to the CE). A subcontractor of a BA is itself a BA. Cloud providers holding encrypted PHI are BAs even without keys.
- No → Q3.

**Q3. Common traps before concluding "no":** employee health data in an employer's hands as employer is generally **not** PHI (but the group health plan's data is); health data collected direct-to-consumer outside a CE relationship (wellness apps) is outside HIPAA but inside the FTC Health Breach Notification Rule (`../../../context/regulations/us-ftc-act-health-breach-rule.md`) and state health-privacy laws (e.g., Washington My Health My Data) — add those rows instead. No hit → **HIPAA does not apply.** Re-test trigger: first healthcare customer or PHI-touching service.

---

## 20. NERC CIP — bulk electric system

Context: `../../../context/regulations/nerc-cip.md`

**Q1. Registration test (CIP-002-5.1a §4.1).** Is the org registered with NERC as a Balancing Authority, Generator Owner, Generator Operator, Reliability Coordinator, Transmission Owner, Transmission Operator or Interchange Coordinator/Authority — or as a Distribution Provider that owns qualifying UFLS/UVLS systems (automatic shedding of at least 300 MW), Remedial Action Schemes, transmission Protection Systems or Cranking Paths for Blackstart Resources?
- No → **Not in scope.** Facilities used in the local distribution of electric energy are excluded by statute (16 U.S.C. §824o(a)(1)).
- Yes → Q2.

**Q2. Cyber system test.** Would loss, compromise or misuse of the system adversely impact reliable operation **within 15 minutes**? The 15-minute test is what keeps corporate IT and most business systems out of scope.
- No → out of scope for CIP, though the asset may still be in a wider programme.
- Yes → Q3.

**Q3. Impact rating (Attachment 1).** **High** — BES Cyber Systems at a Reliability Coordinator's Control Centre, a Balancing Authority's Control Centre for at least 3,000 MW aggregate generation in one Interconnection, or a Transmission or Generator Operator Control Centre controlling medium-impact assets. **Medium** — generation of at least 1,500 MW at one plant, reactive resources of at least 1,000 MVAR, transmission at 500 kV or above, 200–499 kV stations with aggregate weighted value above 3,000, IROL-critical facilities, nuclear interface facilities, qualifying RAS/SPS and UFLS/UVLS, and other Control Centres at the stated thresholds. **Low** — everything else.

**Q4. Associated systems.** EACMS, PACS and PCAs sharing an ESP carry obligations in their own right — scope them explicitly.

**Q5. Exemptions.** Cyber systems at facilities regulated by the Canadian Nuclear Safety Commission, systems under an NRC 10 CFR §73.54 cyber security plan, and communication networks between discrete ESPs are exempt (§4.2.3). In **Canada**, NERC standards bind through provincial regulators with their own versions and effective dates → check the provincial register, not the US status list.

---

## 21. TSA surface transportation cyber directives

Context: `../../../context/regulations/us-tsa-transportation-cyber.md`

The surface directives are **notification-driven**: scope follows a TSA letter, not self-assessment.

**Q1. Pipelines and LNG.** Has TSA notified the owner/operator that its pipeline system or facility is **critical** (9/11 Act §1557(b), 6 U.S.C. 1207)?
- Yes → SD Pipeline-2021-01G / -02G apply to the operator's **Critical Cyber Systems** — any IT or OT system or data whose compromise could cause operational disruption, including business services. An operator with none must tell TSA in writing within 60 days of the SD's effective date.

**Q2. Rail.** Is the org a freight railroad carrier identified in 49 CFR 1580.101, a TSA-designated freight or passenger railroad, or a TSA-specified higher-risk rail transit or passenger railroad? → the SD 1580/1582 series applies. All other surface operators received the voluntary Information Circulars instead — register those as guidance, not obligation.

**Q3. Aviation.** Is the org a TSA-regulated airport or aircraft operator that received an emergency amendment to its security programme? → in scope through the amendment.

**Q4. Maritime.** Does the org own or operate a US-flagged vessel, facility or OCS facility required to hold a security plan under 33 CFR parts 104–106? → the Coast Guard maritime cyber rule applies. **Foreign-flagged vessels are excluded** (33 CFR 101.605(b)).

**Q5. Rulemaking horizon.** The proposed cyber risk management rule would cover a named population — 73 freight railroads, 34 rail transit and passenger railroads, 115 pipeline owner/operators and incident reporting for 71 over-the-road bus operators. Register as "monitor" until final.

**Q6.** Managed security service providers and authorized representatives may perform the measures, but the owner/operator **retains sole responsibility** — do not register the duty against the vendor.

---

## 22. FDA cyber devices (FD&C Act §524B)

Context: `../../../context/regulations/us-fda-medical-device-cybersecurity.md`

**Q1. Submission test (§524B(a)).** Will the org submit a 510(k) (original, special or abbreviated), a PMA or PMA supplement, a Product Development Protocol, a De Novo, or an HDE or HDE supplement?
- No → §524B does not bite. IDE, BLA and IND submissions sit outside §524B but inside the guidance's documentation recommendations.
- Yes → Q2.

**Q2. Cyber device test (§524B(c)).** Does the device meet **all three** prongs: (1) includes software validated, installed or authorized by the sponsor as or in a device (FDA reads this to include firmware and programmable logic); (2) has the ability to connect to the internet; (3) contains technological characteristics that could be vulnerable to cybersecurity threats?
- Yes → **§524B applies** to that submission.
- No → out of scope for §524B; the premarket guidance may still apply (Q5).

**Q3. Connectivity, read broadly.** "Ability to connect to the internet" covers any means the device *can* use, intentionally or not — network, server and cloud connections, Wi-Fi, cellular, Bluetooth/BLE, magnetic inductive links, and hardware connectors such as USB, ethernet or serial ports. A device serviced briefly over USB qualifies.

**Q4. Timing and modifications.** Applies to submissions made on or after 29 March 2023; earlier authorisations are untouched until a modification requires a new submission. FDA distinguishes changes that may affect cybersecurity (authentication or encryption changes, new connectivity, changed update mechanism) from those unlikely to.

**Q5. Wider guidance.** The premarket guidance reaches every device with cybersecurity considerations, including 510(k)-exempt devices and the device constituent of combination products.

**Q6. Who is not directly regulated.** Healthcare delivery organisations, third-party servicers and refurbishers — their duties come from HIPAA (tree 19), contracts and HHS practices.

---

## 23. CIRCIA — covered entity

Context: `../../../context/regulations/us-circia.md`

**Status gate before anything else:** the implementing rule (6 CFR Part 226) is **still at final-rule stage with no final rule published as of September 2026**, and the reporting duties take effect only on the dates the final rule prescribes (§ 681b(a)(7)). Register CIRCIA as "statute in force, duties not yet triggered — reporting voluntary" and re-run this tree within days of publication.

**Q1.** Is the entity in one of the 16 PPD-21 critical infrastructure sectors — chemical; commercial facilities; communications; critical manufacturing; dams; defense industrial base; emergency services; energy; financial services; food and agriculture; government facilities; healthcare and public health; information technology; nuclear reactors, materials and waste; transportation systems; water and wastewater?
- No → **Not a covered entity.**
- Yes → Q2 and Q3, running both limbs of the NPRM proposal.

**Q2. Size limb (proposed).** Does the entity exceed the SBA small business size standard for its NAICS code (13 CFR Part 121) by employee count or annual revenue? This limb is expressly under reconsideration.

**Q3. Sector limb (proposed).** Does the entity meet any one of the sector-based criteria — regardless of which sector it self-identifies with? Examples from the proposal: DoD contractors and subcontractors subject to DFARS 252.204-7012 reporting; bulk electric or distribution entities subject to NERC CIP reporting or DOE form OE-417; emergency services to a population of at least 50,000; SLTT government entities for a jurisdiction of at least 50,000; education agencies with at least 1,000 students; hospitals with at least 100 beds and critical access hospitals; TSA-regulated pipeline, rail, aviation and transit entities; MTSA-regulated vessels and facilities; community water systems and POTWs serving more than 3,300 people.

**Q4. Exemptions.** Federal agencies already reporting under FISMA; DNS multistakeholder functions; and reports made to another federal agency under a published **CIRCIA Agreement** — none can be relied on until CISA publishes them, so do not assume SEC, HHS, banking-agency or TSA reporting discharges CIRCIA.

**Q5.** Any hit on Q2 or Q3 → **candidate covered entity**; document the analysis per legal entity and facility so it can be refreshed against the final rule.

---

## 24. CJIS Security Policy

Context: `../../../context/regulations/us-cjis-security-policy.md`

**Q1. Data test (§4.1).** Does the org access, or operate a system that processes, stores or transmits, **Criminal Justice Information** — biometric data, identity history data, biographic data, property data accompanied by PII, or case/incident history? Transaction control numbers alone (ORI, NIC, UCN) are exempt.
- No → **Not in scope.** Re-test trigger: any contract touching law-enforcement data.
- Yes → Q2.

**Q2. Role.** Criminal Justice Agency (§3.2.4) · Noncriminal Justice Agency (§3.2.5, e.g. a licensing body using criminal history record information) · **contractor or private entity** supporting either, including cloud providers.

**Q3. Contractual gate.** A contractor reaches CJI only under a specific agreement with a CJA or NCJA that incorporates the **Security Addendum** (28 CFR §20.33(a)(7)), or, for noncriminal justice functions, the Compact Council Outsourcing Standard. No addendum in place → the access itself is the finding.

**Q4. CHRI overlay (§4.1.1).** Criminal history record information carries additional access, use and dissemination controls under 28 CFR Part 20. CJI released to the public through the courts or by authorised dissemination leaves scope.

**Q5. Geographic constraint.** CJI, encrypted or not, may be stored in cloud environments only where the data sit physically within an **APB-member country** (US, US territories, Indian Tribes, Canada) and under the legal authority of an APB-member agency → a hosting-region decision, not a paperwork one.

---

## 25. IRS Publication 1075

Context: `../../../context/regulations/us-irs-pub-1075.md`

**Q1. Recipient test.** Is the org a federal, state, tribal or local agency, body, commission or other person named in 26 U.S.C. §6103(p)(4) that receives Federal Tax Information under a §6103 exception — typically state revenue, child support, human services, Medicaid/CMS or law-enforcement recipients?
- Yes → **Pub 1075 applies.**
- No → Q2.

**Q2. Contractor test.** Does the org act as a contractor, sub-contractor, consolidated data centre or state consolidated IT organisation to such an agency and touch FTI? → in scope **through the agency**, which must have safeguard requirements in effect, conduct an on-site review every 3 years (mid-point for contracts shorter than 3 years; none for contracts under 6 months) and certify compliance annually. Human services agencies receiving FTI under §6103(l)(7) may not disclose FTI to contractors at all.

**Q3. Data test.** Does the org hold or control FTI, including information it creates from FTI? An IRS-sourced address entered into agency records stays FTI unless overwritten from an independent taxpayer or third-party source.

**Q4. Secondary receipt.** FTI obtained via SSA, OCSE, the Bureau of the Fiscal Service, CMS or another IRS agent under a §6103(p)(2)(B) agreement is in scope and covered by Safeguard Reviews.

**Q5. Boundary and territory.** Every system that receives, processes, stores, accesses, protects or transmits FTI is in the assessment boundary — workstations, hypervisors, storage, cloud, firewalls, VPN, wireless, VoIP. **No offshore access, storage, processing, transmission, support or disposal.**

**Q6. Exit.** Agencies that stop receiving FTI remain in scope until destruction is certified; statutory retention periods keep the annual reporting duty alive.

---

## 26. FedRAMP

Context: `../../../context/frameworks/fedramp.md`

**Q1.** Does the org offer a **cloud computing product or service** (IaaS, PaaS or SaaS)?
- No → **Not in scope.**
- Yes → Q2.

**Q2.** Will that service create, collect, process, store or maintain **federal information on behalf of a federal agency**?
- No → **Not in scope.**
- Yes → Q3.

**Q3. Exclusion test (M-24-15).** Is the use one of the listed out-of-scope categories — a system used only for a single agency's operations and not offered as a shared service under a shared responsibility model; a social media or communications platform used under agency social media policy; a search engine; a widely available service supplying commercially available information without collecting federal information; an ancillary service whose compromise would pose negligible risk?
- Yes → out of scope for that use, subject to exceptions granted by the FedRAMP Director with OMB approval.
- No → **FedRAMP authorization required** for that use.

**Q4. Record the framing.** Scope is a **use-case determination made by the agency**, not a property of the product: the same service can be in scope for one agency use and out of scope for another, and FedRAMP publishes no list of always-out-of-scope services. Record the agency, the use and the impact level per row.

**Q5. Downstream.** A cloud service handling CUI for a DoD contractor must be FedRAMP Moderate (or higher) authorized, or meet FedRAMP Moderate–equivalent requirements — see tree 28.

---

## 27. Government contracts — clause-driven regimes (US federal pattern)

**Q1.** Any US federal contracts or subcontracts? Check clauses, not assumptions: FAR 52.204-21 (basic safeguarding of federal contract information), DFARS 252.204-7012 (covered defense information → NIST SP 800-171 compliance + 72-hour incident reporting to DoD), CMMC clauses phasing in per DoD program (tree 28), FedRAMP if selling cloud services to agencies (tree 26). Subcontractors inherit via flow-down. See `../../../context/frameworks/nist-800-53.md` and `../../../context/frameworks/nist-800-161-cscrm.md`.
**Q2.** Operating or supporting a system **on behalf of** a federal agency rather than selling to one? → FISMA reaches contractor-operated systems (`../../../context/regulations/us-fisma-federal-cyber.md`); national security systems follow separate direction.
**Q3.** Non-US public sector contracts → the buyer's national security-clause frameworks (register per contract).
Classify all of these as **contractually binding** with statutory enforcement backdrops (e.g., False Claims Act exposure for US federal misrepresentations — counsel flag).

---

## 28. CMMC — DoD contract level

Context: `../../../context/frameworks/nist-800-171-cmmc.md`

**Q1. Contractual trigger (32 CFR 170.3).** Will the org, as prime or subcontractor at any tier, process, store or transmit **Federal Contract Information or CUI on unclassified contractor systems** under a DoD solicitation or contract? Commercial-item acquisitions above the micro-purchase threshold are included; acquisitions exclusively for **commercially available off-the-shelf items are excluded** (170.3(c)).
- No → **Not in scope.**
- Yes → Q2.

**Q2. Data test.** FCI only → **Level 1 (Self)**. CUI → the level the contract dictates; Level 3 is reserved for the most critical programs and technologies. **Level selection is the government's call** (170.5(b)), not the contractor's.

**Q3. Flow-down (170.23).** A subcontractor handling only FCI needs Level 1; one handling CUI needs the level the prime's contract dictates. Register the flow-down obligation for every tier the org supplies.

**Q4. Assessment scope is asset-driven, not enterprise-wide (170.19(c)).** Sort assets into CUI Assets, Security Protection Assets, Contractor Risk Managed Assets, Specialized Assets and Out-of-Scope Assets. Specialized Assets — IoT, IIoT, OT, government-furnished equipment, Restricted Information Systems, test equipment — are out of scope entirely at Level 1.

**Q5. Cloud and external providers.** A CSP processing, storing or transmitting CUI must be FedRAMP Moderate (or higher) Authorized or meet FedRAMP Moderate–equivalent requirements per DoD policy. External Service Providers are scoped by whether they handle CUI and/or Security Protection Data.

**Q6. Waivers.** Waiver of CMMC requirements sits at Service/Component Acquisition Executive level only (170.5(d)); a DFARS 7012 variance adjudicated by the DoD CIO and carried in the SSP is scored as met. Do not assume either is available → **counsel/contracts flag.**

---

## 29. DOJ bulk data rule (28 CFR Part 202)

Context: `../../../context/regulations/us-doj-bulk-data-rule.md`

**Q1. Person test.** Is the org a **U.S. person** — a citizen, permanent resident, U.S.-organized entity including its foreign branches, or any person in the U.S.?
- No → the rule's prohibitions do not attach directly (they may reach you as a counterparty).
- Yes → Q2.

**Q2. Transaction test (§ 202.210).** Does a transaction give a country of concern or a **covered person** access to government-related data or bulk U.S. sensitive personal data through **data brokerage, a vendor agreement, an employment agreement or an investment agreement**? "Knowingly" means actual knowledge or reason to know.

**Q3. Covered person test (§ 202.211).** Foreign entities 50%-or-more owned by, organized under the laws of, or with principal place of business in a country of concern; foreign entities 50%-or-more owned by covered persons; foreign individuals who are employees or contractors of either; foreign individuals primarily resident in a country of concern; and anyone the Attorney General designates. Country-of-concern citizens located in the U.S. are U.S. persons, not covered persons, unless designated.

**Q4. Bulk thresholds (§ 202.205),** counted over the preceding 12 months per U.S.-person/foreign-person pair: human genomic data **>100** U.S. persons; other human 'omic data, biometric identifiers and precise geolocation **>1,000** persons or devices; personal health data and personal financial data **>10,000** persons; covered personal identifiers **>100,000** persons; combined data takes the lowest applicable threshold.

**Q5. Government-related data (§ 202.222)** is covered at **any volume**: precise geolocation for an area on the Government-Related Location Data List, and any sensitive personal data marketed as linked to current or recent former U.S. Government employees, contractors or former senior officials.

**Q6. Exemptions (subpart E)** include personal communications, informational materials, travel, official U.S. Government business, financial services ordinarily incident to banking and payments, intra-corporate-group administrative transactions, transactions required by federal law, CFIUS-covered investment agreements, telecommunications services other than data brokerage, and specified FDA regulatory data — but the on-demand and rejected-transaction reporting duties survive the exemption. **Counsel flag** on every exemption claim.

---

## 30. COPPA

Context: `../../../context/regulations/us-coppa.md`

**Q1. Operator test.** Does the org operate a commercial website or online service (including apps and connected toys) in interstate or foreign commerce that collects or maintains personal information from users, or on whose behalf it is collected — including where the operator **benefits by allowing another person to collect** it directly from users? Non-profits exempt from FTC Act §5 are excluded.
- No → **Not in scope.**
- Yes → Q2.

**Q2. Child-directed test (16 CFR §312.2, para. 1).** Is the service directed to children under 13 on the totality test — subject matter, visual content, animated characters, child-oriented activities and incentives, music, age of models, child celebrities, language, advertising, plus empirical evidence of audience composition and intended audience (marketing plans, representations to consumers or third parties, user reviews, ages of users on similar services)?
- Yes → **COPPA applies**; check Q4.
- No → Q3.

**Q3. Deemed and actual-knowledge limbs.** A service is **deemed** child-directed when it has actual knowledge it collects personal information directly from users of another child-directed service — this is the limb that catches ad networks, SDKs and plug-ins (para. 2). A general-audience service is covered only on **actual knowledge** that a user is under 13; the Rule does not require it to investigate ages, but knowledge acquired later, for example from a parent, triggers the Rule from that point.

**Q4. Mixed audience.** Child-directed but children are not the primary audience, and no personal information beyond the §312.5(c) exceptions is collected before a **neutral** age screen — no default age, no encouragement to falsify. Then the service is not treated as child-directed for visitors not identified as under 13.

**Q5. Reach.** Foreign-based services must comply if directed to US children or if they knowingly collect US children's personal information; US-based services collecting from foreign children are also covered.

**Q6. Teens are outside COPPA** — route them to tree 32 and the state kids codes, not here.

---

## 31. FERPA and student privacy

Context: `../../../context/regulations/us-ferpa-education-privacy.md`

**Q1. Entity test (34 CFR 99.1).** Is the org an educational agency or institution to which funds are made available under any program administered by the Secretary of Education — by grant, contract, subgrant, or because students bring Pell Grants or federal loans?
- Yes → **FERPA applies to the whole entity, every component.** SEAs are subject to Subpart B access rights where they maintain education records.
- No → Q3.

**Q2. Record test.** Does the org maintain **education records** — records directly related to a student and maintained by the agency or institution *or by a party acting for it*? Excluded: sole-possession notes, law-enforcement-unit records, employee records, and treatment records of students 18 or older or in postsecondary education.

**Q3. Vendor test.** Vendors are **not directly regulated** by FERPA: they are reached through the school-official exception (99.31(a)(1)(i)(B)), the redisclosure limits (99.33) and the 5-year debarment for third parties that violate them (99.67). Register the duty as contractual, with the debarment as the enforcement backdrop.

**Q4. PPRA.** Is the org an LEA — an elementary or secondary school, district or local board receiving ED funds? PPRA does **not** reach postsecondary institutions; rights transfer at 18 or emancipation.

**Q5. State edtech laws.** Is the org an "operator" of a site, service, application or mobile app with actual knowledge that it is used primarily for, and was designed and marketed for, K-12 school purposes (California, Illinois — cloud services included, general-audience services excluded), or a "third-party contractor" receiving student or teacher data under contract (New York)? These bind the vendor directly where FERPA does not.

**Q6.** If children under 13 are involved, run tree 30 in parallel — a school may consent as the parent's agent only for the educational context.

---

# United States — state regimes

## 32. State comprehensive privacy laws — threshold tests

Context: `../../../context/regulations/us-state-privacy.md`

Run per state where the org does business or targets residents. Two structural patterns:

**California (CCPA/CPRA).** Applies to a **for-profit** entity doing business in California that determines processing purposes/means and meets **any one** of:
1. annual gross revenues above the inflation-adjusted threshold (originally USD 25 million — check the current adjusted figure);
2. buys, sells, or shares personal information of **100,000+** California consumers or households; or
3. derives **50%+** of annual revenue from selling or sharing California personal information.
Note: CCPA covers employee and B2B contact data — a B2B-only business is not exempt. "Doing business in California" is broad. Data broker registration (Delete Act) is a separate test.

**Virginia-pattern states (VA, CO, CT, and most others).** Applies to entities doing business in the state or targeting its residents that, in a year:
1. control/process personal data of **100,000+** residents (some states exclude payment-transaction-only processing from the count), or
2. control/process personal data of **25,000+** residents **and** derive a specified share (commonly 25–50%) of gross revenue from the **sale** of personal data.
Several states diverge from the pattern: **Texas** ties applicability to not being an SBA small business (with a sale carve-in) rather than record counts; **Nebraska** follows Texas; some states have lower counts for small populations. Most exclude nonprofits (California does too, with narrow exceptions), and most exempt GLBA/HIPAA-regulated entities or data at entity or data level — **check whether the exemption is entity-level or data-level per state**, it changes scope materially.

**Always-on rows regardless of thresholds:** state **breach notification** laws (`../../../context/regulations/us-state-breach-notification-laws.md` — no size thresholds; applicability follows the residence of the individual, not the location of the company or the data), state data-broker registration laws, and sectoral state laws (WA My Health My Data; biometric statutes — tree 33; state AI statutes — tree 34).

---

## 33. State biometric privacy laws

Context: `../../../context/regulations/us-biometric-privacy-laws.md`

**Q1. Illinois BIPA (740 ILCS 14).** Is the org a **private entity** (not a state or local agency or an Illinois court) that possesses, collects, captures, purchases or receives through trade an Illinois person's retina or iris scan, fingerprint, voiceprint, or scan of hand or face geometry? There is **no commercial-purpose limiter and no volume threshold**, and employee data is squarely in scope — timekeeping and access-control systems are the largest case category. Exclusions: GLBA Title V financial institutions and affiliates (§25(c)), and contractors working for state or local government (§25(e)). Photographs, writing samples, physical descriptions, biological samples for testing, and data captured in a health-care setting or for HIPAA treatment, payment or operations are outside the definition.
- Yes → **BIPA applies** — and it carries a private right of action, so treat this as a litigation-exposure row, not a paperwork one.

**Q2. Texas CUBI (§503.001).** Does any "person" capture a retina or iris scan, fingerprint, voiceprint or record of hand or face geometry **for a commercial purpose**? Voiceprints retained by GLBA financial institutions are excluded; since 1 January 2026 biometric identifiers used to develop, train or offer AI models are excluded unless the system uniquely identifies a person, as is AI used for security, fraud or incident purposes.

**Q3. Washington (RCW 19.375).** Does a non-government person **enrol** a biometric identifier — capture it, convert it to a non-reconstructible template and store it in a matching database — for a "commercial purpose", defined narrowly as sale or disclosure to third parties for marketing unrelated goods? Security and law-enforcement purposes are not commercial, so workforce systems often fall outside.

**Q4. Colorado (C.R.S. §6-1-1314).** Does a controller doing business in Colorado or targeting its residents process **any amount** of biometric identifiers, including an employee's? The CPA's 100,000/25,000-consumer thresholds do **not** apply to the biometric duties, so a controller below the general thresholds still complies for its biometric data.

**Q5. Portland City Code ch. 34.10.** Does a private entity use face recognition in a **place of public accommodation in Portland**? Exceptions: compliance with law, user verification to access one's own devices, automatic face detection in social-media apps.

- No hit → **Not in scope**; re-test on any new biometric enrolment, including workforce timekeeping.

---

## 34. State AI laws

Context: `../../../context/regulations/us-state-ai-laws.md`

**Q1. Colorado ADMT Act (SB 26-189, effective 1 January 2027).** Does the org **develop** covered ADMT — technology processing personal data to generate predictions, recommendations or scores used to *materially influence* a consequential decision — marketed or contracted for that use, or **deploy** it in a consequential decision affecting a Colorado consumer, employee or job applicant? Excluded: anti-malware, anti-virus and similar listed technologies; incidental, trivial or clerical uses; insurers under C.R.S. 10-3-1104.9; routine academic administration.

**Q2. Texas TRAIGA (in force since 1 January 2026).** Does the org promote, advertise or conduct business in Texas, produce a product or service used by Texas residents, or develop or deploy an AI system in Texas (§551.002)? "Consumer" means a Texas resident acting in an individual or household context, not employment or commercial. Insurance entities under unfair-discrimination law and federally insured financial institutions complying with banking law are excluded (§552.056).

**Q3. California CPPA ADMT regulations (effective 1 January 2026, ADMT compliance by 1 January 2027).** Is the org a CCPA "business" using technology that replaces or substantially replaces human decision-making for a **significant decision** — financial or lending services, housing, education, employment or independent-contracting opportunities or compensation, or health care (§7001(ddd))?

**Q4. California SB 53.** Has the org trained a model using more than **10^26** integer or floating-point operations (*frontier developer*), and do its affiliates' annual gross revenues exceed **USD 500,000,000** (*large frontier developer*)? Smaller frontier developers owe only transparency and incident reports.

**Q5. California AB 2013.** Does the org develop a generative AI system or service, or a substantial modification of one, released on or after 1 January 2022 and made available to Californians? Systems whose sole purpose is security and integrity are excluded.

**Q6. Employment-specific rows.** NYC Local Law 144 — employer or employment agency using an automated employment decision tool to substantially assist or replace discretionary decisions for NYC candidates or employees. Illinois P.A. 103-0804 — employer using AI in recruitment, hiring, promotion, discipline, discharge or other terms of employment. Utah ch. 72 / ch. 75 — generative AI in consumer transactions and in Department of Commerce–licensed regulated occupations, with a disclosure safe harbour; ch. 72 sunsets 1 July 2027 unless extended.

- Any hit → register per law **and** per system, and hand system-level classification to `../../ai-governance/SKILL.md`. Where the EU AI Act also applies, keep the rows separate — the role vocabulary differs.

---

# Asia-Pacific

## 35. Australia — SOCI Act and Cyber Security Act

Context: `../../../context/regulations/australia-soci-cyber-security-act.md`

**Q1. SOCI asset test (ss. 8D, 9).** Does the org own or operate, or hold a direct interest in, an asset falling in one of the 22 statutory asset classes across the 11 sectors — communications; data storage or processing; financial services and markets; water and sewerage; energy; health care and medical; higher education and research; food and grocery; transport; space technology; defence industry? Each class has its own quantitative definition in Part 1, Division 2 — **verify the threshold for your class**. Commonwealth-owned assets are excluded unless declared (s 9(2A)).
- No → Q4.
- Yes → Q2.

**Q2. Which obligations switch on** depends on the rules, not the Act: the Application Rules list the classes subject to the Part 2 register and Part 2B incident reporting; the CIRMP Rules list 13 classes subject to Part 2A risk-management programmes; telecommunications assets sit under the separate TSRMP Rules. Banking, superannuation and insurance assets carry register and Part 2B duties but **no CIRMP obligation** — they sit under APRA prudential standards (tree 36). Part 2C applies only to assets declared Systems of National Significance under s 52B.

**Q3. Data storage overlay (s 9(7)).** A data storage system holding **business critical data** is part of the critical infrastructure asset. Business critical data includes personal information on at least **20,000 individuals**, R&D information, and information about or needed to operate the asset (s 5) — this is the limb that pulls cloud and managed-service providers in, and the responsible entity must tell the provider it holds such data (s 12F(3)).

**Q4. Cyber Security Act, Part 2 (smart devices).** Does the org manufacture or supply **relevant connectable products** (internet- or network-connectable, s 13) new on or after commencement? The standard applies to consumer-grade products, excluding desktops, laptops, tablets, smartphones, therapeutic goods, and road vehicles and their components.

**Q5. Cyber Security Act, Part 3 (ransomware payment reporting).** Is the org a business carried on in Australia (not a Commonwealth or State body) with previous-financial-year turnover above **A$3 million** (pro-rated for part-year businesses), or a responsible entity for a Part 2B SOCI asset regardless of turnover (s 26(2))? → the ransomware payment reporting duty applies.

- No hit anywhere → **Not in scope**; the Privacy Act row still stands (`../../../context/regulations/australia-privacy-act.md`, small business operators at or below A$3,000,000 turnover exempt under s 6D, with health service providers and information traders losing the exemption regardless).

---

## 36. Australia — APRA CPS 234 and CPS 230

Context: `../../../context/regulations/australia-apra-cps-234-230.md`

**Q1.** Is the entity in one of the five APRA-regulated classes — ADIs (including foreign ADIs and authorised banking NOHCs); general insurers (including Category C insurers, insurance NOHCs and Level 2 insurance group parents); life companies (including friendly societies, EFLICs and registered life NOHCs); private health insurers; or RSE licensees?
- Yes → **both CPS 234 and CPS 230 apply.** CPS 234 has been in force since 1 July 2019; CPS 230 commenced 1 July 2025, with the amended CPS 230 and CPG 230 from 1 July 2026.
- No → Q3.

**Q2. Foreign branches and groups.** For foreign ADIs, Category C insurers and EFLICs, both standards apply to **Australian branch operations only**, with "Board" read as the senior officer outside Australia (para 3). A **Head of a group** must apply the standards throughout the group, including to entities that are not themselves APRA-regulated (para 4) — so an unregulated subsidiary can be in scope through its parent.

**Q3. Non-APRA financial firms.** AFS licensees that are not ADIs, insurers or trustees, and payment providers not yet APRA-licensed, are outside both standards **unless inside a regulated group** — check Q2 before concluding.

**Q4. Third parties.** CPS 234 extends assessment, control-design evaluation, testing, internal audit and notification duties to information assets managed by related parties and third parties; CPS 230 applies to all service providers with heightened duties for **material** service providers and arrangements, and reaches fourth parties. A vendor does not become an obligor, but inherits the duties by contract — register as flow-down.

**Q5. Adjustments.** APRA may adjust or exclude a specific requirement for an entity (CPS 234 para 11, CPS 230 para 10), and CPS 230 paras 57–58 exempt some non-traditional service provider arrangements. Proportionality is expressed as "size, business mix and complexity", with stronger expectations of significant financial institutions → **document the adjustment, do not assume it.**

---

## 37. China — CSL, DSL and PIPL

Context: `../../../context/regulations/china-pipl-dsl-csl.md`

**Q1. CSL network operator.** Does the org own or manage a network, or provide network services, in mainland China? Any company running IT systems in mainland China qualifies → **CSL applies**, including MLPS grading.

**Q2. CIIO.** Does the org operate important network facilities or systems in public communications and information services, energy, transport, water, finance, public services, e-government or defence science and industry — or any system whose destruction could seriously endanger national security, the economy, people's livelihood or the public interest? Sector "protection work departments" identify CII and **notify** the operator (CII Regs Arts. 8–10): until notified, register CII status as a **risk, not a fact**.

**Q3. DSL.** Does the org carry out data handling activities in mainland China (Art. 2)? "Data" is any record of information in electronic or other form. Extraterritorial reach attaches to handling outside China that harms national security, public interest or citizens' rights.

**Q4. PIPL.** Does the org handle personal information **in** China (Art. 3(1)), or, from outside China, handle PI of individuals in China to provide them products or services or to analyse or assess their behaviour (Art. 3(2))? Extraterritorial handlers must establish a dedicated entity or appoint a representative in China and report it to the regulator (Art. 53).

**Q5. Volume tiers.** Under 100,000 individuals → "small processor" simplified regime from 1 September 2026. Over 1 million → designate a PI protection officer responsible for audits. Over 10 million → audit at least every two years, and the important-data-processor duties of the Network Data Regulations attach. Large network platforms — at least 50 million registered users, or at least 10 million monthly active users with complex business — carry the additional PIPL Art. 58 duties.

**Q6. Important data.** A handler need not treat data as "important" for export purposes unless notified or the category is published in a sector or regional catalogue → record as an open fact, not an assumption.

---

## 38. India — DPDP Act and CERT-In Directions

Context: `../../../context/regulations/india-dpdp-cert-in.md`

**Q1. DPDP Act (s.3).** Does the org process digital personal data **in India** (collected digitally, or non-digital and later digitised), or process personal data **outside India** in connection with any activity related to offering goods or services to Data Principals in India?
- Yes → **DPDP applies**; record the role — Data Fiduciary (decides purpose and means) or Data Processor (engaged only under a valid contract, s.8(2), with the fiduciary staying responsible for processor conduct).
- No → Q3.

**Q2. Exclusions.** Personal or domestic processing; personal data made publicly available by the individual or under a legal obligation (s.3(c)); and the **outsourcing carve-out** in s.17(1)(d) — an Indian entity processing non-Indian individuals' data under contract with a person outside India — though s.8(1) accountability and s.8(5) security still apply.

**Q3. Significant Data Fiduciary (s.10).** Has the Central Government notified the org as an SDF on volume and sensitivity of data, risk to individuals, sovereignty, electoral democracy, security of State or public order? Obligations apply **from notification**, so this is a status to confirm, not to self-assess.

**Q4. CERT-In Directions.** Is the org a service provider, intermediary, data centre, body corporate or government organisation — or a data centre, VPS, cloud or VPN provider (direction v), or a virtual-asset provider (direction vi)? Foreign firms serving Indian users are covered for incident reporting and must name a point of contact. Individual citizens are outside; enterprise and corporate VPNs are outside the VPN-registration duty.

**Q5. Sectoral overlays.** RBI Master Direction 2023 (commercial banks, small finance and payments banks, NBFCs in the Top/Upper/Middle layers, credit information companies, AIFIs — Local Area Banks and NBFC-CICs excluded, foreign bank branches comply-or-explain); SEBI CSCRF (all SEBI-regulated entities in five graded categories set each financial year on prior-year thresholds, with listed exclusions); IRDAI Guidelines 2026 (all insurers including foreign reinsurance branches, intermediaries and the IIB). Register each separately from the DPDP row.

---

## 39. Japan — APPI and the cyber regimes

Context: `../../../context/regulations/japan-appi-cyber.md`

**Q1. APPI Chapter IV.** Does the org use a "personal information database or the equivalent" — a searchable, systematically organised collection of personal information (Art. 16(1)) — **for business** (Art. 16(2))?
- Yes → **APPI applies.** There is **no headcount, record-count or revenue threshold.** National and local government organs and incorporated administrative agencies fall under Chapter V instead.
- No → Q3.

**Q2. Extraterritorial reach (Art. 171).** Does a foreign operator handle personal information of a person in Japan in connection with supplying goods or services to that person? → in scope, and subject to the same PPC powers as a domestic operator.

**Q3. Carve-outs.** Art. 57 excludes journalistic, literary, religious and political uses **for those purposes**; Art. 59 requires academic research organisations to endeavour to comply and to self-regulate research handling.

**Q4. Data-category check.** Most handling duties attach to **personal data** — personal information held in a database (Art. 16(3)) — not to loose personal information. Identify special care-required information (Art. 2(3)), individual identification codes including biometrics (Art. 2(2)), and personal-related information such as cookies and device data that is not personal information for the holder (Art. 2(7)).

**Q5. Critical-infrastructure overlay.** Is the org a **special critical-infrastructure operator** — already designated as a specified critical-infrastructure operator under Art. 50 of the Economic Security Promotion Act **and** using "specified important computers" as defined by Cabinet Order No. 47 of 2026 and the joint ministerial ordinance? Both limbs are needed.

**Q6. Sectoral and voluntary layers.** FSA Guidelines (October 2024) apply supervisory expectations to the listed financial populations; the Basic Act on Cybersecurity imposes only a duty to endeavour on private companies; METI Guidelines v3.0 are voluntary but widely used in procurement. Register these as guidance, not obligation, unless a supervisor has applied them to the org.

---

## 40. South Korea — PIPA

Context: `../../../context/regulations/south-korea-pipa.md`

**Q1. Controller test.** Does the org operate personal information files as a personal information controller — public or private, **of any size**?
- Yes → **PIPA applies.** Micro-enterprises are exempt only from the duty to *designate* a CPO, in which case the owner or representative is the CPO by law (Art. 31(1)–(2)).
- No → out of scope, but note the Act has **no territorial limiter**, so a foreign controller processing Koreans' data is in scope.

**Q2. Data test.** Personal information is information on a living individual identifiable directly or when easily combined with other information. **Pseudonymized information is personal information**; fully anonymized information is outside the Act (Art. 58-2).

**Q3. Domestic agent (Art. 31-2).** Does the org lack an address or place of business in Korea **and** meet any of: previous-year total sales of at least **KRW 1 trillion**; at least **1 million** domestic data subjects on average over the preceding three months; or a PIPC resolution? → a written domestic agent must be designated, and from the 2025 amendment a Korean subsidiary or controlled affiliate must be chosen where one exists.

**Q4. Outsourcees (Art. 26).** Entrustment must be documented in writing with purpose limits and safeguards; the entruster must disclose, train and supervise; re-entrustment needs consent. The outsourcee is deemed the controller's employee for damages and is **directly bound** by the listed articles — register the processor row, not just the controller row.

**Q5. Financial carve-out.** Personal **credit** information is governed by the Credit Information Act under FSC supervision, and the EU adequacy decision expressly excludes FSC-supervised credit-information processing → **counsel flag** for financial-sector data flows.

**Q6. Partial exemptions (Art. 58)** disapply Arts. 15–57 for listed categories while keeping the Art. 3 principles, Art. 4 rights and the Art. 58(4) minimum duties.

---

## 41. Singapore — PDPA and Cybersecurity Act

Context: `../../../context/regulations/singapore-pdpa-cybersecurity.md`

**Q1. PDPA (ss. 2, 4).** Does the org collect, use or disclose personal data in Singapore? Any "organisation" is caught, "whether or not formed or recognised under the law of Singapore" or resident there — **extraterritorial by design**. Excluded: individuals acting in a personal or domestic capacity, employees acting in the course of employment, public agencies, business contact information, and records over 100 years old.
- Yes → **PDPA applies.** If the org acts as a **data intermediary** under a written contract, it is bound only by protection, retention, breach-notification-to-the-controller and the s. 26E duties; the controlling organisation remains liable as if it processed the data itself.

**Q2. Cybersecurity Act — CII (s. 7).** Has the Commissioner designated a computer or computer system the org owns as **critical information infrastructure** — necessary for the continuous delivery of an essential service, with loss or compromise having a debilitating effect on that service in Singapore, located wholly or partly in Singapore (s. 7(1A) extends to systems located wholly outside Singapore that would otherwise qualify)? Essential services are listed in the First Schedule; designation lasts 5 years.
- Designated → in scope. Not designated → register as designation risk.

**Q3. Third-party-owned CII (Part 3A).** Is the org an **essential-service provider** designated as responsible for a CII it depends on but does not own? → it must obtain a legally binding commitment from the owner, report on the prescribed cycle and notify material changes to that commitment.

**Q4. STCC (Part 3B).** Has a system been temporarily designated as a system of temporary cybersecurity concern because of an event or situation?

**Q5. Not-yet-commenced limbs.** Parts 3C (entities of special cybersecurity interest) and 3D (major foundational digital infrastructure providers such as cloud and data-centre operators) were enacted in 2024 but are **absent from the in-force consolidation as at September 2026** → register as "monitor", not "applies".

**Q6. Cloud note.** "Computer" and "computer system" include virtual computers, and a virtual system is in Singapore if any physical resource simulating it is located there — cloud-hosted CII is squarely within scope.

**Q7. MAS.** MAS-regulated financial institutions carry the FSM-series Notices by licence category in addition to the above.

---

## 42. Hong Kong — PDPO and PCICSO

Context: `../../../context/regulations/hong-kong-pdpo-critical-infrastructure.md`

**Q1. PDPO.** Is the org a **data user** — controlling, alone or jointly, the collection, holding, processing or use of personal data? Public and private sectors alike are covered.
- Yes → **PDPO applies.** A **data processor is not directly regulated**: DPP2 and DPP4(2) put the duty on the data user to bind processors by contractual or other means. Part 8 exemptions are case-by-case defences, not standing carve-outs. Section 33 (cross-border transfer restriction) is **not in operation** — the PCPD's model contractual clauses are best practice, not law.

**Q2. PCICSO — operator designation (s.12).** Has the Commissioner designated the org in writing as a **critical infrastructure operator**? The list of operators is **not published**, so the only reliable answer is the notice itself.
- Not designated → **out of scope of PCICSO**; register as designation risk if the org runs infrastructure essential to a Schedule 1 sector (energy; information technology; banking and financial services; air, land and maritime transport; healthcare services; telecommunications and broadcasting services), or other infrastructure whose damage may substantially affect critical societal or economic activities.
- Designated → Q3.

**Q3. Critical computer systems (s.13).** Which systems has the Commissioner designated as CCSs? Only designated CCSs carry the obligations. A CCS may sit **outside the operator's control** if it is accessible in or from Hong Kong and essential to the core function (s.22(2)(c)); whether a system is isolated from the internet is irrelevant.

**Q4. Which regulator.** The Commissioner regulates incident reporting and response for every sector; the Monetary Authority regulates organisational and preventive obligations for authorized institutions, SVF licensees and designated-system operators, and the Communications Authority for its licensees.

**Q5. Suppliers.** Not regulated directly — "CI operators can outsource their work, but not their responsibilities". Register supplier duties as contractual flow-down.

---

# Americas beyond the United States

## 43. Canada — PIPEDA, Quebec Law 25 and provincial laws

Context: `../../../context/regulations/canada-pipeda-law-25.md`

**Q1. PIPEDA Part 1 (s. 4).** Does the org collect, use or disclose personal information **in the course of commercial activities**, or handle employee/applicant information of a **federal work, undertaking or business**?
- Yes → **PIPEDA applies**, subject to Q2.
- No → Q2 anyway; provincial laws have their own tests.

**Q2. Substantially similar provincial laws.** Intra-provincial activity in **Quebec, Alberta and British Columbia** is carved out of PIPEDA by exemption order (s. 26(2)(b)) and governed instead by:
- **Quebec P-39.1 (s. 1)** — any person collecting, holding, using or communicating personal information in the course of carrying on an enterprise, whatever the medium. The Act states **no establishment or residency test**; its reach to enterprises outside Quebec handling Quebec residents' data is a matter of interpretation and CAI practice → **counsel flag, verify case by case.**
- **Alberta PIPA (ss. 4, 56)** — organizations in Alberta; non-profits only for their commercial activities.
- **BC PIPA (s. 3)** — every organization in BC for personal information in its custody or control.

**Q3. Exclusions.** Government institutions under the Privacy Act; individuals acting for personal or domestic purposes; journalistic, artistic or literary purposes; and the listed provincial exclusions.

**Q4. CCSPA (ss. 2, 6–7, Schedules 1–2).** Is the org a **designated operator** — a member of a class the Governor in Council has established by order for a Schedule 1 vital service or system (telecommunications; interprovincial or international pipelines and power lines; nuclear energy; federally regulated transportation; banking; clearing and settlement)?
- **Schedule 2 was enacted empty**: nothing is in scope until the Governor in Council fills it and Part 2 is brought into force. Register as "monitor".

**Q5. OSFI.** Federally regulated financial institutions — banks, foreign bank branches, foreign insurance branches, life and fraternal insurers, P&C insurers, trust and loan companies — carry OSFI B-13 and the incident advisory. Provincially regulated credit unions and insurers fall under provincial supervisors instead.

---

## 44. Brazil — LGPD

Context: `../../../context/regulations/brazil-lgpd.md`

**Q1. Territorial limb (Art. 3(I)).** Is a processing operation carried out in the national territory? → **LGPD applies.**
**Q2. Targeting limb (Art. 3(II)).** Is the purpose of processing to offer or supply goods or services to, or to process data of, individuals **located in Brazil**? → applies.
**Q3. Collection limb (Art. 3(III)).** Were the personal data **collected in Brazil** — that is, was the data subject in Brazil at the moment of collection (§1)? → applies. The medium, the country where the agent is headquartered and the location of the data are all irrelevant.
- No limb met → **Not in scope.**

**Q4. Exclusions (Art. 4).** Processing by a natural person for exclusively private, non-economic purposes; exclusively journalistic, artistic or academic purposes (Arts. 7 and 11 still apply to academic processing); public security, national defence, State security and criminal investigation; and data originating abroad that are not shared with Brazilian agents or onward-transferred, provided the country of origin offers adequate protection — a limb the transfer regulation narrows to pure transit and to return of data to an ANPD-recognised adequate country.

**Q5. Role.** *Controller* decides; *operator* processes on the controller's behalf; an *encarregado* (DPO) is the communication channel with data subjects and the ANPD. Anonymised data fall outside the law unless reversible by reasonable means (Art. 12).

**Q6. Small processing agents.** Micro and small enterprises, startups, non-profits, natural persons and unincorporated private entities get a lighter regime — simplified records, no mandatory DPO but a required contact channel, a simplified security policy and doubled response deadlines. The regime is **lost** on high-risk processing (one general criterion plus one specific criterion), on exceeding the applicable revenue ceilings, or where the agent belongs to a group that does.

---

# Europe beyond the EU, Middle East and Africa

## 45. Switzerland — FADP and the ISA reporting duty

Context: `../../../context/regulations/switzerland-fadp-isa.md`

**Q1. FADP material scope (Art. 2).** Does the org process personal data of **natural persons** as a private person or federal body? Data of **legal entities is outside the Act**. Purely personal use is excluded.

**Q2. FADP territorial scope (Art. 3).** Does the processing have an **effect in Switzerland**, even if initiated abroad? → in scope.

**Q3. Swiss representative (Art. 14).** A foreign private controller must appoint a representative in Switzerland only where **all four** conditions hold: the processing relates to offering goods or services to, or monitoring the behaviour of, persons in Switzerland; it is **large scale**; it is **regular**; and it poses a **high risk** to data subjects. Fewer than four → no representative duty.

**Q4. ISA reporting obligation (Art. 74b).** Is the org in one of the 21 categories — including universities; authorities; security, rescue, drinking-water, wastewater and waste organisations; energy supply, trading, metering and control; institutions under the Banking Act, Insurance Supervision Act or Financial Market Infrastructure Act; hospitals on cantonal hospital lists; licensed medical laboratories; pharmaceutical manufacturers and importers; social and health insurers; registered postal providers; rail and concessioned public transport; civil aviation and national airports; suppliers of essential daily goods; registered telecoms providers; domain registries and registrars; **Swiss-domiciled cloud, search-engine, digital security/trust-service and data-centre providers**; and **manufacturers of hardware or software used by critical infrastructures** where the product has remote-maintenance access or is used for OT control or monitoring or for public safety?
- Yes → Q5. Mixed-activity entities report only attacks affecting the critical activity (Art. 74b(2)).

**Q5. CSO exemptions (Art. 12).** Among others: universities with fewer than 2,000 students; electricity operators not required to meet protection level A or B; gas pipeline operators below 400 GWh/year on a five-year average; transport operators without system tasks or jointly ordered services; cloud, search, trust-service and data-centre providers that do not serve third parties for remuneration; and laboratories, pharmaceutical companies, postal providers and essential-goods suppliers employing **fewer than 50 persons** in the affected area with turnover or balance sheet **not exceeding CHF 10 million**.

**Q6.** Uncertain? BACS confirms on request whether an entity is subject and issues a ruling (Art. 74a(2)) — prefer the ruling to an assumption.

---

## 46. Saudi Arabia — PDPL and NCA controls

Context: `../../../context/regulations/saudi-arabia-pdpl-nca.md`

**Q1. PDPL (Art. 2).** Does the org process personal data of individuals **in the Kingdom** by any means, or process **Kingdom residents' data from abroad**? Data of the deceased is covered where identifiable. Purely personal or family use is excluded — publishing to the public is not family use.
- Yes → **PDPL applies.** Note that for entities obliged to follow NCA controls, those controls are the PDPL security baseline (Implementing Regulations Art. 23(b)).

**Q2. NCA ECC-2:2024.** Is the org a government agency or an affiliated company, inside or outside the Kingdom, or a **private-sector entity owning, operating or hosting Critical National Infrastructure**? → ECC-2 applies; other entities are "strongly encouraged".

**Q3. Cloud (CCC-2:2024).** Is the org a cloud service provider serving in-scope tenants, or a cloud service tenant that is a government agency or CNI private entity? CSPs serving only individuals or non-CNI private entities are outside scope.

**Q4. NCNICC-1:2025 (non-CNI private entities).** Category A (large): more than **250** full-time employees **or** more than **SAR 200m** annual revenue. Category B (SMEs): **6–249** full-time employees **or** **SAR 3m–200m** annual revenue. Each category's controls bind only entities the **NCA circulates them to** — record circulation as the trigger, not the size test alone.

**Q5. Other NCA families.** DCC-1:2022 (same government plus CNI population, all data); CSCC-1:2019 (systems the organisation deems critical under NCA criteria); OTCC-1:2022 (industrial control systems in critical facilities owned or operated by government or CNI private organisations, in the Kingdom or abroad).

**Q6. Sectoral.** SAMA CSF for banks, insurance and reinsurance companies, financing companies, credit bureaus, financial market infrastructure, payment systems and PSPs; CST CRF for organisations licensed or registered by CST in the ICT sector.

---

## 47. United Arab Emirates — federal PDPL, DIFC and ADGM

Context: `../../../context/regulations/uae-data-protection-cyber.md`

**Q1. Free-zone gate first.** Is the entity incorporated or established in the **DIFC** or **ADGM**?
- DIFC → DIFC Data Protection Law applies to controllers and processors incorporated in the DIFC wherever processing occurs, to any entity processing personal data in the DIFC as part of stable arrangements, and — since the 2025 amendment — to any entity, wherever incorporated, offering goods or services to or monitoring the behaviour of data subjects in the DIFC.
- ADGM → ADGM DPR 2021 applies to processing in the context of the activities of an establishment in ADGM, wherever processing occurs; processors for non-ADGM controllers comply "to the extent possible".
- Neither → Q2.

**Q2. Federal PDPL (Art. 2).** Does the org process data of a data subject who resides or has a place of business **in the UAE**; act as a controller or processor **in the UAE** processing data of subjects inside or outside the UAE; or act as a controller or processor **outside the UAE** processing data of subjects inside the UAE?
- Yes → PDPL applies, subject to Q3.

**Q3. PDPL exclusions.** Government data and government authorities; data held by security and judicial authorities; purely personal processing; **health data** subject to its own legislation; **banking and credit data** subject to its own legislation; and free-zone companies with their own data-protection law. Art. 3 also lets the Office exempt establishments that do not process "a large amount" of data — thresholds await the Executive Regulations, so record this as an **open fact**.

**Q4. Sectoral overlays.** Health ICT Law 2/2019 covers all ICT use in health fields, onshore and in the free zones. CBUAE C 1/2026 covers all Licensed Financial Institutions that are juridical persons, not banks only. Cybercrime Decree-Law 34/2021 applies to any person, with aggravated penalties for attacks on government entities and critical facilities.

**Q5. Critical information infrastructure.** Is the org a federal government entity, or a non-government operator **designated** as CII? Designation is communicated by the sector regulator or the CSC — **confirm status rather than assume**. Dubai government entities, their contractors and consultants additionally carry the DESC ISR.

---

## 48. Israel — Privacy Protection Law

Context: `../../../context/regulations/israel-privacy-protection-law.md`

**Q1. Database test (s. 3).** Does the org hold a **collection of personal data processed by digital means**? Excluded: collections for personal, non-business use, and name/address/contact-only lists of **100,000 people or fewer** that reveal nothing further, provided the owner (or a controlled company) holds no other collection about the same people.
- No → **Not in scope.**
- Yes → Q2.

**Q2. Role.** *Controller* — determines, alone or jointly, the purposes of processing, or is statutorily authorised to process. *Holder* — an external party processing on the controller's behalf; Data Security Regulations reg. 19 extends the controller's security duties to the holder and to the database manager.

**Q3. Registration (s. 8A(a)).** Registration with the PPA is required only for (a) databases whose primary purpose is collecting personal data for supply to others as a business or for consideration, including direct-mail services, holding data on **more than 10,000 people**, and (b) databases controlled by a public body under s. 23 paragraph (1), unless they hold only employee data.

**Q4. Notification (s. 8A(b)).** A non-registrable database holding **data of special sensitivity on more than 100,000 people** must be notified to the PPA within 30 days of crossing the threshold.

**Q5. DPO (ss. 17B1–17B3).** Mandatory for public-body controllers and holders (except security bodies); data brokers with more than 10,000 people; controllers or holders whose core activities require regular and systematic monitoring at significant scale; and those whose core activity involves processing special-sensitivity data at significant scale.

**Q6. Security level.** Classify each database as individual-managed, basic, medium or high using the Schedules' data-type, headcount (100,000) and authorised-user (100) thresholds — the level drives every other security obligation.

**Q7. Territorial reach.** The PPL has **no GDPR-style territorial-scope article**: application to foreign controllers turns on the location of the database, the processing and the affected individuals, and on general conflict-of-laws principles → **counsel flag, verify case by case.** Sectoral overlays (Bank of Israel directives, Capital Market Authority circulars, INCD methodologies) run in parallel and are not displaced.

---

## 49. South Africa — POPIA

Context: `../../../context/regulations/south-africa-popia.md`

**Q1. Material scope (s.3(1)(a)).** Is personal information entered in a record by automated means, or by non-automated means where it forms (or is intended to form) part of a filing system?

**Q2. Territorial scope (s.3(1)(b)).** Is the **responsible party domiciled in the Republic**, or not domiciled but **using means in the Republic** — unless those means are used only to forward information through the Republic?
- Yes to Q1 and Q2 → **POPIA applies.** Note personal information covers an identifiable, existing **juristic person** as well as a natural person, so B2B data is in scope.
- No → **Not in scope.**

**Q3. Role.** *Responsible party* determines purpose and means; *operator* processes for a responsible party under contract or mandate without coming under its direct authority — and operators carry **direct duties** under ss.20–21, so register the processor row separately.

**Q4. Exclusions (ss.6–7).** Purely personal or household activity; information de-identified so it cannot be re-identified; certain national-security, law-enforcement and prosecution processing by public bodies with adequate safeguards; Cabinet and provincial executive councils; judicial functions of courts; journalistic, literary or artistic expression subject to a code-of-ethics carve-out. Section 37 allows the Regulator to grant a Gazetted exemption on application.

**Q5. Cybercrimes Act s.54.** The reporting duty reaches only **electronic communications service providers** licensed or exempted under the Electronic Communications Act 2005, including operators of exempt private networks, and **financial institutions** as defined in the Financial Sector Regulation Act 2017.

**Q6. Joint Standard 2 of 2024.** Applies to financial institutions as defined in the standard, with group-wide coverage obligations for banks and insurers and proportionality by nature, size, complexity and risk profile.

---

# Cross-sector and product regimes

## 50. PCI DSS — contractual scope test

Context: `../../../context/frameworks/pci-dss-4.md`

**Q1.** Does the org **store, process, or transmit cardholder data**, or can it **impact the security of cardholder data or the cardholder data environment** (e.g., hosting the payment page, managing systems that could affect the payment flow)?
- Yes → **PCI DSS applies contractually** (via acquirer/merchant agreement or as a service provider to such parties). Determine merchant vs service provider role, transaction-volume level, and eligible validation route (SAQ type vs on-site assessment/ROC).
- No, payments fully outsourced with no CHD contact and no impact on its security → validate the SAQ A-style eligibility claim with the acquirer; register as "not applicable — outsourced, confirmed [date]."

**Q2.** Does the org build, sell or operate payment software, PIN entry devices, point-of-interaction terminals, HSMs or 3-D Secure components? → the adjacent PCI SSC standards apply on their own terms; see `../../../context/frameworks/pci-other-standards.md`.

---

## 51. UN R155 / R156 — vehicle type approval

Context: `../../../context/regulations/automotive-un-r155-iso-21434.md`

**Q1. Contracting-party test.** Does the org seek vehicle type approval in a Contracting Party to the 1958 Agreement that applies R155/R156 — the EU and the UK do; Japan and South Korea are commonly listed with their own phase-in dates (verify against the UNECE status document)? The **United States has no equivalent type-approval requirement**.
- No → **Not in scope** through this route; contractual and customer requirements may still apply.
- Yes → Q2.

**Q2. R155 scope (para. 1.1).** Is the vehicle in categories **L, M, N or O fitted with at least one electronic control unit**? → a certified **CSMS** and vehicle-type cybersecurity approval are required.

**Q3. R156 scope (para. 1.1).** Is the vehicle in categories **M, N, O, R, S or T and does it permit software updates**? → a **SUMS** is required. Categories R, S and T are in R156 but not R155, so a towed-machinery programme can need a SUMS without needing a CSMS certificate.

**Q4. Transitional relief (R155 para. 7.3.1).** For type approvals of M, N and O vehicles first issued **before 1 July 2024**, and of L-category vehicles **before 1 July 2029**, and for each extension of those approvals, a manufacturer that can demonstrate the type could not be developed in compliance with the CSMS may instead demonstrate that cybersecurity was adequately considered during development. The same dates gate the "technically not feasible" carve-out for the Annex 5 Part B/C mitigations.

**Q5. Suppliers.** Not directly approved. R155 para. 7.2.2.5 makes the manufacturer demonstrate how its CSMS manages dependencies on contracted suppliers, service providers and sub-organisations → register supplier duties as **contractual flow-down**, usually via ISO/SAE 21434 distributed cybersecurity activities.

**Q6. EU overlap.** Vehicle type-approval products are excluded from the EU Cyber Resilience Act (tree 6) and, in Great Britain, from PSTI (tree 11) — record the exclusion with its source so the "no" is defensible.

---

## Using the trees

1. Run every tree, even where the answer seems obvious — the register needs the documented "no" with its test outcome.
2. One register row per regime **per legal entity** where group entities differ.
3. Any tree that ends on an unresolved fact → the fact goes to the "open facts" list and the row's confidence drops to Medium at best.
4. Any tree that ends on legal interpretation (targeting, "significantly engaged," hybrid entity, NIS2 national divergence, DORA carve-outs, Quebec's reach, UAE "large amount" thresholds) → counsel flag, confidence Low or Medium.
5. Any tree whose outcome depends on a **designation or notification by an authority** — CER, CIRCIA, UK CTPs, Hong Kong PCICSO, Singapore CII, China CIIO, India SDF, UAE CII, TSA criticality, Saudi NCNICC circulation — is answered by the notice, not by self-assessment. Record "designated / not designated / designation risk" and the date the status was checked.
6. Any tree whose regime is not yet in force (UK Cyber Security and Resilience Bill, CIRCIA final rule, Canada's CCSPA Schedule 2, Singapore Parts 3C and 3D) is registered as **monitor**, with the trigger handed to `../../regulatory-horizon-scanning/SKILL.md`.
7. Date every tree run; re-run affected trees on the change triggers recorded in the register.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
