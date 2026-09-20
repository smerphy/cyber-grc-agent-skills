# PCI SSC standards beyond PCI DSS (SSF, P2PE, PIN, KMO, PTS, 3DS, MPoC)

## At a glance

| Attribute | Detail |
|---|---|
| Publisher | PCI Security Standards Council (PCI SSC), LLC — founded by the card brands; standards developed with participating organizations through Request for Comments (RFC) periods |
| What this pack is | A navigator for the fifteen PCI standards listed alongside PCI DSS that are **not** PCI DSS. For PCI DSS itself see [pci-dss-4.md](pci-dss-4.md) — this file does not restate its requirements |
| Who they bind | Mostly **product and service providers** (terminal makers, software vendors, solution providers, acquirers/processors, card personalizers), not ordinary merchants. Merchants consume them as listed, validated products |
| Validation model | Vendor/provider is assessed by a PCI-qualified assessor → report (ROV/ROC/P-ROV) + attestation (AOV/AOC) → PCI SSC quality review → public **listing** with an expiry/reassessment date |
| Enforcement | Contractual. PCI SSC publishes the standards and the product/provider listings; compliance programs, validation obligations and any penalties are set by the payment brands and acquirers |
| Newest standard | **PCI Key Management and Operations (KMO) v1.0**, published 14 September 2026 |
| Retiring | **SPoC**, **CPoC** and **3DS SDK** are in a formal sunset period: 1 May 2026 – 31 October 2026; no new submissions accepted after 31 October 2026 |
| Already retired | **PA-DSS** — retired 28 October 2022, superseded by the Software Security Framework (Secure Software + Secure SLC) |
| Why GRC cares | Scope reduction (P2PE, MPoC), vendor due-diligence evidence (listings and AOVs), and secure-SDLC assurance (SSF) — all cheaper than proving equivalent controls yourself |

## What it is

PCI DSS protects the *environment* that stores, processes or transmits account data. The rest of the PCI portfolio protects the *things that environment is built from*: the terminal, the HSM, the keys, the payment software, the mobile acceptance app, the 3-D Secure authentication components, and the card-personalization bureau. PCI SSC splits the portfolio into standards organizations apply inside their own environment (PCI DSS, PIN Security, Card Production, 3DS Core, TSP — none of these produce a public product listing, although PIN service providers may opt into one) and standards under which a product or service is validated and publicly listed (Secure Software, Secure SLC, P2PE, PTS POI, PTS HSM, MPoC, KMO).

For a security or GRC function the practical value is asymmetric. Three of these standards materially shrink PCI DSS effort (P2PE, MPoC, and the PTS device approvals they depend on); two of them are what a software vendor is asked for instead of a PCI DSS AOC (Secure Software, Secure SLC); the rest are due-diligence questions you ask a counterparty rather than obligations you carry.

2025–2026 has been the portfolio's heaviest revision cycle in years: PTS POI v7.0 (May 2025), P2PE v3.2 (June 2025), Secure Software v2.0 (January 2026), PTS HSM v5.0 (May 2026) and KMO v1.0 (September 2026), with Secure SLC v2.0 and Card Production v3.0.1 in flight and three standards sunsetting.

## Who it covers / Scope

