# Changelog

All notable changes to this repository are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
[Semantic Versioning](https://semver.org/) applied to content: MAJOR for
restructures that break existing links/integrations, MINOR for new skills,
packs, workflows, or templates, PATCH for corrections and clarifications.

## [1.1.0] — 2026-07

### Added

- **Four new skills**: `security-questionnaire-response` (answering inbound
  customer questionnaires from a canonical answer library),
  `dsar-handling` (data subject rights requests across regimes),
  `ropa-data-mapping` (GDPR Art. 30 records and data mapping),
  `bcdr-readiness` (BIA, recovery-gap analysis, exercise programs) —
  21 skills total; personas updated to recommend them.
- **Claude Code plugin packaging** (`.claude-plugin/plugin.json` +
  `marketplace.json`): install everything with
  `/plugin marketplace add smerphy/Cyber-GRC-Agent-Skills` then
  `/plugin install cyber-grc@cyber-grc-skills`.
- **Install script** (`scripts/install.sh`): copy or symlink any subset of
  skills into project or user scope.
- **Provider bundles** (`scripts/build_bundles.py`): per-persona knowledge
  bundles under `dist/`, including 20-file variants sized for Custom GPT
  limits, each with a manifest of contents and omissions.
- **Worked examples** (`examples/`): incident notification decision table,
  NIST CSF 2.0 gap assessment excerpt, vendor SOC 2 report review.
- **Documentation site**: mkdocs-material configuration and GitHub Pages
  workflow (`.github/workflows/docs.yml`), assembled by
  `scripts/build_docs_site.py`; architecture diagram added to the README.

## [1.0.0] — 2026-07

Initial public release.

### Added

- **17 skills** in the portable Agent Skills format (`SKILL.md` + `references/`):
  framework gap assessment, control mapping, policy authoring/review, risk
  assessment, exception management, third-party risk, GRC metrics & board
  reporting, audit preparation, control testing, incident regulatory
  reporting, regulatory applicability, DPIA, AI governance, SOC 2 readiness,
  ISO 27001 readiness, regulatory horizon scanning.
- **19 framework packs** (`context/frameworks/`): NIST CSF 2.0, ISO/IEC
  27001:2022, CIS Controls v8, SOC 2 TSC, NIST SP 800-53 r5, SP 800-171 +
  CMMC 2.0, FedRAMP, PCI DSS v4, HITRUST CSF, CSA CCM v4, COBIT 2019,
  NERC CIP, NIST AI RMF, ISO/IEC 42001, ISO/IEC 27701, ISO 22301, ACSC
  Essential Eight, UK Cyber Essentials, TISAX.
- **26 regulation packs** (`context/regulations/`): GDPR, NIS2, DORA, EU AI
  Act, EU CRA, CER Directive, ePrivacy, UK regime, HIPAA, US state privacy,
  SOX ITGC, SEC cyber disclosure, GLBA/FTC Safeguards, NYDFS Part 500,
  CIRCIA, FISMA, US sectoral privacy, Australia, Canada, Singapore, Japan,
  South Korea, India, China, Brazil, plus a jurisdiction index with
  Switzerland, Saudi Arabia, UAE, South Africa, New Zealand, Israel.
- **Crosswalks**: domain-level framework crosswalk; breach-notification
  deadline matrix across all covered regimes with clock-start semantics.
- **8 workflows**, **11 templates**, **6 personas**, glossary, risk-scoring
  methods.
- **Primary sources** section in every framework/regulation/crosswalk pack,
  linking the official text or publisher (links verified 2026-07).
- **Validator** (`scripts/validate_skills.py`): skill format, cross-file
  links, verification footers with parseable review dates, primary-sources
  presence, workflow/persona headers with resolvable skill references, CSV
  integrity, and a `--stale N` freshness report. Runs in CI on every push
  and PR.
- Integration guides for Claude, OpenAI, and generic providers;
  architecture documentation; contribution, security, and issue/PR
  templates.
