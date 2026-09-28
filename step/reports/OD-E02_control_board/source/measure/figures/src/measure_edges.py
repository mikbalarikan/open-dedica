#!/usr/bin/env python3
"""measure_edges.py - OD-E02 edge-round radii, measured on the scan (run after make_params.py once).

Estimator: for a convex (or concave) edge between two measured faces meeting at interior angle
alpha, a round of radius r leaves the scan surface d = r * (1/sin(alpha/2) - 1) away from the sharp
corner; for 90 deg, r = d / 0.4142. The sharp corner points are computed from params.json (the two
faces are each measured independently), never from the CAD. d = median nearest-scan distance over the
sampled corner points (points whose nearest scan sample is > 3 mm away are unobserved and dropped).
Writes measure/figures/m_edges.json. Seed 0.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import trimesh
from scipy.spatial import cKDTree
from shapely.geometry import Polygon

RUN = Path.cwd()
P = {k: v["value"] for k, v in json.loads((RUN / "measure/params.json").read_text())["params"].items()}
m = trimesh.load(RUN / "intake/aligned_work.stl")
pts, _ = trimesh.sample.sample_surface(m, 1500000, seed=0)
tree = cKDTree(pts)
K90 = 1 / np.sin(np.radians(45)) - 1

BL, BR, TR, TL = (np.array(P[k]) for k in ("core_BL", "core_BR", "core_TR", "core_TL"))
bTL, bTR = np.array(P["bump_TL"]), np.array(P["bump_TR"])
yfoot = min(TL[1], TR[1]) - 3.0
ytop = lambda x: TL[1] + (TR[1] - TL[1]) * (x - TL[0]) / (TR[0] - TL[0])


def outline(Rm, Rb):
    main = Polygon([BL, BR, TR, TL]).buffer(Rm, 256)
    bump = Polygon([(bTL[0], yfoot), (bTR[0], yfoot), bTR, bTL]).buffer(Rb, 256)
    return main.union(bump)


def ring_points(poly, z, step=0.25, keep=None, inner=False):
    ring = poly.exterior
    n = int(ring.length / step)
    xy = np.array([ring.interpolate(i * step).coords[0] for i in range(n)])
    if keep is not None:
        xy = xy[keep(xy)]
    return np.c_[xy, np.full(len(xy), z)]


def est(corner_pts, k=K90):
    d, _ = tree.query(corner_pts)
    obs = d < 3.0
    dd = d[obs]
    return {"n": int(obs.sum()), "d_med": float(np.median(dd)), "d_p25_p75": np.percentile(dd, [25, 75]).tolist(),
            "r_est": float(np.median(dd) / k)}


# exclusion masks: hoop/boss x-ranges on the side walls, the tab leg
hx = [P[f"hoop_H{i}"][:2] for i in (1, 2, 3, 4)]
def not_hoops(xy):
    ok = np.ones(len(xy), bool)
    for a, b in hx:
        ok &= ~((xy[:, 0] > a - 1.0) & (xy[:, 0] < b + 1.0))
    return ok


out = {}
out["T0_bottom_edge"] = est(ring_points(outline(P["T0_R_main"], P["T0_R_bump"]), P["T0_bottom_z"]))
out["T2_bottom_edge"] = est(ring_points(outline(P["T2_R_main"], P["T2_R_bump"]), P["T2_bottom_z"],
                                        keep=lambda xy: xy[:, 1] > ytop(xy[:, 0]) - 6))
out["T3_bump_bottom_edge"] = est(ring_points(outline(P["T3_R_main"], P["T3_R_bump"]), P["T3_bottom_z"],
                                             keep=lambda xy: (xy[:, 1] > ytop(xy[:, 0]) + 3.0)))
yL, yR = P["band_top_y"]
xs = np.r_[np.linspace(-20, -10, 40), np.linspace(10, 20, 40)]
out["band_top_bottom_edge"] = est(np.c_[xs, yL + (yR - yL) * (xs + 16) / 32, np.full(len(xs), P["band_bottom_z"])])
# rim top edges (outer and inner), away from hoops, bosses and the tab leg
keep_rim = lambda xy: not_hoops(xy) & ~((np.abs(xy[:, 0]) < 17) & (xy[:, 1] < -14))
out["rim_top_outer_edge"] = est(ring_points(outline(P["rim_out_R_main"], P["rim_out_R_bump"]), P["rim_top_z"], keep=keep_rim))
out["rim_top_inner_edge"] = est(ring_points(outline(P["rim_in_R_main"], P["rim_in_R_bump"]), P["rim_top_z"], keep=keep_rim))
# caps
th = np.linspace(0, 2 * np.pi, 400, endpoint=False)
d = np.asarray(P["cap_B2_axis_dir"])
x0, y0 = P["cap_B2_axis_xy0"]
n = np.asarray(P["cap_B2_top_normal"])
zc = -P["cap_B2_top_offset"]  # approx plane z at the axis
c = np.array([x0 + d[0] / d[2] * zc, y0 + d[1] / d[2] * zc, zc])
ring = c + P["cap_B2_r"] * np.c_[np.cos(th), np.sin(th), np.zeros_like(th)]
ring[:, 2] = (P["cap_B2_top_offset"] - n[0] * ring[:, 0] - n[1] * ring[:, 1]) / n[2]
out["cap_B2_top_edge"] = est(ring)
for key in ("B1", "B3"):
    cx, cy, a, b, phi = P[f"cap_{key}_ellipse"]
    ph = np.radians(phi)
    ex = cx + a * np.cos(th) * np.cos(ph) - b * np.sin(th) * np.sin(ph)
    ey = cy + a * np.cos(th) * np.sin(ph) + b * np.sin(th) * np.cos(ph)
    nn = np.asarray(P[f"cap_{key}_top_normal"])
    ez = (P[f"cap_{key}_top_offset"] - nn[0] * ex - nn[1] * ey) / nn[2]
    out[f"cap_{key}_top_edge"] = est(np.c_[ex, ey, ez])
# shroud top edges and inner vertical corners
xo0, xo1, yo0, yo1 = P["shroud_outer"]
xi0, xi1, yi0, yi1 = P["shroud_inner"]
zs = P["shroud_top_z"]
box = lambda x0_, x1_, y0_, y1_: Polygon([(x0_, y0_), (x1_, y0_), (x1_, y1_), (x0_, y1_)])
out["shroud_top_outer_edge"] = est(ring_points(box(xo0, xo1, yo0, yo1).buffer(-P["shroud_outer_corner_r"]).buffer(P["shroud_outer_corner_r"], 64), zs))
out["shroud_top_inner_edge"] = est(ring_points(box(xi0, xi1, yi0, yi1), zs, keep=lambda xy: (np.abs(xy[:, 0] - xi0) > 1.5) & (np.abs(xy[:, 0] - xi1) > 1.5)))
zz = np.linspace(2.0, 8.5, 30)
cp = np.vstack([np.c_[np.full(30, x), np.full(30, y), zz] for x in (xi0, xi1) for y in (yi0, yi1)])
out["shroud_inner_vertical_corner"] = est(cp)
# tab end top edge: y = tab_end_y on the top plane
tp = P["tab_top_plane"]
xs = np.linspace(-12, 12, 60)
ye = P["tab_end_y"]
out["tab_end_top_edge"] = est(np.c_[xs, np.full(60, ye), (tp[3] - tp[0] * xs - tp[1] * ye) / tp[2]])
up = P["tab_under_plane"]
out["tab_end_under_edge"] = est(np.c_[xs, np.full(60, ye), (up[3] - up[0] * xs - up[1] * ye) / up[2]])

hdr = {"schema": "stl-re/measure_edges@1", "tool": "measure_edges.py", "seed": 0,
       "estimator": __doc__.strip().splitlines()[2:6]}
(RUN / "measure/figures/m_edges.json").write_text(json.dumps({**hdr, **out}, indent=1))
for k, v in out.items():
    print(f"{k:32s} n={v['n']:5d} d={v['d_med']:.3f} r_est={v['r_est']:.3f} (d IQR {v['d_p25_p75'][0]:.3f}..{v['d_p25_p75'][1]:.3f})")
