# Style: Assurance Formal

A conservative audit-house format in the tradition of Big Four assurance and internal-audit reporting: findings-led, rating-driven, with heavy document control and a management-response column on every finding. Choose it when the deliverable is an audit report, control assessment, or anything a regulator, external auditor, or audit committee will file rather than read once. No affiliation with any firm — this is a format specification, not a brand.

Use this spec when `branding/brand-profile.md` selects `style: assurance-formal`. Profile overrides (logo, palette, fonts, footer) apply on top of everything below.

## Principles — these govern every formatting decision

1. **Findings are the product.** The report exists to state findings, their ratings, and management's response. Everything else — background, scope, methodology — supports the findings and stays brief.
2. **Rate everything, define the ratings.** Every finding carries a severity from a defined scale (e.g., Critical / High / Medium / Low, or Priority 1–3) and the scale's definitions appear in the report itself, not by reference. An undefined rating is an opinion, not a finding.
3. **Condition, criteria, cause, consequence.** Each finding states what is (condition), what should be (criteria, citing the control, policy, or clause), why the gap exists (cause), and what it exposes (consequence). Recommendations address the cause, not the symptom.
4. **Management owns the response.** Every finding closes with a management response: agreed action, named owner, target date — or a documented disagreement. A finding without a response is a draft.
5. **Traceability over narrative.** Findings are numbered and stable across drafts; evidence is referenced by identifier; scope inclusions and exclusions are explicit. A reader must be able to reconstruct what was tested and what was not.
6. **Formal register throughout.** No informality, no humor, no rhetorical flourish. The report may be read in a dispute; write accordingly.

## Document anatomy

1. **Cover** — engagement title, entity and period covered, report date, report classification, distribution list reference, logo (profile) or text wordmark.
2. **Document control** *(always, never trimmed)* — version history table (version, date, author, change summary), approver, distribution list, review/expiry date.
3. **Executive summary** — one to two pages: engagement objective and scope in two sentences; overall opinion or conclusion (e.g., "Satisfactory with exceptions"), stated with the rating scale it comes from; findings summary table (count by rating); the two or three findings the audit committee must know about, one paragraph each.
4. **Background, objective, and scope** — what was examined, the period, the criteria used (framework, policy set), and explicit scope exclusions. Half a page.
5. **Detailed findings** — one numbered subsection per finding: title, rating, condition / criteria / cause / consequence, recommendation, management response (owner + target date). Order by severity, then by domain.
6. **Appendices** — rating definitions, methodology and sampling approach, evidence register, glossary, follow-up status of prior findings.
7. **Back matter** — the repository's verification footer and analysis-support disclaimer stay intact on regulatory content; never strip them for layout reasons.

**Deck variant:** rarely appropriate — assurance content is a document. If a committee briefing deck is required, it carries only the opinion, the findings-by-rating table, and the top findings; the document remains the deliverable of record.

## Formatting specification (defaults — profile can override)

| Element | Specification |
|---|---|
| Palette | Charcoal primary `#2B2B2B`; restrained steel-blue accent `#33566E`; body near-black `#1A1A1A`; rules mid-gray `#B5BBC2`; background white. Color is administrative, not persuasive. |
| Rating colors | Critical `#7B241C`, High `#C0392B`, Medium `#B9770E`, Low `#1E8449` — used only in rating cells and the summary table, never in prose. Ratings must also work in grayscale: pair color with the rating word, never color alone. |
| Headings | Serif (Georgia/Times stack) or the profile's brand font, charcoal, numbered (1, 1.1, 1.2). H1 ~18pt, H2 ~14pt bold, H3 ~12pt bold. |
| Body | Serif ~10.5–11pt, 1.15–1.3 spacing, justified acceptable; margins ≥2.5 cm. Findings sections may use a two-column condition/criteria layout or labeled paragraphs — pick one and keep it for the whole report. |
| Emphasis | Bold for finding titles, ratings, and defined terms at first use. No italics for emphasis; italics reserved for document titles and Latin conventions if unavoidable. |
| Tables | Full grid acceptable (this style tolerates vertical rules); thin gray lines, header row shaded light gray `#EFF1F3`. Findings summary table always appears in the executive summary. |
| Charts | Rare. Use tables unless a trend genuinely needs a line. No decorative charts. |
| Logo | Cover: top-left, ≤20% page width. Body pages: none, or `short_name` in the running header. |
| Footer | Classification marking (left) · report reference number and footer_text (center) · page numbering "Page X of Y" (right). Every page. |

## Finding and exhibit conventions

- Findings numbered stably: **Finding 3 — Terminated users retain access beyond policy (High)**. Numbers never reshuffle between drafts; withdrawn findings leave a gap with a note.
- Each finding's evidence cited by identifier ("Evidence ref. E-12: IdP export, 2026-06-30, n = 214") and listed in the evidence-register appendix.
- Tables numbered separately from findings ("Table 2 — Findings by rating and domain") with source and as-of date beneath.
- Prior-finding follow-ups carry their original number and status (Closed / Open / Superseded).

## Language rules

- **Third-person institutional voice** ("Internal Audit assessed…", "Management has agreed to…") unless the profile's tone overrides.
- Findings state fact, not blame: "Access revocation exceeded the 24-hour standard in 9 of 25 sampled cases," never "IT failed to revoke access."
- Criteria always cited specifically (policy section, control ID, framework clause) — and per repository rules, only where confident; otherwise flag for verification rather than inventing a citation.
- **Preserve calibrated uncertainty**: sampling limitations, scope exclusions, and "verify against official text" flags are substance. State them in scope or the finding, not a buried footnote.
- Acronyms expanded at first use; glossary appendix mandatory if more than ~8.
- No superlatives, no speculation about intent, no recommendations phrased as criticism.

## Applying this to the repository's deliverables

| Deliverable (skill/template) | Assurance-formal treatment |
|---|---|
| Control test reports ([control-testing](../../skills/control-testing/SKILL.md)) | Native fit: findings with condition/criteria/cause/consequence, sampling detail in methodology appendix, workpaper references as evidence identifiers. |
| Audit preparation / readiness ([audit-preparation](../../skills/audit-preparation/SKILL.md)) | Readiness gaps presented as pre-findings with ratings and owner responses, so the format matches what the real audit will produce. |
| Gap assessment report ([framework-gap-assessment](../../skills/framework-gap-assessment/SKILL.md)) | Overall conclusion with rating scale up front; gaps as numbered findings; roadmap becomes the agreed-actions table. |
| Vendor assessments ([third-party-risk-assessment](../../skills/third-party-risk-assessment/SKILL.md)) | Verdict as an opinion statement; issues as rated findings; contractual asks as recommendations awaiting vendor response. |
| Board / committee report ([templates/grc-board-report.md](../../templates/grc-board-report.md)) | Usually better served by consulting-classic; use this style only where the committee expects audit-report form. |

Working artifacts — registers, workpapers, logs, questionnaires — keep their native template formats; this style applies to *formal assurance deliverables*.
