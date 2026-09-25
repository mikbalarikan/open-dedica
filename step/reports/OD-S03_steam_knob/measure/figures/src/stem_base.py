"""Stem base: lowest z where the between-rib outward-face radius comes within 0.03 mm of the core
cone line (stem frame). Appends 'stem_base_z' to ../measurements.json"""
import json, sys, numpy as np, trimesh
RUN = sys.argv[1]; FIG = f"{RUN}/measure/figures"
M = json.load(open(f"{FIG}/measurements.json")); L = json.load(open(f"{FIG}/axis_stations.json"))["stem_group_line"]
m = trimesh.load(f"{RUN}/intake/aligned_work.stl"); C = m.triangles_center; N = m.face_normals
x = C[:, 0] - (L["x0"] + L["dxdz"] * C[:, 2]); y = C[:, 1] - (L["y0"] + L["dydz"] * C[:, 2]); r = np.hypot(x, y)
th = np.degrees(np.arctan2(y, x)); betw = ((th + 360) % 90 > 20) & ((th + 360) % 90 < 70)
R18, R28 = M["stem_core_R_z18"]["value"], M["stem_core_R_z28"]["value"]; core = lambda z: R18 + (R28 - R18) * (z - 18) / 10
prof = []
for z0 in np.arange(16.6, 19.51, 0.1):
    s = betw & (np.abs(C[:, 2] - z0) < 0.05) & (r > 4.8) & (r < 6.0) & ((N[:, 0] * x + N[:, 1] * y) > 0)
    if s.sum() > 20: prof.append([round(float(z0), 2), float(np.median(r[s]))])
zb = min(z for z, rr in prof if rr <= core(z) + 0.03)
M["stem_base_z"] = {"value": zb, "estimator": "lowest z (0.1 steps, z 16.6-19.5) where the between-rib median outward radius is within 0.03 of the stem-core cone line (stem frame)", "profile": prof}
json.dump(M, open(f"{FIG}/measurements.json", "w"), indent=1, default=float)
print("stem_base_z", zb, prof[:12])
