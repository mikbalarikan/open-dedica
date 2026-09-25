#!/usr/bin/env python3
"""Workaround wrapper for stl-re-intake-datum/scripts/align.py (repo not modified).

Defect: align.py clock_angle(rule='fourier_mass') sums e^{i n theta} over VERTICES
(align.py:251-259). Scan vertex density is not uniform (and scan holes remove vertices
on one side), so the phase is biased. On OD-S03 the vertex phase put the lever
centreline 3.8 deg off the bisector of its two fitted flank planes.

This wrapper replaces ONLY the fourier_mass branch with an AREA-WEIGHTED sum over
FACE CENTRES (same r_range / z_range / n / candidate / pick logic). Every other part of
align.py (primary, origin, tilt, STOP rule, landmarks, outputs) is imported and run
unchanged. Usage: python3 align_areaw.py <spec.json>
"""
import math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-intake-datum/scripts")
import align  # noqa: E402

_orig = align.clock_angle


def clock_angle(m, R_cur, c, seed):
    if c["rule"] != "fourier_mass":
        return _orig(m, R_cur, c, seed)
    n = int(c["n"])
    C, A = m.triangles_center, m.area_faces
    rr = np.hypot(C[:, 0], C[:, 1])
    s = (rr > c["r_range"][0]) & (rr < c["r_range"][1])
    if "z_range" in c:
        s &= (C[:, 2] > c["z_range"][0]) & (C[:, 2] < c["z_range"][1])
    th = np.arctan2(C[s, 1], C[s, 0])
    cn = (A[s] * np.exp(1j * n * th)).sum()
    ph = math.degrees(np.angle(cn)) / n
    cands = sorted(((ph + 360.0 / n * k + 180) % 360) - 180 for k in range(n))
    pick = c.get("pick_nearest_deg", 0.0)
    chosen = min(cands, key=lambda a: abs(((a - pick + 180) % 360) - 180))
    return -chosen, {"n": n, "candidates_deg": cands, "chosen_deg": chosen,
                     "strength": float(abs(cn) / max(A[s].sum(), 1e-12)), "n_faces": int(s.sum()),
                     "weighting": "AREA-weighted face centres (workaround wrapper align_areaw.py; "
                                  "align.py vertex-count fourier is density-biased)",
                     "label_rule": c.get("label_rule", "candidate nearest pick_nearest_deg")}


align.clock_angle = clock_angle
if __name__ == "__main__":
    sys.exit(align.main())
