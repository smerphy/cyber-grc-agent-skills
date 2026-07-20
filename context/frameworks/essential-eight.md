# ACSC Essential Eight — Australian Baseline Mitigation Strategies

## At a glance

| Attribute | Detail |
|---|---|
| Owner | Australian Cyber Security Centre (ACSC), part of the Australian Signals Directorate (ASD) |
| What it is | Eight prioritized mitigation strategies drawn from ASD's broader *Strategies to Mitigate Cyber Security Incidents*, plus a maturity model for implementing them |
| Current version | The Essential Eight Maturity Model is updated periodically (a significant update landed **November 2023**); always pull the current model from cyber.gov.au — there is no version number scheme like ISO editions |
| Structure | 8 mitigation strategies × 4 maturity levels (ML0–ML3); requirements defined per strategy per level |
| Certifiable? | No formal certification scheme. Assessments follow the ACSC *Essential Eight Assessment Process Guide*; Australian government entities self-assess/report, and IRAP assessors commonly evaluate it |
| Mandate | Effectively mandatory for Australian federal **non-corporate Commonwealth entities** under the Protective Security Policy Framework (PSPF) — see below and **verify current PSPF release**; voluntary but widespread in AU private sector; referenced by SOCI CIRMP rules, insurers, and contracts |
| Platform focus | Written primarily for **Microsoft Windows internet-connected networks**; ACSC notes it may not directly translate to cloud-native, mobile, or OT environments |
| Typical use | Baseline hardening target for AU organizations; contractual/insurance evidence; the "cyber framework" option in SOCI risk-management programs |

## The eight mitigation strategies

Grouped by intent (prevent attacks, limit extent, recover):

1. **Application control** — allow-listing of executables, software libraries, scripts, installers, compiled HTML, HTML applications, and control panel applets on workstations and servers; only approved code runs.
2. **Patch applications** — timely patching/updating of internet-facing services and workstation applications (browsers, office suites, PDF readers, email clients), driven by vulnerability scanning; remove unsupported applications.
3. **Configure Microsoft Office macro settings** — block macros from the internet, allow only vetted/signed macros for users with a demonstrated business need, prevent users from changing settings.
4. **User application hardening** — disable or remove risky functionality: internet-facing Java, web browser ad/Java processing, Internet Explorer 11, unneeded features in Office/PDF readers; harden browser settings.
5. **Restrict administrative privileges** — validate need on request and revalidate periodically; separate privileged and unprivileged accounts and operating environments; privileged accounts blocked from internet/email/web browsing.
6. **Patch operating systems** — timely patching of internet-facing and internal OSes driven by scanning; replace unsupported OS versions.
7. **Multi-factor authentication** — MFA for remote access, for privileged users, for important data repositories, and for users of internet-facing and third-party services; higher levels push toward **phishing-resistant** MFA.
8. **Regular backups** — backups of important data, software, and configuration performed and retained per business criticality; restoration tested; backups protected from modification/deletion, with privileged access restrictions.

The exact per-strategy requirements differ materially at each maturity level — quote the current model, not this summary, when writing findings.

## Maturity model (ML0–ML3)

Levels are defined against **increasing adversary tradecraft**, not simply "more controls":

| Level | Rough meaning |
|---|---|
| ML0 | Weaknesses exist that undermine the intent of the strategy — not aligned even with ML1 |
| ML1 | Mitigates adversaries using widely available commodity tradecraft and opportunistic targeting |
| ML2 | Mitigates adversaries with modestly more capability who invest in targeting (e.g., better phishing, credential attacks, defeating weak MFA) |
| ML3 | Mitigates more adaptive adversaries who exploit gaps in tooling coverage and focus on particular targets; assumes better logging, faster patching, stricter allow-listing |

Key operating rules:

- **Implement as a package.** ACSC guidance is to reach the *same* maturity level across all eight strategies before advancing any of them — the strategies complement each other, and an overall posture is only as strong as the weakest strategy. An organization's Essential Eight maturity is generally reported as the lowest level achieved across the eight.
- Levels build cumulatively: ML2 includes ML1 requirements, ML3 includes ML2.
- ACSC recommends a **risk-based target**: most organizations target ML2; entities facing more capable adversaries or holding more sensitive data target ML3. ML3 does not claim to stop top-tier state actors.
- The **November 2023 update** tightened several areas — themes included stronger emphasis on phishing-resistant MFA, faster patching expectations for exploited/critical vulnerabilities (48-hour language for the most urgent cases), governance of privileged access, and incident detection/response and reporting hooks. Specific wording and timeframes changed per level — **verify against the current published model** before citing exact requirements.

