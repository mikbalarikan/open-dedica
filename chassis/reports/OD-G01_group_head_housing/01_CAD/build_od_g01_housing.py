"""build_od_g01_housing.py - the OD-G01 printed group-head housing, concept C1 (D4).

One parametric build123d script in Algebra mode, one parameter structure at the
top and no number below it. Every face and edge is selected by type or by measured
position, never by index. The datum is DESIGN_SPEC §2's frame: Z is the cup axis,
+Z toward the mouth, z = 0 the plane of the lug top pads, theta counter-clockwise
about +Z from +X, lug 1 starting at 336 deg.

Feature order follows DESIGN_PLAN §3 with the WP-03 amendments (spec 1.1):

  F01 cup outer wall          F02 rear slab 100 x 100 x 5.00     F03 blank
  F04 main bore               F05 upper lip wall                 F06 lower lip wall
  F07 three tab pockets       F08 three lug blanks               F09 lug underside + stop
  F10 keyhole and rear counterbore                               F11 two pair-A lobes
  F12 two pair-B recesses     F13 two pair-B screw holes
  F14 four carrier bosses     F15 four carrier insert bores
  F16 boss root fillets       F17 shelf fillets                  F18 lug root fillets
  F19 name the body

Run: uv run tools/run.py python 01_CAD/build_od_g01_housing.py
It writes the STEP and the STL, re-imports them, runs every check of
check_od_g01_housing.py, writes the check assembly STEP and the D6 sections, and
leaves 01_CAD/measured_v01.json with every gate row and its measurement.
"""
from __future__ import annotations

import json
import math
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path

from build123d import (Cylinder, Plane, Pos, Rectangle, RectangleRounded, Rot, extrude, loft)

from tools.core import fillet_ladder, read_step, write_step, write_stl

WORKSPACE = Path(__file__).resolve().parents[1]
OUT = WORKSPACE / "02_STEP_STL"
SECTIONS = WORKSPACE / "03_Sections"
VERSION = 1
TIMESTAMP = "2026-09-30T00:00:00"
PART_NAME = "od_g01_housing"
STEP_PATH = OUT / f"{PART_NAME}_C1_v{VERSION:02d}.step"
STL_PATH = OUT / f"{PART_NAME}_C1_v{VERSION:02d}.stl"
ASSEMBLY_PATH = OUT / f"od_g01_assembly_C1_v{VERSION:02d}.step"


