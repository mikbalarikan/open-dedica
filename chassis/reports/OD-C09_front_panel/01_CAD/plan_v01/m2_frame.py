"""D1: OD-C10 below y 215, OD-C01 holes and top, carrier/housing/G04 near the panel."""
import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent))
from poses import HOUSING, load
from build123d import Box, Pos, Solid, Compound, Shape
from tools.core import solids
from tools.measure import bore_census

def clip(shape, x0, x1, y0, y1, z0, z1):
    b = Pos((x0+x1)/2, (y0+y1)/2, (z0+z1)/2) * Box(x1-x0, y1-y0, z1-z0)
    out = []
    for so in solids(shape):
        c = Solid(so) & b
        for p in (c.solids() if hasattr(c, 'solids') else [c]):
            if p.volume > 1e-6:
                bb = p.bounding_box(); out.append((round(p.volume,2), [round(v,2) for v in (bb.min.X,bb.max.X,bb.min.Y,bb.max.Y,bb.min.Z,bb.max.Z)]))
    return out

c10 = load("OD-C10_top_panel.step")
print("C10 below y215:", clip(c10, -130,130, 200,215, -310,110))
print("C10 front skirt region z>90:", clip(c10, -130,130, 200,250, 90,110)[:6])
c01 = load("OD-C01_base_frame.step")
bc = bore_census(c01)
print("C01 bores", bc.measured)
for b in bc.detail["bores"]:
    print("  d%.2f start %s end %s through %s" % (b["diameter"], [round(v,2) for v in b["start"]], [round(v,2) for v in b["end"]], b.get("through")))
for name in ("OD-C05_group_head_carrier.step", "od_g01_assembly_C1_v03.step"):
    s = load(name, HOUSING)
    print(name, "z>70:", clip(s, -130,130, -10,260, 70,120))
    print(name, "z>60 |x|>45:", clip(s, -130,-45, -10,260, 60,120), clip(s, 45,130, -10,260, 60,120))
