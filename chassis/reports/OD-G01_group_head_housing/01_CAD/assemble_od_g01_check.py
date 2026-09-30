"""The joints of DESIGN_SPEC 1.1 §5 / WP-03 §"Plan amendments": OD-G04 seated and
OD-G10 at the locked and insertion poses, plus the feature pieces U-03(a) gates.

Every frame comes from a measured feature of the part itself (its own faces and its
own tab / ear angles), never from a bounding box (L-02):

- OD-G04's frame: z = 0 on its plate back face, material in -Z, +X through tab 1,
  whose centre its own report measures at -3.3 deg. The joint is a rotation about Z
  of +6.05 deg (tab 1 centre onto pocket 1's sector centre 2.75 deg) and a
  translation that puts its flange bottom face (its z -13.12) on the housing floor
  z -19.94, so its plate back face lands at housing z -6.82.
- OD-G10's frame: z = 0 on its cup rim end face, +Z out of the cup opening, +X
  toward the handle, ears centred 59.5 / 180 / 300.5 deg from the handle. The joint
  turns it 180 deg about +X (its +Z onto the housing -Z, so the rim leads into the
  bore), then about Z by the clock, then puts the rim face at the pose's z.

A feature piece is the placed part intersected with a region of space, so every
face of the piece is a face of the part except the region's own boundary, which is
kept away from the housing; each clearance reports its nearest points so the
REPORT can show which face it lies on.
"""
from __future__ import annotations

import math
from pathlib import Path

from build123d import Compound, Cylinder, Pos, Rot

from tools.core import read_step, write_step

WORKSPACE = Path(__file__).resolve().parents[1]
INPUTS = WORKSPACE / "00_Spec" / "inputs"

G04_STEP = INPUTS / "OD-G04_brewing_gasket_support.step"
G10_STEP = INPUTS / "OD-G10_portafilter.step"

G04_CLOCK_DEG = 6.05           # spec 1.1 §5 joint (A-12): tab 1 (-3.3) onto pocket 1 (2.75)
G04_BACK_FACE_Z = -6.82        # its z = 0 lands here: flange bottom (-13.12) on the floor (-19.94)
G04_TAB_PHASE_DEG = -3.3       # tab 1 centre in its own frame (its report, measured)
G04_TAB_PITCH_DEG = 120.0
G04_TAB_SPAN_DEG = 61.08
G04_PAIR_A_THETA = (-6.55, 172.95)     # its own frame
G04_PAIR_A_R = 15.5
G04_PAIR_B_THETA = (113.27, -62.02)
G04_PAIR_B_R = 19.03

G10_EAR_THETA = (59.5, 180.0, 300.5)   # its own frame, from the handle
G10_LOCK_CLOCK_DEG = 60.26             # §5 joint
G10_LOCK_RIM_Z = -11.20
G10_INSERT_CLOCK_DEG = 122.5


def place_g04(shape):
    """OD-G04 at its seated pose."""
    return Pos(0, 0, G04_BACK_FACE_Z) * Rot(Z=G04_CLOCK_DEG) * shape


def place_g10(shape, clock_deg: float, rim_z: float):
    """OD-G10 with its rim face at rim_z and its ears at (clock - ear angle)."""
    return Pos(0, 0, rim_z) * Rot(Z=clock_deg) * Rot(X=180) * shape


def g04_tab_centres() -> list[float]:
    return [(G04_TAB_PHASE_DEG + G04_CLOCK_DEG + G04_TAB_PITCH_DEG * k) % 360 for k in range(3)]


def g10_ear_centres(clock_deg: float) -> list[float]:
    return [(clock_deg - t) % 360 for t in G10_EAR_THETA]


def load_mates():
    return read_step(G04_STEP), read_step(G10_STEP)


def _tube(r_in: float, r_out: float, z_low: float, z_high: float, arc: float | None = None,
          start: float = 0.0):
    """A cylindrical region (optionally a sector) between two radii and two levels."""
    height = z_high - z_low
    if arc is None:
        region = Pos(0, 0, z_low + height / 2) * Cylinder(radius=r_out, height=height)
    else:                       # a sector keeps its apex on the axis: align=None
        region = (Pos(0, 0, z_low) * Rot(Z=start)
                  * Cylinder(radius=r_out, height=height, arc_size=arc, align=None))
    if r_in > 0:
        region = region - Pos(0, 0, z_low + height / 2) * Cylinder(radius=r_in, height=height * 1.5)
    return region


def _column(centre_r: float, centre_theta: float, radius: float, z_low: float, z_high: float):
    x, y = centre_r * math.cos(math.radians(centre_theta)), centre_r * math.sin(math.radians(centre_theta))
    return Pos(x, y, (z_low + z_high) / 2) * Cylinder(radius=radius, height=z_high - z_low)


def feature_pieces(g04_placed) -> dict:
    """The OD-G04 features §5 U-03(a) keeps clear of the housing, each cut out of the
    placed part by a region whose own boundary is well away from the housing."""
    pieces = {}
    for k, centre in enumerate(g04_tab_centres(), start=1):
        region = _tube(31.0, 40.0, -16.50, -13.50, arc=G04_TAB_SPAN_DEG,
                       start=centre - G04_TAB_SPAN_DEG / 2)
        pieces[f"tab{k}"] = g04_placed & region
    pieces["bead"] = g04_placed & _tube(30.9, 40.0, -16.20, -13.70)
    for k, theta in enumerate(G04_PAIR_A_THETA, start=1):
        pieces[f"pairA{k}"] = g04_placed & _column(G04_PAIR_A_R, theta + G04_CLOCK_DEG, 5.0,
                                                   -23.40, -19.95)
    for k, theta in enumerate(G04_PAIR_B_THETA, start=1):
        pieces[f"pairB{k}"] = g04_placed & _column(G04_PAIR_B_R, theta + G04_CLOCK_DEG, 5.0,
                                                   -23.40, -19.95)
    pieces["hub"] = g04_placed & _tube(0.0, 11.5, -23.40, -19.95)
    return pieces


def write_assembly(housing, g04_placed, g10_placed, path: Path, timestamp: str):
    """The check assembly: the housing with OD-G04 seated and OD-G10 at the locked pose."""
    housing.label = "od_g01_housing"
    g04_placed.label = "od_g04_brewing_gasket_support"
    g10_placed.label = "od_g10_portafilter"
    assembly = Compound(children=[housing, g04_placed, g10_placed])
    assembly.label = "od_g01_assembly_C1_v01"
    return write_step(assembly, path, timestamp=timestamp)
