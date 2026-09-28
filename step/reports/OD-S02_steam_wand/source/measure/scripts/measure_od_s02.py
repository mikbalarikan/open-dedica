#!/usr/bin/env python3
"""OD-S02 steam rod: run-local measurement script (stl-re-measure-intent stage).

The skill's sections/fits scripts assume one datum Z axis; this part has four non-coaxial
axes (rod A = datum Z, tube B, tube C, tip T, bushing axis), so the per-axis fits are done
here with the same estimators the skill uses (Kasa section circles on vertex slabs, line
through the centres; percentile/median radius per station; least-squares plane; spherical
cap). Deterministic (no randomness). Reads intake/aligned_work.stl (datum frame, frozen
intake/alignment.json). Writes measure/figures/measurements.json. Run from the run folder:
    python3 measure/scripts/measure_od_s02.py
"""
import datetime, hashlib, json, sys
from pathlib import Path
import numpy as np, trimesh
from scipy.optimize import least_squares
sys.path.insert(0, str(Path(__file__).resolve().parent))
from axfit import fit_axis, frame, kasa

run = Path.cwd()
mesh_p = run / "intake/aligned_work.stl"
m = trimesh.load(mesh_p)
V, C, N, A = m.vertices, m.triangles_center, m.face_normals, m.area_faces
VN = m.vertex_normals
out = {}
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

def refit(p, d, lo, hi, rmax, rmin=0.0, iters=4, halfw=0.2):
    p = np.array(p, float); d = np.array(d, float) / np.linalg.norm(d)
    cs = None
    for _ in range(iters):
        u, v, dd = frame(d); q = V - p; t = q @ dd; r = np.hypot(q @ u, q @ v)
        s = (r < rmax) & (r > rmin) & (t > lo - 1) & (t < hi + 1)
        p2, d2, cs = fit_axis(V[s], p, d, [(lo, hi)], iters=1, halfw=halfw)
        if d2 @ d < 0: d2 = -d2
        p, d = p2, d2
    return p, d, cs

def stat(cs):
    return {"r_median": float(np.median(cs[:, 3])), "station_rms_median": float(np.median(cs[:, 4])),
            "stations": int(len(cs)), "r_min": float(cs[:, 3].min()), "r_max": float(cs[:, 3].max())}

# ---------------- rod A (datum Z): radius table and station circles
r = np.hypot(V[:, 0], V[:, 1]); th = np.degrees(np.arctan2(V[:, 1], V[:, 0])); z = V[:, 2]
lug = (th > -110) & (th < -65) & (z > 2.8) & (z < 6.0)
ok = (r < 9.6) & ~lug
tab = []
for z0 in np.arange(-0.25, 67.5, 0.25):
    s = ok & (np.abs(z - z0) < 0.125)
    if s.sum() >= 20:
        tab.append([round(float(z0), 3)] + [round(float(x), 4) for x in np.percentile(r[s], [10, 50, 90])] + [int(s.sum())])
out["rod_radius_table"] = {"estimator": "p10/p50/p90 of vertex radius about datum Z per 0.25 mm z-slab (+/-0.125), lug sector excluded",
                           "rows[z,p10,p50,p90,n]": tab}
circ = []
for z0 in [0.8, 1.5, 2.5, 6.0, 7.5, 8.2, 10, 13.5, 15, 16.5, 18, 19.5, 20.5, 22, 24, 27.3, 30, 40, 55, 64]:
    s = (np.abs(z - z0) < 0.15) & (r < 9) & ~lug
    c, R = kasa(V[s, :2]); res = np.hypot(*(V[s, :2] - c).T) - R
    circ.append({"z": z0, "cx": float(c[0]), "cy": float(c[1]), "r": float(R), "rms": float(np.sqrt((res ** 2).mean())), "n": int(s.sum())})
