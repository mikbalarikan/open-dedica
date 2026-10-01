from pathlib import Path
from tools.core.step import read_step
from tools.core.shapes import solids, occ
from tools.core.validity import solid_count
s = read_step(Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead/02_STEP_STL/od_c02_bulkhead_C1_v02.step"))
print(type(s), len(solids(s)), solid_count(s).to_dict())
print([x.IsSame(solids(s)[0]) for x in solids(s)], [x.IsEqual(solids(s)[0]) for x in solids(s)])
print(type(occ(s)), getattr(s, 'children', None), len(s.solids()))
