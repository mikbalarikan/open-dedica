#!/usr/bin/env python3
"""measure_all.py - OD-S03 steam knob: every scan measurement the model needs, in the frozen
datum frame (intake/alignment.json), with estimator + residual per value.

Usage: python3 measure_all.py <RUN>   ->  <RUN>/measure/figures/measurements.json

Frames:
  datum  : intake/aligned_work.stl as is (crown z=0, +Z to the sleeve, lever on +X).
  cap    : datum XY shifted to the cap-wall axis (axes.json cap_wall_cone cx, cy); Z-parallel.
  collar : datum XY shifted to the collar axis (axes.json collar).
  stem   : datum XY shifted to the tilted stem-group line (axis_stations.json stem_group_line).
All angles theta CCW about +Z from datum +X. Deterministic (no randomness).
"""
from __future__ import annotations

import json
import sys

import numpy as np
import trimesh
from scipy.optimize import least_squares

RUN = sys.argv[1]
FIG = f"{RUN}/measure/figures"
m = trimesh.load(f"{RUN}/intake/aligned_work.stl")
C0, N, A = m.triangles_center.copy(), m.face_normals, m.area_faces
AX = json.load(open(f"{FIG}/axes.json"))
LS = json.load(open(f"{FIG}/axis_stations.json"))["stem_group_line"]
out: dict = {}


def rec(name, value, estimator, **kw):
    out[name] = {"value": value, "estimator": estimator, **kw}
    v = value if not isinstance(value, float) else round(value, 4)
    print(f"{name:28s} {v}  | {estimator[:90]}  {({k: (round(x, 4) if isinstance(x, float) else x) for k, x in kw.items()})}")


def frame(name):
    C = C0.copy()
    if name == "cap":
        C[:, 0] -= AX["cap_wall_cone"]["cx"]; C[:, 1] -= AX["cap_wall_cone"]["cy"]
    elif name == "collar":
        C[:, 0] -= AX["collar"]["cx"]; C[:, 1] -= AX["collar"]["cy"]
    elif name == "stem":
        C[:, 0] -= LS["x0"] + LS["dxdz"] * C[:, 2]; C[:, 1] -= LS["y0"] + LS["dydz"] * C[:, 2]
    r = np.hypot(C[:, 0], C[:, 1]); th = np.degrees(np.arctan2(C[:, 1], C[:, 0]))
    return C, r, th


def angwin(th, lo, hi):
    return (th > lo) & (th < hi)


def circ_rz(r, z, w=None, q0=None):
    """robust circle fit in the (r,z) plane"""
    w = np.ones_like(r) if w is None else w
    f = lambda q: (np.hypot(r - q[0], z - q[1]) - q[2]) * w
    q0 = q0 or [r.mean(), z.mean(), 1.0]
    s = least_squares(f, q0, loss="soft_l1", f_scale=0.03); res = s.fun / w
    return s.x, float(np.sqrt(np.mean(res ** 2))), float(np.percentile(np.abs(res), 95)), int(len(r))


def line_fit(x, y):
    X = np.c_[np.ones_like(x), x]; b = np.linalg.lstsq(X, y, rcond=None)[0]; res = y - X @ b
    return b, float(res.std()), int(len(x))


def plane_z(sel):
    z = C0[sel, 2]; w = A[sel]; med = float(np.median(z))
    k = np.abs(z - med) < 0.08
    return float(np.average(z[k], weights=w[k])), float(z[k].std()), int(k.sum())