out["rod_station_circles"] = circ
tz = np.array([[row[0], row[2]] for row in tab if 30 <= row[0] <= 64])
k, b = np.polyfit(tz[:, 0], tz[:, 1], 1)
out["rod_taper_line"] = {"dr_dz": float(k), "r_at_z30": float(k * 30 + b), "half_angle_deg": float(np.degrees(np.arctan(-k))),
                         "rms": float(np.sqrt(np.mean((tz[:, 1] - (k * tz[:, 0] + b)) ** 2))), "z_range": [30, 64]}
out["rod_tip_zmax"] = float(z[r < 3.5].max())
# lug
s = (r > 6.85) & lug
s2 = s & (r > 7.6); cth = np.radians(np.median(th[s2]))
tan = -V[s2, 0] * np.sin(cth) + V[s2, 1] * np.cos(cth)
out["collar_lug"] = {"theta_deg": float(np.degrees(cth)), "z_range": [float(np.percentile(z[s], 1)), float(np.percentile(z[s], 99))],
                     "r_top_p95": float(np.percentile(r[s], 95)), "tangential_p1_p99": [float(np.percentile(tan, 1)), float(np.percentile(tan, 99))],
                     "n": int(s.sum())}
# ---------------- knob
secs = {}
for lo, hi in [(60, 120), (-120, -60), (120, 180), (-60, 0)]:
    s = (z > -3.6) & (z < -0.6) & (th > lo) & (th < hi) & (r > 8) & (r < 10)
    secs[f"{lo}..{hi}"] = float(np.median(r[s]))
s = (z > -3.6) & (z < -0.6) & (r > 8) & (r < 10) & (np.abs(th) > 40) & (np.abs(th) < 140)
c, R = kasa(V[s, :2])
out["knob_cylinder"] = {"sector_median_r": secs, "kasa_centre": c.tolist(), "kasa_r": float(R), "z_range": [-3.6, -0.6]}
mer = []
for z0 in np.arange(-3.5, -13.6, -0.5):
    a = (np.abs(z - z0) < 0.12) & (((th > 70) & (th < 110)) | ((th > -110) & (th < -70))) & (r > 2.8) & (r < 10)
    r1, r2 = np.median(r[a & (th > 0)]), np.median(r[a & (th < 0)])
    mer.append([round(float(z0), 2), round(float(r1), 4), round(float(r2), 4), round(float((r1 + r2) / 2), 4)])
out["knob_meridian"] = {"estimator": "median vertex radius in the +Y (70..110 deg) and -Y (-110..-70 deg) sectors per 0.5 mm z (+/-0.12)",
                        "rows[z,r+Y,r-Y,mean]": mer}
s = (N[:, 2] > 0.95) & (np.abs(C[:, 2]) < 0.4) & (np.hypot(C[:, 0], C[:, 1]) > 6.8) & (np.hypot(C[:, 0], C[:, 1]) < 9)
out["knob_top_face_z"] = float(np.median(C[s, 2]))
# knob fairing toward tube B: ellipse per YZ section (x stations), lower part only
from trimesh.intersections import mesh_plane
fair = []
for x0 in [0.0, 1.5, 3.0, 4.5, 6.0, 7.0]:
    Sg = mesh_plane(m, [1, 0, 0], [x0, 0, 0]).reshape(-1, 3)
    yy, zz = Sg[:, 1], Sg[:, 2]
    s = (zz < -3.5) & (zz > -15.5) & ~((np.abs(yy) < 2.9) & (zz < -12.3)) & (np.abs(yy) < 9.8)
    if x0 >= 6.5:
        s &= (zz < -8.0)          # above z -8 at x >= 6.5 the section holds torn flash (photos)
    Y_, Z_ = yy[s], zz[s]
    fe = lambda p: (np.sqrt(((Y_ - p[0]) / p[2]) ** 2 + ((Z_ - p[1]) / p[3]) ** 2) - 1) * min(p[2], p[3])
    so = least_squares(fe, [0, -6, 8, 8], loss="soft_l1", f_scale=0.02); rr_ = fe(so.x)
    fair.append({"x": x0, "yc": float(so.x[0]), "zc": float(so.x[1]), "ay": float(so.x[2]), "az": float(so.x[3]),
                 "rms": float(np.sqrt(np.mean(rr_ ** 2))), "n": int(s.sum())})
