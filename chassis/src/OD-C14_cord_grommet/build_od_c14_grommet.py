"""Build od_c14_grommet_half, concept C1 (job 20261002-od-c14-cord-grommet, spec 1.1).

build123d 0.11.1, Algebra mode. The whole grommet is one closed (r, z) profile revolved
about the cord's axis, then cut by the plane 0.4 short of the axis (the split face);
the result is one half at its installed open pose. The half is built in a local frame
(origin where the OD-C11 cord hole's axis meets the wall's outer face, +Z into the
machine) and placed by one joint on the hole as measured with tools.measure.locate_bore.

The check assembly carries OD-C11 and OD-C01 at the identity, the half, its copy turned
180° about the measured hole axis, and the cord, tie and tie-head envelopes. The tie
envelope is placed on the half's measured groove: its inner face on the groove floor
and its outer side on the groove's neck-side face.

Usage (from the repo root, through tools/run.py):
  python 01_CAD/build_od_c14_grommet.py            nominal, into 02_STEP_STL/
  python 01_CAD/build_od_c14_grommet.py --sweep    the D7 runs, into 01_CAD/sweep_v01/
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from pathlib import Path

import build123d as bd
from build123d import Axis, Box, Compound, Cylinder, GeomType, Keep, Location, Plane, Pos

HERE = Path(__file__).resolve().parent
WS = HERE.parent

from tools.core import read_step, write_step, write_stl          # noqa: E402
from tools.measure import bore_census, locate_bore              # noqa: E402
from tools.measure.features import cylinder                     # noqa: E402

# ---- parameters (mm, degrees; local z from the wall's outer face along the hole axis) --
PARAMS = {
    "flange_d": 20.0,          # §4 REQ-01
    "flange_t": 2.0,           # §4: z -304.0 … -302.0
    "neck_d": 11.3,            # §4 1.1: 0.35 per side in the Ø12.0 hole (D-04d)
    "neck_len": 3.2,           # §4 1.1: -302.0 … -298.8, 0.2 beyond the inner face
    "groove_d": 10.3,          # §4 1.1: wall 1.65 over the Ø7.0 bore (D-01b)
    "groove_w": 5.2,           # §4: -298.8 … -293.6, the 4.8 tie + 0.4
    "flank_deg": 60.0,         # §4 1.1 Q1: from horizontal (D-03a)
    "collar_d": 11.3,          # §4 1.1
    "collar_top": 11.0,        # §4: z -291.0
    "bore_d": 7.0,             # §4, A-02
    "chamfer_in": 0.5,         # §4: 0.5 × 45° at the inside end
    "chamfer_out_axial": 0.50,     # §4: outside end, 60° from horizontal in the print
    "chamfer_out_radial": 0.29,
    "split_y": 0.4,            # §4, A-05: the split face 0.4 short of the axis (machine y 30.4)
    "stl_tol": 0.01,           # §5 U-07
    "stl_ang": 0.10,           # §5 U-07: ≤ 4·acos(1 − 0.01/10.0) = 0.1789 rad
    "tie_w": 4.8,              # §2 A-04
    "tie_band": 1.3,           # §2 A-04
    "head_x": 5.0, "head_y": 6.0, "head_z": 5.0,     # §5 U-03 (spec 1.1 Q2)
    "cord_d": 7.0,             # §2 A-02
    "cord_z": (-330.0, -260.0),    # §5 U-03, machine z
}
FIT_CRITICAL = {               # D7 sweep: each REQ-01 / REQ-02 tolerance band (plan §4, spec 1.1 Q4)
    "neck_d": 0.05, "neck_len": 0.1, "groove_d": 0.05, "groove_w": 0.1, "collar_d": 0.05,
    "bore_d": 0.1, "split_y": 0.02,
}
TIMESTAMP = "2026-10-02T12:00:00"
HALF_LABEL = "od_c14_grommet_half"
LABELS = ("od_c11_back_panel", "od_c01_base_frame", "half_upper", "half_lower",
          "cord_envelope", "tie_envelope", "tie_head_box")


def hole_frame(c11):
    """The joint: the OD-C11 cord hole as measured (start point on the wall's outer face,
    axis direction). Refuses an axis off machine Z, since the half carries no rotation."""
    loc = locate_bore(bore_census(c11), (95.0, 30.0, -300.5), (0, 0, 1))
    for k in ("diameter", "offset", "through"):
        if not loc[k].ok:
            raise RuntimeError(f"the cord hole is not measured: {loc[k].reason}")
    start, end = loc["diameter"].detail["start"], loc["diameter"].detail["end"]
    length = math.dist(start, end)
    direction = tuple((e - s) / length for s, e in zip(start, end))
    if abs(direction[2] - 1.0) > 1e-6:
        raise RuntimeError(f"the hole axis {direction} is not machine +Z")
    return {"origin": tuple(start), "dir": direction, "hole_d": loc["diameter"].measured}


def profile_points(p):
    """The closed (r, z) outline of the whole grommet, in the local XZ half-plane (x = r)."""
    r_fl, r_nk, r_gr = p["flange_d"] / 2, p["neck_d"] / 2, p["groove_d"] / 2
    r_co, r_bo = p["collar_d"] / 2, p["bore_d"] / 2
    z_bed, z_wall = -p["flange_t"], 0.0
    z_neck_end = p["neck_len"]
    z_groove_end = z_neck_end + p["groove_w"]
    z_flank_end = z_groove_end + (r_co - r_gr) * math.tan(math.radians(p["flank_deg"]))
    z_top = p["collar_top"]
    return [
        (r_bo + p["chamfer_out_radial"], z_bed),     # outside bore chamfer, bed end
        (r_fl, z_bed), (r_fl, z_wall),               # flange
        (r_nk, z_wall), (r_nk, z_neck_end),          # neck
        (r_gr, z_neck_end), (r_gr, z_groove_end),    # tie groove floor
        (r_co, z_flank_end),                         # 60° flank
        (r_co, z_top),                               # collar
        (r_bo + p["chamfer_in"], z_top),             # inside bore chamfer, 45°
        (r_bo, z_top - p["chamfer_in"]),
        (r_bo, z_bed + p["chamfer_out_axial"]),      # bore
    ]


def build_half(p, frame):
    pts = [(r, 0.0, z) for r, z in profile_points(p)]
    outline = bd.Polyline(*pts, close=True)
    section = bd.make_face(outline)
    whole_local = bd.revolve(section, Axis.Z, 360)            # seam in the +X half-plane (y 0)
    split_plane = Plane(origin=(0, p["split_y"], 0), z_dir=(0, 1, 0))
    half_local = bd.split(whole_local, bisect_by=split_plane, keep=Keep.TOP)   # keeps y ≥ split_y
    solids = half_local.solids()
    if len(solids) != 1:
        raise RuntimeError(f"the split gave {len(solids)} solids")
    half = solids[0].moved(Location(frame["origin"]))
    half.label = HALF_LABEL
    return half


def groove_of(half, p):
    """The groove floor's radius and its z span, measured on the built half."""
    near = [f for f in half.faces() if f.geom_type == GeomType.CYLINDER
            and abs(cylinder(f.wrapped)[2] - p["groove_d"] / 2) < 0.2]
    if len(near) != 1:
        raise RuntimeError(f"{len(near)} groove floor faces")
    box = near[0].bounding_box()
    return cylinder(near[0].wrapped)[2], box.min.Z, box.max.Z


