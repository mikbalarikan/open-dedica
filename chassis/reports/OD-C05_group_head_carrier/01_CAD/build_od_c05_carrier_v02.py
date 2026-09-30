"""Build od_c05_carrier v02, concept C4 (job 20260930-od-c05-group-head-carrier, spec 2.0).

build123d Algebra mode, one parameter structure, no index-based selectors. Frame: the
OD-G01 STEP frame (spec 2.0 section 2): Z the group head axis, +Z the mouth (down in
the machine, A-02), +Y the front; the housing's rear face z -24.94 is the plate's
underside, the floor is z +180.06 (A-03). Print: on its side, x = -55 on the bed,
build direction +X (A-13).

Usage (from the repository root):
  uv run tools/run.py python <ws>/01_CAD/build_od_c05_carrier_v02.py             # v02 deliverables
  uv run tools/run.py python <ws>/01_CAD/build_od_c05_carrier_v02.py --out 01_CAD/sweep_v02 \
      --tag cb_d_hi --set cb_d=6.6                                                 # a sweep run
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass, replace
from pathlib import Path

from build123d import (Axis, Box, Circle, Compound, Cylinder, Location, Plane, Polygon, Pos,
                       Rectangle, extrude, fillet)

from tools.core import compare_step, read_step, write_step, write_stl

WS = Path(__file__).resolve().parents[1]
TAG = "v02"
CONCEPT = "C4"
TIMESTAMP = "2026-09-30T12:00:00"


@dataclass(frozen=True)
class Params:
    # plate (spec 2.0 section 4 C4, REQ-03, A-01)
    z_contact: float = -24.94        # plate underside = housing rear face, measured on OD-G01
    plate_t: float = 5.0
    half_x: float = 55.0
    y_front: float = 50.0
    corner_r: float = 6.0            # front corners, centres (+-(half_x - r), y_front - r) = (+-49, 44)
    # housing holes and counterbores from the top face (REQ-01, REQ-02, A-09)
    hole_d: float = 3.4
    hole_xy: float = 44.0
    cb_d: float = 6.5
    cb_depth: float = 2.0
    # hub window (REQ-04, A-06): R about the axis, 45 deg gable toward +X, apex hub_r*sqrt(2)
    hub_r: float = 30.0
    # wall (REQ-08)
    wall_y_rear: float = -58.0
    wall_y_front: float = -52.0
    # foot (REQ-05, REQ-06, REQ-07, A-03, A-04, A-05)
    z_floor: float = 180.06
    foot_t: float = 4.0
    foot_y_rear: float = -102.0
    foot_hole_d: float = 3.4
    foot_hole_x: float = 35.0
    foot_hole_y1: float = -72.0
    foot_hole_y2: float = -92.0
    # gussets (E-06, REQ-08): |x| gusset_x_in .. half_x, legs gusset_leg, 45 deg hypotenuse
    gusset_x_in: float = 51.0
    gusset_leg: float = 40.0
    # through-cut overrun beyond the faces (construction only)
    overrun: float = 1.0
    # STL export (U-07)
    stl_tol: float = 0.01
    stl_ang: float = 0.20

    @property
    def z_top(self) -> float:
        return self.z_contact - self.plate_t

    @property
    def z_foot_top(self) -> float:
        return self.z_floor - self.foot_t


def gusset(p: Params, tri, x_low: float):
    """A right-triangle prism along X from x_low, gusset_t = half_x - gusset_x_in thick;
    placement checked against its bounding box (never assumed)."""
    t = p.half_x - p.gusset_x_in
    body = extrude(Plane.YZ.offset(x_low) * Polygon(*tri, align=None), amount=t, dir=(1, 0, 0))
    box = body.bounding_box()
    if abs(box.min.X - x_low) > 1e-6 or abs(box.max.X - x_low - t) > 1e-6:
        raise RuntimeError(f"gusset at x {box.min.X:.3f} .. {box.max.X:.3f}, expected from {x_low}")
    ys = sorted(v[0] for v in tri)
    zs = sorted(v[1] for v in tri)
    if abs(box.min.Y - ys[0]) > 1e-6 or abs(box.max.Y - ys[-1]) > 1e-6 or \
            abs(box.min.Z - zs[0]) > 1e-6 or abs(box.max.Z - zs[-1]) > 1e-6:
        raise RuntimeError(f"gusset placed at y {box.min.Y:.3f}..{box.max.Y:.3f}, z {box.min.Z:.3f}..{box.max.Z:.3f}")
    return body


def build(p: Params):
    # F01 plate: rectangle with the two front corners (y = y_front) rounded
    outline = Pos(0, (p.y_front + p.wall_y_rear) / 2) * Rectangle(2 * p.half_x, p.y_front - p.wall_y_rear)
    front_vertices = [v for v in outline.vertices() if abs(v.Y - p.y_front) < 1e-6]
    outline = fillet(front_vertices, p.corner_r)
    plate = Pos(0, 0, p.z_top) * extrude(outline, amount=p.plate_t)
    # F02 wall, from the plate top down to the floor
    wall = Location((-p.half_x, p.wall_y_rear, p.z_top)) * \
        Box(2 * p.half_x, p.wall_y_front - p.wall_y_rear, p.z_floor - p.z_top, align=None)
    # F03 foot, behind the wall
    foot = Location((-p.half_x, p.foot_y_rear, p.z_foot_top)) * \
        Box(2 * p.half_x, p.wall_y_rear - p.foot_y_rear, p.foot_t, align=None)
    # F04 front gussets under the plate, F05 rear gussets on the foot (triangles in (y, z))
    tri_front = [(p.wall_y_front, p.z_contact), (p.wall_y_front + p.gusset_leg, p.z_contact),
                 (p.wall_y_front, p.z_contact + p.gusset_leg)]
    tri_rear = [(p.wall_y_rear, p.z_foot_top), (p.wall_y_rear - p.gusset_leg, p.z_foot_top),
                (p.wall_y_rear, p.z_foot_top - p.gusset_leg)]
    gussets = [gusset(p, tri, x) for tri in (tri_front, tri_rear) for x in (p.gusset_x_in, -p.half_x)]
    body = plate + wall + foot
    for gz in gussets:
        body = body + gz
    # F06 hub window: circle R hub_r united with the 45 deg gable toward +X
    t = p.hub_r / math.sqrt(2)
    profile = Circle(p.hub_r) + Polygon((0, 0), (t, -t), (p.hub_r * math.sqrt(2), 0), (t, t), align=None)  # counter-clockwise
    window = Pos(0, 0, p.z_top - p.overrun) * extrude(profile, amount=p.plate_t + 2 * p.overrun)
    body = body - window
    # F07 holes and F08 counterbores along Z through the plate (counterbore from the top face)
    for sx in (1, -1):
        for sy in (1, -1):
            x, y = sx * p.hole_xy, sy * p.hole_xy
            hole = Location((x, y, p.z_top - p.overrun)) * Cylinder(p.hole_d / 2, p.plate_t + 2 * p.overrun, align=None)
            cbore = Location((x, y, p.z_top - p.overrun)) * Cylinder(p.cb_d / 2, p.cb_depth + p.overrun, align=None)
            body = body - hole - cbore
    # F09 foot holes along Z
    for sx in (1, -1):
        for y in (p.foot_hole_y1, p.foot_hole_y2):
            fh = Location((sx * p.foot_hole_x, y, p.z_foot_top - p.overrun)) * \
                Cylinder(p.foot_hole_d / 2, p.foot_t + 2 * p.overrun, align=None)
            body = body - fh
    # F10 clean-up
    body = body.clean()
    solids = body.solids()
    if len(solids) != 1:
        raise RuntimeError(f"expected one solid, built {len(solids)}")
    carrier = solids[0]
    carrier.label = "od_c05_carrier"
    return carrier


def place_neighbours():
    """OD-G01 at the identity (spec section 2 frame); OD-G04 rotated +6.05 deg about Z,
    then moved z -6.82 (OD-G01 REPORT v02 section 5; plan v02 section 5)."""
    g01s = read_step(WS / "00_Spec/inputs/OD-G01_housing_C1_v02.step").solids()
    g04s = read_step(WS / "00_Spec/inputs/OD-G04_brewing_gasket_support.step").solids()
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
    stem = f"od_c05_carrier_{CONCEPT}_{TAG}"
    astem = f"od_c05_assembly_{CONCEPT}_{TAG}"
    if a.out:
        out = WS / a.out
        step, asm_path = out / f"{stem}_{a.tag}.step", out / f"{astem}_{a.tag}.step"
        stl = None if a.no_stl else out / f"{stem}_{a.tag}.stl"
        log = out / f"build_{a.tag}.json"
    else:
        out = WS / "02_STEP_STL"
        step, asm_path = out / f"{stem}.step", out / f"{astem}.step"
        stl = None if a.no_stl else out / f"{stem}.stl"
        log = WS / f"01_CAD/build_od_c05_carrier_{TAG}.json"
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
