"""D2 probe 6: where is OD-H11's body axis? Pin centres from a section at z 50.0, circle
fits of the body's outer and the central bore's inner outline from ray reads about a
trial centre, and the web hole."""
import math, json
import numpy as np
from pathlib import Path
HERE = Path(__file__).resolve().parent
WS = HERE.parents[1]
from build123d import Plane, Box, Pos
from tools.core import read_step
from tools.measure import radial_extent
tb = read_step(WS / "00_Spec/inputs/OD-H11_thermoblock.step")
out = {}
# pins: slice above the top face
sl = tb & (Pos(0, 0, 49.5) * Box(300, 300, 1.0))
pins = [tuple(round(c, 3) for c in s.center()) for s in sl.solids()]
out["pin_centres_z49_50"] = pins
print("pins", pins, flush=True)
if len(pins) == 3:
    P = np.array([p[:2] for p in pins])
    A = np.c_[2 * P, np.ones(3)]; b = (P ** 2).sum(1)
    cx, cy, c = np.linalg.solve(A, b); R = math.sqrt(c + cx * cx + cy * cy)
    out["pin_circle"] = (cx, cy, 2 * R); print("pin circle centre", cx, cy, "PCD", 2 * R, flush=True)
def fit(pts):
    P = np.array(pts); A = np.c_[2 * P, np.ones(len(P))]; b = (P ** 2).sum(1)
    (cx, cy, c), *_ = np.linalg.lstsq(A, b, rcond=None)
    R = math.sqrt(c + cx * cx + cy * cy)
    res = np.abs(np.hypot(P[:, 0] - cx, P[:, 1] - cy) - R)
    return cx, cy, R, float(res.max())
centre = (-8.33, -14.13)
for z in (20.0, 30.0):
    outer, inner = [], []
    for a in range(0, 360, 10):
        ro = radial_extent(tb, (centre[0], centre[1], 0), (0, 0, 1), (1, 0, 0), a, z, side="outer", r_max=36.0)
        ri = radial_extent(tb, (centre[0], centre[1], 0), (0, 0, 1), (1, 0, 0), a, z, side="inner", r_min=0.0)
        for lst, r in ((outer, ro), (inner, ri)):
            if r.status == "MEASURED" and r.measured is not None:
                lst.append((a, r.measured))
    out[f"outer_z{z}"] = outer; out[f"inner_z{z}"] = inner
    print("z", z, "outer", [(a, round(r, 2)) for a, r in outer], flush=True)
    print("z", z, "inner", [(a, round(r, 2)) for a, r in inner], flush=True)
    rad = lambda lst: [(centre[0] + r * math.cos(math.radians(a)), centre[1] + r * math.sin(math.radians(a))) for a, r in lst]
    body = [p for (a, r), p in zip(outer, rad(outer)) if 33.0 <= r <= 35.5]
    if len(body) >= 3:
        out[f"body_fit_z{z}"] = fit(body); print("body fit (cx, cy, R, max residual)", out[f"body_fit_z{z}"], len(body), flush=True)
json.dump(out, open(HERE / "probe_odh11_axis_v01.json", "w"), indent=1, default=str)
