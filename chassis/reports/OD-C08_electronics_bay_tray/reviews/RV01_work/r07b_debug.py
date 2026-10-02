import sys; sys.path.insert(0, "/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/reviews/RV01_work")
from rcommon import *
from build123d import *
from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
from tools.core import read_step, common_volume
from tools.core.shapes import solids, volume_mm3
t = Solid(read_step(PART).wrapped)
board = read_step(E01).solids()[0].moved(Location(Plane(origin=(84.0, 80.0, -100.0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))))
XCYL = lambda x0, y, z, r, L: Pos(x0, y, z) * Rot(0, 90, 0) * Cylinder(r, L, align=(Align.CENTER, Align.CENTER, Align.MIN))
BOX = lambda x0, y0, z0, dx, dy, dz: Pos(x0, y0, z0) * Box(dx, dy, dz, align=(Align.MIN, Align.MIN, Align.MIN))
def raw(a, b, fuzzy=0.0):
    op = BRepAlgoAPI_Common(); 
    from OCP.TopTools import TopTools_ListOfShape
    la, lb = TopTools_ListOfShape(), TopTools_ListOfShape(); la.Append(a.wrapped); lb.Append(b.wrapped)
    op.SetArguments(la); op.SetTools(lb); op.SetFuzzyValue(fuzzy); op.Build()
    r = op.Shape(); return op.IsDone(), sum(volume_mm3(s) for s in solids(r))
for name, piece in (("annulus x82.438..82.498 r2..5", XCYL(82.438, 80, -100, 5, 0.06) - XCYL(82.3, 80, -100, 2.0, 0.3)),
                    ("annulus x82.0..82.498 r2..5", XCYL(82.0, 80, -100, 5, 0.498) - XCYL(81.9, 80, -100, 2.0, 0.7)),
                    ("disc x82.0..82.498 r5 (no bore)", XCYL(82.0, 80, -100, 5, 0.498)),
                    ("annulus x82.0..82.498 r2.5..5", XCYL(82.0, 80, -100, 5, 0.498) - XCYL(81.9, 80, -100, 2.5, 0.7)),
                    ("annulus x82.2..82.498 r2..5", XCYL(82.2, 80, -100, 5, 0.298) - XCYL(81.9, 80, -100, 2.0, 0.7)),
                    ("box x82.0..82.498 near H1", BOX(82.0, 76, -104, 0.498, 3, 8)),
                    ("box x82.3..82.498 near H1", BOX(82.3, 76, -104, 0.198, 3, 8)),
                    ("box x82.438..82.498 near H1", BOX(82.438, 76, -104, 0.06, 3, 8)),
                    ("box x82.0..82.498 far mid-board", BOX(82.0, 50, -150, 0.498, 3, 8))):
    print(f"{name:36s} vol {piece.volume:8.3f}  cv {common_volume(piece, board).measured}  raw {raw(piece, board)}  fuzzy1e-5 {raw(piece, board, 1e-5)}")
