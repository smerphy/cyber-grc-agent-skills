---
name: ropa-data-mapping
description: >-
  Builds and maintains Records of Processing Activities under GDPR Art. 30 and
  the underlying data map — inventorying processing across business functions,
  capturing the required fields per record, mapping system-to-system and
  cross-border data flows, and reusing one inventory across multiple privacy
  regimes. Use when a user says "RoPA", "Article 30 record", "data map",
  "data inventory", "processing register",
  or asks what personal data the organization holds and where it flows.
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Produce a RoPA that survives regulator scrutiny and stays current: decide which record perspective(s) the organization owes (controller Art. 30(1), processor Art. 30(2), or both), discover the processing activities that actually exist — not just the ones people remember — capture every required field per record, draw the data flow map underneath the records, wire lawful-basis assignment into the DPIA process instead of duplicating it, and set the triggers that keep the inventory alive.

The same inventory then serves as the single source for US state data inventories, Quebec Law 25, LGPD, and other regimes' mapping obligations — one inventory, multiple views. The RoPA is also the foundation artifact for most other privacy work: DPIAs, transfer assessments, retention schedules, subject-rights fulfilment, and breach scoping all start from "what do we hold, why, and where does it flow" — which is exactly what this skill produces.

## When to use

- The organization needs to create a GDPR Art. 30 RoPA for the first time, or an existing RoPA is stale, incomplete, or was inherited from a template nobody verified.
- A data map or data inventory is needed as the foundation for other privacy work: DPIAs, transfer assessments, retention schedules, subject-rights fulfilment, breach scoping, or US state privacy law data inventories (see [../../context/regulations/us-state-privacy.md](../../context/regulations/us-state-privacy.md)).
- A trigger event fired: new system or vendor, new processing purpose, market entry, M&A due diligence or integration, or a supervisory authority asked for the RoPA (they can, under Art. 30(4), and typically expect it within days).
- A customer, prospect, or auditor asks for evidence of the data inventory as part of due diligence — an export-ready RoPA is the standard answer.
- **Not for:**
  - Assessing the privacy risk of a specific processing activity — use [../dpia-privacy-assessment/SKILL.md](../dpia-privacy-assessment/SKILL.md). The RoPA tells you *what* exists; the DPIA assesses *whether it is acceptable*.
  - Deciding which privacy regimes apply at all — use [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md) first; its output determines which extra columns this skill adds.
  - Vendor security due diligence — use [../third-party-risk-assessment/SKILL.md](../third-party-risk-assessment/SKILL.md). The RoPA records *that* a vendor receives data, not whether the vendor is safe.

## Inputs to gather

Ask for these before starting; do not guess:

1. **Role and scope**: which legal entities are in scope, and for each, whether it acts as controller, processor, or both. Most B2B SaaS companies are both — controller for their own HR/marketing/CRM data, processor for customer data in the product.
2. **Org chart or function list**: the business functions to interview — at minimum HR, marketing, sales, product/engineering, support, finance, legal, security/IT.
3. **Existing artifacts** — stale ones are still useful as a discovery seed:
   - Prior RoPA, data inventory, or system register; CMDB export.
   - Vendor list, DPA repository, retention schedule.
   - SSO/identity-provider application list and procurement or vendor-payment extracts for the system sweeps.
4. **Jurisdictions and regimes**: where data subjects are, which regimes apply (GDPR/UK GDPR, US state laws, LGPD, Quebec, others) — this determines which extra fields to capture beyond the Art. 30 minimum.
5. **Transfer posture**: known third-country recipients, transfer mechanisms in use (adequacy, SCCs, BCRs), and whether transfer impact assessments exist.
6. **DPO / privacy owner**: who signs off on records and who will own the maintenance process after the build.
7. **Format constraints**: spreadsheet, GRC tool, or dedicated privacy platform — the fields are the same; the procedure is tool-agnostic.

## Procedure

