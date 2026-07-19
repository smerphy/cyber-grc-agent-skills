# How to Read a SOC 2 Report

A SOC 2 report is not a pass/fail certificate. It is an auditor's opinion about a described system over a stated period against selected criteria, with test results you must read yourself. Most of the value — and most of the risk signal — is in the parts vendors hope you skip: exceptions, CUECs, carve-outs, and the system description boundary. Background on the Trust Services Criteria: `../../../context/frameworks/soc2-tsc.md`.

## Report anatomy

A SOC 2 report typically contains:

| Section | Contents | What you extract |
|---------|----------|------------------|
| Section 1 | Independent service auditor's report (the opinion) | Opinion type, period, criteria in scope, carve-out vs. inclusive method, any emphasis-of-matter paragraphs |
| Section 2 | Management's assertion | Should mirror Section 1; discrepancies are a flag |
| Section 3 | System description | System boundary (which product/service), infrastructure, subservice organizations, CUECs (sometimes listed here, sometimes in Section 4) |
| Section 4 | Description of controls, auditor's tests, and results | Every control, how it was tested, every exception |
| Section 5 (optional) | Other information provided by management | Unaudited. Management responses to exceptions live here. Do not treat as attested |

## Step-by-step review

### Step 1 — Type and period

- **Type I**: design and implementation at a *point in time*. No operating-effectiveness testing. Acceptable only as a bridge for young companies; ask for the Type II timeline.
- **Type II**: operating effectiveness over a *period* (commonly 6 or 12 months). This is the standard for Tier 1-2 vendors.
- Check the period end date. A report whose period ended 10 months ago is stale; ask for a **bridge letter** (gap letter) from the vendor asserting no material control changes since period end. Bridge letters are management assertions, not audit evidence — acceptable to cover a few months, not another year.
- A first-ever Type II covering only 3 months is common and acceptable with a note; two consecutive 3-month reports is a flag (why can't they sustain a 12-month period?).

### Step 2 — Opinion

Find the opinion paragraph in Section 1:

- **Unqualified** ("in all material respects...") — the normal case. Keep reading; unqualified does NOT mean zero exceptions.
- **Qualified** ("except for...") — the auditor found material problems in specific areas. Read the basis-for-qualification paragraph, identify which criteria failed, and decide whether those criteria matter to your engagement. A qualification on Processing Integrity may be irrelevant if you only rely on Security; a qualification on CC6 (logical access) almost never is.
- **Adverse** — the description is not fairly presented or controls are broadly ineffective. Treat as no attestation.
- **Disclaimer** — the auditor could not obtain sufficient evidence. Treat as no attestation and ask hard questions about why.

Also note the auditing firm. An unknown firm is not automatically a problem, but a report from a firm with no visible attestation practice deserves a search.

### Step 3 — Scope: criteria and system boundary

- **Criteria**: Security (Common Criteria, CC-series) is mandatory in every SOC 2. Availability, Confidentiality, Processing Integrity, and Privacy are opt-in. Map to your engagement: relying on the vendor for uptime? Availability should be in scope. They store your sensitive data? Confidentiality should be. Absence of a relevant category is a finding, not a footnote.
- **System boundary**: Section 3 names the specific platform/product and often the environments and locations. Verify the product and region *you* purchase is inside the boundary. Vendors with multiple products sometimes attest only their flagship. "Acme Platform" in the report vs. "Acme Edge" on your order form = the report may not cover you at all.

### Step 4 — Exceptions (test results)

Go through Section 4's test results and list every "exception noted" or "deviation":

For each exception record:
1. The control and criterion it maps to.
2. Nature and extent (e.g., "3 of 25 sampled terminated users retained access beyond 24 hours").
3. Whether the auditor identified compensating controls.
4. Management's response (Section 5, unaudited) — is it a concrete fix with a date, or "we have reinforced training"?
5. **Relevance to you**: does it touch a control your risk depends on?

Exceptions that should always get scrutiny for a SaaS vendor: access provisioning/deprovisioning, privileged access review, change management approvals, backup restoration testing, vulnerability remediation SLAs, incident response execution.

Volume heuristic: one or two isolated exceptions with credible responses is normal in a real Type II. Zero exceptions across hundreds of tests in a 12-month period is either an excellent program or a soft audit — weight the rest of the evidence accordingly. Recurring exceptions across consecutive years' reports (ask for last year's) indicate management doesn't fix what auditors find.

