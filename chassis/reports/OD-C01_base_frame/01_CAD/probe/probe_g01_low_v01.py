"""WP-02 probe (J2): where OD-G01 v02, placed at (0, 175, 0), reaches its lowest y, and the
lowest y of its material in z bands (the spec section 4 states 'lowest point at y 131.9').
Paths relative to the workspace."""
import json
from pathlib import Path
from build123d import Box, Location
from tools.core import read_step
from tools.measure import envelope

WS = Path(__file__).resolve().parents[2]
g01 = read_step(WS / "00_Spec" / "inputs" / "OD-G01_housing_C1_v02.step").moved(Location((0, 175, 0)))
out = {}
def band(z0, z1, xabs=None):
    x0, x1 = (-200, 200) if xabs is None else (-xabs, xabs)
    b = Box(x1 - x0, 400, z1 - z0).moved(Location(((x0 + x1) / 2, 175, (z0 + z1) / 2)))
    c = g01 & b
    if not c or not c.solids():
        return None
    e = envelope(c)
    return {k: round(e[k].measured, 4) for k in ("min_y", "max_y", "min_x", "max_x", "min_z", "max_z")}
for z0, z1 in ((-24.94, -19.94), (-19.94, -15.0), (-15.0, -10.0), (-10.0, -5.0), (-5.0, 0.0), (0.0, 3.30), (-19.94, 3.30)):
    out[f"z {z0}..{z1}"] = band(z0, z1)
out["z -19.94..3.30, |x| <= 30"] = band(-19.94, 3.30, 30)
out["z -24.94..3.30, |x| <= 20"] = band(-24.94, 3.30, 20)
print(json.dumps(out, indent=1))
(WS / "01_CAD" / "probe" / "probe_g01_low_v01.json").write_text(json.dumps(out, indent=1))
