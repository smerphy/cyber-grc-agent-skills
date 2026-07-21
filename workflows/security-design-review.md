# Workflow: Security Design Review

```yaml
name: security-design-review
description: >-
  Security and architecture review of a new system, product feature, or major
  change before build or launch: intake and risk-tiering, a threat-informed
  design review led by the fatal-flaw hunt, regulatory and privacy screening,
  security requirements with named owners, a conditional approval gate, and
  post-implementation verification that what shipped is what was approved.
skills_used:
  - risk-assessment
  - regulatory-applicability
  - control-mapping
  - dpia-privacy-assessment
typical_duration: 2-5 business days for standard changes; 2-4 weeks for major new systems
roles:
  - greybeard
  - grc-analyst
  - risk-manager
```

## Trigger

- A new system, product feature, integration, or major architectural change enters design — trigger **at design, not at pre-launch**. A review that can only say yes or no to a finished build is a launch veto, not a design review.
- A significant change to an already-reviewed system (new data categories, new exposure to the internet, new trust boundary, authentication model change) — re-run from step 1.
- Discovery of a system launched without review — run retroactively and record the unreviewed period as a finding.

## Prerequisites

- A review-tiering rubric (data sensitivity, internet exposure, blast radius, novelty of the pattern) so depth is proportionate. If none exists, define one before the first intake.
- A baseline security requirements set or internal control library to draw requirements from — reviews that invent requirements per-project produce inconsistency and appeals.
- A named delivery owner for the change; no owner, no review.
- Design artifacts standard: architecture diagram, data-flow description, trust boundaries, dependency list. Enforce this at intake — reviewing a verbal description reviews nothing.

## Steps

### 1. Intake and risk-tiering — grc-analyst, with the delivery owner

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (context-establishment step)
- **Inputs:** change description from the delivery team.
- **Actions:** capture the facts that drive tiering: what the system does, data categories and classifications handled, user population, internet exposure, privileged integrations, dependencies on existing crown-jewel systems, and whether the pattern is novel or a repeat of an approved one. Verify against the actual design intent, not the project pitch. Apply the tiering rubric mechanically and record the driving factor.
- **Outputs:** intake record with assigned review tier and rationale.
- **Decision gate:** low-tier changes (no sensitive data, no new exposure, established pattern) get a checklist review against the baseline requirements and skip to step 5. Everything else proceeds to step 2.

### 2. Scoping and design-package assembly — grc-analyst

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (scope boundary)
- **Inputs:** intake record; design artifacts from the delivery team.
- **Actions:** fix the review boundary in writing: components, data flows, environments, and integrations in scope; explicitly name what is out of scope and why. Chase missing artifacts before the review session — an incomplete package wastes the reviewers and hides the flaw. Confirm the data-flow description matches the diagram; mismatches are the first finding.
- **Outputs:** frozen design package and scope statement circulated to reviewers.

### 3. Threat-informed design review — greybeard leads; grc-analyst scribes

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (threat- and scenario-based identification)
- **Inputs:** design package; threat landscape inputs (recent incidents, sector intel).
- **Actions:** hunt the fatal flaw first — the assumption that makes the whole design not work: shared blast radius between primary and backup, credentials that survive the compromise they are meant to contain, a recovery path that depends on the system being recovered. Ask what fails first, what fails silently, what fails together; check the boring things (time sync, certificate expiry, key rotation, quota limits). Demonstrated beats declared — a claimed control without test evidence is recorded as an assumption, not a control. Develop 3-5 scenarios for the highest-stakes combinations and write findings as event-based risk statements. State explicitly when no fatal flaw was found, then move to lesser findings ranked by what actually breaks the system.
- **Outputs:** review findings list, fatal-flaw determination first, each finding tied to a design element.

### 4. Regulatory and privacy screening — grc-analyst; privacy function joins if personal data is involved

- **Skill:** [regulatory-applicability](../skills/regulatory-applicability/SKILL.md) (change-scoped pass); [dpia-privacy-assessment](../skills/dpia-privacy-assessment/SKILL.md) (screening step)
- **Inputs:** intake record; the organization's applicability register.
- **Actions:** test whether the change moves any regulatory needle: new jurisdictions of users or data, new data categories that engage sectoral regimes, new processing that changes the org's profile (verify determinations against the official text — do not decide scope questions from memory). If personal data is processed, run the DPIA screening and record the decision either way — a documented negative screening is a required artifact, not an optional one. If the screening triggers a full DPIA, launch it in parallel; the design review does not wait, but step 6 cannot approve launch until the DPIA concludes.
- **Outputs:** screening record; updated applicability register rows if the profile changed; DPIA opened where triggered.

