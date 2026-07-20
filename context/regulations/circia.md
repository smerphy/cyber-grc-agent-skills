# CIRCIA — Cyber Incident Reporting for Critical Infrastructure Act (2022)

## At a glance

| Item | Detail |
|---|---|
| Jurisdiction | United States, federal |
| Instrument | Statute (enacted March 2022 as part of the Consolidated Appropriations Act, 2022; codified at 6 U.S.C. § 681 et seq.), implemented through CISA rulemaking |
| Status | **Statute in force, but reporting obligations attach only under the final rule.** CISA published the notice of proposed rulemaking (NPRM) in April 2024; the statutory deadline for the final rule fell in late 2025. As of this writing, confirm whether the final rule has been issued, what changed from the proposal, and when compliance dates begin — do not assume anything below survived unchanged |
| Regulator | CISA (Cybersecurity and Infrastructure Security Agency), within DHS |
| Applies to | "Covered entities" in the 16 critical infrastructure sectors, per size and sector-based criteria defined in the rule (proposal summarized below) |
| Core duties | Report covered cyber incidents within **72 hours**; report ransom payments within **24 hours**; file supplemental reports; preserve supporting data |
| Penalties | No direct civil monetary penalty for non-reporting; enforcement runs through requests for information, **subpoenas**, referral to the Attorney General for civil action, contempt, and false-statement exposure; the proposal also contemplated acquisition-related consequences for federal contractors |

## Read this first: statute vs. rule

CIRCIA is a statute that ordered a rulemaking. The reporting duties described here **do not bind anyone until the final rule's compliance dates arrive**. The sequence:

- **March 2022:** CIRCIA enacted, directing CISA to define covered entities, covered incidents, and reporting mechanics.
- **April 2024:** CISA issued a lengthy NPRM proposing the definitions and procedures below, drawing extensive industry comment (particularly on breadth of coverage and overlap with existing regimes).
- **Late 2025:** statutory deadline for the final rule (18 months after the NPRM). Public reporting during 2025 indicated timeline pressure and possible slippage.
- **As of mid-2026:** verify the current state directly — check CISA's CIRCIA page and the Federal Register for the final rule, its effective date, and its compliance date. Everything in this note that describes "the rule" describes **the proposal** unless you have confirmed the final text.

Treat the NPRM as a preview of the likely shape, not as the law. Where the final rule exists, it controls.

## Covered entities (as proposed)

The NPRM proposed covering an entity in any of the **16 critical infrastructure sectors** (as defined under PPD-21: chemical, commercial facilities, communications, critical manufacturing, dams, defense industrial base, emergency services, energy, financial services, food and agriculture, government facilities, healthcare and public health, information technology, nuclear, transportation, water/wastewater) that meets **either**:

1. A **size-based criterion** — the entity exceeds the SBA small business size standard for its industry; or
2. One of a long list of **sector-based criteria** regardless of size — e.g., owners/operators of covered chemical facilities, certain communications providers, critical manufacturing entities, defense contractors meeting specified conditions, financial services entities already subject to certain regulators, hospitals above a bed threshold, large school districts, certain water systems, and others.

Practical consequences of the proposed design:

- Coverage is entity-level, not incident-level: once covered, all of the entity's covered cyber incidents are reportable, not just those touching critical infrastructure functions.
- Many organizations that do not think of themselves as "critical infrastructure" (mid-size manufacturers, healthcare groups, IT companies) would be covered via the size test alone.
- CISA estimated coverage in the hundreds of thousands of entities. Expect the final rule to adjust these criteria; re-run your scoping analysis against the final text.

## What must be reported (as proposed)

**Covered cyber incident — report within 72 hours** after the covered entity **reasonably believes** the incident occurred. A "substantial cyber incident" was proposed to include incidents causing any of:

- Substantial loss of confidentiality, integrity, or availability of a covered entity's information system or network;
- Serious impact on the safety and resiliency of operational systems and processes;
- Disruption of ability to engage in business or industrial operations, or deliver goods or services;
- Unauthorized access enabled by a compromise of a cloud service provider, managed service provider, other third party, or a **supply chain compromise**.

Proposed exclusions: lawfully authorized activity (e.g., government action), good-faith security research or pentesting authorized by the owner/operator, and mere threats or vulnerabilities without impact.

**Ransom payment — report within 24 hours** of the payment being made. This applies **even if the underlying incident is not itself a covered cyber incident**, and applies when a third party (insurer, negotiator) makes the payment on the entity's behalf — the covered entity still owes the report. A combined incident-plus-payment report is permitted when both duties arise together.

**Supplemental reports** — promptly (proposed: without delay, and CISA suggested within 24 hours of discovery) when **substantial new or different information** becomes available, and when a ransom payment is made after an initial incident report, until the entity notifies CISA the incident is resolved and closed.

