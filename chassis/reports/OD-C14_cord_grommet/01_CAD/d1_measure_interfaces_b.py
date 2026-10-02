"""D1 interface measurement, part b: OD-C11's inner-side features (floor flange, gussets) against the planned grommet, tie and head envelopes."""
import json
from pathlib import Path
from build123d import Box, Pos, Cylinder, GeomType, Rot
from tools.core import read_step
from tools.measure import clearance, envelope

WS = Path(__file__).resolve().parents[1]
c11 = read_step(WS / "00_Spec/inputs/OD-C11_back_panel.step")
inner = c11 & (Pos(95, 20, -288.95) * Box(80, 40, 20.1))   # z -298.995 .. -278.9: everything inside the wall's inner face
def r(res): return [round(res.measured, 4) if isinstance(res.measured, float) else res.measured, str(res.status), res.at]
out = {}
out["inner_env"] = {k: v.measured for k, v in envelope(inner).items()}
fs = []
for f in inner.faces():
    bb = f.bounding_box()
    fs.append((str(f.geom_type)[9:], [round(v, 3) for v in (bb.min.X, bb.min.Y, bb.min.Z, bb.max.X, bb.max.Y, bb.max.Z)]))
out["inner_faces"] = fs
inside_body = Pos(95, 30, -295.1) * Cylinder(5.7, 8.2)          # neck tail, groove, collar envelope inside the wall
tie = Pos(95, 30, -296.6) * (Cylinder(6.4, 4.8) - Cylinder(5.1, 4.8))
out["inside_body_to_inner_features"] = r(clearance(inside_body, inner))
out["tie_to_inner_features"] = r(clearance(tie, inner))
for zlo in (-299.1, -299.0, -298.5):
    head = Pos(95, 30 + 6.4 + 2.5, zlo + 2.5) * Box(5, 5, 5)
    out[f"head5_from_z{zlo}_to_c11"] = r(clearance(head, c11))
head_down = Pos(95, 30 - 6.4 - 2.5, -296.6) * Box(5, 5, 4.8)
out["head_downward_to_c11"] = r(clearance(head_down, c11))
print(json.dumps(out, indent=1, default=str))