# ------------------------------------------------------------------ cap (cap frame)
C, r, th = frame("cap")
cw = AX["cap_wall_cone"]
rec("cap_cx", cw["cx"], "cap wall cone fit (axes.json): Z-parallel axis, faces z 2.8-12.9, lever sector -50..50 excluded", rms=cw["rms"], n=cw["n_faces"])
rec("cap_cy", cw["cy"], "same fit", rms=cw["rms"])
rec("cap_R_z0", cw["R_at_z0"], "cone r(z)=R0+k z extrapolated to the crown plane z=0 (same fit)", rms=cw["rms"])
rec("cap_draft_deg", cw["draft_deg"], "cone slope k -> atan(k) (same fit)", rms=cw["rms"])
# crown round: faces between crown flat and wall, away from lever and holes
nonlev = ~angwin(th, -60, 60)
s = nonlev & (C[:, 2] > 0.06) & (C[:, 2] < 2.6) & (r > 10.0) & (r < 12.9)
(rc, zc, R), rms, p95, n = circ_rz(r[s], C[s, 2], np.sqrt(A[s]), [10.3, 2.4, 2.4])
rec("crown_round_R", float(R), "circle fit in (r,z) to cap faces r 10.0-12.9, z 0.06-2.6, theta outside -60..60 (cap frame)", rms=rms, p95=p95, n=n, centre_r=float(rc), centre_z=float(zc))
# crown plane z (datum primary; lever top coplanar)
sc = (N[:, 2] < -0.995) & (C0[:, 2] < 0.3) & (np.hypot(C[:, 0], C[:, 1]) < 10)
zc_, sd, n = plane_z(sc)
rec("crown_z", zc_, "area-weighted mean z of crown faces (n_z<-0.995, r<10) - the datum primary plane", std=sd, n=n)
# step face: underside faces n_z>0.995 at z 13.4-13.9: cap annulus r 12.5-13.1 (non-lever) and lever underside r>23
s1 = (N[:, 2] > 0.995) & (C0[:, 2] > 13.4) & (C0[:, 2] < 13.9) & (r > 12.55) & (r < 13.05) & nonlev
s2 = (N[:, 2] > 0.995) & (C0[:, 2] > 13.4) & (C0[:, 2] < 13.9) & (C0[:, 0] > 23) & (np.abs(C0[:, 1]) < 3)
z1, sd1, n1 = plane_z(s1); z2, sd2, n2 = plane_z(s2)
rec("step_z", [z1, z2], "area-weighted z of up(+Z)-facing faces: [cap annulus r 12.55-13.05, lever underside x>23]", std=[sd1, sd2], n=[n1, n2])
# step outer edge round (cap)
s = nonlev & (C[:, 2] > 12.9) & (C[:, 2] < 13.66) & (r > 12.85) & (r < 13.4) & (N[:, 2] > 0.05)
(rc, zc, R), rms, p95, n = circ_rz(r[s], C[s, 2], np.sqrt(A[s]), [12.8, 13.2, 0.4])
rec("step_edge_R", float(R), "circle fit (r,z) cap faces r 12.85-13.4, z 12.9-13.66, n_z>0.05 (edge round wall->step face)", rms=rms, p95=p95, n=n)

