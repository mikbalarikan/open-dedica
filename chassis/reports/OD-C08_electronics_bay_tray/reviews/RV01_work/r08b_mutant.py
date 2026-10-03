import sys; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
from build123d import *
from tools.core import read_step, common_volume, validity
t = Solid(read_step(PART).wrapped)
board = read_step(E01).solids()[0].moved(Location(Plane(origin=(84.0, 80.0, -100.0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))))
XCYL = lambda x0, y, z, r, L: Pos(x0, y, z) * Rot(0, 90, 0) * Cylinder(r, L, align=(Align.CENTER, Align.CENTER, Align.MIN))
m10 = (t + (XCYL(82.438, 80.0, -100.0, 5.0, 0.06) - XCYL(82.3, 80.0, -100.0, 2.0, 0.3))).solids()[0]
print("m10 faces", len(m10.faces()), "t faces", len(t.faces()))
mc = m10.clean(); print("clean faces", len(mc.faces()), {k: v.measured for k, v in validity(mc).items()})
print("cv clean", common_volume(mc, board).measured)
# rebuilt standoff
mb = (t - XCYL(76.0, 80.0, -100.0, 5.0, 6.438)) 
mb = (mb + (XCYL(76.0, 80.0, -100.0, 5.0, 6.498) - XCYL(76.438, 80.0, -100.0, 2.0, 6.2))).solids()[0]
print("rebuilt faces", len(mb.faces()), {k: v.measured for k, v in validity(mb).items()}, "dvol", mb.volume - t.volume)
print("cv rebuilt", common_volume(mb, board).measured)
for dz in (0.001, 0.01, 0.06, 0.5):
    m = (t + (XCYL(82.438, 80.0, -100.0, 5.0, dz) - XCYL(82.3, 80.0, -100.0, 2.0, 1))).solids()[0].clean()
    print("raise", dz, "cv", common_volume(m, board).measured)
# relocate the tray as a whole into the board by 0.06 in +X
mt = t.moved(Location((0.06, 0, 0)))
print("tray moved +0.06x: cv", common_volume(mt, board).measured)
