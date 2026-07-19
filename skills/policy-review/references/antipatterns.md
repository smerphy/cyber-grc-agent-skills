# Policy Antipattern Catalog

Named defects to cite in review findings. Each entry: recognition signature, why it matters, example, and the fix pattern. Cite antipatterns by name in findings tables so recurring defects become countable across a policy set.

## A. Statement-level antipatterns

### AP-01 Untestable statement (vague qualifier)
- **Signature:** A requirement whose pass/fail condition depends on an undefined word: *appropriate, adequate, sufficient, timely, promptly, regularly, periodically, robust, reasonable, industry best practice, where possible.*
- **Why it matters:** No auditor can test it; no owner can comply with confidence; it converts an audit into a negotiation.
- **Example:** "Backups must be performed regularly and tested where possible."
- **Fix:** Replace the qualifier with a parameter, or a pointer to the standard that holds the parameter.

### AP-02 Missing actor
- **Signature:** Passive voice or agentless construction: "access is reviewed", "logs are retained", "encryption is applied".
- **Why it matters:** Obligations without owners are nobody's job; the review will find the activity happened nowhere.
- **Example:** "User access rights are reviewed on a periodic basis." (also AP-01)
- **Fix:** Name the accountable role: "Line managers MUST certify..."

### AP-03 Compound requirement
- **Signature:** Multiple obligations chained with "and/or" in one sentence, often with different actors and different evidence.
- **Why it matters:** Breaks traceability and partial-compliance reporting; one control ID cannot map cleanly.
- **Example:** "Systems must be patched, monitored, and backed up by the relevant teams in line with best practice."
- **Fix:** Split into one statement per requirement, each with its own ID.

### AP-04 Aspirational statement posing as requirement
- **Signature:** Values language in the requirements section: "we are committed to", "strives to", "takes security seriously", "fosters a culture of".
- **Why it matters:** Harmless in a purpose section; in the statements section it occupies the slot where a control should be, producing phantom coverage.
- **Example:** "The organization is committed to protecting customer data at all times."
- **Fix:** Move to Purpose, or replace with the concrete obligations the commitment implies.

### AP-05 Keyword inflation / deflation
- **Signature:** MUST used for things nobody enforces (inflation) or SHOULD used for genuinely mandatory obligations to avoid accountability (deflation); "mandatory" in prose while statements say "should".
- **Why it matters:** Inflation trains readers that MUST is decorative; deflation makes enforcement impossible when it is needed. Both are discoverable inconsistencies in audit and litigation.
- **Fix:** For each statement ask: will we enforce, can we detect? Yes/yes → MUST. Documented-deviation acceptable → SHOULD. Otherwise → guideline or delete.

### AP-06 Hedged mandate
- **Signature:** A MUST immediately neutered by an open escape hatch: "unless impractical", "where feasible", "except when business needs dictate otherwise".
- **Why it matters:** The escape hatch swallows the rule; every violation self-justifies. Distinct from a proper exception process, which requires documented approval.
- **Example:** "MFA MUST be enabled wherever technically feasible."
- **Fix:** State the rule absolutely; route infeasibility through the exception process where it gets recorded, risk-accepted, and time-boxed.

## B. Structure-level antipatterns

### AP-07 Embedded procedure
- **Signature:** Step-by-step instructions, tool names, screenshots, ticket categories, or queue names inside a policy.
- **Why it matters:** Volatile detail forces executive re-approval for operational tweaks — or, in practice, the policy silently rots while the real procedure lives in a wiki.
- **Example:** A policy paragraph explaining how to raise an access request in a named ticketing tool.
- **Fix:** Replace with a one-line requirement pointing to the procedure; move the steps to a procedure document with its own owner.

### AP-08 Embedded parameter
- **Signature:** Numeric or technical parameters (key lengths, password rules, retention days, SLA hours) hard-coded in a policy instead of a standard.
- **Why it matters:** Same rot mechanism as AP-07, plus it seeds AP-09 when a standard also exists.
- **Fix:** Move parameters to the standard; policy keeps the pointer.

### AP-09 Duplicated parameter (drift pair)
- **Signature:** The same parameter defined in two documents — usually a policy and a standard — with values that have drifted or will.
- **Why it matters:** Dual source of truth; operations follows the weaker value, audit tests the stricter one.
- **Example:** 12-character minimum in the policy, 14 in the authentication standard.
- **Fix:** Single source of truth in the standard; every other document references by title.

### AP-10 Orphaned reference
- **Signature:** Pointer to a document, appendix, role, or system that does not exist, was renamed, or was retired ("per the Data Handling Procedure" — no such document; "approved by the Security Steering Committee" — disbanded 2023).
- **Why it matters:** The obligation dangles; compliance is formally impossible.
- **Fix:** Repoint to the surviving document/role, or commission the missing one. Maintain a document register to catch these systematically.