# ------------------------------------------------------------------ collar region (collar frame)
C, r, th = frame("collar")
nonlev = ~angwin(th, -60, 60)
cl = AX["collar"]
rec("collar_cx", cl["cx"], "collar cylinder fit z 14.6-15.9 (axes.json)", rms=cl["rms"], n=cl["n_faces"])
rec("collar_cy", cl["cy"], "same fit", rms=cl["rms"])
rec("collar_R", cl["R"], "same fit (Z-parallel cylinder)", rms=cl["rms"])
# mouth chamfer: sloped faces between step face and ring face, r 11.95-12.45
s = (C[:, 2] > 13.72) & (C[:, 2] < 14.0) & (r > 11.95) & (r < 12.45) & (N[:, 2] > 0.2) & (N[:, 2] < 0.95)
b, sd, n = line_fit(r[s], C[s, 2])
rec("mouth_chamfer_slope", float(b[1]), "line z=a+b r through the mouth chamfer faces r 11.95-12.45 (collar frame)", std=sd, n=n, a=float(b[0]))
# ring face z (faces n_z>0.97, r 11.45-11.9, z 13.95-14.2)
s = (N[:, 2] > 0.97) & (C[:, 2] > 13.95) & (C[:, 2] < 14.25) & (r > 11.45) & (r < 11.95)
zr, sd, n = plane_z(s)
rec("mouth_ring_z", zr, "area-weighted z of +Z-facing ring faces r 11.45-11.95", std=sd, n=n)
# chamfer ends: intersections with step plane (cap annulus z) and ring plane
zs = out["step_z"]["value"][0]
rec("mouth_chamfer_r_out", float((zs - b[0]) / b[1]), "chamfer line evaluated at step_z[0]")
rec("mouth_chamfer_r_in", float((zr - b[0]) / b[1]), "chamfer line evaluated at mouth_ring_z")
# concave round ring face -> collar
s = (C[:, 2] > 14.1) & (C[:, 2] < 14.5) & (r > 11.1) & (r < 11.55) & (N[:, 2] > 0.1)
(rc, zc, R), rms, p95, n = circ_rz(r[s], C[s, 2], np.sqrt(A[s]), [11.5, 14.45, 0.3])
rec("collar_top_round_R", float(R), "circle fit (r,z) faces r 11.1-11.55, z 14.1-14.5, n_z>0.1 (concave round ring face -> collar)", rms=rms, p95=p95, n=n)
# collar bottom face z (+Z facing, r 10.3-10.8)
s = (N[:, 2] > 0.97) & (C[:, 2] > 16.3) & (C[:, 2] < 16.9) & (r > 10.25) & (r < 10.8)
zb, sd, n = plane_z(s)
rec("collar_bot_z", zb, "area-weighted z of +Z-facing faces r 10.25-10.8, z 16.3-16.9", std=sd, n=n)
s = (C[:, 2] > 15.9) & (C[:, 2] < zb + 0.02) & (r > 10.6) & (r < 11.2) & (N[:, 2] > 0.1)
(rc, zc, R), rms, p95, n = circ_rz(r[s], C[s, 2], np.sqrt(A[s]), [10.7, 16.1, 0.45])
rec("collar_bot_round_R", float(R), "circle fit (r,z) faces r 10.6-11.2, z 15.9-collar_bot_z, n_z>0.1 (convex round collar -> bottom face)", rms=rms, p95=p95, n=n)
# outer groove (in the collar bottom face), per 45-deg sectors, excluding the lever sector
gr = []
for t0 in range(-180, 180, 30):
    s = angwin(th, t0, t0 + 30) & ~angwin(th, -60, 60) & (r > 8.9) & (r < 10.25) & (C[:, 2] > 15.7) & (C[:, 2] < 16.8) & (N[:, 2] > 0.2)
    if s.sum() > 30:
        (rc, zc, R), rms, p95, n = circ_rz(r[s], C[s, 2], np.sqrt(A[s]), [9.5, 16.6, 0.6])
        gr.append([t0, float(rc), float(zc), float(R), float(zc - R), rms, n])
g = np.array(gr)
rec("groove_out_rc", float(np.median(g[:, 1])), "median over 30-deg sectors of circle fits (r,z) to the collar-face groove faces r 8.9-10.25 (collar frame)", per_sector=g[:, 1].tolist())
rec("groove_out_bottom_z", float(np.median(g[:, 4])), "same fits: centre_z - R (groove bottom)", per_sector=g[:, 4].tolist(), spread=float(np.ptp(g[:, 4])))
rec("groove_out_R", float(np.median(g[:, 3])), "same fits: arc radius", per_sector=g[:, 3].tolist())
# flange ring face z (+Z facing, r 7.4-8.6)
s = (N[:, 2] > 0.97) & (C[:, 2] > 16.4) & (C[:, 2] < 17.4) & (r > 7.4) & (r < 8.6)
zf, sd, n = plane_z(s)
per = []
for t0 in range(-180, 180, 45):
    ss = s & angwin(th, t0, t0 + 45)
    if ss.sum() > 10: per.append([t0, float(np.median(C[ss, 2]))])
rec("flange_z", float(np.mean([p_[1] for p_ in per])), "mean of 45-deg sector medians of z of +Z-facing faces r 7.4-8.6 (stem flange ring face; the face is not level: see spread)",
    per_sector=per, spread=float(np.ptp([p_[1] for p_ in per])))

# ------------------------------------------------------------------ stem group (stem frame)
C, r, th = frame("stem")
for k in ("x0", "y0", "dxdz", "dydz"):
    rec(f"stem_axis_{k}", LS[k], "line fit through 20 station centres (stem core, neck, sleeve, bore), axis_stations.json", resid_rms=LS["resid_rms"], resid_max=LS["resid_max"])
