"""OD-C13 right side panel, concept C1, spec 1.1 (D4). build123d Algebra mode, machine frame.

Features (plan section 3 as amended by spec 1.1): F01-F02 wall, F03 top rail, F04 lip wedge,
F05 merge coplanar faces, F06 three bracket holes. Every number comes from params_od_side_panels.

Run: build_od_c13_right.py [--params JSON] [--out-dir DIR] [--tag C1_v01]
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build123d import Box, Cylinder, Location, Plane, Polygon, extrude  # noqa: E402

from params_od_side_panels import P  # noqa: E402

WS = Path(__file__).resolve().parents[1]
PART = "od_c13_right"


def span_box(x0, x1, y0, y1, z0, z1):
    """A box given by its two corners (machine frame)."""
    x0, x1 = sorted((x0, x1))
    y0, y1 = sorted((y0, y1))
    z0, z1 = sorted((z0, z1))
    return Location(((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)) * Box(x1 - x0, y1 - y0, z1 - z0)


def build(p=P):
    # F01-F02 wall: x 117 .. 120, y 0 .. 215, square ends z -295 .. +90
    wall = span_box(p.wall_inner_x, p.wall_outer_x, p.wall_y0, p.wall_top_y, p.wall_z_rear, p.wall_z_front)
    # F03 top rail on the wall's inner face
    rail = span_box(p.rail_inner_x, p.wall_inner_x, p.rail_y0, p.wall_top_y, p.rail_z0, p.rail_z1)
    # F04 lip wedge: triangle (110, 215), (116.6, 215), (110, apex) in XY, extruded along +Z
    lip_section = Polygon((p.rail_inner_x, p.wall_top_y), (p.lip_outer_x, p.wall_top_y),
                          (p.rail_inner_x, p.lip_top_y), align=None)
    lip = extrude(Plane.XY.offset(p.lip_z0) * lip_section, amount=p.lip_z1 - p.lip_z0, dir=(0, 0, 1))
    # F05 one body, coplanar faces merged
    body = (wall + rail + lip).clean()
    # F06 three bracket holes along X through the wall (y 10, z_c), offset by the sweep's dy, dz
    hole_len = (p.wall_outer_x - p.wall_inner_x) + 2 * p.overrun
    hole_x = (p.wall_inner_x + p.wall_outer_x) / 2
    holes = [Location((hole_x, p.panel_hole_y + p.panel_hole_dy, z + p.panel_hole_dz), (0, 90, 0))
             * Cylinder(p.panel_hole_d / 2, hole_len) for z in p.hole_z]
    panel = body
    for h in holes:
        panel = panel - h
    panel = panel.solids()[0]
    panel.label = PART
    return panel


def r_max(shape):
    """The largest curved-face radius (U-07)."""
    return max(f.radius for f in shape.faces() if f.geom_type.name == "CYLINDER")


def export(shape, part, out_dir: Path, tag: str, p=P):
    """D5: AP242 through tools.core.write_step (with its round trip), STL afresh at the U-07 tolerances."""
    from tools.core import step_roundtrip, write_stl
    out_dir.mkdir(parents=True, exist_ok=True)
    step = out_dir / f"{part}_{tag}.step"
    stl = out_dir / f"{part}_{tag}.stl"
    rt = step_roundtrip(shape, step, timestamp=p.step_timestamp)
    ang = p.stl_angular(r_max(shape))
    w = write_stl(shape, stl, tolerance=p.stl_tol, angular_tolerance=ang)
    facts = {"step": step.name, "stl": stl.name, "roundtrip": {k: (r.measured, r.status) for k, r in rt.items()},
             "stl_tolerance_mm": p.stl_tol, "stl_angular_rad": ang, "r_max": r_max(shape),
             "triangles": w.detail["triangles"], "max_sagitta_mm": w.detail["max_sagitta_mm"],
             "volume_mm3": shape.volume}
    facts_dir = WS / "01_CAD" / "results_v01" if out_dir.resolve() == (WS / "02_STEP_STL").resolve() else out_dir
    facts_dir.mkdir(parents=True, exist_ok=True)
    (facts_dir / f"export_{part}_{tag}.json").write_text(json.dumps(facts, indent=1))
    print(json.dumps(facts))
    return facts


def cli(builder, part):
    ap = argparse.ArgumentParser()
    ap.add_argument("--params", default="{}")
    ap.add_argument("--out-dir", default=str(WS / "02_STEP_STL"))
    ap.add_argument("--tag", default="C1_v01")
    a = ap.parse_args()
    p = replace(P, **json.loads(a.params))
    export(builder(p), part, Path(a.out_dir), a.tag, p)


if __name__ == "__main__":
    cli(build, PART)
