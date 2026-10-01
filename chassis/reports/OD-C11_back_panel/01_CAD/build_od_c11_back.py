"""Build od_c11_back v01, concept C1 (job 20261001-od-c11-back-panel, spec 1.0).

build123d 0.11.1, Algebra mode. One parameter structure at the top, named
intermediates, selectors by position only, no fillets (the spec names none). The
frame is the OD-C01 machine frame of spec section 2: X to the user's right, +Y up,
+Z toward the front; y = 0 is the plate's top face; the outer face is z = -302.0.
Plan: 01_CAD/DESIGN_PLAN.md.

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/build_od_c11_back.py \
        [--variant '{"flange_hole_d": 3.3}'] [--out-dir 02_STEP_STL] [--tag v01] [--no-stl] [--no-asm] \
        [--record 01_CAD/build_record_v01.json]
Relative paths are taken from the job workspace (the folder above 01_CAD).
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

from build123d import (Align, Box, Compound, Cylinder, Location, Plane, Polygon, Pos, RigidJoint,
                       SlotCenterToCenter, extrude)

from tools.core import read_step, write_step, write_stl

HERE = Path(__file__).resolve().parent
WS = HERE.parent
INPUTS = WS / "00_Spec" / "inputs"
TIMESTAMP = "2026-10-01T00:00:00"


@dataclass(frozen=True)
class Params:
    # F01 wall (spec 4 C1, REQ-02, A-02)
    wall_x_half: float = 116.0
    wall_z_out: float = -302.0
    wall_z_in: float = -299.0
    y_bottom: float = 0.0
    y_top: float = 215.0                      # REQ-07, A-05
    # F02 floor flanges (spec 4, REQ-01, REQ-05, A-07)
    flange_x: tuple = (72.0, 114.0)           # mirrored about x = 0
    flange_t: float = 4.0
    flange_z1: float = -283.0
    # F03 gussets (spec 4, E-06)
    gusset_t: float = 4.0
    gusset_leg_wall: float = 30.0
    gusset_x0: tuple = (72.0, 110.0)          # each 4.0 thick, mirrored
    # F04 top ledge (spec 4, REQ-07)
    ledge_x_half: float = 114.0
    ledge_y0: float = 211.0
    ledge_z1: float = -287.0
    # F05 insert bosses (spec 4, D-05a, J-05)
    boss_x: tuple = (84.0, 96.0)              # mirrored
    boss_y0: float = 203.0
    # F06 flange holes (REQ-01, D-04a, A-01)
    flange_hole_d: float = 3.4
    flange_hole_xz: tuple = ((81.0, -290.0), (100.0, -290.0), (-81.0, -290.0), (-100.0, -290.0))
    # F07 insert bores (REQ-07, D-05b, A-05)
    insert_d: float = 4.0
    insert_depth: float = 6.0
    insert_xz: tuple = ((90.0, -293.0), (-90.0, -293.0))
    # F08 pass-throughs (REQ-03, REQ-04, A-03, A-04)
    pass_d: float = 12.0
    pass_xy: tuple = ((95.0, 30.0), (-100.0, 30.0), (-84.0, 30.0))
    # F09 vent slots (REQ-06, A-06)
    vent_w: float = 4.0
    vent_y: tuple = (100.0, 180.0)
    vent_x: tuple = (78.0, 86.0, 94.0, 102.0, 110.0)
    # plan derivation: cutters pass this far beyond a free face
    overshoot: float = 1.0
    # sweep only: the flange holes shifted along X (each away from x = 0 by this much)
    flange_hole_dx: float = 0.0
    # U-07 export mesh (plan: 0.20 rad <= 4 acos(1 - 0.01/6.0) = 0.2310)
    stl_tol: float = 0.01
    stl_ang: float = 0.20
    # OD-C01 A-03 joint of OD-C03 and OD-H01 (local x -> +Z, y -> -Y, z -> +X)
    c03_origin: tuple = (0.0, 40.0, -205.0)
    c03_x_dir: tuple = (0.0, 0.0, 1.0)
    c03_z_dir: tuple = (1.0, 0.0, 0.0)


def box(x0, x1, y0, y1, z0, z1):
    return Pos(x0, y0, z0) * Box(x1 - x0, y1 - y0, z1 - z0, align=(Align.MIN, Align.MIN, Align.MIN))


def y_cylinder(x, z, r, y0, y1):
    """A cylinder along +Y from y0 to y1 on the axis (x, z)."""
    up = Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))
    return Pos(x, y0, z) * (up * Cylinder(r, y1 - y0, align=(Align.CENTER, Align.CENTER, Align.MIN)))


def z_cylinder(x, y, r, z0, z1):
    return Pos(x, y, z0) * Cylinder(r, z1 - z0, align=(Align.CENTER, Align.CENTER, Align.MIN))


def gusset(p: Params, x0: float):
    """Right triangle in the YZ plane, 4.0 thick from x0 along +X: a leg along the
    flange's top over the flange's whole depth (y = flange_t, z wall_z_in .. flange_z1,
    16.0 at nominal, spec 4) and a leg up the wall (z = wall_z_in, y flange_t .. +30)."""
    yz = Plane(origin=(x0, 0.0, 0.0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))   # local u -> +Y, v -> +Z
    y0, z0 = p.y_bottom + p.flange_t, p.wall_z_in
    tri = Polygon((y0, z0), (y0, p.flange_z1), (y0 + p.gusset_leg_wall, z0), align=None)
    return extrude(yz * tri, amount=p.gusset_t, dir=(1, 0, 0))   # along +X whatever the winding


def build_panel(p: Params):
    xh = p.wall_x_half
    # F01 wall
    wall = box(-xh, xh, p.y_bottom, p.y_top, p.wall_z_out, p.wall_z_in)
    body = wall
    # F02 floor flanges, mirrored
    fx0, fx1 = p.flange_x
    for s in (1.0, -1.0):
        flange = box(min(s * fx0, s * fx1), max(s * fx0, s * fx1), p.y_bottom, p.y_bottom + p.flange_t,
                     p.wall_z_in, p.flange_z1)
        body = body + flange
    # F03 gussets, four, each 4.0 thick at the flange's ends
    for g0 in p.gusset_x0:
        body = body + gusset(p, g0)                       # +X side: x g0 .. g0 + 4
        body = body + gusset(p, -g0 - p.gusset_t)         # -X side: mirrored
    # F04 top ledge
    ledge = box(-p.ledge_x_half, p.ledge_x_half, p.ledge_y0, p.y_top, p.wall_z_in, p.ledge_z1)
    body = body + ledge
    # F05 insert bosses under the ledge
    bx0, bx1 = p.boss_x
    for s in (1.0, -1.0):
        boss = box(min(s * bx0, s * bx1), max(s * bx0, s * bx1), p.boss_y0, p.ledge_y0, p.wall_z_in, p.ledge_z1)
        body = body + boss
    # F06 flange holes, through along Y
    for x, z in p.flange_hole_xz:
        xs = x + (p.flange_hole_dx if x > 0 else -p.flange_hole_dx)
        hole = y_cylinder(xs, z, 0.5 * p.flange_hole_d, p.y_bottom - p.overshoot,
                          p.y_bottom + p.flange_t + p.overshoot)
        body = body - hole
    # F07 insert bores, blind along -Y from the top, flat floor
    for x, z in p.insert_xz:
        bore = y_cylinder(x, z, 0.5 * p.insert_d, p.y_top - p.insert_depth, p.y_top + p.overshoot)
        body = body - bore
    # F08 pass-throughs, through the wall along Z
    z0, z1 = p.wall_z_out - p.overshoot, p.wall_z_in + p.overshoot
    for x, y in p.pass_xy:
        body = body - z_cylinder(x, y, 0.5 * p.pass_d, z0, z1)
    # F09 vent slots, through the wall along Z
    vy0, vy1 = p.vent_y
    for xc in p.vent_x:
        pl = Plane(origin=(xc, 0.5 * (vy0 + vy1), z0), x_dir=(1, 0, 0), z_dir=(0, 0, 1))
        slot = extrude(pl * SlotCenterToCenter(vy1 - vy0 - p.vent_w, p.vent_w, rotation=90), amount=z1 - z0)
        body = body - slot
    body = body.clean()
    solids = body.solids()
    part = solids[0] if len(solids) == 1 else body
    part.label = "od_c11_back"
    return part


def c03_location(p: Params) -> Location:
    return Location(Plane(origin=p.c03_origin, x_dir=p.c03_x_dir, z_dir=p.c03_z_dir))


def build_assembly(p: Params) -> dict:
    """Panel + OD-C01 + OD-C02 + OD-C03 + OD-H01, each imported part placed by a
    RigidJoint on the panel at its OD-C01 section 4 joint (the identity for OD-C01 and
    OD-C02; A-03 for OD-C03 and OD-H01), connected to the part's own STEP frame origin.
    A fresh panel is built (a part in an assembly is not the part file's)."""
    panel = build_panel(p)
    joints = {"plate": Location((0.0, 0.0, 0.0)), "c02": Location((0.0, 0.0, 0.0)),
              "c03": c03_location(p), "h01": c03_location(p)}
    files = {"plate": ("OD-C01_base_frame.step", "od_c01_frame"),
             "c02": ("OD-C02_bulkhead.step", "od_c02_bulkhead"),
             "c03": ("OD-C03_pump_cradle.step", "od_c03_cradle"),
             "h01": ("OD-H01_ulka_ep5_pump.step", "od_h01_pump")}
    parts, placements = {}, {}
    for key, (fname, label) in files.items():
        comp = read_step(INPUTS / fname)
        sol = comp.solids()
        comp = sol[0] if len(sol) == 1 else comp
        comp.label = label
        RigidJoint(f"joint_{key}", panel, joints[key])
        RigidJoint("own_frame", comp, Location((0.0, 0.0, 0.0)))
        panel.joints[f"joint_{key}"].connect_to(comp.joints["own_frame"])
        parts[key] = comp
        placements[label] = {"joint": f"RigidJoint joint_{key} on the panel (machine frame) -> own_frame",
                             "location": str(comp.location)}
    assembly = Compound(children=[panel, parts["plate"], parts["c02"], parts["c03"], parts["h01"]],
                        label="od_c11_assembly")
    return {"assembly": assembly, "placements": placements}


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
    part = build_panel(p)
    part_path = out / f"od_c11_back_C1_{a.tag}.step"
    w_part = write_step(part, part_path, timestamp=TIMESTAMP)
    record = {"params": asdict(p), "solids": len(part.solids()), "faces": len(part.faces()),
              "step": {"path": str(part_path.relative_to(WS)), "sha256": w_part.sha256}}
    if not a.no_stl:
        stl_path = out / f"od_c11_back_C1_{a.tag}.stl"
        w_stl = write_stl(part, stl_path, tolerance=p.stl_tol, angular_tolerance=p.stl_ang)
        record["stl"] = {"path": str(stl_path.relative_to(WS)), "sha256": w_stl.sha256, **w_stl.detail,
                         "tolerance": p.stl_tol, "angular_tolerance": p.stl_ang,
                         "max_sagitta": w_stl.checks["max_sagitta"].measured}
    if not a.no_asm:
        built = build_assembly(p)
        asm_path = out / f"od_c11_assembly_C1_{a.tag}.step"
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
