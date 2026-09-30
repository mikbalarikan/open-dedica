"""Build od_c05_carrier v03, concept C4 with the closed column (job
20260930-od-c05-group-head-carrier, spec 2.1).

build123d Algebra mode, one parameter structure, no index-based selectors. Frame: the
OD-G01 STEP frame (spec 2.1 section 2): Z the group head axis, +Z the mouth (down in
the machine, A-02), +Y the front; the housing's rear face z -24.94 is the plate's
underside, the floor is z +180.06 (A-03). Print: the plate's top face z -29.94 on the
bed, build direction +Z (A-13).

Usage (from the repository root):
  uv run tools/run.py python <ws>/01_CAD/build_od_c05_carrier_v03.py             # v03 deliverables
  uv run tools/run.py python <ws>/01_CAD/build_od_c05_carrier_v03.py --out 01_CAD/sweep_v03 \
      --tag cb_d_hi --set cb_d=6.6                                                 # a sweep run
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, replace
from pathlib import Path

from build123d import (Axis, Box, Circle, Compound, Cylinder, Location, Plane, Polygon, Pos,
                       RectangleRounded, extrude)

from tools.core import compare_step, read_step, write_step, write_stl

WS = Path(__file__).resolve().parents[1]
TAG = "v03"
CONCEPT = "C4"
TIMESTAMP = "2026-09-30T12:00:00"


@dataclass(frozen=True)
class Params:
    # plate (spec 2.1 section 4 C4, REQ-03, A-01): square corners
    z_contact: float = -24.94        # plate underside = housing rear face, measured on OD-G01
    plate_t: float = 5.0
    half_x: float = 55.0
    y_front: float = 50.0
    y_rear: float = -102.0           # plate, column and foot rear face (REQ-07)
    # housing holes and counterbores from the top face (REQ-01, REQ-02, A-09)
    hole_d: float = 3.4
    hole_xy: float = 44.0
    cb_d: float = 6.5
    cb_depth: float = 2.0
    # hub window (REQ-04, A-06): round, R about the axis
    hub_r: float = 30.0
    # hatch through the plate's lid part (A-07, A-14)
    hatch_half_x: float = 40.0
    hatch_y_lo: float = -96.0
    hatch_y_hi: float = -64.0
    hatch_r: float = 4.0
    # column (REQ-08): front wall, side walls, rear wall
    wall_y_rear: float = -58.0       # front wall's rear face
    wall_y_front: float = -52.0      # front wall's front face
    side_t: float = 4.0              # side walls |x| half_x - side_t .. half_x
    rear_t: float = 4.0              # rear wall y_rear .. y_rear + rear_t
    # rear window (A-07): x +-win_half_x, z win_z_lo .. win_z_hi, 45 deg gable toward -Z
    win_half_x: float = 10.0
    win_z_lo: float = 130.0
    win_z_hi: float = 160.0
    # foot and tent (REQ-05, REQ-06, A-03, A-04, A-13)
    z_floor: float = 180.06
    foot_t: float = 4.0              # at the walls; the tent planes start at z_floor - foot_t
    ridge_y: float = -80.0           # tent ridge along X; 45 deg planes through (y_rear, z_foot_top) and (wall_y_rear, z_foot_top)
    foot_hole_d: float = 3.4
    foot_hole_x: float = 35.0
    foot_hole_y1: float = -72.0
    foot_hole_y2: float = -92.0
    foot_cb_d: float = 6.5           # counterbore from the tent face down to z_foot_top
    # gussets (E-06, REQ-08): the front pair, |x| gusset_x_in .. half_x, legs gusset_leg, 45 deg hypotenuse
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

    @property
    def ridge_z(self) -> float:
        """45 deg from the front plane's foot line (wall_y_rear, z_foot_top): 154.06 at nominal."""
        return self.z_foot_top - (self.wall_y_rear - self.ridge_y)

    @property
    def win_apex_z(self) -> float:
        """45 deg gable toward -Z over the window's half width: 120.0 at nominal (spec)."""
        return self.win_z_lo - self.win_half_x


def check_box(name, body, lo, hi):
    """Placement checked against the bounding box (never assumed)."""
    bb = body.bounding_box()
    got = (bb.min.X, bb.min.Y, bb.min.Z, bb.max.X, bb.max.Y, bb.max.Z)
    want = (*lo, *hi)
    if any(abs(a - b) > 1e-6 for a, b in zip(got, want)):
        raise RuntimeError(f"{name} placed at {got}, expected {want}")
    return body


