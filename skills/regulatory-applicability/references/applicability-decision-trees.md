# Applicability Decision Trees per Major Regime

Structured trigger questions for the regimes most often mis-scoped. Each tree yields **Applies / Does not apply / Needs counsel review**, plus the facts that must be documented in the register rationale. Work every question in order; the first decisive answer ends the tree. Where a question depends on a fact you do not have, the output is not a guess — it is "open fact: [X]" in the register.

Regime substance (obligations, deadlines, penalties) lives in the context files linked per section — this file only answers "in scope or not."

---

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

**Also record:** controller vs processor role per processing activity (processors are directly caught by Art. 3 too), and UK GDPR as a separate row — its territorial test mirrors Art. 3 with the UK substituted.

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

**Q3. Size-independent inclusion.** Small/micro entities are still in scope if they are: qualified trust service providers; TLD name registries or DNS service providers; sole providers in a member state of a service essential to critical societal/economic activity; providers whose disruption could significantly impact public safety, security, or health, or induce systemic risk; critical entities under CER; certain public administration entities; providers of public electronic communications networks/services (these are in scope regardless of size, classification by size). Any hit → in scope (member-state identification may be required for some categories). No hit → **Not in scope.**

**Q4. Essential vs important.** Broad rule: **essential** = Annex I sectors at **large** size (250+ employees, or turnover > EUR 50M / balance sheet > EUR 43M), plus the special categories designated essential regardless of size (e.g., qualified trust service providers, TLD registries and DNS providers, sole providers) and entities designated essential by a member state or under CER. **Important** = other in-scope entities (Annex I medium-sized; Annex II regardless of large/medium). Classification changes supervision intensity (ex-ante vs ex-post) and fine caps, not the core Art. 21 measures or Art. 23 reporting duties.

**Q5. Which member state(s)?** Jurisdiction generally follows establishment; for DNS/TLD/cloud/data centre/CDN/managed service/digital providers, main-establishment rules apply and non-EU providers of those services need an EU representative. National transpositions add registration duties and diverge in detail → **counsel/local review flag for every multi-state footprint.**

---

## 3. DORA — financial entity types

Context: `../../../context/regulations/dora.md`

**Q1. Is the organization one of the financial entity types listed in DORA Art. 2?** Principal list: credit institutions; payment institutions; account information service providers; electronic money institutions; investment firms; crypto-asset service providers and issuers of asset-referenced tokens; central securities depositories; central counterparties; trading venues; trade repositories; managers of alternative investment funds; UCITS management companies; data reporting service providers; insurance and reinsurance undertakings; insurance, reinsurance, and ancillary insurance intermediaries; institutions for occupational retirement provision; credit rating agencies; administrators of critical benchmarks; crowdfunding service providers; securitisation repositories.
- Yes → **DORA applies** to that entity. Note the exclusions/carve-outs (e.g., certain small AIFMs under the AIFMD registration regime, small IORPs, microenterprise intermediaries, and entities excluded from their sectoral directive) and proportionality provisions — verify the specific entity type against Art. 2's exclusion list. **Counsel flag** for borderline license types.
- No → Q2.

**Q2. Does the organization provide ICT services to EU financial entities** (software, cloud, data analytics, data centres, managed services)?
- Yes → not directly a DORA obligor, but two exposures: (a) **contractual flow-down** — financial entity customers must impose DORA-derived contract terms (Art. 30: audit/access rights, exit strategies, incident support, subcontracting conditions); (b) possible designation as a **critical ICT third-party provider (CTPP)** subject to direct oversight by an ESA-led framework, with fees and remediation powers. Register as "contractual + designation risk," not "applies."
- No → **Not in scope.**

---

## 4. HIPAA — covered entity and business associate tests

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

**Q3. Common traps before concluding "no":** employee health data in an employer's hands as employer is generally **not** PHI (but the group health plan's data is); health data collected direct-to-consumer outside a CE relationship (wellness apps) is outside HIPAA but inside FTC Health Breach Notification Rule and state health-privacy laws (e.g., Washington My Health My Data) — add those rows instead. No hit → **HIPAA does not apply.** Re-test trigger: first healthcare customer or PHI-touching service.

---

## 5. SEC reporting and SOX — listed status

