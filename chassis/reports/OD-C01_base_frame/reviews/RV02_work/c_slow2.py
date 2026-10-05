import json
from pathlib import Path
from build123d import import_step, Solid, Pos, Rot, Box, Cone, Align
from tools.measure import overhang_census, flat_ceiling_spans
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame"); WK=W/"reviews/RV02_work"
part = Solid(import_step(str(W/"02_STEP_STL/od_c01_frame_C1_v03.step")).wrapped)
out={}
def note(fam,mut,got,req,fails):
    out.setdefault(fam,[]).append(dict(mutant=mut,got=got,required=req,got_word="FAIL" if fails else "PASS"))
    print(f"[{fam}] {mut}\n    got {got} | need {req} -> {'FAIL' if fails else 'NO-FAIL'}", flush=True)
Y=(0,1,0)
# one mutant serving D-03a and D-03b: a 10 x 2 mm pocket milled into the bed face
m = part - Pos(0,-6,-160)*Box(10,2,60, align=(Align.CENTER,Align.MIN,Align.CENTER))
oh = overhang_census(m, build_dir=Y, spacing=0.7)
print("  overhang raw:", oh.measured, oh.status, getattr(oh,"reason",None), flush=True)
note("overhang_census (D-03a)", "degrade: a 10 x 2 mm pocket milled into the bed face at z -160, leaving a flat ceiling 2 mm above the bed",
     f"least {oh.measured if oh.measured is None else round(oh.measured,3)} deg at {oh.at} ({oh.status}{': '+str(oh.reason) if getattr(oh,'reason',None) else ''})",
     ">= 45 deg", str(oh.status)!="MEASURED" or oh.measured < 44.999)
fs = flat_ceiling_spans(m, build_dir=Y, max_span=5.0, spacing=0.7)
print("  bridge raw:", fs.measured, fs.status, getattr(fs,"reason",None), flush=True)
note("flat_ceiling_spans (D-03b)", "degrade: the same 10 x 2 mm pocket in the bed face at z -160",
     f"span {fs.measured if fs.measured is None else round(fs.measured,3)} mm at {fs.at} ({fs.status}{': '+str(fs.reason) if getattr(fs,'reason',None) else ''})",
     "<= 5 mm", str(fs.status)!="MEASURED" or fs.measured > 5.005)
json.dump(out, open(WK/"c_slow2.json","w"), indent=1, default=str)
