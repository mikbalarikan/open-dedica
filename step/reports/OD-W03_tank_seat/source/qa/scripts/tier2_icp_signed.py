#!/usr/bin/env python3
"""QA workaround (skill defect, tier2_icp.py:52): the correspondence normal test is SIGN-FREE
(np.abs(n_cad . n_scan) > cos 70). On a CAD with an invented hollow shell (owner decision: 1.2 mm
walls, unscanned underside/interiors), inward-facing interior faces lying 1.2 mm behind the scanned
outer skin pass that test and the 3.0 mm distance test, and pull the registration (default run:
+0.659 mm in z, contradicting the independent datum audit). This variant changes ONLY that line to a
signed agreement (n_cad . n_scan > cos 70), i.e. an outward CAD face may only pair with an
outward-facing scan face. Every other parameter, sample, seed and the Kabsch loop are tier2_icp.py's
own (imported, not copied). Both runs are kept and reported."""
import json, math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
import tier2_icp as T2  # noqa: E402
from _common import rot_angle_deg  # noqa: E402


def icp_signed(cp, cn, sp, sn, btree, normal_deg, boundary_mm, max_corr_mm, max_iter, tol):
    from scipy.spatial import cKDTree
    stree = cKDTree(sp)
    cosang = math.cos(math.radians(normal_deg))

    def corr(P, Nn):
        d, i = stree.query(P, workers=-1)
        ok = ((Nn * sn[i]).sum(1) > cosang) & (d < max_corr_mm)          # SIGNED (the only change)
        if btree is not None:
            ok &= btree.query(sp[i], workers=-1)[0] > boundary_mm
        return d, i, ok

    T = np.eye(4); P, Nn = cp.copy(), cn.copy(); trace = []; converged = False; it = -1
    for it in range(max_iter):
        d, i, ok = corr(P, Nn)
        A_, B_ = P[ok], sp[i][ok]
        ca, cb = A_.mean(0), B_.mean(0)
        U, _, Vt = np.linalg.svd((A_ - ca).T @ (B_ - cb))
        D = np.diag([1.0, 1.0, float(np.sign(np.linalg.det(Vt.T @ U.T)))])
        R = Vt.T @ D @ U.T; t = cb - R @ ca
        P = P @ R.T + t; Nn = Nn @ R.T
        rot = rot_angle_deg(R); step = float(np.linalg.norm(t) + rot)
        Tn = np.eye(4); Tn[:3, :3], Tn[:3, 3] = R, t; T = Tn @ T
        trace.append({"it": it, "step": step, "rot_deg": rot, "trans_mm": float(np.linalg.norm(t)),
                      "kept_fraction": float(ok.mean()), "mean_d_kept": float(d[ok].mean())})
        if step < tol:
            converged = True
            break
    d, i, ok = corr(P, Nn)
    return {"T_refine": T, "iterations": it + 1, "converged": converged, "trace_tail": trace[-6:],
            "final_kept_fraction": float(ok.mean()), "max_point_move_mm": float(np.linalg.norm(P - cp, axis=1).max())}


T2.icp = icp_signed
rc = T2.main(sys.argv[1:])
out = sys.argv[sys.argv.index("--out") + 1]
j = json.loads(Path(out).read_text())
j["method"] = ("point-to-point ICP, CAD samples -> scan samples, masked correspondences (B02 q20_tier2.py), "
               "SIGNED normal agreement (QA workaround qa/scripts/tier2_icp_signed.py; tier2_icp.py:52 is sign-free)")
j["variant"] = "signed-normal correspondence; all other parameters = tier2_icp.py defaults"
j["companion_run"] = "qa/registration_default_signfree.json (tier2_icp.py as shipped)"
Path(out).write_text(json.dumps(j, indent=1) + "\n")
raise SystemExit(rc)
