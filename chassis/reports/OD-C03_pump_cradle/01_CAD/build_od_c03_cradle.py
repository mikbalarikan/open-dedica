"""Build od_c03_cradle (job 20260930-od-c03-pump-cradle, concept C1, spec 1.1).

One solid in the OD-H01 frame: pump axis at the origin along +Z, theta counter-
clockwise about +Z from +X, +Y down in the machine, the foot underside at y = +40.0
(spec section 2). build123d Algebra mode, named intermediates, one parameter
structure (Usta U-14). Also places OD-H01 (identity joint at the origin, axis +Z)
and the assumed sleeve solid A-03 for the check assembly, exports through the
AP242 writer, and runs check_od_c03_cradle on the re-imported files.

Usage (from the repository root, after sourcing the environment):
    uv run tools/run.py python <workspace>/01_CAD/build_od_c03_cradle.py          (deliverable v01)
    uv run tools/run.py python <workspace>/01_CAD/build_od_c03_cradle.py sweep    (D7 sweep)
"""
from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass, replace
from pathlib import Path

from build123d import (Box, Compound, Cylinder, Face, Line, Location, Pos, Polyline, RigidJoint,
                       Rot, ThreePointArc, Wire, extrude)

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_od_c03_cradle as chk  # noqa: E402

from tools.core import read_step, write_step, write_stl  # noqa: E402

WS = Path(__file__).resolve().parents[1]
PUMP_STEP = WS / "00_Spec/inputs/OD-H01_ulka_ep5_pump.step"
TIMESTAMP = "2026-09-30T00:00:00"


@dataclass(frozen=True)
class P:
    # foot plate (spec 4 C1; U-02; REQ-08; A-11)
    foot_x: float = 40.0            # half width, x -40 ... 40
    foot_y1: float = 40.0           # underside
    foot_t: float = 3.0             # thickness: top at y 37.0
    foot_z0: float = -10.0
    foot_z1: float = 42.0
    # saddle ribs (spec 4 C1; REQ-01, REQ-02; A-03, A-06)
    r_in: float = 26.65             # sleeve OD 53.3 / 2
    r_out: float = 32.0
    th0: float = 45.0
    th1: float = 135.0
    rib_t: float = 6.0
    rib_z0: tuple = (15.0, 25.0)
    # post blocks (spec 4 C1; REQ-06)
    post_x_in: float = 29.5
    post_t: float = 4.0
    post_y_top: float = 0.0
    post_z0: float = 13.0
    post_z1: float = 33.0
    # strap slots (spec 4 C1; REQ-05; A-07)
    slot_w: float = 6.0             # clear, along Z
    slot_h: float = 2.5             # clear, along Y
    slot_yc: float = 7.0
    slot_zc: tuple = (18.0, 28.0)
    roof_deg: float = 45.0          # gable roof from horizontal (D-03a)
    # frame holes (spec 4 C1; REQ-07; A-11)
    hole_d: float = 3.4
    hole_x: float = 34.0
    hole_z: tuple = (-4.0, 37.0)
    # construction (stated derivation: rib webs and posts overlap the foot by this
    # much so the union is a volume overlap, not a face contact; no effect on shape)
    overlap: float = 1.0
    cut_extra: float = 1.0          # cutters run this far past the faces they pierce
    # assumed sleeve OD-H02 (A-03)
    sleeve_id: float = 47.3
    sleeve_od: float = 53.3
    sleeve_z0: float = -6.0
    sleeve_z1: float = 32.0
    sleeve_x_half: float = 23.5
    # STL (U-07)
    stl_tol: float = 0.01
    stl_ang: float = 0.1


