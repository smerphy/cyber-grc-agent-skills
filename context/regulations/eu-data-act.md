# EU Data Act (Regulation (EU) 2023/2854)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | Regulation (EU) 2023/2854 of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act), OJ L, 22.12.2023; legal basis Art. 114 TFEU; directly applicable, no transposition |
| Publisher / regulator | European Commission (DG CNECT) for guidance; enforcement by national competent authorities designated under Art. 37, with a national "data coordinator" where several are designated; DPAs for personal-data aspects; EDPS for Union bodies |
| Status and key dates | In force 11 January 2024; applies since 12 September 2025; Art. 3(1) access-by-design duty live since 12 September 2026 for connected products and related services placed on the market after that date; switching charges abolished from 12 January 2027; Chapter IV reaches certain legacy contracts from 12 September 2027; no amending act adopted, Digital Omnibus still a proposal |
| Who is covered | Manufacturers of connected products and providers of related services (regardless of establishment), users in the EU, data holders and data recipients, public sector bodies, providers of data processing services (cloud/edge, IaaS/PaaS/SaaS) serving EU customers, data-space participants and smart-contract vendors (Art. 1(3)) |
| Structure | 11 chapters, 50 articles: IoT data access (Ch. II), B2B sharing terms (Ch. III), unfair terms (Ch. IV), B2G access (Ch. V), cloud switching (Ch. VI), international governmental access (Ch. VII), interoperability (Ch. VIII), enforcement (Ch. IX), database right (Ch. X), final provisions (Ch. XI) |
| Penalties | Set nationally (Art. 40), must be effective, proportionate and dissuasive; DPAs may fine Chapter II, III and V infringements up to the GDPR Art. 83(5) ceiling (EUR 20 million or 4% of worldwide annual turnover, whichever is higher) |
| Assessment model | No certification; self-compliance, contract and product design, complaint-driven supervision, certified dispute-settlement bodies (Art. 10) |
| Relationship to neighbours | Complements GDPR (which prevails on conflict, Art. 1(5)); adds binding cloud-switching obligations to the self-regulatory approach of Regulation (EU) 2018/1807 (Art. 1(7)); sits alongside the Data Governance Act; the Digital Omnibus proposal of 19 November 2025 would fold the DGA, the Open Data Directive and 2018/1807 into it |

## What it is

The Data Act is the horizontal "who may use what data, on what terms" law of the EU data strategy. It gives users of connected products (vehicles, industrial machinery, smart appliances, wearables) and their related services a right to the data those products generate, lets users route that data to third parties of their choice, regulates the terms on which data holders must share data under any EU or national law, polices unilateral unfair contract terms between enterprises, creates a business-to-government access route for exceptional needs, and imposes switching, exit and interoperability duties on cloud and edge providers. It was adopted on 13 December 2023, published on 22 December 2023, entered into force on 11 January 2024 and has applied since 12 September 2025.

For security and GRC teams it matters in two directions. As a **customer** of cloud services, it hands you statutory exit rights (notice, transition and retrieval periods, data erasure, no switching charges) that should be written into contracts and exit plans. As a **manufacturer, service provider or cloud provider**, it imposes design, transparency, contractual and security obligations, including a duty to resist unlawful third-country governmental access to non-personal data (Art. 32) and to disclose the jurisdiction of your infrastructure (Art. 28).

## Who it covers / Scope

| Actor (Art. 1(3)) | Coverage test | Notes |
|---|---|---|
| Manufacturers of connected products; providers of related services | Product placed on the EU market or service provided to EU users, **irrespective of place of establishment** | "Connected product" (Art. 2(5)): item that obtains, generates or collects data on its use or environment and can communicate it; primary function is not storing/processing data for others. Virtual assistants are included when they interact with a connected product (Art. 1(4)) |
| Users in the EU | Owner or holder of contractual usage rights of a connected product, or recipient of a related service (Art. 2(12)) | Consumers and businesses alike |
| Data holders | Natural or legal person with the right or obligation to use and make data available (Art. 2(13)), irrespective of establishment, when making data available to recipients in the EU | Typically the manufacturer or related-service provider |
| Data recipients | Business receiving data in the EU (Art. 2(14)) | Gatekeepers under the DMA cannot be eligible third parties (Art. 5(3)) |
| Public sector bodies, Commission, ECB, Union bodies | Requesting data under Chapter V | Data holders responding are also in scope |
| Providers of data processing services | Serving customers in the EU, irrespective of establishment | Definition (Art. 2(8)) mirrors cloud computing; Recital 81 and the Commission FAQ confirm IaaS, PaaS and SaaS are all covered |
| Data-space participants; smart-contract vendors | Offering data or data services in a data space; deploying smart contracts to execute data-sharing agreements | Chapter VIII essential requirements |