out["knob_fairing_ellipses"] = {"estimator": "soft-L1 ellipse fit (centre yc,zc, semi-axes ay,az) to the scan section in the plane x = const, points z -15.5..-3.5 outside the lever plate", "rows": fair}
# ---------------- paddle
pl = {}
s = (N[:, 1] > 0.8) & (C[:, 1] > 0) & (C[:, 1] < 3.5) & (C[:, 0] < -2) & (C[:, 2] < -6)
X, Z, Y = C[s, 0], C[s, 2], C[s, 1]; w = np.ones(len(X), bool)
for _ in range(5):
    co = np.linalg.lstsq(np.c_[X[w], Z[w], np.ones(w.sum())], Y[w], rcond=None)[0]
    d = np.c_[X, Z, np.ones(len(X))] @ co - Y; w = d < 0.15
pl["+Y_face"] = {"y=a*x+b*z+c": co.tolist(), "rms": float(np.sqrt(np.mean(d[w] ** 2))), "estimator": "LSQ plane, 5 passes dropping points >0.15 below (the dish)"}
inr = np.hypot(X + 11.45, Z + 16.88) < 8.5
def capres(p):
    cx, cz, h, Rs = p; rr = np.hypot(X[inr] - cx, Z[inr] - cz); a = np.sqrt(max(2 * Rs * h - h * h, 1e-6))
    return d[inr] - np.where(rr < a, h - (Rs - np.sqrt(np.maximum(Rs ** 2 - rr ** 2, 0))), 0.0)
sol = least_squares(capres, [-11.45, -16.88, 0.8, 30], loss="soft_l1", f_scale=0.1); res = capres(sol.x)
cx, cz, h, Rs = sol.x
pl["dish"] = {"centre_xz": [float(cx), float(cz)], "depth": float(h), "sphere_R": float(Rs), "chord_r": float(np.sqrt(2 * Rs * h - h * h)),
              "rms": float(np.sqrt(np.mean(res ** 2))), "estimator": "spherical cap in the +Y face (soft-L1 LSQ, depth below the fitted face)"}
# -Y (under) face: one tilted plane outside the dish (ring rho 5.6..8.8 around the end circle + the
# knob-side flat), 3-sigma trimmed; then a concave spherical dish (rho < 4.6)
s = (N[:, 1] < -0.8) & (C[:, 1] < -1.5) & (C[:, 1] > -4) & (C[:, 0] < 9) & (C[:, 0] > -23) & (C[:, 2] < -3)
Xu, Yu, Zu = C[s].T
ec_ = np.array([-11.452, -16.884])            # seed: end-circle centre (refit below, same value to 0.01)
rho_u = np.hypot(Xu - ec_[0], Zu - ec_[1])
qq = ((rho_u > 5.6) & (rho_u < 8.8)) | ((Xu > -4) & (Xu < 7) & (Zu < -8) & (Zu > -21))
Am = np.c_[Xu[qq], Zu[qq], np.ones(qq.sum())]; ww = np.ones(qq.sum(), bool)
for _ in range(4):
    co2 = np.linalg.lstsq(Am[ww], Yu[qq][ww], rcond=None)[0]; rs_ = Yu[qq] - Am @ co2; ww = np.abs(rs_) < 3 * np.std(rs_[ww])
pl["-Y_face"] = {"y=a*x+b*z+c": co2.tolist(), "rms": float(np.sqrt(np.mean(rs_[ww] ** 2))), "n": int(ww.sum()),
                 "estimator": "LSQ plane on the underside outside the dish (ring rho 5.6..8.8 about the end circle + knob-side flat), 3-sigma trimmed x4"}
