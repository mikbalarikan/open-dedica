"""Build od_c08_tray v01, concept C1 (job 20261001-od-c08-electronics-bay-tray, spec 1.0).

build123d 0.11.1, Algebra mode. One parameter structure at the top, named
intermediates, no index selectors. The frame is the OD-C01 machine frame of spec
section 2: X to the user's right, +Y up, +Z toward the front; y = 0 is the plate's
top face. Plan: 01_CAD/DESIGN_PLAN.md (features F01 .. F08).

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/build_od_c08_tray.py \
        [--variant '{"pin_d": 1.85}'] [--out-dir 02_STEP_STL] [--tag v01] [--no-stl] [--no-asm] \
        [--record 01_CAD/build_record_v01.json]
Relative paths are taken from the job workspace (the folder above 01_CAD).
"""
from __future__ import annotations

import argparse
import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path

from build123d import Align, Box, Compound, Cylinder, Face, Location, Plane, Pos, RigidJoint, Wire, extrude

from tools.core import read_step, write_step, write_stl

HERE = Path(__file__).resolve().parent
WS = HERE.parent
INPUTS = WS / "00_Spec" / "inputs"
TIMESTAMP = "2026-10-01T00:00:00"


@dataclass(frozen=True)
class Params:
    # F01 wall and floor flange (spec 4 C1; U-02, REQ-01, REQ-03)
    wall_x0: float = 73.0
    wall_x1: float = 76.0
    wall_y1: float = 92.0
    flange_x1: float = 112.0
    flange_t: float = 4.0
    z_min: float = -230.0
    z_max: float = -70.0
    # F02 gussets (spec 4; E-06)
    gusset_t: float = 3.0
    gusset_leg: float = 20.0
    gusset_z0: tuple = (-230.0, -212.0, -88.0, -73.0)
    # F03-F06 standoffs, insert bores, pins (spec 4; REQ-02, D-04d, D-05a, D-05b, J-05)
    seat_x: float = 82.438            # plan: the measured solder face of the placed OD-E01 (84.0 - 1.562)
    insert_boss_d: float = 10.0
    bore_d: float = 4.0
    bore_depth: float = 6.0
    insert_yz: tuple = ((80.00, -100.00), (27.99, -100.01))
    pin_boss_d: float = 6.0
    pin_d: float = 1.8
    pin_len: float = 2.5
    pin_yz: tuple = ((81.98, -157.52), (30.99, -157.51))
    # F07 flange holes (spec 4; REQ-01, D-04a, A-01)
    hole_d: float = 3.4
    hole_xz: tuple = ((88.0, -222.0), (106.0, -222.0), (88.0, -78.0), (106.0, -78.0))
    # F08 tie slots (spec 4; E-11)
    slot_w_z: float = 2.0
    slot_h_y: float = 4.0
    slot_y0: float = 86.0
    slot_zc: tuple = (-176.0, -168.0, -122.0, -114.0)
    # plan derivation: cutters pass this far beyond a free face
    overshoot: float = 1.0
    # sweep only: every standoff, bore and pin shifted by (dy, dz)
    shift_y: float = 0.0
    shift_z: float = 0.0
    # U-07 export mesh (plan: 0.20 rad <= 4 acos(1 - 0.01/5.0) = 0.2530)
    stl_tol: float = 0.01
    stl_ang: float = 0.20
    # board joint of spec 4 (A-03): board x -> -Z, board z -> +X (so board y -> +Y)
    board_origin: tuple = (84.0, 80.0, -100.0)
    board_x_dir: tuple = (0.0, 0.0, -1.0)
    board_z_dir: tuple = (1.0, 0.0, 0.0)


def box(x0, x1, y0, y1, z0, z1):
    return Pos(x0, y0, z0) * Box(x1 - x0, y1 - y0, z1 - z0, align=(Align.MIN, Align.MIN, Align.MIN))


def x_cylinder(x0, length, y, z, d):
    """A cylinder of diameter d along +X from x0, axis at (y, z)."""
    pl = Plane(origin=(x0, y, z), x_dir=(0, 1, 0), z_dir=(1, 0, 0))
    return pl * Cylinder(0.5 * d, length, align=(Align.CENTER, Align.CENTER, Align.MIN))


def y_cylinder(y0, length, x, z, d):
    """A cylinder of diameter d along +Y from y0, axis at (x, z)."""
    pl = Plane(origin=(x, y0, z), x_dir=(1, 0, 0), z_dir=(0, 1, 0))
    return pl * Cylinder(0.5 * d, length, align=(Align.CENTER, Align.CENTER, Align.MIN))


def xy_prism(points, z0, depth):
    """A prism of the XY polygon `points`, from z0 along +Z by depth."""
    face = Face(Wire.make_polygon([(x, y, z0) for x, y in points], close=True))
    if face.normal_at().Z < 0:
        face = -face
    return extrude(face, amount=depth)