@dataclass(frozen=True)
class Params:
    """Every number of the part. Source per row: DESIGN_PLAN §4 with the WP-03
    amendments; a row marked (derivation) is a design choice stated there."""
    # cup body -------------------------------------------------------------
    wall_r_out: float = 43.10        # §4 C1 outer Ø86.2
    front_z: float = 3.30            # §4 C1 flat front face
    bore_r: float = 37.10            # §4 C1 Ø74.20 straight, A-03
    # lugs -----------------------------------------------------------------
    lug_starts: tuple = (336.0, 96.0, 216.0)      # §2, A-04
    lug_span: float = 54.0                        # A-04
    lug_inner_r: float = 31.68                    # A-02
    lug_top_z: float = 0.0                        # the datum plane
    lug_outer_r: float = 38.50       # (derivation) past the bore, into the wall, so the
                                     # union leaves no sliver at r = bore_r
    stop_end_off: float = 5.76                    # A-06
    stop_bottom_z: float = -10.52                 # A-06
    # the lug underside, (angle from the lug start, z): A-05 gives +7, +41.8 and +54;
    # the knots at +50 and +53 are a derivation, the only shape that meets REQ-03
    # (material at z -3.0 at start + 53) and REQ-04 (no material at z -3.2 at
    # start + 50) together with A-05's three points.
    under_knots: tuple = ((5.76, -6.605), (7.0, -6.57), (41.8, -5.59),
                          (50.0, -3.10), (53.0, -3.10), (54.0, -1.15), (56.0, -0.42))
    under_cut_floor_z: float = -13.50             # (derivation) above the shelf
    under_cut_r: tuple = (25.0, 45.0)             # (derivation) the loft's radial span
    # shelf, pockets and lip ring -------------------------------------------
    shelf_z: float = -14.10                       # §4 C1, A-07
    pocket_floor_z: float = -17.30                # §4 C1, A-08
    pocket_riser_r: float = 35.10    # (derivation) OD-G04's tab tip measures 34.5191 on
                                     # the placed solid; 35.10 keeps U-03's 0.5 clearance,
                                     # which §4 C1's 35.00 misses by 0.019
    pocket_start_off: float = -5.0                # A-08
    pocket_end_off: float = 58.5                  # A-08
    lip_upper_r: float = 31.70                    # A-09, the bead + 0.5
    lip_lower_r: float = 31.30                    # A-09, the flange + 0.5
    lip_step_z: float = -17.70                    # A-09
    floor_z: float = -19.94                       # A-09, A-10
    # rear slab -------------------------------------------------------------
    plate_t: float = 5.00                         # §4 C1 (amended), A-10
    flange_side: float = 100.0                    # §4 C1, A-18
    flange_corner_r: float = 8.0                  # §4 C1
    keyhole_d: float = 26.0                       # REQ-06, A-10, A-11
    counterbore_d: float = 34.0                   # REQ-13, A-24
    counterbore_depth: float = 2.50               # REQ-13, REQ-11
    lobe_d: float = 9.0                           # REQ-13, A-11
    lobe_r: float = 15.5                          # REQ-13, A-11
    lobe_theta: tuple = (359.5, 179.0)            # REQ-13, A-11
    pair_b_r: float = 19.03                       # REQ-07, A-12
    pair_b_theta: tuple = (119.3, 304.0)          # REQ-07, A-12
    recess_d: float = 9.0                         # REQ-07
    recess_depth: float = 2.30                    # REQ-07
    screw_d: float = 3.8                          # REQ-07, D-04a, A-26
    # carrier inserts --------------------------------------------------------
    carrier_xy: float = 44.0                      # REQ-08, A-18
    insert_d: float = 4.00                        # D-05b, A-17
    insert_depth: float = 5.70                    # D-05b, A-17
    boss_od: float = 10.30           # (derivation) J-05 wants 3.0 of wall around a Ø4.0
                                     # hole, so 10.0 across; 10.30 keeps margin and still
                                     # sits inside the R 8 flange corner (5.172 from the
                                     # insert axis)
    # fillets ----------------------------------------------------------------
    boss_fillet: tuple = (1.0, 0.8, 0.6, 0.4)     # E-06
    shelf_fillet: tuple = (0.8, 0.6, 0.4)         # capped so the round stays below REQ-02's z -13.0
    lug_fillet: tuple = (0.6, 0.5, 0.4, 0.3)           # capped so it stays clear of REQ-03's start - 1
    # export ------------------------------------------------------------------
    stl_spec_tol: float = 0.01       # U-07's stated tolerance: the sagitta limit and the
                                     # angular cap are read from it
    stl_tol: float = 0.002           # (derivation) what the mesher is given: asked for 0.01 it
                                     # meets 0.0431 on the lug underside faces, over U-07's
                                     # sagitta limit; 0.002 measures 0.0094
    density: float = 1070.0                       # A-15, mass reported only

    @property
    def plate_back_z(self) -> float:
        return self.floor_z - self.plate_t

    @property
    def keyhole_bottom_z(self) -> float:
        return self.plate_back_z + self.counterbore_depth

    @property
    def boss_rise(self) -> float:
        return self.insert_depth - self.plate_t

    @property
    def stl_angular_tol(self) -> float:
        return 4 * math.acos(1 - self.stl_spec_tol / self.wall_r_out)

    @property
    def insert_centres(self) -> list:
        return [(sx * self.carrier_xy, sy * self.carrier_xy) for sx in (1, -1) for sy in (1, -1)]


P = Params()


# ------------------------------------------------------------------ helpers
def polar(r: float, theta_deg: float) -> tuple:
    return (r * math.cos(math.radians(theta_deg)), r * math.sin(math.radians(theta_deg)))


def disc(radius: float, z_low: float, z_high: float):
    """A cylinder between two levels, on the axis."""
    return Pos(0, 0, (z_low + z_high) / 2) * Cylinder(radius=radius, height=z_high - z_low)


def sector(radius: float, z_low: float, z_high: float, start_deg: float, span_deg: float):
    """A pie sector between two levels, its apex on the axis, from start to start + span."""
    pie = Cylinder(radius=radius, height=z_high - z_low, arc_size=span_deg, align=None)
    solid = Pos(0, 0, z_low) * Rot(Z=start_deg) * pie
    box = solid.bounding_box()
    assert abs(box.min.Z - z_low) < 1e-9 and abs(box.max.Z - z_high) < 1e-9, "sector z placement"
    return solid


def column(x: float, y: float, diameter: float, z_low: float, z_high: float):
    return Pos(x, y, (z_low + z_high) / 2) * Cylinder(radius=diameter / 2, height=z_high - z_low)