Key carve-outs and limits:

- **Data in scope:** Chapter II covers data on the performance, use and environment of connected products and related services, **excluding content** (Art. 1(2)(a)); "readily available data" (Art. 2(17)) is what the holder can obtain without disproportionate effort.
- **SME exemption (Art. 7):** Chapter II duties do not apply to data from products or services of micro and small enterprises (unless partnered/linked to a larger enterprise or subcontracted), nor to medium-sized enterprises for their first year of that status, nor for one year after a medium-sized enterprise places a product on the market.
- **Personal data:** GDPR, Regulation (EU) 2018/1725 and the ePrivacy Directive apply in full and prevail on conflict (Art. 1(5)); a user who is not the data subject only receives personal data where a GDPR Art. 6 (and, if relevant, Art. 9) basis exists (Arts. 4(12), 5(7)).
- **Out of scope:** law-enforcement, customs, taxation, national security and defence (Art. 1(6)); voluntary data-sharing arrangements are not pre-empted (Arts. 1(6), 1(10)); IP law is unaffected (Art. 1(8)); sector-specific EU access rules in force on or before 11 January 2024 remain unaffected (Art. 44).
- **Non-EU entities** offering connected products or services in the EU must designate an EU legal representative (Art. 37(11)–(13)); until they do, every Member State's authority may act against them.

## Core obligations

### Chapter II — access to product and related-service data (Arts. 3–7)

| Art. | Obligation | Detail |
|---|---|---|
| 3(1) | Access by design | Product and related-service data, with the metadata needed to interpret them, accessible to the user by default: easily, securely, free of charge, in a comprehensive, structured, commonly used, machine-readable format and, where relevant and feasible, directly. Applies to products/services placed on the market after 12 September 2026 (Art. 50) |
| 3(2)–(3) | Pre-contract transparency | Before purchase, rent or lease: data type, format, estimated volume, real-time capability, on-device vs remote storage and retention, how to access/retrieve/erase; related services add identity of the data holder, intended own use and third-party use, trade-secret holder identity, complaint route, contract duration |
| 4(1) | Access on request | Where direct access is not possible: make readily available data accessible without undue delay, same quality as the holder has, free, continuously and in real time where feasible, on a simple electronic request |
| 4(2) | Security restriction | Access may be contractually restricted only where processing could undermine legal security requirements with serious adverse effects on health, safety or security of persons; refusals must be notified to the competent authority |
| 4(4)–(5) | No dark patterns; minimal verification | Choices must be offered neutrally; no data collected or logs retained beyond what verification and infrastructure security need |
| 4(6)–(9) | Trade secrets | Holder identifies trade-secret data (including in metadata) and agrees proportionate technical and organisational confidentiality measures; may withhold or suspend if measures are not agreed or are breached; may refuse only in exceptional cases of demonstrable, highly likely serious economic damage. Each withholding, suspension or refusal must be notified to the competent authority and is challengeable |
| 4(10)–(14) | Use limits | User may not build a competing connected product or profile the manufacturer's economics; data holder may use non-personal product data only under contract with the user and may not pass it to third parties beyond that contract |
| 5 | Sharing with third parties | On the user's request the holder must make data available to a designated third party on the same terms, free of charge to the user, under Arts. 8–9; DMA gatekeepers excluded; trade-secret mechanics mirror Art. 4 |
| 6 | Third-party duties | Use only for agreed purposes; erase when no longer needed; no profiling unless necessary for the service; no onward transfer without user contract; no transfer to gatekeepers; no competing product; no adverse impact on the product's security |

### Chapter III — terms for mandatory B2B data sharing (Arts. 8–12)

