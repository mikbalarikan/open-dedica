import sys; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
from build123d import *
from tools.core import read_step, common_volume, validity
t = Solid(read_step(PART).wrapped)
e = read_step(E01).solids()[0]
board = e.moved(Location(Plane(origin=(84.0, 80.0, -100.0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))))
XCYL = lambda x0, y, z, r, L: Pos(x0, y, z) * Rot(0, 90, 0) * Cylinder(r, L, align=(Align.CENTER, Align.CENTER, Align.MIN))
disc = XCYL(82.438, 80.0, -100.0, 5.0, 0.06) - XCYL(82.3, 80.0, -100.0, 2.0, 0.3)
m10 = (t + disc).solids()[0]
print("valid m10", {k: v.measured for k, v in validity(m10).items()}, m10.volume - t.volume)
print("cv m10", common_volume(m10, board))
print("cv t", common_volume(t, board))
# alternative: raise by a fresh solid build: cut standoff top and re-add taller
m10b = (t + XCYL(82.0, 80.0, -100.0, 5.0, 0.498) ).solids()[0] - XCYL(76.438, 80.0, -100.0, 2.0, 7)
print("valid m10b", {k: v.measured for k, v in validity(m10b).items()}, m10b.volume - t.volume)
print("cv m10b", common_volume(m10b, board))
for dz in (0.06, 0.2, 1.0):
    m = (t + (XCYL(82.438, 80.0, -100.0, 5.0, dz) - XCYL(82.3, 80.0, -100.0, 2.0, 2))).solids()[0]
    print(dz, "cv", common_volume(m, board).measured, common_volume(m, board).status)
