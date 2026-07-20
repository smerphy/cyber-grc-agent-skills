# Exemptions and Redaction in DSAR Responses

Exemptions are the pressure point of every contested DSAR. Applied well, they protect other people and legitimate interests while the requester still gets everything they are entitled to. Applied lazily — as a blanket reason to withhold — they are the fastest route to a regulator finding against you. The operating rule throughout: **exemptions are construed narrowly, applied to the exempt content only, and documented at the moment of decision.**

## Common exemptions

### Rights and freedoms of others (third-party data)

The most frequently used ground (GDPR Art. 15(4); parallel concepts in UK DPA 2018 and most regimes). Disclosure of the requester's data must not adversely affect others — but the exemption protects the *other person's* data, not the document containing it.

- Default action is **redaction, not withholding**: remove the third party's identifying data, release the rest.
- Consider whether the third party's identity is already known to the requester (a manager's comments in the requester's own review are usually disclosable as the requester's data, in their professional context) versus genuinely confidential (a whistleblower, a grievance witness). UK law frames this as a consent/reasonableness analysis — verify the applicable test.
- Mixed-data records (emails discussing several people, shared household accounts) get line-level treatment, not wholesale exclusion.
- Employee DSARs live here: investigation notes, references, and complaint records are predominantly mixed data. Budget the majority of response effort for this analysis.

### Legal professional privilege

Communications covered by legal privilege (advice and litigation privilege, or the local equivalent) are typically exempt from disclosure.

- Privilege attaches to specific communications, not to a topic. "Legal was involved in this matter" does not exempt the matter's records.
- Privilege is easy to claim and painful to defend if over-claimed — have counsel confirm the claim per document/thread, and log each privileged item withheld (date, parties, basis) in a withholding log even though the content is not disclosed.
- The existence of a dispute or litigation with the requester does **not** suspend their access right; it only exempts the genuinely privileged subset. Verify any broader litigation-related exemption in the specific regime before relying on it.

### Trade secrets and confidential commercial information

Recognized in GDPR Recital 63 and analogues: access should not adversely affect trade secrets or intellectual property (e.g., scoring algorithms, fraud models, pricing logic).

- The exemption shields the secret, not the outcome. The requester is still generally entitled to their data and, where automated decision-making rules apply, meaningful information about the logic involved — at a level of description that does not hand over the model.
- "Commercially embarrassing" is not "commercially confidential". Internal candor about the requester ("this customer is difficult") is their personal data and is normally disclosable — a fact worth circulating to staff *before* it is learned this way.

### Other regime-specific exemptions

Most regimes carry a further list — crime prevention and detection, regulatory functions, management forecasting, negotiations with the requester, confidential references, research and statistics, immigration (contested), and more (UK DPA 2018 Schedules 2-4 is a representative catalogue; CCPA has its own exception set including legal compliance and security/fraud). These are narrow, condition-laden, and regime-specific: identify the exact provision, check its conditions, and cite it in the withholding log. Never apply an exemption "by analogy" from another regime.

## Redaction technique

- **Work on copies** in a working folder; the originals stay untouched. The response package is built from redacted copies.
- **Redact irreversibly.** Black-highlighting text in a document, layering a box over a PDF, or hiding spreadsheet columns all survive copy-paste or export. Use a proper redaction tool that removes the underlying text/metadata, or export to a flattened format and verify by searching the output for the redacted strings.
- **Strip metadata**: document properties, tracked changes, comments, and hidden sheets carry exactly the content you meant to remove.
- **Redact identifiers, not mentions of existence.** "A colleague raised a concern about [REDACTED]'s conduct" often becomes "[A colleague] raised a concern about your conduct" — the requester's data survives, the third party's identity does not. Beware jigsaw identification: a redacted name is worthless if the surrounding detail (role, date, event) identifies the person anyway; widen the redaction until it holds.
- **Be consistent**: the same third party redacted in one document and named in another defeats both.
- **Keep a redaction log** alongside the withholding log: document, location, what class of information was removed, and the exemption relied on. The log is internal; it exists for the regulator conversation.
- Four-eyes review on contested or high-volume redaction sets — one person redacts, another verifies against the logs and spot-checks reversibility.

## Disproportionate-effort boundaries

Search and retrieval must be reasonable and proportionate — but disproportionality is a boundary on *how far you dig*, not a get-out from responding at all. Regulators (notably the ICO) expect controllers to make reasonable efforts and to engage with the requester rather than plead burden. Defensible positions share these features:

- **A documented, pre-existing policy** on what is searched (live systems from the data map, mailboxes for employee requests) and what is not (backup tapes where live data answers the request, decommissioned systems with no retrieval path, unindexed logs with no per-person lookup) — with written reasoning per exclusion.
- **Dialogue first**: where a request is enormous ("every email mentioning me in 10 years"), ask the requester to narrow scope (dates, systems, topics). Under GDPR, asking for specification of a large request is expressly contemplated; a refusal to narrow strengthens your proportionality position. Note the regime's rule on whether clarification affects the clock — do not assume it pauses.
- **Effort proportional to the data's significance**: more effort is expected for records with real consequence to the individual (HR investigations, credit decisions) than for trivial mentions.
- **The line is documented per request**: which sources were excluded, why, and what the requester was told. "It was hard" is not a position; "backup archives are excluded because all live data was produced and the archive contains only expiring copies of the same records, per our stated retention policy" is.
- Manifestly unfounded/excessive (GDPR Art. 12(5)) is a different, narrower gate than disproportionate effort — it targets abusive or genuinely repetitive requests, the burden of proof is on the controller, and hostility or inconvenience does not qualify. Use it rarely and document heavily.

## Documenting the withholding decision

Every exemption applied gets a contemporaneous record — this is the artifact that decides the complaint later:

1. **What** was withheld or redacted (document/record identifier, portion).
2. **Which provision** — the specific article/section/schedule, not "an exemption".
3. **Why it applies here** — the facts satisfying the provision's conditions, including the balancing analysis where the test requires one (rights of others, objection balancing).
4. **Why nothing less would do** — why redaction could not preserve more (for full withholdings).
5. **Who decided** and when; counsel sign-off for privilege claims.
6. **What the requester was told** — the response should acknowledge that information was withheld and cite the ground at the safe level of generality, except in the rare cases where the regime permits or requires not revealing the withholding itself (verify before relying on a "neither confirm nor deny" posture).

If the withholding log for a request is empty but the response is visibly incomplete, you have a documentation failure even if every judgment call was right.

---

**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