### AP-11 Versioned or path-based reference
- **Signature:** References that include version numbers, dates, or file paths: "per Cryptographic Standard v2.3", "see \\\\fileserver\\policies\\...".
- **Why it matters:** Guaranteed staleness; every child revision breaks every parent.
- **Fix:** Reference by stable title only; the register resolves title → current version.

### AP-12 Scope holes and untrue absolutes
- **Signature:** "Applies to all employees" (contractors excluded by omission); "all systems" in an organization with a JV, OT estate, or unmanaged SaaS; or no scope section at all.
- **Why it matters:** The populations omitted are usually the risky ones; untrue absolutes are instant findings.
- **Fix:** Enumerate populations and system classes explicitly; state exclusions with rationale.

### AP-13 Inlined exception process
- **Signature:** Each policy defines its own approval workflow for deviations, with different approvers and forms.
- **Why it matters:** Processes drift apart; exception data fragments; nobody can report the organization's exception posture.
- **Fix:** One sentence per policy pointing to the single security exception process.

### AP-14 Missing mandatory element
- **Signature:** No scope, no roles, no enforcement clause, no review cadence, or no version/approval block.
- **Why it matters:** Each missing element is a specific failure: no scope → unenforceable boundaries; no version block → cannot demonstrate approval; no cadence → cannot be overdue, therefore never reviewed.
- **Fix:** Apply the standard template (see the policy-authoring skill's template) and backfill.

## C. Set-level antipatterns

### AP-15 Shadow requirement
- **Signature:** Binding obligations living outside the policy set: in slide decks, onboarding emails, wiki pages, contract boilerplate, or one team's runbook — sometimes stricter than the published policy.
- **Why it matters:** Untracked obligations are unreviewed, unversioned, and often contradict the official set; staff cannot know which rule governs. In audits they surface as "you told employees X but your policy says Y."
- **Detection:** Ask interviewees "where else are security rules written down?"; sample onboarding materials and customer-facing security claims.
- **Fix:** Promote into the policy set (as statement, standard, or guideline) or explicitly retire.

### AP-16 Terminology fork
- **Signature:** Sibling documents use different terms or scales for the same concept: "Confidential/Secret" vs "Restricted/Sensitive"; 4-level severity here, 3-level there.
- **Why it matters:** Handling rules and severity-driven SLAs become untranslatable across documents; tooling encodes one scheme, policies another.
- **Fix:** One authoritative definition (glossary or the owning policy); all siblings reference it.

### AP-17 Frankenstein policy
- **Signature:** A single "Information Security Policy" of 40+ pages containing policy, standards, procedures, and guidance interleaved, typically assembled from a template pack or merged over years.
- **Why it matters:** Wrong approver for most content, unreviewable as a whole, high internal-conflict density, and readers cannot find their obligations.
- **Fix:** Decompose along the document hierarchy; run coverage mapping before and after to prove nothing was dropped.

### AP-18 Copy-paste template residue
- **Signature:** Another organization's name, industry-inapplicable obligations (PCI language in a company with no card data), unfilled placeholders ("[Company]", "TBD"), or US-only legal references in an EU entity.
- **Why it matters:** Demonstrates the policy was never operationalized; auditors treat residue as evidence the whole document is fictional (see rubric D5).
- **Fix:** Full localization pass; delete inapplicable obligations rather than leaving them as accidental commitments.

### AP-19 Fictional control
- **Signature:** The document confidently describes a control, team, or system that does not exist ("the Security Operations Center monitors all alerts 24/7" — there is no SOC).
- **Why it matters:** The worst class of finding: it is a written misrepresentation, discoverable in incident litigation, customer audits, and regulatory examinations. Also inflates coverage maps.
- **Fix:** Never fix by deleting silently; escalate — either build/assign the capability or formally amend the document with risk acceptance for the gap.

### AP-20 Review theater
- **Signature:** Change log shows annual "reviewed, no changes" entries for many years across a period spanning reorgs, cloud migration, and new regulations.
- **Why it matters:** Signals rubber-stamp reviews; the document is current on paper and stale in fact. Correlates strongly with AP-10/AP-18/AP-19 findings.
- **Fix:** Reviews must record what was checked (regulatory changes considered, references verified, owner confirmed); require substantive review triggers, not just calendar cadence.

## Using this catalog

- Cite antipattern IDs in the findings table's finding column, e.g., "(AP-01, AP-02)".
- Count antipattern frequency across a policy set review — the top three recurring IDs define the systemic fix (template change, register creation, glossary adoption) that outperforms statement-by-statement correction.
- AP-19 and Critical-rated AP-15 findings always escalate to management regardless of the document-level verdict.