q2 = rho_u < 4.6
fs = lambda p_: np.linalg.norm(np.c_[Xu[q2], Yu[q2], Zu[q2]] - p_[:3], axis=1) - p_[3]
so = least_squares(fs, [ec_[0], -25, ec_[1], 23], loss="soft_l1", f_scale=0.05); rr_ = fs(so.x)
pl["under_dish"] = {"sphere_centre": so.x[:3].tolist(), "sphere_R": float(so.x[3]), "rms": float(np.sqrt(np.mean(rr_ ** 2))),
                    "apex_y": float(so.x[1] + so.x[3]), "n": int(q2.sum()), "estimator": "soft-L1 sphere fit to underside faces within 4.6 of the end-circle centre"}
ymid = lambda x, zz: (co[2] + co2[2]) / 2 + (co[0] + co2[0]) / 2 * x + (co[1] + co2[1]) / 2 * zz
edge = (np.abs(N[:, 1]) < 0.35) & (np.abs(C[:, 1] - ymid(C[:, 0], C[:, 2])) < 1.6) & (C[:, 2] < -2) & (C[:, 0] < 10)
P = C[edge][:, [0, 2]]
e_ = P[(P[:, 0] < -14.5) | ((P[:, 1] < -22) & (P[:, 0] < -8))]
c, R = kasa(e_); res = np.hypot(*(e_ - c).T) - R
pl["end_circle"] = {"centre_xz": c.tolist(), "r": float(R), "rms": float(np.sqrt(np.mean(res ** 2))), "n": int(len(e_))}
for nm, Q in [("upper_edge", P[(P[:, 0] > -17) & (P[:, 0] < -10.5) & (P[:, 1] > -13)]), ("lower_edge", P[(P[:, 0] > -10) & (P[:, 0] < 5) & (P[:, 1] < -14)])]:
    kk_, bb = np.polyfit(Q[:, 0], Q[:, 1], 1)
    pl[nm] = {"z=k*x+b": [float(kk_), float(bb)], "rms": float(np.sqrt(np.mean((Q[:, 1] - (kk_ * Q[:, 0] + bb)) ** 2))),
              "x_range": [float(Q[:, 0].min()), float(Q[:, 0].max())], "n": int(len(Q))}
lo_end = P[(P[:, 0] > 7.5) & (P[:, 0] < 9.2) & (P[:, 1] < -14.8)]
pl["lower_edge_end_xz"] = [float(lo_end[:, 0].max()), float(np.median(lo_end[lo_end[:, 0] > lo_end[:, 0].max() - 0.4, 1]))]
out["paddle"] = pl
# ---------------- tube B (steel, clock crop), sleeve, band
al = json.loads((run / "intake/alignment.json").read_text())
cd = al["clock"]["detail"]; ang = np.radians(al["clock"]["angle_deg"])
Rz = np.array([[np.cos(ang), -np.sin(ang), 0], [np.sin(ang), np.cos(ang), 0], [0, 0, 1]])
pB, dB, cs = refit(Rz @ np.array(cd["axis_point_before_clock"]), Rz @ np.array(cd["axis_dir_before_clock"]), -2.3, 2.5, 3.8)
t0 = -(pB[:2] @ dB[:2]) / (dB[:2] @ dB[:2]); oB = pB + t0 * dB
out["tube_B"] = {"point_at_closest_to_Z": oB.tolist(), "direction": dB.tolist(), "elevation_deg": float(np.degrees(np.arcsin(dB[2]))),
                 "offset_from_Z_axis": float(np.hypot(*oB[:2])), **stat(cs)}
u, v, dd = frame(dB); q = V - oB; tB = q @ dd; rB = np.hypot(q @ u, q @ v)
s = (tB > 10.3) & (tB < 20.2) & (rB < 5) & (rB > 3)
pS, dS, cs = fit_axis(V[s], oB + dB * 15, dB, [(-4.5, 4.5)], iters=4, halfw=0.2)
cs = np.array(cs); kS, bS = np.polyfit(cs[:, 0], cs[:, 3], 1)
w_ = pS - oB
out["sleeve"] = {"point": pS.tolist(), "direction": dS.tolist(), "angle_vs_B_deg": float(np.degrees(np.arccos(abs(dS @ dB)))),
                 "offset_from_B": float(np.linalg.norm(w_ - (w_ @ dB) * dB)), "t_of_point_along_B": float((pS - oB) @ dB),
                 "r_at_point": float(bS), "dr_dt": float(kS), "station_rms_median": float(np.median(cs[:, 4])), "local_t_range": [-4.5, 4.5]}
