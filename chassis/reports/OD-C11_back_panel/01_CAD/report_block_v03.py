"""D8 helper: the REPORT v03 JSON block from the measured check JSON, the sweep summary and
the files on disk (hashes taken now). Standard library only. Prints the block; writes
01_CAD/report_block_v03.json. Paths relative to the workspace (pathlib)."""
import hashlib
import json
from pathlib import Path

WS = Path(__file__).resolve().parent.parent
CAD = WS / "01_CAD"
check = json.loads((CAD / "check_od_c11_back_v03.json").read_text())
sweep = json.loads((CAD / "sweep_v03" / "sweep_summary.json").read_text())

IDS = ["U-01", "U-02", "U-03", "U-04", "U-05", "U-06", "U-07", "U-08", "D-01a", "D-01b", "D-02", "D-03a", "D-03b",
       "D-04a", "D-05a", "D-05b", "D-06a", "D-07", "J-05", "E-06", "E-11", "REQ-01", "REQ-02", "REQ-03", "REQ-04",
       "REQ-05", "REQ-06", "REQ-07", "REQ-08", "REQ-09", "exactly_one_solid", "feature_census", "envelope_within_spec"]
RANK = {"FAIL": 0, "INCONCLUSIVE": 1, "PASS_ASSUMED": 2, "PASS": 3, "N/A": 4}


def gid(row_gate):
    g = row_gate.split(".")[0]
    for i in IDS:
        if g == i or g.startswith(i + "(") or g.startswith(i + " "):
            return i
    return g


gates = []
for i in IDS:
    rows = [r for r in check["gates"] if gid(r["gate"]) == i]
    if not rows:
        gates.append({"gate": i, "status": "MISSING"})
        continue
    w = min(rows, key=lambda r: (RANK.get(r["status"], 1),
                                 r["margin"] if isinstance(r.get("margin"), (int, float)) else 1e9))
    gates.append({"gate": i, "measured": w.get("measured"), "unit": w.get("unit"), "required": w.get("required"),
                  "margin": w.get("margin"), "at": w.get("at"), "status": w["status"],
                  "assumes": w.get("assumes", []), "worst_row": w["gate"], "rows": len(rows)})

files = sorted([*CAD.glob("*_v03*"), *(CAD / "probe").glob("*_v03*"), CAD / "DESIGN_PLAN_v03.md", CAD / "sweep_v03" / "sweep_summary.json",
                *(WS / "02_STEP_STL").glob("*_v03.*"), *(WS / "03_Sections").glob("*_v03_*.png")])
files = [f for f in dict.fromkeys(files) if f.is_file() and f.suffix != ".md" or f.name == "DESIGN_PLAN_v03.md"]
files = [f for f in files if f.name not in ("report_block_v03.json",)]
frows = [{"path": str(f.relative_to(WS)), "sha256": hashlib.sha256(f.read_bytes()).hexdigest()} for f in files]

PARAMS = {"flange_hole_d": ("flange_hole_d_lo", "flange_hole_d_hi"),
          "flange_hole_dx": ("flange_hole_dx_lo", "flange_hole_dx_hi"),
          "insert_d": ("insert_d_lo", "insert_d_hi"), "insert_depth": ("insert_depth_lo", "insert_depth_hi"),
          "pass_d": ("pass_d_lo", "pass_d_hi"), "wall_z": ("wall_z_lo", "wall_z_hi"),
          "y_top": ("y_top_lo", "y_top_hi")}
sw = []
for p, (lo, hi) in PARAMS.items():
    runs = [sweep[r] for r in (lo, "nominal", hi) if r in sweep]
    sw.append({"parameter": p, "runs": [lo, "nominal", hi],
               "all_built_one_solid": all(r["solids"] == 1 for r in runs) and len(runs) == 3,
               "not_pass": sorted({g for r in runs for g in r["not_pass"]}),
               "worst_gate": min(runs, key=lambda r: r["worst_mm_margin"])["worst_mm_gate"],
               "worst_margin": min(r["worst_mm_margin"] for r in runs)})

block = {"schema": "oguz-report-v1", "job_id": "20261001-od-c11-back-panel", "part": "od_c11_back", "tag": "v03",
         "spec_version": "1.2", "outcome": "SUBMITTED", "fix_cycles": "0 of 3",
         "files": frows,
         "versions": {"python": "3.13.7", "build123d": "0.11.1", "ocp": "cadquery-ocp-novtk 7.9.3.1.1",
                      "repo_commit": "10929db1408d89144bd4af9cad971440427933d0"},
         "gates": gates, "sweep": sw}
(CAD / "report_block_v03.json").write_text(json.dumps(block, indent=1, default=str))
print(json.dumps(block, indent=1, default=str))
