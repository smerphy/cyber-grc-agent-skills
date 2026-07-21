# Workflow: Regulatory Examination Management

```yaml
name: regulatory-exam-management
description: >-
  Managing a regulator examination, supervisory inquiry, or information request
  end to end: legal triage and a single point of contact, scope clarification,
  evidence collection to audit-grade standards, formal response drafting,
  privilege and consistency review, controlled submission with a full
  interaction log, and tracking of resulting findings and undertakings.
skills_used:
  - audit-preparation
  - regulatory-applicability
  - incident-regulatory-reporting
  - grc-metrics-reporting
typical_duration: days for a simple information request; 3-9 months for a full examination
roles:
  - compliance-officer
  - grc-analyst
```

## Trigger

- A regulator or supervisory authority announces an examination, sends an information request, questionnaire, or supervisory letter, or requests a meeting.
- A follow-up arrives on a prior incident notification or filing.
- An examiner contacts any employee directly — that contact itself triggers this workflow; the employee routes it to the compliance-officer and does not answer substantively.

## Prerequisites

- Legal counsel identified and reachable — internal or external. Counsel is engaged at step 1, before any substantive contact with the authority.
- The applicability register identifying this regulator, the regime, and the organization's obligations under it ([regulatory-applicability](../skills/regulatory-applicability/SKILL.md)); if none exists, building the relevant slice is part of step 1.
- Records of prior interactions with this authority: filings, incident notifications (see the [notification log](../templates/incident-regulatory-notification-log.md)), previous exam findings and undertakings.
- A document repository with access control — exam material is need-to-know from day one.

## Steps

### 1. Intake and legal triage — compliance-officer with counsel

- **Skill:** [regulatory-applicability](../skills/regulatory-applicability/SKILL.md) (confirming regime, powers, and obligations as framed)
- **Inputs:** the request or announcement as received; applicability register; prior-interaction records.
- **Actions:** engage counsel before anything else — the legal basis of the request (statutory power cited, voluntary vs compulsory, penalties for non-response) shapes every subsequent decision, and counsel determines whether privilege structures apply to the response work. Verify the request's authenticity and the authority's actual jurisdiction over the entity as framed — verify the cited provisions against the official text; do not accept the request's own characterization of scope. Record the response deadline and the mechanics for seeking extension. Appoint one single point of contact (normally the compliance-officer): every inbound and outbound interaction flows through that person from this moment.
- **Outputs:** triage memo (legal basis, deadline, jurisdiction check, privilege approach); named SPOC; exam file opened.
- **Decision gate:** counsel decides whether the matter is routine supervision or carries enforcement risk. Enforcement-flavored matters run under counsel's direction with litigation-hold discipline; do not proceed on the routine track by default.

### 2. Scope clarification — compliance-officer (SPOC), counsel reviewing

- **Skill:** [regulatory-applicability](../skills/regulatory-applicability/SKILL.md)
- **Inputs:** triage memo; the request's itemized questions.
- **Actions:** decompose the request into numbered items and identify ambiguities: undefined terms, unclear entity or period scope, items disproportionate to the stated purpose. Seek written clarification from the authority early — regulators expect clarifying questions, and answering the wrong question is worse than asking. Negotiate a realistic timetable where volume warrants it, before the deadline is missed rather than after. Fix the scope boundary internally: what is asked is answered; what is not asked is not volunteered.
- **Outputs:** clarified, itemized scope register (one row per question); agreed timetable.

### 3. Evidence collection and quality review — grc-analyst collects; compliance-officer reviews

- **Skill:** [audit-preparation](../skills/audit-preparation/SKILL.md) (evidence standards, applied at full strictness)
- **Inputs:** scope register; document repository; system owners.
- **Actions:** run collection like a PBC exercise with the scope register as the request list: owner, source system, due date per item. Apply the audit evidence standards to everything before it is a production candidate — completeness across all in-scope entities, correct period, system-generated extracts with query and date, screenshots with timestamps and system identifiers. Regulators judge control environments partly by evidence quality; a sloppy production invites a wider exam. Where a requested record does not exist, record that fact for an honest statement in step 4 — never reconstruct or backdate, which converts a supervision issue into a conduct issue.
- **Outputs:** evidence set indexed to scope-register items, quality-reviewed; gaps documented.

### 4. Response drafting — compliance-officer drafts; owners confirm facts