| Standard | Current version / date | Who must care | Validation route |
|---|---|---|---|
| Secure Software | **v2.0**, 15 Jan 2026 (prior v1.2.1) | Software vendors whose products touch **sensitive assets** (data, resources, functionality) in payment flows; from v2.0 also generic SDKs, including EMVCo 3DS SDKs | Secure Software Assessor → ROV + AOV → Validated Secure Software listing |
| Secure Software Lifecycle (Secure SLC) | **v1.1** (verify), published 18 Feb 2021; v2.0 RFC closed 15 Jun 2026 | Software vendors wanting their development and change-management processes qualified once instead of per product | Secure SLC Assessor → ROC + AOC → Secure SLC Qualified Vendor listing |
| Point-to-Point Encryption (P2PE) | **v3.2**, 30 Jun 2025 | Solution providers, component providers (key injection, encryption/decryption/key-management services) and P2PE application developers | P2PE Assessor → P-ROV per product type → listed P2PE Solution / Component / Application |
| Key Management and Operations (KMO) | **v1.0**, 14 Sep 2026 | Entities operating key-management systems for PIN and P2PE keys, including cloud and remote HSM deployments | KMO Assessor (qualification requirements pending as of Sep 2026) → KMO listing, referenceable by a P2PE implementation |
| PIN Security | Requirements and Testing Procedures published 11 Mar 2021; version number not shown on any open publisher page (verify) | Acquirers and their agents processing PINs at ATMs and attended/unattended POS | Qualified PIN Assessor (QPA) → PIN ROC + PIN AOC; optional public PIN listing |
| PTS Point of Interaction (POI) | **v7.0**, 29 May 2025 (from v6.2) | PIN-entry and payment terminal manufacturers | PCI Recognized Laboratory evaluation → Approved PTS Devices listing |
| PTS Hardware Security Module (HSM) | **v5.0**, 18 May 2026 (from v4.0) | HSM manufacturers, including HSM-as-a-Service and multi-tenant offerings | PCI Recognized Laboratory evaluation → approval listing |
| Mobile Payments on COTS (MPoC) | **v1.1**, Nov 2024 | Vendors of phone/tablet payment acceptance (PIN entry and/or contactless on COTS) | MPoC lab/assessor evaluation → MPoC Solution, Software or Service listing |
| SPoC / CPoC | Sunsetting 1 May – 31 Oct 2026 | Legacy software-PIN-entry and contactless-on-COTS solutions; successor is MPoC | Existing listings run their normal lifecycle; no new submissions after 31 Oct 2026 |
| PCI 3DS Core | **v1.0** (Oct 2017); v2.0 drafted, RFC Dec 2023–Jan 2024, unpublished as of Sep 2026 | Entities running EMV 3-D Secure Access Control Server, Directory Server, 3DS Server or Split-SDK Server functions | 3DS Assessor → 3DS Core ROC + AOC |
| PCI 3DS SDK | Sunsetting 1 May – 31 Oct 2026 | EMVCo 3DS SDK vendors — assessment migrates to Secure Software v2.0 | Existing SDK listings run their normal lifecycle; new assessments move to Secure Software v2.0, with the 3DS Data Matrix v1.2 carrying the SDK sensitive-data context |
| Card Production and Provisioning (Logical + Physical) | Published 30 Jun 2022 and unchanged since (v3.0 (verify)); exploratory RFC on a v3.0.1 draft 13 Feb – 16 Mar 2026 | Card manufacturers, personalizers, and digital provisioning operations | Card Production Security Assessor (CPSA) → ROC + AOC |
| Token Service Provider (TSP) | v1.0, 2015 (verify — the open publisher page carries no version or date) | TSPs generating and issuing EMV payment tokens under the EMVCo tokenisation framework | Assessed by P2PE Assessors; confirm brand-specific validation obligations |

Note that MPoC, SPoC and CPoC solutions are **not** eligible for P2PE approval — they are separate standards for separate use cases, though the devices can coexist in one merchant estate.

## Structure and requirements

**Software Security Framework (SSF).** Two standards, deliberately separable: Secure Software assesses the *product*; Secure SLC assesses the *vendor's lifecycle*. A vendor need not be Secure SLC qualified to list a product, but qualification avoids re-proving development and change-management processes for every product and unlocks the streamlined delta-change route. Secure Software v2.0 is the first major revision since 2019 and drops the v1.x term "payment software" in favour of **sensitive assets** (sensitive data, sensitive resources, sensitive functionality), with a companion *Sensitive Asset Identification* document; it pins allowable cryptography to PCI DSS's definition of **strong cryptography**, introduces version-schema wildcards for non-security-impacting changes, and replaces the v1.x low/high-impact change model with a rebuilt delta-change process and a new Change Impact template. Secure SLC v2.0 (RFC 15 May – 15 June 2026, publication expected in the second half of 2026) adds "digital tools" content covering the use of AI inside a vendor's development lifecycle and realigns to the sensitive-asset model.

