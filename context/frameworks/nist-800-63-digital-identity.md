# NIST SP 800-63-4 — Digital Identity Guidelines (SP 800-63 Revision 4)

## At a glance

| Attribute | Detail |
|---|---|
| Instrument | NIST Special Publication 800-63, Revision 4 — a four-volume suite: SP 800-63-4 (base), 800-63A-4 (identity proofing and enrollment), 800-63B-4 (authentication and authenticator management), 800-63C-4 (federation and assertions) |
| Publisher | National Institute of Standards and Technology (NIST), Information Technology Laboratory |
| Status and key dates | All four volumes published July 2025; CSRC document history records 31 July 2025 as the final-publication date. Supersedes SP 800-63-3 (last updated 2 March 2020) |
| Who is covered | US federal agencies operating online services (employees, contractors and public users); incorporated by reference into other regimes and widely adopted voluntarily by private-sector and state/local identity programs |
| Structure | Three independent assurance scales — IAL (proofing), AAL (authentication), FAL (federation) — each with levels 1/2/3, selected per user group through a five-step Digital Identity Risk Management (DIRM) process |
| Normative language | Requirements are written as SHALL / SHALL NOT, with SHOULD / MAY recommendations; each of the four volumes contains both normative and informative material |
| Certifiable? | No NIST certification or accreditation scheme. Conformance is asserted and evidenced — for relying parties through a Digital Identity Acceptance Statement (DIAS); for credential service providers through a documented practice statement plus independent biometric performance testing |
| Cost | Free; full text published openly on csrc.nist.gov, nvlpubs.nist.gov and pages.nist.gov |
| Scope exclusions | National security systems (44 U.S.C. § 3552(b)(6)); machine-to-machine authentication, IoT devices and APIs acting on behalf of subjects are not explicitly addressed; physical access control is out of scope |
| Related but distinct | FIPS 201-3 (PIV) extends these guidelines for the federal enterprise; OMB M-19-17 (ICAM), M-22-09 (zero trust, phishing-resistant MFA) and M-26-18 (Login.gov as universal sign-on, August 2026) are the policy instruments that make them mandatory for agencies |

## What it is

SP 800-63 is the US government's technical baseline for digital identity: how much confidence you need that a real person is who they claim (IAL), that the person returning to the account is the same person (AAL), and that an assertion passed between an identity provider and a relying party can be trusted (FAL). Revision 4 is the first major rewrite since 2017 and is the culmination of a nearly four-year process with two public drafts (December 2022 and August 2024) and roughly 6,000 individual public comments.

The suite's defining architectural choice — introduced in Rev. 3 and retained in Rev. 4 — is that the three assurance scales are **selected independently**. A service may legitimately require AAL2 with no identity proofing at all (pseudonymous accounts), or IAL2 proofing with FAL1 federation. Rev. 4 pushes this further by replacing compliance-driven level selection with an explicit, documented **risk-based** process, and by requiring organizations to assess risk *to individuals and communities*, not only to the organization.

