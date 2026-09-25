"""QA-own probe (adapted from _it1_SUPERSEDED/qa/qa_scripts/tess_probe.py): tessellate BOTH it1 and it2
STEPs (datum + scan frame) at several linear/angular settings and count open / non-manifold edges.
step_check.py tessellates only at 0.005/0.05 and does not fold watertightness into validity (known defect).
Scan-frame meshes are mapped to the datum frame with intake/alignment.json for locating defects."""
import sys, json, tempfile, os, numpy as np, trimesh
sys.path.insert(0, '/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts')
from _common import step_to_mesh, sha256_file
T = np.array(json.load(open('intake/alignment.json'))['matrix_4x4'])
SETTINGS = [(0.005, 0.1), (0.005, 0.05), (0.01, 0.1), (0.01, 0.05), (0.003, 0.1), (0.02, 0.1)]
FILES = [('it1', '_it1_SUPERSEDED/build/OD-S03_steam-knob_datum.step', np.eye(4)),
         ('it1', '_it1_SUPERSEDED/build/OD-S03_steam-knob.step', T),
         ('it2', 'build/OD-S03_steam-knob_datum.step', np.eye(4)),
         ('it2', 'build/OD-S03_steam-knob.step', T)]
out = {'schema': 'stl-re/tess_probe@1', 'tool': 'qa_scripts/tess_probe.py (QA-own)', 'seed': None,
       'inputs': {f: sha256_file(f) for _, f, _ in FILES}, 'settings': SETTINGS, 'results': []}
for it, f, M in FILES:
    for tol, ang in SETTINGS:
        tmp = tempfile.mktemp(suffix='.stl')
        m = step_to_mesh(f, tmp, tolerance=tol, angular_tolerance=ang); os.remove(tmp)
        m.apply_transform(M)
        u, c = np.unique(m.edges_sorted, axis=0, return_counts=True)
        bad = u[c != 2]
        P = m.vertices[bad].mean(1) if len(bad) else np.zeros((0, 3))
        locs = [{'xyz': p.round(3).tolist(), 'r': round(float(np.hypot(p[0], p[1])), 3),
                 'theta_deg': round(float(np.degrees(np.arctan2(p[1], p[0])) % 360), 1)} for p in P[:40]]
        rec = {'iteration': it, 'step': f, 'tolerance_mm': tol, 'angular_rad': ang, 'tris': int(len(m.faces)),
               'watertight': bool(m.is_watertight), 'winding_consistent': bool(m.is_winding_consistent),
               'open_edges': int((c == 1).sum()), 'nonmanifold_edges': int((c > 2).sum()),
               'components': int(len(m.split(only_watertight=False))) if len(m.faces) < 2_000_000 else None,
               'volume_mm3': float(m.volume) if m.is_watertight else None,
               'defect_locations_datum_frame': locs}
        out['results'].append(rec)
        print(it, os.path.basename(f), tol, ang, 'tris', rec['tris'], 'wt', rec['watertight'],
              'open', rec['open_edges'], 'nm', rec['nonmanifold_edges'], locs[:2], flush=True)
json.dump(out, open('qa/tess_probe.json', 'w'), indent=1)