**P2PE.** Account data is encrypted in a PTS-approved POI device and decrypted only inside the solution provider's controlled environment. The POI must be PCI PTS-approved, non-expired, and listed with **SRED** as a function provided *and* enabled (verify); any software present on the POI that was not part of its PTS-approved firmware must itself be assessed against the P2PE Standard. The decryption environment's HSM and key-management requirements sit in the licensed standard text and are not reproduced on any open page (verify). v3.2 is a minor revision clarifying POI device testing and sampling, whitelist management, non-payment software and P2PE Applications; the major v4.0 revision is still in development.

**PIN, keys and hardware.** PIN Security governs PIN management, processing and transmission end to end; PTS POI and PTS HSM govern the devices. KMO v1.0 consolidates the generic key-management requirements that previously sat inside PIN and P2PE into one modular, "assess-once-use-many" standard covering generation, conveyance, loading, use, archive, retirement and destruction, explicitly including cloud-based and remote HSMs, and built in alignment with HSM v5.0. PTS HSM v5.0 is a major rewrite: device-security keys must use cryptography with an effective strength of at least 128 bits, TDES is no longer permitted for device-security purposes, new evaluation modules cover Key-Transfer Functionality, Remote Administration and HSM Solution Security, and multi-tenant controls (tenant key erasure, tenant isolation) were added alongside post-quantum considerations and alignment to ANSI X9.143. PTS POI v7.0 carried 59 requirement changes and 23 additions of guidance, including a new biometric-interface requirement, third-party application (app store) allowance, the same 128-bit effective key strength floor for terminal security keys, and an optional accessibility PIN-entry mode.

**3-D Secure.** PCI 3DS Core sets physical and logical security requirements for the ACS, DS, 3DS Server and Split-SDK Server components implementing the EMVCo protocol; the accompanying 3DS Data Matrix (v1.1 until January 2026, then v1.2; the Document Library copy was refreshed again on 9 September 2026, current version (verify)) defines which data elements are sensitive. For PCI DSS purposes, 3DS authentication values are **not** sensitive authentication data.

**PCI DSS supporting-document layer.** These are not separate standards but are frequently mistaken for them. Current items include the Prioritized Approach for PCI DSS and its tool (Jan 2025), the ROC Template (Jan 2025), the Supplemental ROC Template and Supplemental AOC for **Designated Entities** (PCI DSS Appendix A3, Aug 2024), the SAQ set (Oct 2024 – Jan 2025) and SAQ Instructions and Guidelines (Apr 2025), Targeted Risk Analysis guidance and sample TRA template (Nov 2023), the ASV Program Guide and ASV Resource Guide, guidance on Requirements 6.4.3/11.6.1 (Apr 2025), *Guidance for Compensating Controls and the Customized Approach* (Jun 2026), and a PCI DSS v4.0.1 → NIST CSF 2.0 mapping (Jul 2026). The published SAQ set is A, A-EP, B, B-IP, C, C-VT, D-Merchant, D-Service Provider, **P2PE** and **SPoC**; SAQ D for Service Providers is the only correct SAQ for a service provider. Requirement-level detail belongs in [pci-dss-4.md](pci-dss-4.md).

## Assessment, certification and evidence

- **Assessor programs** map one-to-one onto the standards: QSA and ISA (PCI DSS), ASV (external scanning), QPA (PIN), P2PE Assessor (P2PE and TSP), Secure Software Assessor and Secure SLC Assessor (SSF), 3DS Assessor, CPSA (card production), KMO Assessor (new), plus PFI (forensic investigation) and QIR (integrator/reseller); PTS device and HSM evaluations are performed by PCI Recognized Laboratories. In PCI DSS assessments, assessor independence is a fundamental tenet — an assessor who designed or implemented a control cannot assess that control.
- **What you collect from a vendor** is the *listing entry* plus the attestation: for P2PE the listed solution name and its reassessment date; for SSF the Validated Secure Software or Secure SLC Qualified Vendor entry; for terminals the Approved PTS Devices entry with SRED status. An AOV/AOC with no matching listing, or a listing whose product version differs from the one you deployed, is weak evidence. See [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md) and [../../templates/vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md).
- **Listing colour codes matter.** On the P2PE lists, an orange reassessment date means revalidation is up to 90 days overdue and red means more than 90 days overdue; both still count as validated. A listing that stays red for more than 90 days is moved to the *Expired Validations* list; solutions on that list are **not** validated — merchants relying on them for SAQ P2PE must check with their acquirer or the brands.
- **Listing durations are finite.** PIN Service Provider listings, for example, are valid two years from the QPA signature date on the AOC. Track expiry dates in the vendor register the same way you track SOC 2 report periods.

