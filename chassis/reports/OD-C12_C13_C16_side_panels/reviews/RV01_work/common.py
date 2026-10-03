"""RV01 reviewer helpers: paths, reading, placement (spec 1.2 sec. 2 joints)."""
import json, math, hashlib
from pathlib import Path
from build123d import Location, Plane, Vector, Box, Cylinder, Pos, Rot, Compound, Solid
from tools.core import read_step, solids
from tools.result import Result

WS = Path("/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels")
WORK = WS / "reviews/RV01_work"
EXP = WS / "02_STEP_STL"
INP = WS / "00_Spec/inputs"
BAND_MM, BAND_DEG, BAND_MM3, BAND_N = 0.005, 0.001, 0.001, 0
ZC = (-262.0, -15.0, 62.0)

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def sols(shape):
    return [Solid(s) for s in solids(shape)]

def one(shape):
    s = sols(shape)
    assert len(s) == 1, len(s)
    return s[0]

def load(name):
    return read_step(EXP / name)

def place(shape, origin, xdir, zdir):
    return shape.moved(Location(Plane(origin=origin, x_dir=xdir, z_dir=zdir)))

def bracket_pose(br, side, zc):
    if side == "R":
        return place(br, (117.0, 0, zc), (1, 0, 0), (0, 0, 1))
    return place(br, (-117.0, 0, zc), (-1, 0, 0), (0, 0, -1))

def references():
    r = {}
    r["OD-C01"] = one(read_step(INP / "OD-C01_base_frame.step"))
    r["OD-C02"] = one(read_step(INP / "OD-C02_bulkhead.step"))
    c05 = read_step(INP / "OD-C05_group_head_carrier.step")
    r["OD-C05"] = [place(s, (0, 180.06, 32.0), (1, 0, 0), (0, -1, 0)) for s in sols(c05)]
    c07 = read_step(INP / "OD-C07_valve_flowmeter_mount.step")
    r["OD-C07"] = [place(s, (-92, 0, -60), (0, 0, -1), (0, 1, 0)) for s in sols(c07)]
    r["OD-C08"] = sols(read_step(INP / "OD-C08_electronics_bay_tray.step"))
    r["OD-C10"] = sols(read_step(INP / "OD-C10_top_panel.step"))
    r["OD-C11"] = sols(read_step(INP / "OD-C11_back_panel.step"))
    foot = sols(read_step(INP / "OD-C15_foot.step"))
    for i, (x, z) in enumerate(((110, 90), (-110, 90), (110, -295), (-110, -295))):
        r[f"OD-C15_{i+1}"] = [place(s, (x, -6, z), (1, 0, 0), (0, -1, 0)) for s in foot]
    # flatten lists into single solids where one
    out = {}
    for k, v in r.items():
        if isinstance(v, list):
            if len(v) == 1:
                out[k] = v[0]
            else:
                for i, s in enumerate(v):
                    out[f"{k}#{i+1}"] = s
        else:
            out[k] = v
    return out

def dump(obj, name):
    def conv(o):
        if isinstance(o, Result):
            return o.to_dict()
        if hasattr(o, "row"):
            return o.row()
        if isinstance(o, dict):
            return {str(k): conv(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [conv(v) for v in o]
        if isinstance(o, float) and not math.isfinite(o):
            return None
        return o
    (WORK / name).write_text(json.dumps(conv(obj), indent=1, default=str))
