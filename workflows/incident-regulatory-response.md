# Workflow: Incident Regulatory Response

```yaml
name: incident-regulatory-response
description: >-
  Regulatory and disclosure track of incident response, run in parallel with —
  never instead of — technical containment and eradication: characterize the
  incident against applicable regimes, work the notification decision table,
  track every deadline clock, draft and file notifications, manage supplements,
  and close with a disclosure review. Maintains a decision log throughout.
skills_used:
  - incident-regulatory-reporting
  - regulatory-applicability
typical_duration: first 72 hours are decisive; tail runs weeks to months (supplements, final reports)
roles:
  - compliance-officer
  - privacy-officer
  - grc-analyst
```

## Trigger

- The incident response process declares an incident at a severity that could plausibly involve personal data, regulated data, service disruption to regulated services, or material business impact.
- Trigger this workflow **at declaration, not at confirmation of impact**. Several clocks start earlier than teams assume — NIS2's 24-hour early warning runs from awareness of a significant incident, and GDPR's 72 hours run from awareness of a personal data breach, not from completed forensics.

## Prerequisites

- A pre-built applicability profile: which regimes apply to this organization (from [regulatory-applicability](../skills/regulatory-applicability/SKILL.md)), with per-regime notification criteria, deadlines, competent authorities, and filing channels. Building this during a live incident is the single most common cause of missed deadlines — see the [breach notification timeline matrix](../context/crosswalks/breach-notification-timelines.md).
- Contact sheet: regulators' filing portals/addresses, external counsel, cyber insurer notification requirements, and internal escalation chain including disclosure committee members for public companies.
- A decision log template and a named scribe.

## Parallel-track principle

This workflow runs **alongside** technical IR, consuming its outputs (facts, scope, timeline) and never blocking it. The two tracks synchronize at every IR status update; the regulatory track must never wait for "final" forensics, because every major regime permits — and effectively requires — notifying on incomplete information and supplementing later. Conversely, the technical track must know that its factual statements ("no evidence of exfiltration") become regulatory representations; imprecise language in IR channels becomes tomorrow's filing problem.

## Steps

### 1. Regulatory intake — compliance-officer (privacy-officer joins if personal data plausible)

- **Skill:** [incident-regulatory-reporting](../skills/incident-regulatory-reporting/SKILL.md)
- **Inputs:** IR declaration; whatever facts exist (often almost none).
- **Actions:** open the decision log with entry zero: date/time of awareness, who became aware, and of what — this timestamp anchors every clock and will be scrutinized later. Join the IR bridge. Establish the fact-pull cadence (what the regulatory track needs from IR at each sync: data categories, record counts, affected jurisdictions, service impact, attacker actions).
- **Outputs:** opened decision log; awareness timestamp; sync cadence agreed with IR lead.

### 2. Regulatory characterization — compliance-officer and privacy-officer

- **Skill:** [regulatory-applicability](../skills/regulatory-applicability/SKILL.md) (incident-scoped pass) plus [incident-regulatory-reporting](../skills/incident-regulatory-reporting/SKILL.md)
- **Inputs:** applicability profile; current facts.
- **Actions:** determine which regimes this specific incident could engage: personal data breach regimes (GDPR Art. 33/34, US state breach laws, HIPAA, others), operational/sectoral regimes (NIS2, DORA, GLBA/FTC Safeguards), securities disclosure (SEC 8-K Item 1.05 for material incidents), and contractual duties (customer contracts, cyber insurance, vendor DPAs where we are the processor — processor-to-controller notification duties run fast). Record "could engage / cannot engage / unknown" per regime with rationale in the decision log. Re-run this step every time facts change materially.
- **Outputs:** engaged-regime list, logged with rationale.

### 3. Notification decision table — compliance-officer chairs; counsel advises

- **Skill:** [incident-regulatory-reporting](../skills/incident-regulatory-reporting/SKILL.md) (decision table)
- **Inputs:** engaged-regime list; per-regime thresholds; current facts.
- **Actions:** build one table, one row per regime: threshold test, facts for/against meeting it, decision (notify / do not notify / undetermined — re-review by <time>), deadline, decider. Key discipline: **"undetermined" is a valid state but must carry a re-review time**, because clocks may be running regardless. For GDPR, a decision not to notify must itself be documented with reasoning (accountability under Art. 33(5) — the internal record obligation applies even when no notification is made). For SEC Item 1.05, log the materiality-determination process: the four-business-day clock runs from the materiality determination, and the determination itself must be made without unreasonable delay.
- **Outputs:** notification decision table; every row logged in the decision log with decider and time.
- **Decision gate:** any "notify" row immediately spawns steps 4-5 for that regime. Any "undetermined" row past its re-review time is escalated, not silently extended.

