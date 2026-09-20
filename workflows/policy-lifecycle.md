# Workflow: Annual Policy Lifecycle

```yaml
name: policy-lifecycle
description: >-
  Annual management of the policy corpus: inventory and review scheduling,
  structured review of each policy, gap-driven updates, stakeholder review,
  approval, publication with attestation, and linkage of exceptions so the
  policy set stays enforceable rather than ornamental.
skills_used:
  - policy-review
  - policy-authoring
  - exception-management
typical_duration: rolling program across the year; 2-6 weeks per policy batch
roles:
  - grc-analyst
  - compliance-officer
  - risk-manager
```

## Trigger

- Annual policy program kickoff on the governance calendar.
- Off-cycle triggers for individual policies: a [new regulation](new-regulation-impact-assessment.md) imposes documentation obligations — entry into a new market brings a whole jurisdiction's set with it, so check the [global jurisdiction index](../context/regulations/other-jurisdictions.md) rather than waiting for a single instrument to surface; an audit finding cites a policy defect; an incident exposes a policy gap; a major technology or organizational change invalidates policy content.

## Prerequisites

- A policy inventory: every policy, standard, and procedure with owner, approver, last-review date, and applicable audience. If none exists, building it is step 1's first task.
- A policy-on-policies (document control standard) defining the hierarchy (policy vs standard vs procedure), template, approval authorities, and review cadence. If absent, author it first via [policy-authoring](../skills/policy-authoring/SKILL.md) — nothing downstream works without agreed approval authorities.
- Access to inputs that drive updates: audit findings, risk assessment results, incident lessons, regulatory changes, and the exception register.

## Steps

### 1. Inventory and review scheduling — grc-analyst

- **Skill:** [policy-review](../skills/policy-review/SKILL.md) (program planning step)
- **Inputs:** policy inventory; governance calendar; known drivers (audits, certifications, regulatory deadlines).
- **Actions:** reconcile the inventory against reality — find documents in circulation but not in the inventory ("shadow policies") and inventory entries nobody can locate. Batch policies into a review schedule across the year, sequencing by: overdue reviews first, then policies feeding upcoming audits, then the rest. Confirm each policy still has a living owner; reassign orphans before scheduling their review.
- **Outputs:** reconciled inventory; twelve-month review schedule with owner and batch per policy.
- **Decision gate:** a policy with no willing owner is a retirement candidate — escalate to the compliance-officer to reassign or retire, do not review ownerless documents.

### 2. Policy review — grc-analyst per policy; owner consulted

