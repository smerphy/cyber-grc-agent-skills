# NIST SP 800-171 and CMMC 2.0 — Protecting CUI in the Defense Supply Chain

## At a glance

| Attribute | Detail |
|---|---|
| Publisher | NIST publishes SP 800-171; U.S. Department of Defense (DoD) runs CMMC |
| Current revisions | SP 800-171 Rev. 2 (Feb 2020) and Rev. 3 (final May 2024) both in circulation — contracts specify which applies; CMMC 2.0 codified at 32 CFR Part 170 |
| Full titles | SP 800-171: Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations; CMMC: Cybersecurity Maturity Model Certification |
| Structure | 800-171 r2: 110 security requirements in 14 families; CMMC 2.0: three levels (L1/L2/L3) layered on FAR 52.204-21, 800-171, and 800-172 |
| Assessment guides | SP 800-171A (r2 and r3 editions); DoD Assessment Methodology (SPRS scoring); CMMC Assessment Guides per level |
| Certifiable? | CMMC L2 (C3PAO) and L3 (government-led DIBCAC) yield certificates; 800-171 alone is self-attested via SPRS |
| Legal anchor | DFARS 252.204-7012, -7019, -7020, -7021; FAR 52.204-21 for FCI |
| Who it applies to | DoD contractors and subcontractors handling FCI or CUI — flows down the entire supply chain |
| Cost/licensing | NIST documents free; CMMC assessments are paid engagements with C3PAOs |

## Why this framework pair exists

**Controlled Unclassified Information (CUI)** is government information that is sensitive but not classified — technical drawings, export-controlled data, procurement-sensitive material — that routinely lives on *contractor* systems. SP 800-171 defines the security requirements for protecting CUI in nonfederal systems; it is the 800-53 Moderate baseline with federal-specific and non-confidentiality material removed (see [nist-800-53.md](./nist-800-53.md)).

The problem CMMC solves is assurance: for years, DFARS 252.204-7012 required 800-171 compliance on a purely self-attested basis, and DoD assessments found widespread non-implementation. CMMC adds a verification layer — self-assessment with executive affirmation at the low end, third-party or government certification at the high end — as a **condition of contract award**.

## The DFARS clause stack

Four clauses do the work; expect to see them together in defense contracts:

| Clause | What it requires |
|---|---|
| DFARS 252.204-7012 | Implement SP 800-171 on covered contractor systems; report cyber incidents to DoD within 72 hours; preserve images/logs; flow the clause down to subcontractors. The foundational clause since 2017. |
| DFARS 252.204-7019 | Before award, the contractor must have a current (within 3 years) SP 800-171 self-assessment score posted in **SPRS** (Supplier Performance Risk System). |
| DFARS 252.204-7020 | Contractor must give the government access for Medium/High assessments and flow the SPRS requirement down to subs handling CUI. |
| DFARS 252.204-7021 | The CMMC clause: contractor must hold the CMMC level specified in the contract at time of award and maintain it for the life of the contract; flows down to subcontractors at the level appropriate to the information they handle. |

Separately, **FAR 52.204-21** (Basic Safeguarding of Covered Contractor Information Systems) defines 15 basic safeguarding requirements for **Federal Contract Information (FCI)** — the substrate for CMMC Level 1. Note the counting quirk: the 15 FAR requirements are commonly decomposed into **17 practices** in older CMMC 1.0 material; CMMC 2.0 Level 1 documentation describes them as 15 requirements mapping to 17 practices. Cite the FAR clause, not a practice count, when precision matters.

## SP 800-171 Rev. 2 vs Rev. 3

**Rev. 2** (the version CMMC Level 2 is currently anchored to) contains **110 security requirements in 14 families**:

Access Control, Awareness and Training, Audit and Accountability, Configuration Management, Identification and Authentication, Incident Response, Maintenance, Media Protection, Personnel Security, Physical Protection, Risk Assessment, Security Assessment, System and Communications Protection, System and Information Integrity.

Requirements are numbered `3.x.y` (e.g., `3.1.1` account authorization, `3.5.3` MFA, `3.13.11` FIPS-validated cryptography). Rev. 2 splits requirements into "basic" (from FIPS 200) and "derived" (from 800-53) — a distinction that matters for SPRS scoring weights.

**Rev. 3** (final May 2024):

