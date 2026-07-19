# Board-Level Security Reporting

The board's job is oversight, not operations: are the major risks understood, is management handling them competently, is the trajectory acceptable, and where is a board-level decision needed? Every element of the report either serves one of those four questions or wastes the scarcest resource in the room — minutes of directed attention. Boards of US public companies also describe their cyber oversight in the 10-K (Item 106); a coherent reporting process is part of what gets described — see `../../../context/regulations/sec-cyber-disclosure.md`.

## Structure of an effective board risk report

Target: 5-7 slides or 2-3 pages for a 10-15 minute slot, plus appendix. Order matters — lead with judgment, not data.

### 1. Posture statement (one slide)

A plain-language answer to "how exposed are we, and is that within what we agreed to tolerate?"

- One or two sentences of overall position against risk appetite, in words: "We remain within appetite in all areas except third-party concentration, where we are outside appetite and expect to return within it by Q1 following the <X> migration."
- Top 3-5 risks, each with: business impact framing (money, downtime, records, regulatory exposure), current rating, direction arrow since last report, and one-line treatment status.
- Nothing else on this slide. No architecture, no tool names, no threat statistics.

### 2. Movement since last report

What changed and why — this is where trend earns its place:

- Risks that moved (up or down) with the cause: environment change, new information, treatment completed, treatment slipped.
- Incidents above the board reporting threshold (define that threshold once with the board — severity, regulatory notification triggered, material cost — and honor it symmetrically: report qualifying incidents even when the quarter was embarrassing).
- Program milestones: delivered / slipped, with slip reasons owned plainly ("we deprioritized X to absorb the acquisition" beats "resource constraints").
- Metric threshold breaches and the response underway — only breached metrics get airtime; green metrics live in the appendix.

### 3. External context (half slide, optional per quarter)

Threat landscape and regulatory changes *with a stated consequence for this organization*. "Ransomware groups now do X, which matters to us because Y, and we are doing Z" — never a threat-intel tour. Regulatory horizon items feed from `../../regulatory-horizon-scanning/SKILL.md`; include only those requiring board awareness or future budget.

### 4. Asks and decisions (one slide, always present)

The most important slide, and the one most reports omit:

- **Decisions requested**: risk acceptances requiring board/committee sign-off, budget approvals, policy approvals, appetite changes. Each with the decision, alternatives considered, and recommendation.
- **For awareness**: items the board should know before they read them in the news.
- If nothing is needed: state "No decisions requested this quarter" explicitly. The habit of an explicit ask slide is what keeps reporting connected to governance rather than performance art.

### 5. Appendix

Full metric table with definitions and trends, risk register extract, incident log summary, glossary. Exists for the director who digs; never presented.

## Writing rules

- **Business language.** Translate every technical impact: not "unpatched CVE-XXXX on the VPN concentrator", but "a remotely exploitable flaw in the remote-access system that, until patched Tuesday, exposed us to network intrusion of the kind behind the <peer company> breach."
- **Quantify honestly.** Ranges and confidence beat false precision: "estimated exposure $2-8M" with a stated basis beats "$4.7M" from a model nobody can defend. If using FAIR-style quantification, present the range, not the mean — see `../../../context/risk-scoring.md`.
- **Consistent structure across quarters.** Directors compare reports; a stable skeleton makes movement visible and builds trust. Change the skeleton at most annually, and flag the change.
- **Symmetry.** Report bad news with the same prominence as good. The first time a board learns of a suppressed incident from a journalist, the reporting franchise is gone.
- **One acronym rule.** Define on first use; better, don't use it. MFA and ransomware are fine; "EDR telemetry via our XDR into the SIEM" is not.
- **Attribution of judgment.** Distinguish fact ("control tests: 3 failures"), inference ("we assess vendor risk as rising"), and opinion ("I recommend accepting this risk"). Boards are professional consumers of exactly this distinction.

## Anti-patterns

| Anti-pattern | Why it fails | Fix |
|--------------|-------------|-----|
| The FUD open ("4,000% rise in attacks...") | Habituates the board; erodes credibility; supports no decision | Open with your posture, not the world's |
| The tool tour (slideware of platforms deployed) | Activity ≠ risk reduction; boards can't evaluate tools | Report risk movement; tools appear only as treatment status |
| The wall of green (30 RAG tiles, all green) | Either thresholds are meaningless or reporting is filtered; both destroy trust | Report threshold breaches; greens to appendix; ensure some ambers exist over time — a report that is never amber is broken |
| The single security score ("we are 87/100") | Composite hides the red that matters; invites score-management | Small set of named metrics with defined thresholds |
| Maturity-score-as-outcome ("CMMI 2.8 → 3.1") | Maturity is an input; boards mistake it for risk reduction | Usable annually as program context, never as the headline |
| No ask, ever | Teaches the board the item is informational; oversight atrophies | Always include the asks slide, even to say "none" |
| Heat-map theater (5×5 matrix as the whole story) | Ordinal arithmetic and clustering hide movement; see `../../../context/risk-scoring.md` | Top risks as a *list* with direction and treatment; matrix at most as appendix |
| The 40-slide deck for a 10-minute slot | Guarantees the asks slide is never reached | Fit the slot; cut until it fits; appendix absorbs the rest |
| Quarter-to-quarter metric redefinition | Breaks trends; looks like manipulation even when innocent | Version definitions; annotate any change on the chart |
| Jargon-laden incident retelling | Board retains nothing; asks no useful questions | Impact, response quality, lesson, and what changed — four sentences |
| Reporting only when things are calm | Silence during an incident quarter reads as concealment | Fixed cadence regardless; incident quarters get more candor, not less |

## Calibrating to your board

- **Ask the audience.** Annually, ask the committee chair: what did you use, what did you skip, what was missing? Adjust.
- **Know the composition.** A board with a former CISO or CIO tolerates more depth; a board without one needs the translation layer everywhere. Both need the same structure.
- **Committee vs. full board.** Audit/risk committee gets the full report; full board typically gets posture + asks only. Prepare both from one source to prevent drift.
- **Pre-wire big asks.** A budget or risk-acceptance ask should never surprise the committee chair in the meeting. The report documents the ask; the decision is socialized before.
- **Prepare for the standard questions.** "Are we secure?" (answer: posture vs. appetite, never yes/no), "Could <headline breach> happen to us?" (answer prepared per major public incident: similarity, our exposure, our compensating position), "Are we spending enough?" (answer: peer benchmarks + risk-based argument, both with stated limitations).

## Cadence and inputs

Typical rhythm: quarterly committee report; annual deep-dive (strategy, appetite refresh, program roadmap); ad-hoc briefing within days for material incidents (a materiality determination may separately trigger disclosure obligations — see `../../../context/regulations/sec-cyber-disclosure.md`).

Standing input pipeline: risk register (`../../risk-assessment/SKILL.md`), control test results (`../../control-testing/SKILL.md`), metric extracts (`metric-catalog.md`), TPRM status (`../../third-party-risk-assessment/SKILL.md`), audit findings (`../../audit-preparation/SKILL.md`), exception register (`../../exception-management/SKILL.md`). If assembling the report takes more than 2-3 days of effort, the data pipeline — not the report — is the problem to fix.

---
**Verification note:** Framework and regulatory details reflect publicly available sources as of mid-2026. Verify against the official text before relying on them for compliance decisions. Last reviewed: 2026-07.
