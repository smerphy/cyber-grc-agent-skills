#!/usr/bin/env python3
"""Query the domain-level framework crosswalk from data/control-crosswalk.json.

Examples:
  scripts/crosswalk_query.py --ref A.8.8                 # locate an ISO control everywhere
  scripts/crosswalk_query.py --ref CC6.2 --framework soc2
  scripts/crosswalk_query.py --ref "Req 8"               # PCI requirement
  scripts/crosswalk_query.py --domain vulnerability      # fuzzy domain lookup
  scripts/crosswalk_query.py --list                      # frameworks + domains

Matching is domain-level navigation, NOT clause-level equivalence: two
frameworks landing in the same domain does not mean their controls are
interchangeable. For defensible mappings use the official publisher
mappings and skills/control-mapping. Stdlib only.
"""

import argparse
import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(REPO_ROOT, "data", "control-crosswalk.json")

CAVEAT = ("Note: domain-level navigation aid, not clause-level equivalence. "
          "For defensible mappings see context/crosswalks/framework-crosswalk.md "
          "and skills/control-mapping.")

_TRAILING_NUM = re.compile(r"^(.*?)(\d+)$")


def load():
    with open(DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


def norm(token):
    t = token.strip().lower().replace("–", "-")
    t = re.sub(r"^req\.?\s*", "", t)          # "Req 8" -> "8"
    return t.rstrip(".")


def parse_range(ref):
    """Return (prefix, lo, hi) if ref is a range like 'A.5.1-A.5.8', else None."""
    if "-" not in ref:
        return None
    left, _, right = ref.partition("-")
    ml, mr = _TRAILING_NUM.match(left), _TRAILING_NUM.match(right)
    if not (ml and mr):
        return None
    if ml.group(1) != mr.group(1):
        return None
    return ml.group(1), int(ml.group(2)), int(mr.group(2))


def ref_matches(query, ref):
    """Does a normalized query id fall under a normalized catalog ref?"""
    if query == ref:
        return True
    rng = parse_range(ref)
    if rng:
        prefix, lo, hi = rng
        m = re.match(r"^" + re.escape(prefix) + r"(\d+)($|[.\-])", query)
        return bool(m) and lo <= int(m.group(1)) <= hi
    # Family/category containment in either direction: query 'ac-2' under
    # ref 'ac'; query 'pr.aa' surfacing ref 'pr.aa-06'.
    for sep in (".", "-"):
        if query.startswith(ref + sep) or ref.startswith(query + sep):
            return True
    return False


def find_by_ref(data, query, framework=None):
    """[(framework_key, domain)] whose refs cover the queried identifier."""
    if framework is None and re.match(r"^req\.?\s*\d", query.strip().lower()):
        framework = "pcidss4"                 # "Req 8" is PCI phrasing
    q = norm(query)
    hits = []
    for domain in data["domains"]:
        for fw_key, cell in domain["mappings"].items():
            if framework and fw_key != framework:
                continue
            if any(ref_matches(q, norm(r)) for r in cell.get("refs", [])):
                hits.append((fw_key, domain))
    return hits


def find_domains(data, text):
    t = text.strip().lower()
    return [d for d in data["domains"] if t in d["id"] or t in d["name"].lower()]


def render_domain(data, domain, highlight=None):
    lines = [f"Domain: {domain['name']}  [{domain['id']}]"]
    for fw_key, meta in data["frameworks"].items():
        cell = domain["mappings"].get(fw_key, {})
        refs = ", ".join(cell.get("refs", [])) or "(no dedicated control)"
        mark = " <--" if fw_key == highlight else ""
        line = f"  {meta['name']}: {refs}{mark}"
        if cell.get("notes"):
            line += f"  ({cell['notes']})"
        lines.append(line)
    if domain.get("friction"):
        lines.append(f"  Friction: {domain['friction']}")
    return "\n".join(lines)


def render_list(data):
    lines = ["Frameworks (use the key with --framework):"]
    for key, meta in data["frameworks"].items():
        lines.append(f"  {key}: {meta['name']} — ids like {meta['id_style']}")
    lines.append("")
    lines.append("Domains:")
    for d in data["domains"]:
        lines.append(f"  {d['id']}: {d['name']}")
    lines.append("")
    lines.append("Derived frameworks (map through a parent, not the tables):")
    for f in data["derived_frameworks"]:
        lines.append(f"  {f['name']} -> {f['maps_through']} — {f['note']}")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", help="control identifier to locate, e.g. A.8.8, CC6.2, AC-2, 'Req 8', PR.AA")
    ap.add_argument("--framework", choices=None,
                    help="limit --ref search to one framework key (see --list)")
    ap.add_argument("--domain", help="fuzzy domain name/id lookup, e.g. vulnerability")
    ap.add_argument("--list", action="store_true", help="list frameworks and domains")
    args = ap.parse_args(argv)

    data = load()
    if args.framework and args.framework not in data["frameworks"]:
        ap.error(f"unknown framework '{args.framework}' — one of: {', '.join(data['frameworks'])}")

    out = []
    if args.list or not (args.ref or args.domain):
        out.append(render_list(data))
    if args.ref:
        hits = find_by_ref(data, args.ref, args.framework)
        if not hits:
            out.append(f"No domain covers '{args.ref}'"
                       + (f" in {args.framework}" if args.framework else "")
                       + ". Try --list, or a broader id (family/category).")
        else:
            seen = set()
            for fw_key, domain in hits:
                if domain["id"] in seen:
                    continue
                seen.add(domain["id"])
                out.append(render_domain(data, domain, highlight=fw_key))
    if args.domain:
        matches = find_domains(data, args.domain)
        if not matches:
            out.append(f"No domain matches '{args.domain}'. Try --list.")
        for d in matches:
            out.append(render_domain(data, d))

    out.append(CAVEAT)
    print("\n\n".join(out))


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.stderr.close()
