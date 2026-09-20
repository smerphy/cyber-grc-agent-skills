# Contributing

This repo holds practitioner-grade GRC skills that people will feed into AI agents and then rely on for compliance work. The bar is accordingly high: precise, portable, verifiable, zero fluff. Read [docs/architecture.md](docs/architecture.md) first — it defines the format and the three-layer model every contribution must fit.

## Adding a skill

1. Create `skills/<kebab-name>/SKILL.md`. Frontmatter (exactly these keys):

   ```yaml
   ---
   name: <kebab-name>            # must equal the directory name
   description: >-
     <Third person. What the skill does AND when an agent should use it,
     including trigger phrases. 300-500 chars.>
   license: MIT
   metadata:
     version: "1.0.0"
     domain: cyber-grc
   ---
   ```

2. Body sections, in this order (all required): `## Purpose`, `## When to use`, `## Inputs to gather`, `## Procedure`, `## Output format`, `## Quality checklist`, `## References`.
3. Target 150–350 body lines; the validator hard-fails at 500. Push depth — long tables, per-framework detail, question banks — into `skills/<name>/references/*.md` (self-contained, own H1, no frontmatter) and link to it from the procedure. Progressive disclosure is the core design principle, not an afterthought.
4. Cross-link with relative paths only: `../../context/regulations/gdpr.md`, `../control-testing/SKILL.md`, `references/question-bank.md`. Link to context packs instead of restating their facts.
5. "When to use" must include when **not** to use the skill, pointing at the better one.
6. "Output format" must include a short concrete worked example, not just a section list.

Pre-PR checklist for a new skill:

- [ ] `python3 scripts/validate_skills.py` passes from the repo root
- [ ] Description states trigger phrases an agent can route on
- [ ] No provider-specific syntax, tool names, or XML tags in the body
- [ ] Every regulatory/framework specific is either verified or stated generically
- [ ] Verification footer present if the file contains regulatory/framework specifics
- [ ] Related skills' References sections updated to point back where it helps routing

## Adding a context pack

A context pack is one instrument — a law, rule, framework, standard or scheme — in one file: `context/regulations/<kebab-name>.md` for a legal instrument, `context/frameworks/<kebab-name>.md` for a framework or assurance scheme. No frontmatter; the file opens with its own H1 giving the instrument's full name and citation. Packs hold facts; the procedure that uses them stays in a skill.

1. Required sections, in this order: `## At a glance` (attribute/detail table), `## What it is`, `## Who it covers / Scope`, `## Core obligations` (a framework uses `## Structure and requirements`), `## Enforcement and penalties` (a framework uses `## Assessment, certification and evidence`), `## Timeline and status`, `## Key obligations for security/GRC teams`, `## Interplay`, `## Primary sources`, then the verification footer. What belongs in each: [docs/architecture.md](docs/architecture.md).
2. **Primary sources only.** Every specific traces to the official text or its publisher — the official journal or statute book, the regulator's own guidance, the standards body's page — and `## Primary sources` lists that official URL. Where an official page could not be retrieved and a secondary source carried the point, say so on that line. Trade press, vendor blogs and consultancy summaries are not sources for a citation, a deadline or a threshold.
3. **Verification footer, always.** Close with the standard footer shown in the next section, carrying the current `Last reviewed: YYYY-MM`. State time-sensitive facts as of that date ("no final rule published as of ...") rather than as open-ended present tense.
4. **Length: roughly 90–200 lines.** That is the band the existing packs sit in. If an instrument overruns it, split by layer — the level-1 instrument and its technical standards or national transpositions become separate packs that cross-link — rather than one sprawling file.
5. **Wire it in, or it will not be found.** Add a row to the index [context/README.md](context/README.md); add a country row to the jurisdiction index [context/regulations/other-jurisdictions.md](context/regulations/other-jurisdictions.md) if the pack covers a jurisdiction not already routed; add the clock to [context/crosswalks/breach-notification-timelines.md](context/crosswalks/breach-notification-timelines.md) if the regime carries a notification deadline, or a column/row to [context/crosswalks/framework-crosswalk.md](context/crosswalks/framework-crosswalk.md) if it is a control framework; and link the pack from the skills whose procedures need it.
6. **Link, don't restate.** Neighbouring regimes get a relative link in `## Interplay`, not a second summary. Relative paths only — the validator checks every one.