- **FRAND terms and non-discrimination** between comparable recipient categories (Art. 8); exclusivity only at the user's request; no disclosure of trade secrets beyond Arts. 4(6) and 5(9).
- **Compensation** must be reasonable and non-discriminatory, may include a margin; for SMEs and not-for-profit research recipients it is capped at the direct cost of making data available (Art. 9). Commission guidelines on reasonable compensation are mandated by Art. 9(5) after consulting the EDIB; FAQ v1.4 (22 January 2026) expected them in Q2/Q3 2026, but the Commission's Data Act page (last updated 2 July 2026) still lists them as future work, so they were not adopted as of September 2026.
- **Dispute settlement bodies** certified by Member States decide within 90 days; decisions bind only if both parties agreed in advance (Art. 10).
- **Technical protection measures** (Art. 11): holders may use encryption and smart contracts to enforce terms; misuse triggers erasure, cessation and compensation remedies.
- Applies to data-sharing obligations under EU or national law entering into force after 12 September 2025 (Art. 50).

### Chapter IV — unfair contractual terms (Art. 13)

Terms on data access, use, liability or remedies **unilaterally imposed** by one enterprise on another are non-binding if unfair. Blacklist (always unfair, Art. 13(4)): excluding liability for intent or gross negligence; excluding remedies for non-performance; sole right to judge conformity or interpret the contract. Grey list (presumed unfair, Art. 13(5)): inappropriate remedy limits, detrimental access to the counterparty's data, blocking the counterparty's use of its own data, blocking termination within a reasonable period, denying a copy of data during or after the contract, unreasonably short termination notice, unilateral price or substantive changes without a valid reason and exit right. The imposing party bears the burden of proving the term was negotiable (Art. 13(6)). Applies to contracts concluded after 12 September 2025 and, from 12 September 2027, to earlier contracts that are indefinite or run at least 10 years from 11 January 2024 (Art. 50).

### Chapter V — business-to-government access (Arts. 14–22)

| Element | Rule |
|---|---|
| Trigger | Exceptional need: (a) public emergency where data cannot be obtained otherwise in time; (b) non-personal data needed for a legally mandated public-interest task after all other means, including market purchase, are exhausted (Art. 15). Micro and small enterprises are exempt from (b) |
| Request content | Written, specific, proportionate, states legal basis, purpose, retention, sharing, penalties for non-compliance; published online by the data coordinator; DPA notified if personal data are requested (Art. 17) |
| Response clock | Comply without undue delay; may decline or seek modification within **5 working days** (public emergency) or **30 working days** (other exceptional need) (Art. 18(2)) |
| Personal data | Anonymise unless disclosure is required; otherwise pseudonymise (Art. 18(4)) |
| Compensation | Emergency data free of charge (except micro/small enterprises); otherwise cost plus reasonable margin (Art. 20) |
| Recipient duties | Purpose limitation, confidentiality, integrity and transfer security measures, erasure when no longer needed, no reuse under the DGA or Open Data Directive, responsibility for security of received data (Arts. 17(3), 19) |

### Chapter VI — switching between data processing services (Arts. 23–31)

| Art. | Obligation | Specifics |
|---|---|---|
| 23 | Remove obstacles | No pre-commercial, commercial, technical, contractual or organisational obstacles to terminating, contracting elsewhere, porting exportable data and digital assets (including after a free tier), achieving functional equivalence, or unbundling |
| 25 | Mandatory contract content | Written, available before signature; switching completed within a **maximum transitional period of 30 calendar days** after a **notice period of at most 2 months**; if technically unfeasible, notify within **14 working days** with justification and an alternative period of **at most 7 months**; customer may extend the transitional period once; **data retrieval period of at least 30 calendar days** after transition; full erasure guarantee after retrieval; exhaustive list of portable data and digital assets, and of trade-secret-related exemptions; support for the customer's exit strategy; continuity, security and known-risk information during switching |
| 26 | Information | Switching procedures, available methods and formats, known restrictions and technical limitations; a reference to an up-to-date online register hosted by the provider giving the data structures, data formats, standards and open interoperability specifications for the exportable data |
| 27 | Good faith | All parties, including the destination provider, cooperate |
| 28 | Transparency on jurisdiction | Publish on the website the jurisdiction to which the ICT infrastructure of each service is subject, and a description of measures against unlawful international governmental access; reference the page in every contract |
| 29 | Switching charges | Cost-based reduced charges only from 11 January 2024 to 12 January 2027; **no switching charges (including egress for switching) from 12 January 2027**; pre-contract disclosure of fees and early-termination penalties |
| 30 | Technical duties | IaaS-type services (Art. 30(1)): the source provider takes all reasonable measures in its power to facilitate the customer achieving functional equivalence **in the use of the destination service**, with capabilities, information, documentation, technical support and tools; PaaS/SaaS: free open interfaces for all customers and destination providers, compatibility with harmonised standards or common specifications within 12 months of their listing in the central Union repository, and export in a structured, commonly used, machine-readable format meanwhile; no duty to hand over IP or trade secrets or to compromise security |
| 31 | Lighter regime | Custom-built services not offered at broad commercial scale are exempt from Arts. 23(d), 29 and 30(1) and (3); non-production test versions are outside Chapter VI; customers must be told which duties do not apply |
| 34 | In-parallel (multi-cloud) use | Core switching rules apply mutatis mutandis; egress charges limited to cost pass-through |

