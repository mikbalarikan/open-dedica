"""D2 probe of OD-H11: validity, envelope, the two blind screw holes, rearmost surface,
pad radial extents. Writes probe_odh11_v01.json beside this script."""
import json, sys, platform
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
WS = HERE.parents[1]
import build123d, OCP
from tools.core import read_step, validity
from tools.measure import bore_census, locate_bore, envelope, radial_extent, radial_profile

def r2d(r):
    return {"measured": r.measured, "unit": r.unit, "status": r.status, "at": r.at,
            "reason": getattr(r, "reason", None), "detail": r.detail if not isinstance(r.detail, dict) or len(str(r.detail)) < 4000 else "long"}

out = {"python": platform.python_version(), "build123d": build123d.__version__,
       "ocp": getattr(OCP, "__version__", "?")}
shape = read_step(WS / "00_Spec/inputs/OD-H11_thermoblock.step")
out["validity"] = {k: r2d(v) for k, v in validity(shape).items()}
out["envelope"] = {k: v.measured for k, v in envelope(shape).items()}
census = bore_census(shape)
out["bore_count"] = census.measured
out["bores"] = census.detail["bores"]
for name, pt in {"S1": (-19.62, 20.18, 5.5), "S2": (25.01, 9.08, 30.1)}.items():
    loc = locate_bore(census, pt, (0, 0, 1))
    out[name] = {k: r2d(v) for k, v in loc.items()}
json.dump(out, open(HERE / "probe_odh11_v01.json", "w"), indent=1, default=str)
print(json.dumps({k: out[k] for k in ("python","build123d","ocp","validity","envelope","bore_count","S1","S2")}, indent=1, default=str))
