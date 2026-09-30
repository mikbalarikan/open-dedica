"""Build od_c05_carrier, concept C1 (job 20260930-od-c05-group-head-carrier, spec 1.1).

build123d Algebra mode, one parameter structure, no index-based selectors. Frame:
the OD-G01 STEP frame (spec section 2): Z the group head axis, +Z toward the user,
+Y up, housing rear face z -24.94. Print: foot on the bed, build direction +Y.

Usage (from the repository root):
  uv run tools/run.py python <ws>/01_CAD/build_od_c05_carrier.py            # v01 deliverables
  uv run tools/run.py python <ws>/01_CAD/build_od_c05_carrier.py --out 01_CAD/sweep_v01 \
      --tag cb_d_hi --set cb_d=6.6 --no-stl                                     # a sweep run
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass, replace
from pathlib import Path

from build123d import (Axis, Box, Circle, Compound, Cylinder, Location, Plane, Polygon, Pos,
                       Rectangle, extrude, fillet)

from tools.core import compare_step, read_step, validity, write_step, write_stl

WS = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-09-30T12:00:00"


@dataclass(frozen=True)
class Params:
    # wall (spec 1.1 section 4 C1, REQ-03, A-01)
    z_front: float = -24.94          # housing rear face, measured on OD-G01 (plan section 1)
    wall_t: float = 5.0
    wall_x: float = 50.0             # half width
    y_top: float = 50.0
    y_floor: float = -175.0          # spec 1.1 (A-03): foot underside
    corner_r: float = 6.0            # spec 1.1 K-1: R 6 about (+-44, 44)
    # housing holes and counterbores (REQ-01, REQ-02, A-09)
    hole_d: float = 3.4
    hole_xy: float = 44.0
    cb_d: float = 6.5
    cb_depth: float = 2.0
    # windows (REQ-04, REQ-08, A-06, A-07); gables at 45 deg, apex = centre + r*sqrt(2)
    hub_r: float = 30.0
    hub_c_y: float = 0.0
    low_r: float = 25.0
    low_c_y: float = -110.0          # spec 1.1
    # foot (REQ-05, REQ-06, REQ-07, A-04, A-05)
    foot_t: float = 4.0
    foot_z_rear: float = -69.94
    foot_hole_d: float = 3.4
    foot_hole_x: float = 35.0
    foot_hole_z1: float = -40.0
    foot_hole_z2: float = -60.0
    # gussets (E-06)
    gusset_t: float = 4.0
    gusset_leg: float = 40.0
    # through-cut overrun beyond the faces (construction only)
    overrun: float = 1.0
    # STL export (U-07)
    stl_tol: float = 0.01
    stl_ang: float = 0.20

    @property
    def z_rear(self) -> float:
        return self.z_front - self.wall_t

    @property
    def y_foot_top(self) -> float:
        return self.y_floor + self.foot_t


def window_cutter(p: Params, r: float, cy: float):
    """Circle R r about (0, cy) united with the 45 deg gable over it (tangents at 45 and
    135 deg meeting at the apex (0, cy + r*sqrt(2))), extruded through the wall."""
    t = r / math.sqrt(2)
    circle = Pos(0, cy) * Circle(r)
    gable = Polygon((0, cy), (t, cy + t), (0, cy + r * math.sqrt(2)), (-t, cy + t), align=None)
    profile = circle + gable
    z0 = p.z_rear - p.overrun
    return Pos(0, 0, z0) * extrude(profile, amount=p.wall_t + 2 * p.overrun)


def build(p: Params):
    wall_h = p.y_top - p.y_floor
    # F01 wall: sketch with the two top corners rounded concentric with the top holes
    outline = Pos(0, (p.y_top + p.y_floor) / 2) * Rectangle(2 * p.wall_x, wall_h)
    top_vertices = [v for v in outline.vertices() if abs(v.Y - p.y_top) < 1e-6]
    outline = fillet(top_vertices, p.corner_r)
    wall = Pos(0, 0, p.z_rear) * extrude(outline, amount=p.wall_t)
    # F02 foot
    foot_len = p.z_front - p.foot_z_rear
    foot = Location((-p.wall_x, p.y_floor, p.foot_z_rear)) * Box(2 * p.wall_x, p.foot_t, foot_len, align=None)
    # F03 gussets: right triangles in the YZ plane, legs gusset_leg, hypotenuse at 45 deg
    tri = [(p.y_foot_top, p.z_rear), (p.y_foot_top + p.gusset_leg, p.z_rear),
           (p.y_foot_top, p.z_rear - p.gusset_leg)]
    gusset_r = extrude(Plane.YZ.offset(p.wall_x - p.gusset_t) * Polygon(*tri, align=None),
                       amount=p.gusset_t, dir=(1, 0, 0))
    gusset_l = extrude(Plane.YZ.offset(-p.wall_x) * Polygon(*tri, align=None), amount=p.gusset_t, dir=(1, 0, 0))
    for gusset, x_low in ((gusset_r, p.wall_x - p.gusset_t), (gusset_l, -p.wall_x)):
        box = gusset.bounding_box()
        if abs(box.min.X - x_low) > 1e-6 or abs(box.max.X - x_low - p.gusset_t) > 1e-6:
            raise RuntimeError(f"gusset placed at x {box.min.X:.3f} .. {box.max.X:.3f}, expected from {x_low}")
    body = wall + foot + gusset_r + gusset_l
    # F04, F05 windows
    hub_window = window_cutter(p, p.hub_r, p.hub_c_y)
    low_window = window_cutter(p, p.low_r, p.low_c_y)
    body = body - hub_window - low_window
    # F06, F07 housing holes and counterbores (counterbore from the rear face)
    hole_len = p.wall_t + 2 * p.overrun
    for sx in (1, -1):
        for sy in (1, -1):
            x, y = sx * p.hole_xy, sy * p.hole_xy
            hole = Location((x, y, p.z_rear - p.overrun)) * Cylinder(p.hole_d / 2, hole_len, align=None)
            cbore = Location((x, y, p.z_rear - p.overrun)) * Cylinder(p.cb_d / 2, p.cb_depth + p.overrun, align=None)
            body = body - hole - cbore
    # F08 frame holes along Y through the foot
    for sx in (1, -1):
        for z in (p.foot_hole_z1, p.foot_hole_z2):
            fh = Location((sx * p.foot_hole_x, p.y_floor - p.overrun, z), (-90, 0, 0)) * \
                Cylinder(p.foot_hole_d / 2, p.foot_t + 2 * p.overrun, align=None)
            body = body - fh
    # F09 clean-up
    body = body.clean()
    solids = body.solids()
    if len(solids) != 1:
        raise RuntimeError(f"expected one solid, built {len(solids)}")
    carrier = solids[0]
    carrier.label = "od_c05_carrier"
    return carrier


def place_neighbours():
    """OD-G01 at the identity (spec section 2 frame); OD-G04 rotated +6.05 deg about Z,
    then moved z -6.82 (OD-G01 REPORT v02 section 5; plan section 5)."""
    g01 = read_step(WS / "00_Spec/inputs/OD-G01_housing_C1_v02.step")
    g04 = read_step(WS / "00_Spec/inputs/OD-G04_brewing_gasket_support.step")
    g01s = g01.solids()
    g04s = g04.solids()
    assert len(g01s) == 1 and len(g04s) == 1
    housing = g01s[0]
    support = g04s[0].rotate(Axis.Z, 6.05).translate((0, 0, -6.82))
    housing.label = "od_g01_housing"
    support.label = "od_g04_brewing_gasket_support"
    return housing, support


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None, help="folder for a sweep run (never 02_STEP_STL)")
    ap.add_argument("--tag", default="nominal")
    ap.add_argument("--set", action="append", default=[])
    ap.add_argument("--no-stl", action="store_true")
    a = ap.parse_args(argv)
    p = Params()
    for item in a.set:
        k, v = item.split("=")
        p = replace(p, **{k: float(v)})
    if a.out:
        out = WS / a.out
        step = out / f"od_c05_carrier_C1_v01_{a.tag}.step"
        asm_path = out / f"od_c05_assembly_C1_v01_{a.tag}.step"
        stl = None if a.no_stl else out / f"od_c05_carrier_C1_v01_{a.tag}.stl"
        log = out / f"build_{a.tag}.json"
    else:
        out = WS / "02_STEP_STL"
        step = out / "od_c05_carrier_C1_v01.step"
        asm_path = out / "od_c05_assembly_C1_v01.step"
        stl = None if a.no_stl else out / "od_c05_carrier_C1_v01.stl"
        log = WS / "01_CAD/build_od_c05_carrier_v01.json"
    carrier = build(p)
    w = write_step(carrier, step, timestamp=TIMESTAMP)
    rt = compare_step(carrier, step)
    housing, support = place_neighbours()
    part_back = read_step(step).solids()[0]
    part_back.label = "od_c05_carrier"
    asm = Compound(label="od_c05_assembly", children=[part_back, housing, support])
    wa = write_step(asm, asm_path, timestamp=TIMESTAMP)
    info = {"params": asdict(p), "step": {"path": step.name, "sha256": w.sha256},
            "assembly": {"path": asm_path.name, "sha256": wa.sha256},
            "roundtrip_built_vs_file": {k: r.to_dict() for k, r in rt.items()}}
    if stl is not None:
        back = read_step(step)
        ws = write_stl(back, stl, tolerance=p.stl_tol, angular_tolerance=p.stl_ang)
        info["stl"] = {"path": stl.name, "sha256": ws.sha256, **ws.detail}
    log.parent.mkdir(parents=True, exist_ok=True)
    log.write_text(json.dumps(info, indent=1, default=str))
    print(json.dumps({k: v for k, v in info.items() if k != "roundtrip_built_vs_file"}, indent=1, default=str))
    print({k: (r.measured, r.status) for k, r in rt.items()})


if __name__ == "__main__":
    main()
