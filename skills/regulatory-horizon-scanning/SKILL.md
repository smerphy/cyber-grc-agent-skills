---
name: regulatory-horizon-scanning
description: >-
  Tracks upcoming regulatory and framework change and assesses organizational impact. Builds a
  jurisdiction-by-sector watchlist, identifies authoritative sources to monitor, triages each
  development for applicability and effective dates, rates impact, maintains a horizon register,
  and produces lead-time-based stakeholder briefings. Use when asked to monitor regulatory change,
  assess an upcoming law or amendment, build a horizon register, or answer "what is coming that
  affects us."
license: MIT
metadata:
  version: "1.0.0"
  domain: cyber-grc
---

## Purpose

Regulatory horizon scanning converts a stream of legislative proposals, adopted texts, delegated
acts, enforcement guidance, and framework revisions into a prioritized register of changes the
organization must prepare for — with enough lead time to act. This skill provides the method:
watchlist definition, source selection, triage, impact rating, register maintenance, and
stakeholder briefing. It produces a living horizon register, not a one-off memo.

**Critical caution:** An LLM's knowledge of regulations is frozen at its training cutoff.
Proposals get amended, effective dates slip, delegated acts land, and enforcement positions
change after that date. Never present model knowledge as the current state of a pending
regulation. This skill defines the scanning METHOD; every substantive claim about a development's
status, text, or dates must be sourced from a current authoritative publication (see
[references/source-catalog.md](references/source-catalog.md)) and cited with a retrieval date.
If current sources cannot be checked in the working environment, label all status statements as
"as of [model cutoff / last verified date] — verify before use."

## When to use

- Establishing or refreshing a regulatory change monitoring program.
- Assessing a specific upcoming development ("What does the new X act mean for us?").
- Building or updating a horizon register for board, risk committee, or compliance reporting.
- Prioritizing readiness work across multiple pending obligations.
- **Not for:** determining which regulations apply to the org *today* — that baseline comes
  first; use [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md).
- **Not for:** deciding whether a live incident triggers a notification duty — use
  [../incident-regulatory-reporting/SKILL.md](../incident-regulatory-reporting/SKILL.md).
- **Not for:** measuring compliance against a regime already in force — use
  [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md).

## Inputs to gather

Ask for these before starting; proceed with stated assumptions if unavailable and flag the gaps:

1. **Applicability register** (or equivalent): jurisdictions of establishment and of offering,
   sectors, entity classifications (e.g., NIS2 essential/important, public company, covered
   entity, financial entity). If none exists, run
   [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md) first or capture
   a minimal version: jurisdictions, sector, data types, customer base, listing status.
