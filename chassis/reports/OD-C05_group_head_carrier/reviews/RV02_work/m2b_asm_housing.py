import sys; sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_work")
from common import *
from build123d import Solid, Pos
from tools.core.boolean import common_volume
from tools.measure import mass_properties
g01s = Solid(solids(read_step(G01))[0])
a = read_step(ASM)
h = [Solid(s) for s in solids(a)][1]
out = {}
out["mp_mine"] = mass_properties(g01s, 1000); out["mp_asm"] = mass_properties(h, 1000)
out["common_shift"] = common_volume(Pos(0,0,0.01)*g01s, h)
out["nfaces"] = (len(faces(g01s)), len(faces(h)))
dump("m2b", out); print("ok")
