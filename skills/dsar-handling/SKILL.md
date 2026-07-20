---
name: dsar-handling
description: >-
  Handles data subject rights requests (DSARs) end to end under GDPR Articles
  15-22, CCPA/CPRA, and other privacy regimes: intake and deadline tracking,
  proportionate identity verification, determining the regime and right invoked,
  scoping the search from the RoPA, applying exemptions and third-party redaction,
  and assembling or refusing the response with documented grounds. Use when asked
  to "process a DSAR", "respond to an access or erasure request", or "handle a
  right-to-know request".
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Take a data subject rights request from receipt to a lawful, on-time, documented response. The output is a delivered response (data package, confirmation of action, or a refusal with grounds and appeal information), a complete request log entry that would survive regulator scrutiny, and metrics for the privacy program. The clock is the organizing constraint: everything in this procedure is sequenced so verification, search, and review fit inside the statutory deadline with margin for the hard cases.

## When to use

- An individual (customer, user, employee, ex-employee, or their authorized agent) asks for access to, a copy of, correction of, deletion of, or restriction on their personal data, or objects to processing or opts out of sale/sharing.
- A request arrives through any channel — privacy inbox, web form, support ticket, social media, verbally to staff — that invokes a data subject right, even without legal citations ("send me everything you have on me" is a DSAR).
- A portal/agent service (e.g., authorized-agent deletion platforms) submits requests on behalf of consumers.
- **Not for:** assessing whether a new processing activity is lawful — use [../dpia-privacy-assessment/SKILL.md](../dpia-privacy-assessment/SKILL.md). Not for breach notification duties — use [../incident-regulatory-reporting/SKILL.md](../incident-regulatory-reporting/SKILL.md). Not for deciding which privacy regimes apply to the business overall — use [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md); this skill assumes that analysis exists and applies it per request. Systemic inability to meet deadlines is a program risk for [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md), not something to hide in individual request logs.

## Inputs to gather

Ask for these before starting; proceed with assumptions flagged if unavailable:

1. **The request itself** — verbatim text, channel, date and time received, and any identity evidence already provided.
2. **Requester relationship** — customer, prospect, employee, ex-employee, agent-on-behalf-of, parent/guardian; which products or services they used.
3. **Applicable regime(s)** — where the requester resides and which laws attach (GDPR, UK GDPR, CCPA/CPRA and other US state laws, others). See [../../context/regulations/gdpr.md](../../context/regulations/gdpr.md), [../../context/regulations/us-state-privacy.md](../../context/regulations/us-state-privacy.md), [../../context/regulations/uk-data-protection.md](../../context/regulations/uk-data-protection.md), [../../context/regulations/other-jurisdictions.md](../../context/regulations/other-jurisdictions.md).
4. **Systems inventory** — the RoPA / data map listing systems holding personal data, their owners, and search/export/deletion capabilities. Without this, scoping is guesswork; flag its absence as a program gap.
5. **Controller/processor posture** — for the data in question, are you the controller or a processor? Processors route requests to the controller per the DPA rather than answering directly.
6. **Backup and retention posture** — documented policy position on backups, logs, and archives (what is searched, what is exempted and why, how deletion propagates on backup expiry/restore).
7. **Prior history** — earlier requests from the same person (repetition matters for the manifestly-excessive analysis) and any open disputes or litigation holds involving them.

## Procedure

### 1. Intake and log — the clock starts at receipt

- Log immediately: date/time received, channel, verbatim request, requester identity as claimed, right(s) apparently invoked. **The statutory clock generally runs from receipt of the request, not from verification or from when it reached the privacy team** — a request stuck in a support queue for two weeks has already spent two weeks of the deadline. (Regimes differ on whether verification pauses or extends the clock; verify the position for the applicable regime before relying on it.)
- Acknowledge receipt promptly, stating the expected response timeframe.
- Compute and diary the deadline and the extension-notice deadline now. GDPR: respond within **one month of receipt, extendable by two further months** where requests are complex or numerous, provided the requester is told of the extension and the reasons **within the first month**. CCPA/CPRA: **45 calendar days, extendable once by a further 45 days** with notice to the consumer within the first window; opt-out-of-sale/sharing requests run on a shorter clock (15 business days). Other regimes vary — see [references/rights-by-regime.md](references/rights-by-regime.md), and verify against the official text.

### 2. Verify identity — proportionately

- Match verification strength to the sensitivity of the data and the consequence of the action. Erasure and access to sensitive data justify stronger verification than an opt-out (which under CCPA generally must **not** require a verifiable request).
- Prefer verification through existing means: a logged-in account action, or a confirmation link to the email address already on file, usually suffices for routine requests.
- **Do not over-collect.** Demanding government ID for a request about a newsletter subscription is itself a privacy failure; only request additional information where you have reasonable doubts, use it solely for verification, and delete it afterward. Never require account creation to exercise a right.
- Decision point — verification fails or stalls: if reasonable doubt remains after proportionate attempts, you may refuse with documented reasoning (and, under CCPA, treat an unverifiable deletion request as an opt-out where applicable — verify the current regulation text). Record every verification step taken.

