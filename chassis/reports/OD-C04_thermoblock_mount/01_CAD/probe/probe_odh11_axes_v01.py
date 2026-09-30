"""D2 probe 2: material along and around the two screw-hole axes, nearest OD-H11 material
to the spec's standoff and plate volumes, rearmost surface, pad radial extents.
Primitive volumes only (feasibility of spec §4 values); nothing here is a deliverable."""
import json, math
from pathlib import Path
HERE = Path(__file__).resolve().parent
WS = HERE.parents[1]
from build123d import Cylinder, Box, Pos, Vector, Location
from OCP.BRepClass3d import BRepClass3d_SolidClassifier
from OCP.gp import gp_Pnt
from OCP.TopAbs import TopAbs_IN, TopAbs_ON
from tools.core import read_step
from tools.measure import clearance, radial_profile, envelope

tb = read_step(WS / "00_Spec/inputs/OD-H11_thermoblock.step")
solid = tb.solids()[0].wrapped
from OCP.IntCurvesFace import IntCurvesFace_ShapeIntersector
from OCP.gp import gp_Lin, gp_Dir
ISX = IntCurvesFace_ShapeIntersector(); ISX.Load(solid, 1e-6)
def inside(x, y, z):
    c = BRepClass3d_SolidClassifier(solid, gp_Pnt(x, y, z), 1e-6)
    return c.State() == TopAbs_IN
def zruns(x, y, z0=-5.0, z1=55.0):
    ISX.Perform(gp_Lin(gp_Pnt(x, y, z0), gp_Dir(0, 0, 1)), 0.0, z1 - z0)
    ws = sorted({round(z0 + ISX.WParameter(i), 4) for i in range(1, ISX.NbPnt() + 1)})
    pts = [z0] + ws + [z1]
    iv = []
    for a, b in zip(pts[:-1], pts[1:]):
        if b - a > 1e-3 and inside(x, y, (a + b) / 2):
            if iv and abs(iv[-1][1] - a) < 1e-4: iv[-1][1] = b
            else: iv.append([a, b])
    return iv

out = {}
holes = {"S1": (-19.62, 20.18), "S2": (25.01, 9.08)}
for name, (hx, hy) in holes.items():
    rows = {}
    for r in (0.0, 1.9, 3.5, 6.0, 10.0, 16.0):
        angs = [0] if r == 0 else range(0, 360, 15)
        rows[str(r)] = [(a, zruns(hx + r * math.cos(math.radians(a)), hy + r * math.sin(math.radians(a)))) for a in angs]
    out[name + "_material_z_intervals"] = rows; print(name, "axes done", flush=True)
# nearest OD-H11 material to the spec's standoff columns (Ø12) and spacer (Ø7), spec lengths
def cyl(d, z0, z1, x, y):
    return Pos(x, y, (z0 + z1) / 2) * Cylinder(d / 2, z1 - z0)
cases = {"S1_standoff_z-12_-6.8": cyl(12, -12, -6.8, *holes["S1"]),
         "S1_spacer_z-6.8_3.2": cyl(7, -6.8, 3.2, *holes["S1"]),
         "S2_standoff_z-12_17.6": cyl(12, -12, 17.6, *holes["S2"]),
         "S2_spacer_z17.6_27.6": cyl(7, 17.6, 27.6, *holes["S2"]),
         "plate_z-17_-12": Pos(0, -15, -14.5) * Box(100, 110, 5),
         "foot_y-70_-66": Pos(0, -68, 8) * Box(100, 4, 50)}
for k, s in cases.items():
    r = clearance(s, tb)
    out["clearance_" + k] = {"mm": r.measured, "status": r.status, "at": r.at, "detail": r.detail}; print(k, r.measured, r.at, flush=True)
# pads: outer radius over z 0..47.64 at the pad angles
for ang in (262.5, 339.0):
    rp = radial_profile(tb, (0, 0, 0), (0, 0, 1), (1, 0, 0), [ang - 10, ang - 5, ang, ang + 5, ang + 10],
                        (0.0, 47.64), margin=(0, 0), z_step=0.5)
    out[f"pad_{ang}"] = {k: {"mm": v.measured, "status": v.status, "at": v.at} for k, v in rp.items()} if isinstance(rp, dict) else {"mm": rp.measured, "at": rp.at, "status": rp.status}
# overall outer radius sweep
rp = radial_profile(tb, (0, 0, 0), (0, 0, 1), (1, 0, 0), list(range(0, 360, 5)), (0.0, 47.64), margin=(0, 0), z_step=1.0)
out["outer_all"] = {k: {"mm": v.measured, "status": v.status, "at": v.at} for k, v in rp.items()} if isinstance(rp, dict) else {"mm": rp.measured, "at": rp.at}
json.dump(out, open(HERE / "probe_odh11_axes_v01.json", "w"), indent=1, default=str)
for k, v in out.items():
    if "intervals" in k:
        print(k)
        for r, runs in v.items():
            uniq = {}
            for a, iv in runs: uniq.setdefault(json.dumps(iv), []).append(a)
            print("  r", r, {kk: vv[:6] for kk, vv in uniq.items()})
    else:
        print(k, json.dumps(v, default=str)[:400])
