"""Build the pump, export STEP/STL in the datum frame AND in the original scan
frame (inverse of T1), then re-import both STEPs and verify one closed valid solid."""

import json
import sys
from pathlib import Path

import numpy as np
from build123d import Location, Solid, export_step, export_stl, import_step
from OCP.gp import gp_Trsf

import build_pump

out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
T1 = np.load("T1.npy")
Tinv = np.linalg.inv(T1)
u, _, vt = np.linalg.svd(Tinv[:3, :3])
R = u @ vt  # re-orthonormalise (transform_shape rejects near-orthonormal)
t = Tinv[:3, 3]
tr = gp_Trsf()
tr.SetValues(*R[0], t[0], *R[1], t[1], *R[2], t[2])

part = build_pump.build()
if len(part.solids()) != 1 or not part.is_valid:
    raise SystemExit(f"ABORT: expected 1 valid solid, got {len(part.solids())} (valid={part.is_valid})")
scan_frame = part.moved(Location(tr))

files = {
    "datum": (part, out / "OD-H01_ulka_ep5_pump.step", out / "OD-H01_ulka_ep5_pump.stl"),
    "scan": (scan_frame, out / "OD-H01_ulka_ep5_pump_scanframe.step", out / "OD-H01_ulka_ep5_pump_scanframe.stl"),
}
report = {}
for key, (shape, step, stl) in files.items():
    export_step(shape, str(step))
    export_stl(shape, str(stl), tolerance=0.01, angular_tolerance=0.1)
    back = import_step(str(step))
    solids = back.solids()
    bb = back.bounding_box()
    report[key] = {
        "step": step.name,
        "solids": len(solids),
        "valid": bool(back.is_valid),
        "closed": all(s.is_manifold for s in solids),
        "faces": len(back.faces()),
        "volume_mm3": round(back.volume, 1),
        "area_mm2": round(back.area, 1),
        "bbox_min": [round(v, 3) for v in (bb.min.X, bb.min.Y, bb.min.Z)],
        "bbox_max": [round(v, 3) for v in (bb.max.X, bb.max.Y, bb.max.Z)],
    }
    print(key, report[key])
json.dump({"T1_scan_to_datum": T1.round(9).tolist(), "exports": report}, open(out / "export_check.json", "w"), indent=2)
