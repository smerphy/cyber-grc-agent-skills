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
