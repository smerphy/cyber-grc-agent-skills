# Workflow: Annual Privacy Program Review

```yaml
name: privacy-program-review
description: >-
  Standing annual review of the privacy program: RoPA refreshed against
  operational reality, DPIA portfolio re-validated, DSAR performance measured,
  privacy notices checked against actual processing, regulatory changes swept
  in, and consolidated findings taken to governance with named owners.
skills_used:
  - ropa-data-mapping
  - dpia-privacy-assessment
  - dsar-handling
  - policy-review
  - regulatory-horizon-scanning
typical_duration: 4-8 weeks, run annually; schedule before the governance cycle it reports into
roles:
  - privacy-officer
  - grc-analyst
  - compliance-officer
```

## Trigger

- Annual privacy review date on the governance calendar (fix one; "when we get to it" means never).
- Off-cycle full or partial re-run: supervisory authority contact or audit announcement, M&A integration, a breach that exposed inventory gaps, or a [new privacy regulation](new-regulation-impact-assessment.md) taking effect.

## Prerequisites

- An existing RoPA/data map, DPIA register, and DSAR log — even stale ones. If any of these does not exist at all, this is not a review; run the underlying skill as a build project first.
- A regulatory applicability baseline: which regimes attach and in what roles (controller/processor) — see [regulatory-applicability](../skills/regulatory-applicability/SKILL.md) if it is missing or older than the last market entry.
- Named business-function contacts (HR, marketing, sales, product, support, finance) willing to sit for a 30-60 minute interview each.
- A governance body that receives the readout and can assign owners (privacy committee, risk committee, or equivalent).

## Steps

### 1. RoPA and data map refresh — grc-analyst interviews; privacy-officer signs off

- **Skill:** [ropa-data-mapping](../skills/ropa-data-mapping/SKILL.md)
- **Inputs:** current RoPA; system inventory; vendor inventory; SSO/expense reports for shadow-IT discovery.
- **Actions:** re-interview each business function against its existing records — do not circulate the spreadsheet for self-certification, because "no changes" is the default lie of the busy. Run the two discovery tracks from the skill in parallel: interviews top-down, system/vendor inventory bottom-up. Hunt drift specifically: new tools adopted mid-year, purposes quietly extended, retention "policies" nobody deletes against, subprocessor changes, and transfers that appeared when a vendor moved regions. Update every changed record; date-stamp the review on unchanged ones.
- **Outputs:** refreshed RoPA with per-record review dates; drift list (what changed without notification — feeds step 6).
- **Decision gate:** any newly discovered processing that was never assessed goes onto the step 2 screening backlog before this workflow closes — not into a parking lot.

### 2. DPIA portfolio review — privacy-officer; grc-analyst prepares

- **Skill:** [dpia-privacy-assessment](../skills/dpia-privacy-assessment/SKILL.md)
- **Inputs:** DPIA register; step 1 drift list; screening backlog; [DPIA template](../templates/dpia-template.md).
- **Actions:** three passes. (a) Backlog: screen every unscreened activity from step 1 — the screening decision, including "no DPIA needed", is itself a required record. (b) Staleness: for each existing DPIA, compare its described processing against the refreshed RoPA record; material change (new purpose, new data categories, new technology such as AI features, new recipients) means the DPIA must be revisited — GDPR requires review when the risk changes; verify the current text. (c) Measures: check that mitigation measures with owners and deadlines from prior DPIAs were actually implemented — an unimplemented measure is an open risk, not a completed assessment.
- **Outputs:** updated DPIA register with per-DPIA status (current / revise / new required); measure-implementation deltas.

### 3. DSAR performance review — grc-analyst; privacy-officer adjudicates

- **Skill:** [dsar-handling](../skills/dsar-handling/SKILL.md) (program-level review of the request log)
- **Inputs:** twelve months of DSAR log entries; complaint records; regulator correspondence if any.
- **Actions:** compute volumes by right and regime, on-time completion rate against statutory clocks, extension usage, and refusal/exemption grounds invoked. Then read a sample of actual responses: were searches scoped from the RoPA, were exemptions applied narrowly and documented, was identity verification proportionate? Repeated deadline misses or ad-hoc scoping are program risks to surface in step 6, not log entries to tidy. Cross-check: did step 1 discover systems holding personal data that DSAR searches have never covered? That gap invalidates past responses' completeness.
- **Outputs:** DSAR performance summary with metrics and sampled-quality findings.

