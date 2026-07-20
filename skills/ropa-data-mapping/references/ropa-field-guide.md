# RoPA Field Guide — Art. 30(1) and 30(2) Records

Field-by-field guidance for completing Records of Processing Activities, with a worked controller record and the mistakes that make RoPAs fail regulator review. Use during Steps 1 and 3 of the RoPA skill procedure.

## Structure of the obligation

- **Art. 30(1)** — each **controller** (and, where applicable, its representative) maintains a record of processing activities under its responsibility.
- **Art. 30(2)** — each **processor** (and, where applicable, its representative) maintains a record of all categories of processing carried out **on behalf of each controller**.
- **Art. 30(3)** — records must be in writing, including electronic form. Spreadsheets qualify; version control and an owner per record are what make them defensible.
- **Art. 30(4)** — records must be made available to the supervisory authority **on request**. Treat "on request" as days, not weeks: keep an export-ready view at all times.
- **Art. 30(5)** — derogation for organizations with fewer than 250 employees, **unless** the processing is likely to result in a risk to data subjects, is not occasional, or includes Art. 9 special categories or Art. 10 criminal-offence data. Because routine HR, payroll, and customer processing is not occasional, the derogation rarely eliminates the obligation in practice — at most it narrows which activities must be recorded, and the safest and cheapest position is usually to record everything anyway.

## Art. 30(1) — controller record fields

| Field | What good looks like | Guidance |
|---|---|---|
| Controller name and contact details | Legal entity name, address, contact point; joint controllers, representative (Art. 27), and DPO listed where they exist | One record set per legal entity acting as controller. Name joint controllers explicitly and reference the Art. 26 arrangement. |
| Purposes of processing | One specific purpose per line, e.g., "resolve customer support requests" | The single most-failed field. "Business operations", "service improvement", and "marketing" are not purposes — they are categories hiding several purposes with different lawful bases and retention periods. Split them. |
| Categories of data subjects | Named groups: "job applicants", "customer end users", "site visitors" | Distinguish your own personnel from customers' personnel. Include non-obvious groups: referees, emergency contacts, beneficiaries, children of employees. |
| Categories of personal data | Grouped but concrete: "contact data; payment card data (PAN truncated); precise geolocation" | Flag Art. 9 special categories and Art. 10 criminal-offence data explicitly — they change the derogation analysis, DPIA screening, and the required Art. 9 condition. "Various personal data" is a finding, not an entry. |
| Categories of recipients | "Ticketing SaaS provider (processor); group HR shared-services entity; tax authorities on statutory request" | Include processors, group companies, and public authorities. "Various third parties" fails review. Internal teams are not recipients for this field, but cross-entity disclosures within a group are. |
| Third-country transfers | Destination country per recipient, transfer mechanism (adequacy decision, SCCs with module and date, BCRs), and — for Art. 49(1) second-subparagraph derogation transfers — the documented suitable safeguards | Remote access from a third country is a transfer. Sub-processor infrastructure counts: record where the data can be accessed from, not just where the primary region is. Link the transfer impact assessment where one exists. |
| Envisaged erasure time limits | Per data category or purpose: "24 months after ticket closure", "6 months after hiring decision" | "Where possible" in the text is not an exemption from trying. If retention is undefined, record "undefined — finding F-xx" and route it; do not leave the cell blank or write "as long as necessary". |
| Security measures (Art. 32(1)) | General description by reference: "per ISMS Statement of Applicability v3.2; encryption at rest and in transit; RBAC; logging" | Reference the control framework rather than pasting prose that will drift. Per-activity deviations (e.g., a system outside SSO) are worth recording here. |

Practically useful additions beyond the legal minimum — lawful basis per purpose (and Art. 9 condition), source of the data, linked systems, DPIA reference, DPA/contract reference, record owner, and last-reviewed date. Most regulator RoPA templates include lawful basis even though Art. 30(1) does not literally require it; capturing it here (linked to the DPIA analysis, not duplicated) is standard practice.

## Art. 30(2) — processor record fields

| Field | Guidance |
|---|---|
| Processor name and contact details | Plus representative and DPO where applicable. |
| Each controller on whose behalf you act | One row (or record set) **per controller** — a single generic "our customers" record does not satisfy the text. For large customer bases, generate per-controller records from the contract system rather than hand-maintaining them. |
| Categories of processing per controller | Describe operations ("hosting and storage; analytics on instruction; support access"), not purposes — purposes belong to the controller. If you find yourself writing your own purposes here, you may be a controller for that activity; re-run the role analysis. |
| Third-country transfers | Same rigor as the controller record: destination, mechanism, safeguards; include your own sub-processors' locations. |
| Security measures | General description; reference the ISMS and the security annex of your standard DPA. |

## Worked example — controller record: customer support ticketing

| Field | Entry |
|---|---|
| Record ID / owner | C-014 / Head of Support (last reviewed 2026-06) |
| Controller | ExampleCo GmbH; DPO: dpo@example.test |
| Purpose | Resolve product support requests from customer users; secondary purpose recorded separately (C-015: support-quality analytics) |
| Data subjects | Customer end users; customer administrators |
| Data categories | Name, business email, ticket content (may incidentally contain any data the user pastes — handled via redaction procedure SOP-22), product diagnostic logs, satisfaction ratings |
| Recipients | Ticketing SaaS provider (processor, DPA ref VND-031); CRM (internal system, sales team read access); no routine public-authority disclosure |
| Transfers | Ticketing provider hosts in EU region; US-based provider support staff have break-glass access → transfer to US under SCCs (module 2, signed 2024-03) + TIA-007 |
| Retention | Ticket content and logs: 24 months after closure, then deletion; aggregated satisfaction metrics retained indefinitely (anonymized per SOP-19) |
| Security measures | Per ISMS SoA v3.2; SSO + RBAC; encryption in transit/at rest; vendor attestation reviewed annually |
| Lawful basis | Art. 6(1)(b) contract (for contracting users) / 6(1)(f) legitimate interests (end users of corporate customers) — analysis in DPIA-2025-09, not restated here |

Note the moves this example makes: the incidental-data problem in free-text tickets is acknowledged and proceduralized; the analytics purpose is split into its own record; remote support access is recorded as a transfer; lawful-basis analysis is linked, not copied.

## Common field mistakes

1. **Vague purposes.** "Marketing" instead of "send product newsletters to opted-in prospects" + "retarget site visitors via ad platforms" — two purposes, two lawful bases, two retention periods, different regime flags (the second is a "share" under several US state laws).
2. **"Various" recipients.** Any cell containing "various", "misc", or "etc." is an unfinished record. Name recipient categories concretely or record a finding.
3. **Missing or fake retention.** Blank cells, "as long as necessary", or a period copied from a template that no system actually enforces. Record the *envisaged* period and, where enforcement is absent, a finding.
4. **System-keyed records.** "Salesforce" is not a processing activity. Records keyed to systems hide multiple purposes and collapse when the system is replaced.
5. **Mixed controller/processor records.** A SaaS company recording its customers' end-user data in its controller RoPA (or its own HR data in the processor record) signals role confusion — the error regulators probe first.
6. **Transfers recorded only at the primary-hosting level.** Sub-processor chains, support access, and disaster-recovery regions are where undocumented transfers hide.
7. **No owner, no date.** A record nobody signed and nobody reviews is evidence of a paper exercise. Owner and last-reviewed date are the two cheapest credibility fields in the register.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