st = json.load(open(f"{FIG}/axis_stations.json"))["stations"]
core = [s_ for s_ in st if s_["feature"] == "stem_core"]
zz = np.array([s_["z"] for s_ in core]); RR = np.array([s_["R"] for s_ in core])
b, sd, n = line_fit(zz, RR)
rec("stem_core_R_z18", float(b[0] + b[1] * 18.0), "line R(z) through stem-core station circle fits z 18.5-27.5, evaluated at z=18", std=sd, n=n)
rec("stem_core_R_z28", float(b[0] + b[1] * 28.0), "same line evaluated at z=28", std=sd, n=n)
nk = [s_ for s_ in st if s_["feature"] == "neck"]
rec("neck_R", float(np.mean([s_["R"] for s_ in nk])), "mean of neck station circle fits z 30.3, 30.9", reads=[s_["R"] for s_ in nk])
# stem shoulder: top of the core cone and bottom of the neck (between ribs)
betw = angwin((th + 360) % 90, 20, 70)
for zlo, zhi, nm in ((28.3, 28.95, "core_top"),):
    pass
prof = []
for z0 in np.arange(28.0, 30.21, 0.1):
    s = betw & (np.abs(C[:, 2] - z0) < 0.05) & (r > 4.3) & (r < 5.6) & (N[:, 2] > -0.3)
    if s.sum() > 20: prof.append([round(float(z0), 2), float(np.median(r[s]))])
out["shoulder_profile_between_ribs"] = {"value": prof, "estimator": "median r of outward faces per 0.1 mm z, theta 20-70 mod 90 (between ribs), stem frame"}
p = np.array(prof)
# core top z: last z where r >= core_R(z) - 0.05 ; neck start: first z where r <= neck_R + 0.05
coreR = lambda z: b[0] + b[1] * z
zt = [z for z, rr in p if rr >= coreR(z) - 0.06]
zn = [z for z, rr in p if rr <= out["neck_R"]["value"] + 0.05]
rec("stem_core_top_z", float(max(zt)), "highest z (0.1 steps) where the between-rib radius is within 0.06 of the core line", profile="shoulder_profile_between_ribs")
rec("neck_bot_z", float(min(zn)), "lowest z (0.1 steps) where the between-rib radius is within 0.05 of neck_R")
# ribs
rib = {}
for nom in (0, 90, 180, -90):
    d = ((th - nom + 180) % 360) - 180
    tips = []
    for z0 in (18.0, 27.0):
        s = (np.abs(C[:, 2] - z0) < 0.5) & (np.abs(d) < 12) & (r > 5.7) & (r < 7.0)
        tips.append(float(np.percentile(r[s], 98)))
    s = (C[:, 2] > 18) & (C[:, 2] < 27.5) & (np.abs(d) < 12) & (r > 5.75)
    ang = float(np.average(d[s], weights=r[s] - 5.7)) + nom
    # width at r = 5.85 (tangential extent), median over z
    ws = []
    for z0 in np.arange(18.5, 27.1, 1.0):
        ss = (np.abs(C[:, 2] - z0) < 0.3) & (np.abs(d) < 15) & (np.abs(r - 5.85) < 0.06)
        if ss.sum() > 6:
            t = r[ss] * np.radians(d[ss]); ws.append(float(t.max() - t.min()))
    # rib top: z where the rib crest radius (max r in +-2.5 deg, 0.05 mm z steps) falls through
    # the midpoint between the rib tip (z 27) and the core radius at z 28
    zs_ = np.arange(27.0, 29.5, 0.05); crest = []
    for z0 in zs_:
        ss = (np.abs(d) < 2.5) & (np.abs(C[:, 2] - z0) < 0.05) & (r < 7.0) & (r > 4.0)
        crest.append(float(r[ss].max()) if ss.sum() else np.nan)
    crest = np.array(crest); mid = 0.5 * (tips[1] + (b[0] + b[1] * 28.0))
    k = np.where((crest[:-1] >= mid) & (crest[1:] < mid))[0]
    ztop = float(zs_[k[-1]] + 0.05 * (crest[k[-1]] - mid) / (crest[k[-1]] - crest[k[-1] + 1])) if len(k) else float("nan")
    rib[nom] = dict(theta=ang, tip_r_z18=tips[0], tip_r_z27=tips[1], width_r585=float(np.median(ws)) if ws else None, top_z=ztop)