### 4. Privacy notice and policy review — grc-analyst; privacy-officer approves findings

- **Skill:** [policy-review](../skills/policy-review/SKILL.md)
- **Inputs:** external privacy notices (web, product, employee), cookie/consent disclosures, internal privacy policies; refreshed RoPA from step 1.
- **Actions:** the test is accuracy against actual processing, not literary quality. Check each notice statement (purposes, categories, recipients, retention, transfers, rights channels) against the refreshed RoPA — a notice describing processing you do not do, or silent on processing you do, is a live regulatory exposure, and "we updated the RoPA but not the notice" is how it happens. Run the standard review passes on internal privacy policies: currency, ownership, enforceability, consistency with sibling documents.
- **Outputs:** review memo per document with classification (reaffirm / minor edit / substantive revision) and a notice-to-RoPA discrepancy list. Substantive revisions route into the [policy lifecycle](policy-lifecycle.md).

### 5. Regulatory change sweep — compliance-officer with privacy-officer

- **Skill:** [regulatory-horizon-scanning](../skills/regulatory-horizon-scanning/SKILL.md)
- **Inputs:** applicability register; horizon register if one exists; strategic roadmap (market entries, AI features, new products).
- **Actions:** sweep the privacy watchlist: amendments and new guidance in regimes already applicable, new regimes triggered by footprint changes ([US state laws](../context/regulations/us-state-privacy.md) accrete annually), enforcement trends that reprioritize known gaps, and upcoming effective dates within the next review cycle. Anything requiring structured impact analysis routes to the [new-regulation workflow](new-regulation-impact-assessment.md) rather than being absorbed here.
- **Outputs:** updated privacy horizon register; list of changes with readiness owners and dates.

### 6. Consolidation and governance readout — privacy-officer

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md) for the readout pack
- **Inputs:** outputs of steps 1-5.
- **Actions:** consolidate findings into one register: each with severity, owner, and due date — a finding without an owner is an observation, not a finding. Deduplicate across steps (the same shadow system often appears in steps 1, 3, and 4). Present to the governance body: state of the program, material findings, resourcing asks, and last year's findings closed vs. still open — the year-over-year closure rate is the single most honest program metric. Record decisions and accepted risks.
- **Outputs:** consolidated findings register; governance readout with recorded decisions; next review date confirmed.
- **Decision gate:** findings the governance body declines to fund or fix are formally risk-accepted through [exception-management](../skills/exception-management/SKILL.md) — silence is not acceptance.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Refreshed RoPA + drift list | 1 | RoPA / privacy platform |
| Updated DPIA register + screening decisions | 2 | DPIA register |
| DSAR performance summary | 3 | Privacy program file |
| Notice/policy review memos + discrepancy list | 4 | Policy inventory |
| Privacy horizon register | 5 | Horizon register |
| Findings register + governance readout | 6 | Governance minutes; risk register |

## Failure modes

- **Self-certification refresh.** Emailing functions "confirm your RoPA entries are current" and filing the non-replies as confirmation. Step 1 requires interviews; drift hides from questionnaires.
- **DPIAs as monuments.** DPIAs written at launch and never touched while the processing they describe evolves underneath them. Step 2's staleness pass exists because a DPIA of processing you no longer do protects nobody.
- **Metrics without reading.** Reporting DSAR on-time percentages while never sampling response quality. A 100% on-time rate of incomplete searches is worse than a late complete one.
- **Notice drift.** The RoPA gets maintained, the public notice does not, and the gap between them is discoverable by any regulator or plaintiff with a browser. Step 4's cross-check is mechanical on purpose.
- **Findings without owners.** A beautifully consolidated list that assigns nothing to nobody. If step 6 ends without names and dates, the review was a documentation exercise.
- **Annual-only cadence.** Treating this workflow as the only time privacy records get touched. The annual review is the backstop that catches what per-change triggers missed — if it catches everything, the triggers are broken; fix those too.
- **Scope creep into remediation.** Trying to fix every finding inside the review window, so the review never closes. Log, own, date, and close the review; remediation runs on its own clock.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