Pre-PR checklist for a new pack:

- [ ] `python3 scripts/validate_skills.py` passes from the repo root
- [ ] Every required section present, in order, with the heading spelled as above
- [ ] Every citation, deadline, threshold and penalty figure verified against the official text
- [ ] `## Primary sources` lists official URLs; any secondary source flagged as such
- [ ] Verification footer present with the current `Last reviewed` date
- [ ] Index, jurisdiction index and crosswalk rows added where applicable
- [ ] No licensed standard text reproduced verbatim (see scope boundaries below)
- [ ] Provider-neutral: no tool names, no XML tags, no vendor-specific markup

## Updating regulatory or framework content

Files under `context/` (and any file citing article numbers, deadlines, control counts, or penalties) follow a strict currency discipline:

1. **Update the last-reviewed date.** Any change to a regulatory or framework fact must update that file's footer to the current `YYYY-MM`. A fact change without a date bump will be rejected.
2. **Cite the official source in the PR description.** Link the official text (EUR-Lex, eCFR/Federal Register, the framework publisher's page) and quote or reference the provision that supports the change. "Saw it in a blog post" is not a source.
3. **Keep the footer.** Every file with regulatory/framework specifics ends with:

   ```markdown
   ---
   **Verification note:** Framework and regulatory details reflect publicly
   available sources as of <period>. Verify against the official text before
   relying on them for compliance decisions. Last reviewed: YYYY-MM.
   ```

4. Do **not** add per-paragraph legal disclaimers in file bodies — the repo carries one global disclaimer and the standard footer; scattering more adds noise, not safety.

## Accuracy standard

- **No fabricated citations. Ever.** An article number, section, deadline, or control count appears only if you verified it against the official text. If you are not certain, describe the obligation generically without a citation. A plausible-but-wrong "Art. 33(4)" in an agent's context becomes a confident wrong answer to a practitioner under deadline — treat invented citations as the most serious defect class in this repo.
- Numbers agents are known to mangle (notification deadlines, control counts, thresholds) deserve extra review; call them out explicitly in your PR description so reviewers re-verify them.
- Reviewers will spot-check specifics against official sources; expect to be asked for yours.

## Scope boundaries: no proprietary framework text

Some frameworks are copyrighted, paid publications — ISO/IEC 27001 and 27002, PCI DSS, and others. Contributions must:

- **Never reproduce licensed standard text verbatim.** Full ISO control text, requirement wording from paid standards, or substantial extracts are copyright violations and will be rejected regardless of usefulness.
- **Summarize and structure at domain level instead.** Control identifiers, themes, counts, and paraphrased intent ("A.8.x addresses logging and monitoring") are fine; the standard's own sentences are not.
- The same applies to templates and references: model them on publicly available material or write them from scratch.
- Freely published frameworks (NIST publications, CIS Controls under their license terms, EU legal texts) may be quoted within their license terms — still prefer concise paraphrase; agents follow tight summaries better than pasted legalese.

## Running the validator

```bash
python3 scripts/validate_skills.py
```

Run from the repo root; Python 3.10+ with no dependencies. It checks skill frontmatter (required keys, name/directory match, description length), required H2 sections, body length, and that every relative markdown link across `skills/`, `workflows/`, `context/`, `docs/`, `agents/`, and `templates/` resolves. CI ([.github/workflows/validate.yml](.github/workflows/validate.yml)) runs the same script on every push and PR — a red validator blocks merge.

## Pull request expectations

- One logical change per PR: one new skill, one regulation update, one doc fix. Don't bundle a new skill with unrelated context edits.
- PR description states **what changed, why, and (for regulatory content) the official source**.
- Validator green before requesting review.
- Wording follows the house voice: direct, imperative, specific. No throat-clearing openers, no filler ("it is important to note that..."), no marketing adjectives. If a sentence doesn't change what the agent does, delete it.
- Keep files provider-neutral; anything provider-specific goes in `docs/integrations/` only.
- Breaking changes to a skill's output format bump `metadata.version` major and note migration impact in the PR.

## Questions

Open an issue for format questions, proposed new skills (describe the task, trigger phrases, and intended deliverable), or disputes about a regulatory specific — the official text wins every dispute.