## Timeline and status (as of September 2026)

| Date | Event |
|---|---|
| 28 Oct 2022 | PA-DSS retired; SSF is the only route for payment software validation |
| 26 Nov 2024 | MPoC v1.1 published |
| 19 May 2025 | PCI SSC PIN Listing Program launched (promotional pricing to 31 Dec 2025; standard fee from 1 Jan 2026) |
| 29 May 2025 | PTS POI v7.0 published (from v6.2) |
| 30 Jun 2025 | P2PE v3.2 published; P2PE v4.0 revision continues |
| 31 Dec 2025 / 31 Mar 2026 | Last date for P2PE v3.1 submissions / last date for those submissions to clear quality review |
| 1 Jan 2026 | All new P2PE submissions and reassessments must be against v3.2 |
| 15 Jan 2026 | Secure Software Standard v2.0 and Program Guide v2.0 published; 3DS Data Matrix updated to v1.2 |
| 13 Feb – 16 Mar 2026 | RFC on draft Card Production and Provisioning Physical and Logical Security Standards v3.0.1 |
| 1 May 2026 | Sunset periods open for SPoC, CPoC and 3DS SDK |
| 15 May – 15 Jun 2026 | RFC on draft Secure SLC Standard v2.0; publication expected in H2 2026 |
| 18 May 2026 | PTS HSM v5.0 published (from v4.0) |
| 3 Jun – 20 Jul 2026 | RFC on published PCI DSS v4.0.1, opening the next PCI DSS iteration (AI and future technology explicitly in scope for feedback) |
| 1 Jul 2026 | Updated P2PE Program Guide and a Secure Software ROV template for P2PE Applications published |
| 9 Sep 2026 | PCI 3DS Data Matrix reissued in the Document Library |
| 14 Sep 2026 | PCI KMO Standard v1.0 and KMO Program Guide published; assessor qualification requirements pending |
| 15 Sep 2026 | Information supplement *Security Considerations for AI Systems* published (guidance, not requirements) |
| 31 Oct 2026 | Sunset periods close — no new SPoC, CPoC or 3DS SDK submissions accepted |

## Key obligations for security/GRC teams

