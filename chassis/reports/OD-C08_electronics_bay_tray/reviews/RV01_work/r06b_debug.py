import sys; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
from build123d import *
from tools.core import read_step, common_volume
from tools.measure import clearance
t = Solid(read_step(PART).wrapped)
e = read_step(E01).solids()[0]
board = e.moved(Location(Plane(origin=(84.0, 80.0, -100.0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))))
XCYL = lambda x0, y, z, r, L: Pos(x0, y, z) * Rot(0, 90, 0) * Cylinder(r, L, align=(Align.CENTER, Align.CENTER, Align.MIN))
disc = XCYL(82.438, 80.0, -100.0, 5.0, 0.06) - XCYL(82.3, 80.0, -100.0, 2.0, 0.3)
print("disc bbox", disc.bounding_box(), disc.volume)
print("disc&board", common_volume(disc, board))
for dz in (0.06, 0.2, 0.5):
    d2 = XCYL(82.438, 80.0, -100.0, 5.0, dz) - XCYL(82.3, 80.0, -100.0, 2.0, 1.0)
    print(dz, "cv", common_volume(d2, board).measured, "occ", (d2 & board).volume)
# board solder face near H1: what does the board look like at x 82.44..82.6 around H1?
probe = Pos(82.438, 80, -100) * Box(0.3, 14, 14, align=(Align.MIN, Align.CENTER, Align.CENTER))
print("board in slab around H1", (probe & board).volume, "of", probe.volume)
for x in (82.45, 82.5, 83.0, 83.9):
    print(x, [ board.is_inside(Vector(x, 80 + r, -100)) for r in (2.5, 3, 4, 5, 6, 8)])
m10 = (t + disc).solids(); print(len(m10)); m10 = m10[0]
print("m10&board", common_volume(m10, board), (m10 & board).volume)
