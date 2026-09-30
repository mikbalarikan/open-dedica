"""WP-02 probe (D2): the OD-C01 plate's top face and bulkhead inserts, and the wet-side
neighbours placed by the OD-C01 spec 1.2 section 4 joints, measured against the
bulkhead's planes. Measures only; no gate reads this file.
Paths relative to the workspace (pathlib)."""
import json
from pathlib import Path

from build123d import Box, Location, Plane
from tools.core import read_step, validity
from tools.measure import bore_census, clearance, envelope, locate_bore

WS = Path(__file__).resolve().parents[2]
IN = WS / "00_Spec" / "inputs"
OUT = WS / "01_CAD" / "probe" / "probe_placements_v01.json"
out = {}


def res(r):
    d = {"measured": r.measured if not isinstance(r.measured, float) else round(r.measured, 6),
         "unit": r.unit, "status": r.status}
    if r.reason:
        d["reason"] = r.reason
    if r.at is not None:
        d["at"] = r.at
    return d


def env(s):
    return {k: round(v.measured, 4) for k, v in envelope(s).items()}


def box(x0, x1, y0, y1, z0, z1):
    return Box(x1 - x0, y1 - y0, z1 - z0).moved(Location(((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)))


# plate at the identity
plate = read_step(IN / "OD-C01_base_frame.step")
out["plate_validity"] = {k: res(v) for k, v in validity(plate).items()}
out["plate_envelope"] = env(plate)
ymax = envelope(plate)["max_y"].measured
tops = [f for f in plate.faces() if f.geom_type.name == "PLANE" and f.normal_at().Y > 0.9999
        and abs(f.center().Y - ymax) < 1e-3]
out["plate_top_face"] = {"y": round(ymax, 6), "faces": len(tops), "area_mm2": round(sum(f.area for f in tops), 3)}
bc = bore_census(plate)
ins = {}
for z in (-45.0, -105.0, -165.0, -225.0):
    L = locate_bore(bc, (65.0, -3.0, z), (0, 1, 0))
    ins[f"(65,{z:g})"] = {k: res(v) for k, v in L.items()}
out["plate_bulkhead_inserts"] = ins

# joints of OD-C01 spec 1.2 section 4
L03 = Location(Plane(origin=(0, 40, -205), x_dir=(0, 0, 1), z_dir=(1, 0, 0)))
L04 = Location((0, 70, -140))
LG = Location(Plane(origin=(0, 180.06, 32), x_dir=(1, 0, 0), z_dir=(0, -1, 0)))
placed = {
    "od_c03": read_step(IN / "OD-C03_pump_cradle.step").moved(L03),
    "od_h01": read_step(IN / "OD-H01_ulka_ep5_pump.step").moved(L03),
    "od_c04": read_step(IN / "OD-C04_thermoblock_mount.step").moved(L04),
    "od_h11": read_step(IN / "OD-H11_thermoblock.step").moved(L04),
    "od_g01": read_step(IN / "OD-G01_housing_C1_v02.step").moved(LG),
    "od_c05_foot_box": box(-55, 55, 0, 210, -70, -26),
}
# the bulkhead's space (spec 4 envelope) and its wet-side planes as thin slabs over its z and y ranges
bulk_env = box(59, 73, 0, 215, -240, -30)
x59 = box(59, 59.001, 0, 215, -240, -30)
x61 = box(61, 61.001, 0, 215, -240, -30)
collars = {f"collar_y{y:g}_z{z:g}": box(61, 63, y - 9, y + 9, z - 9, min(z + 16, -30))
           for y, z in ((150, -200), (150, -130), (150, -60), (60, -40))}
for n, s in placed.items():
    row = {"envelope": env(s)}
    if n != "od_c05_foot_box":
        row["validity"] = {k: res(v) for k, v in validity(s).items()}
    for tag, t in (("to_bulkhead_envelope", bulk_env), ("to_plane_x59", x59), ("to_plane_x61", x61)):
        c = clearance(s, t)
        row[tag] = res(c) | {"on_neighbour": c.detail.get("on_a"), "on_target": c.detail.get("on_b")}
    for cn, cb in collars.items():
        row[f"to_{cn}_box"] = res(clearance(s, cb))
    band = s & box(-300, 300, -10, 400, -240, -30)
    sol = band.solids() if band else []
    row["max_x_in_z_band_-240_-30"] = round(max(v.X for so in sol for v in so.vertices()), 4) if sol else None
    out[n] = row
out["note"] = ("collar boxes: x 61..63, y +-9, z -9 .. +16 about each window centre (clipped at z -30), a"
               " bounding estimate of the round collar with its gable; OD-H11 is unsound (brep_valid 0)")
print(json.dumps(out, indent=1, default=str))
OUT.write_text(json.dumps(out, indent=1, default=str))