1. **Decide which of these you actually carry.** Most enterprises carry none directly; they consume listed products. Run the applicability test before opening a gap assessment — see [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md).
2. **If you are a software vendor, pick the SSF path early.** Secure SLC qualification first, then per-product Secure Software validation, is cheaper across a portfolio than repeated product-only assessments. Budget for the v1.2.1 → v2.0 sensitive-asset re-framing. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).
3. **Treat P2PE and MPoC as scope-reduction projects, not procurement line items.** Eligibility for SAQ P2PE depends on the *listed* solution being current, on no electronic storage of cardholder data anywhere in the merchant estate, and on implementing every control in the provider's P2PE Instruction Manual.
4. **Re-paper PTS device and HSM expectations.** POI v7.0 and HSM v5.0 both set a 128-bit effective-key-strength floor for device security keys; refresh cycles and procurement specifications should state the required standard version, not just "PCI approved".
5. **Watch the three sunsets.** Any roadmap that still assumes SPoC, CPoC or 3DS SDK validation for a *new* product needs re-planning before 31 October 2026; existing listings are unaffected until they expire.
6. **Add listing-expiry tracking to the vendor register** alongside PCI DSS AOCs, and re-check listings at each renewal rather than at onboarding only.
7. **Fold the supporting-document layer into assessment prep** — Prioritized Approach, ROC/SAQ templates, Designated Entity supplements, TRA guidance, and the 2026 compensating-controls/customized-approach supplement. See [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md) and [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
8. **Use the official PCI DSS → NIST CSF 2.0 mapping** rather than a home-grown one when reporting coverage upward; it is directional, not an equivalence claim. See [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md) and [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md).
9. **Track AI guidance separately from requirements.** PCI SSC's AI material — *Integrating Artificial Intelligence in PCI Assessments: Guidelines v1.0* (Mar 2025) and the *Security Considerations for AI Systems* information supplement (Sep 2026) — is explicitly guidance; where guidance and a standard differ, the standard prevails, and AI is scoped like any other technology. See [../../skills/ai-governance/SKILL.md](../../skills/ai-governance/SKILL.md).

## Interplay

- **PCI DSS** — P2PE and MPoC reduce applicable requirements and change which SAQ applies; PTS approval is a precondition for P2PE. None of them remove the merchant's own PCI DSS obligations for whatever remains in scope. See [pci-dss-4.md](pci-dss-4.md).
- **Secure SDLC frameworks** — Secure SLC overlaps heavily with general secure-development expectations in [iso-27001-2022.md](iso-27001-2022.md) (Annex A software development controls) and [nist-800-53.md](nist-800-53.md) SA-family controls; the PCI version is narrower but validated and listed, which general frameworks are not.
- **NIST CSF 2.0** — PCI SSC publishes an official PCI DSS v4.0.1 mapping; use it for coverage analysis, not for asserting that CSF outcomes satisfy PCI requirements. See [nist-csf-2.md](nist-csf-2.md).
- **SOC 2** — a P2PE or SSF listing is narrower and more verifiable than a SOC 2 report but covers only the listed product; the two are complements in vendor files, not substitutes. See [soc2-tsc.md](soc2-tsc.md).
- **CIS Controls** — useful as the implementation-level layer behind a vendor's SSF or P2PE environment controls. See [cis-controls-v8.md](cis-controls-v8.md).
- **Breach handling** — a card-data compromise at a listed provider can trigger PFI investigation and relisting consequences in addition to statutory notification duties; see [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).

## Primary sources

- PCI SSC standards overview — https://www.pcisecuritystandards.org/standards/ (publisher page; scope statements, sunset notices, PA-DSS retirement date) — fetched
- PCI SSC Document Library — https://www.pcisecuritystandards.org/document_library/ (publisher page; document set. The library itself renders client-side, so document dates below were taken from the feed) — fetched
- PCI SSC document feed — https://www.pcisecuritystandards.org/rssfeed/?type=document (publisher feed; titles, categories and publication dates for every library document, read 19 Sep 2026) — fetched
- PCI Perspectives blog feed — https://blog.pcisecuritystandards.org/rss.xml (publisher feed; announcement dates) — fetched
- PCI SSC Bulletin: *Announcement of Sunset Periods for the PCI SPoC and PCI CPoC Standards*, 1 May 2026 — https://www.pcisecuritystandards.org/wp-content/uploads/2026/05/PCI_SPoC_and_PCI_CPoC_Sunset_Bulletin.pdf — fetched
- PCI SSC Bulletin: *Announcement of Sunset Period for the PCI 3DS SDK Standard*, 1 May 2026 — https://www.pcisecuritystandards.org/wp-content/uploads/2026/05/PCI_3DS_SDK_Sunset_Bulletin.pdf — fetched
- PCI SSC, *Just Published: PCI Key Management and Operations (KMO) Standard v1.0*, 14 Sep 2026 — https://blog.pcisecuritystandards.org/just-published-pci-key-management-operations-kmo-standard-v1.0 — fetched
- PCI SSC, *PCI SSC Publishes PCI PTS HSM v5.0*, 18 May 2026 — https://blog.pcisecuritystandards.org/pci-ssc-publishes-pci-pts-hsm-v5.0 — fetched
- PCI SSC, *Just Published: PTS POI v7.0*, 29 May 2025 — https://blog.pcisecuritystandards.org/just-published-pts-poi-v7-0 — fetched
- PCI SSC, *PCI SSC Releases Version 3.2 of the PCI Point-to-Point Encryption (P2PE) Standard*, 30 Jun 2025 — https://blog.pcisecuritystandards.org/pci-ssc-releases-version-3-2-of-the-pci-point-to-point-encryption-p2pe-standard — fetched
- PCI SSC, *PCI SSC Releases Version 2.0 of the PCI Secure Software Standard* (transcript), 28 Jan 2026 — https://blog.pcisecuritystandards.org/coffee-with-the-council-podcast-pci-ssc-releases-version-2-0-of-the-pci-secure-software-standard — fetched
- PCI SSC, *Request for Comments: PCI Card Production and Provisioning Physical and Logical Security Standards v3.0.1*, 13 Feb 2026 — https://blog.pcisecuritystandards.org/request-for-comments-pci-card-production-and-provisioning-physical-and-logical-security-standards-v3.0.1 — fetched
- PCI SSC, *Request for Comments: PCI Secure Software Lifecycle Standard v2.0*, 15 May 2026 — https://blog.pcisecuritystandards.org/request-for-comments-draft-pci-secure-slc-standard-v2.0 — fetched
- PCI SSC, *PCI Mobile Payments on COTS (MPoC) Standard Version 1.1 Now Available*, 26 Nov 2024 — https://blog.pcisecuritystandards.org/pci-mobile-payments-on-cots-mpoc-standard-version-1-1-now-available — fetched
- PCI SSC, *PCI SSC Launches New PIN Listing Program*, 19 May 2025 — https://blog.pcisecuritystandards.org/pci-ssc-launches-new-pin-listing-program — fetched
- PCI SSC, *Request for Comments: Draft PCI 3DS Core Security Standard v2.0 and Draft PCI 3DS Data Matrix v2.0*, 6 Dec 2023 — https://blog.pcisecuritystandards.org/request-for-comments-draft-pci-3ds-core-security-standard-v2-0-and-draft-pci-3ds-data-matrix-v2-0 — fetched
- PCI SSC, *Request for Comments: PCI Data Security Standard (PCI DSS) v4.0.1*, 3 Jun 2026 — https://blog.pcisecuritystandards.org/request-for-comments-pci-data-security-standard-pci-dss-v4.0.1 — fetched
- PCI SSC, *PCI SSC Publishes New Guidance on Compensating Controls and the Customized Approach*, 10 Jun 2026 — https://blog.pcisecuritystandards.org/pci-ssc-publishes-new-guidance-on-compensating-controls-and-the-customized-approach — fetched
- PCI SSC, *Mapping PCI DSS v4.0.1 to the NIST Cybersecurity Framework 2.0*, 23 Jul 2026 — https://blog.pcisecuritystandards.org/mapping-pci-dss-v4.0.1-to-the-nist-cybersecurity-framework-2.0 — fetched
- PCI SSC, *Just Published: Security Considerations for AI Systems*, 15 Sep 2026 — https://blog.pcisecuritystandards.org/just-published-security-considerations-for-ai-systems — fetched
- PCI SSC official FAQ database — https://www.pcisecuritystandards.org/faqs/ — fetched (articles used: 1158 P2PE effect on merchant validation; 1247 SAQ P2PE eligibility; 1339 non-firmware software on a POI; 1457 MPoC/SPoC/CPoC vs P2PE; 1482–1484 listing colours and expired validations; 1578 SAQ D for Service Providers; 1603 3DS authentication values and SAD)
- Standard documents themselves (PCI Secure Software Standard v2.0, P2PE v3.2, PTS POI v7.0, PTS HSM v5.0, KMO v1.0, PIN Security Requirements, Card Production, TSP Security Requirements) are distributed through the PCI SSC Document Library under a licence agreement and direct links are refused — **not fetched**. The version numbers marked "(verify)" above (PIN Security, Card Production, TSP, Secure SLC v1.1, the current 3DS Data Matrix) could not be confirmed from any open publisher page; publication dates for those documents come from the document feed.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
