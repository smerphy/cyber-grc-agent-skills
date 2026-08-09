# Changelog

All notable changes to this repository are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
[Semantic Versioning](https://semver.org/) applied to content: MAJOR for
restructures that break existing links/integrations, MINOR for new skills,
packs, workflows, or templates, PATCH for corrections and clarifications.

## [1.2.0] — 2026-07

### Added

- **Machine-readable data layer**: `data/breach-timelines.json` — every
  covered notification regime with typed deadlines and clock-start
  semantics; the validator enforces name-level sync with the markdown
  matrix so the two cannot drift silently.
- **Deadline calculator** (`scripts/deadline_calc.py`): computes concrete,
  sorted notification deadlines from incident timestamps, honoring
  per-regime clock-start events (awareness vs determination vs materiality
  determination), with business-day and calendar-month math.
- **MCP server** (`scripts/mcp_server.py`, stdlib-only): exposes
  `list_skills`, `get_skill`, `get_file`, `search`, and
  `compute_deadlines` to any MCP client; `.mcp.json.example` and
  `docs/integrations/mcp.md` added.
- **Eval harness** (`evals/` + `scripts/run_evals.py`): three scenarios
  (multi-regime incident notification, regulatory applicability, control
  test sampling design) with machine-gradable rubrics of required findings
  and forbidden wrong claims; grades answers from any provider.
- **Freshness automation** (`.github/workflows/freshness.yml`): monthly
  staleness check that opens/updates a `freshness-review` issue;
  `MAINTENANCE.md` documents the review cadence and release checklist.
- Validator: data-layer checks (JSON schema sanity, pack references,
  deadline types, matrix sync).
- **Greybeard persona** (`agents/greybeard.md`): senior technical reviewer —
  fatal-flaw hunting on architectures, control designs, and DR claims, with
  layered explanation of complex technical issues for any audience.
- **15 new workflows** (workflows now cover the full security-review and
  GRC process space, 8 → 23): security design review, cloud migration
  review, penetration test management, M&A security due diligence,
  internal audit engagement, control assurance cycle, finding remediation,
  regulatory exam management, exception lifecycle, quarterly board
  reporting, incident response tabletop, BC/DR exercise cycle, privacy
  program review, vendor offboarding, customer assurance response.
- **Internal context overlay** (`context/internal/`): fill-in packs for the
  organization's own facts — organization profile, risk appetite and
  acceptance authority matrix, policy index, control catalog, system
  inventory — with a TEMPLATE/FILLED status marker so agents can never
  mistake unfilled examples for organizational fact (AGENTS.md rule 8).
  Consuming skills (risk-assessment, exception-management,
  regulatory-applicability, control-mapping, policy-review) reference the
  overlay; validator link-checks it but exempts it from
  regulatory-content footer rules.
- **Branding layer** (`branding/`): user-editable `brand-profile.md` (logo,
  colors, fonts, tone, classification markings) applied to formatted
  stakeholder deliverables; `branding/assets/` for logo files; default
  report style spec `branding/styles/consulting-classic.md` — answer-first
  pyramid structure, action titles, SCR executive summary, exhibit
  conventions. Three alternative styles: `assurance-formal` (audit-house
  rated findings with management responses), `modern-minimal` (TL;DR-first
  tech-company doc style), `regulator-submission` (numbered-paragraph
  filings for authorities). Wired into the board-report template, the
  reporting and gap-assessment skills, AGENTS.md operating rules, and the
  tooling (validator link checks, docs site, bundles, MCP server).

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
  `/plugin marketplace add smerphy/cyber-grc-agent-skills` then
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