prof = []
for tt in np.arange(6, 32.01, 0.25):
    s = (np.abs(tB - tt) < 0.12) & (rB < 6)
    if s.sum() > 10: prof.append([round(float(tt), 2)] + [round(float(x), 4) for x in np.percentile(rB[s], [10, 50, 90])])
out["B_profile"] = {"estimator": "p10/p50/p90 vertex radius about tube B per 0.25 mm (t from the point closest to datum Z)", "rows[t,p10,p50,p90]": prof}
# ---------------- tube C, tip, bend, bushing
pC, dC, cs = refit([40.541, -3.048, -27.111], [0.0587, 0.2677, 0.9617], -3, 3, 4.0)
out["tube_C"] = {"point": pC.tolist(), "direction_up": dC.tolist(), **stat(cs)}
pT, dT, cs = refit([36.866, -10.996, -53.45], [-0.1537, -0.3039, -0.9402], -3.5, 3.5, 3.6, rmin=2.55)
out["tip"] = {"point": pT.tolist(), "direction_down": dT.tolist(), **stat(cs),
              "angle_vs_C_deg": float(np.degrees(np.arccos(abs(dC @ dT))))}
u2, v2, d2 = frame(dT); q = V - pT; tt = q @ d2; rr = np.hypot(q @ u2, q @ v2)
out["tip"]["end_t_p99.9"] = float(np.percentile(tt[rr < 3.3], 99.9))
bore = (tt > 1.8) & (tt < 3.0) & (rr < 2.5)
out["tip"]["bore_r_median"] = float(np.median(rr[bore]))
out["tip"]["end_profile[t,p50]"] = [[round(float(a), 2), round(float(np.median(rr[(np.abs(tt - a) < 0.15) & (rr > 2.3) & (rr < 3.5)])), 4)] for a in [3.0, 3.25, 3.5, 3.75]]
w0 = pB - pC; a_ = dB @ dB; b_ = dB @ dC; c_ = dC @ dC; d_ = dB @ w0; e_ = dC @ w0; den = a_ * c_ - b_ * b_
sB = (b_ * e_ - c_ * d_) / den; tC = (a_ * e_ - b_ * d_) / den; V0 = (pB + sB * dB + pC + tC * dC) / 2
n_ = np.cross(dB, dC); n_ /= np.linalg.norm(n_)
phi = float(np.arccos(np.clip(dB @ -dC, -1, 1)))
out["bend"] = {"vertex": V0.tolist(), "deflection_deg": float(np.degrees(phi)), "B_C_line_gap": float((pC - pB) @ n_)}
bis = (-dC - dB); bis /= np.linalg.norm(bis)
near = np.linalg.norm(V - V0, axis=1) < 16; Pn = V[near]
def arcres(Rb):
    T = Rb * np.tan(phi / 2); cen = V0 + bis * Rb / np.cos(phi / 2)
    t1 = V0 - dB * T; t2 = V0 - dC * T; qv = Pn - cen; qn = qv @ n_; qp = qv - np.outer(qn, n_); rho = np.linalg.norm(qp, axis=1)
    a1, a2 = t1 - cen, t2 - cen; aa = np.arccos(np.clip(a1 @ a2 / (np.linalg.norm(a1) * np.linalg.norm(a2)), -1, 1))
    g1 = np.arccos(np.clip(qp @ a1 / (rho * np.linalg.norm(a1) + 1e-12), -1, 1)); g2 = np.arccos(np.clip(qp @ a2 / (rho * np.linalg.norm(a2) + 1e-12), -1, 1))
    inarc = (g1 <= aa + 1e-9) & (g2 <= aa + 1e-9); dist = np.hypot(rho - Rb, qn); sel = inarc & (np.abs(dist - 3.0) < 1.0)
    md = np.median(dist[sel]); return float(np.sqrt(np.mean((dist[sel] - md) ** 2))), float(md), int(sel.sum())
