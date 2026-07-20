# Security Policy

## Reporting a vulnerability

This repository contains markdown content and a small stdlib-only Python validator — there is no deployed service and no runtime attack surface beyond the validator script and CI workflow. If you find a security issue (for example, a malicious link introduced into a content file, a CI workflow weakness, or a supply-chain concern), please report it privately:

- Use GitHub's **"Report a vulnerability"** (Security → Advisories → Report a vulnerability) on this repository, or
- Open a regular issue *without exploit details* asking a maintainer to contact you.

Please do not disclose exploitable details in public issues before maintainers have responded. You can expect an acknowledgment within 7 days.

## Content integrity

A different kind of "security" matters more here: **the integrity of compliance guidance**. If you find content that could cause a compliance failure if relied upon (a wrong deadline, threshold, or obligation), report it with the **Content error** issue template — those reports are triaged with the highest priority. Every factual claim in this repository is expected to be traceable to the official sources linked in each pack's `## Primary sources` section.

## Scope notes for users

- Treat this library as analysis support, not legal advice — keep a human accountable for compliance decisions.
- The validator (`scripts/validate_skills.py`) uses only the Python standard library and makes no network calls.
- CI runs on GitHub-hosted runners with the default `GITHUB_TOKEN` permissions; no secrets are required by any workflow.
