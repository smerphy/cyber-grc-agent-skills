# Workflow: M&A Security Due Diligence

```yaml
name: ma-security-due-diligence
description: >-
  Security and compliance due diligence on an acquisition target: pre-LOI
  outside-in review, data-room assessment against a baseline framework,
  regulatory exposure mapping including inherited obligations and open
  incidents, risk quantification feeding deal terms (price, reps and
  warranties, escrow), and a day-1/day-100 security integration plan — all
  under deal confidentiality and a timeline the deal team owns, not you.
skills_used:
  - framework-gap-assessment
  - regulatory-applicability
  - risk-assessment
  - third-party-risk-assessment
typical_duration: 2-6 weeks, dictated by the deal calendar; pre-LOI pass in days
roles:
  - grc-analyst
  - risk-manager
  - compliance-officer
  - greybeard
```

## Trigger

- Corporate development brings security into an acquisition — ideally pre-LOI, realistically at data-room opening. The earlier the entry, the more the findings can shape terms rather than merely document regret.
- A deal already signed without security diligence reaches integration planning — run steps 3-6 immediately; the missed window is itself a lesson for the corporate-development playbook.

## Prerequisites

- Deal-team clearance for every participant: NDA coverage, insider-list registration where securities rules apply, and use of the deal code name in all artifacts. Assessment notes naming the target in a shared drive are a confidentiality breach waiting to happen.
- A chosen baseline framework for the assessment (CIS Controls v8 or NIST CSF 2.0 travel well — see [CIS v8](../context/frameworks/cis-controls-v8.md), [NIST CSF 2.0](../context/frameworks/nist-csf-2.md)) so findings are comparable across deals.
- A standing diligence request list, pre-written — the compressed timeline does not allow drafting one per deal.
- Agreement with the deal lead on the output format: deal teams consume dollar ranges and deal-term asks, not maturity heat maps.

## Steps

### 1. Pre-LOI outside-in review — grc-analyst; greybeard reads the technical signals

- **Skill:** [framework-gap-assessment](../skills/framework-gap-assessment/SKILL.md) (evidence channels, external-only)
- **Inputs:** target name; public sources only — no target contact at this stage.
- **Actions:** build a view from what is observable without tipping the deal: breach history and regulatory enforcement in public reporting, exposed attack surface (registered domains, internet-facing services, leaked credentials in public dumps), certifications claimed on the website versus verifiable registers, security team footprint from public profiles, and the hygiene signals (patch levels on visible services, security disclosure policy). Rate confidence honestly — this is signals intelligence, not an assessment.
- **Outputs:** outside-in memo with red flags and priority questions for the data room.
- **Decision gate:** evidence of an undisclosed active compromise or open enforcement action goes to the deal lead immediately — it can reshape or kill the deal before diligence spend.

### 2. Diligence scoping and request list — grc-analyst, with the deal team

- **Skill:** [framework-gap-assessment](../skills/framework-gap-assessment/SKILL.md) (scope-freeze step)
- **Inputs:** deal structure; outside-in memo; standing request list.
- **Actions:** scope to what is actually being bought — the target entity, carve-out, or asset perimeter; assessing the seller's parent wastes the window. Tailor the request list: policies, prior audits and pen tests, certifications with scope statements, incident history, insurance and claims, org chart, asset and vendor inventories, and open regulatory matters. Sequence requests by decision value; in a compressed window you will not get everything, so ask for the deal-shaping items first. Agree the management-interview slots — usually one or two, shared with other diligence streams.
- **Outputs:** scoped request list submitted through the deal channel.

### 3. Data-room assessment — grc-analyst assesses; greybeard reviews technical claims

- **Skill:** [framework-gap-assessment](../skills/framework-gap-assessment/SKILL.md)
- **Inputs:** data-room documents; interview slots.
- **Actions:** assess against the baseline framework, scoring only what evidence supports — this is a document-review-heavy assessment with minimal interviews, so tag confidence per domain and refuse to inflate. Read certificates the diligence way: scope statements, periods, exceptions — a SOC 2 covering one product of five is a finding, not comfort. What the data room omits is data: no pen test reports, no incident log, or no vendor inventory usually means none exists. Use interview time on the gaps that move value, and note where answers contradict documents.
- **Outputs:** gap register with per-domain maturity and confidence; unanswered-questions list for reps.

### 4. Regulatory exposure and third-party mapping — compliance-officer; grc-analyst on the vendor estate

