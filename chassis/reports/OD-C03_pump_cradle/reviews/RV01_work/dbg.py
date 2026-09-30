import sys
sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c03-pump-cradle/reviews/RV01_work")
from checks import load
from build123d import *
from tools.core.shapes import solids, volume_mm3
from tools.core.validity import validity
part, pump, sleeve = load()
def box(x0,x1,y0,y1,z0,z1): return Pos((x0+x1)/2,(y0+y1)/2,(z0+z1)/2)*Box(x1-x0,y1-y0,z1-z0)
b = box(-40,40,37,40,42,42.5)
print(type(b), b.bounding_box())
m = part + b
print(type(m), [ (volume_mm3(s)) for s in solids(m)])
print({k:(v.measured, v.reason, v.detail) for k,v in validity(m).items()})
m2 = part.fuse(b).clean()
print(type(m2), [ (volume_mm3(s)) for s in solids(m2)], {k:(v.measured) for k,v in validity(m2).items()})