- **Skill:** [audit-preparation](../skills/audit-preparation/SKILL.md) (bounded, evidence-backed answering)
- **Inputs:** scope register; reviewed evidence set.
- **Actions:** draft in the formal register per [regulator-submission](../branding/styles/regulator-submission.md): numbered paragraphs mirroring the authority's own question numbering, each answer complete on its face and citing the exhibits that support it. Three rules with no exceptions — answer exactly what was asked and no more; every factual statement traces to evidence in the production set; never speculate. Where the honest answer is unfavorable, state it plainly with the remediation underway — regulators respond far better to candor with a plan than to discovered spin. Unknowns are stated as unknowns with a commitment to supplement, never papered over.
- **Outputs:** draft response with exhibit index.

### 5. Privilege and consistency review — counsel leads; compliance-officer supports

- **Skill:** [incident-regulatory-reporting](../skills/incident-regulatory-reporting/SKILL.md) (prior-notification record as the consistency baseline)
- **Inputs:** draft response and exhibits; prior filings, incident notifications, public statements.
- **Actions:** counsel reviews for privilege (privileged material identified and withheld or logged per the regime's rules — verify the regime's actual privilege treatment with counsel, it varies by jurisdiction) and for admissions with enforcement consequences. Then the consistency pass: check every statement against prior incident notifications, earlier exam responses, published reports, and disclosures. An inconsistency the examiner finds first becomes a credibility finding worse than either underlying fact — where the facts have genuinely changed since a prior notification, say so explicitly and explain, rather than hoping nobody compares.
- **Outputs:** cleared response; privilege log where applicable; discrepancy resolutions documented.
- **Decision gate:** counsel and the accountable executive sign off before anything is transmitted. No sign-off, no submission — regardless of deadline pressure; seek extension instead.

### 6. Submission and interaction log — compliance-officer (SPOC)

- **Skill:** [audit-preparation](../skills/audit-preparation/SKILL.md) (request tracking discipline)
- **Inputs:** cleared response; authority's transmission requirements.
- **Actions:** submit via the required channel with proof of delivery; retain the exact production as sent. Log every interaction across the whole engagement — calls, emails, meetings, on-site interview questions and answers, informal corridor exchanges — with date, participants, and substance. Interviewed staff get the same briefing discipline as audit interviewees: answer what is asked, no speculation, "I will follow up" over guessing, and every follow-up commitment lands in the log as a tracked item with an owner and due date.
- **Outputs:** submission receipt; living interaction log; follow-up tracker.

### 7. Findings and undertakings tracking — compliance-officer; grc-analyst tracks

- **Skill:** [grc-metrics-reporting](../skills/grc-metrics-reporting/SKILL.md) (tracking and executive reporting)
- **Inputs:** exam close-out letter, findings, required undertakings or remediation commitments.
- **Actions:** register every finding and undertaking with owner and committed date — commitments to a regulator are the least breakable dates the organization holds; route them through [finding remediation](finding-remediation.md) at highest escalation priority, with closure verified by evidence before any completion is reported back. Report status to the executive and board on a fixed cadence until closed. Debrief the engagement: which evidence was weak, which answers were hard to produce — and feed those into the control and readiness programs before the next exam.
- **Outputs:** undertakings register; board reporting; debrief actions.

## Outputs summary

| Output | Step | System of record |
|--------|------|------------------|
| Triage memo + SPOC appointment | 1 | Exam file (privileged as applicable) |
| Scope register + timetable | 2 | Exam file |
| Reviewed evidence set | 3 | Exam file |
| Response + exhibit index | 4 | Exam file |
| Privilege log + sign-offs | 5 | Exam file |
| Submission receipt + interaction log | 6 | Exam file |
| Undertakings register | 7 | Findings register / board reporting |

## Failure modes

- **Answering before counsel.** A well-meaning manager replies to the regulator directly within hours, conceding scope, waiving privilege positions, and framing facts badly. The SPOC rule and step-1 sequencing exist precisely for this.
- **Volunteering beyond scope.** Providing adjacent documents "to be helpful" hands the examiner a map to questions they had not asked. Answer what was asked, completely and honestly — nothing else.
- **Speculation under pressure.** An interviewee guesses at a cause or a number, and the guess becomes a fact the organization must live with or awkwardly correct. "I will follow up" is always the better answer.
- **The inconsistency trap.** The exam response contradicts the 72-hour incident notification filed months earlier because nobody compared them. Step 5's consistency pass against the notification log is mandatory, not optional polish.
- **Unlogged side channels.** Examiners talk to staff at site visits; undocumented exchanges later surface as "your organization told us X". Every interaction goes in the log, however informal.
- **Deadline heroics.** Producing unreviewed material at the deadline instead of requesting an extension early. A short, well-founded extension request costs little; a bad production is permanent.
- **Undertakings amnesia.** Commitments made to close the exam quietly missed a year later — the single fastest route to escalated supervision and enforcement. Step 7 treats them as the organization's hardest deadlines.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
