"""Run-local: bore draft line fit, pocket riser radius, groove at bore base, rim lip outer edge.
Full-res scan, datum frame. Writes measure/figures/misc_fits.json"""
import json, numpy as np, trimesh
m = trimesh.load('input/scan.stl'); T = np.array(json.load(open('intake/alignment.json'))['matrix_4x4']); m.apply_transform(T)
c = m.triangles_center; n = m.face_normals; a = m.area_faces
r = np.hypot(c[:, 0], c[:, 1]); th = np.degrees(np.arctan2(c[:, 1], c[:, 0])) % 360; z = c[:, 2]
starts = [336.0, 96.0, 216.0]
def win(t0, t1): return ((th - t0) % 360) < ((t1 - t0) % 360)
gap = np.any([win(s + 62, s + 112) for s in starts], axis=0)
lugsec = np.any([win(s + 8, s + 50) for s in starts], axis=0)
vert = np.abs(n[:, 2]) < 0.25; up = n[:, 2] > 0.85
out = {}
b = gap & vert & (r > 36.5) & (r < 37.6) & (z > -13.5) & (z < 2.5)
A = np.c_[np.ones(b.sum()), z[b]]; sol, *_ = np.linalg.lstsq(A, r[b], rcond=None); res = r[b] - A @ sol
out['bore_gap_line'] = {'r_at_z0': round(float(sol[0]), 4), 'dr_dz': round(float(sol[1]), 5), 'draft_deg': round(float(np.degrees(np.arctan(sol[1]))), 3),
                        'rms': round(float(res.std()), 4), 'n': int(b.sum()), 'z_range': [-13.5, 2.5]}
rs = lugsec & vert & (r > 33.6) & (r < 35.2) & (z > -16.3) & (z < -15.2)
out['pocket_riser_r'] = {'p50': round(float(np.median(r[rs])), 3), 'p5_p95': [round(float(v), 3) for v in np.percentile(r[rs], [5, 95])], 'n': int(rs.sum())}
# groove at bore base: min z of scan in r 36.6..37.5 per sector type
for nm, sel, zr in [('groove_lug', lugsec, (-17.0, -14.5)), ('groove_gap', gap, (-15.5, -13.0))]:
    rows = []
    for r0 in np.arange(36.0, 37.6, 0.1):
        t = sel & (r >= r0) & (r < r0 + 0.1) & (z > zr[0]) & (z < zr[1]) & (n[:, 2] > 0.3)
        if t.sum() > 20: rows.append([round(r0 + 0.05, 2), round(float(np.percentile(z[t], 5)), 3), round(float(np.median(z[t])), 3), int(t.sum())])
    out[nm] = rows
lip = gap & up & (z > 2.8) & (r > 37.6) & (r < 39.2)
out['rim_lip_top_r_p99'] = round(float(np.percentile(r[lip], 99)), 3)
led = gap & up & (z > 2.0) & (z < 2.8) & (r > 38.0) & (r < 40.0)
out['rim_ledge_r_p1'] = round(float(np.percentile(r[led], 1)), 3)
P = np.c_[r[led], np.ones(led.sum())]; s2, *_ = np.linalg.lstsq(P, z[led], rcond=None)
out['rim_ledge_line_z_vs_r'] = {'slope': round(float(s2[0]), 4), 'z_at_r38.5': round(float(s2[0] * 38.5 + s2[1]), 3), 'z_at_r39.8': round(float(s2[0] * 39.8 + s2[1]), 3)}
json.dump(out, open('measure/figures/misc_fits.json', 'w'), indent=1); print(json.dumps(out, indent=1))