### 4. Deadline tracking — grc-analyst

- **Skill:** [incident-regulatory-reporting](../skills/incident-regulatory-reporting/SKILL.md) (deadline tracker)
- **Inputs:** decision table.
- **Actions:** maintain a single visible tracker of every live clock with its anchor event: e.g., NIS2 early warning 24h and incident notification 72h from awareness, plus final report at one month; GDPR Art. 33 within 72h of awareness (phased/supplemented filing permitted); SEC 8-K Item 1.05 four business days from materiality determination; individual notification duties (GDPR Art. 34 "without undue delay" where high risk; state laws vary). Set internal deadlines at 50-75% of the legal deadline. Review the tracker at every IR sync.
- **Outputs:** live deadline tracker with owner per deadline.

### 5. Notification drafting and filing — privacy-officer (data regimes) / compliance-officer (sectoral, securities); counsel reviews

- **Skill:** [incident-regulatory-reporting](../skills/incident-regulatory-reporting/SKILL.md) (drafting)
- **Inputs:** current confirmed facts; regime-specific content requirements; filing channel details.
- **Actions:** draft to each regime's required content, stating only confirmed facts, clearly marking preliminary information as preliminary, and committing to supplement. Keep drafts consistent **across** regimes and with any public statements — regulators read each other's filings and your press releases. Counsel reviews before filing; where privilege strategy matters, drafting flows through counsel. File through the correct channel; capture proof of submission (receipt, reference number, timestamped copy).
- **Outputs:** filed notifications with proof of filing, logged.

### 6. Supplements and follow-ups — privacy-officer / compliance-officer

- **Skill:** [incident-regulatory-reporting](../skills/incident-regulatory-reporting/SKILL.md)
- **Inputs:** evolving facts from IR; regulator questions.
- **Actions:** file supplements when material facts change (record counts revised, exfiltration confirmed or ruled out) and where regimes require staged reports (e.g., NIS2's final report within one month). Track regulator correspondence like deadlines — an unanswered regulator question is a live clock. If earlier filings contained statements now known to be wrong, correct them affirmatively; do not wait to be asked.
- **Outputs:** supplements filed; correspondence log current.

### 7. Post-incident disclosure review — compliance-officer with internal-auditor

- **Skill:** [incident-regulatory-reporting](../skills/incident-regulatory-reporting/SKILL.md) (close-out)
- **Inputs:** complete decision log; all filings; IR post-incident report.
- **Actions:** after IR closes, review: were all engaged regimes correctly identified and all deadlines met; do periodic disclosures need updating (SEC 10-K Item 106 risk-management disclosure, risk factors); do customer/vendor contractual notifications remain outstanding; what does the incident change in the risk register and control set (feed the [annual risk assessment](annual-risk-assessment.md)). Archive the decision log — it is the defense file for any subsequent enforcement inquiry.
- **Outputs:** close-out memo; archived decision log; action items into risk and control processes.

## Outputs summary

| Output | Maintained by | Why it matters |
|--------|---------------|----------------|
| Decision log | grc-analyst (scribe) | Contemporaneous defense record; the single most valuable artifact |
| Engaged-regime list | compliance-officer | Scoping of everything downstream |
| Notification decision table | compliance-officer | Every notify/don't-notify call with reasoning |
| Deadline tracker | grc-analyst | No missed clocks |
| Filed notifications + proofs | filers | Compliance evidence |
| Close-out memo | compliance-officer | Feeds disclosure, risk, and control updates |

## Failure modes

- **Waiting for perfect facts.** "We'll notify when forensics is done" — forensics takes weeks; most clocks run in hours or days. File preliminary, supplement later.
- **Clock-anchor confusion.** Measuring deadlines from incident confirmation or containment instead of awareness, or missing that SEC's clock runs from the materiality determination — and that delaying the determination itself is not a lawful strategy.
- **Regime tunnel vision.** Handling GDPR and forgetting processor contractual duties, state AGs, sector regulators, the insurer's notice-of-circumstance window, or securities disclosure.
- **Inconsistent narratives.** Press release says "no customer data affected" while a filing says "investigation ongoing." Regulators and plaintiffs collect these deltas. One fact set, one approval path for all outbound statements.
- **No decision log, reconstructed later.** Retrospective logs are visibly retrospective and forfeit the credibility a contemporaneous record buys in enforcement.
- **Undetermined-forever.** Threshold calls parked as "monitoring" without a re-review time until the deadline lapses. The step 3 gate exists for this.
- **Regulatory track blocking IR** (or vice versa). Containment delayed for a notification wording debate, or IR wiping systems the regulatory track needed evidenced. Parallel tracks, explicit syncs.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
