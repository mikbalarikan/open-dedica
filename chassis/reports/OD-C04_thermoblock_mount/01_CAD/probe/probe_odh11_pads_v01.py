"""D2 probe 4: material stretches on the rays at the pad angles, by level."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
WS = HERE.parents[1]
from tools.core import read_step
from tools.measure import radial_extent
tb = read_step(WS / "00_Spec/inputs/OD-H11_thermoblock.step")
out = {}
for ang in (262.5, 339.0):
    for z in (1.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 47.0):
        r = radial_extent(tb, (0, 0, 0), (0, 0, 1), (1, 0, 0), ang, z)
        out[f"{ang}@{z}"] = {"mm": r.measured, "status": r.status, "stretches": r.detail.get("material") if r.detail else None}
        print(ang, z, round(r.measured, 3) if r.measured is not None else None, r.status,
              [[round(a, 2) for a in s] if isinstance(s, (list, tuple)) else s for s in (r.detail or {}).get("material", [])], flush=True)
json.dump(out, open(HERE / "probe_odh11_pads_v01.json", "w"), indent=1, default=str)
