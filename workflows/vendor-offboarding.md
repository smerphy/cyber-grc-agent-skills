# Workflow: Vendor Offboarding and Exit

```yaml
name: vendor-offboarding
description: >-
  Controlled exit from a vendor relationship: exit planning against the
  contract's actual clauses, inventory of what the vendor holds, data return
  and certified deletion with verification, access and integration revocation
  on both sides, contract closure, residual-risk disposition, and register
  cleanup. Includes the compressed fire-drill variant for vendor failure.
skills_used:
  - third-party-risk-assessment
  - ropa-data-mapping
  - risk-assessment
  - exception-management
typical_duration: 2-8 weeks planned; days in the insolvency fire-drill variant
roles:
  - grc-analyst
  - risk-manager
  - privacy-officer
```

## Trigger

- Planned exit: contract non-renewal, migration to a replacement, service consolidation, or termination for cause.
- Unplanned exit (fire-drill variant): vendor insolvency, sudden service shutdown, acquisition by an unacceptable party, or a breach severe enough to force termination. Same steps, compressed to days, executed from the exit plan and any escrow arrangements negotiated at [onboarding](vendor-onboarding.md) — if none exist, you are improvising under the worst possible conditions, which is exactly why onboarding step 4 asks for exit assistance clauses.

## Prerequisites

- The vendor record from the inventory: tier, data categories, integrations, contract, and any open findings or risk acceptances from [onboarding](vendor-onboarding.md).
- The contract and DPA, specifically read for: termination notice periods, exit assistance obligations, data return format and deadline, deletion and certification clauses, and post-termination audit rights. What the contract actually says bounds everything below — locate it before promising the business a timeline.
- A named internal owner for the exit (usually the business owner who sponsored the vendor).
- The replacement path, if any: successor vendor, in-house, or genuine sunset of the capability.

## Steps

### 1. Exit trigger and planning — grc-analyst with business owner; risk-manager for Tier 1/2

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md) (exit analysis)
- **Inputs:** vendor record; contract and DPA exit clauses; replacement path.
- **Actions:** confirm the exit trigger and serve contractual notice on time — missed notice windows create auto-renewals that cost real money. Build the exit plan: sequence of data return, migration cutover, deletion, and access revocation, with the rule that **deletion never precedes confirmed successful migration**. Identify business processes that break during transition and their workaround. For the fire-drill variant, pull the escrow/exit plan from onboarding and compress: data extraction first, everything else after — a vendor in administration may stop answering within days.
- **Outputs:** exit plan with sequence, dates, and owners; notice served and acknowledged.
- **Decision gate:** if the contract has no data-return or deletion clause, escalate to legal before proceeding — the plan then depends on goodwill, and the risk-manager should know that in writing.

### 2. Data inventory — grc-analyst with privacy-officer

- **Skill:** [ropa-data-mapping](../skills/ropa-data-mapping/SKILL.md)
- **Inputs:** RoPA records naming this vendor as recipient/processor; vendor record; DPA subprocessor list.
- **Actions:** enumerate what the vendor actually holds: data categories, volumes, environments (production, backups, logs, analytics copies), and which of the vendor's subprocessors received data downstream. Reconcile the RoPA's answer against the vendor's own account and against reality — integrations added since onboarding often ship data the RoPA never captured. Flag data under retention obligations or legal hold that cannot simply be deleted (step 6).
- **Outputs:** vendor-held data inventory: category, location, subprocessor exposure, disposition (return / migrate / delete / retain-with-reason).

### 3. Data return, migration, and certified deletion — grc-analyst; privacy-officer verifies

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md); [ropa-data-mapping](../skills/ropa-data-mapping/SKILL.md) for updating records
- **Inputs:** data inventory; contractual return format and deadline; replacement system readiness.
- **Actions:** execute return/migration first and validate completeness and integrity in the target before authorizing deletion. Then demand deletion per the DPA: covering production, backups (or a stated backup-expiry schedule with restore-suppression), logs, and subprocessors. Require a **deletion certificate** signed by someone accountable at the vendor, naming scope and method — and spot-verify where feasible: query the vendor's API or portal for known records, attempt a login-based export, or exercise post-termination audit rights for critical vendors. A certificate is a claim; verification is evidence. Backup-cycle deletion timelines are normal — record the stated expiry date and diary a confirmation.
- **Outputs:** migration validation record; deletion certificate(s) including subprocessors; spot-verification results; diary entry for backup-expiry confirmation.
- **Decision gate:** no certificate, or verification contradicts it, means the exit does not close — escalate to legal (breach of DPA) and record an open risk in step 6.