def build_assembly(half, p, frame, c11, c01):
    ox, oy, _ = frame["origin"]
    axis = Axis(frame["origin"], frame["dir"])
    upper = copy.deepcopy(half)                          # own shapes, so each is its own product
    upper.label = "half_upper"
    lower = copy.deepcopy(half).rotate(axis, 180)
    lower.label = "half_lower"
    z0, z1 = p["cord_z"]
    cord = Pos(ox, oy, (z0 + z1) / 2) * Cylinder(p["cord_d"] / 2, z1 - z0)
    cord.label = "cord_envelope"
    r_in, g_lo, _ = groove_of(half, p)                  # joint: inner face on the groove floor,
    r_out = r_in + p["tie_band"]                         # outer side on the neck-side face
    tie = Pos(ox, oy, g_lo + p["tie_w"] / 2) * (Cylinder(r_out, p["tie_w"]) - Cylinder(r_in, p["tie_w"]))
    tie = tie.solids()[0]
    tie.label = "tie_envelope"
    head = Pos(ox, oy + r_out + p["head_y"] / 2, g_lo + p["head_z"] / 2) * Box(p["head_x"], p["head_y"], p["head_z"])
    head.label = "tie_head_box"
    panel = c11.moved(Location())
    panel.label = "od_c11_back_panel"
    frame_part = c01.moved(Location())
    frame_part.label = "od_c01_base_frame"
    parts = [panel, frame_part, upper, lower, cord, tie, head]
    return Compound(label="od_c14_assembly", children=parts)


def export(p, half_step, stl, asm_step, frame, c11, c01):
    half = build_half(p, frame)
    w_step = write_step(half, half_step, timestamp=TIMESTAMP)
    w_stl = write_stl(half, stl, tolerance=p["stl_tol"], angular_tolerance=p["stl_ang"])
    asm = build_assembly(build_half(p, frame), p, frame, c11, c01)
    w_asm = write_step(asm, asm_step, timestamp=TIMESTAMP)
    return {"half_step": [str(w_step.path.relative_to(WS)), w_step.sha256],
            "stl": [str(w_stl.path.relative_to(WS)), w_stl.sha256, w_stl.detail],
            "asm_step": [str(w_asm.path.relative_to(WS)), w_asm.sha256],
            "volume_mm3": half.volume}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sweep", action="store_true")
    args = ap.parse_args()
    c11 = read_step(WS / "00_Spec/inputs/OD-C11_back_panel.step")
    c01 = read_step(WS / "00_Spec/inputs/OD-C01_base_frame.step")
    frame = hole_frame(c11)
    if not args.sweep:
        out = export(PARAMS, WS / "02_STEP_STL/od_c14_grommet_half_C1_v01.step",
                     WS / "02_STEP_STL/od_c14_grommet_half_C1_v01.stl",
                     WS / "02_STEP_STL/od_c14_assembly_C1_v01.step", frame, c11, c01)
        out["frame"] = frame
        print(json.dumps(out, indent=1, default=str))
        return
    runs = {"nominal": dict(PARAMS)}
    for name, delta in FIT_CRITICAL.items():
        for tag, sign in (("low", -1), ("high", 1)):
            q = dict(PARAMS)
            q[name] = round(PARAMS[name] + sign * delta, 6)
            runs[f"{name}_{tag}"] = q
    log = {}
    for run, q in runs.items():
        folder = HERE / "sweep_v01" / run
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "params.json").write_text(json.dumps(q, indent=1) + "\n")
        try:
            log[run] = export(q, folder / "od_c14_grommet_half.step", folder / "od_c14_grommet_half.stl",
                              folder / "od_c14_assembly.step", frame, c11, c01)
        except Exception as exc:                          # noqa: BLE001: a failed build is a result
            log[run] = {"error": f"{type(exc).__name__}: {exc}"}
        print(run, log[run].get("error", "built"), flush=True)
    (HERE / "sweep_v01" / "build_log.json").write_text(json.dumps(log, indent=1, default=str) + "\n")


if __name__ == "__main__":
    sys.exit(main())
