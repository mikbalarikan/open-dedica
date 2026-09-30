"""Build od_c01_frame v02, concept C1 (job 20260930-od-c01-base-frame, spec 1.2).

v02 (brief WP-04) against v01: four more insert holes for the OD-C07 valve and
flowmeter mount (REQ-10, A-17); OD-G01 v02 placed at the vertical group head pose
(spec 1.2 section 4, A-01); the carrier foot reference box x +-55, z -70 .. -26.

build123d 0.11.1, Algebra mode. One parameter structure at the top, named
intermediates, geometric selectors only. The frame is the spec section 2 machine
frame: X to the user's right, +Y up, +Z toward the user; y = 0 is the plate's top
face (the floor plane), x = 0 the group head axis' vertical plane.

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/build_od_c01_frame_v02.py \
        [--variant '{"plate_t": 5.9}'] [--out-dir 02_STEP_STL] [--tag v02] [--no-stl]
Relative paths are taken from the job workspace (the folder above 01_CAD).
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

from build123d import (Align, Box, Compound, Cylinder, Location, Plane, Pos, RectangleRounded, RigidJoint,
                       extrude)

from tools.core import read_step, write_step, write_stl

HERE = Path(__file__).resolve().parent
WS = HERE.parent
INPUTS = WS / "00_Spec" / "inputs"
TIMESTAMP = "2026-09-30T00:00:00"


@dataclass(frozen=True)
class Params:
    # F01 plate (spec 4 C1, U-02, REQ-07)
    y_top: float = 0.0
    plate_t: float = 6.0
    x_half: float = 120.0
    z_min: float = -305.0
    z_max: float = 100.0
    corner_r: float = 10.0
    # F02-F05, F05b insert holes (spec 4 C1, REQ-01 .. REQ-04, REQ-10, A-01 .. A-04, A-17, A-11)
    insert_d: float = 4.0
    carrier_xz: tuple = ((35.0, -40.0), (-35.0, -40.0), (35.0, -60.0), (-35.0, -60.0))
    c04_xz: tuple = ((40.0, -148.0), (-40.0, -148.0), (40.0, -114.0), (-40.0, -114.0))
    c03_xz: tuple = ((-4.0, -239.0), (-4.0, -171.0), (37.0, -239.0), (37.0, -171.0))
    bulkhead_xz: tuple = ((65.0, -45.0), (65.0, -105.0), (65.0, -165.0), (65.0, -225.0))
    valve_xz: tuple = ((-113.0, -42.0), (-71.0, -42.0), (-113.0, -148.5), (-71.0, -148.5))  # OD-C07, A-17
    # F06 feet holes (spec 4 C1, REQ-05, A-12)
    foot_d: float = 3.4
    foot_xz: tuple = ((110.0, 90.0), (-110.0, 90.0), (110.0, -295.0), (-110.0, -295.0))
    # F07 drain holes (spec 4 C1, REQ-06, A-13)
    drain_d: float = 8.0
    drain_xz: tuple = ((-80.0, -120.0), (-80.0, -230.0))
    # sweep only: every hole group shifted by (dx, dz)
    shift_x: float = 0.0
    shift_z: float = 0.0
    # plan derivation: cutters longer than the plate by this at each face
    hole_overshoot: float = 1.0
    # U-07 export mesh (plan: 0.20 rad <= 4 acos(1 - 0.01/6.0) = 0.2310)
    stl_tol: float = 0.01
    stl_ang: float = 0.20
    # joints of spec 4 (A-01 .. A-03)
    # OD-G01 v02 at the carrier's (= housing's) pose, spec 1.2 section 4, A-01: local x -> X,
    # local y -> +Z, local z -> -Y (proper), origin (0, 180.06, 32.0)
    g01_origin: tuple = (0.0, 180.06, 32.0)
    g01_x_dir: tuple = (1.0, 0.0, 0.0)      # local x -> +X
    g01_z_dir: tuple = (0.0, -1.0, 0.0)     # local z -> -Y (so local y -> +Z)
    c04_origin: tuple = (0.0, 70.0, -140.0)
    c03_origin: tuple = (0.0, 40.0, -205.0)
    c03_x_dir: tuple = (0.0, 0.0, 1.0)      # local x -> +Z
    c03_z_dir: tuple = (1.0, 0.0, 0.0)      # local z -> +X (so local y -> -Y)
    # OD-C05 foot outline reference box (A-01, spec 1.2 section 4; brief WP-04): x +-55, y 0 .. 4, z -70 .. -26
    c05_box_x_half: float = 55.0
    c05_box_h: float = 4.0
    c05_box_z: tuple = (-70.0, -26.0)


def hole_table(p: Params) -> list:
    """(feature, diameter, x, z) of every through-hole, with the sweep shift applied."""
    rows = []
    for feat, d, pts in (("F02_carrier", p.insert_d, p.carrier_xz), ("F03_c04", p.insert_d, p.c04_xz),
                         ("F04_c03", p.insert_d, p.c03_xz), ("F05_bulkhead", p.insert_d, p.bulkhead_xz),
                         ("F05b_valve", p.insert_d, p.valve_xz),
                         ("F06_feet", p.foot_d, p.foot_xz), ("F07_drain", p.drain_d, p.drain_xz)):
        rows += [(feat, d, x + p.shift_x, z + p.shift_z) for x, z in pts]
    return rows


def build_plate(p: Params):
    """F01 plate with R corners, F02-F07 through-holes along Y; labelled od_c01_frame."""
    y_bottom = p.y_top - p.plate_t
    # F01: outline on the plane y = y_bottom, normal +Y (its local x -> machine +X, local y -> machine -Z)
    bed_plane = Plane(origin=(0.0, y_bottom, 0.5 * (p.z_min + p.z_max)), x_dir=(1, 0, 0), z_dir=(0, 1, 0))
    outline = RectangleRounded(2.0 * p.x_half, p.z_max - p.z_min, p.corner_r)
    slab = extrude(bed_plane * outline, amount=p.plate_t)
    # F02-F07: cutters along Y, overshooting both faces
    cut_len = p.plate_t + 2.0 * p.hole_overshoot
    y_mid = y_bottom + 0.5 * p.plate_t
    up = Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))
    cutters = [Pos(x, y_mid, z) * (up * Cylinder(0.5 * d, cut_len, align=(Align.CENTER, Align.CENTER, Align.CENTER)))
               for _, d, x, z in hole_table(p)]
    plate = slab
    for c in cutters:
        plate = plate - c
    plate = plate.clean()
    solids = plate.solids()
    plate = solids[0] if len(solids) == 1 else plate
    plate.label = "od_c01_frame"
    return plate


def c03_location(p: Params) -> Location:
    return Location(Plane(origin=p.c03_origin, x_dir=p.c03_x_dir, z_dir=p.c03_z_dir))


def g01_location(p: Params) -> Location:
    return Location(Plane(origin=p.g01_origin, x_dir=p.g01_x_dir, z_dir=p.g01_z_dir))


def build_assembly(p: Params) -> dict:
    """Plate + OD-C03 + OD-H01 + OD-C04 + OD-H11 + OD-G01 v02 + the OD-C05 foot
    reference box, each placed by a RigidJoint on the plate at its spec 4 joint
    connected to the component's own frame origin (its STEP frame)."""
    plate = build_plate(p)
    joints = {"c03": c03_location(p), "h01": c03_location(p), "c04": Location(p.c04_origin),
              "h11": Location(p.c04_origin), "g01": g01_location(p)}
    files = {"c03": ("OD-C03_pump_cradle.step", "od_c03_cradle"),
             "h01": ("OD-H01_ulka_ep5_pump.step", "od_h01_pump"),
             "c04": ("OD-C04_thermoblock_mount.step", "od_c04_mount"),
             "h11": ("OD-H11_thermoblock.step", "od_h11_thermoblock"),
             "g01": ("OD-G01_housing_C1_v02.step", "od_g01_housing")}
    parts = {}
    placements = {}
    for key, (fname, label) in files.items():
        comp = read_step(INPUTS / fname)
        sol = comp.solids()
        comp = sol[0] if len(sol) == 1 else comp
        comp.label = label
        RigidJoint(f"joint_{key}", plate, joints[key])
        RigidJoint("own_frame", comp, Location((0.0, 0.0, 0.0)))
        plate.joints[f"joint_{key}"].connect_to(comp.joints["own_frame"])
        parts[key] = comp
        placements[label] = {"joint": f"RigidJoint joint_{key} on the plate -> own_frame (STEP origin)",
                             "location": str(comp.location)}
    z0, z1 = p.c05_box_z
    box = Pos(0.0, p.y_top, z0) * Box(2.0 * p.c05_box_x_half, p.c05_box_h, z1 - z0,
                                      align=(Align.CENTER, Align.MIN, Align.MIN))
    box.label = "od_c05_foot_reference_A01"
    placements[box.label] = {"joint": "reference box from spec 4 values (A-01), not a deliverable solid",
                             "location": f"x +-{p.c05_box_x_half:g}, y 0 .. {p.c05_box_h:g}, z {z0:g} .. {z1:g}"}
    assembly = Compound(children=[plate, parts["c03"], parts["h01"], parts["c04"], parts["h11"], parts["g01"], box],
                        label="od_c01_assembly")
    return {"assembly": assembly, "placements": placements}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="{}")
    ap.add_argument("--out-dir", default="02_STEP_STL")
    ap.add_argument("--tag", default="v02")
    ap.add_argument("--no-stl", action="store_true")
    ap.add_argument("--record", default="01_CAD/build_record_v02.json")
    a = ap.parse_args()
    p = Params(**json.loads(a.variant))
    out = Path(a.out_dir)
    out = out if out.is_absolute() else WS / out
    out.mkdir(parents=True, exist_ok=True)
    plate = build_plate(p)
    part_path = out / f"od_c01_frame_C1_{a.tag}.step"
    w_part = write_step(plate, part_path, timestamp=TIMESTAMP)
    record = {"params": asdict(p), "holes": len(hole_table(p)),
              "step": {"path": str(part_path.relative_to(WS)), "sha256": w_part.sha256}}
    if not a.no_stl:
        stl_path = out / f"od_c01_frame_C1_{a.tag}.stl"
        w_stl = write_stl(plate, stl_path, tolerance=p.stl_tol, angular_tolerance=p.stl_ang)
        record["stl"] = {"path": str(stl_path.relative_to(WS)), "sha256": w_stl.sha256, **w_stl.detail,
                         "max_sagitta": w_stl.checks["max_sagitta"].measured}
    built = build_assembly(p)
    asm_path = out / f"od_c01_assembly_C1_{a.tag}.step"
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
