# UK Cyber Essentials / Cyber Essentials Plus — Baseline Certification Scheme

## At a glance

| Attribute | Detail |
|---|---|
| Owner | UK National Cyber Security Centre (NCSC); delivered by **IASME** as the sole delivery partner, through a network of licensed certification bodies |
| What it is | A government-backed baseline certification against five technical control themes, aimed at stopping the bulk of commodity internet-borne attacks |
| Two tiers | **Cyber Essentials (CE)** — verified self-assessment questionnaire; **Cyber Essentials Plus (CE+)** — same requirements plus an independent hands-on technical audit |
| Current requirements | Question set and requirements document are updated periodically; the **"Willow"** question set (2025) is the most recent named update as of writing — **verify the current set** on the NCSC/IASME sites before scoping |
| Validity | **12 months** — annual recertification expected; CE+ must be preceded by a pass of the CE questionnaire (within a defined window, historically ~3 months) |
| Certifiable? | Yes — certificate issued by the certification body; certified organizations appear in a searchable public register |
| Cost/effort | Low by certification standards: CE is a signed questionnaire marked by an assessor; CE+ adds device sampling, scanning, and testing — days, not months |
| Typical use | UK government contract eligibility, MOD supply chain, insurer/customer signaling, forcing function for baseline hygiene in small and mid-size organizations |

## The five technical control themes

1. **Firewalls** — every in-scope device protected by a correctly configured boundary or software firewall; default deny inbound; no unauthenticated remote administrative access from the internet; documented, approved rules.
2. **Secure configuration** — remove/disable unused accounts, software, and services; change default passwords; disable auto-run; device locking/authentication requirements (PIN/biometric/password rules for unlocking devices).
3. **Security update management** (formerly "patch management") — all in-scope software licensed and supported; high/critical vendor updates applied within **14 days** of release; unsupported software removed or moved out of scope.
4. **User access control** — accounts provisioned per user with an approval process; admin accounts separate from day-to-day accounts and used only for admin tasks; accounts removed on leaver/no-longer-needed; **MFA required for cloud services**; password/passphrase rules and brute-force protections.
5. **Malware protection** — anti-malware software (with signature/behavioral protection kept current) and/or application allow-listing on in-scope devices; mechanisms differ by platform per the current requirements document.

The controls are deliberately prescriptive and binary — each is either met on every in-scope device or it is not.

Two cross-cutting expectations sit behind the themes:

- **Supported software only** — every in-scope OS and application must be vendor-supported and receiving security updates; this single expectation drives most real-world remediation cost.
- **Password and MFA rules** — the requirements document specifies acceptable password constructions, brute-force protections (throttling/lockout), and where MFA is mandatory; the details have shifted across question-set versions (including treatment of passwordless authentication), so read the current document rather than relying on a remembered rule.

## CE vs CE Plus

| | Cyber Essentials | Cyber Essentials Plus |
|---|---|---|
| Method | Online questionnaire, answered by the applicant, **signed off by board level/senior management**, marked by a licensed assessor | Everything in CE, plus an independent technical assessment by an assessor |
| Testing | None (declaration-based) | Typically: external vulnerability scan of internet-facing services, authenticated scans of a **sample of in-scope devices**, checks that malware defenses block test payloads delivered via email and browser, MFA and account-separation verification — exact test spec per the current CE+ Illustrative Test Specification |
| Assurance value | Low — honest-declaration baseline | Moderate — verifies the declaration on sampled systems at a point in time |
| When required | Minimum for many UK public-sector contracts | Required where the buyer demands it (higher-risk contracts, parts of the MOD supply chain, some insurers/customers) |

## Certification process

