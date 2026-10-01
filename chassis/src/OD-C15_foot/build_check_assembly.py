"""Check assembly for od_c15_foot (job 20261001-od-c15-feet, spec 1.1 §2, U-03).

OD-C01 base frame (imported unchanged, its own frame = the machine frame) plus four feet,
four screw envelopes and four nut envelopes, each placed by build123d RigidJoints on
measured features: the plate's Ø3.4 hole axes (bore_census / locate_bore) at the plate
underside and top, the foot's lid-bore axis at its top face and at the nut seat. The one
rotation is spec §2's (foot x -> X, y -> +Z, z -> -Y: +90 deg about X), never a box fit.

Usage (from the repository root, in the tools venv):
  python build_check_assembly.py --plate <OD-C01.step> --foot <foot.step> --out <assembly.step>
         [--nut-s 5.5]
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from build123d import (Align, Compound, Cylinder, Location, Plane, Pos, RegularPolygon, RigidJoint,
                       Solid, extrude)

from tools.core import read_step, solids, write_step
from tools.measure import bore_census, locate_bore


@dataclass(frozen=True)
class AsmParams:
    hole_xz: tuple = ((110.0, 90.0), (-110.0, 90.0), (110.0, -295.0), (-110.0, -295.0))  # A-01, §2 poses
    plate_mid_y: float = -3.0          # a point between the plate faces, to find each hole (A-01)
    foot_bore_probe_z: float = 1.25    # a point inside the foot's lid bore (z 0 ... 2.5)
    joint_rot: tuple = (90.0, 0.0, 0.0)  # spec §2: foot x -> X, y -> +Z, z -> -Y
    head_d: float = 5.7                # U-03 screw envelope, A-02 (ISO 7380 M3)
    head_h: float = 1.65
    shank_d: float = 3.0
    screw_l: float = 12.0              # M3x12 from the plate top: tip at y -12.0 (REQ-07)
    nut_s: float = 5.5                 # U-03 nut envelope, A-02 (ISO 4032 M3)
    nut_m: float = 2.4
    nut_bore: float = 3.0
    timestamp: str = "2026-10-01T12:00:00"


def _single(shape):
    s = solids(shape)
    if len(s) != 1:
        raise ValueError(f"expected one solid, found {len(s)}")
    return Solid(s[0])


def screw_envelope(p: AsmParams):
    """Local frame: z along the screw from the plate top (z 0) toward the tip; head at z < 0."""
    head = Pos(0, 0, -p.head_h) * Cylinder(p.head_d / 2, p.head_h, align=(Align.CENTER, Align.CENTER, Align.MIN))
    shank = Cylinder(p.shank_d / 2, p.screw_l, align=(Align.CENTER, Align.CENTER, Align.MIN))
    return head + shank


def nut_envelope(p: AsmParams):
    """Local frame: top face (the face on the seat) at z 0, the nut toward +z; flats parallel to x."""
    hexa = extrude(RegularPolygon(radius=p.nut_s / 2, side_count=6, major_radius=False), amount=p.nut_m)
    bore = Plane.XY.offset(-1) * Cylinder(p.nut_bore / 2, p.nut_m + 2, align=(Align.CENTER, Align.CENTER, Align.MIN))
    return hexa - bore


def build(plate_path: Path, foot_path: Path, p: AsmParams):
    plate = _single(read_step(plate_path))
    plate.label = "plate"
    pcensus = bore_census(plate)
    foot_src = _single(read_step(foot_path))
    fb = locate_bore(bore_census(foot_src), (0.0, 0.0, p.foot_bore_probe_z), (0.0, 0.0, 1.0))
    ends = sorted([fb["diameter"].detail["start"], fb["diameter"].detail["end"]], key=lambda q: q[2])
    foot_top, foot_seat = ends[0], ends[1]       # top face point (z 0) and nut seat point (z 2.5)
    record = {"foot_top_point": foot_top, "foot_seat_point": foot_seat, "holes": []}
    feet, screws, nuts = [], [], []
    for i, (x, z) in enumerate(p.hole_xz, start=1):
        hole = locate_bore(pcensus, (x, p.plate_mid_y, z), (0.0, 1.0, 0.0))
        h_ends = sorted([hole["diameter"].detail["start"], hole["diameter"].detail["end"]], key=lambda q: q[1])
        under, top = h_ends[0], h_ends[1]
        record["holes"].append({"pose": i, "underside": under, "top": top,
                                "diameter": hole["diameter"].measured, "offset": hole["offset"].measured})
        RigidJoint(f"under_{i}", plate, Location(tuple(under), p.joint_rot))
        RigidJoint(f"top_{i}", plate, Location(tuple(top), p.joint_rot))
        foot = foot_src.moved(Location((0, 0, 0)))
        foot.label = f"foot_{i}"
        RigidJoint("top_face", foot, Location(tuple(foot_top)))
        RigidJoint("seat", foot, Location(tuple(foot_seat)))
        plate.joints[f"under_{i}"].connect_to(foot.joints["top_face"])
        screw = screw_envelope(p)
        screw.label = f"screw_{i}"
        RigidJoint("under_head", screw, Location((0, 0, 0)))
        plate.joints[f"top_{i}"].connect_to(screw.joints["under_head"])
        nut = nut_envelope(p)
        nut.label = f"nut_{i}"
        RigidJoint("top_face", nut, Location((0, 0, 0)))
        foot.joints["seat"].connect_to(nut.joints["top_face"])
        feet.append(foot)
        screws.append(screw)
        nuts.append(nut)
    return plate, feet, screws, nuts, record


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--plate", required=True)
    ap.add_argument("--foot", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--nut-s", type=float, default=AsmParams.nut_s)
    ap.add_argument("--log-dir", default=str(Path(__file__).resolve().parent))
    a = ap.parse_args(argv)
    p = AsmParams(nut_s=a.nut_s)
    plate, feet, screws, nuts, record = build(Path(a.plate), Path(a.foot), p)
    parts = [plate, *feet, *screws, *nuts]
    copies = []
    for s in parts:
        c = copy.deepcopy(_single(s))          # its own TShape, so each part keeps its own product and name
        c.label = s.label
        copies.append(c)
    asm = Compound(children=copies, label="od_c15_check_assembly")
    out = Path(a.out)
    w = write_step(asm, out, timestamp=p.timestamp)
    record.update({"params": asdict(p), "sha256": w.sha256, "file": out.name})
    (Path(a.log_dir) / f"{out.stem}.placement.json").write_text(json.dumps(record, indent=1, default=str))
    print(json.dumps(record, indent=1, default=str))


if __name__ == "__main__":
    sys.exit(main())
