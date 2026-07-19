---
name: policy-review
description: >-
  Reviews existing security and GRC policies for testability, framework coverage, internal
  consistency, currency, and enforceability. Use when a user asks to "review this policy",
  "audit our policies", "check policy coverage against ISO 27001 / SOC 2 / CIS", "find gaps
  or conflicts in our policy set", or "is this policy enforceable". Produces a
  statement-level findings table with severities and concrete rewrite suggestions.
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Assess whether a policy (or policy set) would survive an audit and actually govern behavior: are its statements testable, does it cover the target framework, does it contradict its siblings, is it current and owned, and can it be enforced? The output is a severity-ranked findings table with rewrite suggestions per defective statement, plus a coverage verdict.

## When to use

- Reviewing one policy, a policy plus its child standards/procedures, or an entire policy set.
- Pre-audit hygiene checks before an ISO 27001, SOC 2, or customer audit — pair with [../audit-preparation/SKILL.md](../audit-preparation/SKILL.md).
- Assessing inherited or acquired policy sets (M&A, new CISO taking stock).
- **Do NOT use** to draft new or replacement documents — use [../policy-authoring/SKILL.md](../policy-authoring/SKILL.md); this skill produces findings and rewrite *suggestions*, authoring produces the revised document.
- **Do NOT use** to assess whether controls *operate* effectively — policy review checks the paper; [../control-testing/SKILL.md](../control-testing/SKILL.md) checks reality.
- **Do NOT use** for full framework gap assessment across the program — [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md) covers people/process/technology, not just documents.

## Inputs to gather

1. **The document(s)** — full text, including version blocks and change logs. If reviewing coverage, request the complete policy set or an index; coverage findings against a partial set must be labeled as such.
2. **Target framework(s)/regulation(s)** — what "coverage" is measured against. If none given, ask; do not silently pick one.
3. **Sibling documents** — other policies/standards that share terms (classification levels, role titles, severity scales) for the consistency check. At minimum, ask which documents define terms this policy uses.
4. **Governance context** — stated review cadence, whether named owners/roles still exist, date of last approval, known reorgs since.
5. **Known pain points** — statements the organization already knows it violates, tooling that changed, prior audit findings. These calibrate the enforceability check.
6. **Review depth** — quick triage (classification counts + top findings) vs. full review (every statement dispositioned).

## Procedure