### 4. Access and integration revocation — grc-analyst with IT/engineering

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md) (access model from the vendor record)
- **Inputs:** vendor record's access model; identity provider and network configs; secrets inventory.
- **Actions:** revoke in both directions. Our side: vendor accounts in our systems, SSO/SCIM app registrations, API keys and OAuth grants issued to the vendor, network paths (VPN, allowlisted IPs, private links), agents or connectors installed in our environment, and any vendor personnel physical access. Their side: our user accounts, our API keys to their service, webhooks and scheduled jobs still calling them. Search for the unofficial: browser extensions, marketplace integrations, and data syncs individual teams set up. Time revocation to the cutover — not before (breaks migration), not weeks after (standing backdoor).
- **Outputs:** revocation checklist executed and evidenced; secrets rotated where the vendor ever held them.

### 5. Contract and financial closure — business owner with procurement/legal; grc-analyst confirms security terms

- **Skill:** [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md) (contractual requirements step, run in reverse)
- **Inputs:** contract; exit plan status; outstanding invoices/credits.
- **Actions:** confirm termination effective date in writing, settle final invoices and unused prepayments, and inventory **surviving obligations** on both sides: confidentiality, breach notification for late-discovered incidents affecting our data, audit rights tails, indemnities, and reference/logo usage rights to revoke. Do not let procurement archive the contract until step 3's certificate is on file — closure order matters.
- **Outputs:** termination confirmation; surviving-obligations list with expiry dates; financial closure record.

### 6. Residual risk disposition — risk-manager; privacy-officer for retained personal data

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md); [exception-management](../skills/exception-management/SKILL.md) for accepted residuals
- **Inputs:** open items from steps 3-5: unverified deletions, backup-expiry timelines, data retained under legal hold, surviving obligations.
- **Actions:** score what remains: data the vendor still holds (lawfully or otherwise), dependencies not fully severed, and knowledge/capability lost with the vendor. Retained-data items under legal hold get an owner and a release condition. Anything the business accepts rather than resolves — e.g., "vendor claims deletion, verification impossible, likelihood low" — goes through formal, time-bound risk acceptance, not a shrug. Close out any onboarding-era risk acceptances tied to this vendor.
- **Outputs:** residual risk entries in the register; time-bound acceptances where taken; closed legacy acceptances.

### 7. Register and inventory updates — grc-analyst

- **Skill:** [ropa-data-mapping](../skills/ropa-data-mapping/SKILL.md); [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md) (monitoring teardown)
- **Inputs:** all prior outputs.
- **Actions:** set the vendor to offboarded (not deleted — the record is audit evidence) with exit date and artifact links. Update RoPA records to remove the vendor as recipient, update the subprocessor list if you are a processor and must notify customers per your own DPAs, cancel monitoring subscriptions and reassessment schedules, and update BC/DR plans that referenced the vendor. Archive the exit file: plan, certificates, verification, revocation evidence.
- **Outputs:** updated vendor inventory, RoPA, and subprocessor list; archived exit file; workflow closed.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Exit plan + served notice | 1 | Vendor file |
| Vendor-held data inventory | 2 | Vendor file; RoPA |
| Deletion certificates + verification | 3 | Vendor file (audit evidence) |
| Revocation checklist + rotated secrets | 4 | Ticketing/IAM records |
| Termination + surviving obligations | 5 | Contract repository |
| Residual risk entries / acceptances | 6 | Risk register; exception register |
| Updated inventories | 7 | Vendor inventory; RoPA |

## Failure modes

- **Deletion by assumption.** The contract ends, everyone moves on, and the vendor holds your data indefinitely. If step 3 produces no certificate, the offboarding did not happen — it just stopped being invoiced.
- **Certificate worship, exit edition.** Accepting a one-line "all data deleted" email covering neither backups nor subprocessors. Scope the certificate and spot-verify; the exemplar breach is always in the copy nobody listed.
- **Deleting before migrating.** Authorizing deletion on the cutover date instead of after validated migration, then discovering the export was partial. Step 1's sequencing rule is absolute.
- **Zombie access.** SSO app disabled but API keys, OAuth grants, and IP allowlists live on for years. Revocation is an inventory problem — work from the recorded access model plus a discovery sweep, not memory.
- **No exit clauses to execute.** Discovering at termination that nobody negotiated data return, deletion, or exit assistance. The fix is upstream in [onboarding](vendor-onboarding.md) step 4; downstream, escalate early and negotiate from whatever leverage remains.
- **Fire-drill with no plan.** Vendor insolvency with no escrow, no export routine, and administrators controlling the servers. Tier 1 vendors need the exit plan tested while relations are good — an untested exit plan is a hypothesis.
- **Registers never updated.** RoPA, subprocessor list, and DR plans still naming a vendor gone for two years — each one a wrong answer waiting for an auditor, a customer, or an incident.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
