"""D2 probe 2: sections of OD-H01 near the frame end plates, and the X-plate z extents."""
import json
from pathlib import Path
from build123d import Box, Pos
from tools.core import read_step

WS = Path(__file__).resolve().parents[2]
pump = read_step(WS / "00_Spec/inputs/OD-H01_ulka_ep5_pump.step")
out = {}
for z in (-12.3, -10.9, -9.4, -9.2, -8.0, 33.0, 34.6, 36.0, 37.6):
    rows = []
    for s in (pump & (Pos(0, 0, z) * Box(200, 200, 0.02))).solids():
        bb = s.bounding_box()
        rows.append([round(bb.min.X, 3), round(bb.min.Y, 3), round(bb.max.X, 3), round(bb.max.Y, 3), round(s.volume / 0.02, 1)])
    out[z] = sorted(rows)
# the X-plates alone: slab x-range of each plate, full z
for name, (x0, x1) in {"plate-x": (-27.2, -24.1), "plate+x": (23.75, 26.85)}.items():
    probe = Pos((x0 + x1) / 2, 0, 0) * Box(x1 - x0 - 0.02, 200, 300)
    rows = []
    for s in (pump & probe).solids():
        bb = s.bounding_box()
        rows.append([round(v, 3) for v in (bb.min.Y, bb.max.Y, bb.min.Z, bb.max.Z)] + [round(s.volume, 1)])
    out[name + " yz-extent"] = rows
# the +Y side above the plates, between |x| 16 and 30 (post and sector-edge region), for z -12.4..37.65
probe = Pos(0, 16.2 + 10.0, 12.6) * Box(60, 20, 50.05)
rows = []
for s in (pump & probe).solids():
    bb = s.bounding_box()
    rows.append([round(v, 3) for v in (bb.min.X, bb.min.Y, bb.min.Z, bb.max.X, bb.max.Y, bb.max.Z)])
out["material y>16.2"] = rows
print(json.dumps(out, indent=1))
