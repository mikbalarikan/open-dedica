"""QA run-local supplement to datum_audit.py (report-only): per-station IRLS circle centres of the
nozzle OD (z -22..-15, 0.5 mm stations) in the builder datum frame, line fit of centre vs z, and
the literal 'nozzle axis ∩ band plane' point extrapolated to z=0 along the tilted axis."""
import sys, json, numpy as np
sys.path.insert(0, '/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts')
from _common import load_mesh, load_matrix, header, write_json
from datum_audit import circle_irls
RUN = sys.argv[1]
m = load_mesh(f'{RUN}/input/scan.stl'); m.apply_transform(load_matrix(f'{RUN}/intake/alignment.json'))
C, N, A = m.triangles_center, m.face_normals, m.area_faces
rows = []
for z0 in np.arange(-22.0, -14.99, 0.5):
    s = (np.abs(C[:, 2] - z0) < 0.25) & (np.hypot(C[:, 0], C[:, 1]) > 5.3) & (np.hypot(C[:, 0], C[:, 1]) < 6.3) & (np.abs(N[:, 2]) < 0.3)
    c, R, rms = circle_irls(C[s, :2], A[s])
    rows.append([z0, c[0], c[1], R, rms, int(s.sum())])
rows = np.array(rows)
px = np.polyfit(rows[:, 0], rows[:, 1], 1); py = np.polyfit(rows[:, 0], rows[:, 2], 1)
tilt = float(np.degrees(np.arctan(np.hypot(px[0], py[0]))))
at0 = [float(px[1]), float(py[1])]; atmid = [float(np.polyval(px, -18.5)), float(np.polyval(py, -18.5))]
out = {**header('datum_supplement', 'qa/src/datum_supplement.py', [f'{RUN}/input/scan.stl', f'{RUN}/intake/alignment.json'], None),
       'stations': [dict(zip(['z', 'cx', 'cy', 'R', 'rms', 'n_faces'], map(float, r))) for r in rows],
       'axis_tilt_deg': tilt, 'centre_at_mid_station_z-18.5': atmid, 'centre_extrapolated_to_z0': at0,
       'offset_mid_mm': float(np.hypot(*atmid)), 'offset_extrapolated_z0_mm': float(np.hypot(*at0)),
       'note': 'report-only. Builder origin = nozzle axis centre at the station mid (projected along the band normal), not the literal intersection of the tilted axis with z=0; the literal intersection lies offset_extrapolated_z0_mm away. ICP delta and deviation are unaffected (they do not use the origin definition).'}
write_json(f'{RUN}/qa/datum_supplement.json', out)
print(json.dumps({k: out[k] for k in ('axis_tilt_deg', 'centre_at_mid_station_z-18.5', 'centre_extrapolated_to_z0', 'offset_mid_mm', 'offset_extrapolated_z0_mm')}, indent=1))
