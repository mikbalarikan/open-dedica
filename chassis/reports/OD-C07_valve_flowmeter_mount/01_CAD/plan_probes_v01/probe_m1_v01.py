from pathlib import Path
from build123d import *
from tools.core import read_step, validity, solid_count
from tools.measure import envelope, feature_census, bore_census
W=Path(__file__).resolve().parents[2] / "00_Spec" / "inputs"
for n in ["OD-H22_3way_valve.step","OD-H24_flowmeter.step"]:
    s=read_step(W/n)
    print("=====",n, type(s), len(s.solids()), [x.label for x in s.solids()])
    v=validity(s); print({k:(r.measured,r.status) for k,r in v.items()} if isinstance(v,dict) else v)
    e=envelope(s); print(e)
    fc=feature_census(s); print(fc)
    bc=bore_census(s); print(bc)
