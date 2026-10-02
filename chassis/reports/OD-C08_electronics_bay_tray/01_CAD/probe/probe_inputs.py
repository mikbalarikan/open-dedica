"""Probe the inputs for the OD-C08 plan (WP-02, D2): OD-E01 placed at the spec section 4
joint, OD-C01's plate top in the zone, OD-C02's rail +X faces. Writes probe_inputs.json.
Usage: uv run tools/run.py python <ws>/01_CAD/probe/probe_inputs.py
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
from build123d import Box, Location, Plane, Pos, Align

from tools.core import read_step, solid_count, brep_valid, naked_edges
from tools.measure import bore_census, locate_bore, envelope

HERE = Path(__file__).resolve().parent
WS = HERE.parents[1]
INPUTS = WS / "00_Spec" / "inputs"

# spec section 4 joint (A-03): board x -> -Z, board y -> +Y, board z -> +X, origin (84, 80, -100)
JOINT = Plane(origin=(84.0, 80.0, -100.0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))


def res(r):
    return {"measured": r.measured, "unit": r.unit, "status": r.status, "at": r.at, "reason": r.reason}


def env(shape):
    return {k: v.measured for k, v in envelope(shape).items()}


def main():
    out = {"started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    t = time.time()
    e01 = read_step(INPUTS / "OD-E01_power_pcb.step")
    sols = e01.solids()
    out["e01_solids"] = len(sols)
    out["e01_faces"] = len(e01.faces())
    e01 = sols[0] if len(sols) == 1 else e01
    out["e01_own_envelope"] = env(e01)
    placed = e01.moved(Location(JOINT))
    out["joint_check_y_dir"] = tuple(round(v, 9) for v in JOINT.y_dir)
    out["e01_placed_envelope"] = env(placed)
    out["e01_valid"] = {"solid_count": solid_count(placed).measured, "brep_valid": res(brep_valid(placed)),
                        "naked_edges": naked_edges(placed).measured}
    cen = bore_census(placed)
    bores = cen.detail.get("bores", []) if cen.detail else []
    out["e01_bores_count"] = cen.measured
    out["e01_bores_along_x"] = [b for b in bores if abs(abs(b["axis_dir"][0]) - 1) < 1e-6]
    want = {"H1": (-100.00, 80.00), "H2": (-100.013, 27.991), "H5": (-157.519, 81.976), "H6": (-157.511, 30.992)}
    loc = {}
    for h, (z, y) in want.items():
        lb = locate_bore(cen, (83.2, y, z), (1, 0, 0))
        loc[h] = {k: res(v) for k, v in lb.items()} | {"start": lb["diameter"].at,
                                                       "detail": lb["diameter"].detail}
    out["e01_holes"] = loc
    # solder face and anything below it: the part of the board at x < 82.44 + 0.05, by a box common
    bb = placed.bounding_box()
    out["e01_min_x"] = bb.min.X
    out["e01_max_x"] = bb.max.X
    # faces of the placed board with any point at x < 82.40
    low = []
    for f in placed.faces():
        fb = f.bounding_box()
        if fb.min.X < 82.40:
            low.append({"kind": f.geom_type.name, "area": round(f.area, 4),
                        "min": [round(fb.min.X, 4), round(fb.min.Y, 4), round(fb.min.Z, 4)],
                        "max": [round(fb.max.X, 4), round(fb.max.Y, 4), round(fb.max.Z, 4)]})
    out["e01_faces_below_x82_40"] = low
    # planar faces facing -X (solder face candidates)
    sf = []
    for f in placed.faces():
        if f.geom_type.name != "PLANE":
            continue
        n = f.normal_at()
        if n.X < -0.999999:
            fb = f.bounding_box()
            sf.append({"x": round(f.center().X, 5), "area": round(f.area, 3),
                       "min": [round(fb.min.Y, 3), round(fb.min.Z, 3)], "max": [round(fb.max.Y, 3), round(fb.max.Z, 3)]})
    sf.sort(key=lambda r: -r["area"])
    out["e01_minus_x_planes"] = sf[:12]
    # board slab extents: section at x 83.2 (inside the board thickness)
    try:
        from build123d import Plane as P
        sec = placed.intersect(Pos(83.2, 0, 0) * Box(0.01, 400, 400))
        out["e01_section_x83_2_envelope"] = env(sec)
    except Exception as exc:  # noqa: BLE001
        out["e01_section_x83_2_envelope"] = f"{type(exc).__name__}: {exc}"
    # what lies at y > 83.9 or y < 24, or z outside the outline (connectors etc)
    out["e01_seconds"] = round(time.time() - t, 1)

    c01 = read_step(INPUTS / "OD-C01_base_frame.step")
    out["c01_solids"] = len(c01.solids())
    out["c01_envelope"] = env(c01)
    top = []
    for f in c01.faces():
        if f.geom_type.name == "PLANE" and f.normal_at().Y > 0.999999:
            fb = f.bounding_box()
            if fb.max.X > 70 and fb.max.Z > -240 and fb.min.Z < -30:
                top.append({"y": round(f.center().Y, 5), "area": round(f.area, 2),
                            "min": [round(fb.min.X, 3), round(fb.min.Z, 3)], "max": [round(fb.max.X, 3), round(fb.max.Z, 3)]})
    out["c01_up_faces_in_zone"] = top
    pc = bore_census(c01)
    pb = pc.detail.get("bores", []) if pc.detail else []
    out["c01_bores_near_zone"] = [{"d": round(b["diameter"], 3), "start": [round(v, 3) for v in b["start"]],
                                   "end": [round(v, 3) for v in b["end"]], "axis": b["axis_dir"]}
                                  for b in pb if b["start"][0] > 60 and -250 < b["start"][2] < -20]
    c02 = read_step(INPUTS / "OD-C02_bulkhead.step")
    out["c02_solids"] = len(c02.solids())
    out["c02_envelope"] = env(c02)
    px = []
    for f in c02.faces():
        if f.geom_type.name == "PLANE" and f.normal_at().X > 0.999999:
            fb = f.bounding_box()
            px.append({"x": round(f.center().X, 5), "area": round(f.area, 2),
                       "y": [round(fb.min.Y, 3), round(fb.max.Y, 3)], "z": [round(fb.min.Z, 3), round(fb.max.Z, 3)]})
    out["c02_plus_x_faces"] = px
    out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    (HERE / "probe_inputs.json").write_text(json.dumps(out, indent=1, default=str))
    print(json.dumps({k: v for k, v in out.items() if k not in ("e01_bores_along_x",)}, indent=1, default=str)[:12000])


if __name__ == "__main__":
    main()
