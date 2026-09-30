"""Robustness sweep (PLAYBOOK D7, Usta U-15) for od_c01_frame v01.

Rebuilds at low and high of every fit-critical parameter of DESIGN_PLAN section 4
(the nominal is the delivered v01 build, checked by check_od_c01_frame.py), one
parameter at a time, exports into 01_CAD/sweep_v01/<variant>/ (never 02_STEP_STL/),
and runs the same predicates on each export. The mounts stay at their fixed joints.
No motion variable exists (U-03 b), so nothing is swept together. The hole-position
variants shift every hole group by (+-0.05, +-0.05), 0.0707 off axis (plan section 4).

Usage: uv run tools/run.py python <ws>/01_CAD/sweep_od_c01_frame.py [--jobs 4] [--only name,...]
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
OUT = HERE / "sweep_v01"

VARIANTS = {
    "nominal": {},
    "plate_t_low": {"plate_t": 5.9}, "plate_t_high": {"plate_t": 6.1},
    "insert_d_low": {"insert_d": 3.95}, "insert_d_high": {"insert_d": 4.05},
    "foot_d_low": {"foot_d": 3.30}, "foot_d_high": {"foot_d": 3.50},
    "drain_d_low": {"drain_d": 7.90}, "drain_d_high": {"drain_d": 8.10},
    "holes_xz_low": {"shift_x": -0.05, "shift_z": -0.05},
    "holes_xz_high": {"shift_x": 0.05, "shift_z": 0.05},
}


def run_one(name: str) -> dict:
    folder = OUT / name
    folder.mkdir(parents=True, exist_ok=True)
    variant = json.dumps(VARIANTS[name])
    tag = f"v01_{name}"
    b = subprocess.run([sys.executable, str(HERE / "build_od_c01_frame.py"), "--variant", variant,
                        "--out-dir", str(folder), "--tag", tag, "--record", str(folder / "build_record.json")],
                       capture_output=True, text=True)
    if b.returncode != 0:
        return {"variant": name, "built": False, "error": b.stderr[-2000:]}
    c = subprocess.run([sys.executable, str(HERE / "check_od_c01_frame.py"),
                        "--step", str(folder / f"od_c01_frame_C1_{tag}.step"),
                        "--asm", str(folder / f"od_c01_assembly_C1_{tag}.step"),
                        "--stl", str(folder / f"od_c01_frame_C1_{tag}.stl"),
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
        one = {"params": VARIANTS[r["variant"]], "built": r["built"], "error": r.get("error")}
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
