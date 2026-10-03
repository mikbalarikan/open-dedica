"""Build od_c09_front, concept C1 (job 20261002-od-c09-front-panel, spec 1.1 section 4, plan 01_CAD/DESIGN_PLAN.md).

Machine frame of OD-C01 (spec section 2): X to the user's right, +Y up, +Z toward the user,
the plate's top face y = 0. build123d Algebra mode, named intermediates, one parameter
structure; nothing numeric below it except unit factors (0.5 for a half, 2 for a diameter).

Usage (repository root, tools venv):
    uv run tools/run.py python <ws>/01_CAD/build_od_c09_front.py [--params <json>] [--out-step <path>]
        [--no-stl] [--no-assembly]
Without arguments it writes the v01 deliverables:
    02_STEP_STL/od_c09_front_C1_v01.step, .stl, 02_STEP_STL/od_c09_assembly_C1_v01.step
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field, replace
from pathlib import Path

from build123d import Box, Compound, Cylinder, Plane, Polygon, Pos, Rot, Solid, extrude

WS = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-10-02T00:00:00"


@dataclass(frozen=True)
class Params:
    # wall (spec 4 C1 wall; REQ-02)
    wall_x_half: float = 116.0
    wall_z_in: float = 94.0
    wall_z_out: float = 97.0
    wall_top_y: float = 215.0
    floor_y: float = 0.0
    # brew opening (spec 4 C1; REQ-03): tray slot and portafilter window
    slot_x_half: float = 75.0
    slot_top_y: float = 50.0
    win_x_left: float = -57.5
    win_x_right: float = 75.0
    win_top_y: float = 188.0
    cut_overrun: float = 1.0          # tool overrun past the faces it cuts through (derivation: clean booleans)
    # return ribs (spec 4 C1)
    rib_t: float = 3.0
    rib_z_back: float = 84.0
    rib_overreach: float = 3.0        # R1 runs past the window edges by one rib thickness (spec: x -60.5 ... +78)
    # floor flanges and gussets (spec 4 C1)
    flange_t: float = 4.0
    flange_z_back: float = 72.0
    flange_x_in: float = 76.0
    flange_x_out: float = 104.0
    gusset_t: float = 4.0
    gusset_leg_z: float = 16.0
    gusset_leg_y: float = 30.0
    # flange holes (spec 4 C1; REQ-01; A-01): (x, z) along Y
    flange_hole_d: float = 3.4
    flange_hole_x: tuple = (-95.0, -85.0, 85.0, 95.0)
    flange_hole_z: float = 77.0
    # board bosses (spec 4 C1, spec 1.1 Q2 and Q4): axes on the posed OD-E02 screw holes,
    # measured with bore_census on the posed board (plan section 4; 01_CAD/diag_v01/d1_board.py)
    boss_d: float = 11.0
    boss_axis_upper: tuple = (-91.0555, 153.2349)
    boss_axis_lower: tuple = (-90.9987, 127.2515)
    boss_end_z: float = 85.485        # the board's measured flat (spec 1.1 Q2)
    insert_bore_d: float = 4.0        # OD-F01 (spec 2; D-05b)
    insert_bore_depth: float = 6.0
    # collar reliefs (spec 1.1 Q4): about the posed OD-E02 collar axes (OD-E02_REPORT collar_B1,
    # collar_B3 posed by spec 2), radius collar + 0.5, from below the boss end to the collar's front + 0.5
    relief_axis_upper: tuple = (-94.1720, 166.5131)    # B1 collar
    relief_r_upper: float = 8.5898                     # 8.0898 + 0.5
    relief_axis_lower: tuple = (-93.7309, 113.5432)    # B3 collar
    relief_r_lower: float = 8.6907                     # 8.1907 + 0.5
    relief_z_top: float = 88.9569                      # collar front 88.4569 (measured) + 0.5
    # button holes (spec 4 C1; spec 1.1 Q5): round, on the measured cap axes at z 95.5
    button_hole_d: float = 15.0
    button_axes: tuple = ((-94.2478, 166.5135), (-98.9908, 139.9014), (-93.7652, 113.4263))
    label: str = "od_c09_front"


def params_with(overrides: dict) -> Params:
    """Parameters with overrides (sweep); tuples given as lists are turned back into tuples."""
    clean = {k: (tuple(tuple(x) if isinstance(x, list) else x for x in v) if isinstance(v, list) else v)
             for k, v in overrides.items()}
    return replace(Params(), **clean)


def box(x0, x1, y0, y1, z0, z1):
    return Pos(0.5 * (x0 + x1), 0.5 * (y0 + y1), 0.5 * (z0 + z1)) * Box(x1 - x0, y1 - y0, z1 - z0)


def cyl_z(cx, cy, d, z0, z1):
    return Pos(cx, cy, 0.5 * (z0 + z1)) * Cylinder(0.5 * d, z1 - z0)


def cyl_y(cx, cz, d, y0, y1):
    return Pos(cx, 0.5 * (y0 + y1), cz) * Rot(90, 0, 0) * Cylinder(0.5 * d, y1 - y0)


def build(p: Params) -> Solid:
    o = p.cut_overrun
    # F01 wall
    wall_blank = box(-p.wall_x_half, p.wall_x_half, p.floor_y, p.wall_top_y, p.wall_z_in, p.wall_z_out)
    # F02 brew opening: tray slot union portafilter window, open at the plate
    tray_slot = box(-p.slot_x_half, p.slot_x_half, p.floor_y - o, p.slot_top_y, p.wall_z_in - o, p.wall_z_out + o)
    pf_window = box(p.win_x_left, p.win_x_right, p.floor_y - o, p.win_top_y, p.wall_z_in - o, p.wall_z_out + o)
    wall = wall_blank - tray_slot - pf_window
    # F03 return ribs on the inner face along the opening's edges
    rib_y_top = p.win_top_y + p.rib_t
    r1 = box(p.win_x_left - p.rib_t, p.win_x_right + p.rib_t, p.win_top_y, rib_y_top, p.rib_z_back, p.wall_z_in)
    r2 = box(p.win_x_right, p.win_x_right + p.rib_t, p.floor_y, rib_y_top, p.rib_z_back, p.wall_z_in)
    r3 = box(p.win_x_left - p.rib_t, p.win_x_left, p.slot_top_y, rib_y_top, p.rib_z_back, p.wall_z_in)
    r4 = box(-p.slot_x_half - p.rib_t, -p.slot_x_half, p.floor_y, p.slot_top_y + p.rib_t, p.rib_z_back, p.wall_z_in)
    r5 = box(-p.slot_x_half - p.rib_t, p.win_x_left, p.slot_top_y, p.slot_top_y + p.rib_t, p.rib_z_back, p.wall_z_in)
    ribs = r1 + r2 + r3 + r4 + r5
    # F04 floor flanges
    flange_l = box(-p.flange_x_out, -p.flange_x_in, p.floor_y, p.floor_y + p.flange_t, p.flange_z_back, p.wall_z_in)
    flange_r = box(p.flange_x_in, p.flange_x_out, p.floor_y, p.floor_y + p.flange_t, p.flange_z_back, p.wall_z_in)
    flanges = flange_l + flange_r
    # F05 gussets: right triangles in YZ, legs along the flange top and up the wall
    y_f = p.floor_y + p.flange_t
    tri = [(y_f, p.wall_z_in - p.gusset_leg_z), (y_f, p.wall_z_in), (y_f + p.gusset_leg_y, p.wall_z_in)]
    gusset_x0 = (-p.flange_x_out, -p.flange_x_in - p.gusset_t, p.flange_x_in, p.flange_x_out - p.gusset_t)
    # the triangle's winding gives its face a -X normal, so the extrusion direction is stated, never implied
    gussets = [extrude(Plane.YZ.offset(x0) * Polygon(*tri, align=None), amount=p.gusset_t, dir=Plane.YZ.z_dir)
               for x0 in gusset_x0]
    gusset_set = gussets[0] + gussets[1] + gussets[2] + gussets[3]
    # F07 bosses, F08 collar reliefs, F09 insert bores (each boss finished before it is fused)
    bosses = []
    for axis, rel_axis, rel_r in ((p.boss_axis_upper, p.relief_axis_upper, p.relief_r_upper),
                                  (p.boss_axis_lower, p.relief_axis_lower, p.relief_r_lower)):
        boss_blank = cyl_z(axis[0], axis[1], p.boss_d, p.boss_end_z, p.wall_z_in)
        relief = cyl_z(rel_axis[0], rel_axis[1], 2 * rel_r, p.boss_end_z - o, p.relief_z_top)
        bosses.append(boss_blank - relief)
    body = wall + ribs + flanges + gusset_set + bosses[0] + bosses[1]
    # F06 flange holes along Y
    for x in p.flange_hole_x:
        body = body - cyl_y(x, p.flange_hole_z, p.flange_hole_d, p.floor_y - o, y_f + o)
    # F09 insert bores, blind from each boss end
    for axis in (p.boss_axis_upper, p.boss_axis_lower):
        body = body - cyl_z(axis[0], axis[1], p.insert_bore_d, p.boss_end_z - o, p.boss_end_z + p.insert_bore_depth)
    # F10 button holes through the wall
    for (x, y) in p.button_axes:
        body = body - cyl_z(x, y, p.button_hole_d, p.wall_z_in - o, p.wall_z_out + o)
    found = body.solids()
    if len(found) != 1:
        raise RuntimeError(f"the build gave {len(found)} solids")
    part = Solid(found[0].wrapped)
    part.label = p.label
    return part


def main():
    from tools.core import read_step, solids, write_step, write_stl
    ap = argparse.ArgumentParser()
    ap.add_argument("--params", default=None)
    ap.add_argument("--out-step", default=str(WS / "02_STEP_STL" / "od_c09_front_C1_v01.step"))
    ap.add_argument("--no-stl", action="store_true")
    ap.add_argument("--no-assembly", action="store_true")
    args = ap.parse_args()
    p = params_with(json.loads(args.params)) if args.params else Params()
    part = build(p)
    step = Path(args.out_step)
    w = write_step(part, step, timestamp=TIMESTAMP)
    print("step", step.name, w.sha256)
    back = Solid(solids(read_step(step))[0])
    if not args.no_stl:
        stl = step.with_suffix(".stl")
        tol, ang = 0.01, 0.15        # U-07: tol 0.01; ang <= 4 acos(1 - 0.01 / R_max), R_max 8.69 (relief) -> 0.1919
        ws = write_stl(back, stl, tolerance=tol, angular_tolerance=ang)
        meta = {"tolerance_mm": tol, "angular_tolerance_rad": ang, **{k: v for k, v in ws.detail.items()},
                "sha256": ws.sha256}
        (WS / "01_CAD" / f"{stl.stem}.stl_meta.json").write_text(json.dumps(meta, indent=1))
        print("stl", stl.name, ws.sha256, ws.detail)
    if not args.no_assembly:
        import sys
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from check_od_c09_front import load_refs
        refs = load_refs()
        refs.pop("_ident")
        names = {"C01": "OD-C01_base_frame", "C05": "OD-C05_group_head_carrier", "housing": "OD-G01_housing",
                 "G04": "OD-G04", "G10": "OD-G10_portafilter_locked", "C10": "OD-C10_top_panel",
                 "E02": "OD-E02_control_board"}
        kids = [Solid(solids(read_step(step))[0])]
        kids[0].label = p.label
        for k, n in names.items():
            s = Solid(refs[k].wrapped)
            s.label = n
            kids.append(s)
        asm = Compound(children=kids, label="od_c09_assembly")
        wa = write_step(asm, step.with_name(step.name.replace("od_c09_front", "od_c09_assembly")), timestamp=TIMESTAMP)
        print("assembly", wa.path.name, wa.sha256)


if __name__ == "__main__":
    main()
