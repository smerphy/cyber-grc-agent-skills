#!/usr/bin/env python3
"""Compute regulatory notification deadlines from incident timestamps.

Reads data/breach-timelines.json (the machine-readable companion to
context/crosswalks/breach-notification-timelines.md) and computes concrete
deadlines for the regimes you select, honoring each regime's clock-start
semantics — awareness vs. discovery vs. determination vs. materiality
determination are different events, often hours or days apart.

Usage (run from anywhere; stdlib only):

  python3 scripts/deadline_calc.py --list
  python3 scripts/deadline_calc.py \\
      --regime gdpr --regime nis2 --regime sec-8k \\
      --when awareness=2026-07-14T06:40Z \\
      --when discovery=2026-07-14T06:40Z \\
      --when materiality_determination=2026-07-16T17:00Z

Any deadline whose basis event has no supplied timestamp is listed as
PENDING with the event it needs. Business-day math skips Sat/Sun only —
it is NOT holiday-aware. Output is a markdown table sorted by deadline.

This is analysis support, not legal advice; verify every deadline against
the official text (see each regime's pack) before filing.
"""

import argparse
import datetime
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(REPO_ROOT, "data", "breach-timelines.json")


def load_regimes():
    with open(DATA_PATH, encoding="utf-8") as f:
        return {r["id"]: r for r in json.load(f)["regimes"]}


def parse_ts(value):
    v = value.strip()
    if v.endswith("Z"):
        v = v[:-1] + "+00:00"
    ts = datetime.datetime.fromisoformat(v)
    if ts.tzinfo is None:
        ts = ts.replace(tzinfo=datetime.timezone.utc)
    return ts


def add_business_days(ts, n):
    d = ts
    added = 0
    while added < n:
        d = d + datetime.timedelta(days=1)
        if d.weekday() < 5:
            added += 1
    return d


def add_calendar_months(ts, n):
    month = ts.month - 1 + n
    year = ts.year + month // 12
    month = month % 12 + 1
    # Clamp the day (Jan 31 + 1 month -> Feb 28/29).
    day = ts.day
    while day > 28:
        try:
            return ts.replace(year=year, month=month, day=day)
        except ValueError:
            day -= 1
    return ts.replace(year=year, month=month, day=day)


def compute_deadline(deadline, when):
    """Return (due_datetime | None, status_note)."""
    basis = deadline["basis"]
    dtype = deadline["type"]
    if dtype == "text":
        return None, f'"{deadline["value"]}" (no computable offset)'
    ts = when.get(basis)
    if ts is None:
        return None, f"PENDING - supply --when {basis}=<ISO timestamp>"
    if dtype == "hours":
        return ts + datetime.timedelta(hours=deadline["value"]), ""
    if dtype == "days":
        return ts + datetime.timedelta(days=deadline["value"]), ""
    if dtype == "business_days":
        return add_business_days(ts, deadline["value"]), "business days (Sat/Sun skipped; NOT holiday-aware)"
    if dtype == "calendar_months":
        return add_calendar_months(ts, deadline["value"]), ""
    return None, f"unknown deadline type '{dtype}'"


def build_rows(regime_ids, when, regimes):
    rows = []
    for rid in regime_ids:
        regime = regimes.get(rid)
        if regime is None:
            print(f"ERROR: unknown regime '{rid}' (see --list)", file=sys.stderr)
            sys.exit(1)
        for d in regime["deadlines"]:
            due, note = compute_deadline(d, when)
            offset = {"hours": f'{d["value"]}h', "days": f'{d["value"]}d',
                      "business_days": f'{d["value"]} business days',
                      "calendar_months": f'{d["value"]} month(s)',
                      "text": str(d["value"])}[d["type"]]
            hedge = " ⚠ verify" if regime.get("hedged") or "verify" in (d.get("notes") or "").lower() else ""
            rows.append({
                "regime": regime["name"] + hedge,
                "step": d["label"],
                "basis": d["basis"],
                "offset": offset,
                "due": due,
                "note": note,
                "recipient": d["recipient"],
            })
    rows.sort(key=lambda r: (r["due"] is None, r["due"] or datetime.datetime.max.replace(tzinfo=datetime.timezone.utc)))
    return rows


def render(rows, when):
    out = []
    out.append("## Computed notification deadlines\n")
    out.append("Inputs: " + ", ".join(f"`{k}` = {v.isoformat()}" for k, v in sorted(when.items())) or "none")
    out.append("")
    out.append("| Due (UTC) | Regime | Step | Clock start | Offset | Recipient |")
    out.append("|---|---|---|---|---|---|")
    for r in rows:
        if r["due"] is not None:
            due = r["due"].astimezone(datetime.timezone.utc).strftime("%a %Y-%m-%d %H:%M")
            if r["note"]:
                due += f" ({r['note']})"
        else:
            due = r["note"]
        out.append(f"| {due} | {r['regime']} | {r['step']} | {r['basis']} | {r['offset']} | {r['recipient']} |")
    out.append("")
    out.append("> Clock-start events differ by regime by design — see "
               "context/crosswalks/breach-notification-timelines.md for the semantics, "
               "and verify hedged (⚠) entries against the official text. "
               "Business-day math is not holiday-aware. Not legal advice.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Compute regulatory notification deadlines from incident timestamps.")
    ap.add_argument("--regime", action="append", default=[], metavar="ID",
                    help="regime id (repeatable); see --list")
    ap.add_argument("--when", action="append", default=[], metavar="EVENT=ISO",
                    help="timestamp for a clock-start event, e.g. awareness=2026-07-14T06:40Z (repeatable)")
    ap.add_argument("--all", action="store_true", help="compute every regime in the data file")
    ap.add_argument("--list", action="store_true", help="list regimes with their clock-start events")
    args = ap.parse_args()

    regimes = load_regimes()

    if args.list:
        for rid, r in sorted(regimes.items()):
            bases = sorted({d["basis"] for d in r["deadlines"] if d["type"] != "text"})
            flag = " (hedged - verify)" if r.get("hedged") else ""
            print(f"{rid:20s} {r['name']}{flag}")
            if bases:
                print(f"{'':20s}   clock events: {', '.join(bases)}")
        return

    when = {}
    for item in args.when:
        if "=" not in item:
            ap.error(f"--when needs EVENT=TIMESTAMP, got '{item}'")
        key, _, value = item.partition("=")
        try:
            when[key.strip()] = parse_ts(value)
        except ValueError:
            ap.error(f"cannot parse timestamp '{value}' (use ISO 8601, e.g. 2026-07-14T06:40Z)")

    regime_ids = list(regimes) if args.all else args.regime
    if not regime_ids:
        ap.error("select regimes with --regime (repeatable) or --all, or use --list")

    print(render(build_rows(regime_ids, when, regimes), when))


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