### Step 5 — CUECs (Complementary User Entity Controls)

CUECs are controls the vendor assumes *you* operate; the auditor's opinion depends on them. Typical CUECs: enforce MFA/SSO on your tenant, manage your own user provisioning and deprovisioning, configure data retention, review audit logs the platform exposes, restrict API key scope.

Action: extract every CUEC into a checklist, assign each to an internal owner, and verify implementation before go-live. **An unmet CUEC is your finding, not the vendor's.** This is the most commonly skipped step in SOC 2 review and the most common root cause of "but they had a SOC 2" incidents (e.g., account takeover on a tenant where the customer never enforced MFA).

### Step 6 — Subservice organizations: carve-out vs. inclusive

Nearly all SaaS vendors use the **carve-out method** for their infrastructure providers: the subservice org (typically the cloud IaaS) is identified, its relevant controls are listed as **Complementary Subservice Organization Controls (CSOCs)**, but those controls are *not tested* in this report.

Actions:
- List all carved-out subservice organizations.
- Confirm each has its own current SOC 2 (major cloud providers do; a niche data center or managed-hosting shop may not — that is a finding).
- Check the vendor's own controls include monitoring of subservice orgs (reviewing their reports annually). A vendor that carves out its host and never reviews the host's report has an unmanaged dependency.
- **Inclusive method** (subservice controls tested within the report) is rare; if present, the coverage is stronger — note it.

### Step 7 — System description quality

Skim Section 3 for consistency: employee counts, data flow diagrams, listed tools, and described processes should match what the vendor told you in sales calls and questionnaires. Contradictions (report says "annual penetration testing by an independent firm"; questionnaire says internal scans only) are integrity flags worth raising directly.

## Red flags summary

| Red flag | Severity | Response |
|----------|----------|----------|
| Adverse or disclaimed opinion | Critical | Treat as unattested; escalate |
| Qualified opinion touching CC6/CC7/CC8 (access, ops, change) | High | Findings + remediation conditions |
| Report covers a different product/region than purchased | High | Request correct-scope report or treat as unattested for your service |
| Period ended >6 months ago, no bridge letter | Medium | Request bridge letter + next report date |
| Type I only, vendor >2 years old | Medium | Require Type II by contractual date |
| Availability/Confidentiality not in scope where relied upon | Medium | Questionnaire deep-dive on the gap; contract SLA/encryption clauses |
| Repeated exceptions vs. prior year | High | Question management follow-through; consider tier-up of monitoring |
| Zero exceptions + unknown audit firm | Medium | Corroborate with pen test attestation and targeted questions |
| Carved-out subservice org with no own attestation | Medium-High | Ask how vendor oversees it; possible finding |
| Only Section 1-2 shared ("summary" or "SOC 3") for a Tier 1 vendor | Medium | SOC 3 is a general-use summary without test results; require the full SOC 2 under NDA |

## What a SOC 2 does not tell you

- Anything about the vendor's product security beyond the described controls (no code review, limited application-security depth).
- Whether *your* configuration of their product is secure (that is the CUEC list and your own hardening).
- Anything after the period end date.
- Financial viability, data residency guarantees, or contractual commitments — those come from the contract, not the report.

Fill these gaps with targeted questionnaire items (`questionnaire-analysis.md`), pen test attestations, and contract clauses (`contract-clauses.md`).

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