def build_tray(p: Params):
    y_fl = p.flange_t
    # F01 wall + flange: one L section along Z
    l_section = [(p.wall_x0, 0.0), (p.flange_x1, 0.0), (p.flange_x1, y_fl), (p.wall_x1, y_fl),
                 (p.wall_x1, p.wall_y1), (p.wall_x0, p.wall_y1)]
    wall_flange = xy_prism(l_section, p.z_min, p.z_max - p.z_min)
    # F02 gussets: right triangles, legs along the wall's +X face and the flange's top
    gusset_tri = [(p.wall_x1, y_fl), (p.wall_x1 + p.gusset_leg, y_fl), (p.wall_x1, y_fl + p.gusset_leg)]
    gussets = [xy_prism(gusset_tri, z0, p.gusset_t) for z0 in p.gusset_z0]
    body = wall_flange
    for g in gussets:
        body = body + g
    # F03, F04 standoffs from the wall's face to the seat
    standoff_h = p.seat_x - p.wall_x1
    insert_bosses = [x_cylinder(p.wall_x1, standoff_h, y + p.shift_y, z + p.shift_z, p.insert_boss_d)
                     for y, z in p.insert_yz]
    pin_bosses = [x_cylinder(p.wall_x1, standoff_h, y + p.shift_y, z + p.shift_z, p.pin_boss_d)
                  for y, z in p.pin_yz]
    # F05 locating pins on the pin bosses
    pins = [x_cylinder(p.seat_x, p.pin_len, y + p.shift_y, z + p.shift_z, p.pin_d) for y, z in p.pin_yz]
    for s in insert_bosses + pin_bosses + pins:
        body = body + s
    # F06 insert bores along -X from the seat (cutters start at the floor, end past the seat)
    insert_bores = [x_cylinder(p.seat_x - p.bore_depth, p.bore_depth + p.overshoot, y + p.shift_y, z + p.shift_z,
                               p.bore_d) for y, z in p.insert_yz]
    # F07 flange holes along Y, through
    flange_holes = [y_cylinder(-p.overshoot, y_fl + 2.0 * p.overshoot, x, z, p.hole_d) for x, z in p.hole_xz]
    # F08 tie slots through the wall along X
    tie_slots = [box(p.wall_x0 - p.overshoot, p.wall_x1 + p.overshoot, p.slot_y0, p.slot_y0 + p.slot_h_y,
                     zc - 0.5 * p.slot_w_z, zc + 0.5 * p.slot_w_z) for zc in p.slot_zc]
    for c in insert_bores + flange_holes + tie_slots:
        body = body - c
    body = body.clean()
    solids = body.solids()
    part = solids[0] if len(solids) == 1 else body
    part.label = "od_c08_tray"
    return part


def board_location(p: Params) -> Location:
    return Location(Plane(origin=p.board_origin, x_dir=p.board_x_dir, z_dir=p.board_z_dir))


def build_assembly(p: Params) -> dict:
    """Tray + OD-E01 at the spec section 4 joint + OD-C01 + OD-C02 (both at the
    identity), each imported part placed by a RigidJoint on the tray connected to the
    part's own STEP frame origin. A fresh tray is built (a part in an assembly is not
    the part file's)."""
    tray = build_tray(p)
    joints = {"board": board_location(p), "plate": Location((0.0, 0.0, 0.0)), "c02": Location((0.0, 0.0, 0.0))}
    files = {"board": ("OD-E01_power_pcb.step", "od_e01_power_pcb"),
             "plate": ("OD-C01_base_frame.step", "od_c01_frame"),
             "c02": ("OD-C02_bulkhead.step", "od_c02_bulkhead")}
    parts, placements = {}, {}
    for key, (fname, label) in files.items():
        comp = read_step(INPUTS / fname)
        sol = comp.solids()
        comp = sol[0] if len(sol) == 1 else comp
        comp.label = label
        RigidJoint(f"joint_{key}", tray, joints[key])
        RigidJoint("own_frame", comp, Location((0.0, 0.0, 0.0)))
        tray.joints[f"joint_{key}"].connect_to(comp.joints["own_frame"])
        parts[key] = comp
        placements[label] = {"joint": f"RigidJoint joint_{key} on the tray (machine frame) -> own_frame",
                             "location": str(comp.location)}
    assembly = Compound(children=[tray, parts["board"], parts["plate"], parts["c02"]], label="od_c08_assembly")
    return {"assembly": assembly, "placements": placements}


def _rel(path: Path) -> str:
    """The path relative to the workspace (portable, rule 10)."""
    return os.path.relpath(path, WS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="{}")
    ap.add_argument("--out-dir", default="02_STEP_STL")
    ap.add_argument("--tag", default="v01")
    ap.add_argument("--no-stl", action="store_true")
    ap.add_argument("--no-asm", action="store_true")
    ap.add_argument("--record", default="01_CAD/build_record_v01.json")
    a = ap.parse_args()
    p = Params(**json.loads(a.variant))
    out = Path(a.out_dir)
    out = out if out.is_absolute() else WS / out
    out.mkdir(parents=True, exist_ok=True)
    part = build_tray(p)
    part_path = out / f"od_c08_tray_C1_{a.tag}.step"
    w_part = write_step(part, part_path, timestamp=TIMESTAMP)
    record = {"params": asdict(p), "solids": len(part.solids()), "volume_mm3": part.volume,
              "step": {"path": _rel(part_path), "sha256": w_part.sha256}}
    if not a.no_stl:
        stl_path = out / f"od_c08_tray_C1_{a.tag}.stl"
        w_stl = write_stl(part, stl_path, tolerance=p.stl_tol, angular_tolerance=p.stl_ang)
        record["stl"] = {"path": _rel(stl_path), "sha256": w_stl.sha256, **w_stl.detail,
                         "tolerance": p.stl_tol, "angular_tolerance": p.stl_ang,
                         "max_sagitta": w_stl.checks["max_sagitta"].measured}
    if not a.no_asm:
        built = build_assembly(p)
        asm_path = out / f"od_c08_assembly_C1_{a.tag}.step"
        try:
            w_asm = write_step(built["assembly"], asm_path, timestamp=TIMESTAMP)
            record["assembly"] = {"path": _rel(asm_path), "sha256": w_asm.sha256}
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
