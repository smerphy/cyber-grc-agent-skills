# Style: Regulator Submission

A formal public-record format for documents addressed to regulators, supervisory authorities, and external counsel: numbered paragraphs, neutral institutional voice, complete self-containment, and formatting that survives grayscale printing and document management systems. Choose it for notification letters, formal responses to regulator inquiries, and filings — documents where precision and completeness outrank readability, because the audience is obligated to read every word and may quote any of them. No affiliation with any authority — this is a format specification, not a brand.

Use this spec when `branding/brand-profile.md` selects `style: regulator-submission`. Profile overrides (logo, palette, fonts, footer) apply on top of everything below.

## Principles — these govern every formatting decision

1. **Every paragraph numbered, every claim addressable.** Continuous paragraph numbering (1, 2, 3 …) through the whole document so any statement can be cited as "paragraph 14" in later correspondence. Structure serves reference, not persuasion.
2. **Answer what was asked, in the order asked.** When responding to an inquiry or a statutory requirement, mirror the regulator's own question numbering or the regulation's article structure. Do not reorganize for narrative effect.
3. **Complete and self-contained.** The document stands alone in a file: full entity identification, reference numbers, the legal basis for the submission, and all attachments enumerated. Assume the reader has no other context and no access to prior emails.
4. **State facts; date them; bound them.** Every factual statement carries its as-of date and known limitations ("as of 18 July 2026, forensic review of 3 of 5 affected systems is complete"). Preliminary information is labeled preliminary, and the update mechanism is stated.
5. **No advocacy dressed as fact.** Characterizations ("robust", "industry-leading") are omitted or attributed. The document may be tested against evidence later; write only what the evidence supports.
6. **Counsel review is part of the format.** This style's deliverables are exactly the documents the repository's rules flag for legal review — the draft states "DRAFT — subject to counsel review" until that review has occurred.

## Document anatomy

1. **Letterhead block** — entity legal name, registered address, and identifiers (registration/LEI where relevant); recipient authority and addressee; date; subject line stating the document's nature and reference ("Re: Notification under [provision] — [entity] — ref. [internal ref.]"); regulator's reference number if responding.
2. **Introduction** — numbered paragraphs stating who is submitting, in what capacity, under what obligation or request, and what the document contains. Cite the provision relied upon only where confident; otherwise describe the obligation and flag for verification.
3. **Body** — numbered paragraphs in the structure the obligation dictates (e.g., for an incident notification: nature of the incident, timeline, categories and volumes affected, measures taken, measures planned, contact point). Headings are plain and descriptive, never rhetorical.
4. **Limitations and updates** — what is not yet known, why, and when supplementary information will follow ("a supplementary report will be provided by [date] in accordance with [provision]").
5. **Closing** — contact point (name, role, address, phone, email), signature block (name, title, entity), and the list of enclosures, each numbered ("Enclosure 2 — Timeline of events, 3 pages").
6. **Enclosures** — each with its own title page carrying the parent reference and enclosure number.
7. **Back matter** — the repository's verification footer and analysis-support disclaimer belong on the *internal draft*; strip repository footers from the version actually filed, but never file without counsel review.

**Deck variant:** none. Supervisory meetings take a document plus, at most, a one-page numbered summary in the same style.

## Formatting specification (defaults — profile can override)

| Element | Specification |
|---|---|
| Palette | Black text on white. No accent color in the filed document. Internal-draft annotations may use one muted highlight `#8A6D3B`, removed before filing. |
| Status colors | None. Severity and status are words, not colors — the document must be identical in grayscale, photocopy, and plain-text extraction. |
| Headings | Same face as body, bold, sentence case, optionally numbered (1., 1.1). No color, no rules under headings. |
| Body | Serif (Times/Georgia stack) ~11–12pt, 1.15–1.5 spacing, left-aligned or justified per local convention, margins ≥2.5 cm. Continuous paragraph numbers in the left margin or leading each paragraph. |
| Emphasis | Minimal. Bold only for headings and defined terms at first definition; never for advocacy. No italics except document titles and foreign terms. |
| Tables | Simple full-grid tables with thin black lines; every table numbered and titled with its as-of date; units in column headers. Tables carry facts (timelines, counts), never styling. |
| Charts | Avoid. If genuinely necessary, monochrome, directly labeled, and duplicated as a data table in an enclosure. |
| Dates and numbers | Unambiguous date format — ISO 8601 or fully written ("18 July 2026"); never numeric day/month forms that vary by locale. Times carry the time zone. Exact counts where known; bounded ranges where not ("no fewer than 4,100 and no more than 4,600 records"). |
| Logo | Letterhead only. Nothing decorative anywhere else. |
| Footer | Entity reference and page "X of Y" on every page, including enclosures. Classification marking per profile on internal drafts. |

## Reference and enclosure conventions

- One internal reference for the matter, carried on every document and enclosure in the correspondence chain.
- Enclosures numbered in citation order; the body cites them as "(Enclosure 2)" — never "see attached."
- Facts in the body trace to evidence held internally; the body states the fact and date, the evidence register (internal) records the source. Do not attach raw evidence unless required or requested.
- Quotations from regulation or prior correspondence are exact, in quotation marks, with the source cited — and only where the text is available and confirmed; otherwise paraphrase and flag for verification.

## Language rules

- **Institutional third person or first-person-plural formal** ("The Company became aware…", "We confirm that…"). Consistent throughout; no voice mixing.
- Full sentences, no contractions, no rhetorical questions, no bullet fragments in the filed body (bullets acceptable inside tables and enclosures).
- Terms used as defined in the applicable regulation; where the entity's internal terminology differs, define the mapping once.
- **Preserve calibrated uncertainty** — it is the substance of a good filing: "preliminary", "under investigation", "expected to be confirmed by", each with a date. Never state a preliminary figure as final.
- No admissions of legal conclusion ("we breached Article X") — state facts; leave legal characterization to counsel.
- Acronyms expanded at first use, even common ones; the reader's file may be reviewed by someone outside the domain.

## Applying this to the repository's deliverables

| Deliverable (skill/template) | Regulator-submission treatment |
|---|---|
| Regulator notifications ([incident-regulatory-reporting](../../skills/incident-regulatory-reporting/SKILL.md)) | Native fit: notification letters and supplementary reports in this format, structured per the regime's required content; the internal decision table stays internal. |
| Notification log ([templates/incident-regulatory-notification-log.md](../../templates/incident-regulatory-notification-log.md)) | Stays in its native template — it is a working artifact; this style formats the outbound letters it tracks. |
| DPIA excerpts for supervisory consultation ([dpia-privacy-assessment](../../skills/dpia-privacy-assessment/SKILL.md)) | Consultation submissions in this format; the working DPIA keeps its template. |
| Responses to regulator inquiries / audit requests | Mirror the inquiry's numbering; one numbered response per question; enclosures for evidence the regulator requested. |
| Board / internal reports | Wrong style — use consulting-classic or modern-minimal internally, and translate into this format only at the regulator boundary. |

Working artifacts — registers, workpapers, logs, questionnaires — keep their native template formats; this style applies to *documents addressed to authorities and external counsel*.
