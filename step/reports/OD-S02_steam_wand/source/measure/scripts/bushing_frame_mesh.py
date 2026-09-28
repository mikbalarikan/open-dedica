#!/usr/bin/env python3
"""OD-S02 run-local: write the aligned scan re-expressed in the BUSHING frame (z = t along
bush_dir_down from bush_point, x = frame() reference) so stl-re-measure-intent's
pattern_count.py (which counts about datum Z) can count the bushing underside spokes.
Output: measure/figures/bushing_frame.stl (regenerable intermediate)."""
import json, sys
from pathlib import Path
import numpy as np, trimesh
sys.path.insert(0, str(Path(__file__).resolve().parent))
from axfit import frame
run = Path.cwd()
M = json.loads((run / "measure/figures/measurements.json").read_text())
p = np.array(M["bushing"]["axis_used"]["point"]); u, v, d = frame(np.array(M["bushing"]["axis_used"]["direction_down"]))
m = trimesh.load(run / "intake/aligned_work.stl")
T = np.eye(4); T[:3, :3] = np.vstack([u, v, d]); T[:3, 3] = -T[:3, :3] @ p
m.apply_transform(T); m.export(run / "measure/figures/bushing_frame.stl")
print(json.dumps({"x_axis_in_datum": u.tolist(), "y_axis_in_datum": v.tolist(), "z_axis_in_datum": d.tolist()}))
