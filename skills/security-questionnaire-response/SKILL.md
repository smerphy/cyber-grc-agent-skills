---
name: security-questionnaire-response
description: >-
  Responds to inbound security questionnaires from customers and prospects — SIG
  Lite/Core, CAIQ, custom spreadsheets, and portal submissions (OneTrust, Whistic)
  — by triaging the request, mapping questions to a canonical answer library,
  drafting strictly truthful answers, and flagging answers that create contractual
  or audit exposure for legal review. Use when asked to "fill out a security
  questionnaire", "respond to a SIG or CAIQ", or "answer a customer security review".
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Produce accurate, consistent, deadline-met responses to security questionnaires that customers and prospects send you. The output is a completed questionnaire (or portal submission) in which every answer is true today, scoped precisely, consistent with your SOC 2 report and public trust documentation, and reviewed where it could bind the company contractually — plus an updated answer library so the next questionnaire is faster. Speed comes from the library and reuse, never from optimistic answers.

## When to use

- A customer, prospect, or their TPRM platform sends a security questionnaire to complete (SIG Lite/Core, CAIQ, a custom spreadsheet, or a portal like OneTrust or Whistic).
- Sales asks "can you answer these security questions from the deal?"
- A renewal or annual reassessment questionnaire arrives from an existing customer.
- You are building or refreshing the canonical answer library between questionnaires.
- **Not for:** assessing a vendor's *inbound* questionnaire answers — that is the reverse direction; use [../third-party-risk-assessment/SKILL.md](../third-party-risk-assessment/SKILL.md). This skill is the mirror image of that one: there you evaluate answers, here you write them, and everything that skill teaches about detecting non-answers and boilerplate is exactly what your customer's assessor will apply to you. Not for preparing evidence for a formal audit — use [../audit-preparation/SKILL.md](../audit-preparation/SKILL.md). Not for writing the policies your answers cite — use [../policy-authoring/SKILL.md](../policy-authoring/SKILL.md). Gaps you discover while answering ("we said no and we should say yes") go to [../exception-management/SKILL.md](../exception-management/SKILL.md) or the risk register, not into a creative answer.

## Inputs to gather

Ask for these before starting; proceed with assumptions flagged if unavailable:

1. **The questionnaire itself** — format (spreadsheet, doc, portal), question count, and whether it is a recognized standard (SIG Lite/Core, CAIQ — see [../../context/frameworks/csa-ccm.md](../../context/frameworks/csa-ccm.md)) or custom.
2. **Deal context** — customer name, deal stage and size, internal owner (AE/CSM), and whether this customer has received answers from you before (prior versions constrain you — see step 7).
3. **Deadline** — the customer's stated date and the real drop-dead date; negotiate early if the volume is unreasonable for the window.
4. **NDA status** — is an NDA or evaluation agreement in place? SOC 2 reports, pen test summaries, and architecture detail typically require one.
5. **Current evidence set** — latest SOC 2 report (type, period, TSC scope — [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md)), ISO 27001 certificate and scope ([../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md)), pen test attestation, policy set, public trust page and subprocessor list.
6. **The answer library** — the canonical answer set with owners and review dates. If none exists, building one is step 2; structure in [references/answer-library.md](references/answer-library.md).
7. **Product/scope boundaries** — which product or service the customer is buying, since answers differ by product and between corporate and product scope.

## Procedure

### 1. Triage the request

Establish before answering a single question:

- **Is a full response needed at all?** If your trust page, standard security whitepaper, and SOC 2 report answer most of it, offer that package first — many customers accept standard documentation in lieu of a custom-completed spreadsheet. Decision point: for small deals with 300+ custom questions, escalate to the deal owner on effort vs. value before committing.
- **Deadline and format.** Portal questionnaires (OneTrust, Whistic) often lock answers after submission — draft offline, review, then enter. Spreadsheets get a working copy; never edit the customer's original directly.
- **NDA.** If no NDA exists, answer at the level of your public documentation and mark evidence items "available under NDA" — and make sure someone actually sends the NDA rather than leaving a deferral loop.
- **Who signs off.** Name the security reviewer and (if triggered — step 4) the legal reviewer now, with dates that back off from the deadline.

### 2. Map questions to the canonical answer library

- Match each question to a library entry (SIG and CAIQ questions map stably across versions; custom questions match by topic). Record the mapping — it becomes the reuse index for next time.
- For unmatched questions, mark them **new**: they need a drafted-from-scratch answer and a subject-matter owner, and they are candidates for the library in step 7.
- If there is no library, seed one now from the SOC 2 system description, ISO Statement of Applicability, and policy set — the method and entry schema are in [references/answer-library.md](references/answer-library.md). Seeding pays for itself within two questionnaires.

### 3. Draft answers under the truthfulness rules

Every answer must pass the rules in [references/answering-rules.md](references/answering-rules.md). The non-negotiables:

- **True today.** Answer the current state, not the roadmap. "We are implementing X" is an honest answer; "yes" because X ships next quarter is not. Assessors score future tense as a gap anyway.
- **Scoped precisely.** Use "Yes, with the following scope: ..." patterns. State which product, environment, and population the answer covers. Distinguish **corporate scope** (your laptops, your HR processes, your offices) from **product scope** (the platform the customer buys) — most questionnaires mix the two and most wrong answers come from conflating them.
- **Consistent with the record.** The answer must align with what the SOC 2 report, ISO certificate scope, DPA, public trust page, and subprocessor list actually say. Customers cross-check; contradictions get discovered and cost more credibility than any honest "no". If the SOC 2 report notes an exception on a control, do not describe that control as flawless.
- **Evidence-anchored.** Where the question invites it, cite the checkable artifact ("tested in our SOC 2 Type II, period ending 2026-03-31") rather than offering reassurance.

