"""Lever pocket (blind slot open to +Z at the step face): wall positions per z, depth evidence.
Pocket walls = inward-facing faces inside the lever outline. Datum frame. Writes ../pocket.json"""
import json, sys, numpy as np, trimesh
RUN = sys.argv[1]
m = trimesh.load(f"{RUN}/intake/aligned_work.stl"); C, N, A = m.triangles_center, m.face_normals, m.area_faces
inside = (C[:, 0] > 12.5) & (C[:, 0] < 23.5) & (np.abs(C[:, 1]) < 3.6)
out = {"per_z": []}
for z0 in [13.3, 12.8, 12.0, 11.0, 10.0, 9.0, 8.5]:
    s = inside & (np.abs(C[:, 2] - z0) < 0.25) & (np.abs(N[:, 2]) < 0.4)
    row = {"z": z0, "n": int(s.sum())}
    for nm, cond, coord in (("wall+Y (normal -Y)", N[:, 1] < -0.9, 1), ("wall-Y (normal +Y)", N[:, 1] > 0.9, 1),
                            ("end_inner (normal +X)", N[:, 0] > 0.9, 0), ("end_outer (normal -X)", N[:, 0] < -0.9, 0)):
        ss = s & cond
        row[nm] = (round(float(np.median(C[ss, coord])), 3), int(ss.sum())) if ss.sum() > 3 else None
    out["per_z"].append(row); print(row)
# deepest observed pocket-wall z, and any up-facing floor faces inside the pocket footprint
foot = (C[:, 0] > 13.8) & (C[:, 0] < 21.5) & (np.abs(C[:, 1]) < 2.0)
wall = inside & (np.abs(N[:, 2]) < 0.4) & (C[:, 2] > 5) & (C[:, 2] < 13.7) & ((np.abs(N[:, 1]) > 0.9) | (np.abs(N[:, 0]) > 0.9))
floor = foot & (N[:, 2] < -0.9) & (C[:, 2] > 3) & (C[:, 2] < 13.5)
print("deepest wall z p1/min:", np.percentile(C[wall, 2], 1), C[wall, 2].min(), "n wall", wall.sum())
print("floor-like faces (normal -Z, i.e. facing +Z? no: facing -Z) n=", floor.sum())
fl2 = foot & (N[:, 2] > 0.9) & (C[:, 2] > 3) & (C[:, 2] < 13.5)
print("up-facing (+Z normal) faces in footprint n=", fl2.sum(), (np.percentile(C[fl2, 2], [5, 50, 95]) if fl2.sum() else ""))
out["deepest_wall_z_p1"] = float(np.percentile(C[wall, 2], 1)); out["deepest_wall_z_min"] = float(C[wall, 2].min())
out["floor_faces_plusZ_normal"] = int(fl2.sum())
json.dump(out, open(f"{RUN}/measure/figures/pocket.json", "w"), indent=1)