- Realigned to 800-53 **Rev. 5** control language and introduced **organization-defined parameters (ODPs)**, some of which DoD is expected to pre-populate — verify current DoD ODP values before assessing against r3.
- Restructured the families to add organization-level ones (Planning, System and Services Acquisition, Supply Chain Risk Management), bringing the family count to 17.
- Changed the requirement count — fewer top-level requirements than r2's 110, achieved partly by consolidation, though many contain more embedded specificity. Verify the exact count against the official text; do not quote "110" for r3.
- Has its own assessment procedures in SP 800-171A Rev. 3.

**Which one applies?** The contract clause decides. DFARS -7012 historically pointed at "the version in effect at time of solicitation," and the CMMC program rule anchored Level 2 to Rev. 2. DoD signaled a class deviation keeping Rev. 2 in effect pending CMMC transition to r3. Always check the clause text and any class deviations in force — do not assume r3 applies just because it is the newest revision.

## SPRS self-assessment scoring

The **DoD Assessment Methodology** turns an 800-171 r2 self-assessment into a single score posted to SPRS:

- Start at **110** (one point per requirement, fully implemented = perfect score).
- Deduct a **weighted value for each unimplemented requirement**: most are 1 point, but high-impact ones deduct **3 or 5 points** (e.g., MFA and FIPS crypto requirements carry 5-point weights — verify weights against the current methodology annex).
- Because deductions exceed one point, the floor is **negative** (the scale runs to -203).
- Two requirements (security plan `3.12.4` and POA&M `3.12.2`) cannot be scored as "on a POA&M" — no SSP means the assessment cannot be completed at all.
- The score, assessment date, scope, and the date you expect to reach 110 are entered in SPRS. Assessments come in **Basic** (self), **Medium**, and **High** (DIBCAC-conducted) confidence levels.

Practical note: primes increasingly ask subcontractors for their SPRS score during onboarding — treat it as a due-diligence artifact in third-party reviews ([../../skills/third-party-risk-assessment/SKILL.md](../../skills/third-party-risk-assessment/SKILL.md)).

## CMMC 2.0 — the three levels

| Level | Basis | Assessment | Cadence |
|---|---|---|---|
| **Level 1 (Foundational)** | FAR 52.204-21 basic safeguarding practices; protects **FCI** | Annual **self-assessment** + affirmation by a senior official in SPRS | Annual |
| **Level 2 (Advanced)** | The 110 requirements of SP 800-171 Rev. 2; protects **CUI** | Either triennial **self-assessment** or triennial **C3PAO certification assessment** — *the contract specifies which*; annual affirmation either way | 3-year cert, annual affirmation |
| **Level 3 (Expert)** | Level 2 plus a **subset of SP 800-172** enhanced requirements (24 selected requirements per the program rule — verify count against 32 CFR 170) | **Government-led** assessment by DIBCAC; requires a prior L2 C3PAO certification | 3-year, annual affirmation |

Key structural points:

- CMMC 2.0 eliminated the 1.0 maturity levels 2 and 4 and dropped the 1.0-era "process maturity" and CMMC-unique practices — Level 2 is now *exactly* 800-171 r2, which is why an honest SPRS self-assessment is the best predictor of C3PAO readiness.
- DoD determines the required level per procurement; most CUI-handling contracts are expected to require **L2 with C3PAO certification**, with self-assessment L2 reserved for a smaller set of non-prioritized acquisitions.
- **C3PAOs** (CMMC Third-Party Assessment Organizations) are accredited by the CMMC Accreditation Body (the Cyber AB); assessors are individually certified (CCP/CCA).

## POA&Ms under CMMC — deliberately narrow

Unlike FedRAMP-style open-ended POA&M management, CMMC allows Plans of Action and Milestones only under tight conditions:

- Permitted at **Level 2** (and conditionally at L3), **not at Level 1**.
- Only certain lower-weighted requirements may be on a POA&M — the highest-weighted (5-point) requirements generally may not, with limited exceptions defined in the rule.
- A **minimum score** is required to receive a conditional status: for L2, at least **0.8 × 110 = 88** on the SPRS methodology.
- All POA&M items must be **closed out within 180 days** of the assessment, verified by a closeout assessment; otherwise the conditional certification expires.
- Verify the exact eligible-requirement list against 32 CFR 170 before advising — the details are rule text, not guidance.

