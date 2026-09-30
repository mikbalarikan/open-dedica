"""D7: summarise the v02 sweep (01_CAD/sweep_v02/<variant>/check.json) into
01_CAD/sweep_v02/sweep_summary_v02.json: per variant, one solid or not, the rows
that are not PASS (INCONCLUSIVE-by-row OD-H11 rows apart), and the worst margin per
gate family across the sweep. Plain Python, no CAD."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SW = HERE / "sweep_v02"
BY_ROW = {"U-03.h11.interference", "U-04.assembly.od_h11_thermoblock.volume_delta", "E-06", "REQ-09(Soft)"}
VARIANTS = {"bore_d": ("bore_d_low", "bore_d_high", [3.95, 4.0, 4.05]),
            "bore_depth": ("bore_depth_low", "bore_depth_high", [5.9, 6.0, 6.1]),
            "bore_shift (dx, dz)": ("bore_shift_low", "bore_shift_high", ["(-0.07, -0.07)", "0", "(+0.07, +0.07)"]),
            "wall_x0 / wall_x1": ("wall_low", "wall_high", ["62.9 / 66.9", "63.0 / 67.0", "63.1 / 67.1"]),
            "brail_x0": ("brail_x0_low", "brail_x0_high", [58.9, 59.0, 59.1]),
            "brail_x1": ("brail_x1_low", "brail_x1_high", [70.9, 71.0, 71.1])}


def family(g):
    return g.split(".")[0].replace("(Soft)", "").replace("(b)", "")


def load(name):
    p = HERE / "check_od_c02_bulkhead_v02.json" if name == "nominal" else SW / name / "check.json"
    return json.loads(p.read_text())["gates"] if p.exists() else None


def worst(rows):
    best = None
    for r in rows:
        if r["gate"] in BY_ROW or r.get("margin") is None or r["status"] in ("N/A",):
            continue
        if best is None or r["margin"] < best["margin"]:
            best = r
    return best


out = {"variants": {}, "parameters": []}
for pname, (lo, hi, values) in VARIANTS.items():
    runs = {}
    for tag, name in (("low", lo), ("nominal", "nominal"), ("high", hi)):
        rows = load(name)
        if rows is None:
            runs[tag] = {"name": name, "missing": True}
            continue
        solid = next((r for r in rows if r["gate"] == "exactly_one_solid"), {})
        bad = [{"gate": r["gate"], "measured": r["measured"], "required": r["required"], "margin": r["margin"],
                "status": r["status"], "at": r.get("at")}
               for r in rows if r["status"] in ("FAIL", "INCONCLUSIVE") and r["gate"] not in BY_ROW]
        w = worst(rows)
        runs[tag] = {"name": name, "one_solid": solid.get("status") == "PASS", "not_pass": bad,
                     "worst": None if w is None else {k: w.get(k) for k in ("gate", "measured", "margin", "status")}}
        out["variants"][name] = runs[tag]
    all_built = all(r.get("one_solid") for r in runs.values())
    ws = [r["worst"] for r in runs.values() if r.get("worst")]
    wmin = min(ws, key=lambda w: w["margin"]) if ws else None
    out["parameters"].append({"parameter": pname, "values": values, "all_built": all_built,
                              "failing": {t: [b["gate"] for b in r.get("not_pass", [])] for t, r in runs.items()},
                              "worst_gate": None if wmin is None else wmin["gate"],
                              "worst_margin": None if wmin is None else wmin["margin"]})
# worst margin per gate family across the sweep (nominal included)
fam = {}
for name in ["nominal"] + [n for v in VARIANTS.values() for n in v[:2]]:
    rows = load(name) or []
    for r in rows:
        if r["gate"] in BY_ROW or r.get("margin") is None:
            continue
        f = family(r["gate"])
        if f not in fam or r["margin"] < fam[f]["margin"]:
            fam[f] = {"margin": r["margin"], "gate": r["gate"], "variant": name, "measured": r["measured"],
                      "status": r["status"]}
out["worst_margin_per_gate"] = fam
(SW / "sweep_summary_v02.json").write_text(json.dumps(out, indent=1, default=str))
for p in out["parameters"]:
    print(p["parameter"], p["all_built"], p["failing"], p["worst_gate"], p["worst_margin"])
for k, v in sorted(fam.items()):
    print(f"{k:<22} {v['margin']!s:<24} {v['gate']:<45} {v['variant']:<18} {v['status']}")