rec("rib_theta_deg", [rib[k]["theta"] for k in (0, 90, 180, -90)], "per rib: (r-5.7)-weighted mean azimuth of rib faces r>5.75, z 18-27.5 (stem frame)")
rec("rib_tip_r_z18", [rib[k]["tip_r_z18"] for k in (0, 90, 180, -90)], "per rib: p98 radius in +-12 deg, z 17.5-18.5")
rec("rib_tip_r_z27", [rib[k]["tip_r_z27"] for k in (0, 90, 180, -90)], "per rib: p98 radius in +-12 deg, z 26.5-27.5")
rec("rib_width", [rib[k]["width_r585"] for k in (0, 90, 180, -90)], "per rib: tangential extent at r=5.85+-0.06, median over z 18.5-27 (1 mm steps)")
rec("rib_top_z", [rib[k]["top_z"] for k in (0, 90, 180, -90)], "per rib: z where the crest radius (max r within +-2.5 deg, 0.05 mm steps) crosses the midpoint between the z=27 tip radius and the core radius at z=28")
# crevice (inner groove) at the stem base: bottom z and centre r, between ribs
gi = []
for t0 in (20, 110, 200, 290):
    s = angwin((th + 360) % 360, t0, t0 + 50) & (r > 5.5) & (r < 7.1) & (C[:, 2] > 15.6) & (C[:, 2] < 16.9) & (N[:, 2] > 0.2)
    if s.sum() > 20:
        (rc, zc, R), rms, p95, n = circ_rz(r[s], C[s, 2], np.sqrt(A[s]), [6.3, 16.8, 0.7])
        gi.append([t0, float(rc), float(zc), float(R), float(zc - R), rms, n])
g = np.array(gi)
rec("groove_in_rc", float(np.median(g[:, 1])), "median of circle fits (r,z) to +Z-ish faces r 5.5-7.1, z 15.6-16.9, 50-deg sectors between ribs (stem frame)", per_sector=g[:, 1].tolist())
rec("groove_in_bottom_z", float(np.median(g[:, 4])), "same fits: centre_z - R", per_sector=g[:, 4].tolist())
rec("groove_in_R", float(np.median(g[:, 3])), "same fits: arc radius", per_sector=g[:, 3].tolist())

# ------------------------------------------------------------------ sleeve (stem frame)
J = json.load(open(f"{FIG}/jog.json"))
for end in ("bottom", "top"):
    for k, nm in (("level_z", "z"), ("ramp_start_deg", "ramp_start_deg"), ("ramp_end_step_deg", "ramp_end_deg"), ("ramp_h", "ramp_h")):
        rec(f"sleeve_{end}_{nm}", J[end][k], f"piecewise fit (level + linear helical ramp + step) to the sleeve {end} edge heights at 3-deg azimuths (jog.json)", rms=J[end]["rms"], p95=J[end]["p95"])
# ripple: crest radius, valley depth, pitch and phase on the planar sector (theta -95..120)
plan = angwin(th, -95, 120)
s = plan & (C[:, 2] > 32.6) & (C[:, 2] < 36.95) & (r > 5.5) & (r < 6.3) & (np.abs(N[:, 2]) < 0.6)
zz, rr, ww = C[s, 2], r[s], np.sqrt(A[s])
def crest_model(q, z):
    rc, rho, p, z1 = q  # crest radius, crest arc radius, pitch, first crest z
    k = np.round((z - z1) / p); dz = z - (z1 + k * p)
    return rc - rho + np.sqrt(np.maximum(rho ** 2 - dz ** 2, 0))
best = None
for p0 in (1.18, 1.22, 1.26, 1.30):
    for z10 in np.arange(32.7, 33.2, 0.1):
        so = least_squares(lambda q: (crest_model(q, zz) - rr) * ww, [5.97, 1.0, p0, z10], loss="soft_l1", f_scale=0.03,
                           bounds=([5.7, 0.3, 1.0, 32.4], [6.3, 3.0, 1.5, 33.5]))
        cst = float(np.sqrt(np.mean((so.fun / ww) ** 2)))
        if best is None or cst < best[1]: best = (so.x, cst)
