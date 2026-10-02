"""D7 robustness sweep of od_t01_rig: rebuild at low and high of every fit-critical
parameter (DESIGN_PLAN §4), export into 01_CAD/sweep_<tag>/, and run every predicate
of check_od_t01_rig.py on each export (the motion checks U-03b and REQ-04 included).
Nominal is the delivered 02_STEP_STL export, checked by the same script.

Usage (repo root): uv run tools/run.py python <ws>/01_CAD/sweep_od_t01_rig.py [--tag v01] [--jobs 4]
"""
from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = 0.1 / math.sqrt(2.0)          # a 0.10 radial offset of the screw holes, split over x and z

SWEEP = {  # parameter: (low overrides, high overrides)
    "screw_d": ({"screw_d": 3.3}, {"screw_d": 3.5}),
    "cbore_d": ({"cbore_d": 6.4}, {"cbore_d": 6.6}),
    "cbore_floor_y": ({"cbore_floor_y": 137.9}, {"cbore_floor_y": 138.1}),
    "screw_xz_radial": ({"screw_x": 44.0 - D, "screw_z": 44.0 - D}, {"screw_x": 44.0 + D, "screw_z": 44.0 + D}),
    "window_r": ({"window_r": 29.9}, {"window_r": 30.1}),
    "theta_roof": ({"theta_roof": 45.05}, {"theta_roof": 45.14}),
    "bench_d": ({"bench_d": 4.4}, {"bench_d": 4.6}),
    "plate_y0": ({"plate_y0": 134.9}, {"plate_y0": 135.1}),
    "wall_x_in": ({"wall_x_in": 74.9}, {"wall_x_in": 75.1}),
    "depth_z1": ({"depth_z1": 59.9}, {"depth_z1": 60.1}),
}


def one(tag, param, side, over):
    out = HERE / f"sweep_{tag}"
    name = f"od_t01_rig_C1_{param}_{side}"
    sets = [f"{k}={v!r}" for k, v in over.items()]
    b = subprocess.run([sys.executable, str(HERE / "build_od_t01_rig.py"), "--out-dir", str(out), "--tag", tag,
                        "--name", name, "--no-assembly", "--meta-dir", str(out), "--set", *sets], capture_output=True, text=True)
    if b.returncode != 0:
        return {"parameter": param, "side": side, "over": over, "built": False, "error": b.stderr[-2000:]}
    step = out / f"{name}_{tag}.step"
    gates = out / f"{name}_{tag}.gates.json"
    c = subprocess.run([sys.executable, str(HERE / "check_od_t01_rig.py"), "--step", str(step), "--stl",
                        str(out / f"{name}_{tag}.stl"), "--params", str(out / f"{name}_{tag}.params.json"),
                        "--mesh-meta", str(out / f"{name}_{tag}.mesh.json"), "--out", str(gates)], capture_output=True, text=True)
    if c.returncode != 0:
        return {"parameter": param, "side": side, "over": over, "built": True, "error": c.stderr[-2000:]}
    return {"parameter": param, "side": side, "over": over, "built": True, "gates": gates.name}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="v01")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    jobs = [(a.tag, p, side, over) for p, (lo, hi) in SWEEP.items() if not a.only or p in a.only
            for side, over in (("low", lo), ("high", hi))]
    with ThreadPoolExecutor(a.jobs) as pool:
        results = list(pool.map(lambda j: one(*j), jobs))
    (HERE / f"sweep_{a.tag}" / "sweep_index.json").write_text(json.dumps(results, indent=1))
    for r in results:
        print(r["parameter"], r["side"], r.get("gates") or r.get("error", "")[-300:])


if __name__ == "__main__":
    main()
