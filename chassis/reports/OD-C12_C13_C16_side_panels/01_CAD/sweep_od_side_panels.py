"""D7 robustness sweep: every fit-critical parameter at low and high (nominal is the delivered
build), rebuilt and exported into 01_CAD/sweep_v01/, re-imported and checked with the same predicates.
Position pairs move together (L-09), at the four diagonal corners of the 0.10 position circle.
Assembly-level readings (coaxiality, plate holes at the six poses, lid path for the tightest lip)
are taken on the swept parts placed by the same joints.
"""
from __future__ import annotations

import json
import math
import subprocess
import sys
from dataclasses import replace
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from params_od_side_panels import P  # noqa: E402

SW = HERE / "sweep_v01"
RES = HERE / "results_v01" / "sweep"
D = 0.10 / math.sqrt(2.0)   # each axis of a diagonal corner on the 0.10 position circle

PANEL = [
    ("lip_outer_x", {"lip_outer_x": 116.55}, {"lip_outer_x": 116.65}),
    ("panel_hole_d", {"panel_hole_d": 3.3}, {"panel_hole_d": 3.5}),
    ("panel_hole_pos_mm", {"panel_hole_dy": -D, "panel_hole_dz": -D}, {"panel_hole_dy": D, "panel_hole_dz": D}),
    ("panel_hole_pos_pm", {"panel_hole_dy": D, "panel_hole_dz": -D}, {"panel_hole_dy": -D, "panel_hole_dz": D}),
]
LEFT_ONLY = [("relief_floor_x", {"relief_floor_x": -117.85}, {"relief_floor_x": -117.95})]
BRACKET = [
    ("br_hole_d", {"br_hole_d": 3.3}, {"br_hole_d": 3.5}),
    ("br_hole_pos_mm", {"br_hole_x": P.br_hole_x - D, "br_hole_z": -D}, {"br_hole_x": P.br_hole_x + D, "br_hole_z": D}),
    ("br_hole_pos_pm", {"br_hole_x": P.br_hole_x + D, "br_hole_z": -D}, {"br_hole_x": P.br_hole_x - D, "br_hole_z": D}),
    ("cbore_d", {"cbore_d": 6.4}, {"cbore_d": 6.6}),
    ("cbore_floor_y", {"cbore_floor_y": 2.9}, {"cbore_floor_y": 3.1}),
    ("insert_bore_d", {"insert_bore_d": 3.95}, {"insert_bore_d": 4.05}),
    ("insert_bore_depth", {"insert_bore_depth": 5.9}, {"insert_bore_depth": 6.1}),
    ("insert_bore_pos_mm", {"insert_bore_y": P.insert_bore_y - D, "insert_bore_z": -D},
     {"insert_bore_y": P.insert_bore_y + D, "insert_bore_z": D}),
    ("insert_bore_pos_pm", {"insert_bore_y": P.insert_bore_y + D, "insert_bore_z": -D},
     {"insert_bore_y": P.insert_bore_y - D, "insert_bore_z": D}),
]


def run(args):
    r = subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-2000:])
    return r.stdout


def one(part, name, which, over):
    tag = f"C1_v01_{name}_{which}"
    run([HERE / f"build_{part}.py", "--params", json.dumps(over), "--out-dir", SW, "--tag", tag])
    out = RES / f"check_{part}_{name}_{which}.json"
    run([HERE / f"check_{part}.py", "--step", SW / f"{part}_{tag}.step", "--stl", SW / f"{part}_{tag}.stl",
         "--params", json.dumps(over), "--json", out])
    rows = json.loads(out.read_text())["rows"]
    return {"part": part, "parameter": name, "which": which, "override": over,
            "solids": next((r["measured"] for r in rows if r["gate"] == "exactly_one_solid"), None),
            "statuses": sorted({r["status"] for r in rows}),
            "fails": [r["gate"] for r in rows if r["status"] in ("FAIL",)],
            "inconclusive": [r["gate"] for r in rows if r["status"] == "INCONCLUSIVE" and "REQ-08" not in r["gate"]],
            "rows": rows}


