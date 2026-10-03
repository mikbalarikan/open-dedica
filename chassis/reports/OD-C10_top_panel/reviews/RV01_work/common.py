"""RV01 reviewer helpers: load the delivered lid and the references placed per spec 1.2 §2."""
import json, sys
from pathlib import Path
from build123d import Location, Plane, Box, Cylinder, Pos, Solid, Compound, Align
from tools.core import read_step
from tools.core.shapes import solids

JOB = Path("/root/oguz-jobs/20261001-od-c10-top-panel")
WORK = JOB / "reviews/RV01_work"
LID = JOB / "02_STEP_STL/od_c10_top_C1_v01.step"
INP = JOB / "00_Spec/inputs"
BAND = {"mm": 0.005, "mm3": 0.001, "deg": 0.001, "count": 0, "bool": 0, "rad": 0.00002, "mm2": 0.001}

def lid():
    s = solids(read_step(LID))
    assert len(s) == 1
    return Solid(s[0])

def placed(name):
    sh = read_step(INP / {"C01": "OD-C01_base_frame.step", "C02": "OD-C02_bulkhead.step",
                          "C05": "OD-C05_group_head_carrier.step", "C07": "OD-C07_valve_flowmeter_mount.step",
                          "C11": "OD-C11_back_panel_v02.step"}[name])
    ss = solids(sh)
    out = []
    for s in ss:
        s = Solid(s)
        if name == "C05":
            s = s.moved(Location(Plane(origin=(0, 180.06, 32.0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))))
        elif name == "C07":
            s = s.moved(Location(Plane(origin=(-92, 0, -60), x_dir=(0, 0, -1), z_dir=(0, 1, 0))))
        out.append(s)
    return out[0] if len(out) == 1 else Compound(out)

def box(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)

def ycyl(x, z, r, y0, y1):
    return Pos(x, (y0 + y1) / 2, z) * Location((0, 0, 0), (1, 0, 0), 90) * Cylinder(r, y1 - y0)

def crop(shape, b):
    return shape & b

def dump(name, obj):
    (WORK / name).write_text(json.dumps(obj, indent=1, default=str))
