# Style: Consulting Classic (default)

The default report format for all formatted deliverables. It follows the conventions popularized by top-tier strategy consultancies (McKinsey-school document design): answer-first structure, assertive action titles, one message per exhibit, and a restrained, authoritative visual language. No affiliation with any firm — this is a format specification, not a brand.

Use this spec when `branding/brand-profile.md` selects `style: consulting-classic` (the default). Profile overrides (logo, palette, fonts, footer) apply on top of everything below.

## Principles — these govern every formatting decision

1. **Answer first (pyramid principle).** Lead with the conclusion, then the supporting arguments, then the evidence. The executive summary states the governing thought in the first sentence; every section opens with its takeaway, not its background.
2. **Action titles.** Every section heading, slide title, and exhibit title is a complete assertion that carries the message — "Access control is the largest gap and blocks SOC 2 readiness," never "Access Control Findings." A reader skimming only the titles gets the full storyline (horizontal logic).
3. **MECE structure.** Sections are mutually exclusive, collectively exhaustive. No overlapping findings, no orphan topics; if something doesn't fit the structure, the structure is wrong.
4. **One message per exhibit.** Each table or chart makes exactly one point, stated in its action title. If an exhibit needs two sentences to explain, split it.
5. **So-what discipline.** Every fact earns its place by changing a decision. Findings pair with implications; implications pair with recommendations; recommendations pair with owners and dates.
6. **80/20 the detail.** The body carries what the decision-maker needs; everything else (methods, full data, per-control detail) goes to the appendix with pointers.

## Document anatomy

Order and content for a full report (trim for shorter deliverables — but never cut the executive summary):

1. **Cover** — document title as an assertion where possible, subtitle (scope + period), company logo (profile) or text wordmark, date, classification marking, "Prepared by / Prepared for."
2. **Document control** *(formal deliverables)* — version, owner, approver, distribution, review date. One compact table.
3. **Executive summary** *(one page, never more)* — structured as **Situation → Complication → Resolution**: two or three sentences of context, the tension that prompted the work, then the governing thought and the 3–5 key messages as bold assertions with one supporting line each. Close with the decision(s) requested.
4. **Storyline sections** — each opens with its takeaway in bold, then supporting argument, then evidence (exhibits). Use kickers (one-line bold statements) to open subsections.
5. **Recommendations / next steps** — verb-first, sequenced, each with owner, effort, and date. Present as a table when more than four.
6. **Appendix** — methodology, full data tables, per-item detail, glossary of acronyms used. Reference from the body ("full control-level detail: Appendix B").
7. **Back matter** — the repository's verification footer and analysis-support disclaimer stay intact on regulatory content; never strip them for layout reasons.

**Deck variant (slides):** same storyline, one idea per slide; action title (max two lines) + one exhibit or one structured layout per slide; a tracker (small storyline navigator) in the corner of section slides; end with the next-steps slide, not a "thank you" slide.

## Formatting specification (defaults — profile can override)

| Element | Specification |
|---|---|
| Palette | Deep navy primary `#0A2540`; bright blue accent `#1F6FEB`; body text near-black `#1A1A1A`; rules and table borders light gray `#D9DCE1`; background white. Use the accent sparingly — emphasis series, callouts, links. |
| RAG / status colors | Red `#C0392B`, amber `#E67E22`, green `#1E8449` — used only for status semantics, never decoration. |
| Headings | Sans-serif (Helvetica/Arial stack), navy, sentence case. H1 ~24pt, H2 ~16pt bold, H3 ~13pt bold. No underlines, no all-caps except the classification marking. |
| Body | Sans-serif ~10.5–11pt, 1.15–1.3 line spacing, left-aligned (never justified), generous margins (≥2.2 cm). Serif (Georgia) acceptable for print-heavy documents if set in the profile. |
| Emphasis | Bold for takeaways and key figures. No italics for emphasis, no exclamation marks, no decorative icons or clipart. |
| Tables | Horizontal rules only (header rule + bottom rule + light row separators); no vertical lines, no zebra striping, no filled header backgrounds beyond a thin navy rule. Numbers right-aligned with units in the column header. |
| Charts | One series emphasized (accent color), others neutral gray. Direct-label data points instead of legends where possible. No 3-D, no gradients, no dual axes without explicit justification. |
| Whitespace | More than feels natural. One exhibit per page-third; never wrap text around exhibits. |
| Logo | Cover: centered or top-left, ≤25% page width. Body pages: small, top-right running header with `short_name`. Never stretch, recolor, or place on clashing backgrounds. |
| Footer | Classification marking (left) · footer_text (center) · page numbering (right). |

## Exhibit conventions

- Number sequentially: **Exhibit 1 —** followed by the action title ("Exhibit 3 — Three of six CSF functions score below target").
- Action title above the exhibit; **source and as-of date line below** in small text ("Source: access review exports, Q2 2026; n = 214 accounts"). Every number in a GRC deliverable traces to named evidence — the source line is where that trace lives.
- Units stated once (in the title or column header), not repeated per cell.
- Callout boxes (thin navy left border) for the one implication the reader must not miss.

## Language rules

- **Assertions, not topics.** Titles and kickers are full sentences with a verb and a so-what.
- **Verb-first recommendations** ("Stand up quarterly access reviews by Q4"), quantified wherever the evidence allows ("reduces past-SLA criticals from 34 to ≤5").
- **No hedging filler** ("it could be argued," "somewhat") — but **preserve calibrated uncertainty**: confidence levels, "verify against official text" flags, and open-facts lists are substance, not filler. State uncertainty precisely, then move on.
- Acronyms expanded at first use; a glossary in the appendix if more than ~8.
- Numbers: one decimal max in body text; ranges over false precision; "~" for estimates.
- Voice: first-person-plural professional ("we assessed," "we recommend") unless the profile's tone says otherwise.

## Applying this to the repository's deliverables

| Deliverable (skill/template) | Consulting-classic treatment |
|---|---|
| Gap assessment report ([framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md)) | Exec summary with governing thought ("The program is audit-ready in 9 of 12 domains; three gaps block certification"); one exhibit per function/domain; roadmap as the recommendations table. |
| Board / committee report ([grc-metrics-reporting](../../skills/grc-metrics-reporting/SKILL.md), [templates/grc-board-report.md](../../templates/grc-board-report.md)) | One-page posture summary up front; risk movement as a single exhibit; the "decisions requested" section is the resolution of the pyramid — never bury it. |
| Risk assessment readout ([risk-assessment](../../skills/risk-assessment/SKILL.md)) | Top risks as an exhibit with action title; register detail to appendix. |
| Incident notification decision table ([incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md)) | The decision table **stays a table** — deadlines and clock-starts are not prose candidates. Wrap with a one-paragraph situation summary and the immediate-actions list. |
| Audit readiness / vendor assessments | Verdict first ("Conditional pass — three conditions"), conditions as the recommendation set, evidence detail to appendix. |

Working artifacts — registers, workpapers, logs, questionnaires — keep their native template formats; this style applies to *narrative deliverables for stakeholders*.
