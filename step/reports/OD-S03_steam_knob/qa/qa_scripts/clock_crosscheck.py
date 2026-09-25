"""QA-own clock cross-check (not a skill script): area-weighted Fourier n=1 and lever-flank
plane bisector, both on the RAW scan, expressed in the QA-audited frame (qa/datum_audit.json T_qa).
Builder matrix used only to select regions."""
import json, numpy as np, trimesh
m = trimesh.load('input/scan.stl')
Tb = np.array(json.load(open('intake/alignment.json'))['matrix_4x4'])
Tq = np.array(json.load(open('qa/datum_audit.json'))['T_qa'])
Cb = m.triangles_center @ Tb[:3,:3].T + Tb[:3,3]; Nb = m.face_normals @ Tb[:3,:3].T
Cq = m.triangles_center @ Tq[:3,:3].T + Tq[:3,3]; A = m.area_faces
r = np.hypot(Cb[:,0], Cb[:,1]); out = {}
s = (r > 16) & (r < 28.5)
out['fourier_area_weighted_deg'] = float(np.degrees(np.angle((A[s]*np.exp(1j*np.arctan2(Cq[s,1], Cq[s,0]))).sum())))
V = m.vertices @ Tq[:3,:3].T + Tq[:3,3]; rv = np.hypot(*(m.vertices @ Tb[:3,:3].T + Tb[:3,3])[:, :2].T)
sv = (rv > 16) & (rv < 28.5)
out['fourier_vertex_count_deg'] = float(np.degrees(np.angle(np.exp(1j*np.arctan2(V[sv,1], V[sv,0])).sum())))
ang = []
for sg in (+1, -1):
    f = (Cb[:,0] > 15) & (Cb[:,0] < 24) & (Cb[:,2] > 3) & (Cb[:,2] < 12) & (sg*Nb[:,1] > 0.95) & (sg*Cb[:,1] > 3.5)
    P = m.vertices[m.faces[f]].reshape(-1,3) @ Tq[:3,:3].T + Tq[:3,3]
    c = P.mean(0); _, sv_, vt = np.linalg.svd(P - c, full_matrices=False); n = vt[2]; n = n*np.sign(n[1])*sg
    res = (P - c) @ vt[2]
    a = float(np.degrees(np.arctan2(-n[0]*sg, n[1]*sg)))  # flank direction angle about Z from +X (plan)
    out[f'flank_{"py" if sg>0 else "my"}'] = {'faces': int(f.sum()), 'rms': float(np.sqrt((res**2).mean())), 'plan_angle_deg': a, 'normal': n.tolist()}
    ang.append(a)
out['flank_bisector_deg_in_QA_frame'] = float(np.mean(ang))
Tq_in_b = Tb @ np.linalg.inv(Tq)
out['QA_vs_builder_clock_deg'] = float(np.degrees(np.arctan2(Tq_in_b[1,0], Tq_in_b[0,0])))
json.dump(out, open('qa/clock_crosscheck.json','w'), indent=1); print(json.dumps(out, indent=1))
