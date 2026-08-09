# Internal Context Overlay

Everything else in `context/` is public knowledge — frameworks and regulations. This directory holds the other half of real GRC work: **your organization's own facts**. Skills constantly need them ("gather the risk appetite statement", "identify the approval authority", "which regulators supervise you?"); this overlay gives those inputs a standard, loadable home instead of a fresh interview every session.

## The files

| File | What it holds | Skills that consume it |
|---|---|---|
| [organization-profile.md](organization-profile.md) | Legal entities, sectors, footprint, regulators, certifications, key roles | regulatory applicability, incident reporting, audit prep — almost everything |
| [risk-appetite.md](risk-appetite.md) | Appetite statements, scoring thresholds, risk-acceptance authority matrix | risk assessment, exception management, board reporting |
| [policy-index.md](policy-index.md) | Index of internal policies with owners and review dates | policy review, gap assessment, audit preparation |
| [control-catalog.md](control-catalog.md) | Internal control set with owners and framework mappings | control mapping, control testing, gap assessment |
| [system-inventory.md](system-inventory.md) | Key systems with criticality tiers, data classes, owners | risk assessment, BC/DR, incident reporting, DPIA |

## The status marker — how agents know what's real

Every file in this directory opens with a status line:

- `**Status: TEMPLATE — not filled in.**` — the file's tables and examples are **illustrative only**. Agents must not cite anything in it as an organizational fact; treat the input as "not provided" and ask the user or flag the gap, exactly as if the file didn't exist.
- `**Status: FILLED — maintained by <owner>; last updated YYYY-MM.**` — the contents are organizational facts and can be relied on, subject to the update date. If the date looks stale for the task at hand (e.g., an inventory a year old during incident scoping), say so.

Fill a file partially if that's what you have — delete the example rows you don't replace, and keep the marker at TEMPLATE until the content is trustworthy. A half-filled file marked FILLED is worse than an empty one: agents will treat leftover examples as facts.

## Keeping it private

These files contain exactly what you don't publish: your risk positions, control gaps, system inventory. If your copy of this repository is public:

- Maintain the real overlay in a **private fork or private mirror**, and treat the public repo as upstream, or
- keep real values in a private location and add `context/internal/*.md` (except this README) to your fork's `.gitignore` before filling anything in.

In a private repository, fill the files in place and version them like everything else — org context changes are reviewable diffs, and the git history *is* your update log.

## Validation

The repository validator link-checks this directory but exempts it from the verification-footer and primary-sources rules that apply to regulatory content — these files are your data, on your review cycle. The `document owner` line in each file is the review mechanism; put the overlay on the same annual refresh as the policies it indexes.