- **Skill:** [regulatory-applicability](../skills/regulatory-applicability/SKILL.md); [third-party-risk-assessment](../skills/third-party-risk-assessment/SKILL.md) (portfolio pass)
- **Inputs:** target's business profile; data room contracts and disclosures.
- **Actions:** derive the target's applicability register — these obligations transfer with the deal, and post-close the combined entity may cross thresholds neither party met alone (size caps, listing status, new jurisdictions); flag determinations for counsel and verify against the official text. Hunt inherited liabilities specifically: open incidents and notifications in flight, unresolved regulator correspondence, consent decrees, past breaches inside statutes of limitation, and processor obligations in customer DPAs. Sweep the vendor estate: critical dependencies, change-of-control clauses that fire at close, and contracts that will not survive integration.
- **Outputs:** target applicability register; inherited-liability list; critical-vendor and change-of-control list.

### 5. Risk quantification into deal terms — risk-manager, with the deal team

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md)
- **Inputs:** gap register; inherited-liability list; remediation cost estimates.
- **Actions:** convert findings into the deal team's language: event-based risk statements with likelihood, impact ranges in currency, and remediation cost-to-fix estimates ([risk scoring](../context/risk-scoring.md)). Route each material item to a deal mechanism: price adjustment (cost-to-fix), specific indemnity or escrow (identified liabilities like an unresolved breach), representations and warranties (the unanswered questions from step 3 become seller reps), closing conditions (fix-before-close items), or walk-away triggers. Be explicit about uncertainty — a Low-confidence domain is a rep-and-warranty ask, not a fabricated score.
- **Outputs:** quantified risk schedule mapped to proposed deal terms.
- **Decision gate:** the deal decision belongs to the deal committee; security's job is that they decide with the exposure stated. "Proceed, priced" and "proceed with indemnity" are wins; an unpriced surprise post-close is the failure.

### 6. Day-1/day-100 integration plan — grc-analyst drafts; risk-manager owns; greybeard reviews connectivity

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (treatment planning); [framework-gap-assessment](../skills/framework-gap-assessment/SKILL.md) (roadmap step)
- **Inputs:** all prior outputs; integration strategy (absorb, stand-alone, carve-out TSAs).
- **Actions:** day-1: what must be true at close — identity and access decisions for target staff, no flat network interconnection until the target environment is assessed hands-on (the diligence view was documents; treat the network as hostile until verified), incident response and notification paths for the combined entity, critical-vendor continuity. Day-100: hands-on validation of the diligence findings, control uplift sequenced by the gap register, applicability register merge, and monitoring integration. Fund it in the deal model — an unfunded integration plan is a wish list. Post-close, re-run [vendor-onboarding](vendor-onboarding.md) for inherited critical vendors and feed residual risks to the [annual risk assessment](annual-risk-assessment.md).
- **Outputs:** funded day-1/day-100 plan with owners; diligence file archived under deal confidentiality rules.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Outside-in memo | 1 | Deal file (code name) |
| Scoped request list | 2 | Deal channel |
| Gap register with confidence tags | 3 | Deal file |
| Applicability register + inherited-liability list | 4 | Deal file; counsel copy |
| Quantified risk schedule → deal terms | 5 | Deal file; deal model |
| Day-1/day-100 plan | 6 | Integration program |

## Failure modes

- **Security invited after signing.** Diligence becomes documentation of what was already bought. Every finding that could have been an escrow is now your remediation budget. Fix the playbook so security enters at LOI.
- **Heat map to a deal team.** A maturity radar chart answers no deal question. Step 5 exists because deal teams trade in dollars, indemnities, and conditions — translate or be ignored.
- **Confidentiality leak.** Target-named calendar invites, questionnaires sent from corporate accounts, notes outside the clean channel. On a listed target this is a securities problem, not an etiquette one.
- **Trusting the data room.** A data room is curated by the seller. Score what evidence supports, treat omissions as findings, and convert unverifiable claims into reps and warranties instead of assessment scores.
- **Missing the inherited breach.** The undisclosed incident inside the limitation period surfaces post-close as the buyer's regulatory problem. Step 4's liability hunt and a specific indemnity are the defenses.
- **Day-1 flat network.** Integration enthusiasm connects the environments at close; the target's undetected compromise is now yours enterprise-wide. Keep segmentation until hands-on assessment clears it.
- **Diligence findings evaporate post-close.** The deal closes, the team disbands, the gap register is never re-validated hands-on. Day-100 exists to convert diligence paper into an actual assessment and funded uplift.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
