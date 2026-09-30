"""D2 probe: measure the OD-H01 STEP for the plan (frame side plate, corners, validity,
clearance of the planned C1 keep-in volumes). Probe only: nothing here is a deliverable."""
import json
import math
import sys
from pathlib import Path

from build123d import Box, Cylinder, Pos, Rot, Solid, Vector, Face, Wire, Polyline, extrude, Plane, Location

from tools.core import validity, read_step
from tools.core.boolean import common_volume
from tools.measure import clearance, envelope, radial_extent

WS = Path(__file__).resolve().parents[2]
PUMP = WS / "00_Spec/inputs/OD-H01_ulka_ep5_pump.step"
out = {}

pump = read_step(PUMP)
v = validity(pump)
out["validity"] = {k: (r.measured, r.status, r.reason) for k, r in v.items()}
env = envelope(pump)
out["envelope"] = {k: round(r.measured, 4) for k, r in env.items()}


def rnd(t):
    return [round(x, 3) for x in t]


# cross-sections: thin slabs at the rib mid-planes and between the ribs
sections = {}
for z in (3.0, 15.0, 27.0, 0.0, 6.0, 24.0, 30.0):
    slab = Pos(0, 0, z) * Box(200, 200, 0.02)
    pieces = (pump & slab)
    sols = pieces.solids()
    rows = []
    for s in sols:
        bb = s.bounding_box()
        rows.append({"min": rnd((bb.min.X, bb.min.Y)), "max": rnd((bb.max.X, bb.max.Y)),
                     "area_mm2": round(s.volume / 0.02, 2)})
    sections[z] = rows
out["sections"] = sections

# side plate: material along +X and -X rays at y = 0 and y = +-12, several z
rays = {}
for ang in (0.0, 180.0):
    for z in (-6.0, 3.0, 15.0, 27.0, 32.0):
        r = radial_extent(pump, (0, 0, 0), (0, 0, 1), (1, 0, 0), ang, z, side="outer", r_min=23.95, r_max=40.0)
        rays[f"{ang}@{z}"] = (r.measured, r.status, r.reason, r.detail.get("material"))
out["side_rays"] = rays

# pump material near the saddle sector edges and posts: max radius at theta 40..140 at rib planes
sector = {}
for z in (3.0, 27.0):
    for ang in (30, 35, 40, 45, 50, 90, 130, 135, 140, 145, 150):
        r = radial_extent(pump, (0, 0, 0), (0, 0, 1), (1, 0, 0), float(ang), z, side="outer")
        sector[f"{ang}@{z}"] = (r.measured, r.status, r.reason)
out["sector_rays_outer"] = sector

# planned C1 keep-in volumes (probe only)
C = dict(r_in=26.65, r_out=32.0, th0=45.0, th1=135.0, foot_y0=37.0, foot_y1=40.0,
         post_x_in=29.5, post_t=4.0, rib_z=((0.0, 6.0), (24.0, 30.0)))
xo = C["r_out"] * math.cos(math.radians(C["th0"]))


def rib(z0, z1):
    th0, th1 = map(math.radians, (C["th0"], C["th1"]))
    n = 64
    pts = [(C["r_in"] * math.cos(th0 + (th1 - th0) * i / n), C["r_in"] * math.sin(th0 + (th1 - th0) * i / n)) for i in range(n + 1)]
    pts = pts + [(-xo, xo), (-xo, C["foot_y0"]), (xo, C["foot_y0"]), (xo, xo)]
    face = Face(Wire(Polyline(*[(x, y, z0) for x, y in pts], close=True)))
    return extrude(face, amount=z1 - z0, dir=(0, 0, 1))


probes = {}
for i, (z0, z1) in enumerate(C["rib_z"]):
    probes[f"rib{i+1}"] = rib(z0, z1)
    for s in (1, -1):
        xc = s * (C["post_x_in"] + C["post_t"] / 2)
        probes[f"post{i+1}{'+' if s > 0 else '-'}"] = Pos(xc, C["foot_y0"] / 2, (z0 + z1) / 2) * Box(C["post_t"], C["foot_y0"], z1 - z0)
probes["foot"] = Pos(0, 38.5, 15.0) * Box(80, 3, 50)
clr = {}
for k, p in probes.items():
    r = clearance(p, pump)
    clr[k] = (round(r.measured, 4), rnd(r.at), rnd(r.detail["on_b"]))
out["clearance_keepin_to_pump"] = clr

# assumed sleeve solid A-03 against the pump
sleeve = Pos(0, 0, -6.0) * (Cylinder(26.65, 38.0, align=None) - Cylinder(23.65, 38.0, align=None))
sleeve = Pos(0, 0, 0) * sleeve
cv = common_volume(sleeve, pump)
out["sleeve_pump_common_mm3"] = (cv.measured, cv.status, cv.reason)
sc = clearance(probes["rib1"], sleeve)
out["rib1_sleeve_clearance"] = (sc.measured, rnd(sc.at))
out["rib_probe_z"] = {k: (round(probes[k].bounding_box().min.Z, 3), round(probes[k].bounding_box().max.Z, 3)) for k in ("rib1", "rib2")}
out["rib_sleeve_common_mm3"] = {k: common_volume(probes[k], sleeve).measured for k in ("rib1", "rib2")}
out["sleeve_env"] = {k: round(r.measured, 3) for k, r in envelope(sleeve).items()}

print(json.dumps(out, indent=1, default=str))
