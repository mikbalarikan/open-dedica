"""v02 fact (not a gate): how much of each pass-through's opening the outer gussets block
just behind the wall. A Ø12 disc of thickness 0.1 on each hole's axis, at z -297.9 ..
-297.8 (0.1 behind the 1.0 cutter notch) and at -298.95 .. -298.85 (inside the notch),
intersected with the re-imported panel; area = common volume / 0.1."""
import json, math
from pathlib import Path
from build123d import Align, Cylinder, Pos
from tools.core import common_volume, read_step
WS = Path(__file__).resolve().parents[2]
one = read_step(WS / "02_STEP_STL" / "od_c11_back_C1_v02.step").solids()[0]
out = {}
for name, (x, y) in {"cord_x95_y30": (95.0, 30.0), "tube_x-100_y30": (-100.0, 30.0), "tube_x-84_y30": (-84.0, 30.0)}.items():
    row = {"hole_area_mm2": math.pi * 36.0}
    for tag, z0 in (("behind_notch_z-297.9", -297.9), ("in_notch_z-298.95", -298.95)):
        disc = Pos(x, y, z0) * Cylinder(6.0, 0.1, align=(Align.CENTER, Align.CENTER, Align.MIN))
        cv = common_volume(one, disc)
        row[tag] = {"blocked_mm2": None if cv.measured is None else cv.measured / 0.1, "status": cv.status,
                    "reason": cv.reason}
    out[name] = row
(WS / "01_CAD" / "probe" / "probe_passthrough_block_v02.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
