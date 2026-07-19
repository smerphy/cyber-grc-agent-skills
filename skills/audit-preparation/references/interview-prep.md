# Control-Owner Interview Preparation

How to brief control owners and subject-matter experts before auditor interviews and walkthroughs. Interviews are where audits are won or lost: evidence problems can be recollected; a control owner who describes a control that doesn't match the evidence creates a finding no recollection can fix.

## What an auditor interview actually is

An interview (or walkthrough) serves the auditor three purposes:

1. **Corroboration** — does the person's description match the documented control and the evidence?
2. **Understanding** — how does the control really operate, including the parts not written down?
3. **Fraud/override probing** — are there ways around the control, and does the interviewee know of any?

Inquiry alone is the weakest form of audit evidence, so auditors use interviews to decide *what to inspect harder*. Every inconsistency, hedge, or overclaim in an interview converts into an expanded evidence request. The goal of prep is not to script answers — it is to ensure answers are accurate, bounded, and consistent with the evidence already submitted.

## The seven rules (give these to every interviewee)

1. **Answer the question asked, then stop.** Do not volunteer adjacent topics, planned improvements, or history. "Do you review access quarterly?" — "Yes, each quarter I export the user list from the admin console and review it against the team roster." Done. Unprompted mention of "we used to miss quarters back in 2023" opens a line of inquiry.
2. **Describe what you actually do, not what the policy says.** Auditors read the policy before the interview. Reciting it back is a red flag; describing a practice that *differs* from it is a finding either way — but an honest description lets the team fix the policy or the practice. A description that matches neither policy nor evidence is the worst outcome.
3. **"I don't know — I'll follow up by [date]" is a good answer.** Guessing is not. A wrong guess is an inconsistency the auditor must chase. Log the follow-up on the PBC tracker immediately.
4. **Never speculate about other teams' controls.** "That's owned by the infrastructure team; I can connect you with them." Speculation creates cross-team inconsistencies that take days to untangle.
5. **Know your own evidence.** Re-read what was submitted for your controls before the interview. If you describe a monthly review and the submitted evidence shows quarterly, the interview just impeached your own evidence.
6. **Precision over reassurance.** Say "the tool blocks deployment if the approval field is empty" not "it's impossible to deploy without approval". Absolute claims ("always", "never", "impossible") invite the auditor to find the one counterexample. Say what the mechanism is; let the mechanism be impressive.
7. **If a known issue comes up, state the prepared position.** For pre-disclosed items: what happened, period affected, compensating controls, remediation status. Calm, factual, no minimizing ("it's not a big deal") and no catastrophizing.

## What auditors probe for, by theme

Prepare interviewees for these standard probe patterns:

### Exception paths and overrides
- "What happens if the approver is on vacation?" — probing for undocumented bypasses.
- "Has the control ever been skipped? When? Who authorized it?" — honest answer plus the exception record beats a "never" the ticket data contradicts.
- "Can anyone push directly to production?" — probing admin/break-glass paths. Know the break-glass procedure and its logging.

### Precision and diligence of review controls
- "Walk me through the last review you performed." — the single most common walkthrough request. The interviewee should be able to do this with the actual artifact on screen.
- "How long does the review take you?" — a 5,000-line access review "completed" in 10 minutes tells the auditor the review is a rubber stamp.
- "What would cause you to flag something? When did you last flag something?" — a review that has never found anything is a review the auditor doubts. Knowing a real example of a caught-and-fixed item is powerful evidence of operating effectiveness.
- "What threshold do you investigate at?" — for management review controls (ITDM-adjacent), the auditor needs the review's precision: what would this review actually catch?

### Segregation of duties
- "Can you approve your own request?" — know whether the system technically prevents it or process prevents it, and answer exactly that.
- "Who else can do what you do?" — know the admin population for your systems.

### Consistency across interviewees
- Auditors ask the same question of multiple people and compare. Prep sessions should align on *facts* (what the process is), never on *scripts*. If two owners describe the process differently, reconcile before fieldwork — one of them is describing a practice drift.

### Change and incident specifics
- "Tell me about the last emergency change / last security incident." — auditors love recency because it's hard to prep. The owner should review the most recent 2-3 instances of their process before the interview.

## The 30-minute prep session (per interviewee)

1. **(5 min) Context** — audit type, period, which controls this person owns, when their interview is.
2. **(10 min) Evidence review** — walk their submitted evidence items together; confirm they can explain each artifact and reproduce the extraction if asked.
3. **(10 min) Mock questions** — run the probe patterns above for their control types. Correct overclaiming and speculation in the moment.
4. **(5 min) The seven rules + logistics** — who else is in the room, how to hand off out-of-scope questions, how follow-ups get logged.

Run a full-length mock interview (not just the 10-minute segment) for:
- First-time interviewees.
- Owners of controls with a pre-disclosed issue or prior-year finding.
- Anyone whose evidence QA revealed inconsistencies.

## During fieldwork: interview logistics

- Assign a **scribe** (audit liaison, not the interviewee) to every interview to capture questions asked, answers given, and commitments made. Every "I'll get back to you" becomes a tracker row the same day.
- Keep interviews to the invited attendees. Well-meaning colleagues who jump in with "actually, we also…" are a leading source of scope expansion.
- If an interviewee realizes post-interview that an answer was wrong, correct it proactively through the liaison within 24 hours. A volunteered correction is routine; a discovered inconsistency is a credibility problem that taints the rest of their testimony.
- Debrief after each interview day: new follow-ups, apparent auditor concerns, inconsistencies to reconcile before the next session.

## Anti-patterns that create findings

| Anti-pattern | What the auditor concludes |
|---|---|
| Reciting the policy verbatim | Owner doesn't actually operate the control |
| "That never happens" (then the population shows it did) | Owner unaware of own process; expand testing |
| Blaming a tool or another team unprompted | Control environment problem; probe governance |
| Overexplaining a simple question | Something is being managed; keep digging |
| Two owners describing the same process differently | Process is undocumented practice; test both variants |
| "We're fixing that in Q3" volunteered about an untested area | New scope: what exactly is broken today? |
