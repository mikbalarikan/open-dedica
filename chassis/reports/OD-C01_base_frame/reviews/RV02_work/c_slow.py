import json, math
from pathlib import Path
from build123d import import_step, Solid, Pos, Rot, Cylinder, Box, Cone, Align
from tools.measure import min_wall, min_wall_wide, overhang_census, flat_ceiling_spans, radial_extent
from tools.core import write_step
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame"); WK=W/"reviews/RV02_work"
M = WK/"mutants"
part = Solid(import_step(str(W/"02_STEP_STL/od_c01_frame_C1_v03.step")).wrapped)
part.label="od_c01_frame"
out={}
def note(fam,mut,got,req,fails):
    out.setdefault(fam,[]).append(dict(mutant=mut,got=got,required=req,got_word="FAIL" if fails else "PASS"))
    print(f"[{fam}] {mut}\n    got {got} | need {req} -> {'FAIL' if fails else 'NO-FAIL'}", flush=True)
Y=(0,1,0)
# DEGRADE the governing web: an extra Dia 4.0 insert hole at x -117.5 -> 0.5 mm to the edge
m4 = part - Pos(-117.5,-3,-42)*Rot(90,0,0)*Cylinder(2.0, 6.4)
write_step(m4, M/"c9_thin_web.step", timestamp="2026-10-05T00:00:00")
mw = min_wall(m4, spacing=0.7)
note("min_wall (D-01a, D-01b, D-06a, J-05)",
     "degrade: an extra Dia 4.0 insert hole at (-117.5, -42), 0.5 mm from the left edge",
     f"{mw.measured:.4f} mm at {mw.at}", ">= 2.0 mm (D-01b); >= 3.0 (J-05); >= 1.0 (D-06a); >= 0.8 (D-01a)",
     mw.measured < 1.995)
mww = min_wall_wide(m4, spacing=0.7)
note("min_wall_wide (U-06)", "degrade: an extra Dia 4.0 insert hole at (-117.5, -42)",
     f"{mww.measured:.4f} mm at {mww.at}", ">= 2.0 mm", mww.measured < 1.995)
least=None; ang=None
for a in range(0,360,5):
    rr = radial_extent(m4, (-117.5,-6.0,-42.0), Y, (1,0,0), float(a), 5.5, side="outer")
    if str(rr.status)=="MEASURED" and (least is None or rr.measured<least): least, ang = rr.measured, a
note("radial_extent (D-05a, J-05 ring wall)", "degrade: an extra Dia 4.0 insert hole at (-117.5, -42)",
     f"{2*least:.4f} mm across (ring {least-2:.4f} mm) at {ang} deg", ">= 8.0 mm across; ring >= 3.0 mm",
     2*least < 7.995)
# DEGRADE the print orientation: a countersink cut up from the bed face
m5 = part - Pos(-80,-6,-120)*Rot(-90,0,0)*Cone(6.0, 2.0, 4.0, align=(Align.CENTER,Align.CENTER,Align.MIN))
oh = overhang_census(m5, build_dir=Y, spacing=0.7)
note("overhang_census (D-03a)",
     "degrade: a 30 deg countersink cut up from the bed face at the drain (-80, -120)",
     f"least {oh.measured:.3f} deg at {oh.at} ({oh.status})", ">= 45 deg",
     str(oh.status)!="MEASURED" or oh.measured < 44.999)
# DEGRADE: a 10 mm wide pocket in the bed face -> a 10 mm flat ceiling off the bed
m6 = part - Pos(0,-6,-160)*Box(10,2,60, align=(Align.CENTER,Align.MIN,Align.CENTER))
fs = flat_ceiling_spans(m6, build_dir=Y, max_span=5.0, spacing=0.7)
note("flat_ceiling_spans (D-03b)",
     "degrade: a 10 x 2 mm pocket milled into the bed face at z -160",
     f"span {fs.measured:.3f} mm at {fs.at} ({fs.status})", "<= 5 mm",
     str(fs.status)!="MEASURED" or fs.measured > 5.005)
json.dump(out, open(WK/"c_slow.json","w"), indent=1, default=str)
print("\n--- summary ---")
for k,v in out.items(): print(k,"->",", ".join(r["got_word"] for r in v))
