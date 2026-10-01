"""sweep_od_g01_v02.py - D7: the fit-critical parameters at nominal, low and high,
and the lock path swept over its motion variables together (L-09, L-10).

Every run rebuilds the part, exports its STEP into 01_CAD/sweep_v02/ (never into
02_STEP_STL/), re-imports it, and runs the same predicates of
check_od_g01_housing_v02.py. The geometric rows run on every parameter; the rows
that need OD-G10 as placed (REQ-10, U-03) run on the parameters that can move the
ear passage, because each of those poses is a distance computation against a
scanned portafilter.

Run: uv run tools/run.py python 01_CAD/sweep_od_g01_v02.py [only|motion|<case>]
"""
from __future__ import annotations

import json
import sys
import time
from dataclasses import replace
from pathlib import Path

from tools.core import write_step

import check_od_g01_housing_v02 as check
from build_od_g01_housing_v02 import P, TIMESTAMP, build

WORKSPACE = Path(__file__).resolve().parents[1]
SWEEP = WORKSPACE / "01_CAD" / "sweep_v02"

# (parameter, low, high, does it move the ear passage?) - ranges from DESIGN_PLAN §4's
# tolerance column, which reads them from spec §5's bands and the §6 rows.
CASES = [
    ("bore_r", 37.05, 37.15, True),
    ("lug_inner_r", 31.58, 31.78, True),
    ("lug_span", 53.75, 54.25, True),
    ("lug_starts", (335.75, 95.75, 215.75), (336.25, 96.25, 216.25), True),
    ("stop_end_off", 5.26, 6.26, True),
    ("stop_bottom_z", -10.82, -10.22, True),
    ("shelf_z", -14.20, -14.00, False),
    ("pocket_floor_z", -17.40, -17.20, False),
    ("pocket_riser_r", 34.95, 35.25, False),
    ("pocket_start_off", -5.5, -4.5, False),
    ("pocket_end_off", 58.0, 59.0, False),
    ("lip_upper_r", 31.65, 31.75, False),
    ("lip_lower_r", 31.25, 31.35, False),
    ("plate_t", 4.90, 5.10, False),
    ("keyhole_d", 25.95, 26.05, False),
    ("pair_b_r", 18.98, 19.08, False),
    ("carrier_xy", 43.95, 44.05, False),
    ("insert_d", 3.98, 4.02, False),
    ("insert_depth", 5.70, 6.00, False),
]
# the lug underside knots move together: (angle, z) pairs, low and high on z (A-05's
# own +-0.3 bracket)
UNDER_LOW = tuple((a, z - 0.3) for a, z in P.under_knots)
UNDER_HIGH = tuple((a, z + 0.3) for a, z in P.under_knots)


def run_case(name: str, value, tag: str, motion: bool) -> dict:
    started = time.time()
    params = replace(P, **{name: value})
    try:
        part = build(params)["part"]
    except Exception as exc:                                    # noqa: BLE001
        return {"case": tag, "parameter": name, "value": value, "built": False,
                "error": f"{type(exc).__name__}: {exc}"}
    path = SWEEP / f"od_g01_housing_C1_v02_{tag}.step"
    part.label = "od_g01_housing"
    write_step(part, path, timestamp=TIMESTAMP)
    # the sweep walks the same three-leg path more coarsely (25 poses against the
    # 43 of the delivered STEP), so the "at least 40 poses" row of spec §5 U-03(b) is
    # not asserted here; it is answered on the delivered STEP
    out = check.run(path, assembly=motion, heavy=False, coarse=True, path_poses=motion,
                    insert_steps=12, rotate_steps=8, seat_steps=4, pose_count=False)
    rows = [r for r in out["gates"] if r["status"] != "PASS" or r["margin"] is not None]
    return {"case": tag, "parameter": name, "value": value, "built": True,
            "seconds": round(time.time() - started, 1),
            "file": str(path.relative_to(WORKSPACE)),
            "gates": rows,
            "path_min": (min([p["clearance"] for p in out["detail"]["assembly"]["lock_path"]
                              if p["clearance"] is not None], default=None)
                         if motion and out["detail"].get("assembly") else None),
            "worst": sorted([(r["gate"], r["status"], r["measured"], r["margin"])
                             for r in out["gates"]],
                            key=lambda t: (t[1] == "PASS", t[3] if t[3] is not None else 0))[:6]}


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    SWEEP.mkdir(parents=True, exist_ok=True)
    cases = []
    todo = [(name, low, high, motion) for name, low, high, motion in CASES
            if which in ("all", "only") or which == name]
    for name, low, high, motion in todo:
        for tag, value in (("lo", low), ("hi", high)):
            cases.append(run_case(name, value, f"{name}_{tag}", motion))
            print(cases[-1]["case"], cases[-1].get("seconds"), cases[-1].get("worst"), flush=True)
    if which in ("all", "only", "under_knots"):
        for tag, value in (("lo", UNDER_LOW), ("hi", UNDER_HIGH)):
            cases.append(run_case("under_knots", value, f"under_knots_{tag}", True))
            print(cases[-1]["case"], cases[-1].get("seconds"), cases[-1].get("worst"), flush=True)
    out = SWEEP / ("sweep_v02.json" if which in ("all", "only") else f"sweep_v02_{which}.json")
    out.write_text(json.dumps(cases, indent=1, default=str), encoding="utf-8")
    print("written", out)


if __name__ == "__main__":
    main()
