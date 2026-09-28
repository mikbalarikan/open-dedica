"""Run-local QA helper (qa/ only): locate coverage-gap masks FROM THE SCAN (mask-policy rule 7).
Reads input/scan.stl + intake/alignment.json only. No CAD is loaded."""
import json, sys
import numpy as np
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import load_mesh, load_matrix
s = load_mesh("input/scan.stl", process=False); s.merge_vertices()
s.apply_transform(load_matrix("intake/alignment.json"))
C, N, A = s.triangles_center, s.face_normals, s.area_faces
r = np.hypot(C[:, 0], C[:, 1]); th = (np.degrees(np.arctan2(C[:, 1], C[:, 0])) + 360) % 360; z = C[:, 2]
out = {"faces": int(len(C)), "area_mm2": float(A.sum())}
# C1: downward-facing area
out["C1_area_frac_nz_lt_-0.5"] = float(A[N[:, 2] < -0.5].sum() / A.sum())
# C2/C3: anything below the plate top, inside the outer wall
for zc in (-20.3, -20.5, -21.0):
    m = (z < zc) & (r < 39.5)
    out[f"C2_below_z{zc}_r_lt_39.5"] = {"faces": int(m.sum()), "area_mm2": float(A[m].sum()),
                                         "z_min": float(z[m].min()) if m.any() else None}
out["scan_z_min"] = float(z.min())
# C3: plate interior coverage (angular coverage per radial band near the plate level)
pl = (z > -21) & (z < -18.5)
bands = {}
for r0, r1 in ((0, 10), (10, 20.3), (20.3, 22.4), (22.4, 24.0), (24.0, 24.6), (24.6, 26), (26, 28)):
    m = pl & (r >= r0) & (r < r1)
    occ = np.unique((th[m] // 5).astype(int))
    bands[f"{r0}-{r1}"] = {"faces": int(m.sum()), "deg_covered_5deg_bins": int(len(occ) * 5)}
out["C3_plate_level_coverage"] = bands
# C6: outer wall coverage per 5 deg bin, z -27.8..2
w = (r > 39.6) & (r < 40.7) & (np.abs(N[:, 2]) < 0.3)
hist = np.zeros(72)
np.add.at(hist, (th[w] // 5).astype(int), A[w])
out["C6_outer_wall_area_per_5deg_bin_mm2"] = [round(float(h), 1) for h in hist]
empty = [i * 5 for i in range(72) if hist[i] < 5.0]
out["C6_bins_lt_5mm2_start_deg"] = empty
json.dump(out, open("qa/scan_coverage_survey.json", "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "C6_outer_wall_area_per_5deg_bin_mm2"}, indent=1))
print("wall area/5deg:", out["C6_outer_wall_area_per_5deg_bin_mm2"])
