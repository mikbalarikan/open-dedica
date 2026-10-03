"""RV02 control for the flank-plane angle reading (REQ-03 roof 45.1 +- 1 deg)."""
import json, math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from rv_pose import *
from build123d import Location
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.GeomAbs import GeomAbs_Plane
from OCP.TopAbs import TopAbs_REVERSED
from OCP.BRepBndLib import BRepBndLib
from OCP.Bnd import Bnd_Box
from tools.result import Result, gate
def flanks(shape):
    out = []
    for f in shape.faces():
        s = BRepAdaptor_Surface(f.wrapped)
        if s.GetType() != GeomAbs_Plane: continue
        d = s.Plane().Axis().Direction(); n = [d.X(), d.Y(), d.Z()]
        if f.wrapped.Orientation() == TopAbs_REVERSED: n = [-c for c in n]
        b = Bnd_Box(); BRepBndLib.Add_s(f.wrapped, b); x0, y0, z0, x1, y1, z1 = b.Get()
        if abs(n[1]) < 1e-6 and abs(n[0]) > 0.1 and n[2] < -0.5 and x1 - x0 > 15:      # the window's two roof flanks
            out.append(math.degrees(math.acos(-n[2])))
    return out
rig = load_rig()
nom = flanks(rig)
mut = flanks(Location((0, 0, 0), (0, 1, 0), 2.0) * rig)
worst = max(nom, key=lambda a: abs(a - 45.1)); worst_m = max(mut, key=lambda a: abs(a - 45.1))
g0 = gate("REQ-03", Result("flank_angle", worst, "deg"), "in", (44.1, 46.1), band=0.001)
g1 = gate("REQ-03", Result("flank_angle", worst_m, "deg"), "in", (44.1, 46.1), band=0.001)
R = {"nominal": nom, "nominal_gate": g0.row(), "mutant_rot2deg_about_Y": mut, "mutant_gate": g1.row(),
     "apex_from_R": 30.0 / math.cos(math.radians(nom[0]))}
print(json.dumps(R, indent=1))
(Path(__file__).parent / "control_flank.json").write_text(json.dumps(R, indent=1))