scan = [[round(float(Rb), 2), *arcres(Rb)] for Rb in np.arange(10.4, 12.81, 0.2)]
best = min(scan, key=lambda x: x[1])
out["bend"].update({"radius_scan[Rb,rms,median_tube_r,n]": scan, "radius_best": best[0], "rms_at_best": best[1], "tube_r_in_bend": best[2]})
# bushing barrel axis and profile
dd0 = -dC; u, v, dd0 = frame(dd0); q = V - V0; tb = q @ dd0; rb = np.hypot(q @ u, q @ v)
perp = q - np.outer(tb, dd0); rh = perp / np.maximum(rb, 1e-9)[:, None]; ndr = (VN * rh).sum(1)
s = (tb > 19) & (tb < 30) & (rb > 5) & (rb < 11) & (ndr > 0.5)
pK, dK, cs = fit_axis(V[s], V0 + dd0 * 25, dd0, [(-5, 2)], halfw=0.25)
out["bushing"] = {"point": pK.tolist(), "direction_down": dK.tolist(), "angle_vs_C_deg": float(np.degrees(np.arccos(abs(dK @ dC)))),
                  "angle_vs_tip_deg": float(np.degrees(np.arccos(abs(dK @ dT)))),
                  "centre_to_tip_line": float(np.linalg.norm((pK - pT) - ((pK - pT) @ dT) * dT)),
                  "t_of_point_from_vertex_along_minusC": float((pK - V0) @ -dC)}
# bushing coaxial with the tip: its bottom ring/hub faces are normal to within 0.7/1.4 deg of the tip
# axis but 3.4-3.8 deg off the barrel-circle axis above (it1 self-check). Profile about the TIP axis,
# origin = barrel point projected onto the tip line.
bf = []
u0, v0, d0_ = frame(dK); q0 = C - pK; t0_ = q0 @ d0_; r0_ = np.hypot(q0 @ u0, q0 @ v0); nd0 = N @ d0_
for lab_, s_ in [("bottom_ring", (nd0 > 0.8) & (t0_ > 4.4) & (t0_ < 5.6) & (r0_ > 7.05) & (r0_ < 8.2)),
                 ("bottom_hub", (nd0 > 0.8) & (t0_ > 4.4) & (t0_ < 5.6) & (r0_ > 2.7) & (r0_ < 4.4))]:
    Pp, wp = C[s_], A[s_]; cp = (Pp * wp[:, None]).sum(0) / wp.sum()
    nn = np.linalg.svd((Pp - cp) * np.sqrt(wp)[:, None], full_matrices=False)[2][2]; nn = nn if nn @ d0_ > 0 else -nn
    bf.append({"face": lab_, "normal": nn.tolist(), "angle_vs_tip_deg": float(np.degrees(np.arccos(abs(nn @ dT)))),
               "angle_vs_barrel_axis_deg": float(np.degrees(np.arccos(abs(nn @ d0_)))), "n": int(s_.sum())})
out["bushing"]["flat_face_normals"] = bf
pK = pT + ((pK - pT) @ dT) * dT; dK = dT.copy()
out["bushing"]["axis_used"] = {"point": pK.tolist(), "direction_down": dK.tolist(), "rule": "coaxial with the tip (flat_face_normals)"}
u, v, dK_ = frame(dK); q = V - pK; tk = q @ dK_; x_, y_ = q @ u, q @ v; rk = np.hypot(x_, y_)
rh = np.c_[x_, y_] / np.maximum(rk, 1e-9)[:, None]; nr = (VN @ u) * rh[:, 0] + (VN @ v) * rh[:, 1]; ntk = VN @ dK_
prof = []
for a in np.arange(-9, 6.6, 0.5):
    s = (np.abs(tk - a) < 0.15) & (rk > 3.6) & (rk < 10.5) & (nr > 0.3)
    if s.sum() > 10: prof.append([round(float(a), 2)] + [round(float(x), 4) for x in np.percentile(rk[s], [10, 50, 90])])