## Illustrative deltas across maturity levels

Exact requirements per level change with model updates — the table below shows the *shape* of escalation for four high-friction strategies (paraphrased; quote the current model for findings):

| Strategy | ML1 flavor | ML2 flavor | ML3 flavor |
|---|---|---|---|
| Application control | Enforced on workstations for executables/libraries/scripts/installers in user profiles | Extends coverage (servers, more file types) and requires centralized event logging of blocked executions | Vendor-recommended block rules (e.g., driver/LOLBin rulesets), annual ruleset validation, protected and monitored logs |
| Patch applications | Internet-facing services patched fast (within two weeks; faster when exploits exist); regular scanning | Tighter timeframes and broader application coverage | Shortest timeframes for exploited vulnerabilities (48-hour language for the most urgent cases) and removal of unsupported software |
| MFA | MFA for internet-facing services and third-party services holding org data | MFA for privileged users and more internal cases; stronger factor requirements | Phishing-resistant MFA broadly, including for important data repositories |
| Restrict admin privileges | Requests validated; privileged accounts blocked from internet/email/web | Privileged access management practices (e.g., separate privileged environments, time-limited access) and logging | Just-in-time style administration, stricter separation, comprehensive privileged-event monitoring |

Treat these as orientation only — the November 2023 update moved several requirements between levels.

## Mandate status

- **Federal government:** under the PSPF, non-corporate Commonwealth entities are directed to implement the Essential Eight, with Maturity Level 2 commonly cited as the required baseline, and to report maturity annually (ASD cyber security surveys / PSPF reporting). The PSPF was restructured (2024 release) and mandate wording has shifted over time — **verify the current PSPF release and any Direction text** before advising a Commonwealth entity. Corporate Commonwealth entities and state/territory governments have separate (often similar) policies.
- **SOCI Act:** the Critical Infrastructure Risk Management Program rules accept the Essential Eight (at a specified maturity level) as one of the recognized cyber frameworks — see [../regulations/other-jurisdictions.md](../regulations/other-jurisdictions.md) for the SOCI regime itself.
- **Private sector:** no general statutory mandate, but the Essential Eight is the de facto AU baseline — commonly required in government supply-chain contracts, requested by cyber insurers, and used by boards as the reporting yardstick.
- **APRA-regulated entities:** CPS 234 does not mandate the Essential Eight, but APRA has repeatedly benchmarked regulated entities against it and expects banks/insurers/super funds to measure themselves against it as part of demonstrating CPS 234 information-security capability. Treat CPS 234 as the enforceable obligation and the Essential Eight as a common evidence baseline underneath it.

## Relationship to the ISM

The **Information Security Manual (ISM)** is ACSC's full control catalogue (used with IRAP assessments for government systems). The Essential Eight is a prioritized subset/overlay: ACSC publishes a mapping from each Essential Eight maturity-level requirement to ISM control identifiers. Practical implications:

- If a client is already ISM/IRAP-scoped (government cloud, hosting, defence supply chain), assess the Essential Eight *through* the ISM mapping rather than as a separate exercise.
- For everyone else, the Essential Eight stands alone as the assessment target and the ISM serves as implementation detail.

## Position among other baselines

- **CIS Controls** ([cis-controls-v8.md](cis-controls-v8.md)): the Essential Eight roughly corresponds to a hardened subset of IG1/IG2 technical safeguards, with stricter enforcement expectations (allow-listing rather than inventory-first). Organizations reporting to US customers often map E8 evidence onto CIS.
- **NIST CSF** ([nist-csf-2.md](nist-csf-2.md)): E8 sits almost entirely in Protect, with slivers of Identify (asset/patch scanning) and Recover (backups) — it is not a CSF substitute.
- **ISM/IRAP:** for Australian government work, the ISM is the authoritative catalogue and IRAP the assessment mechanism; the Essential Eight is the prioritized floor within it.
- Mapping across these belongs in a maintained crosswalk — see [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md) and [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).

