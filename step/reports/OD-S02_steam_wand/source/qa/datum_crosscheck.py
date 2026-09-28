#!/usr/bin/env python3
"""QA run-local cross-check (report-only): section-circle axis of the rod taper and the steel-tube
clock, fitted by QA on the raw scan (builder matrix used only to select regions / express results).
Not a skill script; written because datum_audit.py has no 'tube axis' clock type and its axis-primary
method is normals-eigen only (the intake used section circles)."""
import json, sys
import numpy as np, trimesh
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import header, write_json

m = trimesh.load_mesh("input/scan.stl", process=False); m.merge_vertices()
T = np.array(json.load(open("intake/alignment.json"))["matrix_4x4"])
m.apply_transform(T)  # builder datum frame (selection + expression only)
V = m.vertices
out = {}
# 1) section circles on the rod taper, stations every 1 mm z 30..62, Kasa + 3 sigma trim
cs = []
for z0 in np.arange(30, 62.01, 1.0):
    s = (np.abs(V[:, 2] - z0) < 0.2) & (np.hypot(V[:, 0], V[:, 1]) < 4.9) & (np.hypot(V[:, 0], V[:, 1]) > 3.0)
    Q = V[s, :2]
    if len(Q) < 50: continue
    for _ in range(3):
        A = np.c_[2 * Q, np.ones(len(Q))]; b = (Q ** 2).sum(1)
        sol = np.linalg.lstsq(A, b, rcond=None)[0]; c = sol[:2]; R = np.sqrt(sol[2] + c @ c)
        res = np.hypot(*(Q - c).T) - R
        keep = np.abs(res) < 3 * res.std() + 1e-9
        Q = Q[keep]
    cs.append([c[0], c[1], z0, R, float(res.std())])
cs = np.array(cs)
px = np.polyfit(cs[:, 2], cs[:, 0], 1); py = np.polyfit(cs[:, 2], cs[:, 1], 1)
tilt = np.degrees(np.arctan(np.hypot(px[0], py[0])))
out["rod_taper_section_axis"] = {"stations": int(len(cs)), "tilt_vs_datum_Z_deg": float(tilt),
    "tilt_dir_deg": float(np.degrees(np.arctan2(py[0], px[0]))),
    "axis_xy_at_z0_mm": [float(px[1]), float(py[1])], "offset_at_z0_mm": float(np.hypot(px[1], py[1])),
    "station_rms_median_mm": float(np.median(cs[:, 4]))}
# 2) tube clock: faces of the steel tube leaving the elbow, datum x 25..29 (steel, r~3.0, between the sealing band and the bend; located from QA x-slices)
C, N, Af = m.triangles_center, m.face_normals, m.area_faces
s = (C[:, 0] > 25) & (C[:, 0] < 29) & (C[:, 2] < -5) & (C[:, 2] > -25)
# refine: keep faces within 3.6 mm of a provisional line through the centroid along +x-ish
M = (N[s] * Af[s, None]).T @ N[s]; w, E = np.linalg.eigh(M); ax = E[:, 0]; ax = ax if ax[0] > 0 else -ax
cen = C[s].mean(0)
for _ in range(5):
    d = C - cen; along = d @ ax; perp = np.linalg.norm(d - np.outer(along, ax), axis=1)
    s2 = (np.abs(along) < 2) & (perp < 3.6) & (np.abs(N @ ax) < 0.3)
    M = (N[s2] * Af[s2, None]).T @ N[s2]; w, E = np.linalg.eigh(M); ax = E[:, 0]; ax = ax if ax[0] > 0 else -ax
    # centre: least squares circle in plane normal to ax
    u = np.cross(ax, [0, 0, 1.0]); u /= np.linalg.norm(u); v = np.cross(ax, u)
    Q = np.c_[(C[s2] - cen) @ u, (C[s2] - cen) @ v]
    A = np.c_[2 * Q, np.ones(len(Q))]; b = (Q ** 2).sum(1); sol = np.linalg.lstsq(A, b, rcond=None)[0]
    cen = cen + sol[0] * u + sol[1] * v
    R = float(np.sqrt(sol[2] + sol[:2] @ sol[:2]))
out["tube_clock"] = {"faces": int(s2.sum()), "azimuth_deg_in_datum": float(np.degrees(np.arctan2(ax[1], ax[0]))),
    "elevation_deg": float(np.degrees(np.arcsin(ax[2]))), "radius_mm": R, "point": cen.tolist(),
    "note": "builder rule: this azimuth -> 0 deg. A non-zero value is the clock disagreement (report-only)."}
write_json("qa/datum_crosscheck.json", {**header("datum_crosscheck", "qa/datum_crosscheck.py (run-local)", ["input/scan.stl", "intake/alignment.json"], None), **out})
print(json.dumps(out, indent=1))