**Preservation** — preserve data and records relevant to the incident or payment (forensic images, logs, ransom demand and payment records, comms with the actor) for a proposed period of **two years** from the final report submitted.

Reports go through a CISA web portal, with report content requirements enumerated in the rule (identity/contact, description, vulnerabilities exploited, TTPs, indicators, impact, responders engaged, and for ransom payments the demand, instructions, and amount).

## Protections and enforcement

**Protections for reports** (statutory, so relatively stable): CIRCIA reports are exempt from FOIA, cannot be used as the sole basis for regulatory enforcement against the reporting entity, are not subject to discovery or admissible in most litigation arising from reported activity, and submitting a report does not waive privilege. Liability protection attaches to the act of reporting — it is not an amnesty for the underlying security failures.

**Enforcement for non-reporting:** CISA may issue a **request for information** if it believes an entity failed to report, then a **subpoena**; noncompliance can be referred to the **Attorney General** for civil enforcement (contempt), and information obtained via subpoena loses some of the protections voluntary reports enjoy — an intentionally uncomfortable asymmetry. False statements in reports carry criminal exposure under 18 U.S.C. § 1001. The NPRM also floated suspension/debarment referrals for federal contractors. There is no private right of action.

## Overlap with existing reporting regimes

CIRCIA lands on top of a crowded field. The statute anticipates this with a **substantially similar reporting exception**: a covered entity that reports substantially similar information in a substantially similar timeframe to another federal agency does not owe a duplicate CIRCIA report, **provided** a CIRCIA Agreement (an information-sharing agreement between CISA and that agency) is in place. Track which agencies have executed such agreements once the rule is final — the exception only works where the agreement exists.

Regimes to reconcile:

- **SEC 8-K Item 1.05** — different trigger (investor materiality vs. substantial incident), different clock (4 business days from materiality determination vs. 72 hours from reasonable belief), different audience. Both can apply to one incident; neither substitutes for the other. See [sec-cyber-disclosure.md](sec-cyber-disclosure.md).
- **Banking regulators' 36-hour notification rule** (OCC/FRB/FDIC, for banking organizations) — faster clock, narrower audience; a prime candidate for the substantially-similar exception. See [glba-ftc-safeguards.md](glba-ftc-safeguards.md) for the broader financial-sector stack.
- **Sector rules** — NERC CIP reporting for the bulk electric system ([../frameworks/nerc-cip.md](../frameworks/nerc-cip.md)), TSA security directives (pipeline/rail/aviation), HHS/OCR breach notification ([hipaa.md](hipaa.md)), NYDFS 72-hour notice ([nydfs-500.md](nydfs-500.md)), and state breach laws ([us-state-privacy.md](us-state-privacy.md)) all continue to apply on their own terms.
- Federal contractors and agencies live under a separate stack entirely — see [fisma.md](fisma.md).

Map every clock you are subject to in [../crosswalks/breach-notification-timelines.md](../crosswalks/breach-notification-timelines.md).

## What to do while the rule finalizes

The cheapest time to build the reporting muscle is before the deadline exists:

1. **Scope now:** run the proposed covered-entity criteria against your org (sector + SBA size standard + sector-specific triggers) and record the conclusion; refresh when the final rule publishes.
2. **Draft the report template:** the NPRM's content list is a reasonable bet for the final form; wire it into the IR plan so the 72-hour report is an assembly job, not an authoring job.
3. **Instrument the ransom path:** the 24-hour payment clock is unforgiving and third-party payments count — insurers and negotiators must be contractually obligated to tell you immediately when payment occurs.
4. **Fix preservation:** confirm log retention and forensic-artifact preservation can span two years from final report; most default retention settings cannot.
5. **Assign the trigger decision:** "reasonable belief that a covered cyber incident occurred" needs a named decider and a documented decision log, exactly like the SEC materiality determination.
6. **Track CIRCIA Agreements:** once final, inventory which of your existing reports can satisfy CIRCIA via the exception, and which cannot.

See [../../skills/incident-regulatory-reporting/SKILL.md](../../skills/incident-regulatory-reporting/SKILL.md) for the operational reporting procedure.

## Key obligations for security/GRC teams

1. Determine and document covered-entity status against the final rule when issued; re-check after M&A or growth past SBA size thresholds.
2. Implement the 72-hour incident and 24-hour ransom-payment clocks in the IR plan, with the supplemental-report loop through incident closure.
3. Preserve incident data and payment records for the required period; pre-approve a legal-hold-style preservation checklist for cyber incidents.
4. Negotiate immediate-notification duties into insurer, negotiator, MSP, and MSSP contracts (both for payments they make and incidents they detect).
5. Reconcile CIRCIA with every other reporting regime you face and identify where the substantially-similar exception can collapse duplicate work.
6. Do not report through informal channels and assume it counts — only the mechanism specified in the final rule discharges the duty.

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
