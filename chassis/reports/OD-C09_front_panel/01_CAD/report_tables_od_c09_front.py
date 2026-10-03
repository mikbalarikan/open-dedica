"""Tables for REPORT_od_c09_front_v01.md from the check and sweep JSON (no measurement here).
Usage: python report_tables_od_c09_front.py  ->  01_CAD/report_tables_v01.md and report_gates_v01.json"""
from __future__ import annotations

import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECK = HERE / "check_od_c09_front_v01.json"
SWEEP = HERE / "sweep_v01"
ORDER = {"FAIL": 4, "INCONCLUSIVE": 3, "PASS_ASSUMED": 1, "PASS": 0, "N/A": -1, "INFO": -2}


def fmt(v, unit=""):
    if v is None:
        return "—"
    if isinstance(v, float):
        if math.isnan(v):
            return "nan"
        return f"{v:.4f}".rstrip("0").rstrip(".") if abs(v) < 1e6 else f"{v:.3e}"
    return str(v)


def worst_rows(rows):
    """Per gate: the row with the worst status, then the least margin."""
    out = {}
    for r in rows:
        g = r["gate"]
        if g.startswith("_"):
            continue
        key = (ORDER.get(r["status"], 3), -(r["margin"] if isinstance(r.get("margin"), (int, float)) else 0.0))
        if g not in out or key > out[g][0]:
            out[g] = (key, r)
    return {g: v[1] for g, v in out.items()}


def main():
    data = json.loads(CHECK.read_text())
    rows = data["rows"]
    lines = ["| Gate | Item | Measured | Unit | Required | Margin | At | Status | Assumes |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        if r["gate"].startswith("_"):
            continue
        st = r["status"]
        if st == "PASS_ASSUMED":
            st = "PASS (assumed: " + ", ".join(r.get("assumes") or []) + ")"
        extra = ""
        if r.get("clearance_mm") is not None:
            extra = f" (clearance {fmt(r['clearance_mm'])} mm)"
        note = (r.get("note") or "").replace("|", "/")
        lines.append(f"| {r['gate']} | {r.get('item', '')}{(' — ' + note) if note else ''} | {fmt(r.get('measured'))}{extra} | "
                     f"{r.get('unit', '')} | {r.get('required', '')} | {fmt(r.get('margin'))} | {fmt(r.get('at'))} | {st} | "
                     f"{', '.join(r.get('assumes') or []) or '—'} |")
    worst = worst_rows(rows)
    gates_json = []
    for g, r in worst.items():
        gates_json.append({"gate": g, "item": r.get("item"), "measured": r.get("measured"), "unit": r.get("unit"),
                           "required": r.get("required"), "margin": r.get("margin"), "at": r.get("at"),
                           "status": r["status"], "assumes": r.get("assumes") or []})
    # sweep
    sw_lines = ["| Run | Overrides | Built, one solid | Gates not PASS / PASS_ASSUMED | Worst margin per gate (least of the run) |",
                "|---|---|---|---|---|"]
    sweep_json = []
    worst_by_gate = {}
    for js in sorted(SWEEP.glob("*.json")):
        if js.name in ("sweep_summary.json", "ref_cache.json"):
            continue
        d = json.loads(js.read_text())
        name = js.stem
        # U-07 gates the delivered STL; sweep runs write no STL, so their U-07 reads "no STL given"
        bad = {g: s for g, s in d["summary"].items() if s not in ("PASS", "PASS_ASSUMED", "N/A", "INFO")
               and g not in ("U-07", "REQ-08")}
        w = worst_rows(d["rows"])
        one = [r for r in d["rows"] if r["gate"] == "exactly_one_solid"]
        built = bool(one) and one[0]["status"] == "PASS"
        least = None
        for g, r in w.items():
            m = r.get("margin")
            if isinstance(m, (int, float)) and r["status"] in ("PASS", "PASS_ASSUMED", "FAIL"):
                cur = worst_by_gate.get(g)
                if cur is None or m < cur[0]:
                    worst_by_gate[g] = (m, name, r.get("item"), r.get("measured"))
                if least is None or m < least[0]:
                    least = (m, g, r.get("item"))
        sw_lines.append(f"| {name} | {json.dumps(d.get('params'))} | {'yes' if built else 'NO'} | "
                        f"{', '.join(f'{g} {s}' for g, s in bad.items()) or 'none'} | "
                        f"{(fmt(least[0]) + ' (' + least[1] + ' ' + str(least[2]) + ')') if least else '—'} |")
        sweep_json.append({"run": name, "params": d.get("params"), "built_one_solid": built, "not_pass": bad})
    wg = ["| Gate | Worst margin over the sweep | Run | Item | Measured |", "|---|---|---|---|---|"]
    for g, (m, name, item, meas) in sorted(worst_by_gate.items()):
        wg.append(f"| {g} | {fmt(m)} | {name} | {item} | {fmt(meas)} |")
    out = ["## Gate rows (all)", "", *lines, "", "## Sweep runs", "", *sw_lines, "", "## Sweep worst margin per gate", "", *wg]
    (HERE / "report_tables_v01.md").write_text("\n".join(out) + "\n")
    (HERE / "report_gates_v01.json").write_text(json.dumps({"gates": gates_json, "sweep": sweep_json,
                                                             "summary": data["summary"]}, indent=1, default=str))
    for g in gates_json:
        print(g["gate"], g["status"], fmt(g["measured"]), g["unit"], g["item"])


if __name__ == "__main__":
    main()
