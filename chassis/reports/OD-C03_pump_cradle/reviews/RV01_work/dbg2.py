import sys
sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c03-pump-cradle/reviews/RV01_work")
from checks import load, run
from build123d import *
from tools.core.shapes import solids, volume_mm3
from tools.measure import bore_census, clearance
part, pump, sleeve = load()
def box(x0,x1,y0,y1,z0,z1): return Pos((x0+x1)/2,(y0+y1)/2,(z0+z1)/2)*Box(x1-x0,y1-y0,z1-z0)
m = part + box(-40,40,37,40,42,42.5)
print("alone", bore_census(m).measured, clearance(m, pump).measured)
c = Compound([part, box(50,52,0,2,0,2)])
print("part after compound", bore_census(part).measured, clearance(part, pump).measured, part.location, part.parent is not None)
m = part + box(-40,40,37,40,42,42.5)
print("after", bore_census(m).measured, clearance(m, pump).measured, [volume_mm3(s) for s in solids(m)])
