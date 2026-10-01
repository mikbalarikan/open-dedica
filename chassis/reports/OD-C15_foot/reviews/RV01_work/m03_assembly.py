"""RV01 measurement 3: own placement of 4 feet + screw/nut envelopes on the OD-C01 input (spec §2 joint)."""
import json, math
from pathlib import Path
from build123d import Cylinder, Polygon, extrude, Location, Pos, Align, Vector, Compound
from tools.core import read_step, validity
from tools.core.boolean import common_volume
from tools.core.step import labels
from tools.core.shapes import solids, faces
from tools.measure import (envelope, bore_census, locate_bore, clearance, interference,
                           mass_properties, radial_profile, radial_extent, engaged_area)

W = Path("/home/claude/oguz-env/jobs/20261001-od-c15-feet")
foot = read_step(W / "02_STEP_STL/od_c15_foot_C1_v01.step")
plate = read_step(W / "00_Spec/inputs/OD-C01_base_frame.step")
out = {}
def rx(res): return {"m": None if res.measured is None else round(res.measured, 6), "at": res.at, "st": res.status, "why": res.reason}

out["plate_validity"] = {k: v.measured for k, v in validity(plate).items()}
out["plate_env"] = {k: round(v.measured, 6) for k, v in envelope(plate).items()}
bc = bore_census(plate)
holes = []
for X, Zh in ((110, 90), (-110, 90), (110, -295), (-110, -295)):
    lb = locate_bore(bc, (X, -3, Zh), (0, 1, 0))
    holes.append({"X": X, "Z": Zh, "d": lb["diameter"].measured, "offset": lb["offset"].measured,
                  "through": lb["through"].measured, "start": lb["diameter"].detail["start"], "end": lb["diameter"].detail["end"]})
out["plate_holes"] = holes
mp = mass_properties(plate, 1000); out["plate_com"] = (mp["com_x"].measured, mp["com_y"].measured, mp["com_z"].measured)

# spec §2 joint: foot x -> X, y -> +Z, z -> -Y : Rx(+90)
def L(X, Zh): return Location((X, -6.0, Zh), (90, 0, 0))
t = L(110, 90) * Location((1, 2, 3))
out["joint_check_(1,2,3)->"] = tuple(round(v, 9) for v in t.position)   # expect (111, -9, 92)

# envelopes in the foot frame (then placed with the same joint)
def hexagon(s):
    e2 = s / math.sqrt(3)
    return Polygon(*[(e2 * math.cos(math.radians(60 * k)), e2 * math.sin(math.radians(60 * k))) for k in range(6)], align=None)
def nut(s=5.5, top=2.5):
    body = extrude(hexagon(s), 2.4)            # z 0..2.4
    body = body - Cylinder(1.5, 3, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0, 0, -0.3)))
    return body.moved(Location((0, 0, top)))
def screw():
    head = Cylinder(2.85, 1.65, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0, 0, -7.65)))
    shank = Cylinder(1.5, 12.0, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0, 0, -6.0)))
    return head + shank

poses = {}
for i, (X, Zh) in enumerate(((110, 90), (-110, 90), (110, -295), (-110, -295)), 1):
    loc = L(X, Zh)
    f = foot.moved(loc); n = nut().moved(loc); s = screw().moved(loc)
    poses[i] = (X, Zh, f, n, s)
res = {}
for i, (X, Zh, f, n, s) in poses.items():
    p = {}
    p["foot_env"] = {k: round(v.measured, 6) for k, v in envelope(f).items()}
    p["screw_env"] = {k: round(v.measured, 6) for k, v in envelope(s).items()}
    p["nut_env"] = {k: round(v.measured, 6) for k, v in envelope(n).items()}
    p["c_foot_plate"] = rx(clearance(f, plate)); p["c_nut_foot"] = rx(clearance(n, f)); p["c_screw_plate"] = rx(clearance(s, plate))
    it = interference({"foot": f, "plate": plate, "nut": n, "screw": s})
    p["interf"] = {k: rx(v) for k, v in it.items()}
    # engaged areas (corroboration)
    p["ea_foot_on_plate"] = rx(engaged_area(f, plate, (0, 1, 0), 0.005))
    p["ea_nut_on_foot"] = rx(engaged_area(n, f, (0, 1, 0), 0.01))
    p["ea_head_on_plate"] = rx(engaged_area(s, plate, (0, -1, 0), 0.01))
    # axis: foot lid bore located in placed frame vs plate hole
    fb = bore_census(f); lbf = locate_bore(fb, (X, -7.25, Zh), (0, 1, 0))
    p["foot_bore_offset_from_hole_axis"] = rx(lbf["offset"]); p["foot_bore_start_end"] = (lbf["diameter"].detail["start"], lbf["diameter"].detail["end"])
    # REQ-05: straight edges and corner arc; plate outer radius about the hole axis, outward sector
    sx = 1 if X > 0 else -1; sz = 1 if Zh > 0 else -1
    # outward sector angles measured from +X about +Y axis... use ref (sx,0,0) and sweep toward sz
    # right hand about +Y: from +X toward -Z. angle a gives dir (cos a, 0, -sin a)
    angs = [a for a in range(0, 360, 5) if (math.cos(math.radians(a)) * sx >= -1e-9 and -math.sin(math.radians(a)) * sz >= -1e-9)]
    pr = radial_profile(plate, (X, -6, Zh), (0, 1, 0), (1, 0, 0), angs, (0.5, 5.5), margin=0, z_step=1.0, side="outer", r_min=0.0)
    p["plate_corner_outer_r"] = {k: rx(v) for k, v in pr.items()}
    pf = radial_profile(f, (X, -6, Zh), (0, -1, 0), (1, 0, 0), list(range(0, 360, 10)), (0.6, 8.9), margin=0, z_step=1.0, side="outer")
    p["foot_outer_r_about_hole"] = {k: rx(v) for k, v in pf.items()}
    pe = p["plate_env"] = out["plate_env"]
    p["REQ05_x_edge"] = round(pe["max_x"] - p["foot_env"]["max_x"], 6) if X > 0 else round(p["foot_env"]["min_x"] - pe["min_x"], 6)
    p["REQ05_z_edge"] = round(pe["max_z"] - p["foot_env"]["max_z"], 6) if Zh > 0 else round(p["foot_env"]["min_z"] - pe["min_z"], 6)
    p["REQ05_arc"] = round(pr["min"].measured - pf["max"].measured - (lbf["offset"].measured or 0), 6)
    res[i] = p
out["poses"] = res
# REQ-06 COM inside the rectangle of the four axes
cx, cy, cz = out["plate_com"]
out["REQ06_com_margins"] = {"x+": 110 - cx, "x-": cx + 110, "z+": 90 - cz, "z-": cz + 295}
json.dump(out, open(W / "reviews/RV01_work/m03_assembly.json", "w"), indent=1, default=str)
for k, v in out.items():
    if k != "poses": print(k, json.dumps(v, default=str)[:600])
for i, p in res.items():
    print("POSE", i)
    for k, v in p.items():
        if k != "plate_env": print("  ", k, json.dumps(v, default=str)[:500])