Source-provider duties are limited to the source provider's own services and practices (Art. 24); the Commission FAQ stresses no obligation to rebuild the service at the destination.

### Chapter VII — international governmental access to non-personal data (Art. 32)

Providers must take all adequate technical, organisational and legal measures, including contracts, to prevent third-country governmental access to or transfer of non-personal data held in the EU that would conflict with EU or Member State law. Third-country orders are enforceable only under an international agreement such as an MLAT; absent one, compliance is permitted only if the third-country system requires reasoned, proportionate, specific orders, allows the addressee's objection to be reviewed by a court, and lets that court weigh the interests protected by EU law. Providers may seek an opinion from the national body for international legal cooperation (one-month window), must provide the minimum data, and must inform the customer before complying unless law-enforcement effectiveness requires secrecy. Recital 102 names encryption of data, frequent submission to audits, verified adherence to relevant security reassurance certification schemes and modification of corporate policies as the kind of measures expected.

### Chapter VIII — interoperability (Arts. 33–36)

- Data-space participants must describe dataset content, licences, quality, structures, vocabularies and APIs in machine-readable, public form (Art. 33); harmonised standards and common specifications give a presumption of conformity.
- Cloud interoperability specifications must cover transport, syntactic, semantic, behavioural and policy interoperability plus data and application portability (Art. 35); the Commission publishes references in a central Union repository by implementing act (Art. 35(8)).
- **Smart contracts** executing data-sharing agreements must meet essential requirements (robustness, access control, safe termination, archiving, consistency) with a vendor conformity assessment and EU declaration of conformity (Art. 36). The Digital Omnibus proposal would delete Art. 36.

### Chapter X — database right (Art. 43)

The sui generis database right of Directive 96/9/EC does not apply to data obtained from or generated by connected products or related services.

## Enforcement and penalties

| Topic | Rule |
|---|---|
| Competent authorities | One or more per Member State; a data coordinator is the single point of contact where several exist (Art. 37(1)–(2)); the cloud-switching authority must have data and electronic-communications expertise (Art. 37(4)); the Commission keeps a public register (Art. 37(7)) |
| Personal data | DPAs supervise the Data Act insofar as personal data are concerned, using GDPR Chapters VI–VII powers; the EDPS supervises Union bodies (Art. 37(3)) |
| Jurisdiction | Member State of establishment or main establishment (Art. 37(10)); non-EU entities via their legal representative (Art. 37(11)–(13)) |
| Powers | Complaints handling, investigations, information requests, financial penalties including periodic and retroactive penalties (Art. 37(5), (14)) |
| Remedies | Individual or collective complaints (Art. 38); judicial remedy against authority decisions (Art. 39); the Act is added to the annexes of Regulation (EU) 2017/2394 and Directive (EU) 2020/1828, opening consumer-protection cooperation and representative actions (Arts. 47–48) |
| Penalties | National rules, notified to the Commission by 12 September 2025, judged on gravity, mitigation, prior infringements, gains and EU turnover (Art. 40(1)–(3)); DPAs may impose GDPR Art. 83 fines up to the Art. 83(5) ceiling for Chapters II, III and V; the EDPS may fine Union bodies under Regulation (EU) 2018/1725 for Chapter V (Art. 40(4)–(5)) |
| Coordination | The European Data Innovation Board (EDIB) coordinates enforcement practice, including penalty-setting recommendations (Art. 42) |

