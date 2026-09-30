"""The joints of DESIGN_SPEC 1.2 §5 (v02): OD-G04 seated, OD-G10 at the locked and
insertion poses, the lug and feature pieces the U-03(a) rows are measured on, and
the lock path U-03(b) sweeps.

Every frame comes from a measured feature of the part itself, never from a bounding
box (L-02):

- OD-G04's frame: z = 0 on its plate back face, material in -Z, +X through tab 1,
  whose centre its own report measures at -3.3 deg. The joint is a rotation about Z
  of +6.05 deg (tab 1 centre onto pocket 1's sector centre 2.75 deg) and a
  translation that puts its flange bottom face (its z -13.12) on the housing floor
  z -19.94, so its plate back face lands at housing z -6.82.
- OD-G10's frame: z = 0 on its cup rim end face, +Z out of the cup opening, +X
  toward the handle, ears centred 59.5 / 180 / 300.5 deg from the handle. The joint
  turns it 180 deg about +X (its +Z onto the housing -Z, so the rim leads into the
  bore), then about Z by the clock, then puts the rim face at the pose's z.

Unchanged from v01: the clocks (+6.05 deg, +60.26 deg, +122.5 deg), the OD-G04 seat
and the locked rim z -11.20. New in v02:

- `lug_pieces`: the housing cut into its three lug sectors, so the three ear-top
  contacts of spec 1.2 §5 U-03(a) are three located rows. The housing is cut, not
  OD-G10: the housing is a sound solid, and the cutting planes lie in the gaps
  where the housing's own material is the bore wall, more than 1 mm from OD-G10.
- `lock_path`: the assembly path of U-03(b) in three legs - insertion at the
  insertion clock, rotation at the rotation depth, then the seating rise onto the
  lug undersides - with the travel each pose still has to make, so the spec's
  "last 0.5 mm of approach" is a measured distance and not a guess.
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

G04_CLOCK_DEG = 6.05           # spec §5 joint (A-12): tab 1 (-3.3) onto pocket 1 (2.75)
G04_BACK_FACE_Z = -6.82        # its z = 0 lands here: flange bottom (-13.12) on the floor (-19.94)
G04_TAB_PHASE_DEG = -3.3       # tab 1 centre in its own frame (its report, measured)
G04_TAB_PITCH_DEG = 120.0
G04_TAB_SPAN_DEG = 61.08
G04_PAIR_A_THETA = (-6.55, 172.95)     # its own frame
G04_PAIR_A_R = 15.5
G04_PAIR_B_THETA = (113.27, -62.02)
G04_PAIR_B_R = 19.03

G10_EAR_THETA = (59.5, 180.0, 300.5)   # its own frame, from the handle (A-19)
G10_EAR_SPAN_DEG = 37.0                # A-19
G10_LOCK_CLOCK_DEG = 60.26             # §5 joint (A-14)
G10_LOCK_RIM_Z = -11.20                # §5 joint (A-14)
G10_INSERT_CLOCK_DEG = 122.5           # §5 joint, ears centred in the gaps
G10_START_RIM_Z = -5.0                 # REQ-10: the path starts here

# The rotation depth: the portafilter is pushed this far past the locked pose before
# it is turned. A derivation, stated here and in REPORT §8: 0.45 mm below the locked
# pose, which is (a) deeper than the housing's own first contact with the ear tops,
# so the ears turn clear of the lug undersides, and (b) inside the 0.5 mm of approach
# spec §5 U-03(b) exempts, so the seating leg is the exempt one.
G10_ROTATE_DROP = 0.45
G10_ROTATE_RIM_Z = G10_LOCK_RIM_Z - G10_ROTATE_DROP

# The radius at which the rotation's travel is measured: the lug inner radius, where
# the ear meets the stop block (measured on v01 at r 31.68).
PATH_REF_R = 31.68

LUG_STARTS = (336.0, 96.0, 216.0)
LUG_PIECE_START_OFF, LUG_PIECE_END_OFF = -1.0, 55.0   # the lug sector plus its two gap edges
LUG_PIECE_Z = (-13.5, 3.5)


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
    x = centre_r * math.cos(math.radians(centre_theta))
    y = centre_r * math.sin(math.radians(centre_theta))
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


def lug_pieces(housing) -> dict:
    """The housing cut into its three lug sectors, for the three located ear-top rows
    of U-03(a). Each region spans the lug and one degree of gap either side, so its
    two radial cut faces sit in the gaps, where the housing's own material starts at
    the bore wall r 37.10 - more than 1 mm outside OD-G10's largest radius (the ear
    OD 35.97), so a cut face can never be the nearest point."""
    out = {}
    span = LUG_PIECE_END_OFF - LUG_PIECE_START_OFF
    for k, start in enumerate(LUG_STARTS, start=1):
        region = _tube(0.0, 45.0, LUG_PIECE_Z[0], LUG_PIECE_Z[1], arc=span,
                       start=start + LUG_PIECE_START_OFF)
        out[f"lug{k}"] = housing & region
    return out


def lock_path(insert_steps: int = 22, rotate_steps: int = 14, seat_steps: int = 6) -> list[dict]:
    """The assembly path of U-03(b), L-09 and L-10, from first approach to the final
    pose, as a list of poses. Three legs, each swept in its own variable and every
    other variable held at the value the previous leg left:

      1. insertion: rim from -5.0 down to the rotation depth, at the insertion clock
         (the ears centred in the three gaps);
      2. rotation: clock from the insertion clock to the locked clock, at the
         rotation depth;
      3. seating: rim from the rotation depth up to the locked rim, at the locked
         clock - the gasket pushing the ear tops onto the lug undersides.

    Each pose carries `remaining`, the travel still to be made to the final pose in
    mm, rotation counted as arc length at PATH_REF_R: spec §5 U-03(b) asks for
    clearance >= 0.30 at every pose "except the last 0.5 mm of approach", where it
    asks for >= 0, and that exemption is read off this number.
    """
    arc_per_deg = math.radians(1.0) * PATH_REF_R
    rotate_arc = abs(G10_INSERT_CLOCK_DEG - G10_LOCK_CLOCK_DEG) * arc_per_deg
    seat_len = abs(G10_LOCK_RIM_Z - G10_ROTATE_RIM_Z)
    poses = []
    for i in range(insert_steps + 1):
        t = i / insert_steps
        rim = G10_START_RIM_Z + (G10_ROTATE_RIM_Z - G10_START_RIM_Z) * t
        poses.append({"leg": "insertion", "clock_deg": G10_INSERT_CLOCK_DEG, "rim_z": rim,
                      "remaining": abs(G10_ROTATE_RIM_Z - rim) + rotate_arc + seat_len})
    for i in range(1, rotate_steps + 1):
        t = i / rotate_steps
        clock = G10_INSERT_CLOCK_DEG + (G10_LOCK_CLOCK_DEG - G10_INSERT_CLOCK_DEG) * t
        poses.append({"leg": "rotation", "clock_deg": clock, "rim_z": G10_ROTATE_RIM_Z,
                      "remaining": abs(clock - G10_LOCK_CLOCK_DEG) * arc_per_deg + seat_len})
    for i in range(1, seat_steps + 1):
        t = i / seat_steps
        rim = G10_ROTATE_RIM_Z + (G10_LOCK_RIM_Z - G10_ROTATE_RIM_Z) * t
        poses.append({"leg": "seating", "clock_deg": G10_LOCK_CLOCK_DEG, "rim_z": rim,
                      "remaining": abs(G10_LOCK_RIM_Z - rim)})
    return poses


def write_assembly(housing, g04_placed, g10_placed, path: Path, timestamp: str, label: str):
    """The check assembly: the housing with OD-G04 seated and OD-G10 at the locked pose."""
    housing.label = "od_g01_housing"
    g04_placed.label = "od_g04_brewing_gasket_support"
    g10_placed.label = "od_g10_portafilter"
    assembly = Compound(children=[housing, g04_placed, g10_placed])
    assembly.label = label
    return write_step(assembly, path, timestamp=timestamp)
