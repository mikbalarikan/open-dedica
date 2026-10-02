"""D7: the worst margin per sweep run and per gate, from 01_CAD/sweep_v02/<run>/check.json.
Writes 01_CAD/sweep_v02/sweep_summary.json. Standard library only."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SW = HERE / "sweep_v02"
KNOWN = ()   # v02: every row is reported; the D9 rows show in not_pass
out = {}
for d in sorted(p for p in SW.iterdir() if (p / "check.json").exists()):
    j = json.loads((d / "check.json").read_text())
    rec = json.loads((d / "build_record.json").read_text())
    rows = [r for r in j["gates"] if r.get("margin") is not None]
    fails = [r["gate"] for r in j["gates"] if r["status"] in ("FAIL", "INCONCLUSIVE")
             and r["gate"] not in ("E-06", "E-11", "REQ-09(Soft)")]
    other = [r for r in rows if r["gate"] not in KNOWN]
    # the least margin relative to its own unit, lengths first
    worst = min((r for r in other if r["unit"] == "mm"), key=lambda r: r["margin"])
    out[d.name] = {"solids": rec["solids"], "faces": rec["faces"], "variant": {k: rec["params"][k] for k in
                   ("flange_hole_d", "flange_hole_dx", "insert_d", "insert_depth", "pass_d", "wall_z_out",
                    "wall_z_in", "y_top")},
                   "not_pass": fails, "worst_mm_gate": worst["gate"], "worst_mm_margin": worst["margin"],
                   "worst_mm_measured": worst["measured"],
                   "step_sha256": rec["step"]["sha256"]}
(SW / "sweep_summary.json").write_text(json.dumps(out, indent=1))
for k, v in out.items():
    print(f"{k:<20} solids {v['solids']} faces {v['faces']} worst {v['worst_mm_gate']:<40} {v['worst_mm_margin']:<10.4g}"
          f" not_pass {v['not_pass']}")