def radial_section(theta_deg: float, z_low: float, z_high: float, r_in: float, r_out: float):
    """A planar rectangle in the radial plane at theta, spanning r_in..r_out and z_low..z_high."""
    c, s = math.cos(math.radians(theta_deg)), math.sin(math.radians(theta_deg))
    plane = Plane(origin=(0, 0, 0), x_dir=(c, s, 0), z_dir=(s, -c, 0))
    return plane * Pos((r_in + r_out) / 2, (z_low + z_high) / 2) * Rectangle(r_out - r_in,
                                                                            z_high - z_low)


def edge_radii(edge, n: int = 9) -> list:
    return [math.hypot(*(edge @ (i / n)).to_tuple()[:2]) for i in range(n + 1)]


def edge_levels(edge, n: int = 9) -> list:
    return [(edge @ (i / n)).Z for i in range(n + 1)]


def flat_at(edge, z: float, tol: float = 1e-6) -> bool:
    return all(abs(v - z) <= tol for v in edge_levels(edge))


def at_radius(edge, radius: float, tol: float = 1e-6) -> bool:
    return all(abs(v - radius) <= tol for v in edge_radii(edge))


def ladder_on_copy(shape, select, radii):
    """Run a fillet ladder on a copy of the shape: OCCT's fillet builder edits the
    shape it is given even when it fails (measured here: after a failed rung the
    original classifies a point in its own cavity as ON a face), so a ladder that
    finds no radius must leave the part it was handed untouched."""
    trial = deepcopy(shape)
    edges = select(trial)
    if not edges:
        return shape, {"edges": 0, "radius": None, "tried": [], "note": "no edge selected"}
    done = fillet_ladder(trial, edges, radii)
    record = {"edges": len(edges), "radius": done.radius, "tried": [list(t) for t in done.tried]}
    return (shape if done.radius is None else done.shape), record


def edge_theta(edge, n: int = 4, tol: float = 1e-6):
    """The angle of an edge that lies in one radial plane, else None."""
    angles = [math.degrees(math.atan2((edge @ (i / n)).Y, (edge @ (i / n)).X)) % 360
              for i in range(n + 1)]
    return angles[0] if max(angles) - min(angles) <= tol else None


def same_angle(a: float, b: float, tol: float = 1e-6) -> bool:
    return abs((a - b + 180.0) % 360.0 - 180.0) <= tol