q, rms_ = best
dep = q[1] - np.sqrt(q[1] ** 2 - (q[2] / 2) ** 2)
rec("sleeve_crest_R", float(q[0]), "fit of touching-arc ripple r(z)=Rc-rho+sqrt(rho^2-dz^2), period p, to sleeve OD faces z 32.6-36.95, theta -95..120 (planar sector, stem frame)", rms=rms_, n=int(s.sum()))
rec("sleeve_ripple_rho", float(q[1]), "same fit: crest arc radius", rms=rms_)
rec("sleeve_ripple_pitch", float(q[2]), "same fit: period (ring pitch)", rms=rms_)
rec("sleeve_first_crest_z", float(q[3]), "same fit: z of the first crest", rms=rms_)
out["sleeve_ripple_depth_derived"] = {"value": float(dep), "estimator": "rho - sqrt(rho^2 - (p/2)^2) from the ripple fit (derived, not a param)"}
print("  ripple depth derived", round(float(dep), 3))
# sleeve bottom round (outer edge) and top round
bl = J["bottom"]["level_z"]; tl = J["top"]["level_z"]
s = plan & (C[:, 2] > bl - 0.05) & (C[:, 2] < bl + 0.6) & (r > 5.0) & (r < 6.05) & (N[:, 2] < -0.1)
(rc, zc, R), rms, p95, n = circ_rz(r[s], C[s, 2], np.sqrt(A[s]), [5.5, bl + 0.5, 0.5])
rec("sleeve_bot_round_R", float(R), "circle fit (r,z) sleeve faces z bottom_level..+0.6, r 5.0-6.05, n_z<-0.1, planar sector", rms=rms, p95=p95, n=n)
s = plan & (C[:, 2] > tl - 0.6) & (C[:, 2] < tl + 0.05) & (r > 5.3) & (r < 6.05) & (N[:, 2] > 0.1)
(rc, zc, R), rms, p95, n = circ_rz(r[s], C[s, 2], np.sqrt(A[s]), [5.5, tl - 0.5, 0.5])
rec("sleeve_top_round_R", float(R), "circle fit (r,z) sleeve faces z top_level-0.6..top_level, r 5.3-6.05, n_z>0.1, planar sector", rms=rms, p95=p95, n=n)
# top face inner edge radius (tail inner radius): in the ramp sector, faces above top level
ramp = angwin((th + 360) % 360, J["top"]["ramp_start_deg"] + 40, J["top"]["ramp_end_step_deg"] - 5)
s = ramp & (C[:, 2] > tl + 0.25) & (r > 3.8) & (r < 6.2)
rec("sleeve_tail_r_in", float(np.percentile(r[s], 2)), "p2 radius of scan faces above top_level+0.25 inside the top-ramp sector (inner edge of the helical tail)", n=int(s.sum()))
# bore
bo = [s_ for s_ in st if s_["feature"] == "bore"]
rec("bore_R", float(np.mean([s_["R"] for s_ in bo])), "mean of bore station circle fits z 36.3, 36.8 (inward faces)", reads=[s_["R"] for s_ in bo])
s = (C[:, 2] > 34.8) & (C[:, 2] < 36.0) & (r > 2.8) & (r < 4.05) & (N[:, 2] > 0.2)
b2, sd, n = line_fit(r[s], C[s, 2])
rec("bore_shoulder_slope", float(b2[1]), "line z=a+b r through +Z-facing bore-shoulder faces r 2.8-4.05, z 34.8-36.0", std=sd, n=n, a=float(b2[0]))
s = (C[:, 2] > 34.5) & (C[:, 2] < 36.2) & (r < 4.3) & (N[:, 2] > -0.5)
rec("bore_seen_min_z", float(np.percentile(C[s, 2], 0.5)), "p0.5 z of scan faces inside the bore (deepest observed)", n=int(s.sum()))
rec("bore_seen_min_r", float(np.percentile(r[s & (C[:, 2] < 35.3)], 1)), "p1 radius of bore faces below z 35.3 (innermost observed)")

