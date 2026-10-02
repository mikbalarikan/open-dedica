"""RV01 positive controls, second set: E-11 through-ray on the filled-vent mutant; mesh_deviation on the coarse re-mesh."""
import json
from tools.core import read_step
from tools.measure import radial_extent, mesh_deviation
from tools.result import gate, Result
J = "/root/oguz-jobs/20261001-od-c11-back-panel"; W = f"{J}/reviews/RV01_work"; M = f"{W}/mutants"
out = {}
m = read_step(f"{M}/census_vent110_filled.step")
r = radial_extent(m, (110, 140, -310), (1, 0, 0), (0, 0, 1), 0, 0, side="inner")
through = 0 if r.ok else (1 if "NoMaterial" in r.reason else None)
g = gate("E-11", Result("vent_through", through, "bool") if through is not None else r, "==", 1, band=0, assumes=["A-03", "A-06"])
out["through_ray"] = {"mutant": "vent slot at x 110 filled", "measured": g.measured, "status": g.status}
p = read_step(f"{J}/02_STEP_STL/od_c11_back_C1_v03.step")
d = mesh_deviation(f"{M}/stl_coarse_0p1.stl", p)
g2 = gate("U-07", d, "<=", 0.01, band=0.0)
out["mesh_deviation"] = {"mutant": "re-mesh at 0.1 mm, 0.5 rad", "measured": g2.measured, "status": g2.status}
print(out); json.dump(out, open(f"{W}/m10_controls2.json", "w"), indent=1)