Context: `../../../context/regulations/sec-cyber-disclosure.md`, `../../../context/regulations/sox-itgc.md`

**Q1. Is the organization an SEC registrant** (securities registered under the Exchange Act, or required to file periodic reports)?
- No → SOX and SEC disclosure do not apply. Re-test trigger: IPO preparation (obligations begin with the registration process), US listing, or crossing shareholder-of-record thresholds.
- Yes → Q2.

**Q2. Domestic issuer or foreign private issuer (FPI)?**
- **Domestic:** cyber disclosure via **Form 8-K Item 1.05** (material incidents, four business days from materiality determination) and **Form 10-K Item 106** (Reg S-K: risk management, strategy, governance).
- **FPI:** furnish material incident information on **Form 6-K**; annual report cyber disclosure in **Form 20-F**. Do not put 8-K obligations in an FPI's register.

**Q3. SOX scope.** All registrants: s302 officer certifications and s404(a) management assessment of ICFR — ITGCs over financially relevant systems in scope. **s404(b) auditor attestation** depends on filer category (accelerated and large accelerated filers; exemptions for smaller/emerging companies) → record filer status as a register fact. Newly public companies get transition accommodations → counsel/auditor confirmation.

**Q4. Adjacent:** listed on a non-US exchange → that market's listing rules and disclosure regime instead (register per jurisdiction).

---

## 6. US state comprehensive privacy laws — threshold tests

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