## Assessment approach

ACSC publishes an **Essential Eight Assessment Process Guide** covering evidence quality, testing methods, and per-strategy assessment techniques. Practitioner notes:

- Assessment is **binary per requirement at each level** — partial credit is not averaged up. A single unmet requirement caps the strategy at the lower level, and the weakest strategy caps the package.
- Prefer **technical testing over attestation**: run allow-list bypass tests for application control, query patch/vulnerability data for patching strategies, inspect actual GPO/MDM/IdP configuration for macros, hardening, and MFA, and perform test restores for backups.
- **Common failure points:**
  - *Application control scoping* — allow-listing only .exe files while scripts, installers, and DLLs run freely; enforcing on workstations but not servers; user-writable paths allowed; audit-mode-only deployments claimed as enforcement.
  - *Patching* — measuring deployment rather than confirmed installation; missing internet-facing service inventory; unsupported software retained "temporarily."
  - *MFA* — push-based or SMS MFA where the level demands phishing-resistant methods; break-glass accounts excluded without compensating controls; third-party SaaS out of scope.
  - *Privileged access* — admin accounts that can browse the web/read email; shared local admin passwords (no LAPS-equivalent); revalidation never performed.
  - *Backups* — untested restores; backup infrastructure administrable from the same accounts an attacker would compromise.
- Cloud/SaaS-heavy estates need interpretation: several requirements assume on-prem Windows. Document interpretation decisions explicitly in the assessment.

## Reporting and governance

- Report results as a **matrix**: eight strategies × achieved level, with the package level (the minimum) called out, the declared target level, and dated evidence per requirement.
- Maturity claims decay fast — patching and MFA posture drift within months. Recommend re-assessment at least annually, and continuous measurement (patch SLAs, allow-list block events, MFA coverage) as ongoing metrics; see [../../skills/grc-metrics-reporting/SKILL.md](../../skills/grc-metrics-reporting/SKILL.md).
- Where a requirement genuinely cannot be met (legacy OT, vendor-locked systems), document a risk-accepted exception with compensating controls rather than silently scoping it out — per [../../skills/exception-management/SKILL.md](../../skills/exception-management/SKILL.md). Note that under the model, unmet requirements still cap the maturity level regardless of internal risk acceptance.

## Using this in assessments

- **Fix the target level first.** Agree ML1/ML2/ML3 with the client based on threat profile and any mandate (PSPF, SOCI CIRMP, contracts) before testing — findings are only meaningful against a declared target. Structure the work per [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md) and test controls per [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
- **Report per-strategy maturity plus the package level.** Boards want the single number; remediation owners need the per-strategy, per-requirement gap list.
- **Don't oversell coverage.** The Essential Eight is endpoint/AD-centric baseline hardening — it does not cover governance, risk management, third-party risk, detection/response depth, or data protection. Pair it with ISO 27001 ([iso-27001-2022.md](iso-27001-2022.md)) or NIST CSF ([nist-csf-2.md](nist-csf-2.md)) for program-level assessments; it overlaps heavily with the technical safeguards in CIS Controls IG1/IG2 ([cis-controls-v8.md](cis-controls-v8.md)).
- **Regulatory context:** breach notification and APRA/SOCI reporting clocks sit in the Australian regulatory regime, not this framework — see [../regulations/other-jurisdictions.md](../regulations/other-jurisdictions.md) and [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md).
- **Common pitfall:** clients claiming "Essential Eight compliant" with no declared maturity level or with levels averaged across strategies — always ask "which level, per strategy, assessed how, when."

## References

- Related frameworks: [cis-controls-v8.md](cis-controls-v8.md), [nist-csf-2.md](nist-csf-2.md), [iso-27001-2022.md](iso-27001-2022.md)
- Regulations: [../regulations/other-jurisdictions.md](../regulations/other-jurisdictions.md) (Australia: Privacy Act NDB, APRA CPS 234, SOCI Act)
- Crosswalks: [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md)
- Skills: [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md), [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md), [../../skills/regulatory-applicability/SKILL.md](../../skills/regulatory-applicability/SKILL.md)

## Primary sources

- [ACSC — Essential Eight and the Information Security Manual (cyber.gov.au)](https://www.cyber.gov.au)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
