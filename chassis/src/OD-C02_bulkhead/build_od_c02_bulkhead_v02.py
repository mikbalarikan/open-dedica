"""Build od_c02_bulkhead v02, concept C1 (job 20260930-od-c02-bulkhead, spec 1.1).

build123d 0.11.1, Algebra mode. One parameter structure at the top, named
intermediates, selectors by position only. The frame is the OD-C01 machine frame
of spec section 2: X to the user's right, +Y up, +Z toward the front; y = 0 is the
plate's top face; the wall is centred on x = 65 (OD-C01 A-04). Plan: DESIGN_PLAN.md
with the amendment DESIGN_PLAN_v02.md (brief WP-03).

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/build_od_c02_bulkhead_v02.py \
        [--variant '{"bore_d": 3.95}'] [--out-dir 02_STEP_STL] [--tag v02] [--no-stl] \
        [--record 01_CAD/build_record_v02.json]
Relative paths are taken from the job workspace (the folder above 01_CAD).
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

from build123d import (Align, Box, Compound, Cylinder, Face, Line, Location, Plane, Pos, RigidJoint,
                       ThreePointArc, Wire, extrude)

from tools.core import read_step, write_step, write_stl

HERE = Path(__file__).resolve().parent
WS = HERE.parent
INPUTS = WS / "00_Spec" / "inputs"
TIMESTAMP = "2026-09-30T00:00:00"


@dataclass(frozen=True)
class Params:
    # F01 wall (spec 4 C1, REQ-02, A-01)
    wall_x0: float = 63.0
    wall_x1: float = 67.0
    y_bottom: float = 0.0
    y_top: float = 215.0              # REQ-06, A-06
    z_min: float = -240.0
    z_max: float = -30.0
    # F02 base rail (spec 1.1 section 4, REQ-03, REQ-05, REQ-08)
    brail_x0: float = 59.0
    brail_x1: float = 71.0
    brail_h: float = 12.0
    # F03 top rail (spec 1.1 section 4, REQ-08, A-07)
    trail_x0: float = 59.5
    trail_x1: float = 70.5
    trail_y0: float = 207.0
    # F04 windows (spec 1.1 section 4, REQ-04, A-04)
    win_d: float = 14.0
    win_centres: tuple = ((150.0, -200.0), (150.0, -130.0), (150.0, -60.0), (60.0, -55.0))  # (y, z)
    win_apex_rise: float = 7.0        # beyond the circle's +Z edge (REQ-04)
    win_cut_x: tuple = (62.0, 68.0)   # plan v02: 1.0 past each wall face
    # F05, F06 insert bores (REQ-01, REQ-07, D-05b, A-03, A-05)
    bore_d: float = 4.0
    bore_depth: float = 6.0
    base_bore_xz: tuple = ((65.0, -45.0), (65.0, -105.0), (65.0, -165.0), (65.0, -225.0))
    top_bore_xz: tuple = ((65.0, -60.0), (65.0, -210.0))
    # plan derivation: cutters pass this far beyond a free face
    overshoot: float = 1.0
    # sweep only: every bore shifted by (dx, dz); the wall shifted along X
    shift_x: float = 0.0
    shift_z: float = 0.0
    # U-07 export mesh (plan: 0.20 rad <= 4 acos(1 - 0.01/6.0) = 0.2310)
    stl_tol: float = 0.01
    stl_ang: float = 0.20
    # joints of OD-C01 spec 1.2 section 4 (A-02)
    c03_origin: tuple = (0.0, 40.0, -205.0)
    c03_x_dir: tuple = (0.0, 0.0, 1.0)      # local x -> +Z
    c03_z_dir: tuple = (1.0, 0.0, 0.0)      # local z -> +X (so local y -> -Y)
    c04_origin: tuple = (0.0, 70.0, -140.0)
    g01_origin: tuple = (0.0, 180.06, 32.0)
    g01_x_dir: tuple = (1.0, 0.0, 0.0)      # local x -> +X
    g01_z_dir: tuple = (0.0, -1.0, 0.0)     # local z -> -Y (so local y -> +Z)
    # OD-C05 foot box (spec 2): x +-55, y 0 .. 210, z -70 .. -26
    c05_box_x_half: float = 55.0
    c05_box_y: tuple = (0.0, 210.0)
    c05_box_z: tuple = (-70.0, -26.0)


def box(x0, x1, y0, y1, z0, z1):
    return Pos(x0, y0, z0) * Box(x1 - x0, y1 - y0, z1 - z0, align=(Align.MIN, Align.MIN, Align.MIN))


def gable_outline(r: float, apex: float) -> Face:
    """The window outline in a plane's (u, v) = (Y, Z): the lower half-circle of radius
    r, straight sides from the centre height up to where the 45-degree roof lines
    through the apex (apex above the centre) meet them, and the roof."""
    shoulder = apex - r * math.tan(math.radians(45.0))
    edges = [ThreePointArc((-r, 0.0), (0.0, -r), (r, 0.0)),
             Line((r, 0.0), (r, shoulder)), Line((r, shoulder), (0.0, apex)),
             Line((0.0, apex), (-r, shoulder)), Line((-r, shoulder), (-r, 0.0))]
    return Face(Wire(edges))


def yz_plane(x: float, y: float, z: float) -> Plane:
    """Local u -> +Y, v -> +Z, normal +X."""
    return Plane(origin=(x, y, z), x_dir=(0, 1, 0), z_dir=(1, 0, 0))


def build_bulkhead(p: Params):
    r_win = 0.5 * p.win_d
    apex_win = r_win + p.win_apex_rise                     # 14.0 above the centre
    up = Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))
    # F01-F03
    wall = box(p.wall_x0, p.wall_x1, p.y_bottom, p.y_top, p.z_min, p.z_max)
    base_rail = box(p.brail_x0, p.brail_x1, p.y_bottom, p.y_bottom + p.brail_h, p.z_min, p.z_max)
    top_rail = box(p.trail_x0, p.trail_x1, p.trail_y0, p.y_top, p.z_min, p.z_max)
    body = wall + base_rail + top_rail
    # F04 windows through the wall along X
    x0, x1 = p.win_cut_x
    for yc, zc in p.win_centres:
        window = extrude(yz_plane(x0, yc, zc) * gable_outline(r_win, apex_win), amount=x1 - x0)
        body = body - window
    # F05 base-rail insert bores along +Y from the underside
    for x, z in p.base_bore_xz:
        bore = Pos(x + p.shift_x, p.y_bottom - p.overshoot, z + p.shift_z) * (up * Cylinder(
            0.5 * p.bore_d, p.bore_depth + p.overshoot, align=(Align.CENTER, Align.CENTER, Align.MIN)))
        body = body - bore
    # F06 top-rail insert bores along -Y from the top
    for x, z in p.top_bore_xz:
        bore = Pos(x + p.shift_x, p.y_top - p.bore_depth, z + p.shift_z) * (up * Cylinder(
            0.5 * p.bore_d, p.bore_depth + p.overshoot, align=(Align.CENTER, Align.CENTER, Align.MIN)))
        body = body - bore
    body = body.clean()
    solids = body.solids()
    part = solids[0] if len(solids) == 1 else body
    part.label = "od_c02_bulkhead"
    return part


def c03_location(p: Params) -> Location:
    return Location(Plane(origin=p.c03_origin, x_dir=p.c03_x_dir, z_dir=p.c03_z_dir))


def g01_location(p: Params) -> Location:
    return Location(Plane(origin=p.g01_origin, x_dir=p.g01_x_dir, z_dir=p.g01_z_dir))


def build_assembly(p: Params) -> dict:
    """Bulkhead + OD-C01 + OD-C03 + OD-H01 + OD-C04 + OD-H11 + OD-G01 v02 + the OD-C05
    foot box, each imported part placed by a RigidJoint on the bulkhead at its OD-C01
    section 4 joint, connected to the part's own STEP frame origin. A fresh bulkhead
    is built (a part in an assembly is not the part file's)."""
    bulkhead = build_bulkhead(p)
    joints = {"plate": Location((0.0, 0.0, 0.0)), "c03": c03_location(p), "h01": c03_location(p),
              "c04": Location(p.c04_origin), "h11": Location(p.c04_origin), "g01": g01_location(p)}
    files = {"plate": ("OD-C01_base_frame.step", "od_c01_frame"),
             "c03": ("OD-C03_pump_cradle.step", "od_c03_cradle"),
             "h01": ("OD-H01_ulka_ep5_pump.step", "od_h01_pump"),
             "c04": ("OD-C04_thermoblock_mount.step", "od_c04_mount"),
             "h11": ("OD-H11_thermoblock.step", "od_h11_thermoblock"),
             "g01": ("OD-G01_housing_C1_v02.step", "od_g01_housing")}
    parts, placements = {}, {}
    for key, (fname, label) in files.items():
        comp = read_step(INPUTS / fname)
        sol = comp.solids()
        comp = sol[0] if len(sol) == 1 else comp
        comp.label = label
        RigidJoint(f"joint_{key}", bulkhead, joints[key])
        RigidJoint("own_frame", comp, Location((0.0, 0.0, 0.0)))
        bulkhead.joints[f"joint_{key}"].connect_to(comp.joints["own_frame"])
        parts[key] = comp
        placements[label] = {"joint": f"RigidJoint joint_{key} on the bulkhead (machine frame) -> own_frame",
                             "location": str(comp.location)}
    (y0, y1), (z0, z1) = p.c05_box_y, p.c05_box_z
    foot = box(-p.c05_box_x_half, p.c05_box_x_half, y0, y1, z0, z1)
    foot.label = "od_c05_foot_reference_A02"
    placements[foot.label] = {"joint": "reference box from the brief's values (A-02), not a deliverable",
                              "location": f"x +-{p.c05_box_x_half:g}, y {y0:g} .. {y1:g}, z {z0:g} .. {z1:g}"}
    assembly = Compound(children=[bulkhead, parts["plate"], parts["c03"], parts["h01"], parts["c04"],
                                  parts["h11"], parts["g01"], foot], label="od_c02_assembly")
    return {"assembly": assembly, "placements": placements}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="{}")
    ap.add_argument("--out-dir", default="02_STEP_STL")
    ap.add_argument("--tag", default="v02")
    ap.add_argument("--no-stl", action="store_true")
    ap.add_argument("--no-asm", action="store_true")
    ap.add_argument("--record", default="01_CAD/build_record_v02.json")
    a = ap.parse_args()
    p = Params(**json.loads(a.variant))
    out = Path(a.out_dir)
    out = out if out.is_absolute() else WS / out
    out.mkdir(parents=True, exist_ok=True)
    part = build_bulkhead(p)
    part_path = out / f"od_c02_bulkhead_C1_{a.tag}.step"
    w_part = write_step(part, part_path, timestamp=TIMESTAMP)
    record = {"params": asdict(p), "solids": len(part.solids()),
              "step": {"path": str(part_path.relative_to(WS)), "sha256": w_part.sha256}}
    if not a.no_stl:
        stl_path = out / f"od_c02_bulkhead_C1_{a.tag}.stl"
        w_stl = write_stl(part, stl_path, tolerance=p.stl_tol, angular_tolerance=p.stl_ang)
        record["stl"] = {"path": str(stl_path.relative_to(WS)), "sha256": w_stl.sha256, **w_stl.detail,
                         "tolerance": p.stl_tol, "angular_tolerance": p.stl_ang,
                         "max_sagitta": w_stl.checks["max_sagitta"].measured}
    if not a.no_asm:
        built = build_assembly(p)
        asm_path = out / f"od_c02_assembly_C1_{a.tag}.step"
        try:
            w_asm = write_step(built["assembly"], asm_path, timestamp=TIMESTAMP)
            record["assembly"] = {"path": str(asm_path.relative_to(WS)), "sha256": w_asm.sha256}
        except Exception as exc:  # noqa: BLE001: reported, never swallowed silently
            record["assembly"] = {"error": f"{type(exc).__name__}: {exc}"}
        record["placements"] = built["placements"]
    rec = Path(a.record)
    rec = rec if rec.is_absolute() else WS / rec
    rec.parent.mkdir(parents=True, exist_ok=True)
    rec.write_text(json.dumps(record, indent=1, default=str))
    print(json.dumps({k: v for k, v in record.items() if k != "params"}, indent=1, default=str))


if __name__ == "__main__":
    main()
