"""WP-02 probe (J2): can min_wall and overhang_census sample a 240 x 405 x 6 slab (the
plate's size, R 10 corners, one dia 4.0 hole) at their default spacing (refused: 0.63 mm fits) and at 0.7 mm (this run), and how long do
they take. A diagnostic for the plan's risk list, not a gate. Paths relative to the workspace."""
import json, time
from pathlib import Path
from build123d import Box, Cylinder, Location, fillet, Axis
from tools.measure import min_wall, overhang_census

WS = Path(__file__).resolve().parents[2]
slab = Box(240, 6, 405).moved(Location((0, -3, -102.5)))
slab = fillet(slab.edges().filter_by(Axis.Y), 10)
slab = slab - Cylinder(2.0, 10).moved(Location((35, -3, -40), (90, 0, 0)))
out = {}
for name, fn in (("min_wall", lambda: min_wall(slab, spacing=0.7)), ("overhang_census", lambda: overhang_census(slab, build_dir=(0, 1, 0), spacing=0.7))):
    t = time.time()
    r = fn()
    out[name] = {"measured": r.measured, "status": r.status, "reason": r.reason, "seconds": round(time.time() - t, 1),
                 "params": {k: v for k, v in (r.params or {}).items()},
                 "detail_keys": sorted((r.detail or {}).keys())}
    if name == "min_wall":
        out[name]["wide"] = (r.detail or {}).get("wide")
print(json.dumps(out, indent=1, default=str))
(WS / "01_CAD" / "probe" / "probe_sampling_v01.json").write_text(json.dumps(out, indent=1, default=str))