This is a materially stricter regime than most certifications: treat "we'll POA&M it" as a non-answer for high-weight requirements.

## The CMMC rules and phased rollout

Two rulemakings implement CMMC — keep them straight:

- **32 CFR Part 170** (the *program* rule): defines the CMMC model, levels, assessment and affirmation requirements, POA&M rules, and ecosystem roles. Published as a final rule in October 2024, effective December 2024.
- **48 CFR** (the *acquisition* rule, DFARS case 2019-D041): amends the DFARS to put CMMC requirements (clause 252.204-7021) into solicitations and contracts. Finalized in 2025; its effective date starts the contractual clock.

Rollout is **phased over roughly three years** from the 48 CFR effective date: early phases rely mostly on self-assessments (L1 and L2 self), later phases introduce C3PAO-certified L2 as a condition of award, then L3, then CMMC in effectively all applicable DoD solicitations. The phase boundaries, dates, and program-office discretion to accelerate requirements are specified in the rules and have shifted during rulemaking — **verify the current phase and dates against the official rule text and DoD CIO guidance before advising on timelines**.

## Who is in scope, and flow-down

- Anyone in the **DoD supply chain** touching FCI or CUI: primes, subcontractors, and suppliers at any tier — including small machine shops, SaaS tools processing CUI, and MSPs/MSSPs whose services are in scope of a client's assessment.
- Requirements **flow down**: primes must impose the appropriate CMMC level on subs based on the information the sub actually receives (a sub handling only FCI needs L1, not the prime's L2).
- **Cloud services** holding CUI must meet FedRAMP Moderate or equivalency under DFARS -7012(b)(2)(ii)(D) — see [fedramp.md](./fedramp.md). DoD memos define what "equivalency" requires; verify current guidance.
- **Scoping** is its own discipline: CUI enclaves, asset categories (CUI assets, security protection assets, contractor risk-managed assets, specialized assets, out-of-scope assets per the L2 scoping guide), and ESP/MSP treatment drive assessment cost more than any control does.

## Using this in assessments

- **Fix the coordinates first:** which revision (r2 vs r3), which CMMC level, self vs C3PAO, and the assessment scope/enclave boundary. Everything downstream depends on these four answers. See [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md).
- **Use 800-171A objectives, not just requirements:** every requirement decomposes into assessment objectives in SP 800-171A, and CMMC assessors score at the objective level — a requirement is NOT MET if any objective is unmet. Gap assessments that only track the 110 top-level requirements systematically overstate readiness. See [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md).
- **The SSP is the anchor artifact:** no SSP, no score, no assessment. Start there, then evidence per objective.
- **Watch the classic killers:** FIPS-validated (not just FIPS-compatible) cryptography, MFA coverage for all users including local/privileged, flow-down gaps at sub-tier suppliers, and MSP/cloud tools silently pulling CUI out of the defined boundary.
- **Reading vendor claims:** "CMMC compliant" is not a status before certification phases begin — ask for the SPRS score and date, the scope statement, and (when applicable) the C3PAO certificate and level.
- Map once, reuse: because L2 *is* 800-171 r2, and r2 derives from the 800-53 Moderate baseline, crosswalks through 800-53 are reliable — see [../crosswalks/framework-crosswalk.md](../crosswalks/framework-crosswalk.md) and [../../skills/control-mapping/SKILL.md](../../skills/control-mapping/SKILL.md).

## References

- Related frameworks: [nist-800-53.md](./nist-800-53.md) (parent catalog), [fedramp.md](./fedramp.md) (cloud services holding CUI), [nist-csf-2.md](./nist-csf-2.md)
- Skills: [../../skills/framework-gap-assessment/SKILL.md](../../skills/framework-gap-assessment/SKILL.md), [../../skills/control-testing/SKILL.md](../../skills/control-testing/SKILL.md), [../../skills/audit-preparation/SKILL.md](../../skills/audit-preparation/SKILL.md)

## Primary sources

- [NIST SP 800-171 Rev. 3 — official publication](https://csrc.nist.gov/pubs/sp/800/171/r3/final)
- [DoD CIO CMMC program site (rules, scoping and assessment guides)](https://dodcio.defense.gov/cmmc/)

*Links verified 2026-07; if one has moved, search the publisher's site for the identifier.*

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
