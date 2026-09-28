"""it2 (verify it1 clusters 8/9, CAD->scan 5/6/7): lug under-face lead-out at the trailing (high-theta) end.
Under-face z per 1-degree bin = median z of down-facing samples (n_z < -0.7), r 31.8..35, z -6.5..-1.5.
The main ramp line (m11) is extrapolated; the knee is the first bin where the median rises more than 0.1 mm
above it; the lead-out line is fitted to the bins from the knee to the last bin with >= 30 samples."""
import json, numpy as np, trimesh
m = trimesh.load('intake/aligned_work.stl'); P, fi = trimesh.sample.sample_surface(m, 3000000, seed=0); N = m.face_normals[fi]
r = np.hypot(P[:, 0], P[:, 1]); th = np.degrees(np.arctan2(P[:, 1], P[:, 0])) % 360; z = P[:, 2]
D = json.load(open('measure/figures/details.json'))["lug_ramps"]; L = json.load(open('measure/figures/lugs_notches.json'))["lugs"]
base = (r > 31.8) & (r < 35) & (z < -1.5) & (z > -6.5) & (N[:, 2] < -0.7)
out = []
for lug, rp in zip(L, D):
    c = rp["centre_deg"]; bins = []
    for a in np.arange(c, c + lug["span_deg"] / 2 + 3, 1.0):
        t = (th - a) % 360; s = base & (t < 1.0)
        if s.sum() >= 30: bins.append((a + 0.5 - c, float(np.median(z[s]))))
    b = np.array(bins); main = rp["z_at_centre"] + rp["dz_per_deg"] * b[:, 0]
    k = int(np.argmax(b[:, 1] - main > 0.1))
    seg = b[k:]; sl, ic = np.polyfit(seg[:, 0], seg[:, 1], 1)
    out.append({"centre_deg": c, "knee_offset_deg": float(b[k, 0]), "leadout_z_at_centre_line": float(ic), "leadout_dz_per_deg": float(sl),
                "last_bin_offset_deg": float(b[-1, 0]), "last_bin_z": float(b[-1, 1]), "n_bins": int(len(seg)),
                "rms": float(np.sqrt(((seg[:, 1] - (ic + sl * seg[:, 0]))**2).mean()))})
json.dump({"lugs": out}, open('measure/figures/lug_ends.json', 'w'), indent=1); print(json.dumps(out, indent=1))
