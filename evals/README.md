# Eval Harness

Regression tests for the *advice itself*. Each scenario is a realistic GRC task with a machine-gradable rubric of findings a competent response must contain (and wrong claims it must not). Run them when changing skills or context packs, when adopting a new model, or when comparing providers — the goal is catching quality regressions in the guidance, the same way unit tests catch code regressions.

## Layout

```
evals/scenarios/<id>/prompt.md    the task, incl. which skill/context files to load
evals/scenarios/<id>/rubric.json  required findings (regex alternatives, points),
                                  forbidden claims (penalties), pass threshold
```

## Running

**Grade existing answers** — produce an answer per scenario however you like (any provider, any harness), save as `<answers-dir>/<scenario-id>.md`, then:

```bash
python3 scripts/run_evals.py --answers /path/to/answers
```

**Generate and grade in one step** — give a command that reads a prompt on stdin and writes the answer to stdout (e.g. a CLI agent):

```bash
python3 scripts/run_evals.py --exec 'claude -p' --answers /tmp/eval-answers
```

The runner prints a per-check scorecard per scenario and exits non-zero if any scenario lands under its threshold.

## Honest limits

Grading is pattern-based: it verifies that specific facts, identifiers, and reasoning markers appear (with alternatives for phrasing) and that known-wrong claims don't. It cannot judge nuance, tone, or completeness beyond the rubric — treat a pass as "no known regression," not "good advice," and spot-read answers periodically. Rubrics live next to the scenarios; extend them whenever a real-world failure mode is found (that's the point).

## Writing a new scenario

1. Pick a task with objectively checkable outputs (deadlines, regime identification, control references — not open-ended strategy).
2. Write `prompt.md` naming the exact skill and context files to load, then the scenario input. Fictional entities only.
3. Write `rubric.json`: each required check needs `id`, `description`, `points`, and `any` (list of case-insensitive regex alternatives — write 2-4 phrasings). Add `forbidden` entries for the classic wrong answers (e.g., "SEC 4 days from detection").
4. Calibrate: a strong answer should score ≥ threshold comfortably; a weak one shouldn't. Test both.