# ------------------------------------------------------------------ the build
def build(p: Params = P) -> dict:
    record = {"fillets": {}, "params": {k: getattr(p, k) for k in p.__dataclass_fields__}}

    f01_wall = disc(p.wall_r_out, p.floor_z, p.front_z)
    f02_slab = Pos(0, 0, p.plate_back_z) * extrude(
        RectangleRounded(p.flange_side, p.flange_side, p.flange_corner_r), amount=p.plate_t)
    f03_blank = f01_wall + f02_slab

    f04_bore = f03_blank - disc(p.bore_r, p.shelf_z, p.front_z)
    f05_lip_upper = f04_bore - disc(p.lip_upper_r, p.lip_step_z, p.shelf_z)
    f06_lip_lower = f05_lip_upper - disc(p.lip_lower_r, p.floor_z, p.lip_step_z)

    f07_pockets = f06_lip_lower
    for start in p.lug_starts:
        f07_pockets = f07_pockets - sector(p.pocket_riser_r, p.pocket_floor_z, p.shelf_z,
                                           start + p.pocket_start_off,
                                           p.pocket_end_off - p.pocket_start_off)

    f08_lugs = f07_pockets
    for start in p.lug_starts:
        blank = sector(p.lug_outer_r, p.stop_bottom_z, p.lug_top_z, start, p.lug_span)
        f08_lugs = f08_lugs + (blank - disc(p.lug_inner_r, p.stop_bottom_z - 1.0, p.lug_top_z + 1.0))

    f09_under = f08_lugs
    for start in p.lug_starts:
        sections = [radial_section(start + off, p.under_cut_floor_z, level,
                                   p.under_cut_r[0], p.under_cut_r[1])
                    for off, level in p.under_knots]
        cut = loft(sections, ruled=True) & disc(p.bore_r, p.under_cut_floor_z, p.lug_top_z + 1.0)
        f09_under = f09_under - cut

    f10_keyhole = f09_under - disc(p.keyhole_d / 2, p.keyhole_bottom_z, p.floor_z)
    if p.counterbore_depth > 0:
        f10_keyhole = f10_keyhole - disc(p.counterbore_d / 2, p.plate_back_z, p.keyhole_bottom_z)

    f11_lobes = f10_keyhole
    for theta in p.lobe_theta:
        x, y = polar(p.lobe_r, theta)
        f11_lobes = f11_lobes - column(x, y, p.lobe_d, p.plate_back_z, p.floor_z)

    f12_recesses, f13_screws = f11_lobes, None
    for theta in p.pair_b_theta:
        x, y = polar(p.pair_b_r, theta)
        f12_recesses = f12_recesses - column(x, y, p.recess_d,
                                             p.floor_z - p.recess_depth, p.floor_z)
    f13_screws = f12_recesses
    for theta in p.pair_b_theta:
        x, y = polar(p.pair_b_r, theta)
        f13_screws = f13_screws - column(x, y, p.screw_d, p.plate_back_z,
                                         p.floor_z - p.recess_depth)

    f14_bosses = f13_screws
    if p.boss_rise > 0:          # a slab thicker than the insert needs no boss
        for x, y in p.insert_centres:
            f14_bosses = f14_bosses + column(x, y, p.boss_od, p.floor_z, p.floor_z + p.boss_rise)
    f15_inserts = f14_bosses
    for x, y in p.insert_centres:
        f15_inserts = f15_inserts - column(x, y, p.insert_d, p.plate_back_z,
                                           p.plate_back_z + p.insert_depth)

    # F16: the boss roots, selected as the circles of the boss OD lying in the floor plane
    def boss_roots(shape):
        return [e for e in shape.edges()
                if flat_at(e, p.floor_z) and any(
                    all(abs(math.hypot(px - x, py - y) - p.boss_od / 2) < 1e-6
                        for px, py in [tuple(e @ (i / 6))[:2] for i in range(7)])
                    for x, y in p.insert_centres)]

    f16, record["fillets"]["boss_roots"] = ladder_on_copy(f15_inserts, boss_roots, p.boss_fillet)

    # F17: the concave shelf-to-bore edges, in the shelf plane at the bore radius
    def shelf_edges(shape):
        return [e for e in shape.edges() if flat_at(e, p.shelf_z) and at_radius(e, p.bore_r)]

    f17, record["fillets"]["shelf_to_bore"] = ladder_on_copy(f16, shelf_edges, p.shelf_fillet)

    # F18: the lug root edges: the vertical lines where a lug side face meets the bore
    # wall, at the lug's own start and end angles
    def lug_roots(shape):
        sides = [a % 360 for start in p.lug_starts for a in (start, start + p.lug_span)]
        found = []
        for e in shape.edges():
            theta = edge_theta(e)
            if theta is None or not at_radius(e, p.bore_r):
                continue
            levels = edge_levels(e)
            if not (max(levels) <= p.lug_top_z + 1e-6 and min(levels) >= p.stop_bottom_z - 1e-6
                    and max(levels) - min(levels) > 1e-6):
                continue
            if any(same_angle(theta, a) for a in sides):
                found.append(e)
        return found

    f18, record["fillets"]["lug_roots"] = ladder_on_copy(f17, lug_roots, p.lug_fillet)

    part = f18
    part.label = PART_NAME
    record["volume_mm3"] = part.volume
    return {"part": part, "record": record}


def main():
    from assemble_od_g01_check import load_mates, place_g04, place_g10, write_assembly
    from assemble_od_g01_check import G10_LOCK_CLOCK_DEG, G10_LOCK_RIM_Z
    import check_od_g01_housing as check

    built = build(P)
    part, record = built["part"], built["record"]
    OUT.mkdir(parents=True, exist_ok=True)

    step = write_step(part, STEP_PATH, timestamp=TIMESTAMP)
    stl = write_stl(part, STL_PATH, tolerance=P.stl_tol, angular_tolerance=P.stl_angular_tol)
    record["step"] = {"path": str(STEP_PATH.relative_to(WORKSPACE)), "sha256": step.sha256}
    record["stl"] = {"path": str(STL_PATH.relative_to(WORKSPACE)), "sha256": stl.sha256,
                     **stl.detail}

    out = check.run(STEP_PATH, built=part, stl_written=stl, assembly=True, heavy=True)
    out["build"] = record

    g04, g10 = load_mates()
    assembly = write_assembly(read_step(STEP_PATH), place_g04(g04),
                              place_g10(g10, G10_LOCK_CLOCK_DEG, G10_LOCK_RIM_Z),
                              ASSEMBLY_PATH, TIMESTAMP)
    out["build"]["assembly"] = {"path": str(ASSEMBLY_PATH.relative_to(WORKSPACE)),
                                "sha256": assembly.sha256}

    (WORKSPACE / "01_CAD" / f"measured_v{VERSION:02d}.json").write_text(
        json.dumps(out, indent=1, default=str), encoding="utf-8")
    for row in out["gates"]:
        print(f"{row['status']:12} {row['gate']:34} {row['measured']} {row['unit']}"
              f"  req {row['required']}  margin {row['margin']}")


if __name__ == "__main__":
    main()