def rib(p: P, z0: float):
    """XY profile: inner arc r_in over th0 ... th1, radial end faces to r_out, then
    vertical web faces at x = r_out cos(th) down into the foot; extruded +Z."""
    a0, a1 = math.radians(p.th0), math.radians(p.th1)
    y_web = p.foot_y1 - p.foot_t + p.overlap
    arc_start = (p.r_in * math.cos(a0), p.r_in * math.sin(a0))
    end_out0 = (p.r_out * math.cos(a0), p.r_out * math.sin(a0))
    web0 = (end_out0[0], y_web)
    end_out1 = (p.r_out * math.cos(a1), p.r_out * math.sin(a1))
    web1 = (end_out1[0], y_web)
    arc_end = (p.r_in * math.cos(a1), p.r_in * math.sin(a1))
    am = math.radians((p.th0 + p.th1) / 2)
    arc_mid = (p.r_in * math.cos(am), p.r_in * math.sin(am))
    outline = Wire([Line(arc_start, end_out0), Line(end_out0, web0), Line(web0, web1),
                    Line(web1, end_out1), Line(end_out1, arc_end),
                    ThreePointArc(arc_end, arc_mid, arc_start)])
    profile = Face(outline)
    return Pos(0, 0, z0) * extrude(profile, amount=p.rib_t, dir=(0, 0, 1))


def post(p: P, side: int):
    y0, y1 = p.post_y_top, p.foot_y1 - p.foot_t + p.overlap
    xc = side * (p.post_x_in + p.post_t / 2)
    return Pos(xc, (y0 + y1) / 2, (p.post_z0 + p.post_z1) / 2) * Box(
        p.post_t, y1 - y0, p.post_z1 - p.post_z0)


def slot_cutter(p: P, side: int, zc: float):
    """YZ profile: clear rectangle slot_w x slot_h centred (slot_yc, zc) with a gable
    roof at roof_deg from horizontal on the side away from the bed (-Y), extruded
    along X through the post."""
    y_floor = p.slot_yc + p.slot_h / 2
    y_top = p.slot_yc - p.slot_h / 2
    y_apex = y_top - (p.slot_w / 2) * math.tan(math.radians(p.roof_deg))
    x0 = side * (p.post_x_in - p.cut_extra) if side > 0 else -(p.post_x_in + p.post_t + p.cut_extra)
    pts = [(x0, y_floor, zc - p.slot_w / 2), (x0, y_floor, zc + p.slot_w / 2),
           (x0, y_top, zc + p.slot_w / 2), (x0, y_apex, zc), (x0, y_top, zc - p.slot_w / 2)]
    profile = Face(Wire(Polyline(*pts, close=True)))
    return extrude(profile, amount=p.post_t + 2 * p.cut_extra, dir=(1, 0, 0))


def hole_cutter(p: P, x: float, z: float):
    length = p.foot_t + 2 * p.cut_extra
    return Pos(x, p.foot_y1 - p.foot_t / 2, z) * Rot(90, 0, 0) * Cylinder(p.hole_d / 2, length)


def build(p: P):
    foot = Pos(0, p.foot_y1 - p.foot_t / 2, (p.foot_z0 + p.foot_z1) / 2) * Box(
        2 * p.foot_x, p.foot_t, p.foot_z1 - p.foot_z0)
    ribs = [rib(p, z0) for z0 in p.rib_z0]
    posts = [post(p, s) for s in (-1, 1)]
    slots = [slot_cutter(p, s, zc) for s in (-1, 1) for zc in p.slot_zc]
    holes = [hole_cutter(p, s * p.hole_x, z) for z in p.hole_z for s in (-1, 1)]
    body = foot
    for part in ribs + posts:
        body = body + part
    for cut in slots + holes:
        body = body - cut
    found = body.solids()
    if len(found) != 1:
        raise RuntimeError(f"the cradle built {len(found)} solids")
    cradle = found[0]
    cradle.label = chk.CRADLE
    return cradle


def sleeve(p: P):
    """Assumed OD-H02 (A-03): a tube ID 47.3, OD 53.3, z -6 ... 32 on the pump axis,
    cut back to |x| <= 23.5 so it clears both frame side plates."""
    h = p.sleeve_z1 - p.sleeve_z0
    zc = (p.sleeve_z0 + p.sleeve_z1) / 2
    tube = Pos(0, 0, zc) * (Cylinder(p.sleeve_od / 2, h) - Cylinder(p.sleeve_id / 2, h))
    keep = Pos(0, 0, zc) * Box(2 * p.sleeve_x_half, 2 * p.sleeve_od, h + 2)
    cut = tube & keep
    shell = Compound(cut.solids(), label=chk.SLEEVE)
    return shell