def assembly_readings(results):
    """Coaxiality and plate holes on swept brackets and panels placed by the section 2 joints."""
    from checklib_od_side_panels import Rows
    from check_od_side_panels_assembly import coaxial_and_plate_holes, path, from_assembly
    from placements_od_side_panels import bracket_poses, place, references, solid_of
    from tools.core import read_step
    OUT = HERE.parent / "02_STEP_STL"
    nominal = {"r": solid_of(read_step(OUT / "od_c13_right_C1_v01.step")),
               "l": solid_of(read_step(OUT / "od_c12_left_C1_v01.step")),
               "b": solid_of(read_step(OUT / "od_c16_bracket_C1_v01.step"))}

    def named(r=None, l_=None, b=None):
        out = {"od_c13_right": r or nominal["r"], "od_c12_left": l_ or nominal["l"]}
        for label, pose in bracket_poses(P).items():
            out[label] = place(b or nominal["b"], pose)
        return out
    out = []
    cases = []
    for name, lo, hi in BRACKET:
        if name.startswith(("br_hole_pos", "insert_bore_pos")):
            for which in ("lo", "hi"):
                b = solid_of(read_step(SW / f"od_c16_bracket_C1_v01_{name}_{which}.step"))
                cases.append((f"bracket {name} {which}", named(b=b)))
    for name, lo, hi in PANEL:
        if name.startswith("panel_hole_pos"):
            for which in ("lo", "hi"):
                r = solid_of(read_step(SW / f"od_c13_right_C1_v01_{name}_{which}.step"))
                l_ = solid_of(read_step(SW / f"od_c12_left_C1_v01_{name}_{which}.step"))
                cases.append((f"panels {name} {which}", named(r=r, l_=l_)))
    # tolerance stack: panel hole and insert bore each 0.10 off nominal, in opposite directions
    r = solid_of(read_step(SW / "od_c13_right_C1_v01_panel_hole_pos_mm_hi.step"))
    l_ = solid_of(read_step(SW / "od_c12_left_C1_v01_panel_hole_pos_mm_hi.step"))
    b = solid_of(read_step(SW / "od_c16_bracket_C1_v01_insert_bore_pos_mm_lo.step"))
    cases.append(("STACK panel hole +0.10 with insert bore -0.10 (opposite)", named(r=r, l_=l_, b=b)))
    for label, nm in cases:
        rows = Rows("od_side_assembly")
        coaxial_and_plate_holes(rows, nm)
        out.append({"case": label, "rows": rows.rows})
    # lid path with the tightest lip (116.65: gap 0.35), all delivered parts present
    refs = {k: v[0] for k, v in references().items()}
    r = solid_of(read_step(SW / "od_c13_right_C1_v01_lip_outer_x_hi.step"))
    l_ = solid_of(read_step(SW / "od_c12_left_C1_v01_lip_outer_x_hi.step"))
    nm = {**refs, **named(r=r, l_=l_)}
    rows = Rows("od_side_assembly")
    path(rows, nm)
    out.append({"case": "lip_outer_x hi (116.65): assembly path", "rows": rows.rows})
    return out


def main():
    SW.mkdir(parents=True, exist_ok=True)
    RES.mkdir(parents=True, exist_ok=True)
    results = []
    for part, table in (("od_c13_right", PANEL), ("od_c12_left", PANEL + LEFT_ONLY), ("od_c16_bracket", BRACKET)):
        for name, lo, hi in table:
            for which, over in (("lo", lo), ("hi", hi)):
                res = one(part, name, which, over)
                print(part, name, which, res["solids"], res["statuses"], res["fails"], res["inconclusive"], flush=True)
                results.append(res)
    asm = assembly_readings(results)
    for a in asm:
        print(a["case"], sorted({r["status"] for r in a["rows"]}),
              max((r["measured"] for r in a["rows"] if isinstance(r["measured"], (int, float))), default=None), flush=True)
    (HERE / "results_v01" / "sweep_v01.json").write_text(json.dumps({"parts": results, "assembly": asm}, indent=1, default=str))


if __name__ == "__main__":
    main()
