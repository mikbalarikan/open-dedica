"""D2 probe 3: pad radial extents at the exact pad angles, and the clearance of the
trade-off geometry (standoff tips at z -10.0) and of candidate gussets. Primitives only."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
WS = HERE.parents[1]
from build123d import Cylinder, Box, Pos, Polyline, make_face, extrude, Plane, Vector
from tools.core import read_step
from tools.measure import clearance, radial_profile

tb = read_step(WS / "00_Spec/inputs/OD-H11_thermoblock.step")
out = {}
for ang in (262.5, 339.0):
    rp = radial_profile(tb, (0, 0, 0), (0, 0, 1), (1, 0, 0), [ang], (0.0, 47.64), margin=(0, 0), z_step=0.25)
    out[f"pad_{ang}"] = {k: {"mm": v.measured, "status": v.status, "at": v.at} for k, v in rp.items()}
    print(ang, out[f"pad_{ang}"], flush=True)
holes = {"S1": (-19.62, 20.18), "S2": (25.01, 9.08)}
def cyl(d, z0, z1, x, y):
    return Pos(x, y, (z0 + z1) / 2) * Cylinder(d / 2, z1 - z0)
cases = {"S1_standoff_tip-10": cyl(12, -12, -10, *holes["S1"]),
         "S2_standoff_tip-10": cyl(12, -12, -10, *holes["S2"]),
         "S2_spacer_-10_27.6": cyl(7, -10, 27.6, *holes["S2"]),
         "S1_spacer_-10_0": cyl(7, -10, 0, *holes["S1"])}
# candidate gusset: right triangle in the y-z plane, legs 30 along the plate face and the foot, 4 thick at x = +-46
for sx in (-1, 1):
    pts = [(-66.0, -12.0), (-36.0, -12.0), (-66.0, 18.0), (-66.0, -12.0)]
    tri = make_face(Polyline(*[(sx * 44.0, y, z) for y, z in pts]))
    cases[f"gusset_x{sx*46:+d}"] = extrude(tri, amount=4.0 * sx, dir=(1, 0, 0))
for k, s in cases.items():
    r = clearance(s, tb)
    out[k] = {"mm": r.measured, "at": r.at, "detail": r.detail}
    print(k, r.measured, r.at, r.detail, flush=True)
json.dump(out, open(HERE / "probe_odh11_options_v01.json", "w"), indent=1, default=str)
