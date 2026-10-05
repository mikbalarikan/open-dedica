"""D1: clearance of the posed board to every planned panel feature, bosses at two end levels."""
import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent))
from poses import BOARD, load
from standin import panel, cyl_z
from build123d import Solid
from tools.core import solids, common_volume
from tools.measure import clearance
e02 = Solid(solids(load("OD-E02_control_board.step", BOARD))[0])
holes = [(-94.248, 166.514, 15.0), (-98.991, 139.901, 15.0), (-93.765, 113.426, 15.0)]
bosses = [(-91.055, 153.235), (-90.999, 127.251)]
for label, ends in (("spec ends 81.186/81.819", (81.186, 81.819)), ("flat seat 85.485", (85.485, 85.485))):
    print("==", label)
    for k, p in panel(holes, bosses, ends).items():
        r = clearance(p, e02)
        line = f"  {k:6s} clearance {r.measured:.3f} at {r.at} inside {r.detail['inside']}"
        if r.measured < 1e-6:
            cv = common_volume(p, e02); line += f" common {cv.measured}"
        print(line)
# boss side vs board, excluding the end face: a boss shortened 0.5 from its end
for d in (11.0, 10.0):
    for i, (x, y) in enumerate(bosses):
        r = clearance(cyl_z(x, y, d/2, 85.985, 94.0), e02)
        print(f"boss{i} Ø{d} from z 85.985: clearance {r.measured:.3f} at {r.at}")