2. **Strategic roadmap signals:** planned market entries, new products (especially AI features,
   payment handling, health or children's data), M&A pipeline — these expand the watchlist
   beyond current applicability.
3. **Existing horizon register or tracker**, if any, plus who consumes it and how often.
4. **Compliance baseline:** which frameworks/regimes the org already meets, to compute
   obligations deltas rather than restating whole regulations.
5. **Stakeholder map:** who owns readiness decisions (CISO, DPO, GC, product, finance) and the
   reporting cadence (monthly ops review, quarterly risk committee).
6. **Scanning capability:** does the operator have live web/source access this session, or is
   this a register-structure and triage exercise on developments the user supplies?

## Procedure

1. **Define the watchlist.** Build a matrix of jurisdictions × sectors × topics from the
   applicability register plus roadmap signals. Topics typically include: cybersecurity
   regulation, privacy/data protection, incident/breach reporting, AI governance, operational
   resilience, sector rules (financial services, health, critical infrastructure), securities
   disclosure, and the voluntary frameworks the org certifies against (ISO, SOC 2, PCI DSS —
   framework revisions are horizon events too). Explicitly record what is OUT of scope so the
   register's silence is meaningful.

2. **Select authoritative sources.** For each watchlist cell, pick primary sources (official
   journals, regulator sites, standards bodies) and optionally secondary aggregators for early
   signal. Use [references/source-catalog.md](references/source-catalog.md). Rules:
   - Primary sources are the only citable authority for status, text, and dates.
   - Secondary sources (professional associations, law firm alerts) may surface developments
     early but every item must be traced back to a primary source before entering the register.
   - Record for each source: what it publishes, checking frequency, and owner.

3. **Collect developments each cycle.** For each source, capture: title/identifier, issuing
   body, document type (proposal, adopted act, delegated/implementing act, guidance,
   consultation, enforcement action, standard revision), publication date, and link. Do not
   triage during collection — separate the sweep from the analysis.

4. **Triage each development.** Apply the rubric in
   [references/impact-triage.md](references/impact-triage.md). Three gates, in order:
   - **Applicability screen:** does it plausibly reach the org (territorial scope, sector,
     entity class, thresholds)? Outcomes: In scope / Possibly (needs analysis) / Out (record
     the reason and discard — a documented "out" prevents re-triaging the same item).
   - **Timeline extraction:** legislative stage, entry-into-force date, application date(s),
     transition periods, and staged applicability (many regimes phase obligations — capture
     each phase as its own date). Distinguish "in force" from "applicable" from "enforced."
     If a date is not yet fixed (transposition pending, rulemaking open), record the range and
     the trigger event.
   - **Obligations delta:** compare the new obligations against the current compliance
     baseline. The delta — not the regulation's full text — drives effort. A regime that
     mirrors ISO 27001 controls the org already runs is low-delta even if the regulation is
     large. Use [../control-mapping/SKILL.md](../control-mapping/SKILL.md) and
     [../../context/crosswalks/framework-crosswalk.md](../../context/crosswalks/framework-crosswalk.md)
     for the comparison.

5. **Rate impact.** High / Medium / Low using the criteria table below (full rubric with
   scoring guidance in [references/impact-triage.md](references/impact-triage.md)):

   | Rating | Criteria (any one suffices for High) |
   |---|---|
   | High | New mandatory obligations with material delta; personal liability for management; significant sanctions (revenue-based fines, license/authorization risk); requires new capabilities, budget, or headcount; hard deadline < 18 months |
   | Medium | Moderate delta absorbable within existing programs; process or documentation changes; deadline 18 months or more; sanctions meaningful but not existential |
   | Low | Minimal delta (already compliant via existing frameworks); guidance-level (non-binding); early-stage proposal likely to change; monitoring-only |

   Impact rating is about the org's delta and exposure, not the regulation's public profile.

6. **Record in the horizon register.** One row per development (or per phase, if phases hit
   different owners). Schema is fixed — see Output format. Every row needs an owner and a next
   review date; a register without owners is a news feed.

7. **Brief stakeholders with lead-time-based urgency.** Map lead time to action bands:
   - **Act now (applicable in < 6 months, or already applicable with enforcement pending):**
     readiness project must be underway; escalate if no owner or budget.
   - **Plan (6–18 months):** scope the gap formally (run
     [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md)), assign
     owner, put in next planning cycle.
   - **Watch (> 18 months, or date not fixed):** monitor for text changes; no build work yet
     unless the delta requires long-lead capabilities (e.g., re-architecture, new tooling).
   Brief format per Output format below. Feed High items into the risk register via
   [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md) as emerging compliance risks, and
   into metrics reporting via
   [../grc-metrics-reporting/SKILL.md](../grc-metrics-reporting/SKILL.md).

8. **Maintain the register.** Each cycle: re-verify status of open items against primary
   sources (dates slip; texts change between proposal and adoption), advance urgency bands as
   dates approach, close items when readiness is achieved (hand off to normal compliance
   management) or the development dies, and log the review date. Retire watchlist cells when
   applicability lapses.

## Output format

**Horizon register** — one table, this schema:

| Field | Content |
|---|---|
| ID | HR-YYYY-nnn |
| Development | Official title + identifier (regulation number, bill number, standard designation) |
| Issuing body / jurisdiction | e.g., EU Parliament & Council; US SEC; UK ICO |
| Status | Proposal / Adopted / In force–not yet applicable / Applicable / Guidance / Consultation |
| Key dates | Entry into force; application date(s) per phase; transition end; source + date verified |
| Applicability | In / Possibly / notes on scope hooks (thresholds, entity class) |
| Obligations delta | 2–4 bullets: what is new vs current baseline |
| Impact | High / Medium / Low + one-line justification |
| Urgency band | Act now / Plan / Watch |
| Owner | Named role |
| Actions & next review | Current readiness actions; date of next status re-verification |

**Worked example row (verify all dates against current sources before reuse):**

> **HR-2026-014** — EU AI Act (Regulation (EU) 2024/1689), high-risk AI system obligations.
> Status: In force; obligations apply in phases. Key dates: prohibitions and AI literacy applied
> from 2 Feb 2025; GPAI obligations from 2 Aug 2025; most high-risk (Annex III) obligations
> apply from 2 Aug 2026; extended transition applies to high-risk AI embedded in regulated
> products (verified against EUR-Lex, 2026-07). Applicability: In — org deploys a hiring-
> screening model (Annex III candidate). Delta: no conformity assessment process, no technical
> documentation per Annex IV, no registration; risk-management system partially covered by
> existing model governance. Impact: **High** — mandatory obligations, material delta, deadline
> inside 6 months. Urgency: **Act now.** Owner: AI Governance Lead. Actions: classification
> confirmed 2026-06; gap assessment underway via ai-governance skill; next review 2026-08-01.

**Stakeholder brief** — per cycle, max 2 pages:
1. Register movement since last cycle (new / band changes / closed).
2. Act-now items: one paragraph each — obligation, date, delta, readiness status, decision
   needed.
3. Plan items: one line each.
4. Watch list: count + notable status changes only.
5. Source-verification statement: which sources were checked and when.

## Quality checklist

- [ ] Watchlist derives from a documented applicability register plus roadmap signals; out-of-scope areas are explicit.
- [ ] Every register entry cites a primary source with a verification date; no entry rests solely on secondary reporting or model knowledge.
- [ ] Every dated claim distinguishes entry into force, application, and phased deadlines; unfixed dates are shown as ranges with trigger events.
- [ ] Every entry has an obligations delta stated against the org's current baseline — not a summary of the regulation.
- [ ] Impact ratings match the rubric criteria; High ratings identify the specific criterion met.
- [ ] Every open entry has a named owner and a next review date; no orphan rows.
- [ ] Urgency bands are consistent with the lead-time thresholds; Act-now items appear in the stakeholder brief with a decision ask.
- [ ] Out-triaged items are logged with reasons.
- [ ] The brief states which sources were checked and when; any unverified item is flagged as such.

## References

- [references/source-catalog.md](references/source-catalog.md) — authoritative monitoring sources by jurisdiction and what each publishes.
- [references/impact-triage.md](references/impact-triage.md) — full triage rubric and example horizon register entries.
- [../../context/crosswalks/breach-notification-timelines.md](../../context/crosswalks/breach-notification-timelines.md) — deadline matrix for regimes already in force.
- [../../context/crosswalks/framework-crosswalk.md](../../context/crosswalks/framework-crosswalk.md) — for obligations-delta comparisons.
- [../../context/regulations/eu-ai-act.md](../../context/regulations/eu-ai-act.md), [../../context/regulations/nis2.md](../../context/regulations/nis2.md), [../../context/regulations/dora.md](../../context/regulations/dora.md) — recent regimes commonly on horizon registers.
- [../regulatory-applicability/SKILL.md](../regulatory-applicability/SKILL.md) — baseline applicability (prerequisite).
- [../framework-gap-assessment/SKILL.md](../framework-gap-assessment/SKILL.md) — formal gap scoping for Plan-band items.
- [../risk-assessment/SKILL.md](../risk-assessment/SKILL.md) — registering High items as emerging risks.
- [../grc-metrics-reporting/SKILL.md](../grc-metrics-reporting/SKILL.md) — horizon metrics in governance reporting.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
