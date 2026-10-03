"""D1: housing / G04 / G10 near the panel, by y slices."""
import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent))
from poses import HOUSING, load
from build123d import Box, Pos, Solid
from tools.core import solids, brep_valid, naked_edges

def clip1(so, x0, x1, y0, y1, z0, z1):
    b = Pos((x0+x1)/2, (y0+y1)/2, (z0+z1)/2) * Box(x1-x0, y1-y0, z1-z0)
    try:
        c = Solid(so) & b
    except Exception as e:
        return f"boolean raised {e!r}"
    if c is None: return "None"
    ps = c.solids() if hasattr(c, "solids") else [c]
    out=[]
    for p in ps:
        if p.volume>1e-6:
            bb=p.bounding_box(); out.append((round(p.volume,1),[round(v,2) for v in (bb.min.X,bb.max.X,bb.min.Y,bb.max.Y,bb.min.Z,bb.max.Z)]))
    return out

asm = load("od_g01_assembly_C1_v03.step", HOUSING)
for i, so in enumerate(solids(asm)):
    print("solid", i, "brep_valid", brep_valid(so).measured, brep_valid(so).reason[:120], "naked", naked_edges(so).measured)
    for (y0,y1) in [(170,180),(180,188),(188,195),(195,205)]:
        print("   y", y0, y1, "z>=70:", clip1(so, -130,130, y0,y1, 70,200))