out["bushing"]["outer_profile[t,p10,p50,p90]"] = prof
ax_ = []
for a in np.arange(3, 10, 1.0):
    for sg in [1, -1]:
        s = (rk > a) & (rk < a + 1) & (ntk * sg > 0.8) & (tk > -10) & (tk < 7)
        if s.sum() > 10: ax_.append([a, a + 1, sg, *[round(float(x), 3) for x in np.percentile(tk[s], [10, 50, 90])], int(s.sum())])
out["bushing"]["axial_faces[r0,r1,sign,t10,t50,t90,n]"] = ax_
# bushing underside windows, in the bushing frame (z = t along bush_dir_down, x = frame() u)
ub, vb, db_ = frame(np.array(out["bushing"]["axis_used"]["direction_down"]))
qb = C - np.array(out["bushing"]["axis_used"]["point"]); tb_ = qb @ db_; xb, yb = qb @ ub, qb @ vb; rbb = np.hypot(xb, yb)
dn = (N @ db_) > 0.5
bot = (tb_ > 4.7) & (tb_ < 5.4) & dn
hr, er = np.histogram(rbb[bot], bins=np.arange(2, 9, 0.25), weights=A[bot])
sw = (tb_ > 3.0) & (tb_ < 4.7) & (np.abs(N @ db_) < 0.4)
hw, ew = np.histogram(rbb[sw], bins=np.arange(2, 9, 0.25), weights=A[sw])
cnt = json.loads((run / "measure/figures/count_bushing_spokes.json").read_text())
ph = float(np.mean([st_["crest_phase_deg_of_selected"] for st_ in cnt["stations"]]))
thc = ((np.degrees(np.arctan2(yb, xb)) - ph + 30) % 60) - 30
sp = bot & (rbb > 4.8) & (rbb < 6.7)
hs, es = np.histogram(thc[sp], bins=np.arange(-30, 31, 1), weights=A[sp])
half = hs.max() / 2; above = es[:-1][hs >= half]
fl = (tb_ > 2.0) & (tb_ < 4.7) & dn & (rbb > 4.7) & (rbb < 6.8)
out["bushing_windows"] = {"frame_x": ub.tolist(), "frame_y": vb.tolist(), "count_json": "measure/figures/count_bushing_spokes.json",
                          "count": int(cnt["count"]), "spoke_phase_deg": ph,
                          "bottom_faces_by_r[r0,area]": [[float(a), float(b)] for a, b in zip(er[:-1], hr)],
                          "side_walls_by_r[r0,area]": [[float(a), float(b)] for a, b in zip(ew[:-1], hw)],
                          "spoke_fwhm_deg": float(above.max() + 1 - above.min()),
                          "floor_faces_t_p10_p50_p90": np.percentile(tb_[fl], [10, 50, 90]).tolist(), "floor_area": float(A[fl].sum())}
doc = {"schema": "stl-re/measurements@1", "tool": "measure/scripts/measure_od_s02.py (run-local)", "tool_version": "OD-S02",
       "inputs": {"intake/aligned_work.stl": sha(mesh_p), "intake/alignment.json": sha(run / "intake/alignment.json")}, "seed": 0,
       "created": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), **out}
(run / "measure/figures").mkdir(parents=True, exist_ok=True)
(run / "measure/figures/measurements.json").write_text(json.dumps(doc, indent=1))
print(json.dumps({k: v for k, v in out.items() if k not in ("rod_radius_table", "B_profile", "knob_meridian", "rod_station_circles")}, indent=1)[:6000])
