"""RV02 reviewer sections, the REQ-08 section at x 0, and the apex by radial_extent."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from rv_pose import *
from build123d import Compound, Box, Location
from tools.drawing.write import write_sections, nothing_clipped
from tools.measure import radial_extent, mass_properties
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
OUT = W / "reviews/RV02_work"; S = OUT / "sections"; S.mkdir(exist_ok=True)
rig = load_rig(); H, G04, G10, _, _ = identify()
asm = Compound([rig, place(H), place(G04), place(G10)])
R = {"sections": []}
jobs = [(asm, "rv02_asm_z0", ("top",), (0, 100, 0)), (asm, "rv02_asm_z44", ("top",), (0, 100, 44)),
        (asm, "rv02_asm_x0", ("left",), (0, 100, 0)),
        (rig, "rv02_rig_x44", ("left",), (44, 80, 0)), (rig, "rv02_rig_y147p5", ("front",), (0, 147.5, 0)),
        (rig, "rv02_rig_y137p5", ("front",), (0, 137.5, 0)), (rig, "rv02_rig_y5", ("front",), (0, 5, 0)),
        (rig, "rv02_rig_z50", ("top",), (0, 80, 50))]
for shape, name, views, thr in jobs:
    try:
        ws = write_sections(shape, S, part=name, version=2, views=views, through=thr)
        for w in ws:
            R["sections"].append({"file": str(w.path.name), "through": thr, "clipped": w.checks["nothing_clipped"].measured, "detail": str(w.detail)[:200]})
    except Exception as e:
        R["sections"].append({"name": name, "error": repr(e)})
print(json.dumps(R["sections"], indent=1))
# REQ-08: plate section at x 0 (slab 0.01 thick)
t = 0.01
slab = rig & (Location((0, 147.5, 0)) * Box(t, 25.0, 200))
v = slab.volume
p = GProp_GProps(); BRepGProp.VolumeProperties_s(slab.wrapped, p)
cy = p.CentreOfMass().Y()
mi = p.MatrixOfInertia()   # about the centre of mass
Izz = mi.Value(3, 3)  # about Z axis: integral (x^2 + y^2) -> x^2 term negligible
A = v / t
I = (Izz - (t ** 2 / 12) * v) / t   # remove the x^2 part, per unit thickness: second moment about the horizontal axis (bending of a plate spanning X)
c = max(160 - cy, cy - 135)
Z = I / c
M = 1530 * 31.0     # N mm, spec 4
R["REQ08"] = {"area_mm2": A, "centroid_y": cy, "I_mm4": I, "Z_mm3": Z, "sigma_MPa": M / Z, "factor_vs_40": 40 / (M / Z),
              "pullthrough_tau_MPa": 765 / (3.14159265 * 5.7 * 5.0), "shear_area_mm2": 3.14159265 * 5.7 * 5.0}
for y in (135.5, 147.5, 159.5):
    r = radial_extent(rig, (0, y, 0), (0, 1, 0), (0, 0, 1), 0.0, 0.0, side="inner")
    R.setdefault("apex", []).append({"y": y, "r": r.measured, "status": r.status, "reason": r.reason})
R["mass"] = {k: v.measured for k, v in mass_properties(rig, 1240).items()}
print(json.dumps({k: R[k] for k in ("REQ08", "apex", "mass")}, indent=1))
(OUT / "sections.json").write_text(json.dumps(R, indent=1, default=str))