**Always-on rows regardless of thresholds:** state **breach notification** laws (no size thresholds — holding one resident's covered data suffices), state data-broker registration laws, sectoral state laws (WA My Health My Data, Illinois BIPA for biometrics — private right of action, no size threshold).

---

## 7. GLBA — "financial institution" test (and FTC Safeguards Rule)

Context: `../../../context/regulations/glba-ftc-safeguards.md`

**Q1. Is the organization significantly engaged in financial activities** (as defined by reference to the Bank Holding Company Act §4(k))? This reaches far beyond banks. FTC-jurisdiction examples: mortgage lenders and brokers, payday and other non-bank lenders, finance companies, auto dealers that extend credit or lease, check cashers, wire transfer / money services businesses, collection agencies, credit counselors, tax preparation firms, investment advisors not required to register with the SEC, and "finders" bringing together buyers and sellers of financial products. Higher-education institutions participating in federal student aid are held to Safeguards Rule compliance.
- No → Not a GLBA financial institution. Re-test trigger: launching lending, payment, or advisory activity.
- Yes → Q2.

**Q2. Does it handle nonpublic personal information of consumers** (individuals obtaining financial products/services for personal/family/household purposes)?
- No (pure B2B financial activity) → GLBA privacy/safeguards obligations largely fall away — counsel flag before concluding.
- Yes → Q3.

**Q3. Which regulator?** Banks/credit unions → prudential regulators' safeguards and the Interagency Guidelines (plus the 36-hour incident notification rule). Broker-dealers/advisers → SEC Regulation S-P (including its customer notification amendments). Everyone else → **FTC Safeguards Rule**: written ISP, qualified individual, risk assessment, the rule's enumerated safeguards (encryption, MFA, access controls, monitoring/pen-testing, vendor oversight, IR plan, board reporting), and FTC notification of security events affecting **500+ consumers' unencrypted customer information within 30 days of discovery**. Note the rule's limited exemption for institutions maintaining information on fewer than 5,000 consumers (exempts some written-documentation elements, not the safeguards themselves).

**Also:** receiving consumer financial data *from* financial institutions can bind a non-FI via GLBA reuse/redisclosure limits — register as contractual/derived.

---

## 8. EU AI Act — role and reach

Context: `../../../context/regulations/eu-ai-act.md`

**Q1.** Does the org **place on the EU market or put into service** AI systems (or general-purpose AI models), regardless of where the org is established? → **provider** obligations by risk tier.
**Q2.** Is the org established/located in the EU and **using** AI systems under its authority (other than personal non-professional use)? → **deployer** obligations.
**Q3.** Is the org outside the EU but the **output** of its AI system is used in the EU? → in scope.
**Q4.** Importer/distributor of AI systems into the EU market? → respective obligations.
Any yes → classify each system by tier (prohibited / high-risk per Annex III and product-safety route / transparency-risk / minimal) and add register rows per role. Timeline staggering matters — obligations phase in by tier; see the context file. Hand system-level analysis to `../../ai-governance/SKILL.md`.

---

## 9. PCI DSS — contractual scope test

Context: `../../../context/frameworks/pci-dss-4.md`

**Q1.** Does the org **store, process, or transmit cardholder data**, or can it **impact the security of cardholder data or the cardholder data environment** (e.g., hosting the payment page, managing systems that could affect the payment flow)?
- Yes → **PCI DSS applies contractually** (via acquirer/merchant agreement or as a service provider to such parties). Determine merchant vs service provider role, transaction-volume level, and eligible validation route (SAQ type vs on-site assessment/ROC).
- No, payments fully outsourced with no CHD contact and no impact on its security → validate the SAQ A-style eligibility claim with the acquirer; register as "not applicable — outsourced, confirmed [date]."

---

## 10. Government contracts — clause-driven regimes (US federal pattern)

**Q1.** Any US federal contracts or subcontracts? Check clauses, not assumptions: FAR 52.204-21 (basic safeguarding of federal contract information), DFARS 252.204-7012 (covered defense information → NIST SP 800-171 compliance + 72-hour incident reporting to DoD), CMMC clauses phasing in per DoD program, FedRAMP if selling cloud services to agencies. Subcontractors inherit via flow-down. See `../../../context/frameworks/nist-800-53.md`.
**Q2.** Non-US public sector contracts → the buyer's national security-clause frameworks (register per contract).
Classify all of these as **contractually binding** with statutory enforcement backdrops (e.g., False Claims Act exposure for US federal misrepresentations — counsel flag).

---

## 11. Additional regimes — quick trigger tests

Run these one-line tests and pull the linked pack for any "yes"; each pack's "At a glance" table carries the fuller scope test:

- **EU Cyber Resilience Act** — do you manufacture (or import/distribute into the EU) hardware or software "products with digital elements"? → [../../../context/regulations/eu-cra.md](../../../context/regulations/eu-cra.md)
- **CER Directive** — could a member state designate you a critical entity (physical/essential services lens)? → [../../../context/regulations/eu-cer.md](../../../context/regulations/eu-cer.md)
- **ePrivacy / PECR** — do you set cookies/trackers on, or send electronic marketing to, EU/UK users? → [../../../context/regulations/eu-eprivacy.md](../../../context/regulations/eu-eprivacy.md)
- **UK regime** — UK establishment, UK customers, or monitoring of UK individuals? → [../../../context/regulations/uk-data-protection.md](../../../context/regulations/uk-data-protection.md)
- **NYDFS Part 500** — do you hold a NY banking, insurance, or financial-services license or authorization? → [../../../context/regulations/nydfs-500.md](../../../context/regulations/nydfs-500.md)
- **CIRCIA** — do you operate in one of the 16 US critical-infrastructure sectors above the rule's size/criteria thresholds? → [../../../context/regulations/circia.md](../../../context/regulations/circia.md)
- **FISMA stack** — are you a US federal agency, or a contractor operating systems on an agency's behalf? → [../../../context/regulations/fisma.md](../../../context/regulations/fisma.md)
- **US sectoral privacy** — children under 13 (COPPA), student records (FERPA), non-HIPAA health apps (HBNR), video viewing data (VPPA)? → [../../../context/regulations/us-sector-privacy.md](../../../context/regulations/us-sector-privacy.md)
- **APAC / Americas national regimes** — customers, employees, or operations in Australia, Canada, Singapore, Japan, South Korea, India, China, or Brazil? → per-country packs indexed in [../../../context/regulations/other-jurisdictions.md](../../../context/regulations/other-jurisdictions.md); note the sector overlays with the shortest clocks (MAS 1h, CERT-In 6h, SOCI 12h).

## Using the trees

1. Run every tree, even where the answer seems obvious — the register needs the documented "no" with its test outcome.
2. One register row per regime **per legal entity** where group entities differ.
3. Any tree that ends on an unresolved fact → the fact goes to the "open facts" list and the row's confidence drops to Medium at best.
4. Any tree that ends on legal interpretation (targeting, "significantly engaged," hybrid entity, NIS2 national divergence, DORA carve-outs) → counsel flag, confidence Low or Medium.
5. Date every tree run; re-run affected trees on the change triggers recorded in the register.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
