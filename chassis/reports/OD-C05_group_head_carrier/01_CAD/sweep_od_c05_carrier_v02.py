"""D7 sweep of od_c05_carrier v02 (concept C4): rebuild at the low and high rung of every
fit-critical parameter (DESIGN_PLAN_v02 section 4), export into 01_CAD/sweep_v02/, run
the same check script. Usage: uv run tools/run.py python <ws>/01_CAD/sweep_od_c05_carrier_v02.py [tag ...]"""
import json
import math
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

WS = Path(__file__).resolve().parents[1]
OUT = WS / "01_CAD/sweep_v02"
R2 = math.sqrt(2)
RUNS = {  # tag: (settings, expected positive-control values; the gate limits never change)
    "nominal": ({}, {}),
    "hole_d_lo": ({"hole_d": 3.3}, {}), "hole_d_hi": ({"hole_d": 3.5}, {}),
    "hole_xy_lo": ({"hole_xy": 43.95}, {}), "hole_xy_hi": ({"hole_xy": 44.05}, {}),
    "cb_d_lo": ({"cb_d": 6.4}, {}), "cb_d_hi": ({"cb_d": 6.6}, {}),
    "cb_depth_lo": ({"cb_depth": 1.9}, {}), "cb_depth_hi": ({"cb_depth": 2.1}, {}),
    "hub_r_hi": ({"hub_r": 30.1}, {"hub_apex_r": 30.1 * R2, "hub_side_r": 30.1}),
    "wall_y_front_hi": ({"wall_y_front": -52.1}, {"wall_y_front": -52.1}),
    "foot_t_lo": ({"foot_t": 3.9}, {"z_foot_top": 176.16}), "foot_t_hi": ({"foot_t": 4.1}, {"z_foot_top": 175.96}),
    "foot_y_rear_hi": ({"foot_y_rear": -101.9}, {}),
    "foot_hole_d_lo": ({"foot_hole_d": 3.3}, {}), "foot_hole_d_hi": ({"foot_hole_d": 3.5}, {}),
    "foot_hole_x_lo": ({"foot_hole_x": 34.95}, {}), "foot_hole_x_hi": ({"foot_hole_x": 35.05}, {}),
    "foot_hole_y_lo": ({"foot_hole_y1": -72.05, "foot_hole_y2": -92.05}, {}),
    "foot_hole_y_hi": ({"foot_hole_y1": -71.95, "foot_hole_y2": -91.95}, {}),
    "gusset_x_in_hi": ({"gusset_x_in": 51.1}, {"gusset_x_in": 51.1}),
}


def one(tag):
    sets, expect = RUNS[tag]
    args = [sys.executable, str(WS / "01_CAD/build_od_c05_carrier_v02.py"), "--out", "01_CAD/sweep_v02", "--tag", tag]
    for k, v in sets.items():
        args += ["--set", f"{k}={v}"]
    b = subprocess.run(args, capture_output=True, text=True)
    if b.returncode != 0:
        return tag, {"built": False, "error": b.stderr[-800:]}
    c = subprocess.run([sys.executable, str(WS / "01_CAD/check_od_c05_carrier_v02.py"),
                        "--step", str(OUT / f"od_c05_carrier_C4_v02_{tag}.step"),
                        "--assembly", str(OUT / f"od_c05_assembly_C4_v02_{tag}.step"),
                        "--stl", str(OUT / f"od_c05_carrier_C4_v02_{tag}.stl"),
                        "--expect", json.dumps(expect), "--out", str(OUT / f"check_{tag}.json")],
                       capture_output=True, text=True)
    return tag, {"built": True, "check_rc": c.returncode}


if __name__ == "__main__":
    tags = sys.argv[1:] or list(RUNS)
    OUT.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(4) as pool:
        for tag, res in pool.map(one, tags):
            print(tag, res, flush=True)
