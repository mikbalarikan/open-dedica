from pathlib import Path
from tools.core import read_step
from tools.core.shapes import solids, occ
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SOLID
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle")
p = read_step(W/"02_STEP_STL/od_c03_cradle_C1_v01.step")
s = solids(p)
print(len(s), [x.IsSame(s[0]) for x in s], [x.IsPartner(s[0]) for x in s])
print(type(p), p.label, [ (c.label, type(c)) for c in getattr(p,'children',[])])
print(len(p.solids()))
