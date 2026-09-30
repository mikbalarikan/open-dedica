"""Robustness sweep (PLAYBOOK D7, Usta U-15) for od_c04_mount v01.

Rebuilds at nominal, low and high of every fit-critical parameter of DESIGN_PLAN
section 4, one parameter at a time, exports into 01_CAD/sweep_v01/<variant>/ (never
02_STEP_STL/), and runs the same predicates (check_od_c04_mount.run) on each export.
There is no motion variable (U-03 b), so nothing is swept together.
Position parameters move a feature 0.10 along the diagonal (0.0707 in each of the
two coordinates), the edge of the spec's offset <= 0.10 zone.

Usage: uv run tools/run.py python <ws>/01_CAD/sweep_od_c04_mount.py [--jobs 4] [--only name,...]
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
WS = HERE.parent
OUT = HERE / "sweep_v01"
D = 0.10 / math.sqrt(2.0)

VARIANTS = {
    "nominal": {},
    "plate_front_z_low": {"plate_front_z": -12.10}, "plate_front_z_high": {"plate_front_z": -11.90},
    "plate_back_z_low": {"plate_back_z": -17.10}, "plate_back_z_high": {"plate_back_z": -16.90},
    "foot_y_low": {"foot_y_min": -70.10}, "foot_y_high": {"foot_y_min": -69.90},
    "frame_hole_d_low": {"frame_hole_d": 3.30}, "frame_hole_d_high": {"frame_hole_d": 3.50},
    "frame_hole_xz_low": {"frame_shift_x": -D, "frame_shift_z": -D},
    "frame_hole_xz_high": {"frame_shift_x": D, "frame_shift_z": D},
    "standoff_xy_low": {"standoff_shift_x": -D, "standoff_shift_y": -D},
    "standoff_xy_high": {"standoff_shift_x": D, "standoff_shift_y": D},
    "standoff_bore_d_low": {"standoff_bore_d": 3.90}, "standoff_bore_d_high": {"standoff_bore_d": 4.10},
    "tip_z_low": {"tip_z": -10.20}, "tip_z_high": {"tip_z": -10.00},
}


def run_one(name: str) -> dict:
    folder = OUT / name
    folder.mkdir(parents=True, exist_ok=True)
    variant = json.dumps(VARIANTS[name])
    tag = f"v01_{name}"
    runner = [sys.executable]
    b = subprocess.run(runner + [str(HERE / "build_od_c04_mount.py"), "--variant", variant,
                        "--out-dir", str(folder), "--tag", tag, "--record", str(folder / "build_record.json")],
                       capture_output=True, text=True)
    if b.returncode != 0:
        return {"variant": name, "built": False, "error": b.stderr[-2000:]}
    c = subprocess.run(runner + [str(HERE / "check_od_c04_mount.py"),
                        "--step", str(folder / f"od_c04_mount_C1_{tag}.step"),
                        "--asm", str(folder / f"od_c04_assembly_C1_{tag}.step"),
                        "--stl", str(folder / f"od_c04_mount_C1_{tag}.stl"),
                        "--out", str(folder / "check_results.json"), "--variant", variant],
                       capture_output=True, text=True)
    res = json.loads((folder / "check_results.json").read_text())
    return {"variant": name, "built": True, "check_rc": c.returncode, "gates": res.get("gates", []),
            "error": res.get("error")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    names = [n for n in VARIANTS if not a.only or n in a.only.split(",")]
    with ThreadPoolExecutor(a.jobs) as pool:
        results = list(pool.map(run_one, names))
    summary = {"variants": {}, "worst": {}}
    for r in results:
        one = {"built": r["built"], "error": r.get("error")}
        if r["built"]:
            solids = [g for g in r["gates"] if g["gate"] == "exactly_one_solid"]
            one["one_solid"] = bool(solids and solids[0]["status"] == "PASS")
            one["not_passed"] = [(g["gate"], g["status"], g["measured"], g["margin"]) for g in r["gates"]
                                 if g["status"] not in ("PASS", "PASS_ASSUMED", "N/A")]
            for g in r["gates"]:
                if g["margin"] is None:
                    continue
                w = summary["worst"].get(g["gate"])
                if w is None or g["margin"] < w["margin"]:
                    summary["worst"][g["gate"]] = {"margin": g["margin"], "variant": r["variant"],
                                                   "measured": g["measured"], "status": g["status"]}
        summary["variants"][r["variant"]] = one
    (OUT / "sweep_summary_v01.json").write_text(json.dumps(summary, indent=1, default=str))
    for n, v in summary["variants"].items():
        print(n, "built" if v["built"] else "NOT BUILT", "one_solid" if v.get("one_solid") else "",
              v.get("not_passed"), v.get("error") or "")


if __name__ == "__main__":
    main()