1. **Choose a licensed certification body** (via IASME's directory) and purchase the assessment; pricing is tiered by organization size.
2. **Download the current question set and requirements document**; build the asset inventory (device types/OS/editions, cloud services) the questionnaire demands.
3. **Answer the questionnaire** in the assessment portal; answers must describe the actual estate, not aspirations.
4. **Board-level/senior sign-off** on the declaration — this is mandatory and makes the submission an organizational attestation, not an IT one.
5. **Marking:** an assessor reviews the answers, may ask clarifications, and passes or fails; failed submissions typically get a short window to remediate and resubmit (verify current allowance).
6. **CE Plus (if pursued):** book the technical assessment with a certification body; it must follow a valid CE pass within the defined window (historically ~3 months). The assessor samples devices per the published sampling rules, runs the test suite, and reports pass/fail.
7. **Certificate issued** (12-month validity) and the organization is listed on the public register; diarize recertification at month 10–11 to avoid a lapse.

## Scope rules (where applicants get burned)

- **Whole organization is the default and the recommendation.** A **sub-set scope** is permitted (e.g., a business unit or network segment) but must be achieved by genuine segregation (network separation/VLAN+firewall), and the certificate states the declared scope — buyers can and do reject narrow scopes. Whole-org certification is also the condition for the bundled cyber-insurance benefit (small UK organizations; modest indemnity — verify current terms).
- **BYOD is in scope** when user-owned devices access organizational data or services (email counts). Devices used only for calls/texts/MFA are the usual carve-out — check current wording.
- **Cloud services are in scope** — IaaS/PaaS/SaaS the organization subscribes to must be included, with responsibility for each control allocated between the organization and the provider; **MFA must be applied to user and admin access to cloud services**.
- **Home and remote workers are in scope**; requirements treat home-worker devices like any other endpoint (home-router boundary responsibilities have shifted between question-set versions — verify current treatment).
- Unsupported operating systems and applications fail certification unless removed or moved into a properly segregated out-of-scope network.
- All in-scope device types (servers, desktops, laptops, tablets, mobiles, virtual/cloud servers) must be declared with OS/edition — inventory gaps surface as assessment friction.

## Question set evolution

The requirements document and question set are versioned under codenames (e.g., "Evendine" 2022, "Montpellier" 2023, "Willow" 2025). Updates have progressively pulled in cloud services, home working, MFA expectations, and clarified terminology (e.g., "security update management," treatment of passwordless authentication). **Always download the current requirements document and question set from IASME/NCSC at engagement start** — answering against a stale set is a common cause of failed or delayed certification. Certification is against the set in force at application time.

## Common failure points

- **Unsupported software** still in use (old Windows builds, out-of-support server OSes, abandoned applications) with no segregation — the most common hard fail.
- **The 14-day update window** not met for applications (browsers and runtimes usually auto-update; line-of-business apps and firmware do not).
- **Missing MFA** on one or more cloud services, especially admin consoles of secondary SaaS and the MSP's own access.
- **Admin account hygiene** — day-to-day work performed on accounts with admin rights, or shared admin credentials.
- **BYOD sprawl** — personal devices accessing corporate email/data that nobody declared and nobody manages.
- **Inventory gaps** — devices or cloud services discovered mid-assessment, forcing rework of answers and scope.
- **CE+ payload tests failing** because malware protection is installed but misconfigured (exclusions too broad, browser download protections off).

## Why it matters

- **UK government procurement:** since 2014, central government contracts involving handling of certain personal/sensitive information or providing certain ICT services have required Cyber Essentials — check the specific contract notice; requirements vary by department.
- **MOD supply chain:** the MOD mandates Cyber Essentials broadly across its suppliers and flows requirements down the chain; higher-risk MOD contracts attract CE+ and additional Defence-specific cyber requirements (Defence Cyber Protection Partnership / DEF STAN-based schemes — evolving, verify current MOD policy).
- **Commercial signaling:** an inexpensive, recognizable trust mark for SMEs; increasingly requested in supplier questionnaires and by insurers (some price or precondition cover on it). For assessing *other* organizations' CE claims, treat the certificate as evidence of baseline hygiene at a point in time, nothing more — see [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md).
- **Threat rationale:** NCSC positions the five controls as blocking the large majority of untargeted, commodity attacks — internet-scanning exploitation, credential stuffing, malware delivery.

## Position among other baselines

| | Cyber Essentials | CIS Controls IG1 | ACSC Essential Eight (ML1) |
|---|---|---|---|
| Nature | Certifiable declaration (CE) / sampled audit (CE+) | Self-directed prioritized safeguards, no certification | Maturity self-assessment (or assessed), no certificate |
| Breadth | 5 technical themes, endpoint/boundary/cloud-access focused | ~56 safeguards incl. inventory, logging basics, awareness, IR basics | 8 strategies, deeper on allow-listing, macros, privileged access, backups |
| Depth of hardening | Low–moderate, binary | Moderate | Higher enforcement bar per strategy |
| Market recognition | Strong in UK procurement | Global, cross-industry | Strong in Australia |

CE is the easiest to evidence externally; CIS ([cis-controls-v8.md](cis-controls-v8.md)) is broader for building an actual program; the Essential Eight ([essential-eight.md](essential-eight.md)) is stricter on the controls it covers. They coexist happily — one control set, mapped (see [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md)).

Related IASME offering: **IASME Cyber Assurance** — a broader governance-inclusive standard sometimes bundled with CE for SMEs; distinct scheme, not NCSC's, and not a CE substitute in procurement — verify buyer requirements name the right scheme.

## Limits

Cyber Essentials is **baseline hygiene, not a security program**. It contains no requirements for governance, risk assessment, security policy, logging and monitoring, incident response, backups, data protection, physical security, secure development, or supplier management. Consequences for practitioners:

- CE/CE+ certification says nothing about detection/response capability or data-handling maturity — do not accept it as a substitute for SOC 2 ([soc2-tsc.md](soc2-tsc.md)) or ISO 27001 ([iso-27001-2022.md](iso-27001-2022.md)) in vendor due diligence for material services.
- For organizations outgrowing CE, the natural next steps are CIS Controls IG1/IG2 ([cis-controls-v8.md](cis-controls-v8.md)) for technical depth, then ISO 27001 or NIST CSF ([nist-csf-2.md](nist-csf-2.md)) for a management system — run the uplift as a structured gap assessment per [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).
- CE+ testing is a sampled point-in-time check, not a penetration test; do not represent it as one.

## Using this in assessments

- **Start from the device and cloud-service inventory.** Most CE friction is discovering unmanaged BYOD, forgotten SaaS, and unsupported OS builds during the application. An accurate asset list answers half the questionnaire.
- **Check the 14-day update SLA honestly.** It applies to high/critical updates across OS *and* applications on all in-scope devices, including mobiles and BYOD — organizations without patch tooling and rings rarely meet it in practice; test evidence per [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
- **MFA on every cloud service** (admin and user) is the single most common late-breaking gap — enumerate services first, including shadow SaaS.
- **Scope declarations:** if a sub-set scope is used, verify segregation technically and make sure the certificate wording matches what the buyer requires — mismatch discovered at contract award is expensive.
- **Recertify against the current question set** — treat the annual cycle as a regression test; question-set changes can turn last year's pass into this year's gap.
- **CE+ device sampling is not exhaustive** — when relying on someone else's CE+ certificate, remember only a sample of devices was tested; ask how the estate is kept uniform (MDM/baseline enforcement) if the service is material.
- **Managed service providers:** where an MSP administers the estate, their access routes and admin accounts fall inside the applicant's answers — get the MSP's cooperation (and their own certification status) confirmed before starting.
- **Evidence reuse:** CE answers map cleanly onto supplier questionnaires and onto CIS IG1 evidence — capture artifacts (firewall configs, patch reports, MFA coverage exports) once, in a reusable evidence library, per [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md).
- UK regulatory context (UK GDPR, NIS Regulations, the evolving Cyber Security and Resilience Bill) is separate from this scheme — see [../regulations/other-jurisdictions.md](../regulations/other-jurisdictions.md). CE certification is neither necessary nor sufficient for UK GDPR "appropriate technical and organisational measures," though the ICO views it favorably as baseline evidence.

## References

- Related frameworks: [cis-controls-v8.md](cis-controls-v8.md), [iso-27001-2022.md](iso-27001-2022.md), [nist-csf-2.md](nist-csf-2.md), [soc2-tsc.md](soc2-tsc.md)
- Regulations: [../regulations/other-jurisdictions.md](../regulations/other-jurisdictions.md) (UK section)
- Crosswalks: [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md)
- Skills: [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md), [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md), [../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md), [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md)

## Primary sources

- [NCSC Cyber Essentials overview (requirements, question sets)](https://www.ncsc.gov.uk/cyberessentials/overview)
- [IASME (certification delivery partner)](https://iasme.co.uk)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
