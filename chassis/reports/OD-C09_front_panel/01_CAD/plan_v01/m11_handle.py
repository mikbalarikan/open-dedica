"""D1 lead: OD-G10 handle where it passes the wall (locked pose), and the basket's reach."""
import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent))
from poses import HOUSING, load
from standin import box
from build123d import Solid
from tools.core import solids
g10 = Solid(solids(load("od_g01_assembly_C1_v03.step", HOUSING))[2])
for z0, z1 in ((84, 94), (93.8, 97.2), (97, 120)):
    c = g10 & box(-130, 130, 0, 260, z0, z1)
    for p in c.solids():
        bb = p.bounding_box(); print(f"z {z0}..{z1}: x {bb.min.X:.2f}..{bb.max.X:.2f} y {bb.min.Y:.2f}..{bb.max.Y:.2f}")
c = g10 & box(-130, 130, 0, 260, -10, 75)
bb = c.bounding_box(); print(f"basket/ears z<75: x {bb.min.X:.2f}..{bb.max.X:.2f} y {bb.min.Y:.2f}..{bb.max.Y:.2f} z {bb.min.Z:.2f}..{bb.max.Z:.2f}")
