"""Run-local: per-instance levels (3 gaps, 3 lugs) and centre offset of the inner (lug) features
vs the datum axis. Full-res scan, datum frame. Writes measure/figures/instances.json"""
import json, sys, numpy as np, trimesh
sys.path.insert(0, '/home/user/agentic_STL-to-CAD/skills/stl-re-intake-datum/scripts')
from datum_fit import fit_circle_irls
m = trimesh.load('input/scan.stl'); T = np.array(json.load(open('intake/alignment.json'))['matrix_4x4']); m.apply_transform(T)
c = m.triangles_center; n = m.face_normals; a = m.area_faces
r = np.hypot(c[:, 0], c[:, 1]); th = np.degrees(np.arctan2(c[:, 1], c[:, 0])) % 360; z = c[:, 2]
up = n[:, 2] > 0.85; vert = np.abs(n[:, 2]) < 0.3
def win(t0, t1): return ((th - t0) % 360) < ((t1 - t0) % 360)
starts = [336.0, 96.0, 216.0]
out = {'lug_start_deg': starts, 'gaps': [], 'lugs': []}
for k, s in enumerate(starts):
    g0, g1 = (s + 58.5 + 3) % 360, (s + 120 - 5 - 3) % 360   # gap interior, 3 deg in from pocket edges
    sh = up & win(g0, g1) & (r > 32.5) & (r < 36.5) & (z > -15) & (z < -12.8)
    fl = up & (r > 24.5) & (r < 30) & (z > -20.6) & (z < -19.3)
    out['gaps'].append({'theta': [round(g0, 1), round(g1, 1)], 'shelf_z_p50': round(float(np.median(z[sh])), 3),
                        'shelf_z_p5_p95': [round(float(v), 3) for v in np.percentile(z[sh], [5, 95])]})
    l0, l1 = (s - 5 + 3) % 360, (s + 58.5 - 3) % 360
    pi = up & win(l0, l1) & (r > 31.4) & (r < 34.0) & (z > -17.5) & (z < -15.5)
    po = up & win(l0, l1) & (r > 34.8) & (r < 36.6) & (z > -16.0) & (z < -14.2)
    out['lugs'].append({'theta': [round(l0, 1), round(l1, 1)], 'pocket_inner_z_p50': round(float(np.median(z[pi])), 3),
                        'pocket_inner_z_p5_p95': [round(float(v), 3) for v in np.percentile(z[pi], [5, 95])],
                        'pocket_outer_z_p50': round(float(np.median(z[po])), 3),
                        'pocket_outer_z_p5_p95': [round(float(v), 3) for v in np.percentile(z[po], [5, 95])]})
# inner lug faces: circle fit on all 3 lugs together (faces z -5..-1)
f = vert & (r > 31.0) & (r < 32.4) & (z > -5) & (z < -1) & np.any([win(s + 8, s + 40) for s in starts], axis=0)
cf = fit_circle_irls(c[f, :2], a[f]); out['lug_inner_faces_circle'] = {k: round(float(v), 4) for k, v in cf.items() if isinstance(v, (float, int))}
# bore (gap) circle z -10..0
b = vert & (r > 36.5) & (r < 37.5) & (z > -10) & (z < 0) & np.any([win(s + 62, s + 112) for s in starts], axis=0)
cb = fit_circle_irls(c[b, :2], a[b]); out['bore_gap_circle'] = {k: round(float(v), 4) for k, v in cb.items() if isinstance(v, (float, int))}
fl = up & (r > 24.5) & (r < 30) & (z > -20.6) & (z < -19.3)
out['floor_z_p50'] = round(float(np.median(z[fl]))), 
out['floor_z_p50'] = round(float(np.median(z[fl])), 3); out['floor_z_p5_p95'] = [round(float(v), 3) for v in np.percentile(z[fl], [5, 95])]
out['floor_r_min_scanned'] = round(float(np.percentile(r[fl], 0.5)), 2)
json.dump(out, open('measure/figures/instances.json', 'w'), indent=1); print(json.dumps(out, indent=1))