### 5. Security requirements issued — grc-analyst drafts; greybeard confirms coverage

- **Skill:** [control-mapping](../skills/control-mapping/SKILL.md)
- **Inputs:** findings from steps 3-4; baseline security requirements set.
- **Actions:** convert every accepted finding into a specific, testable requirement with a named owner (a role, not "the team") and a due milestone (before build / before launch / within 90 days of launch). Map each requirement to the internal control set or adopted framework (see the [framework crosswalk](../context/crosswalks/framework-crosswalk.md)) so it inherits existing test and evidence machinery instead of becoming an orphan. Requirements the delivery team disputes go to step 6 with the disagreement stated, not silently dropped.
- **Outputs:** security requirements register for the change, mapped to the control library.

### 6. Conditional approval gate — risk-manager decides; greybeard and delivery owner present

- **Skill:** [risk-assessment](../skills/risk-assessment/SKILL.md) (scoring and appetite comparison)
- **Inputs:** requirements register; disputed or deferred requirements with risk scores.
- **Actions:** score the residual risk of launching with each unmet or deferred requirement, against the appetite line ([risk scoring methodology](../context/risk-scoring.md)). Decide: approve, approve with conditions (named requirements, owners, dates — recorded, tracked, and re-verified in step 7), or do not approve. Deliberate deviations from mandated controls route through [exception-management](../skills/exception-management/SKILL.md) with proper authority — the review team never self-approves an above-appetite launch.
- **Outputs:** signed approval decision with conditions; above-appetite residuals entered in the risk register.
- **Decision gate:** an unresolved fatal-flaw finding or a pending Article 36-type prior consultation from the DPIA is an automatic no-go regardless of schedule pressure. "No" and "not yet" are recorded outcomes.

### 7. Post-implementation verification — grc-analyst; greybeard spot-checks material items

- **Skill:** [control-mapping](../skills/control-mapping/SKILL.md) (built-state check against issued requirements)
- **Inputs:** approval conditions; as-built evidence from the delivery team.
- **Actions:** within the committed window after launch, verify each condition and pre-launch requirement against as-built evidence — configuration exports, test results, tickets — not against assertions. Divergence between reviewed design and shipped build is a finding in itself; material divergence reopens step 6. Close the review record; feed durable residual risks to the [annual risk assessment](annual-risk-assessment.md).
- **Outputs:** verification record; closed review or reopened gate.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Intake record + review tier | 1 | Review register |
| Design package + scope statement | 2 | Review file |
| Findings list (fatal-flaw determination first) | 3 | Review file |
| Screening record / DPIA decision | 4 | Applicability register; DPIA file |
| Security requirements with owners | 5 | Requirements register / control library |
| Approval decision + conditions | 6 | Review register; risk register |
| Post-implementation verification | 7 | Review file |

## Failure modes

- **Review at launch, not at design.** The team arrives with a finished build and a launch date; every finding becomes a veto fight. Wire intake into the delivery process at design stage — the review's leverage is proportional to how much can still change.
- **Nitpick blizzard, no fatal-flaw hunt.** Forty style findings and the killing assumption unexamined. Step 3 exists to find the flaw that matters first; everything else is ranked below it.
- **Tiering by team optimism.** Delivery teams minimize intake answers to land the light track. Spot-check intake facts against the design package; make re-tiering on discovery automatic and unremarkable.
- **Requirements without owners or dates.** "The team will address encryption" is not a requirement. Step 5's register is only real when each row survives the owner's departure.
- **Conditional approval, unconditional in practice.** Conditions granted under launch pressure and never verified. Step 7 is the enforcement mechanism; skip it and every future condition is known to be free.
- **Design reviewed, build drifted.** The shipped system quietly differs from the approved design. Verify as-built evidence, and treat divergence as a finding, not an inconvenience.
- **"We did security, so privacy is covered."** The DPIA screening skipped because a threat review happened. They assess different risks to different parties; step 4 records the screening decision even when the answer is no.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
