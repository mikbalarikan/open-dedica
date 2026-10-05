"""RV02 print, wall, round-trip and mesh checks on the delivered STEP and STL."""
import json, math, time
from pathlib import Path
from build123d import Cylinder, Location, Rotation
from tools.core import step as st
from tools.core.validity import validity
from tools.core.mesh import write_stl, mesh_sagitta
from tools.measure import (min_wall, min_wall_wide, overhang_census, flat_ceiling_spans,
                           mesh_census, mesh_deviation, min_wall_mesh)
W = Path("/root/oguz-jobs/20261002-od-t01-pressure-test-rig"); OUT = W / "reviews/RV02_work"
P = W / "02_STEP_STL/od_t01_rig_C1_v02.step"; STL = W / "02_STEP_STL/od_t01_rig_C1_v02.stl"
rig = st.read_step(P)
R = {}
def rd(r): return {"measured": r.measured, "unit": r.unit, "at": r.at, "status": r.status, "reason": r.reason,
                   "detail": {k: v for k, v in r.detail.items() if k in ("wide", "gated_mm", "per_kind_least_deg", "sampling_bound_deg", "below_min_deg", "largest_step_mm", "bed_samples", "ceilings")}}
t = time.time()
R["min_wall"] = rd(min_wall(rig)); print("min_wall", R["min_wall"], time.time() - t, flush=True)
R["min_wall_wide"] = rd(min_wall_wide(rig)); print("wide", R["min_wall_wide"], flush=True)
R["overhang_raw"] = rd(overhang_census(rig, build_dir=(0, 0, 1), min_deg=45)); print("ovh raw", R["overhang_raw"], flush=True)
# plugged copy: the four 3.4 holes filled with r 1.8 cylinders y 135..140 (my own plug)
plugged = rig
for x in (-44, 44):
    for z in (-44, 44):
        c = Location((x, 137.5, z)) * Rotation(-90, 0, 0) * Cylinder(1.8, 5.0)
        plugged = plugged + c
print("plugged validity", {k: v.measured for k, v in validity(plugged).items()}, flush=True)
R["overhang_plugged"] = rd(overhang_census(plugged, build_dir=(0, 0, 1), min_deg=45)); print("ovh plugged", R["overhang_plugged"], flush=True)
R["bridge"] = rd(flat_ceiling_spans(rig, build_dir=(0, 0, 1), max_span=5.0)); print("bridge", R["bridge"], flush=True)
# round trip: re-export the read solid and compare
rt = st.step_roundtrip(rig.solids()[0] if False else rig, OUT / "rt_v02.step", timestamp="2026-10-03T00:00:00")
R["roundtrip"] = {k: (v.measured, v.status, v.reason) for k, v in rt.items()}; print("rt", R["roundtrip"], flush=True)
# mesh: reviewer re-mesh at 0.01 / 0.10
wr = write_stl(rig, OUT / "remesh_v02.stl", tolerance=0.01, angular_tolerance=0.10)
R["remesh"] = str(wr)
R["sagitta"] = rd(mesh_sagitta(rig)); print("sagitta", R["sagitta"], flush=True)
R["stl_sha_delivered"] = st.file_sha256(STL); R["stl_sha_remesh"] = st.file_sha256(OUT / "remesh_v02.stl")
R["mesh_census"] = {k: v.measured for k, v in mesh_census(STL).items()}
R["mesh_deviation"] = rd(mesh_deviation(STL, rig))
R["min_wall_mesh"] = rd(min_wall_mesh(STL))
R["angular_limit"] = 4 * math.acos(1 - 0.01 / 30)
print({k: R[k] for k in ("stl_sha_delivered", "stl_sha_remesh", "mesh_census", "mesh_deviation", "min_wall_mesh", "angular_limit", "remesh")}, flush=True)
(OUT / "part_print.json").write_text(json.dumps(R, indent=1, default=str))