1. **Parse the document into discrete statements.** Extract every sentence carrying normative force (contains must/shall/should/may/will/required/prohibited, or is imperative). Assign each a reference (use the document's own IDs; else `§section.n`). Also extract: scope definition, roles, exceptions clause, enforcement clause, review clause, version block. Non-normative prose (purpose, background) is skimmed for contradictions but not classified.

2. **Classify each statement.** Three classes:
   - **Testable** — an auditor could design a pass/fail test from the sentence (possibly via a pointer to a standard that defines the parameter). Named actor, single requirement, observable evidence.
   - **Aspirational** — expresses intent or values with no verifiable obligation ("we are committed to protecting data"). Not a defect in a purpose section; a defect when it stands in for a requirement.
   - **Vague** — attempts to be a requirement but fails testability: missing actor, banned qualifier without a parameter ("appropriate", "regularly", "timely"), compound requirements, dangling pointer to a nonexistent standard.

   Record the classification and, for every non-testable statement, the specific defect using the antipattern names in [references/antipatterns.md](references/antipatterns.md). Compute the testability ratio (testable / total normative). Below ~70% signals a rewrite rather than spot fixes.

3. **Check framework coverage.** Map each testable statement to the target framework control(s) it supports, using [../../context/crosswalks/framework-crosswalk.md](../../context/crosswalks/framework-crosswalk.md) and the relevant `../../context/frameworks/` file for identifiers. Then invert: list in-scope framework controls with **no** covering statement in the document(s) provided. **Decision point:** a control uncovered by this policy may be covered by a sibling — mark it `not covered here — verify in <sibling>` rather than `gap` unless the full set was provided. Only mapping to *vague* statements counts as partial coverage; note it as such (paper coverage that will fail evidence collection).

4. **Check internal and cross-document consistency.** Within the document: contradictory statements, terms used before definition, keyword inflation (SHOULD in the statement, "mandatory" in the preamble). Across siblings: same subject regulated twice with different parameters (e.g., password length 12 here, 14 in the authentication standard), classification levels or severity scales that differ, role titles that don't match the org design, duplicate statements that will drift. Every conflict finding names both documents and both clauses.

5. **Check currency and ownership.** Version block present and complete; last review within the stated cadence (overdue = finding, severity scaled by how overdue and by the policy's criticality); owner role still exists post-reorg; referenced documents still exist and are current; referenced regulations/frameworks current (e.g., citations to withdrawn ISO 27002:2013 control numbers, "CCPA" without CPRA amendments, pre-2022 Annex A numbering); technology references that no longer exist ("the Symantec DLP console").

6. **Check enforceability.** For each MUST: is there a plausible detection mechanism (log, review, attestation, tool) and a real consequence path? Statements the organization knowingly violates with no exceptions on file are worse than gaps — they establish a pattern of non-enforcement that auditors and, in litigation, opposing counsel will use. Check the exceptions clause points to a live process ([../exception-management/SKILL.md](../exception-management/SKILL.md)) and the enforcement clause references a real disciplinary mechanism. Flag any MUST that is enforced-by-hope as either: rewrite to SHOULD/guideline, build the enforcement, or file exceptions.

7. **Score and assemble findings.** Severity per [references/review-rubric.md](references/review-rubric.md): **Critical** (regulatory/audit exposure or known-violated MUST), **High** (uncovered in-scope control, direct conflict between documents, overdue review of a critical policy), **Medium** (vague statement blocking evidence collection, orphaned reference, ownerless document), **Low** (style, keyword drift, minor currency). Every finding on a defective statement includes a concrete rewrite suggestion following the rules in [../policy-authoring/references/writing-rules.md](../policy-authoring/references/writing-rules.md) — a review without rewrites just relocates the work.

8. **Deliver and route.** Present the findings table, coverage summary, and verdict. Recommend disposition: spot-fix (few Medium/Low), targeted rewrite of sections (clustered findings), or full re-draft via [../policy-authoring/SKILL.md](../policy-authoring/SKILL.md) (testability ratio < ~70% or structural findings). Coverage gaps that reflect missing *controls* (not just missing words) route to [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md).

## Output format

**1. Header summary:**

> **Document:** Access Control Policy v2.1 (approved 2024-03-10, review overdue 4 months)
> **Reviewed against:** ISO 27001:2022 Annex A; SOC 2 CC6
> **Statements parsed:** 24 normative (17 testable, 2 aspirational, 5 vague) — testability 71%
> **Coverage:** 9/11 in-scope controls covered; A.8.2 (privileged access) partial (vague stmt only); A.5.17 not covered here — verify in Authentication Standard
> **Verdict:** Targeted rewrite of §4 and §6; spot fixes elsewhere. 1 Critical, 2 High, 4 Medium, 3 Low findings.

**2. Findings table** — one row per finding, sorted by severity:

| # | Sev | Ref | Class | Finding (antipattern) | Impact | Rewrite suggestion |
|---|---|---|---|---|---|---|
| 1 | Critical | §4.3 | Vague | "Privileged access must be reviewed periodically" — no frequency, no actor (Vague qualifier; Missing actor) | A.8.2/CC6.1 evidence cannot be collected; known 18-month gap since last review | "The IAM team MUST review all privileged accounts quarterly and record outcomes in the access review system." |
| 2 | High | §6.1 vs Auth Std §3 | Conflict | Policy requires 12-char passwords; Authentication Standard requires 14 (Duplicated parameter) | Auditor will test against whichever is stricter; users follow whichever is weaker | Remove parameter from policy: "Credentials MUST meet the Authentication Standard." |
| 3 | Medium | §5.2 | Vague | References "Data Handling Procedure" which does not exist (Orphaned reference) | Statement unenforceable; dangling obligation | Point to the existing Data Classification and Handling Policy §4, or create the procedure |

**3. Coverage appendix:** per target framework, three lists — covered (control ← statement refs), partial (control ← vague statement), uncovered (with `gap` vs `verify in sibling` disposition).

**4. Disposition recommendation** with routing (spot-fix / targeted rewrite / re-draft) and suggested owner.

## Quality checklist

- [ ] Every normative statement in the document appears exactly once in the parse with a classification; counts in the summary reconcile.
- [ ] Every non-testable classification cites a named antipattern, not just "vague".
- [ ] Every Critical/High/Medium finding on a statement includes a rewrite suggestion that itself passes the writing rules (actor, single requirement, keyword, no banned qualifiers).
- [ ] Coverage claims distinguish `gap` from `not covered here — verify in sibling`; no gap declared against a document set the reviewer didn't receive.
- [ ] Conflict findings cite both documents and both clauses verbatim.
- [ ] Currency findings state the review cadence claimed by the document itself, not an assumed one.
- [ ] No finding rests on an invented framework citation; control IDs checked against the context framework files.
- [ ] Verdict and routing recommendation present; severity distribution consistent with the verdict.

## References

- [references/review-rubric.md](references/review-rubric.md) — scoring rubric, severity definitions, example findings
- [references/antipatterns.md](references/antipatterns.md) — catalog of policy antipatterns to cite in findings
- [../policy-authoring/references/writing-rules.md](../policy-authoring/references/writing-rules.md) — the standard rewrites must meet
- [../../context/crosswalks/framework-crosswalk.md](../../context/crosswalks/framework-crosswalk.md) — cross-framework mapping for coverage checks
- [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md), [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md), [../../context/frameworks/cis-controls-v8.md](../../context/frameworks/cis-controls-v8.md), [../../context/frameworks/nist-csf-2.md](../../context/frameworks/nist-csf-2.md), [../../context/frameworks/nist-800-53.md](../../context/frameworks/nist-800-53.md), [../../context/frameworks/pci-dss-4.md](../../context/frameworks/pci-dss-4.md) — control identifiers
- [../policy-authoring/SKILL.md](../policy-authoring/SKILL.md) — rewriting documents the review condemns
- [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md) — when gaps are in controls, not words
- [../control-testing/SKILL.md](../control-testing/SKILL.md) — testing whether stated controls operate
- [../audit-preparation/SKILL.md](../audit-preparation/SKILL.md) — pre-audit use of review results

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
