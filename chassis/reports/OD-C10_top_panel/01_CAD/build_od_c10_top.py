"""Build od_c10_top v01, concept C1 (job 20261001-od-c10-top-panel, spec 1.1).

build123d 0.11.1, Algebra mode. One parameter structure at the top, named
intermediates, selectors by position only, no fillets (the spec names none). The
frame is the OD-C01 machine frame of spec section 2: X to the user's right, +Y up,
+Z toward the front; y = 0 is the plate's top face; the lid's top face is y = 250.0.
Plan: 01_CAD/DESIGN_PLAN.md.

Usage (from the repository root, in the tools venv):
    uv run tools/run.py python <ws>/01_CAD/build_od_c10_top.py \
        [--variant '{"hole_d": 3.3}'] [--out-dir 02_STEP_STL] [--tag v01] [--no-stl] [--no-asm] \
        [--record 01_CAD/build_record_v01.json]
Relative paths are taken from the job workspace (the folder above 01_CAD).
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

from build123d import (Align, Compound, Cylinder, Location, Plane, Polygon, Pos, RectangleRounded, RigidJoint,
                       extrude)

from tools.core import read_step, write_step, write_stl
from tools.measure import envelope

HERE = Path(__file__).resolve().parent
WS = HERE.parent
INPUTS = WS / "00_Spec" / "inputs"
TIMESTAMP = "2026-10-01T00:00:00"


@dataclass(frozen=True)
class Params:
    # F01 skin and outline (spec 4 C1, REQ-01, REQ-02)
    x_half: float = 120.0
    z_min: float = -305.0
    z_max: float = 100.0
    corner_r: float = 10.0
    y_top: float = 250.0
    skin_t: float = 3.0
    # F02 skirt (spec 4, REQ-02, A-04)
    skirt_t: float = 3.0
    skirt_bottom_y: float = 215.0
    # F03 columns (spec 4, REQ-03, REQ-04, A-01, A-02)
    col_d: float = 12.0
    bulkhead_cols: tuple = ((65.0, -60.0), (65.0, -210.0))
    rear_cols: tuple = ((90.0, -293.0), (-90.0, -293.0))
    col_bottom_y: float = 215.0
    # F07, F08 holes (REQ-03, D-04a, REQ-07, A-05)
    hole_d: float = 3.4
    cbore_d: float = 6.5
    cbore_floor_y: float = 218.0
    # F06 pads (spec 4, REQ-05, A-03)
    pad_d: float = 10.0
    pads: tuple = ((48.0, 30.0), (-48.0, 30.0))
    pad_bottom_y: float = 210.5
    # F04, F05 ribs (spec 4, E-06; plan section 4 derivations)
    rib_t: float = 3.0
    rib_reach: float = 20.0
    rib_root_y: float = 222.0
    rear_rib_bottom_y: float = 216.0
    rear_rib_dx: float = 4.0
    rear_rib_into_skirt: float = 1.0
    # plan derivation: cutters pass this far beyond a free face; unions overlap the skin by this much
    overshoot: float = 1.0
    # sweep only: every column (and its ribs and holes) shifted by this much
    col_dx: float = 0.0
    col_dz: float = 0.0
    # U-07 export mesh (plan: 0.17 rad <= 4 acos(1 - 0.01/10.0) = 0.1789)
    stl_tol: float = 0.01
    stl_ang: float = 0.17
    # OD-C01 A-01 joint of OD-C05 (local x -> X, y -> +Z, z -> -Y)
    c05_origin: tuple = (0.0, 180.06, 32.0)
    c05_x_dir: tuple = (1.0, 0.0, 0.0)
    c05_z_dir: tuple = (0.0, -1.0, 0.0)
    # OD-C01 A-17 joint of OD-C07 (local x -> -Z, y -> -X, z -> +Y)
    c07_origin: tuple = (-92.0, 0.0, -60.0)
    c07_x_dir: tuple = (0.0, 0.0, -1.0)
    c07_z_dir: tuple = (0.0, 1.0, 0.0)


def y_cylinder(x, z, r, y0, y1):
    """A cylinder along +Y from y0 to y1 on the axis (x, z)."""
    up = Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))
    return Pos(x, y0, z) * (up * Cylinder(r, y1 - y0, align=(Align.CENTER, Align.CENTER, Align.MIN)))


def outline_prism(p: Params, inset: float, y0: float, y1: float):
    """The plate outline (x +-x_half, z z_min .. z_max, vertical corners corner_r about
    fixed centres) inset by `inset`, as a prism from y0 to y1. The corner radius shrinks
    with the inset, so the centres stay at (+-(x_half - corner_r), z_min + corner_r) etc."""
    xz = Plane(origin=(0.0, y0, 0.5 * (p.z_min + p.z_max)), x_dir=(1, 0, 0), z_dir=(0, 1, 0))
    sk = RectangleRounded(2.0 * (p.x_half - inset), (p.z_max - p.z_min) - 2.0 * inset, p.corner_r - inset)
    return extrude(xz * sk, amount=y1 - y0)


def columns(p: Params):
    return [(x + p.col_dx, z + p.col_dz) for x, z in tuple(p.bulkhead_cols) + tuple(p.rear_cols)]


def bulkhead_rib(p: Params, xc: float, zc: float, sense: float):
    """F04: right-triangle rib in the XY plane, rib_t thick about z = zc, from the column
    axis toward sense * X: vertical leg on the axis from the skin underside down to
    rib_root_y, horizontal leg along the skin to rib_reach; its top runs overshoot into the skin."""
    y_sk = p.y_top - p.skin_t
    xy = Plane(origin=(0.0, 0.0, zc - 0.5 * p.rib_t), x_dir=(1, 0, 0), z_dir=(0, 0, 1))
    tip = xc + sense * p.rib_reach
    poly = Polygon((xc, p.rib_root_y), (tip, y_sk), (tip, y_sk + p.overshoot), (xc, y_sk + p.overshoot), align=None)
    return extrude(xy * poly, amount=p.rib_t, dir=(0, 0, 1))


def rear_rib(p: Params, x_centre: float, zc: float):
    """F05: rib in the YZ plane, rib_t thick about x = x_centre: from rear_rib_into_skirt
    inside the rear skirt to the column axis at rear_rib_bottom_y, then a hypotenuse up to
    the skin at rib_reach in front of the axis; its top runs overshoot into the skin."""
    y_sk = p.y_top - p.skin_t
    z_back = p.z_min + p.skirt_t - p.rear_rib_into_skirt
    yz = Plane(origin=(x_centre - 0.5 * p.rib_t, 0.0, 0.0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))  # u -> +Y, v -> +Z
    poly = Polygon((p.rear_rib_bottom_y, z_back), (p.rear_rib_bottom_y, zc), (y_sk, zc + p.rib_reach),
                   (y_sk + p.overshoot, zc + p.rib_reach), (y_sk + p.overshoot, z_back), align=None)
    return extrude(yz * poly, amount=p.rib_t, dir=(1, 0, 0))


def build_lid(p: Params):
    y_sk = p.y_top - p.skin_t
    # F01 top skin
    skin = outline_prism(p, 0.0, y_sk, p.y_top)
    # F02 perimeter skirt, overlapping the skin by overshoot
    skirt = outline_prism(p, 0.0, p.skirt_bottom_y, y_sk + p.overshoot) - \
        outline_prism(p, p.skirt_t, p.skirt_bottom_y - p.overshoot, y_sk + p.overshoot)
    body = skin + skirt
    cols = columns(p)
    n_bulk = len(p.bulkhead_cols)
    # F03 columns
    for x, z in cols:
        body = body + y_cylinder(x, z, 0.5 * p.col_d, p.col_bottom_y, y_sk + p.overshoot)
    # F04 bulkhead-column ribs along +-X
    for x, z in cols[:n_bulk]:
        for sense in (1.0, -1.0):
            body = body + bulkhead_rib(p, x, z, sense)
    # F05 rear-column ribs along Z, two per column at x = xc +- rear_rib_dx
    for x, z in cols[n_bulk:]:
        for s in (1.0, -1.0):
            body = body + rear_rib(p, x + s * p.rear_rib_dx, z)
    # F06 rest pads
    for x, z in p.pads:
        body = body + y_cylinder(x, z, 0.5 * p.pad_d, p.pad_bottom_y, y_sk + p.overshoot)
    # F07 through-holes, F08 counterbores
    for x, z in cols:
        body = body - y_cylinder(x, z, 0.5 * p.hole_d, p.col_bottom_y - p.overshoot, p.cbore_floor_y + p.overshoot)
        body = body - y_cylinder(x, z, 0.5 * p.cbore_d, p.cbore_floor_y, p.y_top + p.overshoot)
    body = body.clean()
    solids = body.solids()
    part = solids[0] if len(solids) == 1 else body
    part.label = "od_c10_top"
    return part


def c05_location(p: Params) -> Location:
    return Location(Plane(origin=p.c05_origin, x_dir=p.c05_x_dir, z_dir=p.c05_z_dir))


def c07_location(p: Params) -> Location:
    return Location(Plane(origin=p.c07_origin, x_dir=p.c07_x_dir, z_dir=p.c07_z_dir))


FILES = {"plate": ("OD-C01_base_frame.step", "od_c01_frame"),
         "c02": ("OD-C02_bulkhead.step", "od_c02_bulkhead"),
         "c05": ("OD-C05_group_head_carrier.step", "od_c05_carrier"),
         "c07": ("OD-C07_valve_flowmeter_mount.step", "od_c07_valve_mount"),
         "c11": ("OD-C11_back_panel_v02.step", "od_c11_back")}


def build_assembly(p: Params) -> dict:
    """Lid + OD-C01 + OD-C02 + OD-C05 + OD-C07 + OD-C11, each reference placed by a
    RigidJoint on the lid at its OD-C01 joint (the identity for OD-C01, OD-C02 and
    OD-C11; A-01 for OD-C05; A-17 for OD-C07), connected to the part's own STEP frame
    origin. A fresh lid is built (a part in an assembly is not the part file's)."""
    lid = build_lid(p)
    ident = Location((0.0, 0.0, 0.0))
    joints = {"plate": ident, "c02": ident, "c05": c05_location(p), "c07": c07_location(p), "c11": ident}
    parts, placements = {}, {}
    for key, (fname, label) in FILES.items():
        comp = read_step(INPUTS / fname)
        sol = comp.solids()
        comp = sol[0] if len(sol) == 1 else comp
        comp.label = label
        RigidJoint(f"joint_{key}", lid, joints[key])
        RigidJoint("own_frame", comp, Location((0.0, 0.0, 0.0)))
        lid.joints[f"joint_{key}"].connect_to(comp.joints["own_frame"])
        parts[key] = comp
        e = envelope(comp)
        placements[label] = {"joint": f"RigidJoint joint_{key} on the lid (machine frame) -> own_frame",
                             "location": str(comp.location),
                             "placed_envelope": {k: round(v.measured, 4) for k, v in e.items()}}
    assembly = Compound(children=[lid] + [parts[k] for k in FILES], label="od_c10_assembly")
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
    part = build_lid(p)
    part_path = out / f"od_c10_top_C1_{a.tag}.step"
    w_part = write_step(part, part_path, timestamp=TIMESTAMP)
    record = {"params": asdict(p), "solids": len(part.solids()), "faces": len(part.faces()),
              "step": {"path": str(part_path.relative_to(WS)), "sha256": w_part.sha256}}
    if not a.no_stl:
        stl_path = out / f"od_c10_top_C1_{a.tag}.stl"
        w_stl = write_stl(part, stl_path, tolerance=p.stl_tol, angular_tolerance=p.stl_ang)
        record["stl"] = {"path": str(stl_path.relative_to(WS)), "sha256": w_stl.sha256, **w_stl.detail,
                         "tolerance": p.stl_tol, "angular_tolerance": p.stl_ang,
                         "max_sagitta": w_stl.checks["max_sagitta"].measured}
    if not a.no_asm:
        built = build_assembly(p)
        asm_path = out / f"od_c10_assembly_C1_{a.tag}.step"
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
