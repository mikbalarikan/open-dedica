import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from geo import *
from tools.core import write_stl
from tools.measure import mesh_deviation, min_wall_mesh
from tools.result import gate
m = load_mount(); C = []
md = mesh_deviation(W / "mutant_coarse.stl", m)
g = gate("U-07", md, "<=", 0.01, band=BAND_MM); print("mesh_deviation coarse", g.status, g.measured); C.append({"check": "mesh_deviation", "mutant": "STL re-meshed at 0.2 mm / 0.5 rad", "got": g.status})
mut = m - ann(17.0, 18.6, 10.6, 13.1)
write_stl(mut, W / "mutant_thinring.stl", tolerance=0.01, angular_tolerance=0.05)
mw = min_wall_mesh(W / "mutant_thinring.stl")
g = gate("D-01a", mw, ">=", 0.8, band=BAND_MM); print("min_wall_mesh thin ring", g.status, g.measured); C.append({"check": "min_wall_mesh", "mutant": "STL of the thinned-ring mutant", "got": g.status})
dump("s13.json", C)
