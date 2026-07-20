# Branding & Report Design

This directory controls how formatted deliverables look — reports, board packs, assessment readouts, decks. Skills produce the *content*; this layer defines the *presentation*: structure, typography, colors, logo placement, and voice.

## How it works

1. **[brand-profile.md](brand-profile.md)** is the single file an agent reads before producing any formatted deliverable. Fill it in with your company's identity (logo, palette, fonts, tone, document conventions). Every field left as `DEFAULT` falls through to the selected style.
2. **[styles/](styles/)** holds report style specifications. The default is **[styles/consulting-classic.md](styles/consulting-classic.md)** — a top-tier strategy-consulting format (answer-first structure, assertive action titles, numbered exhibits, restrained navy palette). The profile's `style` field selects which spec applies.
3. **[assets/](assets/)** is where you drop logo and image files (`logo.svg`, `logo-dark.png`, …). Reference them from the brand profile by relative path. Nothing in `assets/` is required — with no logo, deliverables render with a text wordmark.

## Setup (two minutes)

```bash
cp branding/brand-profile.md branding/brand-profile.md.bak   # optional
# 1. Drop your logo file(s) into branding/assets/
# 2. Edit branding/brand-profile.md — replace DEFAULT values with your identity
```

That's it. Any skill that produces a formatted deliverable (gap reports, board reports, assessment readouts) will apply the profile automatically; you can also invoke it explicitly: *"Format this as a report per our brand profile."*

## Rules for agents

- **Load `branding/brand-profile.md` before producing any formatted deliverable** (a document, deck, or report intended for stakeholders — not working notes or register rows).
- Apply the selected style spec for structure and layout; apply profile overrides on top (logo, colors, fonts, footer, classification markings).
- Never invent brand elements. If the profile is all-`DEFAULT`, use the style spec's defaults and a plain text wordmark — do not fabricate a logo, tagline, or color scheme.
- Content rules always win over style rules: verification footers, "not legal advice" posture, and evidence citations are never removed for aesthetic reasons.

## Adding a style

Create `styles/<name>.md` following the structure of `consulting-classic.md` (principles → document anatomy → formatting spec → exhibit conventions → language rules), then set `style: <name>` in the brand profile. Keep specs provider-neutral: describe the format in prose and values (hex codes, font stacks) any agent can apply in markdown, HTML, DOCX, or PPTX output.
