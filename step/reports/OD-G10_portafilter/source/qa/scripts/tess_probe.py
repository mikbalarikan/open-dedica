#!/usr/bin/env python3
"""QA probe: why is the 0.005 mm / 0.05 rad tessellation of each STEP not watertight?
Tessellates with the same call as step_check.py (_common.step_to_mesh), lists edges not used exactly
twice and zero-area triangles, and re-tests watertightness with the zero-area triangles removed."""
import json, sys, tempfile
from pathlib import Path
import numpy as np
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import header, step_to_mesh, write_json
out = {}
steps = ["build/OD-G11_portafilter_datum.step", "build/OD-G11_portafilter.step"]
for st in steps:
    m = step_to_mesh(st, Path(tempfile.mkdtemp()) / "t.stl")
    eu, ct = np.unique(np.sort(m.edges, axis=1), axis=0, return_counts=True)
    bad = eu[ct != 2]
    deg = m.area_faces < 1e-9
    m2 = m.copy(); m2.update_faces(~deg); m2.remove_unreferenced_vertices()
    out[st] = {"tris": len(m.faces), "watertight": bool(m.is_watertight),
               "edge_use_counts": {int(k): int(v) for k, v in zip(*np.unique(ct, return_counts=True))},
               "non_manifold_or_open_edges": [{"uses": int(c), "p0": m.vertices[e[0]].round(3).tolist(),
                   "len_mm": float(np.linalg.norm(m.vertices[e[0]] - m.vertices[e[1]]))} for e, c in zip(bad, ct[ct != 2])],
               "zero_area_triangles": int(deg.sum()), "zero_area_centres": m.triangles_center[deg].round(3).tolist(),
               "watertight_without_zero_area": bool(m2.is_watertight), "euler_without_zero_area": int(m2.euler_number)}
write_json("qa/tess_watertight_probe.json", {**header("tess_watertight_probe", "qa/scripts/tess_probe.py", steps, None), "steps": out})
print(json.dumps(out, indent=1))