def assembly(cradle_step: Path, p: P):
    """Cradle as re-imported, OD-H01 placed by a rigid joint at the origin with axis +Z
    (identity, the spec's frame), the assumed sleeve on the same axis."""
    cradle = read_step(cradle_step)
    cradle.label = chk.CRADLE
    pump = read_step(PUMP_STEP)
    pump.label = chk.PUMP
    sl = sleeve(p)
    axis = Location((0, 0, 0), (0, 0, 0))
    RigidJoint("pump_axis", to_part=cradle, joint_location=axis)
    RigidJoint("datum", to_part=pump, joint_location=axis)
    RigidJoint("datum", to_part=sl, joint_location=axis)
    cradle.joints["pump_axis"].connect_to(pump.joints["datum"])
    cradle.joints["pump_axis"].connect_to(sl.joints["datum"])
    return Compound(children=[cradle, pump, sl], label="od_c03_assembly")


def export(p: P, folder: Path, tag: str, *, stl: bool, stl_folder: Path | None = None):
    cradle = build(p)
    step = folder / f"od_c03_cradle_{tag}.step"
    asm_step = folder / f"od_c03_assembly_{tag}.step"
    w_part = write_step(cradle, step, timestamp=TIMESTAMP)
    asm = assembly(step, p)
    w_asm = write_step(asm, asm_step, timestamp=TIMESTAMP)
    out = {"step": str(step.relative_to(WS)), "step_sha256": w_part.sha256,
           "assembly": str(asm_step.relative_to(WS)), "assembly_sha256": w_asm.sha256}
    stl_path = None
    if stl:
        stl_path = (stl_folder or folder) / f"od_c03_cradle_{tag}.stl"
        back = read_step(step)
        w_stl = write_stl(back, stl_path, tolerance=p.stl_tol, angular_tolerance=p.stl_ang)
        out.update({"stl": str(stl_path.relative_to(WS)), "stl_sha256": w_stl.sha256,
                    "stl_detail": w_stl.detail})
    res = chk.run_all(step, asm_step, stl_path, built=cradle, angular=p.stl_ang if stl else None)
    res["export"] = out
    return res


SWEEP = {  # fit-critical rows of plan section 4 (low, high); nominal is P()
    "foot_t": (2.9, 3.1),
    "r_in": (26.60, 26.70),
    "th": ((47.0, 133.0), (43.0, 137.0)),
    "post_x_in": (29.4, 29.6),
    "slot_h": (2.5, 2.7),
    "slot_w": (6.0, 6.2),
    "slot_yc": (6.5, 7.5),
    "hole_d": (3.3, 3.5),
}


def variant(name, value) -> P:
    if name == "th":
        return replace(P(), th0=value[0], th1=value[1])
    return replace(P(), **{name: value})


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "deliver"
    if mode == "deliver":
        res = export(P(), WS / "02_STEP_STL", "C1_v01", stl=True)
        (WS / "01_CAD/check_od_c03_cradle_v01.json").write_text(json.dumps(res, indent=1, default=str))
        for g in res["gates"]:
            print(f'{g["gate"]:70s} {g["status"]:13s} {g["measured"]} {g["unit"]} m={g["margin"]} {g["at"] or ""} {g["reason"]}')
        print(json.dumps(res["info"], default=str))
        print(json.dumps(res["facts"], default=str))
        print(json.dumps(res["export"], default=str))
    else:
        folder = WS / "01_CAD/sweep_v01"
        names = sys.argv[2:] or list(SWEEP)
        for name in names:
            for which, value in zip(("low", "high"), SWEEP[name]):
                tag = f"{name}_{which}"
                try:
                    res = export(variant(name, value), folder, tag, stl=True)
                    res["value"] = value
                    res["built"] = True
                except Exception as exc:                         # noqa: BLE001
                    res = {"value": value, "built": False, "error": f"{type(exc).__name__}: {exc}"}
                (folder / f"sweep_{tag}.json").write_text(json.dumps(res, indent=1, default=str))
                print(tag, value, res.get("built"), res.get("error", ""))
