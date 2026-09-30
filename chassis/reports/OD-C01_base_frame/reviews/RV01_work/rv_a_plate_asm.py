"""RV01 independent measurement A: plate and assembly (reviewer's own script)."""
import json, math, sys
from pathlib import Path
import numpy as np
from build123d import Location, Plane, Box, Pos
from tools.core import read_step, validity, solids, volume_mm3
from tools.measure import envelope, feature_census, bore_census, locate_bore, clearance, interference, mass_properties
from tools.measure.sampling import kind
from tools.core.shapes import faces

J = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
W = J / "reviews/RV01_work"
out = {}
def R(r):
    return r.to_dict() if hasattr(r, "to_dict") else r

plate = read_step(J / "02_STEP_STL/od_c01_frame_C1_v02.step")
out["plate_label"] = getattr(plate, "label", None)
out["plate_validity"] = {k: R(v) for k, v in validity(plate).items()}
out["plate_env"] = {k: v.measured for k, v in envelope(plate).items()}
fc = feature_census(plate)
out["plate_census"] = {k: v.measured for k, v in fc.items()}
bc = bore_census(plate)
out["bores"] = bc.detail["bores"]
mp = mass_properties(plate, 1270)
out["mass"] = {k: v.measured for k, v in mp.items()}
# top face: planar faces whose normal is +Y at y 0
tops = []
for f in plate.faces():
    if kind(f.wrapped) == "plane":
        n = f.normal_at(f.center())
        bb = f.bounding_box()
        tops.append({"n": [round(n.X, 6), round(n.Y, 6), round(n.Z, 6)], "ymin": bb.min.Y, "ymax": bb.max.Y, "area": f.area})
out["planar_faces"] = tops

holes = {
 "REQ-01": [(35,-40),(-35,-40),(35,-60),(-35,-60)],
 "REQ-02": [(40,-148),(-40,-148),(40,-114),(-40,-114)],
 "REQ-03": [(-4,-239),(-4,-171),(37,-239),(37,-171)],
 "REQ-04": [(65,-45),(65,-105),(65,-165),(65,-225)],
 "REQ-10": [(-113,-42),(-71,-42),(-113,-148.5),(-71,-148.5)],
 "REQ-05": [(110,90),(-110,90),(110,-295),(-110,-295)],
 "REQ-06": [(-80,-120),(-80,-230)],
}
loc = {}
for g, pts in holes.items():
    for x, z in pts:
        r = locate_bore(bc, (x, -3.0, z), (0, 1, 0))
        loc[f"{g}@{x},{z}"] = {k: v.measured for k, v in r.items()}
out["located"] = loc

# assembly
asm = read_step(J / "02_STEP_STL/od_c01_assembly_C1_v02.step")
kids = list(asm.children)
parts = {}
for c in kids:
    parts[c.label] = c
out["asm_labels"] = list(parts)
out["asm_parts"] = {}
for n, c in parts.items():
    v = validity(c)
    e = envelope(c)
    out["asm_parts"][n] = {"validity": {k: vv.measured for k, vv in v.items()},
                           "validity_reason": {k: vv.reason for k, vv in v.items()},
                           "env": {k: round(vv.measured, 6) for k, vv in e.items()},
                           "vol": volume_mm3(c), "nfaces": len(faces(c))}

# independent placement of inputs by spec §4 joints
inp = J / "00_Spec/inputs"
c03 = read_step(inp / "OD-C03_pump_cradle.step"); h01 = read_step(inp / "OD-H01_ulka_ep5_pump.step")
c04 = read_step(inp / "OD-C04_thermoblock_mount.step"); h11 = read_step(inp / "OD-H11_thermoblock.step")
g01 = read_step(inp / "OD-G01_housing_C1_v02.step")
L03 = Location(Plane(origin=(0, 40, -205), x_dir=(0, 0, 1), z_dir=(1, 0, 0)))
L04 = Location((0, 70, -140))
LG = Location(Plane(origin=(0, 180.06, 32.0), x_dir=(1, 0, 0), z_dir=(0, -1, 0)))
P = {"c03": c03.moved(L03), "h01": h01.moved(L03), "c04": c04.moved(L04), "h11": h11.moved(L04), "g01": g01.moved(LG)}
# check rotation maps: local (1,0,0),(0,1,0),(0,0,1)
def mapv(L, v):
    t = L.wrapped.Transformation(); import OCP.gp as gp
    p = gp.gp_Pnt(*v).Transformed(t); o = gp.gp_Pnt(0,0,0).Transformed(t)
    return [round(p.X()-o.X(),9), round(p.Y()-o.Y(),9), round(p.Z()-o.Z(),9)]
