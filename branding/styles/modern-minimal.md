# Style: Modern Minimal

A contemporary tech-company document style: plain language, a TL;DR block up front, tight tables, one accent color, and zero ceremony. Choose it for startups, engineering-adjacent audiences, and internal documents that live in wikis and docs tools rather than printed PDFs — where consulting-classic would read as overdressed. No affiliation with any firm — this is a format specification, not a brand.

Use this spec when `branding/brand-profile.md` selects `style: modern-minimal`. Profile overrides (logo, palette, fonts, footer) apply on top of everything below.

## Principles — these govern every formatting decision

1. **TL;DR first.** Every document opens with a labeled TL;DR: three to five bullets covering the conclusion, the numbers that matter, and the ask. A reader who stops there has the decision-relevant picture.
2. **Plain language, short sentences.** Write like a strong engineering design doc: direct, concrete, no corporate register. "We can't pass SOC 2 until access reviews exist" beats any longer version of the same fact.
3. **Scannable structure.** Short sections, descriptive sentence-case headings, bulleted lists over paragraph blocks, tables for anything with more than two attributes. Assume the reader is skimming on a laptop, not studying a printout.
4. **One accent, used sparingly.** A single accent color carries links, callouts, and chart emphasis. Status uses the defined RAG colors and nothing else. Everything else is grayscale.
5. **Show the data, skip the decoration.** Inline numbers, small tables, and simple charts — no cover pages, no letterheads, no filler sections kept for form's sake. If a section would be empty, delete it.
6. **Decisions and owners are explicit.** End with a "Decisions needed" or "Next steps" block naming owner and date for each item. A doc with no ask says so in the TL;DR ("FYI — no decision needed").

## Document anatomy

1. **Title block** — document title (plain, descriptive), one-line summary, author/owner, date, status tag (Draft / In review / Final), classification if the profile sets one. No cover page.
2. **TL;DR** — labeled block, 3–5 bullets, always first. Bold the single most important line.
3. **Context** — only what the reader needs to follow the rest; two or three short paragraphs maximum. Link out to background rather than restating it.
4. **Body sections** — findings, analysis, options. Each section leads with its takeaway in bold, then supporting detail as bullets and small tables. Use callout blocks for warnings and key caveats.
5. **Decisions needed / next steps** — table: item, owner, date, status. This is the section the document exists for.
6. **Appendix / details** — collapsible-style detail sections ("Details: full control mapping") for per-item data, methodology, and evidence tables.
7. **Back matter** — the repository's verification footer and analysis-support disclaimer stay intact on regulatory content; never strip them for layout reasons.

**Deck variant:** avoid decks where a doc will do — this style's native habitat is the document. If a deck is required: white slides, sentence-case titles that state the takeaway, one point per slide, big numbers, no slide furniture (no logos on every slide, no decorative footers).

## Formatting specification (defaults — profile can override)

| Element | Specification |
|---|---|
| Palette | Near-black text `#111418` on white; single accent `#4F46E5` (indigo) for links, callout borders, and chart emphasis; borders and rules light gray `#E3E5E8`; secondary text mid-gray `#5C616B`. |
| RAG / status colors | Red `#D64545`, amber `#E8A13C`, green `#2F9E60` — status pills or bold colored words, always paired with the status word. |
| Headings | Sans-serif (Inter/system-ui stack), near-black, sentence case, tight spacing above/below. H1 ~22pt, H2 ~15pt semibold, H3 ~12.5pt semibold. No numbering unless the doc exceeds ~10 sections. |
| Body | Sans-serif ~10–11pt (or 15–16px on screen), 1.4–1.5 line spacing, left-aligned, narrow measure (~70–80 characters). |
| Emphasis | Bold for takeaways and key figures; inline code style for identifiers (control IDs, system names). No italics for emphasis, no ALL CAPS. |
| Tables | Minimal: header rule + light row separators, no vertical lines, no shading. Keep to ≤6 columns; split or pivot anything wider. |
| Charts | Simple line/bar, one emphasized series in the accent, direct labels, no gridline clutter, no 3-D, no dual axes. A big single number with a label often beats a chart. |
| Callouts | Thin accent left border + light background for the caveat or warning the reader must not miss. One per section maximum. |
| Logo | Title block only, small, or none — `short_name` in text is fine. Never a logo on every page. |
| Footer | Minimal: classification (if set) and page numbers for exported/printed copies; nothing in the on-screen version. |

## Exhibit conventions

- Tables and figures take short bold lead-ins instead of numbered exhibit titles ("**Access review coverage by system**"), with source and as-of date in small text beneath ("Source: IdP export, 2026-06-30 · n = 214").
- Numbered exhibits only in long documents where cross-referencing is needed.
- Every number still traces to named evidence — informal tone never loosens the evidence rule.
- Status pills/words in tables come from the defined RAG set; no ad-hoc colors.

## Language rules

- **Direct and concrete.** Short sentences, active voice, verbs over nominalizations ("we tested" not "testing was performed").
- Contractions are fine; slang and humor are not — the doc may end up in front of an auditor.
- **Preserve calibrated uncertainty**: confidence levels, "verify against official text" flags, and open-questions lists are substance. A "What we don't know yet" bullet in the TL;DR is encouraged when material.
- Acronyms expanded at first use; link to the glossary instead of appending one.
- Numbers: round to what the decision needs; "~" for estimates; show n for small samples.
- Voice: first-person-plural ("we recommend") unless the profile's tone says otherwise.

## Applying this to the repository's deliverables

| Deliverable (skill/template) | Modern-minimal treatment |
|---|---|
| Gap assessment report ([framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md)) | TL;DR with readiness verdict + top 3 gaps; one compact table per domain; roadmap as the next-steps table. |
| Risk assessment readout ([risk-assessment](../../skills/risk-assessment/SKILL.md)) | Top risks as a tight table with status pills; register detail linked or in a details section. |
| Board / committee report ([templates/grc-board-report.md](../../templates/grc-board-report.md)) | Works for founder-led boards and exec staff readouts; formal boards usually warrant consulting-classic. Keep the decisions-requested table regardless. |
| Vendor assessments ([third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md)) | Verdict in the TL;DR; issues as a table with severity pills; contractual asks in next steps. |
| Incident notification decision table ([incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md)) | The decision table **stays a table**; TL;DR carries the regimes triggered and the earliest deadline in bold. |

Working artifacts — registers, workpapers, logs, questionnaires — keep their native template formats; this style applies to *narrative deliverables for stakeholders*.
