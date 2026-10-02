import sys
sys.path.insert(0, "/root/oguz-jobs/20261002-od-c14-cord-grommet/reviews/RV01_work")
from common import *
from build123d import Compound, Axis, Location
from tools.drawing.write import write_sections
A = half(); B = A.rotate(Axis((95,30,0),(0,0,1)), 180)
P = c11() & box(78, 112, -2, 50, -306, -286); F = c01() & box(78, 112, -8, 0, -306, -286)
cord = cyl(95, 30, 3.5, -312, -284); tie = ring(95, 30, 5.15, 6.45, -298.8, -294.0); head = box(92.5, 97.5, 36.45, 42.45, -298.8, -293.8)
asm = Compound(children=[P, F, A, B, cord, tie, head])
out = W/"reviews/RV01_work/sections"
for w in write_sections(asm, out, part="rv01_assembly_open", version=1, through=(95, 30.0001, -296.6)):
    print(w.path, w.checks["nothing_clipped"].measured)
for w in write_sections(A, out, part="rv01_half", version=1, through=(95, 32, -296.6)):
    print(w.path, w.checks["nothing_clipped"].measured)
# closed pose
a = A.moved(Location((0,-0.4,0))); b = B.moved(Location((0,0.4,0)))
asm2 = Compound(children=[P, a, b, cord, tie])
for w in write_sections(asm2, out, part="rv01_assembly_closed", version=1, views=("left","top"), through=(95, 30.0001, -296.6)):
    print(w.path, w.checks["nothing_clipped"].measured)