Substantive changes in Rev. 4 (per NIST's own summary) include: reframed risk-management context and new cross-functional engagement expectations; new continuous-evaluation metrics; expanded fraud requirements for identity proofing; restructured proofing controls that define proofing roles and proofing types; new controls for digital injection attacks and forged media (deepfakes); integration of syncable authenticators (synced passkeys); representation of subscriber-controlled wallets in the federation model; and revised password composition and rotation expectations.

## Who it covers / Scope

- **Applies to** all online services for which some level of digital identity assurance is required, regardless of constituency — the public, business partners, and government employees and contractors. "Person" means a natural person.
- **Federal relying parties SHALL implement the DIRM process for all online services.** Agency authorizing officials SHOULD require DIRM documentation as part of the authority-to-operate package, and SHOULD require equivalent documentation from CSPs during procurement or integration.
- **Credential service providers (CSPs) and identity providers (IdPs)** are expected to offer services at the assurance levels their relying parties request, and SHALL clearly communicate any deviation from normative guidance to those relying parties; a CSP or IdP that deviates from or augments the normative guidance SHALL run the DIRM process and produce its own DIAS.
- **Not covered:** national security systems; machine-to-machine and IoT authentication; API access on behalf of subjects; physical access control (though the processes may be applied there).
- **Voluntary adopters.** NIST states that private-sector organizations and state, local and tribal governments whose processes require varying levels of identity assurance may use the standards where appropriate. Onward adoption into sectoral regimes (e.g., criminal-justice, tax-data and cloud-authorization programs) is common but regime-specific — confirm the exact clause and the referenced revision in the governing policy rather than assuming AAL2 (verify).

## Structure and requirements

### Digital Identity Risk Management (DIRM) — SP 800-63-4, Sec. 3

Five normative steps: (1) **define the online service** — mission, user groups, transactions, data, impacted entities; (2) **conduct initial impact assessment** per user group; (3) **select initial assurance levels**; (4) **tailor and document** the determinations; (5) **continuously evaluate and improve**.

At minimum, impact assessments SHALL cover five categories: degradation of mission delivery; damage to trust, standing or reputation; unauthorized access to information; financial loss or liability; and loss of life or danger to human safety, human health or environmental health.

| Combined impact level | Initial IAL | Initial AAL | Initial FAL |
|---|---|---|---|
| Low | IAL1 | AAL1 | FAL1 |
| Moderate | IAL2 | AAL2 | FAL2 |
| High | IAL3 | AAL3 | FAL2 or FAL3 (further IdP-compromise assessment required) |

Tailoring assesses privacy, customer experience (usability/equity) and threat resistance, and may raise or lower an initially assessed level or substitute **compensating** or add **supplemental** controls. All of it lands in the **Digital Identity Acceptance Statement (DIAS)** — required for every online service the organization runs *and* every external online service it relies on, including SaaS. A DIAS SHALL contain at minimum the initial impact assessment results, the initially assessed xALs, any tailored xAL with rationale, all compensating controls with comparability or residual risk, and all supplemental controls.

### Identity proofing — SP 800-63A-4

Four proofing **types** are defined by location and attendance: remote unattended, remote attended (secure video session), on-site unattended (controlled kiosk/workstation), and on-site attended. Hybrid processes are permitted if documented.

| IAL | Evidence to collect | Delivery | Distinguishing requirement |
|---|---|---|---|
| IAL1 | One piece of: FAIR evidence that can be digitally validated or carries a facial portrait/other biometric; **or** STRONG; **or** SUPERIOR | Any proofing type | All core attributes and the government identifier validated against an authoritative or credible source |
| IAL2 | FAIR + STRONG, **or** two STRONG, **or** one SUPERIOR | Any proofing type | Three verification pathways — Non-Biometric, Biometric, Digital Evidence; pathway used SHALL be recorded and disclosed to relying parties |
| IAL3 | Same collection set as IAL2 | **On-site attended only** (agent co-located or via CSP-controlled kiosk) | A biometric sample SHALL be collected and retained for recovery and non-repudiation |

Other 63A obligations that matter for assurance work: core attributes SHALL include a government identifier; SUPERIOR evidence SHALL be validated by cryptographic verification back to a trust anchor (otherwise it may only count as STRONG); CSPs SHALL run a documented **fraud management program** (identification, detection, investigation, reporting, resolution); CSPs SHALL maintain a **practice statement** covering service description, evidence types accepted and justification, validation/verification technologies, personnel training, exception handling (trusted referees and applicant references), core attributes and their authoritative sources, service-change communication, and reverification conditions; and CSPs SHALL implement digital injection prevention and forged-media (deepfake) detection for remote proofing.

Biometric performance thresholds in 63A are hard numbers: 1:1 verification FMR **1:10,000 or better** and FNMR **1:100 or better**; 1:N identification false positive identification rate **1:1,000 or better** tested against a gallery no smaller than 90 % of operational size; performance for any demographic group no more than **25 % worse** than the overall population, at a fixed threshold; presentation attack detection with IAPAR **< 0.07**; testing conformant to ISO/IEC 19795-1:2021, ISO/IEC 19795-10:2024 and ISO/IEC 30107-3:2023; results made publicly available. A 1:N hit SHALL NOT cause enrollment denial without manual review.

### Authentication — SP 800-63B-4

| Requirement | AAL1 | AAL2 | AAL3 |
|---|---|---|---|
| Permitted authenticators | Password, look-up secret, out-of-band, single-factor OTP, single-factor cryptographic, or any AAL2/AAL3 type | Multi-factor cryptographic, MF out-of-band or MF OTP; or password or biometric comparison **plus** a single-factor authenticator (single-factor cryptographic, look-up secret, out-of-band or single-factor OTP) | Multi-factor cryptographic; or single-factor cryptographic plus a password or biometric comparison |
| FIPS 140 validation (government) | Verifiers Level 1 | Verifiers Level 1; authenticators Level 1 overall | Verifiers Level 1; authenticators Level 1 overall |
| Reauthentication (recommended) | 30 days overall | 24 hours overall, 1 hour inactivity | 12 hours overall, 15 minutes inactivity |
| Phishing resistance | Not required | Recommended; must be available | Required |
| Replay resistance | Not required | Required | Required |
| Authentication intent | Not required | Recommended | Required |
| Key exportability | Permitted | Permitted | **Prohibited** |

**Phishing resistance** is defined as the protocol's ability to prevent disclosure of authentication secrets and valid authenticator outputs to an impostor verifier *without relying on the claimant's vigilance*. Only two mechanisms qualify: **channel binding** (e.g., client-authenticated TLS, as used by PIV/CAC) and **verifier name binding** (e.g., WebAuthn/FIDO2 binding to the authenticated domain). Anything requiring manual entry of an output — OTP, out-of-band codes — SHALL NOT be treated as phishing-resistant.

**Passwords** (63B Sec. 3.1.1): minimum **15 characters** when used as a single-factor mechanism, minimum **8** when part of MFA; maximum length SHOULD be at least 64; other composition rules SHALL NOT be imposed; periodic forced rotation SHALL NOT be required (force a change only on evidence of compromise); prospective passwords SHALL be compared in full against a blocklist of common, expected or breached values; password hints and knowledge-based authentication/security questions SHALL NOT be used; password managers SHALL be allowed and paste SHOULD be permitted. Verifiers SHALL limit consecutive failed attempts on a given authenticator to no more than **100**, then disable it pending rebinding.

**Biometrics** may only be used as part of MFA alongside a physical authenticator, never alone; FMR **1 in 10,000 or better for all demographic groups**; FNMR SHOULD be under 5 %; PAD SHALL be implemented for facial recognition; **voice-based biometric comparison SHALL NOT be used**; attempt limits of 5 consecutive failures (10 with conforming PAD), a 30-second delay thereafter, and an overall cap of 50 (100 with PAD); an alternative non-biometric option SHALL always be offered.

**Syncable authenticators (synced passkeys)** are normative in Appendix B. Because the private key is exportable by design, they **SHALL NOT be used at AAL3** but may support AAL2. For federal enterprise use they add four conditions: sync fabrics SHALL have FISMA Moderate protections or equivalent; devices that generate/store/sync the keys SHALL be under MDM or equivalent configuration control preventing sync to unauthorized devices or fabrics; access to the sync fabric SHALL be controlled by agency-managed accounts; and authenticators SHOULD support attestation. Verifiers SHALL indicate WebAuthn user verification as preferred and inspect the UV flag — if the user is not verified, the authenticator SHALL be treated as single-factor.

**Account recovery** (63B Sec. 4.2): saved recovery codes SHALL carry at least 64 bits of entropy, be stored hashed, be invalidated after use and replaced; issued recovery codes SHALL be at least six decimal digits; subscribers SHALL be able to register at least two recovery addresses, each verified by confirmation code; recovery events generate notifications, with postal notification required for AAL3 recovery in defined cases.

### Federation — SP 800-63C-4

Two federation models: general-purpose IdPs, and **subscriber-controlled wallets** (on-device or remote-hosted), new in Rev. 4.

| Requirement | FAL1 | FAL2 | FAL3 |
|---|---|---|---|
| Audience restriction | Multiple RPs allowed per assertion; single RP recommended | Single RP per assertion | Single RP per assertion |
| Replay protection | Required per RP | Required | Required |
| Assertion injection protection | Recommended | Required; transaction begins at the RP | Required; transaction begins at the RP |
| Trust agreement | Subscriber-driven or pre-established | Pre-established | Pre-established |
| Identifier and key establishment | Dynamic or manual | Dynamic or manual | **Manual** |
| Presentation | Bearer assertion | Bearer assertion | Holder-of-key assertion or bound authenticator |

At FAL3 the relying party SHALL independently verify that the subscriber controls an additional authenticator, which protects against a compromised IdP. Both IdPs and RPs SHALL provide subscribers an accessible means of **redress** for matters under their control, and a route to initiate redress with the other party.

## Assessment, certification and evidence

There is no NIST certificate and no accredited "800-63 auditor" regime. Evidence takes four practical forms:

1. **The DIAS** — the single most auditable artifact. Expect an assessor to ask for one per online service, including for third-party services in use.
2. **The CSP practice statement** and its supporting fraud-management documentation, where identity is outsourced. A relying party SHALL review a prospective CSP's or IdP's DIAS and fold the relevant content into its own.
3. **Independent biometric performance test results**, which CSPs SHALL have produced by independent entities and SHALL make publicly available (summary form permitted).
4. **Configuration evidence** mapped to the AAL/FAL tables above — password policy exports, MFA enrolment coverage by authenticator type, reauthentication timeout settings, WebAuthn flag handling, assertion audience/replay settings.

Where SP 800-63 is invoked by a controls framework rather than directly, the controls framework's assessment model governs: 800-63 supplies the parameter values (which AAL, which evidence strength) rather than a separate audit.

## Timeline and status

| Date | Event |
|---|---|
| 2017 | SP 800-63-3 published (the previous major revision) |
| 2 March 2020 | Last update to SP 800-63-3 (the version Rev. 4 supersedes) |
| 16 December 2022 | Initial public draft of Rev. 4 |
| 21 August 2024 | Second public draft of Rev. 4 |
| 6 June 2025 | Executive Order 14306 struck section 5 of EO 14144, removing the federal programme to promote acceptance of digital identity documents (e.g., mobile driver's licences); 800-63-4 itself was unaffected |
| 31 July 2025 | SP 800-63-4 and volumes A-4, B-4, C-4 published final (cover date July 2025) |
| 1 August 2025 | NIST announcement blog summarizing the substantive changes |
| 20 August 2025 | NIST public webinar on Revision 4 |
| 31 August 2026 | OMB M-26-18 makes Login.gov the universal sign-on for public-facing federal services. Agencies must conduct the SP 800-63-4 DIRM process, including assurance-level selection, for public-facing services with authentication and/or verification **within 240 days** (about 28 April 2027); Login.gov deployment is due within one year for High Impact Service Provider services and two years for all other in-scope sites; NIST is directed to publish a DIRM implementation resource within 120 days (about 29 December 2026) |
| As of September 2026 | No revision, errata or supplement to Rev. 4 identified on CSRC; the four volumes as published on 31 July 2025 are the current text. NIST has stated that implementation resources are in development, including machine-readable conformance criteria and a digital identity risk management tool — the DIRM resource now has an OMB-set date but none of these had been published as at September 2026 |

The older "Roadmap: SP 800-63-4" page on nist.gov is explicitly flagged as no longer updated and still shows pre-publication projections; do not cite it for dates.

## Key obligations for security/GRC teams

1. **Run and document the DIRM process per online service and per user group** — not once per organization. Output a DIAS for each. US federal teams now also have an OMB deadline for this (see Timeline and status). See [risk-assessment](../../skills/risk-assessment/SKILL.md).
2. **Set IAL, AAL and FAL independently.** Resist the reflex to align them; the mapping table above is a starting point, not the answer, and tailoring decisions must be written down with rationale.
3. **Rewrite password standards to Rev. 4.** Fifteen characters for single-factor, no composition rules, no scheduled rotation, blocklist screening, no security questions. This usually contradicts an existing policy and an existing platform baseline — handle both. See [policy-authoring](../../skills/policy-authoring/SKILL.md).
4. **Classify your authenticators by phishing resistance honestly.** SMS, push and TOTP do not qualify. 63B itself requires verifiers to offer at least one phishing-resistant option at AAL2 and requires federal agencies to mandate phishing-resistant authentication for staff, contractors and partners; OMB M-22-09 carries the same obligation as policy — required for agency staff, contractors and partners, and an option that must be offered to public users — and was still cited as current OMB policy in August 2026.
5. **Decide the syncable-passkey position explicitly.** AAL2 yes, AAL3 no, and for enterprise use expect the sync fabric, device-management, account-control and attestation conditions to be assessed. Document the WebAuthn flag policy (UV, backup eligible/state).
6. **Treat proofing vendors as regulated third parties.** Demand the practice statement, the fraud-management approach, the verification pathways offered, the biometric test results and the deepfake/injection controls. See [third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md) and [vendor-security-questionnaire.md](../../templates/vendor-security-questionnaire.md).
7. **Build account recovery into the control set.** Recovery is the most common AAL bypass; test it as a control, not as a helpdesk process. See [control-testing](../../skills/control-testing/SKILL.md).
8. **Stand up the continuous-evaluation programme** Rev. 4 requires (63-4 Sec. 3.5) and track its recommended metrics — pass, fail and abandonment rates overall and per proofing type, confirmed/suspected/reported fraud, account recovery attempts, help-desk volumes and resolution times — alongside other program metrics. See [grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md).
9. **Map 800-63 parameters into your control framework** rather than running it as a parallel regime. See [control-mapping](../../skills/control-mapping/SKILL.md) and the [framework crosswalk](../crosswalks/framework-crosswalk.md).

## Interplay

- **[NIST SP 800-53](nist-800-53.md):** the IA (Identification and Authentication) family is where 800-63 lands operationally; 63B requires verifiers to employ appropriately tailored controls from the 800-53 moderate baseline (or an equivalent federal or industry standard), and 800-53 privacy controls for CSP deployments. 800-53 says *have* MFA; 800-63 says *which* MFA counts.
- **[NIST CSF 2.0](nist-csf-2.md):** PR.AA (Identity Management, Authentication and Access Control) is the CSF outcome that 800-63 makes concrete; the DIRM process slots under GV and ID.
- **[ISO/IEC 27001:2022](iso-27001-2022.md):** the Annex A controls on identity management, authentication information and access rights are the hooks (confirm the exact control numbers against the standard itself, which is paywalled). 800-63 is a defensible way to justify the parameters recorded in a Statement of Applicability.
- **[PCI DSS v4.x](pci-dss-4.md), [HIPAA](../regulations/hipaa.md), [GLBA Safeguards](../regulations/glba-ftc-safeguards.md):** each mandates MFA or equivalent without defining assurance; 800-63 AAL2/AAL3 is the usual reference for "what good looks like", but the regime's own prescriptive rules (e.g., PCI DSS password parameters) still govern where they conflict — do not substitute 800-63 password rules for an explicit PCI requirement.
- **[CIS Controls v8/v8.1](cis-controls-v8.md):** Controls 5 and 6 sit at safeguard granularity; 800-63 supplies the assurance-level detail those safeguards leave open.
- **eIDAS (EU Regulation (EU) No 910/2014, as subsequently amended):** the EU uses assurance levels low/substantial/high for electronic identification. NIST and the European Commission released a joint EU-US Trade and Technology Council WG-1 Digital Identity Mapping Exercise Report (preliminary results, published for feedback in December 2023) comparing definitions, assurance levels and standards references — but that mapping was performed against **Rev. 3**, not Rev. 4, and produced commonalities, not equivalence. Treat any IAL↔eIDAS-level equation as an analytical aid only. A separate context pack covers the EU eIDAS regime.
- **FIPS 201-3 (PIV):** extends 800-63 for the federal enterprise with PIV card issuance, derived credentials and PIV federation; PIV/CAC are phishing-resistant by channel binding.
- **Glossary note:** CSP, IdP, RP, verifier, claimant, subscriber and applicant are defined roles in this suite; using them loosely in policy causes real scoping errors. See [glossary.md](../glossary.md).

## Primary sources

- SP 800-63-4, Digital Identity Guidelines (base volume, full text) — https://pages.nist.gov/800-63-4/sp800-63.html ; publication record and document history at https://csrc.nist.gov/pubs/sp/800/63/4/final
- SP 800-63A-4, Identity Proofing and Enrollment (full text) — https://pages.nist.gov/800-63-4/sp800-63a.html ; record at https://csrc.nist.gov/pubs/sp/800/63/a/4/final
- SP 800-63B-4, Authentication and Authenticator Management (full text) — https://pages.nist.gov/800-63-4/sp800-63b.html ; record at https://csrc.nist.gov/pubs/sp/800/63/b/4/final
- SP 800-63C-4, Federation and Assertions (full text) — https://pages.nist.gov/800-63-4/sp800-63c.html ; record at https://csrc.nist.gov/pubs/sp/800/63/c/4/final
- NIST publisher announcement, "Let's get Digital! Updated Digital Identity Guidelines are Here!", 1 August 2025 — https://www.nist.gov/blogs/cybersecurity-insights/lets-get-digital-updated-digital-identity-guidelines-are-here
- NIST SP 800-63 project page (webinar, past updates) — https://www.nist.gov/identity-access-management/projects/nist-special-publication-800-63-digital-identity-guidelines
- NIST EU-US TTC WG-1 Digital Identity Mapping Exercise Report page — https://www.nist.gov/identity-access-management/eu-us-ttc-digital-identity-mapping-exercise-report
- OMB M-26-18, "Scaling Use of Login.gov to Deliver a Universal Sign-on for Public Services", 31 August 2026 — https://www.whitehouse.gov/wp-content/uploads/2026/08/M-26-18-Scaling-Use-of-Login.gov-to-Deliver-a-Universal-Sign-on-for-Public-Services.pdf ; OMB memoranda index at https://www.whitehouse.gov/omb/information-for-agencies/memoranda/
- OMB M-22-09, "Moving the U.S. Government Toward Zero Trust Cybersecurity Principles", 26 January 2022 — https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf
- Executive Order 14144 (16 January 2025) and Executive Order 14306 (6 June 2025), which struck its digital identity section — https://www.govinfo.gov/content/pkg/FR-2025-01-17/html/2025-01470.htm and https://www.govinfo.gov/content/pkg/FR-2025-06-11/html/2025-10804.htm
- Superseded predecessor SP 800-63-3 (publication record, for the supersession date) — https://csrc.nist.gov/pubs/sp/800/63/3/upd2/final
- FIPS 201-3, Personal Identity Verification of Federal Employees and Contractors (publication record) — https://csrc.nist.gov/pubs/fips/201-3/final

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of September 2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-09.
