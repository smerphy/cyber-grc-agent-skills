# Policy Review Scoring Rubric

Use this rubric to score reviewed documents consistently across a policy set and over time. Two layers: per-dimension scores for the document, and per-finding severities.

## Dimension scores (per document, 0–4 each)

Score each dimension; report the profile, not an averaged single number — a 4 in coverage does not offset a 1 in enforceability.

### D1 — Testability

| Score | Criteria |
|---|---|
| 4 | ≥90% of normative statements testable; every MUST has an identifiable evidence source |
| 3 | 70–89% testable; defects are isolated and spot-fixable |
| 2 | 50–69% testable; vague statements cluster in whole sections |
| 1 | <50% testable; document is largely aspirational prose with keywords sprinkled in |
| 0 | No parseable normative statements (essay-style "policy") |

### D2 — Framework coverage

| Score | Criteria |
|---|---|
| 4 | All in-scope controls covered by testable statements (here or in a verified sibling) |
| 3 | ≥90% covered; remainder dispositioned (verified sibling or accepted gap) |
| 2 | 70–89% covered, or coverage relies materially on vague statements (paper coverage) |
| 1 | <70% covered; multiple whole control objectives unaddressed |
| 0 | Document does not address the domain it is titled for |

### D3 — Consistency

| Score | Criteria |
|---|---|
| 4 | No internal contradictions; terminology and parameters match all siblings checked |
| 3 | Minor terminology drift only (synonyms, no conflicting obligations) |
| 2 | ≥1 duplicated parameter that has drifted between documents |
| 1 | Direct conflicts in obligations between this document and a sibling |
| 0 | Document contradicts itself on a material requirement |

### D4 — Currency and ownership

| Score | Criteria |
|---|---|
| 4 | Review current per stated cadence; owner role exists; all references resolve; citations current |
| 3 | Review current; ≤2 minor stale references (renamed doc, superseded framework edition cited correctly in substance) |
| 2 | Review overdue by up to one full cadence period, or owner role no longer exists |
| 1 | Review overdue by more than one cadence period, or multiple orphaned references |
| 0 | No version block / no owner / no evidence the document was ever approved |

### D5 — Enforceability

| Score | Criteria |
|---|---|
| 4 | Every MUST has detection + consequence path; exceptions clause points to a live process; no known unexcepted violations |
| 3 | Isolated MUSTs with weak detection but plausible attestation path |
| 2 | Several MUSTs with no detection mechanism; exceptions process exists but unused |
| 1 | Known, systemic, unexcepted violations of MUSTs; enforcement clause points nowhere |
| 0 | Document is knowingly fictional (describes a program that does not exist) |

**Overall verdict mapping:** all dimensions ≥3 → *spot-fix*; any dimension 2 → *targeted rewrite* of affected sections; any dimension ≤1 → *re-draft* (route to the policy-authoring skill); D5 ≤1 additionally requires an immediate management escalation independent of the rewrite, because it is a live risk posture problem, not a documentation problem.

## Finding severities

| Severity | Definition | Typical remediation window |
|---|---|---|
| **Critical** | Creates regulatory or audit exposure now, or documents an obligation the organization knowingly violates with no exception on file | Before next audit / immediately |
| **High** | Uncovered in-scope control; direct inter-document conflict on an obligation; critical policy overdue > one cadence period; enforcement clause pointing to nothing | This quarter |
| **Medium** | Vague statement blocking evidence collection; orphaned reference; missing mandatory element (no scope, no version block); ownerless document; duplicated parameter not yet drifted | Next scheduled revision |
| **Low** | Keyword drift; passive voice; readability; stale-but-harmless references; style inconsistency | Opportunistic |

Severity modifiers: raise one level if the statement supports a control that failed a prior audit or maps to an active regulatory obligation (breach notification, SOX ITGC, PCI DSS in a CDE); lower one level if the affected system/process is being decommissioned this cycle (note the dependency).

## Example findings (calibration set)

**Critical — known-violated MUST.**
> Ref: Cryptography Policy §4.2 — "All laptops MUST use full-disk encryption."
> Evidence: MDM report shows 214 of 1,890 laptops unencrypted; no exceptions on file.
> Why Critical, not High: the defect is not the sentence — it is a documented obligation with a known, unexcepted 11% violation rate. This is discoverable in audit and in breach litigation.
> Remediation: file exceptions or remediate devices; do NOT weaken the statement to make the paper match the failure.

**Critical — regulatory exposure.**
> Ref: Incident Response Policy §7 — assigns regulatory notification decisions to "the IT Director as time allows" with no deadlines or regime list.
> Impact: organization is subject to GDPR Art. 33 (72-hour supervisory notification) and two US state breach laws; the policy cannot produce a timely decision. See ../../../context/crosswalks/breach-notification-timelines.md.
> Rewrite: name a notification decision owner, require legal engagement on a defined clock, and reference the regulatory notification procedure.

**High — inter-document conflict.**
> Ref: Access Control Policy §6.1 ("passwords MUST be at least 12 characters") vs Authentication Standard §3.1 ("minimum 14 characters").
> Impact: dual source of truth; the weaker value wins operationally.
> Rewrite: strip the parameter from the policy; keep the pointer.

**High — paper coverage.**
> Ref: Coverage map — ISO 27001:2022 A.8.16 (monitoring activities) maps only to §5.4: "systems are monitored as appropriate."
> Impact: control will show as covered in a documentation review and fail at evidence collection.
> Rewrite: "The security operations function MUST monitor the event sources and alert classes defined in the Logging Standard and triage alerts within the SLAs defined there."

**Medium — orphaned reference.**
> Ref: §5.2 requires handling per the "Data Handling Procedure"; no such document exists in the register.
> Rewrite options: point to Data Classification and Handling Policy §4, or commission the procedure. Pick one; do not leave the dangle.

**Medium — missing mandatory element.**
> Ref: Document has no scope section; applicability to contractors and subsidiaries is undefined.
> Impact: unenforceable against exactly the populations that generate most findings.

**Low — keyword drift.**
> Ref: §3 preamble calls all requirements "mandatory" while §4.6–4.9 use "should".
> Rewrite: align: promote to MUST where enforced, or keep SHOULD and delete "mandatory" from the preamble.

## Reporting notes

- Report the classification counts (testable/aspirational/vague) and testability ratio for every document; these are the trendable metrics for the grc-metrics-reporting skill.
- When reviewing a set, add a set-level section: duplicated-parameter matrix (parameter x documents defining it), terminology variance list, and a coverage roll-up across the whole set.
- Never average dimension scores into one number in executive reporting; show the five-dimension profile and the verdict.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