National implementation is uneven. Germany's implementing act (DADG) entered into force on 30 May 2026, making the Bundesnetzagentur the competent authority, dispute-body certifier and cloud-switching supervisor. Other Member States are at varying stages; check the Commission register for the current authority before filing a complaint or notification.

## Timeline and status

| Date | Event |
|---|---|
| 13 Dec 2023 / 22 Dec 2023 | Adopted / published in the Official Journal |
| 11 Jan 2024 | Entry into force; cost-based reduced switching charges permitted from this date (Art. 29(2)) |
| 6 Sep 2024 | Commission FAQ v1.0 published; v1.4 dated 22 January 2026 is the current version |
| 9 Dec 2024 | Corrigendum (OJ L, 2024/90790) renumbering the point added by Art. 48 to Annex I of Directive (EU) 2020/1828; four further language-specific corrigenda exist, none amending the substance |
| 12 Sep 2025 | General application; Chapter IV applies to new contracts; deadline for Member States to notify penalty rules (Art. 40(2)); Art. 41 model terms due; Commission guidance on vehicle data published |
| 19 Nov 2025 | Commission approves and publishes the **draft** Recommendation on non-binding Model Contractual Terms (data sharing) and Standard Contractual Clauses (cloud contracts), in English only pending translation; Digital Omnibus proposal (COM(2025) 837) and Data Union Strategy tabled the same day |
| 16 Dec 2025 | Commission Data Act Legal Helpdesk launched |
| Feb–May 2026 | Digital Omnibus opinions: EDPB-EDPS Joint Opinion 2/2026 (10 Feb), ECB (10 Mar), EESC (18 Mar), Committee of the Regions (7 May) |
| 30 May 2026 | German implementing act (DADG) in force; Bundesnetzagentur becomes the competent authority, certifies dispute-settlement bodies and supervises cloud switching |
| 12 Sep 2026 | Art. 3(1) access-by-design duty starts applying to connected products and related services placed on the market after this date (now in effect) |
| 12 Jan 2027 | Switching charges, including egress for switching, prohibited (Art. 29(1)) |
| 12 Sep 2027 | Chapter IV extends to qualifying legacy contracts (Art. 50) |
| 12 Sep 2028 | Commission evaluation reports due (Art. 49) |

**Digital Omnibus (still a proposal, as of September 2026).** COM(2025) 837 of 19 November 2025, procedure 2025/0360(COD), would amend the Data Act to: add a trade-secret refusal ground in Arts. 4(8) and 5(11) where disclosure poses a high risk of unlawful acquisition, use or disclosure to third-country entities, or to EU entities under their direct or indirect control, subject to jurisdictions offering weaker or non-equivalent protection than Union law; narrow Chapter V from "exceptional need" to public emergencies by deleting Arts. 14 and 15 and inserting a single Art. 15a, with a new Art. 22a complaints route and a derogation letting micro and small enterprises claim compensation for emergency data; delete Art. 36 on smart contracts; insert Art. 31(1a)–(1b) disapplying Chapter VI (except Art. 29 on switching charges) and Art. 34 for custom-adapted services and for SME and small mid-cap providers on contracts concluded before or on 12 September 2025, and permit proportionate early-termination penalties in fixed-duration contracts; and fold the Data Governance Act, the Open Data Directive and Regulation (EU) 2018/1807 into the Data Act as new Chapters VIIa–VIIc, with those acts and Regulation (EU) 2019/1150 repealed. The Commission's Digital Package FAQ describes small mid-caps as companies with "less than 749 employees"; the threshold is set by the final text, not this FAQ. The EDPB and EDPS adopted Joint Opinion 2/2026 on 10 February 2026. The EUR-Lex procedure file records Commission adoption (19 Nov 2025), ECB, EESC and Committee of the Regions opinions (Mar–May 2026) and no Parliament first-reading position or Council general approach; the procedure is still "Ongoing" and the Data Act's EUR-Lex record shows no amending act. Treat all Omnibus changes as proposals until published in the Official Journal.

