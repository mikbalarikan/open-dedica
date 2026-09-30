"""Build od_c04_mount, concept C1 (job 20260930-od-c04-thermoblock-mount, spec 1.1).

build123d 0.11.1, Algebra mode. One parameter structure at the top, named
intermediates, geometric selectors only. The frame is the OD-H11 STEP frame
(spec section 2): z = 0 on the thermoblock's base face, +Z toward its outlet face,
-Y down in the machine.

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/build_od_c04_mount.py \
        [--variant '{"tip_z": -10.0}'] [--out-dir 02_STEP_STL] [--tag v01] [--no-stl]
Relative paths are taken from the job workspace (the folder above 01_CAD).
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

from build123d import (Align, Box, Compound, Cylinder, Edge, Face, GeomType, Location, Pos, Rectangle,
                       RigidJoint, Wire, extrude, fillet)

from tools.core import fillet_ladder, read_step, write_step, write_stl
from tools.measure import bore_census, clearance, envelope, locate_bore

HERE = Path(__file__).resolve().parent
WS = HERE.parent
TIMESTAMP = "2026-09-30T00:00:00"


@dataclass(frozen=True)
class Params:
    # F01/F02 rear plate (spec 4 C1, REQ-04, U-02)
    plate_half_x: float = 50.0
    plate_y_max: float = 40.0
    plate_back_z: float = -17.0
    plate_front_z: float = -12.0
    plate_corner_r: float = 5.0
    # F03 foot (spec 4 C1, REQ-05, A-10); the plate's -Y edge is the foot underside
    foot_y_min: float = -70.0
    foot_t: float = 4.0
    foot_z_max: float = 33.0
    # F04 gussets (spec 4 C1: 4.0 thick at x +-46; legs: plan derivation)
    gusset_x_center: float = 46.0
    gusset_t: float = 4.0
    gusset_leg: float = 20.0
    # F05-F07 standoffs (spec 4 C1, REQ-02, REQ-03 as amended in spec 1.1, D-04a)
    standoff_d: float = 12.0
    s1_x: float = -19.62
    s1_y: float = 20.18
    s2_x: float = 25.01
    s2_y: float = 9.08
    standoff_shift_x: float = 0.0      # sweep only
    standoff_shift_y: float = 0.0      # sweep only
    tip_z: float = -10.10
    standoff_bore_d: float = 4.0
    root_fillet_radii: tuple = (1.0, 0.8, 0.5)
    # F08 frame holes (REQ-06, A-10; teardrop roof: plan derivation for D-03a)
    frame_hole_d: float = 3.4
    frame_hole_x: float = 40.0
    frame_hole_z_low: float = -8.0
    frame_hole_z_high: float = 26.0
    frame_shift_x: float = 0.0         # sweep only
    frame_shift_z: float = 0.0         # sweep only
    teardrop_roof_deg: float = 50.0
    # spacers (A-05, spec 1.1): designer's modelled solids for the check assembly
    spacer_d: float = 7.0
    spacer_bore_d: float = 4.0
    spacer_len_s1: float = 10.10
    spacer_len_s2: float = 37.70
    # U-07 export mesh
    stl_tol: float = 0.01
    stl_ang: float = 4.0 * math.acos(1.0 - 0.01 / 6.0)
    # cutting tools run this far beyond the faces they pierce
    cut_overrun: float = 1.0


def standoff_axes(p: Params) -> dict:
    return {"S1": (p.s1_x + p.standoff_shift_x, p.s1_y + p.standoff_shift_y),
            "S2": (p.s2_x + p.standoff_shift_x, p.s2_y + p.standoff_shift_y)}


def frame_hole_centres(p: Params) -> list:
    return [(sx * p.frame_hole_x + p.frame_shift_x, z + p.frame_shift_z)
            for z in (p.frame_hole_z_low, p.frame_hole_z_high) for sx in (-1.0, 1.0)]


def teardrop_face(p: Params, cx: float, cz: float, y0: float) -> Face:
    """Frame hole profile in the plane y = y0: a circle of frame_hole_d whose crown
    (toward +Z, the build direction) is replaced by two lines tangent at
    teardrop_roof_deg from horizontal meeting above the centre."""
    r = 0.5 * p.frame_hole_d
    phi = math.radians(90.0 - p.teardrop_roof_deg)            # tangent point angle from horizontal
    apex_h = r / math.cos(math.radians(p.teardrop_roof_deg))   # centre to apex along +Z
    right = (cx + r * math.cos(phi), y0, cz + r * math.sin(phi))
    left = (cx - r * math.cos(phi), y0, cz + r * math.sin(phi))
    bottom = (cx, y0, cz - r)
    apex = (cx, y0, cz + apex_h)
    arc = Edge.make_three_point_arc(right, bottom, left)
    return Face(Wire([arc, Edge.make_line(left, apex), Edge.make_line(apex, right)]))


def build_mount(p: Params) -> dict:
    """The mount and the facts of its build (fillet radius achieved)."""
    plate_t = p.plate_front_z - p.plate_back_z
    plate_len_y = p.plate_y_max - p.foot_y_min
    # F01, F02: plate outline with the two free corners (y max) rounded
    outline = Pos(0.0, p.foot_y_min) * Rectangle(2 * p.plate_half_x, plate_len_y, align=(Align.CENTER, Align.MIN))
    free_corners = [v for v in outline.vertices() if v.Y > p.plate_y_max - 1e-6]
    outline_rounded = fillet(free_corners, p.plate_corner_r)
    plate = extrude(Pos(0.0, 0.0, p.plate_back_z) * outline_rounded, amount=plate_t)
    # F03: foot
    foot = Pos(0.0, p.foot_y_min, p.plate_back_z) * Box(
        2 * p.plate_half_x, p.foot_t, p.foot_z_max - p.plate_back_z, align=(Align.CENTER, Align.MIN, Align.MIN))
    # F04: gussets in the plate-foot corner
    foot_inner_y = p.foot_y_min + p.foot_t
    gussets = []
    for sx in (-1.0, 1.0):
        x0 = sx * p.gusset_x_center - 0.5 * p.gusset_t
        tri = Face(Wire.make_polygon([(x0, foot_inner_y, p.plate_front_z),
                                      (x0, foot_inner_y + p.gusset_leg, p.plate_front_z),
                                      (x0, foot_inner_y, p.plate_front_z + p.gusset_leg)], close=True))
        gussets.append(extrude(tri, amount=p.gusset_t, dir=(1, 0, 0)))
    # F05: standoffs
    axes = standoff_axes(p)
    standoff_h = p.tip_z - p.plate_front_z
    standoffs = [Pos(x, y, p.plate_front_z) * Cylinder(0.5 * p.standoff_d, standoff_h,
                                                        align=(Align.CENTER, Align.CENTER, Align.MIN))
                 for x, y in axes.values()]
    body = plate + foot
    for g in gussets:
        body = body + g
    for s in standoffs:
        body = body + s
    # F06: root fillets on the concave circle at each standoff root
    root_edges = [e for e in body.edges()
                  if e.geom_type == GeomType.CIRCLE and abs(e.radius - 0.5 * p.standoff_d) < 1e-6
                  and abs(e.arc_center.Z - p.plate_front_z) < 1e-6
                  and any(math.hypot(e.arc_center.X - x, e.arc_center.Y - y) < 1e-6 for x, y in axes.values())]
    filleted = fillet_ladder(body, root_edges, p.root_fillet_radii)
    body_filleted = filleted.shape
    # F07: standoff bores through plate and standoff
    bore_len = p.tip_z - p.plate_back_z + 2 * p.cut_overrun
    bores = [Pos(x, y, p.plate_back_z - p.cut_overrun) * Cylinder(
        0.5 * p.standoff_bore_d, bore_len, align=(Align.CENTER, Align.CENTER, Align.MIN)) for x, y in axes.values()]
    # F08: frame holes (teardrops) through the foot along +Y
    y_start = p.foot_y_min - p.cut_overrun
    holes = [extrude(teardrop_face(p, cx, cz, y_start), amount=p.foot_t + 2 * p.cut_overrun, dir=(0, 1, 0))
             for cx, cz in frame_hole_centres(p)]
    mount = body_filleted
    for tool in bores + holes:
        mount = mount - tool
    mount.label = "od_c04_mount"
    return {"mount": mount, "fillet_radius": filleted.radius, "fillet_tried": filleted.tried,
            "root_edges": len(root_edges)}


def build_spacer(p: Params, length: float, label: str):
    """A spacer tube along +Z from z 0 (standoff tip end) to z length (seat end)."""
    tube = (Cylinder(0.5 * p.spacer_d, length, align=(Align.CENTER, Align.CENTER, Align.MIN))
            - Cylinder(0.5 * p.spacer_bore_d, length, align=(Align.CENTER, Align.CENTER, Align.MIN)))
    tube.label = label
    RigidJoint("seat_end", tube, Location((0.0, 0.0, length)))
    return tube


def measured_seats(odh11, p: Params) -> dict:
    """Seat points on OD-H11, measured: each screw hole's axis from locate_bore; the
    seat height where a spacer-sized annulus first meets the casting going +Z (a thin
    probe below the casting and the clearance above it); S2's also read as its bore's
    open end on the mid-lug underside."""
    census = bore_census(odh11)
    seats = {}
    env = envelope(odh11)
    probe_top = {"S1": env["min_z"].measured - 1.0, "S2": None}
    for name, (x, y) in (("S1", (p.s1_x, p.s1_y)), ("S2", (p.s2_x, p.s2_y))):
        near = (x, y, 5.5) if name == "S1" else (x, y, 30.4)
        loc = locate_bore(census, near, (0, 0, 1))
        start, end = loc["diameter"].detail["start"], loc["diameter"].detail["end"]
        ax, ay = start[0], start[1]
        open_ends = loc["diameter"].detail["open_ends"]
        bore_open_low = min(start[2], end[2]) if (open_ends[0] and start[2] <= end[2]) or (
            open_ends[1] and end[2] <= start[2]) else None
        top = probe_top[name] if probe_top[name] is not None else (bore_open_low - 0.6)
        probe = Pos(ax, ay, top - 0.01) * (
            Cylinder(0.5 * p.spacer_d, 0.01, align=(Align.CENTER, Align.CENTER, Align.MIN))
            - Cylinder(0.5 * p.spacer_bore_d, 0.01, align=(Align.CENTER, Align.CENTER, Align.MIN)))
        gap = clearance(probe, odh11)
        seats[name] = {"axis_xy": (ax, ay), "bore_diameter": loc["diameter"].measured,
                       "axis_offset_from_spec": loc["offset"].measured,
                       "bore_start": start, "bore_end": end, "open_ends": open_ends,
                       "probe_top_z": top, "probe_gap": gap.measured, "probe_on_casting": gap.detail["on_b"],
                       "seat_z_probe": top + gap.measured, "seat_z_bore_open_end": bore_open_low}
        seats[name]["seat_z"] = seats[name]["seat_z_probe"]
    return seats


def build_assembly(p: Params, mount, odh11_path: Path):
    """Mount + OD-H11 (identity joint at the origin, axis +Z) + the two spacers
    (joints on the measured seats)."""
    odh11 = read_step(odh11_path)
    odh11.label = "OD-H11_thermoblock"
    RigidJoint("mount_frame", mount, Location((0.0, 0.0, 0.0)))
    RigidJoint("step_origin", odh11, Location((0.0, 0.0, 0.0)))
    mount.joints["mount_frame"].connect_to(odh11.joints["step_origin"])
    seats = measured_seats(odh11, p)
    spacers = []
    for name, length in (("S1", p.spacer_len_s1), ("S2", p.spacer_len_s2)):
        s = seats[name]
        RigidJoint(f"seat_{name}", odh11, Location((s["axis_xy"][0], s["axis_xy"][1], s["seat_z"])))
        sp = build_spacer(p, length, f"spacer_{name}_assumed_A05")
        odh11.joints[f"seat_{name}"].connect_to(sp.joints["seat_end"])
        spacers.append(sp)
    return odh11, spacers, seats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="{}")
    ap.add_argument("--out-dir", default="02_STEP_STL")
    ap.add_argument("--tag", default="v01")
    ap.add_argument("--no-stl", action="store_true")
    ap.add_argument("--record", default="01_CAD/build_record_v01.json")
    a = ap.parse_args()
    p = Params(**json.loads(a.variant))
    out = Path(a.out_dir)
    out = out if out.is_absolute() else WS / out
    built = build_mount(p)
    mount = built["mount"]
    part_path = out / f"od_c04_mount_C1_{a.tag}.step"
    w_part = write_step(mount, part_path, timestamp=TIMESTAMP)
    record = {"params": asdict(p), "fillet_radius_achieved": built["fillet_radius"],
              "fillet_tried": built["fillet_tried"], "root_edges": built["root_edges"],
              "step": {"path": str(part_path.relative_to(WS)), "sha256": w_part.sha256}}
    if not a.no_stl:
        stl_path = out / f"od_c04_mount_C1_{a.tag}.stl"
        w_stl = write_stl(mount, stl_path, tolerance=p.stl_tol, angular_tolerance=p.stl_ang)
        record["stl"] = {"path": str(stl_path.relative_to(WS)), "sha256": w_stl.sha256, **w_stl.detail}
    # the check assembly: a fresh mount instance (a part in a Compound is re-parented)
    mount_for_asm = build_mount(p)["mount"]
    odh11, spacers, seats = build_assembly(p, mount_for_asm, WS / "00_Spec/inputs/OD-H11_thermoblock.step")
    assembly = Compound(children=[mount_for_asm, odh11, *spacers], label="od_c04_assembly")
    asm_path = out / f"od_c04_assembly_C1_{a.tag}.step"
    w_asm = write_step(assembly, asm_path, timestamp=TIMESTAMP)
    record["assembly"] = {"path": str(asm_path.relative_to(WS)), "sha256": w_asm.sha256}
    record["seats"] = seats
    record["placements"] = {
        "OD-H11_thermoblock": {"joint": "RigidJoint mount_frame -> step_origin", "location":
                               str(odh11.location)},
        **{sp.label: {"joint": "RigidJoint seat_S# on OD-H11 -> seat_end", "location": str(sp.location)}
           for sp in spacers}}
    rec = Path(a.record)
    rec = rec if rec.is_absolute() else WS / rec
    rec.parent.mkdir(parents=True, exist_ok=True)
    rec.write_text(json.dumps(record, indent=1, default=str))
    print(json.dumps({k: v for k, v in record.items() if k != "params"}, indent=1, default=str))


if __name__ == "__main__":
    main()
