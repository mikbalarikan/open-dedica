"""sweep_od_g01_v01.py - D7: the fit-critical parameters at nominal, low and high,
and the lock path swept over its motion variables together (L-09, L-10).

Every run rebuilds the part, exports its STEP into 01_CAD/sweep_v01/ (never into
02_STEP_STL/), re-imports it, and runs the same predicates of
check_od_g01_housing.py. The geometric rows run on every parameter; the rows that
need OD-G10 as placed (REQ-10, the lock path) run on the parameters that can move
the ear passage, because each of those poses is a distance computation against a
scanned portafilter.

Run: uv run tools/run.py python 01_CAD/sweep_od_g01_v01.py [only|motion]
"""
from __future__ import annotations

import json
import sys
import time
from dataclasses import replace
from pathlib import Path

from tools.core import read_step, write_step
from tools.measure import clearance

import check_od_g01_housing as check
from assemble_od_g01_check import (G10_INSERT_CLOCK_DEG, G10_LOCK_CLOCK_DEG, G10_LOCK_RIM_Z,
                                   load_mates, place_g10)
from build_od_g01_housing import P, STEP_PATH, TIMESTAMP, build

WORKSPACE = Path(__file__).resolve().parents[1]
SWEEP = WORKSPACE / "01_CAD" / "sweep_v01"

# (parameter, low, high, does it move the ear passage?) - ranges from DESIGN_PLAN §4's
# tolerance column, which reads them from spec §5's bands and the §6 rows.
CASES = [
    ("bore_r", 37.05, 37.15, True),
    ("lug_inner_r", 31.58, 31.78, True),
    ("lug_span", 53.75, 54.25, True),
    ("lug_starts", (335.75, 95.75, 215.75), (336.25, 96.25, 216.25), True),
    ("stop_end_off", 5.26, 6.26, True),
    ("stop_bottom_z", -10.82, -10.22, True),
    ("shelf_z", -14.20, -14.00, True),
    ("pocket_floor_z", -17.40, -17.20, False),
    ("pocket_riser_r", 34.95, 35.25, False),
    ("pocket_start_off", -5.5, -4.5, False),
    ("pocket_end_off", 58.0, 59.0, False),
    ("lip_upper_r", 31.65, 31.78, False),
    ("lip_lower_r", 31.25, 31.35, False),
    ("plate_t", 4.90, 5.10, False),
    ("keyhole_d", 25.95, 26.05, False),
    ("pair_b_r", 18.98, 19.08, False),
    ("carrier_xy", 43.95, 44.05, False),
    ("insert_d", 3.98, 4.02, False),
    ("insert_depth", 5.70, 6.00, False),
]
# the lug underside knots move together: (angle, z) pairs, low and high on z
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
    path = SWEEP / f"od_g01_housing_C1_v01_{tag}.step"
    part.label = "od_g01_housing"
    write_step(part, path, timestamp=TIMESTAMP)
    out = check.run(path, assembly=motion, heavy=False, coarse=True, poses=5)
    rows = [r for r in out["gates"] if r["status"] != "PASS" or r["margin"] is not None]
    return {"case": tag, "parameter": name, "value": value, "built": True,
            "seconds": round(time.time() - started, 1),
            "file": str(path.relative_to(WORKSPACE)),
            "gates": rows,
            "worst": sorted([(r["gate"], r["status"], r["measured"], r["margin"])
                             for r in out["gates"]],
                            key=lambda t: (t[1] == "PASS", t[3] if t[3] is not None else 0))[:6]}


def lock_path(housing, g10, steps: int = 21) -> list:
    """U-03(b): insertion and rotation swept together, from first contact to the
    locked pose (L-09, L-10). OD-G10's STEP reads brep_valid = 0, so the boolean
    volume is INCONCLUSIVE (tools.core.common_volume refuses an unsound solid) and
    the path is measured as the distance between the two solids at every pose."""
    out = []
    for i in range(steps + 1):
        t = i / steps
        clock = G10_INSERT_CLOCK_DEG + (G10_LOCK_CLOCK_DEG - G10_INSERT_CLOCK_DEG) * t
        rim = -5.0 + (G10_LOCK_RIM_Z + 5.0) * t
        c = clearance(housing, place_g10(g10, clock, rim))
        out.append({"pose": i, "clock_deg": round(clock, 3), "rim_z": round(rim, 3),
                    "clearance": c.measured if c.ok else None,
                    "at": str(c.at), "reason": c.reason})
    return out


def rotation_leg(housing, g10, rim_z: float, steps: int = 12) -> list:
    """The second leg: at the depth the housing's own first contact gives, the
    portafilter turned from the insertion clock to the locked clock."""
    out = []
    for i in range(steps + 1):
        clock = G10_INSERT_CLOCK_DEG + (G10_LOCK_CLOCK_DEG - G10_INSERT_CLOCK_DEG) * i / steps
        c = clearance(housing, place_g10(g10, clock, rim_z))
        out.append({"pose": i, "clock_deg": round(clock, 3), "rim_z": rim_z,
                    "clearance": c.measured if c.ok else None, "at": str(c.at)})
    return out


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    SWEEP.mkdir(parents=True, exist_ok=True)
    report = {}
    if which in ("all", "motion"):
        housing = read_step(STEP_PATH)
        g04, g10 = load_mates()
        first = check.first_contact(housing, g10, G10_LOCK_CLOCK_DEG, -5.0, -13.0)
        report["motion"] = {"first_contact_rim_z": first,
                            "joint_path": lock_path(housing, g10),
                            "rotation_at_first_contact": rotation_leg(housing, g10,
                                                                      first if first else -11.69)}
        (WORKSPACE / "01_CAD" / "sweep_v01" / "motion_v01.json").write_text(
            json.dumps(report["motion"], indent=1, default=str), encoding="utf-8")
        print("motion path written")
    if which in ("all", "only"):
        cases = []
        for name, low, high, motion in CASES:
            for tag, value in (("lo", low), ("hi", high)):
                cases.append(run_case(name, value, f"{name}_{tag}", motion))
                print(cases[-1]["case"], cases[-1].get("seconds"), cases[-1].get("worst"))
        for tag, value in (("lo", UNDER_LOW), ("hi", UNDER_HIGH)):
            cases.append(run_case("under_knots", value, f"under_knots_{tag}", True))
            print(cases[-1]["case"], cases[-1].get("seconds"), cases[-1].get("worst"))
        report["cases"] = cases
        (WORKSPACE / "01_CAD" / "sweep_v01" / "sweep_v01.json").write_text(
            json.dumps(cases, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
