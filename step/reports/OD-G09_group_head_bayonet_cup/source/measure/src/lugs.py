"""Run-local: angular extents and levels of the 3 bayonet lugs and related sector features
(full-res scan, datum frame, theta CCW about +Z from +X). Writes measure/figures/lugs.json."""
import json, numpy as np, trimesh
m = trimesh.load('input/scan.stl'); T = np.array(json.load(open('intake/alignment.json'))['matrix_4x4']); m.apply_transform(T)
c = m.triangles_center; n = m.face_normals; a = m.area_faces
r = np.hypot(c[:, 0], c[:, 1]); th = np.degrees(np.arctan2(c[:, 1], c[:, 0])) % 360
def occ(sel, step=0.5):
    """occupied theta bins (area > tiny)"""
    b = np.zeros(int(360 / step), bool)
    idx = (th[sel] // step).astype(int)
    w = np.bincount(idx, weights=a[sel], minlength=len(b))
    return w > 0.02 * step
def runs(b, step=0.5, min_len=1.5):
    """runs of True in circular boolean array -> [(start_deg, end_deg)]"""
    out = []; N = len(b)
    if b.all(): return [(0.0, 360.0)]
    k0 = int(np.argmin(b))  # start at a False
    i = 0
    while i < N:
        j = (k0 + i) % N
        if b[j]:
            s = i
            while i < N and b[(k0 + i) % N]: i += 1
            st = ((k0 + s) * step) % 360; en = ((k0 + i) * step) % 360
            if (i - s) * step >= min_len: out.append((round(st, 1), round(en, 1)))
        else: i += 1
    return sorted(out)
up = n[:, 2] > 0.85; vert = np.abs(n[:, 2]) < 0.35
res = {}
res['lug_top'] = runs(occ(up & (r > 31.9) & (r < 34.0) & (np.abs(c[:, 2]) < 0.4)))
res['channel_floor'] = runs(occ(up & (r > 35.0) & (r < 36.6) & (np.abs(c[:, 2] + 2.9) < 0.3)))
res['closed_end_top'] = runs(occ(up & (r > 35.0) & (r < 36.6) & (np.abs(c[:, 2]) < 0.4)), min_len=1.0)
res['stop_face_below_-8'] = runs(occ(vert & (r > 31.0) & (r < 32.4) & (c[:, 2] < -8) & (c[:, 2] > -11.5)), min_len=1.0)
res['rim_lip_top'] = runs(occ(up & (r > 37.5) & (r < 38.2) & (c[:, 2] > 3.0)), min_len=1.0)
res['rim_ledge_at_lip_radius'] = runs(occ(up & (r > 37.5) & (r < 38.2) & (np.abs(c[:, 2] - 2.55) < 0.25)), min_len=1.0)
res['pocket_inner_floor'] = runs(occ(up & (r > 31.9) & (r < 33.6) & (c[:, 2] < -15.6) & (c[:, 2] > -17.5)))
res['shelf_inner_band'] = runs(occ(up & (r > 31.9) & (r < 33.6) & (c[:, 2] > -15.0) & (c[:, 2] < -13.0)))
# lug inner face radius and bottom edge z(theta)
lugs = []
for (s, e) in res['lug_top']:
    span = (e - s) % 360; mid = (s + span / 2) % 360
    def inwin(t0, t1): return ((th - t0) % 360) < ((t1 - t0) % 360)
    fsel = vert & (r > 30.8) & (r < 32.6) & (c[:, 2] < -0.8) & (c[:, 2] > -11.5) & inwin(s, e)
    rin = float(np.median(r[fsel]))
    prof = []
    for k in np.arange(0, span, 2.0):
        t = fsel & inwin((s + k) % 360, (s + k + 2) % 360)
        if t.sum() > 5: prof.append([round(float(k + 1), 1), round(float(np.percentile(c[t, 2], 1)), 2)])
    osel = vert & (r > 33.8) & (r < 35.2) & (c[:, 2] < -0.5) & (c[:, 2] > -2.7) & inwin(s, e)
    lugs.append({'top_theta': [s, e], 'span_deg': round(span, 1), 'mid_deg': round(mid, 1),
                 'inner_face_r_p50': round(rin, 3), 'inner_face_r_p5_p95': [round(float(x), 3) for x in np.percentile(r[fsel], [5, 95])],
                 'channel_inner_wall_r_p50': round(float(np.median(r[osel])), 3) if osel.sum() > 20 else None,
                 'inner_face_bottom_z_vs_dtheta_from_start': prof})
res['lugs'] = lugs
json.dump(res, open('measure/figures/lugs.json', 'w'), indent=1)
for k, v in res.items():
    if k != 'lugs': print(k, v)
for L in lugs: print({k: v for k, v in L.items() if k != 'inner_face_bottom_z_vs_dtheta_from_start'}); print('   bottom', L['inner_face_bottom_z_vs_dtheta_from_start'])
