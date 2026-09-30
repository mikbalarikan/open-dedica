import json
from pathlib import Path
from tools.core import read_step, common_volume
from tools.core.validity import validity
from tools.core.shapes import solids, faces, volume_mm3
from tools.measure import envelope, clearance, interference
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle")
part = read_step(W/"02_STEP_STL/od_c03_cradle_C1_v01.step")
pump_in = read_step(W/"00_Spec/inputs/OD-H01_ulka_ep5_pump.step")
asm = read_step(W/"02_STEP_STL/od_c03_assembly_C1_v01.step")
def walk(n, d=0):
    print("  "*d, repr(getattr(n,"label","")), type(n).__name__, len(solids(n)), round(volume_mm3(n),3) if solids(n) else None, getattr(n, "location", None))
    for c in getattr(n,"children",()) or (): walk(c, d+1)
walk(asm)
kids = {}
def collect(n):
    ch = list(getattr(n,"children",()) or ())
    if not ch: kids[n.label] = n
    for c in ch: collect(c)
collect(asm)
print(list(kids))
out = {}
def env(s): return {k: round(v.measured,4) for k,v in envelope(s).items()}
out["pump_input_validity"] = {k:(v.measured,v.status) for k,v in validity(pump_in).items()}
out["pump_input_env"] = env(pump_in); out["pump_input_vol"] = volume_mm3(pump_in)
for k,v in kids.items():
    out[f"asm_{k}_env"] = env(v); out[f"asm_{k}_vol"] = volume_mm3(v); out[f"asm_{k}_solids"]=len(solids(v))
    out[f"asm_{k}_validity"] = {a:(b.measured,b.status) for a,b in validity(v).items()}
out["part_vol"] = volume_mm3(part); out["part_env"]=env(part)
# cradle in asm vs part file
cr = [v for k,v in kids.items() if "cradle" in k][0]
out["cradle_asm_vs_part_common"] = common_volume(cr, part).to_dict()
pm = [v for k,v in kids.items() if "H01" in k or "ulka" in k.lower()][0]
out["pump_asm_vs_input_common"] = common_volume(pm, pump_in).to_dict()
sl = [v for k,v in kids.items() if "sleeve" in k][0]
# REQ-03 against my own identity placement of the input pump
c = clearance(part, pump_in); out["REQ03_part_pumpinput"] = c.to_dict()
c2 = clearance(cr, pm); out["REQ03_asm"] = c2.to_dict()
out["interf_asm"] = {k:v.to_dict() for k,v in interference({"cradle":cr,"pump":pm,"sleeve":sl}).items()}
out["interf_part_pumpinput"] = common_volume(part, pump_in).to_dict()
out["REQ04_clear"] = clearance(part, sl).to_dict()
out["REQ04_clear_asm"] = clearance(cr, sl).to_dict()
out["REQ04_interf"] = common_volume(part, sl).to_dict()
# per-solid sleeve clearance
out["sleeve_solids"] = [ (volume_mm3(s), env(s)) for s in solids(sl)]
out["sleeve_per_solid_clear"] = [clearance(part, s).to_dict() for s in solids(sl)]
json.dump(out, open(W/"reviews/RV01_work/m2_asm.json","w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
