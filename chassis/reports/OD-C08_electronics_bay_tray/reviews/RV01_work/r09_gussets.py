import sys; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
from build123d import *
from tools.core import read_step
t = read_step(PART)
for f in t.faces():
    n = f.normal_at(f.center())
    if abs(n.X - 0.7071) < 0.01 and abs(n.Y - 0.7071) < 0.01:
        bb = f.bounding_box(); print("hypotenuse", round(bb.min.X,3), round(bb.max.X,3), round(bb.min.Y,3), round(bb.max.Y,3), round(bb.min.Z,3), round(bb.max.Z,3), round(f.area,3))
