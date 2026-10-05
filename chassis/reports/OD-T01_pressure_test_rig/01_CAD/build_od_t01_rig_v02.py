"""Build od_t01_rig v02, concept C1 (job 20261002-od-t01-pressure-test-rig), spec 1.3.

A closed frame printed on its side: top plate, two walls (z −60 … +40), base, four
10 × 10 inside chamfers, four Ø3.4 holes under Ø6.5 counterbores (teardrop roofs),
a R30 hub window (teardrop roof), four Ø4.5 bench holes (teardrop roofs). Rig frame
of spec §2: X right, +Y up, +Z toward the user, bench top y 0, housing axis x 0, z 0.
build123d Algebra mode; every number is in PARAMS (sources in DESIGN_PLAN §4, as amended
by spec 1.3: plate 25 thick, y 135 … 160; counterbore floor y 140, 5.0 under the head).

Usage (repo root, tools venv):
    uv run tools/run.py python <ws>/01_CAD/build_od_t01_rig_v02.py [--out-dir DIR] [--tag v02]
        [--set name=value ...] [--no-assembly] [--no-stl]
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

from build123d import Box, Circle, Compound, Plane, Polygon, Pos, extrude

WS = Path(__file__).resolve().parent.parent
INPUTS = WS / "00_Spec" / "inputs"
TIMESTAMP = "2026-10-03T00:00:00"


@dataclass(frozen=True)
class Params:
    # frame (spec §4 C1)
    depth_z0: float = -60.0          # rear face (bed in the print)
    depth_z1: float = 60.0           # front edge of the plate and the base
    wall_z1: float = 40.0            # walls stop here (spec 1.1, Q1)
    base_x: float = 120.0            # base half-width
    base_t: float = 10.0             # base y 0 … base_t
    wall_x_in: float = 75.0
    wall_x_out: float = 90.0
    plate_y0: float = 135.0          # underside, the housing's rear-face plane
    plate_y1: float = 160.0          # spec 1.3: plate 25 thick
    plate_x: float = 90.0
    corner_chamfer: float = 10.0     # 45° 10 × 10 in the four inside corners
    # housing screws (REQ-01)
    screw_x: float = 44.0
    screw_z: float = 44.0
    screw_d: float = 3.4
    cbore_d: float = 6.5
    cbore_floor_y: float = 140.0     # spec 1.3: 5.0 of plate under the head
    # hub window (REQ-03)
    window_r: float = 30.0
    # every teardrop roof (spec 1.1 Q3)
    theta_roof: float = 45.1
    # bench holes (REQ-06)
    bench_x: float = 105.0
    bench_z: float = 40.0
    bench_d: float = 4.5
    # cutters
    overrun: float = 1.0


def teardrop(r: float, theta_deg: float):
    """A circle of radius r with a roof toward local +Y: two flanks tangent to the
    circle at theta from the local X axis, meeting on the local Y axis at r / cos θ."""
    t = math.radians(theta_deg)
    tx, ty = r * math.sin(t), r * math.cos(t)
    kite = Polygon((0.0, 0.0), (tx, ty), (0.0, r / math.cos(t)), (-tx, ty), align=None)
    return Circle(r) + kite


def cutter_y(sketch, x: float, z: float, y_top: float, y_bot: float):
    """Extrude a sketch drawn in (X, Z) — local y toward rig +Z — down along −Y from y_top to y_bot."""
    plane = Plane(origin=(x, y_top, z), x_dir=(1, 0, 0), z_dir=(0, -1, 0))
    return extrude(plane * sketch, amount=y_top - y_bot)


def build(p: Params = Params()):
    depth = p.depth_z1 - p.depth_z0
    zc = (p.depth_z0 + p.depth_z1) / 2
    plate_t = p.plate_y1 - p.plate_y0
    # F01 frame: plate and base full depth, walls with their chamfers z −60 … +40
    plate = Pos(0, p.plate_y0 + plate_t / 2, zc) * Box(2 * p.plate_x, plate_t, depth)
    base = Pos(0, p.base_t / 2, zc) * Box(2 * p.base_x, p.base_t, depth)
    c = p.corner_chamfer
    wall_profile = Polygon((p.wall_x_in - c, p.base_t), (p.wall_x_out, p.base_t), (p.wall_x_out, p.plate_y0),
                           (p.wall_x_in - c, p.plate_y0), (p.wall_x_in, p.plate_y0 - c),
                           (p.wall_x_in, p.base_t + c), align=None)
    wall_right = extrude(Plane.XY.offset(p.depth_z0) * wall_profile, amount=p.wall_z1 - p.depth_z0)
    wall_left = wall_right.mirror(Plane.YZ)
    frame = plate + base + wall_right + wall_left
    # F02 hub window R30 with a teardrop roof toward +Z, through the plate
    window = cutter_y(teardrop(p.window_r, p.theta_roof), 0.0, 0.0, p.plate_y1 + p.overrun, p.plate_y0 - p.overrun)
    body = frame - window
    # F03 counterbores, F04 Ø3.4 holes (no teardrop: the named exception)
    for sx in (1, -1):
        for sz in (1, -1):
            x, z = sx * p.screw_x, sz * p.screw_z
            cbore = cutter_y(teardrop(p.cbore_d / 2, p.theta_roof), x, z, p.plate_y1 + p.overrun, p.cbore_floor_y)
            hole = cutter_y(Circle(p.screw_d / 2), x, z, p.cbore_floor_y + p.overrun, p.plate_y0 - p.overrun)
            body = body - cbore - hole
    # F05 bench holes with teardrop roofs, through the base
    for sx in (1, -1):
        for sz in (1, -1):
            bench = cutter_y(teardrop(p.bench_d / 2, p.theta_roof), sx * p.bench_x, sz * p.bench_z,
                             p.base_t + p.overrun, -p.overrun)
            body = body - bench
    body = body.clean()
    solids = list(body.solids())
    if len(solids) != 1:
        raise RuntimeError(f"the build gave {len(solids)} solids")
    rig = solids[0]
    rig.label = "od_t01_rig"
    return rig


def main():
    from tools.core import read_step, write_step, write_stl
    from tools.measure import envelope

    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default=str(WS / "02_STEP_STL"))
    ap.add_argument("--tag", default="v02")
    ap.add_argument("--name", default="od_t01_rig_C1")
    ap.add_argument("--set", nargs="*", default=[])
    ap.add_argument("--no-assembly", action="store_true")
    ap.add_argument("--no-stl", action="store_true")
    ap.add_argument("--meta-dir", default=str(WS / "01_CAD"), help="where the params and mesh records go")
    a = ap.parse_args()
    over = {}
    for kv in a.set:
        k, v = kv.split("=")
        over[k] = float(v)
    p = Params(**over)
    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    step = out / f"{a.name}_{a.tag}.step"
    rig = build(p)
    w = write_step(rig, step, timestamp=TIMESTAMP)
    print("step", step.name, w.sha256)
    record = {"params": asdict(p), "step": step.name, "step_sha256": w.sha256}
    meta_dir = Path(a.meta_dir)
    meta_dir.mkdir(parents=True, exist_ok=True)
    (meta_dir / f"{a.name}_{a.tag}.params.json").write_text(json.dumps(record, indent=1))
    if not a.no_stl:
        back = read_step(step)
        stl = out / f"{a.name}_{a.tag}.stl"
        ws = write_stl(back, stl, tolerance=0.01, angular_tolerance=0.10)
        meta = {k: ws.detail.get(k) for k in ("tolerance_mm", "angular_tolerance_rad", "triangles", "max_sagitta_mm")}
        meta.update({"stl": stl.name, "sha256": ws.sha256, "meshed_from": step.name})
        (meta_dir / f"{a.name}_{a.tag}.mesh.json").write_text(json.dumps(meta, indent=1))
        print("stl", stl.name, ws.sha256, meta)
    if not a.no_assembly:
        # F07 the check assembly: a fresh rig (a part in an assembly cannot be written on its own)
        from importlib import util
        spec = util.spec_from_file_location("check", Path(__file__).with_name("check_od_t01_rig_v02.py"))
        chk = util.module_from_spec(spec)
        spec.loader.exec_module(chk)
        housing, g04, g10 = chk.identify(read_step(INPUTS / "od_g01_assembly_C1_v03.step"))
        rig2 = read_step(step)
        rig2 = list(rig2.solids())[0]
        rig2.label = "od_t01_rig"
        seat = chk.seat_y_of(rig2)               # the joint: housing rear face on the measured underside
        loc = chk.housing_pose(seat)
        parts = []
        for name, s in (("od_g01_housing", housing), ("od_g04_gasket_support", g04), ("od_g10_portafilter", g10)):
            q = loc * s
            q.label = name
            parts.append(q)
        asm = Compound(children=[rig2, *parts], label="od_t01_assembly")
        astep = out / f"od_t01_assembly_C1_{a.tag}.step"
        wa = write_step(asm, astep, timestamp=TIMESTAMP)
        print("assembly", astep.name, wa.sha256, "seat y", seat)
    print("envelope", {k: round(v.measured, 4) for k, v in envelope(rig).items()})


if __name__ == "__main__":
    main()
