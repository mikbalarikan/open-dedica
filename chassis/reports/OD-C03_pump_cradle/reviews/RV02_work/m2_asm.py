import json, math
from pathlib import Path
from build123d import Location, Pos
from tools.core.step import read_step
from tools.core import common_volume
from tools.measure import clearance, interference, mass_properties
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle")
OUT = W/"reviews/RV02_work/m2_asm.json"
part = read_step(W/"02_STEP_STL/od_c03_cradle_C1_v02.step")
asm = read_step(W/"02_STEP_STL/od_c03_assembly_C1_v02.step")
pump_in = read_step(W/"00_Spec/inputs/OD-H01_ulka_ep5_pump.step")
ch = {c.label: c for c in asm.children}
cr, pu, sl = ch["od_c03_cradle"], ch["OD_H01_ulka_ep5_pump"], ch["od_h02_sleeve_assumed_A03"]
d = lambda r: r.to_dict()
o = {}
# identity checks
mp_in = mass_properties(pump_in, 1000); mp_as = mass_properties(pu, 1000)
o["pump_com_input"] = {k: v.measured for k, v in mp_in.items()}
o["pump_com_asm"] = {k: v.measured for k, v in mp_as.items()}
o["cradle_asm_vs_part_common"] = d(common_volume(cr, part))
o["cradle_asm_volume"] = cr.volume; o["part_volume"] = part.volume
o["pump_asm_vs_input_common"] = d(common_volume(pu, pump_in))
# gates
o["clr_part_pump_input"] = d(clearance(part, pump_in))
o["clr_asm_cradle_pump"] = d(clearance(cr, pu))
o["clr_part_sleeve"] = d(clearance(part, sl))
o["interf"] = {k: d(v) for k, v in interference({"cradle": part, "pump": pump_in, "sleeve": sl}).items()}
o["interf_asm_cradle_pump"] = d(common_volume(cr, pu))
# per face clearance to pump and to sleeve
pf = []
for i, f in enumerate(part.faces()):
    a = clearance(f, pump_in); b = clearance(f, sl)
    pf.append({"i": i, "type": str(f.geom_type), "pump": a.measured, "pump_at": a.at, "pump_on_b": a.detail.get("on_b"),
               "sleeve": b.measured, "sleeve_at": b.at})
o["per_face"] = pf
# sleeve solids separately against each saddle
from tools.core.shapes import solids
o["sleeve_solids"] = []
for s in sl.solids():
    o["sleeve_solids"].append({"bbox": str(s.bounding_box()), "vol": s.volume, "clr": d(clearance(part, s))})
# assembly path: pump + sleeve lowered along +Y from above (-Y)
path = []
for dy in (-60, -40, -30, -20, -10, -5, -3, -2, -1, -0.5, -0.1, 0.0):
    p = pump_in.moved(Location((0, dy, 0))); s = sl.moved(Location((0, dy, 0)))
    path.append({"dy": dy, "clr_pump": clearance(part, p).measured, "clr_sleeve": clearance(part, s).measured,
                 "int_pump": common_volume(part, p).measured, "int_sleeve": common_volume(part, s).measured})
o["path"] = path
OUT.write_text(json.dumps(o, indent=1, default=str)); print("done")
