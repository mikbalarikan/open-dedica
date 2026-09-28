#!/usr/bin/env python3
"""OD-S02 it2 (REVISE route geometry, qa clusters 2+3 of _it1_SUPERSEDED): measure the two
formerly-assumed depths from scan surfaces that it1's verify found inside the CAD.
Writes measure/figures/revise_it2_probe.json. Run from the run folder after
measure/scripts/bushing_frame_mesh.py."""
import json, hashlib, datetime
from pathlib import Path
import numpy as np, trimesh
run = Path.cwd()
P = json.loads((run / "measure/params.json").read_text())["params"]
m = trimesh.load(run / "measure/figures/bushing_frame.stl"); V = m.vertices
ph = P["bush_spoke_phase"]["value"]; tbot = P["bush_bottom"]["value"][1]
r = np.hypot(V[:, 0], V[:, 1]); t = V[:, 2]
rel = ((np.degrees(np.arctan2(V[:, 1], V[:, 0])) - ph + 30) % 60) - 30
win = (r > 4.7) & (r < 6.8) & (t > 0) & (t < 4.8) & (np.abs(rel) > 3)
pT = np.array(P["tip_point"]["value"]); dT = np.array(P["tip_dir_down"]["value"]); pK = np.array(P["bush_point"]["value"])
k0 = float((pK - pT) @ dT)                        # bushing-frame t=0 in tip-axis t
bore = (r > 1.8) & (r < 2.4) & (t > tbot) & (t < 7.0)
out = {"window_surface_t_p1_p5_p50": np.percentile(t[win], [1, 5, 50]).tolist(), "n_window": int(win.sum()),
       "window_depth_below_bottom_from_p1": float(tbot - np.percentile(t[win], 1)),
       "bore_wall_t_min_max": [float(t[bore].min()), float(t[bore].max())], "n_bore": int(bore.sum()),
       "bore_wall_deepest_tip_t": float(k0 + t[bore].min()),   # bushing t grows toward the tip end: min = deepest
       "bore_depth_from_tip_end_needed": float(P["tip_end_t"]["value"] - (k0 + t[bore].min()))}
doc = {"schema": "stl-re/revise_probe@1", "tool": "measure/scripts/revise_it2_probe.py (run-local)", "tool_version": "OD-S02",
       "inputs": {"measure/figures/bushing_frame.stl": hashlib.sha256((run / "measure/figures/bushing_frame.stl").read_bytes()).hexdigest()},
       "seed": 0, "created": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), **out}
(run / "measure/figures/revise_it2_probe.json").write_text(json.dumps(doc, indent=1)); print(json.dumps(out, indent=1))
