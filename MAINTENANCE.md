# Maintenance Policy

This repository's value depends on its regulatory content staying current. Compliance content rots on a schedule — this file defines the schedule.

## Review cadence

| Content | Cadence | Trigger |
|---|---|---|
| Regulation packs (`context/regulations/`) | **Annual minimum** per pack; sooner on known change | `Last reviewed:` date > 11 months → monthly CI opens/updates a `freshness-review` issue |
| Framework packs (`context/frameworks/`) | Annual minimum; on new framework versions | Same automation |
| Crosswalks (`context/crosswalks/`) | Whenever a linked pack changes; annual sweep | Same automation |
| `data/breach-timelines.json` | In lockstep with the breach-timelines crosswalk | Validator enforces regime-name sync with the markdown matrix |
| Skills, workflows, templates, personas | On feedback and failure modes; no fixed clock | Eval failures, issues |
| Eval rubrics (`evals/`) | Extend whenever a real-world failure mode is found | — |

## How the automation works

- `python3 scripts/validate_skills.py --stale 11` lists context packs whose `Last reviewed: YYYY-MM` footer date is more than 11 months old.
- [`.github/workflows/freshness.yml`](.github/workflows/freshness.yml) runs it monthly and opens (or comments on) a single open issue labeled `freshness-review` with the list. Closing the issue without fixing the dates just means it returns next month.
- The regular validator (`validate.yml`) blocks merges on structural problems but does **not** fail on staleness — freshness is a maintenance signal, not a build break. Maintainers may run `--stale N --fail-stale` locally or in a release checklist.

## Doing a review

For each flagged pack:

1. Open the pack's **Primary sources** links; check the instrument and regulator guidance for changes since the `Last reviewed` date (amendments, new implementing rules, changed deadlines/thresholds, enforcement shifts).
2. Apply corrections; keep the hedging discipline (specifics only where verified; otherwise "verify against the official text").
3. If deadlines changed, update **both** `context/crosswalks/breach-notification-timelines.md` and `data/breach-timelines.json`.
4. Bump `Last reviewed:` to the current `YYYY-MM` and update the source-verification note if links moved.
5. Cite what you checked in the PR description (per [CONTRIBUTING.md](CONTRIBUTING.md)).
6. Run `python3 scripts/validate_skills.py` and, ideally, the evals.

## Release checklist

1. Validator green, including `--stale 12 --fail-stale`.
2. Evals pass against the current reference model (`scripts/run_evals.py`).
3. CHANGELOG entry written; version bumped in `.claude-plugin/plugin.json`.
4. Tag `vX.Y.Z`; GitHub release notes from the CHANGELOG.