### 3. Determine regime(s) and the specific right invoked

- Identify the regime(s): more than one can apply to a single requester, in which case apply the most protective applicable standard per element.
- Classify the right: access/copy, rectification/correction, erasure/deletion, restriction, portability, objection, opt-out of sale/sharing, limit use of sensitive PI, or a bundle. Requesters rarely cite articles — interpret the substance generously ("stop emailing me and delete my account" = objection/opt-out + erasure).
- Map each claimed right to its actual conditions — none are absolute. Erasure under GDPR Art. 17 applies on specific grounds and has exceptions; portability covers data provided by the subject and processed by automated means on consent/contract grounds. Full mapping: [references/rights-by-regime.md](references/rights-by-regime.md).
- Decision points requiring extra care:
  - **Manifestly unfounded or excessive requests** (GDPR Art. 12(5)): repetitive or abusive requests may be refused or charged a reasonable fee — but the burden of demonstrating this is on you, the bar is high, and annoyance is not the test. Document the analysis; when in doubt, respond.
  - **Requests via authorized agents**: verify both the consumer's identity and the agent's authority (signed permission or power of attorney per the applicable regime); respond to the right party.
  - **Employee and ex-employee DSARs**: usually access requests, usually mixed with other people's data (manager emails, grievance and investigation records, references). Coordinate with HR and legal early; third-party redaction (step 5) dominates the effort, and litigation context does not suspend the right — verify any claimed exemption specifically.

### 4. Scope the search

- From the RoPA/data map, list every system plausibly holding the requester's data; have system owners search by the identifiers on file (email, account ID, phone, employee ID). Record which systems were searched, with what identifiers, by whom, and the result — including empty results.
- Include unstructured stores proportionate to the request: shared drives, ticketing systems, and (for employee DSARs) mailboxes. Searches must be reasonable and proportionate, not infinite — document where you drew the line and why. See the disproportionate-effort boundaries in [references/exemptions-and-redaction.md](references/exemptions-and-redaction.md).
- **Backups**: apply your documented policy position — typically, backups are not searched for access requests where the live data answers the request, and deletion propagates as backups expire on schedule, with the data suppressed if restored. State this position transparently in the response. This position must be pre-documented and defensible, not invented per-request.
- Route processor-held data: instruct your processors to search/delete per the DPA; their time is inside your deadline, so instruct them early.

### 5. Assess exemptions and third-party data

- Screen the retrieved data for material that may be withheld or must be redacted: other individuals' data (rights and freedoms of others), legal privilege, trade secrets and confidential commercial information, ongoing investigations, and regime-specific exemptions. All are construed **narrowly** — an exemption removes the exempt content, not the whole response. Full treatment and redaction technique: [references/exemptions-and-redaction.md](references/exemptions-and-redaction.md).
- Redact rather than withhold wherever redaction preserves the requester's own data.
- Document every withholding decision: what was withheld, under which exemption, and the reasoning. This record is what you produce if the requester complains to a regulator.

### 6. Assemble and deliver the response

- **Access/copy**: provide the personal data plus the regime's required accompanying information (for GDPR Art. 15: purposes, categories, recipients, retention, source, rights, safeguards for transfers, existence of automated decision-making — verify the full list against the article). Use a commonly used, intelligible format; deliver securely (not unencrypted email attachments of sensitive data).
- **Rectification/correction**: correct in all systems, propagate to processors and recipients where required, confirm to the requester.
- **Erasure/deletion**: execute per system capability (delete, de-identify where the regime permits it as satisfying deletion — verify), instruct processors, apply the notification-to-recipients obligation where it applies, and state the backup position. Preserve data under legal hold or statutory retention — and say so, citing the exception relied on.
- **Restriction/objection/opt-out**: implement the processing stop, suppress rather than delete where suppression is needed to honor the choice durably, and confirm.
- If invoking an extension, send the extension notice with reasons **before** the initial deadline lapses.
- First-line responses are free under GDPR and CCPA in the normal case; fee rules for excessive/repetitive requests vary by regime — see [references/rights-by-regime.md](references/rights-by-regime.md).

### 7. Refusals — grounds, documentation, appeal routes

