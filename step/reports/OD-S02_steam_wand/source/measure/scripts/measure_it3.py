#!/usr/bin/env python3
"""OD-S02 it3 (REVISE route geometry, _it2_SUPERSEDED/qa): measure the three geometric causes verify
named. Run from the run folder. Writes measure/figures/measure_it3.json.
  Z2: tube centreline through the bend by marching Kasa section circles (1 mm steps, slab +/-0.3,
      points within r 4.2, direction from the last 3 centres) from tube B t 25 until the radius
      jumps at the bushing; radius per station.
  Z3: lever perimeter round radius: points near the round end (angle 100..280 deg about the end
      circle, 0..3.5 inside the outline), per face side, least-squares round tangent to face and outline.
  Z4: tip-tube neck just below the bushing: p50 radius about the tip axis every 0.2 mm."""
import datetime, hashlib, json, sys
from pathlib import Path
import numpy as np, trimesh
from scipy.optimize import least_squares
from scipy.spatial import cKDTree
sys.path.insert(0, str(Path(__file__).resolve().parent))
from axfit import frame, kasa
run = Path.cwd()
mesh_p = run / "intake/aligned_work.stl"
V = trimesh.load(mesh_p).vertices
M = json.loads((run / "measure/figures/measurements.json").read_text())
P = json.loads((run / "measure/params.json").read_text())["params"]
out = {}
# Z2
oB = np.array(M["tube_B"]["point_at_closest_to_Z"]); dB = np.array(M["tube_B"]["direction"])
p = oB + dB * 25.0; d = dB.copy(); pts = []; tree = cKDTree(V)
for _ in range(60):
    Q = V[tree.query_ball_point(p, 5.0)]
    u, v, dd = frame(d); q = Q - p; t = q @ dd; x = q @ u; y = q @ v; r = np.hypot(x, y)
    s = (np.abs(t) < 0.3) & (r < 4.2)
    if s.sum() < 30: break
    c, R = kasa(np.c_[x[s], y[s]]); res = np.hypot(x[s] - c[0], y[s] - c[1]) - R
    pc = p + c[0] * u + c[1] * v
    pts.append([*pc.tolist(), float(R), float(np.sqrt((res ** 2).mean())), int(s.sum())])
    if R > 3.5: break
    if len(pts) >= 3:
        P3 = np.array([q_[:3] for q_ in pts[-3:]]); d = (P3[-1] - P3[0]) / np.linalg.norm(P3[-1] - P3[0])
    p = pc + d * 1.0
out["tube_centerline"] = {"rows[x,y,z,r,rms,n]": pts, "estimator": "marching Kasa section circles, 1 mm steps (slab +/-0.3 mm, r < 4.2), direction from the last 3 centres; starts on tube B at t 25"}
# Z3
(cx, cz), Re = P["paddle_end_c"]["value"], P["paddle_end_r"]["value"]
a1, b1, c1 = P["paddle_face_pos"]["value"]; a2, b2, c2 = P["paddle_face_neg"]["value"]
x, y, z = V.T; rho = np.hypot(x - cx, z - cz); ang = np.degrees(np.arctan2(z - cz, x - cx)) % 360; s_ = Re - rho
yp = a1 * x + b1 * z + c1; yn = a2 * x + b2 * z + c2
sel = (ang > 100) & (ang < 280) & (s_ > -0.3) & (s_ < 3.5) & (y < yp + 0.5) & (y > yn - 0.5)
rf = {}
for lab, side in [("+Y", 1), ("-Y", -1)]:
    q = sel & ((y > (yp + yn) / 2) if side > 0 else (y < (yp + yn) / 2))
    S = s_[q]; H = (yp - y)[q] if side > 0 else (y - yn)[q]
    def res(pp):
        Rf = pp[0]
        return np.where((S < Rf) & (H < Rf), np.hypot(Rf - S, Rf - H) - Rf, np.minimum(np.abs(S), np.abs(H)))
    so = least_squares(res, [1.5], bounds=([0.3], [3.0]), loss="soft_l1", f_scale=0.05); rr = res(so.x)
    rf[lab] = {"Rf": float(so.x[0]), "rms": float(np.sqrt(np.mean(rr ** 2))), "n": int(q.sum())}
out["paddle_perimeter_round"] = {"per_side": rf, "estimator": "round tangent to the face plane and the end-circle outline, soft-L1 LSQ on scan vertices 0..3.5 mm inside the outline, end arc 100..280 deg"}
# Z4
pT = np.array(P["tip_point"]["value"]); u, v, dT = frame(np.array(P["tip_dir_down"]["value"]))
q = V - pT; t = q @ dT; r = np.hypot(q @ u, q @ v)
rows = []
for t0 in np.arange(-10.0, -7.99, 0.2):
    s = (np.abs(t - t0) < 0.08) & (r < 3.4) & (r > 2.2)
    if s.sum() > 10: rows.append([round(float(t0), 2), float(np.percentile(r[s], 50)), int(s.sum())])
out["tip_neck"] = {"rows[t,p50,n]": rows, "bushing_bottom_tip_t": float((np.array(P["bush_point"]["value"]) - pT) @ dT + P["bush_bottom"]["value"][1]),
                   "estimator": "p50 vertex radius about the tip axis, slab +/-0.08 mm, r 2.2..3.4"}
doc = {"schema": "stl-re/measure_it3@1", "tool": "measure/scripts/measure_it3.py (run-local)", "tool_version": "OD-S02",
       "inputs": {"intake/aligned_work.stl": hashlib.sha256(mesh_p.read_bytes()).hexdigest()}, "seed": 0,
       "created": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), **out}
(run / "measure/figures/measure_it3.json").write_text(json.dumps(doc, indent=1))
print(json.dumps({"n_centreline": len(pts), "round": rf, "neck": rows}, indent=1))
