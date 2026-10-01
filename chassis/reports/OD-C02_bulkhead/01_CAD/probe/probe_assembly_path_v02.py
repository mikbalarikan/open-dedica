"""D6 / L-10 diagnostic: the bulkhead's assembly path. It is lowered along -Y onto the
plate, so the space it sweeps from far above to its final pose is its own footprint
(x 59 .. 71, z -240 .. -30, measured from the re-imported STEP) extruded from y 0 up
to y 400. The clearance from that swept box to each wet neighbour as placed in the
check assembly STEP is the least clearance along the whole path. Writes
probe_assembly_path_v02.json. Not a gate row (U-03 (b) is N/A); reported in REPORT section 6."""
import json
from pathlib import Path

from build123d import Align, Box, Pos

from tools.core import read_step
from tools.measure import clearance, envelope

HERE = Path(__file__).resolve().parent
WS = HERE.parents[1]
Y_TOP = 400.0
asm = read_step(WS / "02_STEP_STL/od_c02_assembly_C1_v02.step")
kids = {c.label: c for c in asm.children}
bh = kids["od_c02_bulkhead"]
env = {k: v.measured for k, v in envelope(bh).items()}
x0, x1, z0, z1 = env["min_x"], env["max_x"], env["min_z"], env["max_z"]
swept = Pos(x0, env["min_y"], z0) * Box(x1 - x0, Y_TOP - env["min_y"], z1 - z0,
                                        align=(Align.MIN, Align.MIN, Align.MIN))
out = {"swept_box": {"x": [x0, x1], "y": [env["min_y"], Y_TOP], "z": [z0, z1]}, "clearance_mm": {}}
for label in ("od_c03_cradle", "od_h01_pump", "od_c04_mount", "od_h11_thermoblock", "od_g01_housing",
              "od_c05_foot_reference_A02"):
    r = clearance(swept, kids[label])
    out["clearance_mm"][label] = {"measured": r.measured, "at": r.at, "status": r.status, "reason": r.reason}
(HERE / "probe_assembly_path_v02.json").write_text(json.dumps(out, indent=1, default=str))
print(json.dumps(out, indent=1, default=str))
