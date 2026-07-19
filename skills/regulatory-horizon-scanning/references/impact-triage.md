# Impact Triage Rubric and Example Horizon Register Entries

Companion to the regulatory-horizon-scanning skill. Apply the three gates in order — most
developments exit at gate 1 or rate Low at gate 3, keeping the register short enough to govern.

## Gate 1: Applicability screen

Answer from the development's own scope provisions plus the org's applicability register.

| Question | Screen for |
|---|---|
| Territorial reach | Establishment-based, market/offering-based (extraterritorial hooks like "offering goods or services to persons in X"), or infrastructure-location-based? |
| Sector / activity | Sector-specific (financial, health, critical infrastructure, defense supply chain) or economy-wide? |
| Entity class and thresholds | Size thresholds (revenue, headcount), entity designations (essential/important, covered entity, financial entity, listed company, data fiduciary class), volume thresholds (records processed, transactions)? |
| Role | Does it bind the org directly, or via role (controller vs processor, provider vs deployer, manufacturer vs importer)? Different roles carry different obligation sets. |
| Reach through contracts | Even if not directly bound, will customers or partners flow obligations down contractually (common with financial-sector and public-sector regimes)? |

Outcomes:
- **In scope** — proceed to gate 2.
- **Possibly** — proceed to gate 2, but flag the open scope question and assign someone to
  resolve it (often requires counsel).
- **Out** — record identifier, date, and one-line reason in an out-log. Do not re-triage next
  cycle unless scope provisions change.

## Gate 2: Timeline extraction

Capture every date the text fixes, and characterize the unfixed ones.

| Concept | Distinguish |
|---|---|
| Legislative stage | Consultation → proposal → adopted → published → in force → applicable → enforced. Text can change materially until adoption; effort estimates on proposals need wide error bars. |
| Entry into force vs application | Many EU regulations enter into force days after publication but apply 12–36 months later, often in phases. The application date is the compliance deadline; record each phase separately. |
| Transposition (directives) | The member-state deadline, then each national implementing law's own dates. National laws may gold-plate — the national text governs. |
| Secondary rulemaking | Where obligations depend on delegated acts, RTS/ITS, or agency rules not yet final, the real deadline may be "X months after the technical standard is adopted." Record the trigger event and monitor it. |
| Transition and sunset windows | Certification transition periods after standard revisions; prior-version sunset dates (e.g., an old standard version ceasing to be assessable); grandfathering clauses. |
| Enforcement posture | Regulators sometimes announce grace periods or enforcement priorities. These affect urgency but never the legal deadline — record both, never substitute one for the other. |

Output per development: a dated timeline of phases, each tagged fixed / estimated / trigger-dependent, with the primary-source citation and verification date.

## Gate 3: Obligations delta

Compare against the current baseline, not against zero.

1. List the development's obligation categories (governance, risk assessment, technical
   measures, documentation, reporting/notification, third-party requirements, individual
   rights, conformity assessment/certification, disclosure).
2. For each, mark: **Already met** (by which existing control, framework clause, or process —
   cite it), **Partially met** (what is missing), **New capability** (nothing exists).
3. The delta is the partial + new set. Estimate effort class: documentation-only /
   process change / new tooling or capability / structural (org design, new roles, budget).
4. Note any long-lead items: capabilities that take longer to build than the remaining lead
   time (re-architecture, certifications with audit queues, hiring). Long-lead items can force
   an Act-now band even when the deadline is distant.

## Impact rating criteria

Rate on the org's delta and exposure. One High criterion suffices for High.

| Dimension | High | Medium | Low |
|---|---|---|---|
| Bindingness | Mandatory, in-scope confirmed | Mandatory but scope unresolved, or binding via contract flow-down | Voluntary guidance; early proposal likely to change |
| Delta / effort | New capability or structural change; long-lead items present | Process/documentation change within existing programs | Already met via existing baseline; mapping exercise only |
| Sanctions & exposure | Revenue-based fines, license/authorization risk, personal liability for management, disclosure obligations with market impact | Meaningful fines or supervisory orders; reputational exposure | Nominal penalties; low enforcement likelihood |
| Lead time | Hard deadline < 18 months (or long-lead items consume the margin) | 18+ months with feasible plan | No fixed date; multi-year horizon |
| Strategic fit | Blocks or conditions a planned market entry, product launch, or deal | Affects roadmap items at the margin | No roadmap interaction |

