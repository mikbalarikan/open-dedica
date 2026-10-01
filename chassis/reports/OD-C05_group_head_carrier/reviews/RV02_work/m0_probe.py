import sys; sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_work")
from common import *
from build123d import Solid
c = read_step(STEP)
print(type(c), len(solids(c)))
s = Solid(solids(c)[0]); print(type(s), len(solids(s)), s.volume)
from tools.core.validity import solid_count
print(solid_count(s).measured, solid_count(c).measured)
