# Policy Writing Rules

Style rules for normative documents, each with before/after rewrites. The test for every rule: could an auditor design a pass/fail test from the sentence alone, and could the accountable person know unambiguously what is required of them?

## Rule 1 — One requirement per statement

Compound statements hide requirements, break traceability (which control does the second clause map to?), and make partial compliance unreportable.

**Before:**
> Systems must be patched regularly and monitored for vulnerabilities, and any issues found must be fixed promptly by the responsible teams.

**After:**
> VM-01. System owners MUST ensure their systems are scanned for vulnerabilities at the frequency defined in the Vulnerability Management Standard.
> VM-02. System owners MUST remediate identified vulnerabilities within the SLA for the vulnerability's severity defined in the Vulnerability Management Standard.

Three vague obligations became two testable ones, each with a mappable control reference and an accountable role.

## Rule 2 — Name the accountable role

A statement with no subject has no owner. "Access is reviewed quarterly" — by whom? Passive voice is the main carrier of this defect.

**Before:**
> User access rights are reviewed on a periodic basis.

**After:**
> AC-07. Line managers MUST certify the access rights of their direct reports every calendar quarter and record the outcome in the access review system.

Use role titles, never person names or team nicknames. If no role can be named, the requirement is not yet implementable — resolve ownership before publishing.

## Rule 3 — Replace vague qualifiers with parameters or pointers

Banned without a defined parameter: *appropriate, adequate, sufficient, timely, promptly, regularly, periodically, robust, strong, reasonable, where possible, as needed, industry best practice.* Either state the parameter, or point to the standard that does. Prefer the pointer when the parameter will change: policies should outlive their parameters.

**Before:**
> Sensitive data must be protected with strong encryption.

**After:**
> CR-02. Workforce members MUST NOT store Confidential or Restricted data outside encrypted storage that meets the Cryptographic Standard.

**Before:**
> Backups must be taken frequently and tested from time to time.

**After:**
> BC-04. IT operations MUST back up in-scope systems at the frequency defined per criticality tier in the Backup Standard.
> BC-05. IT operations MUST perform and document a restore test for each criticality-1 system at least annually.

## Rule 4 — RFC-2119-style keyword discipline

- **MUST / MUST NOT**: mandatory; non-compliance is a policy violation requiring an exception or remediation. Use only where the organization will enforce and can verify. A MUST nobody checks trains readers to ignore every MUST.
- **SHOULD / SHOULD NOT**: expected default; deviation requires a documented, justified decision (not a formal exception). If you cannot articulate what a valid deviation looks like, promote to MUST.
- **MAY**: explicitly permitted option. If deleting the sentence changes nothing, delete it.

Never mix registers. "Users are encouraged to..." and "It is recommended that..." are guideline language; in a policy they read as unenforceable and drag down the credibility of adjacent MUSTs.

**Before:**
> Employees should always use MFA and are encouraged to choose strong passwords.

**After (policy):**
> AC-04. Workforce members MUST use multi-factor authentication for all remote access and for all access to systems designated criticality 1 or 2.
> AC-05. Workforce members MUST use credentials that meet the Authentication Standard.

(Password-strength *advice* — passphrases, manager usage tips — moves to a guideline.)

## Rule 5 — Right altitude: no procedures or parameters in a policy

Steps, screenshots, tool names, and numeric parameters belong in standards and procedures. Symptom to watch for: a policy that would need re-approval because a vendor was swapped or a threshold tuned.

**Before (in a policy):**
> To request access, open a ticket in ServiceNow under Category > Access, obtain approval from your manager and the application owner in the tool, after which the IAM team provisions the account within 2 business days.

**After (policy):**
> AC-06. System owners MUST ensure access is granted only after the approvals defined in the Access Provisioning Procedure are recorded.

The ticket tool, category path, and 2-day SLA move to the procedure, where the process owner can change them without executive re-approval.

## Rule 6 — Scope statements must bound the population precisely

"Everyone" and "all systems" are fine only if literally true. Untrue absolutes generate instant audit findings.

**Before:**
> This policy applies to all employees.

**After:**
> This policy applies to all workforce members — employees, contractors, and temporary staff — of Example Corp and its subsidiaries, and to third parties granted access to Example Corp systems. It applies to all information systems owned or operated by Example Corp, including cloud services processing Example Corp data. Out of scope: systems operated by the JV entity under the 2025 separation agreement (covered by that entity's policy set).

## Rule 7 — Point to the exception process; never inline it

Inlining approval workflows in each policy guarantees drift between documents.

**Before:**
> Exceptions to this policy may be granted by the CISO or, in their absence, the Deputy CISO, provided a risk assessment form 27-B is completed and reviewed quarterly...

**After:**
> Deviations from this policy MUST follow the Security Exception Process. Non-compliance without an approved exception is a policy violation.

## Rule 8 — Write for the reader who must comply, not the auditor alone

Statements aimed at general staff (AUP, data handling) use plain words and concrete behaviors; statements aimed at engineers can use technical precision. Split audiences into separate documents rather than mixing registers.

**Before:**
> Personnel shall not effectuate the transmission of organizational data assets via unsanctioned egress channels.

**After:**
> AUP-09. Workforce members MUST NOT send company data classified Confidential or above through personal email, personal messaging, or personal cloud storage accounts.

## Rule 9 — Make time and evidence explicit

If a requirement has a deadline or produces a record, say so — the record is what gets audited.

**Before:**
> Terminated employees' access must be removed quickly.

**After:**
> AC-08. IT operations MUST disable all accounts of a departing workforce member by end of their last working day, based on the HR termination notification, and retain the deprovisioning record for 3 years.

## Rule 10 — Version, date, and cross-reference hygiene

- Reference documents by stable title ("Cryptographic Standard"), never by version number or file path — versioned references rot.
- Every statement carries a stable unique ID (prefix + number). Never renumber existing IDs on revision; retire IDs and append new ones, so traceability tables and test procedures keep resolving.
- The change log records what changed and why, per version, with approver.

## Quick self-test for any statement

1. Who must act? (named role/population)
2. What exactly must they do or not do? (one requirement)
3. How would an auditor test it? (observable evidence)
4. Which keyword — MUST/SHOULD/MAY — and is that the enforceable truth?
5. Which control(s) does it satisfy? (traceability entry exists)

Any "unclear" answer means rewrite before publishing.
