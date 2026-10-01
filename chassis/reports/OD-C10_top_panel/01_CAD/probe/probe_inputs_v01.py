"""WP-02 probe (D2) for od_c10_top: the five reference solids as placed (brief WP-02),
measured in the machine frame. Measures only; no gate reads this file. Paths relative
to the workspace (pathlib).

Usage: uv run tools/run.py python <ws>/01_CAD/probe/probe_inputs_v01.py"""
import json
from pathlib import Path

from build123d import Location, Plane, Vector
from tools.core import read_step, validity
from tools.measure import bore_census, envelope, locate_bore

WS = Path(__file__).resolve().parents[2]
IN = WS / "00_Spec" / "inputs"
OUT = WS / "01_CAD" / "probe" / "probe_inputs_v01.json"
out = {}

L05 = Location(Plane(origin=(0.0, 180.06, 32.0), x_dir=(1, 0, 0), z_dir=(0, -1, 0)))
L07 = Location(Plane(origin=(-92.0, 0.0, -60.0), x_dir=(0, 0, -1), z_dir=(0, 1, 0)))


def res(r):
    d = {"measured": r.measured if not isinstance(r.measured, float) else round(r.measured, 6),
         "unit": r.unit, "status": r.status}
    if r.reason:
        d["reason"] = r.reason
    return d


def env(s):
    return {k: round(v.measured, 4) for k, v in envelope(s).items()}


def one(shape):
    s = shape.solids()
    return s[0] if len(s) == 1 else shape


def axes(L):
    p0 = L.position
    return {n: [round(a - b, 6) for a, b in zip(tuple((L * Location(Vector(*v))).position), tuple(p0))]
            for n, v in (("x", (1, 0, 0)), ("y", (0, 1, 0)), ("z", (0, 0, 1)))}


def planar(s, n, ymin=None):
    rows = []
    for f in s.faces():
        if f.geom_type.name != "PLANE":
            continue
        nn = f.normal_at()
        if nn.dot(Vector(*n)) < 0.9999:
            continue
        bb = f.bounding_box()
        rows.append({"at": round(f.center().dot(Vector(*n)), 5), "area": round(f.area, 3),
                     "min": [round(bb.min.X, 3), round(bb.min.Y, 3), round(bb.min.Z, 3)],
                     "max": [round(bb.max.X, 3), round(bb.max.Y, 3), round(bb.max.Z, 3)]})
    return sorted(rows, key=lambda r: -r["at"])


def bores(s, pred=lambda b: True):
    bc = bore_census(s)
    return bc, [{"d": round(b["diameter"], 4), "start": [round(v, 4) for v in b["start"]],
                 "end": [round(v, 4) for v in b["end"]], "dir": [round(v, 5) for v in b["axis_dir"]],
                 "through": b.get("through")} for b in bc.detail.get("bores", []) if pred(b)]


def loc(bc, p, d):
    return {k: res(v) for k, v in locate_bore(bc, p, d).items()}


# OD-C01 at the identity
c01 = one(read_step(IN / "OD-C01_base_frame.step"))
out["c01_validity"] = {k: res(v) for k, v in validity(c01).items()}
out["c01_envelope"] = env(c01)
out["c01_top_faces"] = planar(c01, (0, 1, 0))[:2]
arcs = []
for f in c01.faces():
    if f.geom_type.name == "CYLINDER" and abs(f.axis_of_rotation.direction.Y) > 0.9999 and f.radius > 5:
        bb = f.bounding_box()
        if bb.max.Y - bb.min.Y > 1:
            arcs.append({"r": round(f.radius, 4), "axis": [round(v, 4) for v in tuple(f.axis_of_rotation.position)],
                         "xz_box": [round(bb.min.X, 3), round(bb.max.X, 3), round(bb.min.Z, 3), round(bb.max.Z, 3)]})
out["c01_vertical_cylinders_r_gt5"] = arcs

# OD-C02 at the identity
c02 = one(read_step(IN / "OD-C02_bulkhead.step"))
out["c02_validity"] = {k: res(v) for k, v in validity(c02).items()}
out["c02_envelope"] = env(c02)
out["c02_up_faces_top3"] = planar(c02, (0, 1, 0))[:3]
bc02, b02 = bores(c02, lambda b: abs(abs(b["axis_dir"][1]) - 1) < 1e-6 and max(b["start"][1], b["end"][1]) > 200)
out["c02_bores_top"] = b02
for x, z in ((65.0, -60.0), (65.0, -210.0)):
    out[f"c02_insert_({x:g},{z:g})"] = loc(bc02, (x, 212.0, z), (0, -1, 0))

# OD-C11 v02 at the identity
c11 = one(read_step(IN / "OD-C11_back_panel_v02.step"))
out["c11_validity"] = {k: res(v) for k, v in validity(c11).items()}
out["c11_envelope"] = env(c11)
out["c11_up_faces_top2"] = planar(c11, (0, 1, 0))[:2]
out["c11_back_faces"] = [r for r in planar(c11, (0, 0, -1)) if r["max"][1] > 200]
bc11, b11 = bores(c11, lambda b: abs(abs(b["axis_dir"][1]) - 1) < 1e-6 and max(b["start"][1], b["end"][1]) > 200)
out["c11_bores_top"] = b11
for x in (90.0, -90.0):
    out[f"c11_insert_({x:g},-293)"] = loc(bc11, (x, 212.0, -293.0), (0, -1, 0))

# OD-C05 as placed
c05l = one(read_step(IN / "OD-C05_group_head_carrier.step"))
out["c05_local_envelope"] = env(c05l)
out["c05_validity"] = {k: res(v) for k, v in validity(c05l).items()}
out["c05_axes"] = axes(L05)
c05 = c05l.moved(L05)
out["c05_envelope"] = env(c05)
out["c05_up_faces_top4"] = planar(c05, (0, 1, 0))[:4]
bc05, b05 = bores(c05, lambda b: abs(abs(b["axis_dir"][1]) - 1) < 1e-6)
out["c05_bores_vertical"] = b05
for x, z in ((44.0, -12.0), (-44.0, -12.0), (44.0, 76.0), (-44.0, 76.0)):
    out[f"c05_cbore_({x:g},{z:g})"] = loc(bc05, (x, 208.0, z), (0, -1, 0))
out["c05_hub_window"] = loc(bc05, (0.0, 205.0, 32.0), (0, -1, 0))

# OD-C07 as placed
c07l = read_step(IN / "OD-C07_valve_flowmeter_mount.step")
out["c07_local_envelope"] = env(c07l)
out["c07_solids"] = len(c07l.solids())
out["c07_axes"] = axes(L07)
c07 = c07l.moved(L07)
out["c07_envelope"] = env(c07)
print(json.dumps(out, indent=1, default=str))
OUT.write_text(json.dumps(out, indent=1, default=str))