### 4. Flag exposure answers for security + legal review

Some questions are not security questions — they are contract terms wearing a questionnaire costume. Route these to security leadership **and** legal before submission:

- Commitments to specific SLAs (breach notification hours, uptime, patch windows, support response) — a questionnaire answer can be incorporated into the contract by reference.
- Audit rights, on-site assessment rights, or right to pen test your environment.
- Insurance amounts, liability, indemnification-adjacent questions.
- Commitments about data residency, retention, or deletion beyond what your DPA states.
- Anything the questionnaire asks you to "certify", "warrant", or sign.

Decision point: if the answer would grant more than your standard contract terms, the default response is "as per the agreement between the parties" or your standard term — deviations are a commercial negotiation, not a questionnaire answer.

### 5. Handle "no" answers honestly

When the true answer is no:

- Say no (or "not currently"), then state the **compensating control** and, only if real and dated, the roadmap: "No, we do not currently support customer-managed encryption keys. Data is encrypted at rest with provider-managed keys (AES-256); CMK support is on the roadmap for H1 2027."
- Distinguish **No** from **N/A**. N/A requires a reason ("N/A — we do not process cardholder data"). A bare N/A on an applicable question scores as evasion.
- Never dress a no as a yes with fine print. Patterns and rewrites: [references/answering-rules.md](references/answering-rules.md).
- If a "no" reveals a genuine gap worth fixing, log it internally (risk register or [../exception-management/SKILL.md](../exception-management/SKILL.md)) — the questionnaire just did free gap analysis for you.

### 6. Review and consistency-check before submission

- Security reviewer confirms technical accuracy; legal confirms the step 4 flags.
- Run the consistency traps list in [references/answering-rules.md](references/answering-rules.md): answers vs. SOC 2 report, vs. public trust page, vs. prior questionnaires to the same customer, vs. the DPA.
- Confirm every attachment referenced actually gets attached, and that nothing under NDA leaks into a no-NDA submission.

### 7. Submit, capture, and version

- Submit in the customer's required format; keep an exact copy of what was sent (portals: export or screenshot the final state).
- **Capture new canonical answers**: every reviewed answer to a "new" question from step 2 goes into the library with owner and review date.
- **Track versions per customer**: record customer, date, questionnaire type, answer set version, and any customer-specific deviations. Next year's reassessment will be diffed against this one — by the customer, so do it yourself first and explain material changes proactively.
- Log cycle time and reuse rate (questions answered from library vs. drafted new) — the reuse rate is your program's efficiency metric.

## Output format

Deliver a **Questionnaire Response Package**:

```
# Questionnaire Response: <Customer> — <Questionnaire type>
Date | Deal owner | Security reviewer | Legal reviewer | NDA: yes/no | Deadline

## 1. Completed questionnaire
(in the customer's format; working-copy answers below)

| # | Question | Answer | Source | Flags |
| Q12 | Is data encrypted at rest? | Yes. Customer data in the <Product> platform is
encrypted at rest using AES-256 with provider-managed keys. | Library AC-ENC-01;
SOC 2 CC6.7 | — |
| Q31 | Do you commit to 24h breach notification? | Breach notification terms are as
set out in our DPA (without undue delay, and within the timeframe agreed in the
agreement between the parties). | Library IR-04 | LEGAL — SLA commitment |
| Q47 | Do you support customer-managed keys? | Not currently. Data is encrypted at
rest with provider-managed AES-256 keys; CMK is on the roadmap (H1 2027, not
contractual). | New — drafted, added to library | — |

## 2. Review log
Flags raised, reviewer dispositions, answers changed in review.

## 3. Library updates
New entries added, existing entries revised (with review dates).

## 4. Version record
Customer, submission date/version, prior submissions, deltas from last time.
```

## Quality checklist

- [ ] Deadline, format, NDA status, and named reviewers established before drafting.
- [ ] Every answer mapped to a library entry or explicitly marked new with an owner.
- [ ] No future-tense capabilities presented as current; roadmap items dated and marked non-contractual.
- [ ] Corporate vs. product scope explicit in every answer where it could differ.
- [ ] Answers cross-checked against SOC 2 report (including exceptions), trust page, subprocessor list, and DPA — no contradictions.
- [ ] All SLA, audit-rights, liability, and certification questions flagged and dispositioned by legal.
- [ ] Every "No" carries compensating-control framing; every "N/A" carries a justification.
- [ ] Nothing NDA-gated sent without an NDA in place.
- [ ] New canonical answers captured into the library with owner and review date.
- [ ] Submission archived and version-recorded per customer; deltas from prior submissions explained.

## References

- [references/answer-library.md](references/answer-library.md) — canonical answer library structure, seeding method, example entries
- [references/answering-rules.md](references/answering-rules.md) — truthfulness rules, dangerous-answer rewrites, consistency traps
- [../../context/frameworks/soc2-tsc.md](../../context/frameworks/soc2-tsc.md) — what your SOC 2 report actually attests
- [../../context/frameworks/csa-ccm.md](../../context/frameworks/csa-ccm.md) — CCM/CAIQ background for CAIQ questionnaires
- [../../context/frameworks/iso-27001-2022.md](../../context/frameworks/iso-27001-2022.md) — certificate scope you can truthfully cite
- [../third-party-risk-assessment/SKILL.md](../third-party-risk-assessment/SKILL.md) — the reverse direction; how your answers will be scored
- [../audit-preparation/SKILL.md](../audit-preparation/SKILL.md) — evidence handling for formal audits
- [../policy-authoring/SKILL.md](../policy-authoring/SKILL.md) — fixing the policies your answers expose as missing
- [../exception-management/SKILL.md](../exception-management/SKILL.md) — routing gaps discovered while answering