Guidance already published: FAQ v1.4 (22 January 2026), sector guidance on vehicle data for Chapter II (12 September 2025), the draft MCT/SCC Recommendation (19 November 2025) and the Data Act Legal Helpdesk (16 December 2025). Still outstanding as of September 2026: Commission guidelines on reasonable compensation (Art. 9(5)); the delegated act establishing the switching-charge monitoring mechanism (Art. 29(7)); the implementing acts that would list harmonised standards and common specifications in the central Union standards repository (Art. 35(8)), which FAQ v1.4 says must follow a mapping exercise; the "European Trusted Data Framework" standardisation request supporting Art. 33 (seven standardisation deliverables, per FAQ v1.4); the Commission register of competent authorities and data coordinators (Art. 37(7)); and the list of certified dispute-settlement bodies (Art. 10(6)). No Data Act enforcement decision or Court of Justice ruling had been identified in the sources reviewed for this pack.

## Key obligations for security/GRC teams

1. **Classify your roles** (manufacturer, related-service provider, data holder, data recipient, cloud provider, cloud customer, data-space participant) per product line and service; confirm the Art. 7 SME exemption and whether a legal representative is needed. See [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **As a cloud customer, rewrite exit clauses to the Art. 25 minimums** (2-month notice cap, 30-day transition, 30-day retrieval, erasure, no switching fees from 12 January 2027) and cite the Commission SCCs in negotiations; fold this into vendor onboarding and the exit plans DORA already demands. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../workflows/vendor-onboarding.md](../../workflows/vendor-onboarding.md).
3. **As a cloud provider, publish the Art. 28 jurisdiction and governmental-access statement**, stand up the Art. 26 online register of data formats and interfaces, and build the Art. 32 request-handling procedure (lawfulness check, national-body consultation, minimum data, customer notice).
4. **Meet the Art. 3(1) access-by-design duty**, which since 12 September 2026 applies to newly placed connected products and related services: data catalogue with metadata, secure user-facing retrieval API, real-time streaming where feasible, verification that collects no more than necessary, and access logs retained only for security and maintenance.
5. **Build the trade-secret workflow**: identify trade-secret data in metadata, template confidentiality measures, a documented decision path for withholding, suspension or refusal, and the mandatory notification to the competent authority. Track refusals as formal exceptions; see [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md).
6. **Screen data-sharing and cloud contracts against the Art. 13 lists** and the Art. 25 checklist; log unilateral terms and evidence of negotiation, because the imposing party carries the burden of proof. See [../../skills/policy-authoring/SKILL.md](../../skills/policy-authoring/SKILL.md) for contract-standard drafting.
7. **Align with GDPR**: map which product data are personal, confirm the Art. 6 basis before releasing data to non-data-subject users or third parties, and update DPIAs for IoT data flows. See [../../skills/dpia-privacy-assessment/SKILL.md](../../skills/dpia-privacy-assessment/SKILL.md).
8. **Prepare a Chapter V response playbook**: request validation against Art. 17, the 5- and 30-working-day objection clocks, anonymisation and pseudonymisation steps, and cost recovery.
9. **Watch the Digital Omnibus and national implementing laws** and re-run impact assessments when the final text lands. See [../../skills/regulatory-horizon-scanning/SKILL.md](../../skills/regulatory-horizon-scanning/SKILL.md) and [../../workflows/new-regulation-impact-assessment.md](../../workflows/new-regulation-impact-assessment.md).

## Interplay

