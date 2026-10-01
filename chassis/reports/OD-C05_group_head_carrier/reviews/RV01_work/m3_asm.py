"""RV01: assembly rows (U-03 a, REQ-01) on my own placement of the inputs and on the delivered assembly STEP."""
import json, sys
from pathlib import Path
import numpy as np
from build123d import Pos, Rot, Axis
from tools.core import read_step, validity, common_volume
from tools.core.shapes import solids, volume_mm3
from tools.core.step import labels
from tools.measure import clearance, interference, bore_census, locate_bore, envelope
J = Path("/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier")
W = J / "reviews/RV01_work"
carrier = read_step(J / "02_STEP_STL/od_c05_carrier_C1_v01.step")
g01 = read_step(J / "00_Spec/inputs/OD-G01_housing_C1_v02.step")
g04raw = read_step(J / "00_Spec/inputs/OD-G04_brewing_gasket_support.step")
g04 = Pos(0, 0, -6.82) * (Rot(0, 0, 6.05) * g04raw)
out = {}
out["validity_g01"] = {k: v.measured for k, v in validity(g01).items()}
out["validity_g04"] = {k: v.measured for k, v in validity(g04).items()}
out["env_g04_placed"] = {k: v.measured for k, v in envelope(g04).items()}
c1 = clearance(carrier, g01); c4 = clearance(carrier, g04)
itf = interference({"carrier": carrier, "g01": g01, "g04": g04})
out["clear_g01"] = c1.to_dict(); out["clear_g04"] = c4.to_dict()
out["interference"] = {k: v.to_dict() for k, v in itf.items()}
print("validity", out["validity_g01"], out["validity_g04"])
print("G04 placed env z", out["env_g04_placed"]["min_z"], out["env_g04_placed"]["max_z"])
print("clear G01", c1.measured, c1.at, c1.detail.get("points") or c1.detail)
print("clear G04", c4.measured, c4.at, c4.detail)
print("interference", {k: (v.measured, v.status) for k, v in itf.items()})
# insert bores on OD-G01 and the carrier holes
bg = bore_census(g01); bc = bore_census(carrier)
rows = []
for sx in (1, -1):
    for sy in (1, -1):
        ins = locate_bore(bg, (sx * 44, sy * 44, -22.0), (0, 0, 1))
        hol = locate_bore(bc, (sx * 44, sy * 44, -26.44), (0, 0, 1))
        a = np.array(ins["diameter"].detail["start"]); b = np.array(ins["diameter"].detail["end"])
        ha = np.array(hol["diameter"].detail["start"]); hb = np.array(hol["diameter"].detail["end"])
        # distance between the two axes (both along Z): xy offset of axis points
        off = float(np.linalg.norm(a[:2] - ha[:2]))
        rows.append(dict(corner=(sx * 44, sy * 44), insert_d=ins["diameter"].measured, insert_len=ins["length"].measured,
                         insert_start=a.tolist(), insert_end=b.tolist(), insert_offset_nominal=ins["offset"].measured,
                         hole_d=hol["diameter"].measured, axis_offset=off))
        print(rows[-1])
out["inserts"] = rows
# the delivered assembly STEP
asm = read_step(J / "02_STEP_STL/od_c05_assembly_C1_v01.step")
kids = list(asm.children)
out["asm_labels"] = [k.label for k in kids]
cmp = {}
for k in kids:
    ref = {"od_c05_carrier": carrier, "od_g01_housing": g01, "od_g04_brewing_gasket_support": g04}.get(k.label)
    if ref is None: cmp[k.label] = "unknown"; continue
    vk, vr = volume_mm3(k), volume_mm3(ref); cv = common_volume(k, ref)
    cmp[k.label] = dict(vol=vk, vol_ref=vr, common=cv.measured, mismatch=vk + vr - 2 * cv.measured)
print("assembly", cmp)
out["asm_compare"] = cmp
# assembly path: the housing (with OD-G04 inside it) offered along -Z from 30 mm in front to the seat
path = []
for d in (30, 20, 10, 5, 2, 1, 0.5, 0.1, 0.0):
    h = Pos(0, 0, d) * g01; s = Pos(0, 0, d) * g04
    cl = clearance(carrier, h); iv = common_volume(carrier, h); iv4 = common_volume(carrier, s)
    path.append((d, cl.measured, iv.measured, iv4.measured))
print("path (d, clearance G01, interference G01, interference G04):", path)
out["path"] = path
(W / "m3_asm.json").write_text(json.dumps(out, indent=1, default=str))
