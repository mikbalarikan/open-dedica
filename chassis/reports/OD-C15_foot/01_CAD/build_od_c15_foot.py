"""od_c15_foot, concept C1 (job 20261001-od-c15-feet, spec 1.1): the printed TPU foot.

Algebra mode, one parameter structure, no numbers below it. Frame (spec §2): origin at
the centre of the top face (the face on the plate underside), on the screw axis; +Z away
from the plate and the print build direction; the foot occupies z 0 ... height; one pair
of hex flats parallel to X.

Usage (from the repository root, in the tools venv):
  python build_od_c15_foot.py --out-dir <dir> --tag v01 [--set name=value ...] [--no-stl]
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass, replace
from pathlib import Path

from build123d import (Align, Cylinder, GeomType, Plane, RegularPolygon, chamfer, extrude)

from tools.core import step_roundtrip, write_stl


@dataclass(frozen=True)
class Params:
    body_d: float = 18.0               # §4 Body, REQ-04; R9 = plate R10 corner arc - 1.0 (REQ-05)
    height: float = 10.0               # §4 Body, REQ-04, A-04
    top_chamfer_axial: float = 0.50    # §4 Body, REQ-04 (spec 1.1, Q1): bed edge, 60 deg from horizontal
    top_chamfer_radial: float = 0.29   # §4 Body, REQ-04, REQ-01 (annulus to Ø17.42)
    counter_chamfer: float = 1.0       # §4 Body, REQ-04: 1.0 x 45 deg at z = height
    lid_t: float = 2.5                 # §4 Lid, REQ-03: the nut seat height
    lid_hole_d: float = 3.4            # §4 Lid, REQ-02, D-04a
    pocket_af: float = 5.60            # §4 Nut pocket, REQ-03, A-06
    pocket_rot_deg: float = 0.0        # REQ-03: flats parallel to X (verified by measurement)
    mouth_chamfer: float = 0.5         # §4 Nut pocket, REQ-03
    overshoot: float = 1.0             # derivation: cutters run 1.0 past each face they open
    label: str = "od_c15_foot"
    timestamp: str = "2026-10-01T12:00:00"


EDGE_TOL = 1e-6   # position tolerance for selecting an edge or face by geometry


def _circle_edges_at(shape, z, r):
    return [e for e in shape.edges() if e.geom_type == GeomType.CIRCLE
            and abs(e.center().Z - z) < EDGE_TOL and abs(e.radius - r) < EDGE_TOL]


def _planar_face_at(shape, z):
    return [f for f in shape.faces() if f.geom_type == GeomType.PLANE
            and abs(f.center().Z - z) < EDGE_TOL and abs(abs(f.normal_at().Z) - 1) < EDGE_TOL]


def build_foot(p: Params):
    r = p.body_d / 2
    # F01 body
    body = Cylinder(r, p.height, align=(Align.CENTER, Align.CENTER, Align.MIN))
    # F02 bed-edge chamfer (z 0): radial leg on the top face, axial leg on the cylinder
    bed_edge = _circle_edges_at(body, 0.0, r)
    top_face = _planar_face_at(body, 0.0)
    body_f2 = chamfer(bed_edge, length=p.top_chamfer_radial, length2=p.top_chamfer_axial,
                      reference=top_face[0])
    # F03 counter-edge chamfer (z height)
    counter_edge = _circle_edges_at(body_f2, p.height, r)
    body_f3 = chamfer(counter_edge, length=p.counter_chamfer)
    # F04 lid hole, overshooting below z 0 and into the pocket void
    lid_cutter = Plane.XY.offset(-p.overshoot) * Cylinder(
        p.lid_hole_d / 2, p.lid_t + 2 * p.overshoot, align=(Align.CENTER, Align.CENTER, Align.MIN))
    body_f4 = body_f3 - lid_cutter
    # F05 hex pocket from the seat z lid_t through the counter face (overshoot)
    hexagon = RegularPolygon(radius=p.pocket_af / 2, side_count=6, major_radius=False,
                             rotation=p.pocket_rot_deg)
    pocket = extrude(Plane.XY.offset(p.lid_t) * hexagon, amount=p.height - p.lid_t + p.overshoot)
    body_f5 = body_f4 - pocket                      # F06 the seat results here
    # F07 pocket mouth chamfer: the six straight edges in the plane z = height inside the counter chamfer
    inner_limit = r - p.counter_chamfer
    mouth_edges = [e for e in body_f5.edges() if e.geom_type == GeomType.LINE
                   and all(abs(v.Z - p.height) < EDGE_TOL for v in e.vertices())
                   and all(math.hypot(v.X, v.Y) < inner_limit for v in e.vertices())]
    foot = chamfer(mouth_edges, length=p.mouth_chamfer)
    foot.label = p.label
    return foot


def export(p: Params, out_dir: Path, tag: str, stl: bool, cad_dir: Path, concept: str = "C1"):
    foot = build_foot(p)
    stem = f"{p.label}_{concept}_{tag}"
    step_path = out_dir / f"{stem}.step"
    rt = step_roundtrip(foot, step_path, timestamp=p.timestamp)
    log = {"params": asdict(p), "step": str(step_path.name),
           "roundtrip": {k: {"measured": v.measured, "status": v.status, "reason": v.reason} for k, v in rt.items()}}
    (cad_dir / f"{stem}.params.json").write_text(json.dumps(
        {k: v for k, v in asdict(p).items()}, indent=1))
    if stl:
        tol = 0.01
        angular = 0.18          # U-07: <= 4 acos(1 - 0.01 / 9.0) = 0.18858 rad
        foot_for_mesh = build_foot(p)
        w = write_stl(foot_for_mesh, out_dir / f"{stem}.stl", tolerance=tol, angular_tolerance=angular)
        meta = {"tolerance_mm": tol, "angular_tolerance_rad": angular, **w.detail}
        (cad_dir / f"{stem}.stlmeta.json").write_text(json.dumps(meta, indent=1, default=str))
        log["stl"] = meta
    (cad_dir / f"{stem}.build_log.json").write_text(json.dumps(log, indent=1, default=str))
    return log


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--cad-dir", default=str(Path(__file__).resolve().parent))
    ap.add_argument("--tag", required=True)
    ap.add_argument("--set", action="append", default=[])
    ap.add_argument("--no-stl", action="store_true")
    a = ap.parse_args(argv)
    p = Params()
    for item in a.set:
        k, v = item.split("=")
        p = replace(p, **{k: type(getattr(p, k))(v)})
    out, cad = Path(a.out_dir), Path(a.cad_dir)
    out.mkdir(parents=True, exist_ok=True)
    cad.mkdir(parents=True, exist_ok=True)
    log = export(p, out, a.tag, not a.no_stl, cad)
    print(json.dumps(log, indent=1, default=str))


if __name__ == "__main__":
    sys.exit(main())