- **GDPR:** applies in full and prevails on conflict (Art. 1(5)); Chapter II rights complement GDPR Arts. 15 and 20 access and portability; DPAs supervise personal-data aspects and can fine at GDPR levels for Chapters II, III and V. See [gdpr.md](gdpr.md).
- **DORA:** financial entities' cloud contracts must satisfy both DORA Art. 30 (exit strategies, data return, audit rights) and Data Act Art. 25 switching terms; the Data Act's statutory transition and retrieval periods and charge abolition give DORA exit plans enforceable minimums, while DORA's register of information and critical-provider oversight are unaffected. See [dora.md](dora.md).
- **NIS2:** cloud computing service providers subject to NIS2 security and incident-reporting duties also carry Data Act switching, transparency and Art. 32 obligations; the Art. 32 "adequate measures" expectation (encryption, audits, certification) overlaps with NIS2 Art. 21 measures. See [nis2.md](nis2.md).
- **EU AI Act:** connected products with embedded AI, and third parties that use Chapter II data to build AI-enabled services, sit under both regimes; Data Act use limits (Arts. 4(10), 6) constrain what recipients may build from product data regardless of AI Act classification. See [eu-ai-act.md](eu-ai-act.md).
- **Digital Markets Act:** designated gatekeepers cannot receive Data Act data as third parties (Arts. 5(3), 6(2)(d)).
- **Data Governance Act and Regulation (EU) 2018/1807:** the Data Act complements 2018/1807's self-regulatory cloud codes with binding switching duties (Art. 1(7)); Art. 32 parallels DGA Art. 31; the Omnibus would merge both into the Data Act.
- **Trade Secrets Directive (EU) 2016/943:** definitions are imported (Art. 2(18)–(19)); the Data Act adds procedural gates for disclosure rather than changing substantive protection.

## Primary sources

- Regulation (EU) 2023/2854 (Data Act), consulted in full — legal text: https://eur-lex.europa.eu/eli/reg/2023/2854/oj
- Corrigendum to Regulation (EU) 2023/2854, OJ L, 2024/90790, 9 December 2024 — legal text: https://eur-lex.europa.eu/eli/reg/2023/2854/corrigendum/2024-12-09/oj
- Regulation (EU) 2016/679 (GDPR), Art. 83(5) fine ceiling — legal text: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- European Commission, "Data Act" policy page — publisher page: https://digital-strategy.ec.europa.eu/en/policies/data-act
- European Commission, "Data Act explained" fact page — regulator guidance: https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained
- European Commission, Frequently Asked Questions on the Data Act, version 1.4, 22 January 2026 — regulator guidance (non-binding): https://ec.europa.eu/newsroom/dae/redirection/document/108144 (landing page: https://digital-strategy.ec.europa.eu/en/library/commission-publishes-frequently-asked-questions-about-data-act)
- European Commission, Draft Recommendation on non-binding Model Contractual Terms on data access and use and non-binding Standard Contractual Clauses for cloud computing contracts, 19 November 2025 — regulator guidance: https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding
- European Commission, "Guidance on vehicle data, accompanying the Data Act", 12 September 2025 — regulator guidance (automotive sector only): https://digital-strategy.ec.europa.eu/en/library/guidance-vehicle-data-accompanying-data-act
- European Commission, "Commission launches Data Act legal helpdesk", 16 December 2025 — publisher page: https://digital-strategy.ec.europa.eu/en/news/commission-launches-data-act-legal-helpdesk
- Proposal for a Regulation (Digital Omnibus), COM(2025) 837 final, 19 November 2025, read in full for the Data Act amendments — preparatory act: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025PC0837 (Commission page: https://digital-strategy.ec.europa.eu/en/library/digital-omnibus-regulation-proposal; Digital Package FAQ, source of the small mid-cap description: https://digital-strategy.ec.europa.eu/en/faqs/digital-package)
- EUR-Lex procedure file 2025/0360(COD), used for the Digital Omnibus legislative status as of September 2026 — procedure record: https://eur-lex.europa.eu/legal-content/EN/HIS/?uri=CELEX:52025PC0837
- EDPB-EDPS Joint Opinion 2/2026 on the Digital Omnibus proposal, adopted 10 February 2026 — regulator opinion: https://www.edpb.europa.eu/system/files/2026-02/edpb_edps_jointopinion_202602_digitalomnibus_en.pdf
- Bundesnetzagentur press release, 30 May 2026, "Bundesnetzagentur wird zuständige Behörde für den Data Act in Deutschland" — regulator page: https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/DE/2026/20260530_DA.html
- Not fetched: the EUR-Lex full-text search interface and the European Parliament pages require JavaScript, so the absence of delegated or implementing acts under Arts. 29(7), 33 and 35(8), and of Parliament or Council positions on the Digital Omnibus, rests on the EUR-Lex document and procedure records and on the Commission pages listed above rather than on an exhaustive search.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
