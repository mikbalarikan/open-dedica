"""Build, export STEP/STL in the datum frame and in the ORIGINAL scan frame (inverse of T),
re-import both STEPs and verify: one closed valid solid, face-type census, no BREP_WITH_VOIDS.

IN : argv[1] output dir (T.npy must sit next to this file)
OUT: OD-H24_flowmeter.step / .stl (datum) and OD-H24_flowmeter_scanframe.step / .stl, export_check.json, params.json
"""

import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from build123d import Location, export_step, export_stl, import_step
from OCP.gp import gp_Trsf

import build_fm

HERE = Path(__file__).resolve().parent
out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
T = np.load(HERE / "T.npy")
Ti = np.linalg.inv(T)
u, _, vt = np.linalg.svd(Ti[:3, :3])
R = u @ vt  # re-orthonormalise (gp_Trsf rejects near-orthonormal)
t = Ti[:3, 3]
tr = gp_Trsf()
tr.SetValues(*R[0], t[0], *R[1], t[1], *R[2], t[2])

part = build_fm.build()
if len(part.solids()) != 1 or not part.is_valid:
    raise SystemExit(f"ABORT: expected 1 valid solid, got {len(part.solids())} (valid={part.is_valid})")
files = {"datum": (part, "OD-H24_flowmeter.step", "OD-H24_flowmeter.stl"),
         "scan": (part.moved(Location(tr)), "OD-H24_flowmeter_scanframe.step", "OD-H24_flowmeter_scanframe.stl")}
rep = {}
for k, (shape, step, stl) in files.items():
    export_step(shape, str(out / step))
    export_stl(shape, str(out / stl), tolerance=0.01, angular_tolerance=0.1)
    back = import_step(str(out / step))
    so = back.solids()
    bb = back.bounding_box()
    txt = (out / step).read_text(errors="ignore")
    rep[k] = dict(step=step, solids=len(so), valid=bool(back.is_valid), closed=all(s.is_manifold for s in so),
                  faces=len(back.faces()), surface_types=dict(Counter(f.geom_type.name for f in back.faces())),
                  volume_mm3=round(back.volume, 1), area_mm2=round(back.area, 1),
                  bbox_min=[round(v, 3) for v in (bb.min.X, bb.min.Y, bb.min.Z)],
                  bbox_max=[round(v, 3) for v in (bb.max.X, bb.max.Y, bb.max.Z)],
                  size_MB=round((out / step).stat().st_size / 1e6, 2),
                  step_BREP_WITH_VOIDS=txt.count("BREP_WITH_VOIDS"), step_CLOSED_SHELL=txt.count("CLOSED_SHELL("),
                  step_MANIFOLD_SOLID_BREP=txt.count("MANIFOLD_SOLID_BREP("))
    print(k, rep[k])
json.dump({"T_scan_to_datum": T.round(9).tolist(), "exports": rep}, open(out / "export_check.json", "w"), indent=2)
json.dump(build_fm.P, open(out / "params.json", "w"), indent=1)
