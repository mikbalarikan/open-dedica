"""D8 helper: the REPORT's gate table (section 3) and the gate rows of its JSON block,
generated from 01_CAD/check_od_c10_top_v01b.json so no number is retyped. Prints
markdown to stdout and writes 01_CAD/report_rows_v01b.json. Standard library only."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
j = json.loads((HERE / "check_od_c10_top_v01b.json").read_text())


def fmt(v, unit=""):
    if v is None:
        return "—"
    if isinstance(v, float):
        s = f"{v:.4f}".rstrip("0").rstrip(".") if abs(v) < 1e5 else f"{v:.1f}"
        if s in ("-0", ""):
            s = "0"
        return s
    return str(v)


def at(a):
    if a in (None, "", []):
        return "—"
    s = str(a)
    return s if len(s) < 60 else s[:57] + "..."


def status(r):
    s = r["status"]
    if s == "PASS_ASSUMED":
        return "PASS (assumed: " + ", ".join(r.get("assumes", [])) + ")"
    return s


lines = ["| Gate | Measured | Required | Margin | At | Status | Assumes |", "|---|---|---|---|---|---|---|"]
rows = []
for r in j["gates"]:
    unit = r.get("unit") or ""
    meas = fmt(r.get("measured")) + (f" {unit}" if r.get("measured") is not None and unit else "")
    lines.append(f"| {r['gate']} | {meas} | {r.get('required')} | {fmt(r.get('margin'))} | {at(r.get('at'))} | "
                 f"{status(r)} | {', '.join(r.get('assumes', [])) or '—'} |")
    m = r.get("measured")
    rows.append({"gate": r["gate"], "measured": m if isinstance(m, (int, float)) else None, "unit": unit,
                 "required": str(r.get("required")), "margin": r.get("margin"), "at": at(r.get("at")),
                 "status": r["status"], "assumes": r.get("assumes", [])})
(HERE / "report_rows_v01b.json").write_text(json.dumps(rows, indent=1))
print("\n".join(lines))
