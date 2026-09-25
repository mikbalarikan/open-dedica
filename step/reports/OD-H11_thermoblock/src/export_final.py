"""Build, export STEP/STL in datum + original scan frame, re-import and verify one closed valid solid."""
import json, sys
from collections import Counter
from pathlib import Path
import numpy as np
from build123d import Location, export_step, export_stl, import_step
from OCP.gp import gp_Trsf
import build_ft
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
T = np.load("T.npy"); Ti = np.linalg.inv(T); u, _, vt = np.linalg.svd(Ti[:3, :3]); R = u @ vt; t = Ti[:3, 3]
tr = gp_Trsf(); tr.SetValues(*R[0], t[0], *R[1], t[1], *R[2], t[2])
part = build_ft.build()
if len(part.solids()) != 1 or not part.is_valid:
    raise SystemExit("ABORT: not one valid solid")
files = {"datum": (part, "OD-H11_thermoblock.step", "OD-H11_thermoblock.stl"),
         "scan": (part.moved(Location(tr)), "OD-H11_thermoblock_scanframe.step", "OD-H11_thermoblock_scanframe.stl")}
rep = {}
for k, (shape, step, stl) in files.items():
    export_step(shape, str(out / step)); export_stl(shape, str(out / stl), tolerance=0.01, angular_tolerance=0.1)
    back = import_step(str(out / step)); so = back.solids(); bb = back.bounding_box()
    rep[k] = dict(step=step, solids=len(so), valid=bool(back.is_valid), closed=all(s.is_manifold for s in so),
                  faces=len(back.faces()), surface_types=dict(Counter(str(f.geom_type).split(".")[-1] for f in back.faces())),
                  volume_mm3=round(back.volume, 1), bbox_min=[round(v, 3) for v in (bb.min.X, bb.min.Y, bb.min.Z)],
                  bbox_max=[round(v, 3) for v in (bb.max.X, bb.max.Y, bb.max.Z)], size_MB=round((out / step).stat().st_size / 1e6, 2))
    print(k, rep[k])
json.dump({"T_scan_to_datum": T.round(9).tolist(), "exports": rep}, open(out / "export_check.json", "w"), indent=2)
