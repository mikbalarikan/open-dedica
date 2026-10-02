"""Turns the check results (01_CAD/results_v01/*.json) into the REPORT's tables and JSON block, so no
number is retyped. Prints markdown to stdout; writes results_v01/gate_summary_v01.json."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = HERE / "results_v01"
ORDER = {"FAIL": 0, "INCONCLUSIVE": 1, "PASS_ASSUMED": 2, "PASS": 3, "N/A": 4, "INFO": 5}


def gate_id(name):
    first = name.split()[0]
    if first.startswith("U-03"):
        return "U-03"
    if first in ("assembly", "assembly:"):
        return "assembly_file"
    return first


def fmt(v):
    if isinstance(v, float):
        return f"{v:.4f}".rstrip("0").rstrip(".") if abs(v) < 1e6 else f"{v:.1f}"
    return "—" if v is None else str(v)


def summarise(rows):
    out = {}
    for r in rows:
        g = gate_id(r["gate"])
        if r["status"] == "INFO":
            continue
        cur = out.get(g)
        key = (ORDER.get(r["status"], 9), r["margin"] if isinstance(r["margin"], (int, float)) else 1e9)
        if cur is None or key < cur[0]:
            out[g] = (key, r)
    return {g: v[1] for g, v in out.items()}


def main():
    files = {"od_c13_right": "check_od_c13_right.json", "od_c12_left": "check_od_c12_left.json",
             "od_c16_bracket": "check_od_c16_bracket.json", "od_side_assembly": "check_od_side_panels_assembly.json"}
    summary = {}
    for part, f in files.items():
        rows = json.loads((R / f).read_text())["rows"]
        print(f"\n#### {part}: every predicate ({len(rows)} rows)\n")
        print("| Gate | Measured | Unit | Required | Margin | At | Status | Assumes |")
        print("|---|---|---|---|---|---|---|---|")
        for r in rows:
            at = r["at"] if r["at"] else ""
            at = re.sub(r"\s+", " ", str(at))[:40]
            st = r["status"] if r["status"] != "PASS_ASSUMED" else f"PASS (assumed: {', '.join(r['assumes'])})"
            req = str(r["required"]).replace("|", "/")
            note = f" ({r['note']})" if r.get("note") and r["status"] in ("INFO", "N/A", "INCONCLUSIVE") else ""
            print(f"| {r['gate'].replace('|', '/')}{note} | {fmt(r['measured'])} | {r['unit']} | {req} | "
                  f"{fmt(r['margin'])} | {at} | {st} | {', '.join(r['assumes']) or '—'} |")
        summary[part] = {g: {"gate": g, "measured": r["measured"], "unit": r["unit"], "required": r["required"],
                             "margin": r["margin"], "at": r["at"], "status": r["status"], "assumes": r["assumes"],
                             "worst_row": r["gate"]} for g, r in summarise(rows).items()}
    (R / "gate_summary_v01.json").write_text(json.dumps(summary, indent=1, default=str))
    print("\n#### summary per gate id (worst row)\n")
    for part, gs in summary.items():
        for g, r in gs.items():
            print(f"{part:16s} {g:22s} {r['status']:13s} {fmt(r['measured'])} {r['unit']}  [{r['worst_row']}]")


if __name__ == "__main__":
    main()
