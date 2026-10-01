"""D6 screening sections of od_c05_carrier v03 (concept C4, closed column) from the
exported STEP files (nothing clipped, L-04)."""
import json
from pathlib import Path

from tools.core import read_step
from tools.drawing import write_sections

WS = Path(__file__).resolve().parents[1]
OUT = WS / "03_Sections"
part = read_step(WS / "02_STEP_STL/od_c05_carrier_C4_v03.step").solids()[0]
asm = read_step(WS / "02_STEP_STL/od_c05_assembly_C4_v03.step")
PLANES = [  # (name, shape, view whose line of sight is the plane normal, point on the plane)
    ("od_c05_carrier_y0", part, "front", (0.0, 0.0, 75.0)),          # plate over the hub window, gusset pair behind
    ("od_c05_carrier_ym80", part, "front", (0.0, -80.0, 75.0)),      # column, tent ridge, hatch
    ("od_c05_carrier_x0", part, "left", (0.0, -26.0, 75.0)),         # hub window, hatch, rear window, tent
    ("od_c05_carrier_x35", part, "left", (35.0, -26.0, 75.0)),       # foot holes and counterbores
    ("od_c05_carrier_x53", part, "left", (53.0, -26.0, 75.0)),       # side wall and a gusset
    ("od_c05_carrier_zm27p44", part, "top", (0.0, -26.0, -27.44)),   # plate plan
    ("od_c05_carrier_z165", part, "top", (0.0, -26.0, 165.0)),       # foot plan through the tent
    ("od_c05_assembly_y0", asm, "front", (0.0, 0.0, 75.0)),          # carrier, OD-G01, OD-G04 as placed
    ("od_c05_assembly_x0", asm, "left", (0.0, -26.0, 75.0)),
]
log = {}
for name, shape, view, through in PLANES:
    try:
        for w in write_sections(shape, OUT, part=name, version=3, views=(view,), through=through):
            nc = w.checks["nothing_clipped"]
            log[w.path.name] = {"sha256": w.sha256, "plane": view, "through": through,
                                "nothing_clipped": nc.measured, "status": nc.status, "reason": nc.reason}
    except Exception as exc:   # noqa: BLE001
        log[name] = {"error": f"{type(exc).__name__}: {exc}"}
(WS / "01_CAD/sections_od_c05_carrier_v03.json").write_text(json.dumps(log, indent=1))
print(json.dumps(log, indent=1))