1. **Choose the record perspective(s).**
   - Acting as **controller** for a processing activity → Art. 30(1) record. Acting as **processor** (processing on a customer's documented instructions) → Art. 30(2) record.
   - Many organizations need both sets. Keep them separate — the required fields differ, and mixing them is a common regulator complaint that signals role confusion. Field-by-field requirements for both: [references/ropa-field-guide.md](references/ropa-field-guide.md).
   - Where roles are genuinely unclear (analytics on customer data, fraud prevention, product improvement), run the controller/processor analysis per activity and record the conclusion — do not leave the role implicit.
   - **Decision point — Art. 30(5) small-business derogation:** the under-250-employees exemption is far narrower than commonly assumed. It falls away if the processing is likely to result in a risk to data subjects, is **not occasional**, or includes special categories or criminal-offence data. Routine HR and customer processing is not occasional, so nearly every operating company processes something that keeps the obligation alive. Default position: the derogation does not apply; say so explicitly and record the reasoning if anyone argues otherwise. Verify against the official text before relying on it.
2. **Inventory processing activities.** Run both discovery tracks in parallel; each catches what the other misses:
   - **Business-function interviews** using the per-function question bank in [references/discovery-question-bank.md](references/discovery-question-bank.md). Interview the people who do the work, not only their managers — practitioners describe the data, managers describe the org chart.
   - **System-of-record sweeps** (full checklist in the question bank):
     - SSO/identity-provider application list — every integrated app.
     - Procurement records and the vendor payment ledger — SaaS bought outside IT.
     - Expense reports — the classic shadow-SaaS channel (individual subscriptions expensed monthly).
     - DNS / secure-web-gateway / CASB logs — SaaS domains with real traffic that appear in no register.
     - DPA repository and contract system — signed DPAs imply processing activities; reconcile both directions.
     - Browser-extension and marketplace-app inventories — add-ons with data access.
   - Reconcile the sweeps against each other and against the interview results; anything on one list but not the others is a lead.
   - Explicitly hunt the activities everyone forgets:
     - **Recruitment data**, including rejected candidates and referees.
     - **CCTV** and visitor management.
     - **Employee monitoring**: endpoint agents, call recording, productivity analytics.
     - **ML/AI training datasets**, plus prompt/output logs of AI tooling.
     - Whistleblowing hotlines, marketing suppression lists, and legacy backups of decommissioned systems.
   - Define the unit of record as a **processing activity** (a purpose-coherent set of operations, e.g., "payroll administration"), not a system. One system usually hosts several activities; one activity usually spans several systems. Records keyed to systems hide purposes and collapse when the system is replaced.
3. **Capture the required fields per record.** For each activity, complete every Art. 30(1) or 30(2) field:
   - Purposes — one specific purpose per line; split compound purposes ("marketing") into their real components, each with its own retention and basis.
   - Categories of data subjects and of personal data — flag Art. 9 special categories and Art. 10 criminal-offence data explicitly; they change the derogation analysis and DPIA screening.
   - Categories of recipients — processors, group companies, authorities; no "various".
   - Third-country transfers — destination and the safeguard relied on, per hop.
   - Envisaged retention/erasure periods — per data category or purpose.
   - Security measures — reference the ISMS control set (see [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md)) rather than pasting boilerplate that will drift.
   - Flag missing fields as findings, not blanks to quietly skip. Common field mistakes and a worked example record: [references/ropa-field-guide.md](references/ropa-field-guide.md).
4. **Draw the data flow map.** For each activity, chart source → systems → recipients:
   - System-to-system flows: integrations, ETL, data warehouse feeds, event streams.
   - Human export paths: reports, spreadsheet downloads, chat-channel shares — the flows that never appear in architecture diagrams.
   - Every **cross-border hop**, including sub-processor infrastructure locations and remote-access-from-third-country arrangements — support or engineering access from a third country is a transfer even when data "stays" in an EU region.
   - Annotate each cross-border hop with the transfer mechanism relied on and the transfer impact assessment reference where one exists.
   - Pick one notation and keep it: a simple hop list per activity (source → system → recipient, one line per hop) scales better and diffs better than elaborate diagrams that no one maintains.
   - The map is what makes transfer gaps, retention conflicts, and breach blast-radius questions answerable; the RoPA table alone does not.
5. **Assign lawful bases — in collaboration with the DPIA process.**
   - Record one lawful basis per purpose, and the Art. 9 condition where special categories are involved. A purpose without a basis is a finding.
   - Where the basis is contested, undefined, or the activity screens as high-risk, route it to [../dpia-privacy-assessment/SKILL.md](../dpia-privacy-assessment/SKILL.md).
   - **Link the DPIA reference into the record instead of duplicating the analysis** — divergent copies of the same lawful-basis reasoning are how RoPAs and DPIAs end up contradicting each other in front of a regulator.
   - Where the basis is consent, add a pointer to where consent records live — a consent basis without retrievable consent evidence is a finding.
6. **Set review triggers and cadence.**
   - Event triggers — update the affected records within the same quarter:
     - New system or SaaS purchase; new vendor or sub-processor.
     - New purpose for existing data; new market or jurisdiction.
     - M&A due diligence and integration; product launches.
     - DPIA outcomes that change the processing description.
   - Wire triggers into existing gates: procurement intake, vendor onboarding, change management, and the DPIA screening step — a RoPA that depends on people remembering to update it will be stale within a quarter.
   - Baseline cadence: annual full review per record owner, with sign-off recorded; high-change functions (product, marketing) every 6 months.
   - Re-run the system sweeps on the same cadence — shadow IT regrows continuously.
7. **Reuse the inventory across regimes.** Add regime-specific columns as views over the same records rather than building parallel inventories:
   - US state laws: sale/share/targeted-advertising flags, sensitive-data flags feeding data protection assessment triggers.
   - Quebec Law 25: privacy impact assessment triggers for out-of-province transfers.
   - UK GDPR: a near-identical Art. 30 duty — same records, but scope them to the UK-relevant entities and transfers separately.
   - LGPD: legal bases differ from GDPR — map them explicitly, do not assume equivalence.
   - One inventory, multiple exports. Which regimes to layer on: [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md).

## Output format

Deliver three artifacts:

1. **RoPA register** — one row per processing activity, per legal entity, per role (controller/processor), covering every required field plus owner, last-reviewed date, and links to the DPIA and DPA where applicable. Keep an export-ready view at all times — Art. 30(4) requests allow days, not weeks.
2. **Data flow map** — diagram or structured narrative per activity showing systems, flows, recipients, and cross-border hops with the transfer safeguard annotated on each hop.
3. **Findings list** — missing fields, undefined retention, unsupported transfers, and orphaned activities with no owner, each routed to an owner with a deadline.

Worked example (controller register rows, abbreviated — full field guidance in references/ropa-field-guide.md):

| ID | Activity | Purpose | Subjects | Data categories | Recipients | Transfers & safeguard | Retention | Owner |
|----|---|---|---|---|---|---|---|---|
| C-014 | Customer support ticketing | Resolve product support requests | Customer end users, customer admins | Contact data, ticket content, diagnostic logs | Ticketing SaaS (processor), CRM sync | US — SCCs (2021) + TIA ref TIA-007 | 24 months after ticket closure | Head of Support |
| C-021 | Recruitment | Assess job applicants | Applicants, referees | CV data, interview notes, assessment scores | ATS vendor (processor), hiring managers | None | 6 months post-decision unless consent to pool | Head of HR |

Example flow-map narrative (activity C-014, abbreviated — one line per hop, safeguard annotated):

```
Web form / support email -> Ticketing SaaS (EU region; US break-glass support access: SCCs module 2 + TIA-007)
Ticketing SaaS -> CRM (nightly sync: requester name, company, ticket status; internal, EU)
Ticketing SaaS -> Data warehouse (EU; aggregated support metrics only, anonymized per SOP-19)
```

Example findings-list rows:

| ID | Finding | Record | Owner | Deadline |
|----|---|---|---|---|
| F-03 | Retention undefined for diagnostic logs | C-014 | Head of Support | 2026-09-30 |
| F-07 | US sub-processor access with no documented transfer mechanism | C-032 | DPO | 2026-08-31 |

## Quality checklist

- [ ] Controller and processor records are separated, and every in-scope legal entity is covered
- [ ] Art. 30(5) derogation position stated explicitly with reasoning, not silently assumed
- [ ] Discovery used both interviews and system sweeps; the commonly forgotten activities (recruitment, CCTV, employee monitoring, ML training data) were explicitly checked
- [ ] Records are keyed to processing activities, not systems
- [ ] Every record has a specific purpose (no "business purposes"), named recipient categories (no "various"), and a retention period or an explicit finding that none is defined
- [ ] Special-category and criminal-offence data flagged per record where present, with the Art. 9 condition captured alongside the lawful basis
- [ ] Every cross-border flow names the destination and the transfer safeguard relied on, including sub-processor and remote-access hops
- [ ] Lawful bases link to DPIA analysis where one exists; no duplicated, divergent reasoning
- [ ] Each record has a named owner and a last-reviewed date; review triggers are wired into procurement, vendor onboarding, and change management
- [ ] Regime-specific views (US state, LGPD, Quebec) derive from the same records, not parallel inventories
- [ ] Findings (gaps, unsupported transfers, orphaned activities) have owners and deadlines
- [ ] The register is export-ready for an Art. 30(4) supervisory-authority request

## References

- [references/ropa-field-guide.md](references/ropa-field-guide.md) — field-by-field guidance for Art. 30(1) and 30(2) records, worked example, common mistakes
- [references/discovery-question-bank.md](references/discovery-question-bank.md) — per-function interview questions, system-sweep checklist, shadow-IT discovery tactics
- [../../context/regulations/gdpr.md](../../context/regulations/gdpr.md) — GDPR scope, Art. 30, lawful bases, transfer mechanisms
- [../../context/regulations/us-state-privacy.md](../../context/regulations/us-state-privacy.md) — US state inventory and assessment obligations layered on the same records
- [../dpia-privacy-assessment/SKILL.md](../dpia-privacy-assessment/SKILL.md) — risk assessment of individual activities; lawful-basis analysis lives there
- [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md) — which regimes' mapping obligations apply
- [../third-party-risk-assessment/SKILL.md](../third-party-risk-assessment/SKILL.md) — due diligence on the vendors the RoPA lists as recipients

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
