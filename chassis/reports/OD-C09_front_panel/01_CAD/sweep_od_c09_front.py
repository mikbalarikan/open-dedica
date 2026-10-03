"""D7 robustness sweep of od_c09_front v01: nominal, low and high of every fit-critical
parameter of DESIGN_PLAN section 4 (one at a time, as the plan's section 6 states).
Each run builds the part with build_od_c09_front.py into 01_CAD/sweep_v01/ (never
02_STEP_STL/) and runs the same predicates (check_od_c09_front.py) on its re-imported STEP.

Usage (repository root, tools venv):
    uv run tools/run.py python <ws>/01_CAD/sweep_od_c09_front.py [--jobs 3] [--only name1,name2]
Writes 01_CAD/sweep_v01/<run>.step, <run>.json, and 01_CAD/sweep_v01/sweep_summary.json.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "sweep_v01"
sys.path.insert(0, str(HERE))
from build_od_c09_front import Params  # noqa: E402

P0 = Params()
# (run name, overrides): the plan's section 6 sweep list
D_HOLE, D_POS, D_BORE, D_DEPTH, D_BUTTON, D_HALF = 0.1, 0.1, 0.05, 0.1, 0.2, 0.05


def shifted_x(xs, d):
    return [x + d for x in xs]


RESUME = False
RUNS = {"nominal": {}}
for sign, tag in ((-1, "low"), (1, "high")):
    s = float(sign)
    RUNS.update({
        f"win_x_left_{tag}": {"win_x_left": P0.win_x_left + s * D_POS},
        f"opening_x_right_{tag}": {"opening_x_right": P0.opening_x_right + s * D_POS},
        f"win_top_y_{tag}": {"win_top_y": P0.win_top_y + s * D_POS},
        f"slot_x_left_{tag}": {"slot_x_left": P0.slot_x_left + s * D_POS},
        f"slot_top_y_{tag}": {"slot_top_y": P0.slot_top_y + s * D_POS},
        f"flange_hole_d_{tag}": {"flange_hole_d": P0.flange_hole_d + s * D_HOLE},
        f"flange_hole_x_{tag}": {"flange_hole_x": shifted_x(P0.flange_hole_x, s * D_POS)},
        f"flange_hole_z_{tag}": {"flange_hole_z": P0.flange_hole_z + s * D_POS},
        f"insert_bore_d_{tag}": {"insert_bore_d": P0.insert_bore_d + s * D_BORE},
        f"insert_bore_depth_{tag}": {"insert_bore_depth": P0.insert_bore_depth + s * D_DEPTH},
        f"button_hole_d_{tag}": {"button_hole_d": P0.button_hole_d + s * D_BUTTON},
        f"boss_end_z_{tag}": {"boss_end_z": P0.boss_end_z + s * D_POS},
        f"boss_d_{tag}": {"boss_d": P0.boss_d + s * D_POS},
        f"wall_z_{tag}": {"wall_z_in": P0.wall_z_in + s * D_POS, "wall_z_out": P0.wall_z_out + s * D_POS},
        f"wall_top_y_{tag}": {"wall_top_y": P0.wall_top_y + s * D_POS},
        # each end +-0.05: the U-02 size band (+-0.1 on 232.0) binds before REQ-02's +-0.1 per end
        f"wall_x_half_{tag}": {"wall_x_half": P0.wall_x_half + s * D_HALF},
    })


def one(name: str, overrides: dict) -> dict:
    step = OUT / f"od_c09_front_C1_v01_{name}.step"
    js = OUT / f"{name}.json"
    if RESUME and js.exists() and step.exists():
        res = json.loads(js.read_text())
        return {"run": name, "overrides": overrides, "built": True, "checked": True, "summary": res["summary"]}
    py = [sys.executable, "-u"]
    pj = json.dumps(overrides)
    b = subprocess.run(py + [str(HERE / "build_od_c09_front.py"), "--params", pj, "--out-step", str(step),
                             "--no-stl", "--no-assembly"], capture_output=True, text=True)
    if b.returncode != 0:
        return {"run": name, "overrides": overrides, "built": False, "error": b.stderr[-800:]}
    c = subprocess.run(py + [str(HERE / "check_od_c09_front.py"), "--step", str(step), "--stl", "",
                             "--params", pj, "--out", str(js), "--cache", str(OUT / "ref_cache.json")], capture_output=True, text=True)
    (OUT / f"{name}.log").write_text(c.stdout + c.stderr)
    if c.returncode != 0 or not js.exists():
        return {"run": name, "overrides": overrides, "built": True, "checked": False, "error": c.stderr[-800:]}
    res = json.loads(js.read_text())
    return {"run": name, "overrides": overrides, "built": True, "checked": True, "summary": res["summary"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--only", default=None)
    ap.add_argument("--resume", action="store_true", help="keep the runs whose STEP and JSON exist")
    args = ap.parse_args()
    global RESUME
    RESUME = args.resume
    OUT.mkdir(parents=True, exist_ok=True)
    runs = RUNS if not args.only else {k: RUNS[k] for k in args.only.split(",")}
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        results = list(pool.map(lambda kv: one(*kv), runs.items()))
    summ = OUT / "sweep_summary.json"
    old = json.loads(summ.read_text()) if summ.exists() else {}
    old.update({r["run"]: r for r in results})
    summ.write_text(json.dumps(old, indent=1))
    for r in results:
        print(r["run"], r.get("built"), r.get("checked"), {k: v for k, v in (r.get("summary") or {}).items()
                                                             if v not in ("PASS", "PASS_ASSUMED", "N/A", "INFO")},
              flush=True)


if __name__ == "__main__":
    main()