def build(p: Params):
    # F01 column block with the plate's lid part: x +-half_x, y y_rear .. wall_y_front, full height
    column = check_box("column", Location((-p.half_x, p.y_rear, p.z_top)) *
                       Box(2 * p.half_x, p.wall_y_front - p.y_rear, p.z_floor - p.z_top, align=None),
                       (-p.half_x, p.y_rear, p.z_top), (p.half_x, p.wall_y_front, p.z_floor))
    # F02 plate's front part, square corners
    plate_front = Location((-p.half_x, p.wall_y_front, p.z_top)) * \
        Box(2 * p.half_x, p.y_front - p.wall_y_front, p.plate_t, align=None)
    # F03 front gussets under the plate on the front wall (triangle in (y, z), prism along X)
    tri = [(p.wall_y_front, p.z_contact), (p.wall_y_front + p.gusset_leg, p.z_contact),
           (p.wall_y_front, p.z_contact + p.gusset_leg)]
    gt = p.half_x - p.gusset_x_in
    gussets = [check_box(f"gusset {x0}", extrude(Plane.YZ.offset(x0) * Polygon(*tri, align=None), amount=gt, dir=(1, 0, 0)),
                         (x0, p.wall_y_front, p.z_contact), (x0 + gt, p.wall_y_front + p.gusset_leg, p.z_contact + p.gusset_leg))
               for x0 in (p.gusset_x_in, -p.half_x)]
    body = column + plate_front
    for gz in gussets:
        body = body + gz
    # F04 column inside with the tent: prism along X over the inner width, profile in (y, z)
    y_in_rear = p.y_rear + p.rear_t
    z_tent_rear = p.z_foot_top - (y_in_rear - p.y_rear)          # rear plane through (y_rear, z_foot_top), 45 deg
    inside_profile = [(y_in_rear, p.z_contact), (p.wall_y_rear, p.z_contact), (p.wall_y_rear, p.z_foot_top),
                      (p.ridge_y, p.ridge_z), (y_in_rear, z_tent_rear)]
    x_in = p.half_x - p.side_t
    inside = check_box("column inside", extrude(Plane.YZ.offset(-x_in) * Polygon(*inside_profile, align=None),
                                                amount=2 * x_in, dir=(1, 0, 0)),
                       (-x_in, y_in_rear, p.z_contact), (x_in, p.wall_y_rear, p.z_foot_top))
    body = body - inside
    # F05 hub window, round
    window = Pos(0, 0, p.z_top - p.overrun) * extrude(Circle(p.hub_r), amount=p.plate_t + 2 * p.overrun)
    body = body - window
    # F06 hatch through the plate's lid part
    hatch = Pos(0, 0.5 * (p.hatch_y_lo + p.hatch_y_hi), p.z_top - p.overrun) * extrude(
        RectangleRounded(2 * p.hatch_half_x, p.hatch_y_hi - p.hatch_y_lo, p.hatch_r), amount=p.plate_t + 2 * p.overrun)
    body = body - check_box("hatch", hatch, (-p.hatch_half_x, p.hatch_y_lo, p.z_top - p.overrun),
                            (p.hatch_half_x, p.hatch_y_hi, p.z_contact + p.overrun))
    # F07 rear window with its 45 deg gable toward -Z, through the rear wall along Y
    win_profile = [(-p.win_half_x, p.win_z_hi), (-p.win_half_x, p.win_z_lo), (0.0, p.win_apex_z),
                   (p.win_half_x, p.win_z_lo), (p.win_half_x, p.win_z_hi)]
    win_plane = Plane(origin=(0, p.y_rear - p.overrun, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))
    rear_window = extrude(win_plane * Polygon(*[(x, -z) for x, z in win_profile], align=None),
                          amount=p.rear_t + 2 * p.overrun, dir=(0, 1, 0))
    body = body - check_box("rear window", rear_window, (-p.win_half_x, p.y_rear - p.overrun, p.win_apex_z),
                            (p.win_half_x, y_in_rear + p.overrun, p.win_z_hi))
    # F08 housing holes and F09 counterbores along Z through the plate (counterbore from the top face)
    for sx in (1, -1):
        for sy in (1, -1):
            x, y = sx * p.hole_xy, sy * p.hole_xy
            hole = Location((x, y, p.z_top - p.overrun)) * Cylinder(p.hole_d / 2, p.plate_t + 2 * p.overrun, align=None)
            cbore = Location((x, y, p.z_top - p.overrun)) * Cylinder(p.cb_d / 2, p.cb_depth + p.overrun, align=None)
            body = body - hole - cbore
    # F10 foot holes along Z and F11 their counterbores from the tent face down to z_foot_top
    for sx in (1, -1):
        for y in (p.foot_hole_y1, p.foot_hole_y2):
            fh = Location((sx * p.foot_hole_x, y, p.z_foot_top - p.overrun)) * \
                Cylinder(p.foot_hole_d / 2, p.foot_t + 2 * p.overrun, align=None)
            fcb = Location((sx * p.foot_hole_x, y, p.ridge_z - p.overrun)) * \
                Cylinder(p.foot_cb_d / 2, p.z_foot_top - p.ridge_z + p.overrun, align=None)
            body = body - fh - fcb
    # F12 clean-up
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
    info = {"params": asdict(p), "derived": {"z_top": p.z_top, "z_foot_top": p.z_foot_top, "ridge_z": p.ridge_z,
                                             "win_apex_z": p.win_apex_z},
            "step": {"path": step.name, "sha256": w.sha256},
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
