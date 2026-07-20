# Brand Profile

Agents: read this file before producing any formatted deliverable (report, deck, board pack, assessment readout). Apply the selected style spec first, then the overrides below. Any field set to `DEFAULT` falls through to the style spec's defaults. Never invent values for empty fields.

```yaml
# ---- identity ----
company_name: DEFAULT            # e.g. "Halvard Payments B.V."
short_name: DEFAULT              # e.g. "Halvard" — used in running headers
logo_light: DEFAULT              # path in branding/assets/ for light backgrounds, e.g. assets/logo.svg
logo_dark: DEFAULT               # variant for dark backgrounds; DEFAULT = reuse logo_light or text wordmark
logo_placement: DEFAULT          # DEFAULT = per style spec (cover: centered; pages: top-right, small)

# ---- style selection ----
style: consulting-classic        # a file in branding/styles/ (without .md):
                                 #   consulting-classic  — strategy-consulting format (default)
                                 #   assurance-formal    — audit-house findings-and-ratings format
                                 #   modern-minimal      — tech-company doc style, TL;DR-first
                                 #   regulator-submission — numbered-paragraph filings for authorities

# ---- palette (hex; DEFAULT = style spec palette) ----
color_primary: DEFAULT           # headings, cover band, exhibit accents
color_accent: DEFAULT            # highlights, callouts, chart emphasis series
color_neutral_dark: DEFAULT      # body text
color_neutral_light: DEFAULT     # rules, table borders, backgrounds
status_colors: DEFAULT           # DEFAULT = style spec RAG colors; override as {red: "#…", amber: "#…", green: "#…"}

# ---- typography (DEFAULT = style spec) ----
font_headings: DEFAULT           # e.g. "Georgia, serif" or a licensed brand font name
font_body: DEFAULT               # e.g. "Arial, Helvetica, sans-serif"
font_data: DEFAULT               # tables/figures; DEFAULT = font_body

# ---- voice ----
tone: DEFAULT                    # DEFAULT = style spec (direct, assertive, evidence-led). Override e.g. "formal UK English, no contractions"
language_variant: DEFAULT        # e.g. "en-US", "en-GB"

# ---- document conventions ----
classification_marking: DEFAULT  # e.g. "CONFIDENTIAL — INTERNAL USE ONLY"; DEFAULT = "Confidential" on cover only
footer_text: DEFAULT             # e.g. "© 2026 Halvard Payments B.V. · Prepared by Security & Compliance"
date_format: DEFAULT             # e.g. "D MMMM YYYY"; DEFAULT = ISO 8601 (YYYY-MM-DD)
page_numbering: DEFAULT          # DEFAULT = "Page X of Y", bottom right
disclaimer_text: DEFAULT         # appended to formal deliverables; DEFAULT = the style spec's analysis-support disclaimer

# ---- ownership ----
document_owner: DEFAULT          # e.g. "GRC Team — grc@example.com"
review_cycle: DEFAULT            # e.g. "Annual" — shown in document control tables
```

## Notes for whoever fills this in

- **Logo files** go in [assets/](assets/) — SVG preferred, PNG fallback. If your logo only works on one background, provide both `logo_light` and `logo_dark`.
- **Brand fonts** that aren't universally available should list a fallback stack (`"Founders Grotesk, Arial, sans-serif"`) so deliverables degrade gracefully.
- **Don't override the content safeguards.** Verification footers, evidence citations, and the analysis-not-legal-advice posture are content rules, not branding, and stay regardless of style.
- Keep this file in version control like everything else — brand changes are reviewable diffs.