- **Skill:** [policy-review](../skills/policy-review/SKILL.md)
- **Inputs:** current policy text; change drivers since last review (regulatory changes, audit findings, incidents, org/tech changes); exception register entries against this policy; framework requirements the policy supports (the pack for each is in [../context/frameworks/](../context/frameworks/), and the [framework crosswalk](../context/crosswalks/framework-crosswalk.md) shows where one policy statement carries several frameworks' requirements at once).
- **Actions:** review each policy for: accuracy (does it describe how things actually work), completeness (does it cover current obligations — check against mapped framework controls), enforceability (are its "musts" testable and actually enforced), clarity and audience fit, and internal consistency with sibling policies. Classify the outcome: reaffirm as-is / minor edit / substantive revision / retire and merge.
- **Outputs:** review memo per policy with classification and change list.
- **Decision gate:** substantive revisions and retirements proceed to step 3. Reaffirmations and minor edits skip to step 5 with an abbreviated approval.

### 3. Gap-driven updates — grc-analyst drafts; owner co-authors

- **Skill:** [policy-authoring](../skills/policy-authoring/SKILL.md)
- **Inputs:** review memo change list; template from the document control standard.
- **Actions:** redraft against the change list, not from a blank page. Keep policy statements at policy altitude (what and why; requirements as testable "musts") and push how-to detail into standards/procedures. Every requirement added must have a plausible enforcement and evidence mechanism — an unenforceable "must" is a future audit finding. Track changes against the prior version for reviewers.
- **Outputs:** redlined draft with change rationale.

### 4. Stakeholder review — grc-analyst coordinates

- **Skill:** [policy-authoring](../skills/policy-authoring/SKILL.md) (review round)
- **Inputs:** redlined draft; stakeholder list (teams that must live under the policy, plus legal/HR/security as relevant).
- **Actions:** time-boxed review round (one to two weeks) with a clear question: "can your team comply with every must in this document, and if not, which ones and why." Adjudicate comments in a disposition log — accepted, rejected with reason, or deferred to next cycle. Where a stakeholder genuinely cannot comply, either amend the requirement or pre-agree an [exception](../skills/exception-management/SKILL.md) — do not publish requirements known to be dead on arrival.
- **Outputs:** final draft; comment disposition log.

### 5. Approval — approver per document control standard; compliance-officer verifies authority

- **Skill:** [policy-review](../skills/policy-review/SKILL.md) (approval step)
- **Inputs:** final draft (or reaffirmation memo for unchanged policies); disposition log.
- **Actions:** route to the approval authority the document control standard names — top-level policies typically to an executive or committee, standards to function leads. Approval is recorded with approver, date, and version. Reaffirmations get the same formal record ("reviewed, no changes required, approved") — auditors treat an unrecorded review as no review.
- **Outputs:** approved, versioned policy with recorded approval.
- **Decision gate:** if the approver rejects or materially amends, return to step 3 or 4 as appropriate; do not negotiate policy content in the approval meeting itself.

### 6. Publication and attestation — grc-analyst

- **Skill:** [policy-authoring](../skills/policy-authoring/SKILL.md) (publication step)
- **Inputs:** approved policy; audience definition; publication platform.
- **Actions:** publish to the single authoritative location; retire superseded versions from circulation (broken links beat stale copies). Announce material changes with a plain-language summary of what changed and what readers must do differently. Where the policy or a regulation requires it, run attestation for the defined audience and chase completion to a target (e.g., 95% within 30 days). Record publication and attestation stats as compliance evidence.
- **Outputs:** published policy; change announcement; attestation completion record.

### 7. Exception linkage — grc-analyst with risk-manager

- **Skill:** [exception-management](../skills/exception-management/SKILL.md)
- **Inputs:** exception register; newly published policy versions.
- **Actions:** after each batch publishes, reconcile exceptions: exceptions against removed requirements are closed; exceptions against changed requirements are re-evaluated against the new text; repeated exceptions against the same requirement are a signal the requirement is wrong — feed that back into the next review cycle rather than perpetually excepting it. Verify every active exception cites the current policy version and section.
- **Outputs:** reconciled exception register; requirement-change candidates for next cycle.

## Outputs summary

| Output | Step | Evidence value |
|--------|------|----------------|
| Reconciled inventory + review schedule | 1 | Demonstrates a managed program |
| Review memos | 2 | Proof reviews happened (auditors ask) |
| Redlined drafts + rationale | 3 | Change traceability |
| Comment disposition log | 4 | Stakeholder engagement record |
| Recorded approvals | 5 | Governance evidence |
| Publication + attestation records | 6 | Awareness/communication evidence |
| Reconciled exception register | 7 | Policy-exception integrity |

## Failure modes

- **Review-date rubber-stamping.** Bumping the "last reviewed" date without a review memo. Step 2's classification requirement makes the review real; auditors increasingly test for it.
- **Policy sprawl.** Every new obligation spawns a new document until nobody knows what applies. Prefer amendment and consolidation; make "retire and merge" a normal step 2 outcome.
- **Aspirational musts.** Requirements published with no enforcement mechanism, generating either mass violation or mass exceptions. Step 3's enforceability test and step 4's "can you comply" question exist for this.
- **Approval bottleneck.** Everything routed to one executive who signs quarterly, so policies queue for months. The document control standard should delegate standards/procedures approval downward.
- **Publication without communication.** Policy silently replaced; staff follow the version they remember. Announce deltas, not just documents.
- **Exception rot.** Skipping step 7, leaving exceptions pointing at requirements that no longer exist — which makes both registers unreliable.
- **Cycle without inputs.** Reviewing policies against last year's policy instead of this year's audit findings, incidents, and regulatory changes. Step 2's inputs list is the point of the whole exercise.
