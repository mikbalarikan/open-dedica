import json, math, sys
from pathlib import Path
J = Path("/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier")
W = J / "reviews/RV02_work"
OUT = W / "out"
STEP = J / "02_STEP_STL/od_c05_carrier_C4_v04.step"
ASM = J / "02_STEP_STL/od_c05_assembly_C4_v04.step"
STL = J / "02_STEP_STL/od_c05_carrier_C4_v04.stl"
MF3 = J / "02_STEP_STL/od_c05_carrier_C4_v04.3mf"
G01 = J / "00_Spec/inputs/OD-G01_housing_C1_v02.step"
G04 = J / "00_Spec/inputs/OD-G04_brewing_gasket_support.step"
from tools.core.step import read_step
from tools.core.shapes import solids, faces, occ

def rd(r):
    return r.to_dict() if hasattr(r, "to_dict") else r

def dump(name, obj):
    def conv(o):
        if hasattr(o, "to_dict"): return o.to_dict()
        if isinstance(o, dict): return {k: conv(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)): return [conv(v) for v in o]
        return o
    (OUT / f"{name}.json").write_text(json.dumps(conv(obj), indent=1, default=str))

def carrier():
    s = read_step(STEP)
    return s