# ------------------------------------------------------------------ lever (datum frame)
C, r, th = C0, np.hypot(C0[:, 0], C0[:, 1]), np.degrees(np.arctan2(C0[:, 1], C0[:, 0]))
L = json.load(open(f"{FIG}/lever.json"))["per_z"]
use = [row for row in L if 3.5 < row["z"] < 13.0]
for side in ("+Y", "-Y"):
    zz = np.array([row["z"] for row in use]); yy = np.array([row[f"flank{side}"]["y_at_x18"] for row in use])
    bb = np.array([row[f"flank{side}"]["b"] for row in use])
    fz, sd, n = line_fit(zz, yy)
    tag = "py" if side == "+Y" else "my"
    rec(f"lever_flank_{tag}_y18_z0", float(fz[0]), f"lever {side} flank: line y(x=18)(z) through per-z plane-strip fits z 4-12.8 (lever.json), extrapolated to z=0", std=sd, n=n)
    rec(f"lever_flank_{tag}_draft_deg", float(np.degrees(np.arctan(abs(fz[1])))), "same line: atan(|dy/dz|)", std=sd)
    rec(f"lever_flank_{tag}_plan_deg", float(np.degrees(np.arctan(np.median(bb)))), "median over z of the per-z plan slope dy/dx (lever.json)", reads=bb.tolist())
zz = np.array([row["z"] for row in use]); tR = np.array([row["tip"]["R"] for row in use])
tx = np.array([row["tip"]["cx"] for row in use]); ty = np.array([row["tip"]["cy"] for row in use])
fz, sd, n = line_fit(zz, tR)
rec("lever_tip_R_z0", float(fz[0]), "tip cone: line R(z) through per-z circle fits of tip faces x>23.5 (lever.json), extrapolated to z=0", std=sd, n=n)
rec("lever_tip_draft_deg", float(np.degrees(np.arctan(fz[1]))), "same line: atan(dR/dz)", std=sd)
rec("lever_tip_cx", float(np.median(tx)), "median of per-z tip circle centres x", reads=tx.tolist())
rec("lever_tip_cy", float(np.median(ty)), "median of per-z tip circle centres y", reads=ty.tolist())
# concave blend radius lever flank -> cap wall at several z (plan circle fit)
bl_ = {"+Y": [], "-Y": []}
for z0 in (4.0, 7.0, 10.0, 12.5):
    for side, sg in (("+Y", 1), ("-Y", -1)):
        s = (np.abs(C[:, 2] - z0) < 0.3) & (C[:, 0] > 9.8) & (C[:, 0] < 14.2) & (C[:, 1] * sg > 4.9) & (C[:, 1] * sg < 8.2) & (np.abs(N[:, 2]) < 0.3)
        if s.sum() < 20: continue
        P = C[s, :2]; w = np.sqrt(A[s])
        f = lambda q: (np.hypot(P[:, 0] - q[0], P[:, 1] - q[1]) - q[2]) * w
        so = least_squares(f, [14.0, sg * 9.0, 4.0], loss="soft_l1", f_scale=0.03); res = so.fun / w
        bl_[side].append([z0, float(so.x[2]), float(np.sqrt(np.mean(res ** 2))), int(s.sum())])