out["joint_maps"] = {n: [mapv(L, e) for e in [(1,0,0),(0,1,0),(0,0,1)]] for n, L in [("C03", L03), ("G01", LG)]}
box = Box(110, 4, 44).moved(Location((0, 2, -48)))  # x ±55, y 0..4, z -70..-26
P["box"] = box
out["my_placed"] = {}
for n, s in P.items():
    e = envelope(s)
    out["my_placed"][n] = {"env": {k: round(v.measured, 6) for k, v in e.items()},
                           "validity": {k: v.measured for k, v in validity(s).items()}}

# compare with the assembly solids: envelope match
out["asm_vs_mine"] = {}
for n, s in P.items():
    me = out["my_placed"][n]["env"]
    best = None
    for an, a in out["asm_parts"].items():
        d = max(abs(me[k] - a["env"][k]) for k in me)
        if best is None or d < best[1]:
            best = (an, d)
    out["asm_vs_mine"][n] = best

# clearances
pairs = [("plate","c03"),("plate","c04"),("plate","h01"),("plate","h11"),("c03","c04"),("plate","box"),
         ("g01","plate"),("g01","c03"),("g01","h01"),("g01","c04"),("g01","h11"),("g01","box"),
         ("box","c04"),("box","h11"),("h01","c04"),("h01","h11"),("c03","h11"),("c03","box"),("h01","box"),("c04","h11"),("c03","h01")]
S = dict(P); S["plate"] = plate
out["clearance"] = {}
for a, b in pairs:
    r = clearance(S[a], S[b])
    out["clearance"][f"{a}|{b}"] = {"d": r.measured, "at": r.at, "on_b": r.detail.get("on_b"), "status": r.status, "reason": r.reason}
inter = interference({k: S[k] for k in ["plate","c03","c04","h01","h11","g01","box"]})
out["interference"] = {k: {"v": v.measured, "status": v.status, "reason": v.reason[:200]} for k, v in inter.items()}

# coaxiality: mounts' holes as placed vs plate holes
out["coax"] = {}
for n in ["c03", "c04"]:
    mb = bore_census(P[n])
    lst = []
    for b in mb.detail["bores"]:
        if abs(b["diameter"] - 3.4) < 0.05:
            s = np.array(b["start"]); e = np.array(b["end"]); mid = (s + e) / 2
            r = locate_bore(bc, (mid[0], -3.0, mid[2]), (0, 1, 0))
            lst.append({"mount_d": b["diameter"], "mount_axis": b["axis_dir"], "mount_mid": mid.round(6).tolist(),
                        "plate_d": r["diameter"].measured, "offset": r["offset"].measured})
    out["coax"][n] = lst

# assembly path: lifts
out["path"] = {}
for n in ["c03", "c04", "box"]:
    for lift in [10, 1, 0.1, 0.01, 0]:
        r = clearance(plate, S[n].moved(Location((0, lift, 0))))
        out["path"][f"{n}@{lift}"] = r.measured
# OD-G01 downward planar faces
gf = []
for f in P["g01"].faces():
    if kind(f.wrapped) == "plane":
        n = f.normal_at(f.center())
        if n.Y < -0.999:
            gf.append(round(f.center().Y, 4))
out["g01_down_planes_y"] = sorted(set(gf))
(W / "rv_a.json").write_text(json.dumps(out, indent=1, default=str))
print("done")
