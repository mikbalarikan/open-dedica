"""Joints of the check assembly (spec 1.1 section 2; plan section 5). Job code.

Every placement is a rigid joint Location(Plane(origin, x_dir = image of local x, z_dir = image
of local z)); the local y image is z x x, checked right-handed below. No bounding box is used.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from build123d import Location, Plane

from params_od_side_panels import P
from tools.core import read_step

WS = Path(__file__).resolve().parents[1]
INP = WS / "00_Spec" / "inputs"
OUT = WS / "02_STEP_STL"

X, Y, Z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
NX, NY, NZ = (-1, 0, 0), (0, -1, 0), (0, 0, -1)

# label: (file, origin, x_dir, z_dir); None = identity (section 2)
REFERENCES = {
    "OD-C01": ("OD-C01_base_frame.step", None),
    "OD-C02": ("OD-C02_bulkhead.step", None),
    "OD-C05": ("OD-C05_group_head_carrier.step", ((0, 180.06, 32.0), X, NY)),      # x->X, y->+Z, z->-Y
    "OD-C07": ("OD-C07_valve_flowmeter_mount.step", ((-92, 0, -60), NZ, Y)),        # x->-Z, y->-X, z->+Y
    "OD-C08": ("OD-C08_electronics_bay_tray.step", None),
    "OD-C10": ("OD-C10_top_panel.step", None),
    "OD-C11": ("OD-C11_back_panel.step", None),
    "OD-C15-RF": ("OD-C15_foot.step", ((110, -6, 90), X, NY)),                     # x->X, y->+Z, z->-Y
    "OD-C15-LF": ("OD-C15_foot.step", ((-110, -6, 90), X, NY)),
    "OD-C15-RR": ("OD-C15_foot.step", ((110, -6, -295), X, NY)),
    "OD-C15-LR": ("OD-C15_foot.step", ((-110, -6, -295), X, NY)),
}


def bracket_poses(p=P):
    """Six poses: right x->X, z->Z at (117, 0, z_c); left 180 deg about Y, x->-X, z->-Z at (-117, 0, z_c)."""
    out = {}
    for i, zc in enumerate(p.hole_z, 1):
        out[f"od_c16_bracket_R{i}"] = ((p.bracket_origin_x, 0.0, zc), X, Z)
        out[f"od_c16_bracket_L{i}"] = ((-p.bracket_origin_x, 0.0, zc), NX, NZ)
    return out


def _right_handed(xd, zd):
    x, z = np.array(xd, float), np.array(zd, float)
    y = np.cross(z, x)
    return abs(np.dot(x, z)) < 1e-12 and np.allclose(np.cross(x, y), z)


def place(shape, pose):
    if pose is None:
        return shape
    origin, xd, zd = pose
    assert _right_handed(xd, zd), (xd, zd)
    return shape.moved(Location(Plane(origin=origin, x_dir=xd, z_dir=zd)))


def solid_of(shape):
    s = shape.solids()
    if len(s) != 1:
        raise ValueError(f"expected one solid, found {len(s)}")
    return s[0]


def references():
    cache, out = {}, {}
    for label, (fname, pose) in REFERENCES.items():
        if fname not in cache:
            cache[fname] = read_step(INP / fname)
        out[label] = [place(s, pose) for s in cache[fname].solids()]
    return out


def new_parts(p=P, step_dir=OUT, tag="C1_v01"):
    """The three part files, re-imported, placed: panels at identity, brackets at the six poses."""
    r = solid_of(read_step(step_dir / f"od_c13_right_{tag}.step"))
    l_ = solid_of(read_step(step_dir / f"od_c12_left_{tag}.step"))
    b = solid_of(read_step(step_dir / f"od_c16_bracket_{tag}.step"))
    out = {"od_c13_right": r, "od_c12_left": l_}
    for label, pose in bracket_poses(p).items():
        out[label] = place(b, pose)
    return out
