# Control Mapping: Common Pitfalls

Failure modes seen in real crosswalks, with detection cues and corrections. Review this list before starting a mapping and again during the quality sample.

---

## 1. Naive 1:1 mapping

**The failure:** forcing every source control onto exactly one target control and calling the pair equivalent. Spreadsheets with one target ID per row invite this structurally.

**Why it corrupts results:** control sets differ in granularity by design. ISO/IEC 27002:2022 has 93 controls; CSF 2.0 has 106 subcategories; CIS v8 has 18 controls decomposed into many safeguards; NIST SP 800-53 Rev. 5 runs far larger with enhancements. A 93-item set cannot map 1:1 onto any of these without either dropping obligations or inventing equivalences. Every forced 1:1 row hides either uncovered target obligations (compliance gap) or unused source obligations (wasted effort).

**Detection cues:** every source control has exactly one target; no coverage-rating column, or every rating is "mapped"; row counts of source and mapping are identical.

**Correction:** many-to-many data model (one row per pair), element-level decomposition, mandatory Full/Partial rating with rationale, residue lists both directions.

## 2. Stale crosswalk reuse

**The failure:** adopting a crosswalk built for prior versions — ISO 27001:2013 mappings applied to 2022, CSF 1.1 mappings applied to 2.0 — or reusing last year's internal mapping after the control library was rewritten.

**Why it corrupts results:** revisions restructure, not just renumber. The 2013→2022 ISO transition merged, split, and added controls (93 controls in 4 themes replacing 114 in 14 clauses; 11 new controls including threat intelligence, cloud services security, data leakage prevention). CSF 2.0 added the Govern function and reorganized categories; 1.1-era mappings have no rows for GV content and mis-house governance obligations that moved. A stale crosswalk silently reports coverage of requirements that no longer exist while missing ones that now do.

**Detection cues:** crosswalk references control IDs that do not exist in the current edition (e.g., ISO "A.12.x" against a 2022 target, CSF "ID.GV" against 2.0); no version pinning in the artifact; file metadata predates the framework revision it claims to cover.

**Correction:** pin both versions in the mapping header; on any framework revision, treat the old mapping as candidate input only and re-rate every row touching changed controls; use the publisher's official transition/correspondence annexes as candidate generators, then apply the rating rubric yourself.

## 3. Keyword-match mappings

**The failure:** pairing controls because they share vocabulary — "encryption" to "encryption", "logs" to "logs" — without comparing obligations.

**Why it corrupts results:** shared nouns hide different verbs, scopes, and intents. "Collect audit logs" vs "review audit logs" vs "protect audit logs from tampering" are three distinct obligations that all match the keyword "logs". The worked example in [mapping-method.md](mapping-method.md) shows ISO A.8.16 (monitoring) correctly rejected against CIS 8.2 (log collection) despite heavy keyword overlap.

**Correction:** rate on normalized assertions (actor–action–object–qualifier), never on titles; require rationales that reference obligations, not words. Treat any LLM- or tool-generated candidate list as exactly that — candidates for step-5 rating, not conclusions.

## 4. Scope mismatch claimed as coverage

**The failure:** rating Full between requirements with different populations: a PCI DSS control scoped to the cardholder data environment claimed to cover an enterprise-wide ISO control; a control implemented on one cloud tenant claimed against an organization-wide framework; SOC 2 criteria scoped to one system description claimed for the whole company.

**Correction:** carry scope as a first-class qualifier in normalization; standard ruling — narrower source scope caps the rating at Partial with the scope delta named. When the consumer of the mapping needs enterprise coverage, aggregate per-scope mappings explicitly rather than letting one scoped instance stand for the whole.

## 5. Governance/operation conflation

**The failure:** mapping a policy-existence control ("a topic-specific policy on X shall be defined") as Full coverage of an operational control ("X is performed and monitored"), or the reverse.

**Why it corrupts results:** frameworks deliberately separate the two — a documented intention neither performs the activity nor proves it happened. Vendor crosswalks are rife with this because policy controls keyword-match everything in their topic.

**Correction:** tag each element `governance | operational | assurance` during normalization; cross-nature pairs rate Partial at most, and the rationale must say which nature is missing.

## 6. Coverage claims silently becoming implementation claims

**The failure:** a mapping ("ISO A.8.16 corresponds to DE.CM-01") drifts in presentation into "we meet DE.CM-01" — without anyone testing whether the ISO control is actually implemented and effective.

**Why it corrupts results:** mapping is a statement about *texts*, not about the organization. An organization can hold a perfect mapping and a failed control.

**Correction:** keep mapping and implementation status in separate columns/artifacts; wording discipline ("requirement corresponds", not "we satisfy"); route implementation questions to [../../framework-gap-assessment/SKILL.md](../../framework-gap-assessment/SKILL.md) (existence/maturity) and [../../control-testing/SKILL.md](../../control-testing/SKILL.md) (effectiveness).

## 7. Ignoring reverse residue

**The failure:** sweeping only "does source cover target?" and never listing source controls that mapped to nothing.

**Why it matters:** unmapped internal controls are where duplicated effort, orphaned legacy controls, and genuinely unique obligations (contractual commitments, jurisdiction-specific requirements) hide. Skipping the reverse sweep forfeits the rationalization value of the exercise and can lead to unique obligations being dropped in a later "cleanup".

**Correction:** always produce both residue lists; classify source residue (`unique-obligation | duplicate | over-spec`) before anyone deletes anything.

## 8. Averaging or majority rollups

**The failure:** a control with elements rated Full, Full, None reported as "mostly covered" or Full.

**Why it corrupts results:** the uncovered element is often the enforceable part (the cadence, the review, the documentation). Auditors and regulators test the element you dropped.

**Correction:** weakest-link rollup only; uncovered elements always surface in the residue list regardless of sibling ratings.

## 9. Mapping from titles or summaries

**The failure:** building the mapping from control titles, marketing one-pagers, or a GRC tool's truncated descriptions instead of the licensed full text.

**Detection cues:** rationales that restate titles; no qualifier deltas anywhere in a large mapping (real control text always produces qualifier deltas).

**Correction:** obtain full text for both sets before rating; where licensing blocks access (ISO texts are paid), say so explicitly and mark affected ratings low-confidence rather than guessing.

## 10. No maintenance triggers

**The failure:** shipping the mapping as a static deliverable with no statement of when it dies. Two years later it is pitfall #2 for someone else.

**Correction:** every deliverable ends with pinned versions and explicit invalidating events (framework revision, internal control rewrite, scope change, M&A). If the organization runs regulatory-change monitoring, register the mapped frameworks as watched items — see [../../regulatory-horizon-scanning/SKILL.md](../../regulatory-horizon-scanning/SKILL.md).

---

## Pre-flight checklist (condensed)

- [ ] Full text of both sets, exact versions pinned
- [ ] Many-to-many table structure with rating + rationale columns
- [ ] Decomposition pass done before any rating
- [ ] Scope and nature (governance/operational/assurance) tagged per element
- [ ] Existing crosswalks demoted to candidate-generator status
- [ ] Both residue sweeps scheduled
- [ ] Weakest-link rollup and blind quality sample planned
- [ ] Maintenance triggers drafted for the deliverable

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
