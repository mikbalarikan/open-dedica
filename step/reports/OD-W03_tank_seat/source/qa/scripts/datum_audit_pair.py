#!/usr/bin/env python3
"""QA workaround (skill defect): datum_audit.py supports a single `position.circle` and a
fourier/plane_normal clock only. OD-W03's datum is origin = midpoint of TWO cup axes and clock =
feature_line cup A -> cup B (intake/alignment.json). This wrapper reuses datum_audit.py's own fit
functions (plane_by_vote, svd_plane, circle_irls, basis) and _common.select, on the RAW scan; the
builder matrix only selects regions. Output keys match datum_audit.py."""
import argparse, math, sys
from pathlib import Path
import numpy as np
S = Path("/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
sys.path.insert(0, str(S))
import datum_audit as DA  # noqa: E402
from _common import header, load_matrix, load_mesh, read_json, rot_angle_deg, select, write_json  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--scan", required=True); ap.add_argument("--align", required=True)
ap.add_argument("--spec", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--seed", type=int, default=0); ap.add_argument("--n-compare", type=int, default=60000)
a = ap.parse_args()
spec = read_json(a.spec)
m = load_mesh(a.scan, process=False); m.merge_vertices()
Tb = load_matrix(a.align)
N, A, C, V, F = m.face_normals, m.area_faces, m.triangles_center, m.vertices, m.faces
Cb = C @ Tb[:3, :3].T + Tb[:3, 3]; Nb = N @ Tb[:3, :3].T
zb = Tb[:3, :3].T @ np.array([0, 0, 1.0]); xb = Tb[:3, :3].T @ np.array([1.0, 0, 0])
out = {"independence": "builder matrix used only to select named regions; all fits are QA code (datum_audit.py functions) on raw scan",
       "workaround": "qa/scripts/datum_audit_pair.py (datum_audit.py has no circle_pair/midpoint origin or feature_line clock)"}
pr = spec["primary"]
cand = select(pr["region"], Cb, Nb)
pl = DA.plane_by_vote(N, A, C, V, F, pr.get("cone_deg", 3.0), pr.get("band_mm", 0.30), cand)
ax, p0 = pl["normal"], pl["point"]
out["primary"] = {"type": "plane", "method": pl["method"], "faces": pl["faces"], "fit_rms_mm": pl["rms"], "fit_max_mm": pl["max"]}
R0 = DA.basis(ax)
po = spec["position"]
cents = {}
for key in ("region_a", "region_b"):
    s_ = select(po[key], Cb, Nb) & (np.abs(N @ ax) < po.get("perp_max_dot", 0.30))
    Cl = (C - p0) @ R0.T
    c2, Rm, rms = DA.circle_irls(Cl[s_][:, :2], A[s_], po.get("cauchy_scale_mm", 0.30))
    cents[key] = p0 + c2[0] * R0[0] + c2[1] * R0[1]
    out.setdefault("position", {"type": "circle_pair", "combine": "midpoint", "single_wall": po.get("single_wall")})[key] = {
        "faces": int(s_.sum()), "R_mm": Rm, "fit_rms_mm": rms, "centre_builder_frame": (Tb[:3, :3] @ cents[key] + Tb[:3, 3]).tolist()}
origin = 0.5 * (cents["region_a"] + cents["region_b"])
d = cents["region_b"] - cents["region_a"]
out["position"]["separation_mm"] = float(np.linalg.norm(d - (d @ ax) * ax))
xdir = d - (d @ ax) * ax; xdir /= np.linalg.norm(xdir)
out["clock"] = {"type": "feature_line", "from": "cup A", "to": "cup B"}
R = np.stack([xdir, np.cross(ax, xdir), ax]); Tq = np.eye(4); Tq[:3, :3], Tq[:3, 3] = R, -R @ origin
rng = np.random.default_rng(a.seed)
smp = V[rng.choice(len(V), min(a.n_compare, len(V)), replace=False)]
dd = np.linalg.norm((smp @ Tq[:3, :3].T + Tq[:3, 3]) - (smp @ Tb[:3, :3].T + Tb[:3, 3]), axis=1)
o_b = Tb[:3, :3] @ origin + Tb[:3, 3]
ang = rot_angle_deg(Tq[:3, :3] @ Tb[:3, :3].T)
ax_ang = float(np.degrees(np.arccos(np.clip(ax @ zb, -1, 1))))
clk = float(np.degrees(np.arctan2(xdir @ (Tb[1, :3]), xdir @ (Tb[0, :3]))))
out.update({"angle_deg": ang, "axis_angle_deg": ax_ang, "clock_diff_deg": clk, "clock_audited": True,
            "origin_offset_mm": float(np.linalg.norm(o_b)), "origin_offset_vec_mm": o_b.tolist(),
            "point_disagreement_mean_mm": float(dd.mean()), "point_disagreement_p95_mm": float(np.percentile(dd, 95)),
            "point_disagreement_max_mm": float(dd.max()), "reference_band": "≤0.3° / ≤0.15 mm (RE_SPEC.md:241)",
            "reference": DA.REF_BAND, "within_reference": bool(ang <= 0.3 and np.linalg.norm(o_b) <= 0.15),
            "blocking": False, "note": "REPORT-ONLY (QUESTIONS.md Q2).", "T_qa": Tq.tolist()})
write_json(a.out, {**header("datum_audit", "datum_audit.py (via qa/scripts/datum_audit_pair.py)", [a.scan, a.align, a.spec], a.seed), **out})
print(f"datum audit: rot {ang:.4f} deg (axis {ax_ang:.4f}, clock {clk:.4f}) | origin offset {o_b} |{np.linalg.norm(o_b):.4f}| mm | "
      f"pts mean {dd.mean():.4f} p95 {np.percentile(dd,95):.4f} max {dd.max():.4f} | sep {out['position']['separation_mm']:.4f}")
print(out["primary"], out["position"])