- Refuse only on documented grounds: identity not verifiable after proportionate effort, exemption covering the whole request, manifestly unfounded/excessive, or the right's conditions not met (e.g., erasure ground not applicable because processing remains necessary for a legal obligation).
- The refusal letter states: the decision, the grounds (specific, not boilerplate), and the requester's next steps — under GDPR, the right to complain to a supervisory authority and seek judicial remedy, communicated within one month; under CPRA and several US state laws, the appeal process where one is required. Verify the appeal mechanics for the specific state — several state laws require an internal appeal route with a mandated response window.
- Partial refusals: deliver everything not covered by the ground, and explain the withheld portion at the level of detail the exemption safely permits.

### 8. Close and log metrics

- Complete the log entry: dates (received, verified, extended, responded), right(s), regime(s), systems searched, exemptions applied, outcome, and total elapsed time.
- Feed program metrics: request volume by right and regime, on-time rate, median cycle time, extension rate, refusal rate with grounds. Rising volume or slipping on-time rate is an early regulator-attention signal — surface it via [../grc-metrics-reporting/SKILL.md](../grc-metrics-reporting/SKILL.md).
- Capture systemic findings: a system missing from the RoPA, a processor that cannot delete, an unsearchable data store. Route them to the data-map owner and the risk register — each one found during a live DSAR will be found again by the next one.

## Output format

Deliver a **DSAR Response File** (internal record) plus the outbound response:

```
# DSAR: <Request ID> — <Right(s)> — <Regime(s)>
Received: 2026-07-02 (web form) | Verified: 2026-07-06 (account email confirmation)
Deadline: 2026-08-02 | Extension: none | Responded: 2026-07-24 | Status: closed

## 1. Request
Verbatim: "Please send me a copy of all data you hold about me and delete my account."
Classified as: access (GDPR Art. 15) + erasure (Art. 17). Requester: EU customer.

## 2. Verification
Confirmation link to email on file; matched account. No additional ID collected.

## 3. Search record
| System | Identifier(s) | Searcher | Result |
| CRM | email | owner-A | 214 records exported |
| Support desk | email | owner-B | 12 tickets exported |
| Analytics | user ID | owner-C | pseudonymized events — included, position noted |
| Backups | n/a | — | not searched per documented policy; stated in response |

## 4. Exemptions / redactions
2 support tickets contained another customer's data — redacted (rights of others).
Redaction log maintained separately.

## 5. Response delivered
Secure download link (7-day expiry): data package + Art. 15 accompanying information.
Erasure executed in CRM/support/auth; invoices retained 10 years (legal obligation —
stated with legal basis); processors instructed 2026-07-15, confirmations on file.

## 6. Metrics
Elapsed: 22 days. On time. No extension. Systemic finding: analytics export was
manual — ticket raised with data-map owner.
```

## Quality checklist

- [ ] Clock computed from receipt at the original channel; deadline and extension-notice date diaried on day one.
- [ ] Verification proportionate to the request; no over-collection; verification data not reused and deleted after use.
- [ ] Regime(s) and specific right(s) explicitly classified, including bundled and implied rights.
- [ ] Agent authority verified for agent-submitted requests; both consumer and agent identity checked.
- [ ] Search record lists every system from the data map with searcher, identifiers, and result — including negatives.
- [ ] Backup position applied as pre-documented policy and stated transparently in the response.
- [ ] Every exemption applied is named, narrowly scoped, and documented with reasoning; redaction preferred over withholding.
- [ ] Access responses include the regime's required accompanying information, delivered securely.
- [ ] Any extension notified with reasons before the initial deadline; any refusal states grounds and appeal/complaint routes.
- [ ] Erasure propagated to processors with confirmations on file; retained data justified by cited exception.
- [ ] Log entry complete; metrics fed; systemic findings routed to the data-map owner and risk register.

## References

- [references/rights-by-regime.md](references/rights-by-regime.md) — rights, deadlines, extensions, verification, and fees per regime
- [references/exemptions-and-redaction.md](references/exemptions-and-redaction.md) — exemptions, redaction technique, disproportionate-effort boundaries
- [../../context/regulations/gdpr.md](../../context/regulations/gdpr.md) — GDPR data subject rights foundation
- [../../context/regulations/us-state-privacy.md](../../context/regulations/us-state-privacy.md) — CCPA/CPRA and other US state laws
- [../../context/regulations/uk-data-protection.md](../../context/regulations/uk-data-protection.md) — UK GDPR / DPA 2018 specifics
- [../../context/regulations/other-jurisdictions.md](../../context/regulations/other-jurisdictions.md) — analogous rights elsewhere
- [../dpia-privacy-assessment/SKILL.md](../dpia-privacy-assessment/SKILL.md) — assessing the processing DSARs surface problems with
- [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md) — which regimes attach to the business
- [../incident-regulatory-reporting/SKILL.md](../incident-regulatory-reporting/SKILL.md) — if a DSAR uncovers a breach
- [../grc-metrics-reporting/SKILL.md](../grc-metrics-reporting/SKILL.md) — DSAR program metrics