allR = [v[1] for sd_ in bl_.values() for v in sd_]
zb_ = np.array([v[0] for sd_ in bl_.values() for v in sd_]); fzb, sdb, nb = line_fit(zb_, np.array(allR))
rec("lever_blend_R_z0", float(fzb[0]), "line R(z) through plan circle fits to the concave lever-cap blend faces (z 4, 7, 10, 12.5; both sides), extrapolated to z=0 (a drafted concave blend shrinks with z)", per_fit=bl_, slope=float(fzb[1]), std=sdb, n=nb)
# lever crown round at the tip (theta 0 meridian) : faces x>23.8, |y|<2
s = (C[:, 0] > 23.8) & (np.abs(C[:, 1]) < 2.0) & (C[:, 2] > 0.06) & (C[:, 2] < 2.9)
(rc, zc, R), rms, p95, n = circ_rz(C[s, 0], C[s, 2], np.sqrt(A[s]), [24.8, 2.5, 2.5])
rec("lever_crown_round_R", float(R), "circle fit (x,z) to lever-tip crown-round faces x>23.8, |y|<2, z 0.06-2.9", rms=rms, p95=p95, n=n)
# lever underside tip edge round
s = (C[:, 0] > 26.6) & (np.abs(C[:, 1]) < 2.0) & (C[:, 2] > 12.8) & (C[:, 2] < 13.8)
(rc, zc, R), rms, p95, n = circ_rz(C[s, 0], C[s, 2], np.sqrt(A[s]), [27.3, 13.3, 0.4])
rec("lever_under_edge_R", float(R), "circle fit (x,z) lever-tip underside edge faces x>26.6, |y|<2, z 12.8-13.8", rms=rms, p95=p95, n=n)
# pocket
PK = json.load(open(f"{FIG}/pocket.json"))
rows = [row for row in PK["per_z"] if row["z"] >= 10.0]
zz = np.array([row["z"] for row in rows])
for key, nm in (("wall+Y (normal -Y)", "pocket_y_plus"), ("wall-Y (normal +Y)", "pocket_y_minus"), ("end_inner (normal +X)", "pocket_x_inner")):
    vv = np.array([row[key][0] for row in rows])
    fz, sd, n = line_fit(zz, vv)
    zs0 = out["step_z"]["value"][1]
    rec(f"{nm}_at_step", float(fz[0] + fz[1] * zs0), f"pocket wall '{key}': line through per-z medians z 10-13.3 (pocket.json), evaluated at the lever step face z", std=sd, n=n)
    rec(f"{nm}_draft_deg", float(np.degrees(np.arctan(abs(fz[1])))), "same line: atan(|d/dz|)", std=sd)
rec("pocket_floor_z", float(np.median([8.42, 8.65])), "floor seen sparsely: 64 +Z-facing faces in the pocket footprint, z p5 8.42 / p50 8.65 (pocket.json); value = mid of p5..p50", n=PK["floor_faces_plusZ_normal"])
# pocket outer (semicircular) end: circle fit in plan to wall faces x>19.8 at z 12-13.4
s = (C[:, 0] > 19.9) & (C[:, 0] < 22.6) & (np.abs(C[:, 1]) < 2.5) & (C[:, 2] > 11.8) & (C[:, 2] < 13.4) & (np.abs(N[:, 2]) < 0.4) & ((N[:, 0] * (C[:, 0] - 20) + N[:, 1] * C[:, 1]) < 0)
P = C[s, :2]; w = np.sqrt(A[s])
so = least_squares(lambda q: (np.hypot(P[:, 0] - q[0], P[:, 1] - q[1]) - q[2]) * w, [20.0, 0.1, 2.2], loss="soft_l1", f_scale=0.03); res = so.fun / w
rec("pocket_end_cx", float(so.x[0]), "plan circle fit to the pocket outer-end wall faces x 19.9-22.6, z 11.8-13.4 (inward-facing)", rms=float(np.sqrt(np.mean(res ** 2))), n=int(s.sum()), R=float(so.x[2]), cy=float(so.x[1]))
# inner-end corner radius: plan circle fits to faces near the two inner corners
cr = []
for sg in (1, -1):
    s = (C[:, 0] > 13.15) & (C[:, 0] < 14.1) & (C[:, 1] * sg > 1.4) & (C[:, 1] * sg < 2.45) & (C[:, 2] > 11.5) & (C[:, 2] < 13.4) & (np.abs(N[:, 2]) < 0.4)
    if s.sum() > 15:
        P = C[s, :2]; w = np.sqrt(A[s])
        so = least_squares(lambda q: (np.hypot(P[:, 0] - q[0], P[:, 1] - q[1]) - q[2]) * w, [13.8, sg * 1.7, 0.5], loss="soft_l1", f_scale=0.03)
        cr.append(float(so.x[2]))
rec("pocket_corner_R", float(np.mean(cr)) if cr else None, "mean of plan circle fits to the two inner-end corner wall faces (z 11.5-13.4)", reads=cr)

json.dump(out, open(f"{FIG}/measurements.json", "w"), indent=1, default=float)
print("wrote", f"{FIG}/measurements.json")