Urgency band is then set by lead time against remaining effort:
- **Act now:** applicable in < 6 months, or already applicable, or long-lead delta exceeds the
  remaining margin whatever the date.
- **Plan:** 6–18 months; formal gap assessment and budget cycle placement.
- **Watch:** > 18 months or trigger-dependent date; monitor for text/status changes only.

Re-rate every cycle. Ratings decay: a Watch item with a fixed date becomes Plan, then Act now,
purely by time passing — the register must move items without waiting for news.

## Example horizon register entries

### Example 1 — real development (dates verified as of 2026-07; re-verify before reuse)

| Field | Entry |
|---|---|
| ID | HR-2026-014 |
| Development | EU AI Act — Regulation (EU) 2024/1689, high-risk AI system obligations (Annex III) |
| Issuing body / jurisdiction | European Parliament & Council / EU |
| Status | In force; phased application |
| Key dates | In force 1 Aug 2024. Prohibitions + AI literacy applied 2 Feb 2025. GPAI obligations applied 2 Aug 2025. Most Annex III high-risk obligations apply 2 Aug 2026. Extended transition for high-risk AI embedded in products covered by listed EU product legislation. Verified: EUR-Lex, 2026-07. |
| Applicability | In — org deploys a candidate Annex III system (employment screening model); role: deployer, possibly provider if fine-tuning crosses the provider threshold (open question, with counsel). |
| Obligations delta | Partially met: risk management (existing model governance covers ~half). New: technical documentation, conformity assessment path, logging/record-keeping to required standard, human oversight documentation, registration. |
| Impact | High — mandatory, deadline < 6 months, delta includes new capabilities. |
| Urgency band | Act now |
| Owner | AI Governance Lead |
| Actions & next review | Classification memo done 2026-06; gap assessment in progress; provider/deployer question with counsel due 2026-07-31. Next review 2026-08-01. |

### Example 2 — illustrative (hypothetical; shows an amendment to an in-force regime)

| Field | Entry |
|---|---|
| ID | HR-2026-021 |
| Development | [State X] SB 123 — amendment to breach notification statute: adds 30-day notification deadline and expands "personal information" to include biometric identifiers |
| Issuing body / jurisdiction | State X legislature / US state |
| Status | Adopted; signed; effective 1 Jan 2027 |
| Key dates | Effective 2027-01-01, no transition period. Verified: state legislature enrolled bill text, 2026-07. |
| Applicability | In — org holds State X resident data above the statute's threshold; already subject to the current version. |
| Obligations delta | Partially met: IR plan has notification workflow but no deadline tracking per state; biometric data not currently tagged in the data inventory. Changes: update IR runbook deadline matrix, extend data classification to biometrics, refresh breach counsel playbook. |
| Impact | Medium — process/documentation change within existing IR program; AG-enforced penalties per violation. |
| Urgency band | Plan (about 6 months lead; effort small) |
| Owner | Privacy Officer, with IR manager |
| Actions & next review | Runbook update scheduled Q4 2026; feeds breach-notification deadline matrix update. Next review 2026-10-01. |

### Example 3 — illustrative (hypothetical; shows a framework revision as a horizon event)

| Field | Entry |
|---|---|
| ID | HR-2026-030 |
| Development | Revision of a certified management-system standard (e.g., a future ISO/IEC 27001 revision cycle), with an expected 3-year certification transition window from publication |
| Issuing body / jurisdiction | ISO/IEC JTC 1/SC 27 / international |
| Status | Committee stage — no published text; publication date estimated, not fixed |
| Key dates | Trigger event: publication of the revised standard starts the transition clock. Certification bodies stop issuing certs against the old version partway through the window. Verified: SC 27 project status, 2026-07. |
| Applicability | In — org holds certification to the current version; customer contracts require maintaining it. |
| Obligations delta | Unknown until draft stabilizes; historically revisions restructure controls and add themes, requiring SoA rework, control re-mapping, and transition audit. |
| Impact | Low (today) — no text, no date; certification maintenance is routine capability. |
| Urgency band | Watch — escalate to Plan on DIS-stage draft publication. |
| Owner | ISMS Manager |
| Actions & next review | Monitor SC 27 stage codes quarterly. Next review 2026-10-01. |

Note what the three examples demonstrate: a real phased regulation in the Act-now band, an
amendment whose delta is small because the baseline regime is already handled, and a
trigger-dependent standards revision correctly parked at Watch with an explicit escalation
condition. Hypothetical entries in this file are labeled as such — never copy them into a real
register without replacing every fact.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
