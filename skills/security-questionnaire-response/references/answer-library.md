# The Canonical Answer Library

The answer library is the single source of truth for questionnaire responses. Without one, every questionnaire is answered from scratch by whoever is free that week, and answers drift until two customers hold contradictory statements about the same control. With one, 70-90% of any standard questionnaire is a lookup, and drafting effort concentrates on the questions that are genuinely new.

## Entry schema

Every entry carries these fields. An answer without an owner and a review date is a rumor, not a canonical answer.

| Field | Content |
|-------|---------|
| ID | Stable key, grouped by domain (e.g., `AC-03`, `ENC-01`, `IR-02`) |
| Question pattern | The question(s) this entry answers, including SIG/CAIQ IDs where known and common custom phrasings |
| Canonical answer | The approved answer text, written to the truthfulness rules (see `answering-rules.md`) |
| Scope caveats | What the answer does and does not cover: product vs. corporate, environments, populations, exclusions |
| Evidence pointer | The checkable artifact behind the answer: SOC 2 criterion/section, ISO SoA control, policy name and section, pen test attestation |
| Owner | Named role accountable for the answer's accuracy (not "the security team") |
| Review date | Last verified date; stale entries (>12 months, or older than the current SOC 2 period) must be re-verified before reuse |
| Sensitivity | Public / NDA-only / do-not-share (e.g., detailed architecture) |

## Seeding the library

Build the first cut from evidence you already have, in this order:

1. **SOC 2 system description and control list** — the system description is pre-approved language about your environment; every tested control yields an answer with an evidence pointer built in. Where the report notes exceptions, the canonical answer must acknowledge the control honestly (the customer will read the same report).
2. **ISO 27001 Statement of Applicability** — included controls give answers; *excluded* controls give you pre-drafted honest "no/N/A with justification" entries.
3. **Policy set** — policies supply governance answers (review cycles, ownership, training). Do not let policy quotes stand alone as operational answers; pair the policy citation with the operational fact.
4. **DPA, trust page, subprocessor list** — these are already public or contractual; canonical answers must match them verbatim in substance.
5. **One or two completed questionnaires** — mine past responses, but re-verify each answer before canonizing; past answers are where drift lives.

Then map entries to SIG and CAIQ question IDs once — both are stable enough across versions that the mapping mostly survives updates. CAIQ questions map to CSA CCM control IDs (see `../../../context/frameworks/csa-ccm.md`), which makes CAIQ the cheapest standard questionnaire to answer from a seeded library.

## Example canonical entries

Illustrative entries with realistic content — replace specifics with your own verified facts. Shown compressed; in the library each is a full record per the schema.

### Access control

- **AC-01 — Unique IDs and authentication.** Q pattern: "Do users have unique IDs? Is MFA enforced?" Answer: "Yes. All workforce access to production and corporate systems uses named individual accounts via SSO (SAML) with MFA enforced at the IdP. Shared accounts are prohibited by policy; break-glass accounts are vaulted, monitored, and reviewed quarterly." Scope: corporate + product. Evidence: SOC 2 CC6.1; Access Control Policy §3. Owner: IT Security Lead.
- **AC-02 — Access provisioning and least privilege.** Answer: "Access is role-based and granted via ticketed request with manager and system-owner approval. Production access is restricted to the on-call engineering group." Scope: product platform; contractor access follows the same flow. Evidence: SOC 2 CC6.2-6.3.
- **AC-03 — Termination revocation.** Answer: "HR offboarding triggers same-business-day deprovisioning of SSO-federated access; non-federated systems within an additional 24 hours via generated ticket. Quarterly access reviews catch residuals." Caveat: state your *measured* timeframe, not the policy target, if they differ. Evidence: SOC 2 CC6.3 (note any exception from the current report here).
- **AC-04 — Privileged access management.** Answer: "Administrative access requires separate privileged accounts with MFA; sessions to production infrastructure go through a bastion/PAM layer and are logged." Scope: product infrastructure; corporate IT admin follows a parallel process. Evidence: SOC 2 CC6.1; PAM standard.

### Encryption

- **ENC-01 — At rest.** Answer: "Customer data in the platform is encrypted at rest using AES-256 via provider-managed keys (<cloud provider> KMS)." Caveat: state key management honestly — provider-managed vs. customer-managed is a favorite follow-up. Evidence: SOC 2 CC6.7; architecture doc (NDA).
- **ENC-02 — In transit.** Answer: "All external connections require TLS 1.2 or higher; internal service-to-service traffic within the production VPC is encrypted in transit." Caveat: if internal traffic is *not* uniformly encrypted, say what is and is not. Evidence: SOC 2 CC6.7; TLS scan of public endpoints (customer-verifiable).
- **ENC-03 — Key management.** Answer: "Keys are managed in <cloud provider> KMS with automatic rotation; access to key administration is restricted and logged. Customer-managed keys (CMK/BYOK) are not currently supported." Sensitivity: the honest CMK "no" lives here so nobody improvises a yes.

### Incident response

- **IR-01 — IR plan and testing.** Answer: "A documented incident response plan exists, owned by <role>, with severity definitions and escalation paths; it is exercised at least annually via tabletop, most recently <date>." Evidence: IR Plan; SOC 2 CC7.3-7.4.
- **IR-02 — Customer notification.** Answer: "We notify affected customers of confirmed incidents involving their data without undue delay, per the terms of our DPA and agreement." Caveat: never state hour-commitments here beyond the DPA — SLA questions route to legal review. Evidence: DPA §<n>.
- **IR-03 — Breach history.** Answer pattern: answer truthfully for the period asked; if none, "No reportable breaches of customer data in the period requested." Caveat: verify with legal before answering; "reportable" is doing legal work in that sentence.

### Business continuity / disaster recovery

- **BC-01 — BC/DR program.** Answer: "Documented BC and DR plans exist and are tested annually; the most recent DR test was <date> with results tracked to closure." Evidence: DR test report (NDA); SOC 2 Availability criteria if in scope — do not cite Availability if your report covers Security only.
- **BC-02 — RTO/RPO.** Answer: "Platform recovery objectives are RTO <n> hours / RPO <n> hours, validated by the annual DR test." Caveat: these numbers become contractual expectations; confirm they are the *tested* numbers and route commitments beyond them to legal.
- **BC-03 — Backups.** Answer: "Customer data is backed up <frequency> with encryption at rest; restoration is tested <frequency>. Backup retention is <n> days." Caveat: retention interacts with deletion commitments in the DPA — keep the two consistent.

### Subprocessors and third parties

- **SUB-01 — Subprocessor list.** Answer: "Current subprocessors are listed at <trust page URL>; changes are notified per the DPA with an objection mechanism." Caveat: the library must point at the list, not copy it — copies drift.
- **SUB-02 — Vendor security review.** Answer: "Third parties with access to customer data undergo security assessment before onboarding and periodic reassessment, tiered by data access and criticality." Evidence: TPRM procedure; SOC 2 CC9.2.

## Maintenance

- Review every entry at least annually and whenever its evidence changes (new SOC 2 report, cert renewal, architecture change, subprocessor change). The new SOC 2 report is the natural annual trigger: re-verify the whole library against it.
- One owner per entry; the library curator chases review dates, not content.
- Version the library. Record which library version each customer submission used, so you can reconstruct exactly what any customer was told and diff honestly at renewal.
- Feed the library from both directions: new questions coming in (step 7 of the skill) and control changes going out (a control change should trigger a search for every entry that cites it).
