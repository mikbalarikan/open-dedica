import json, math, struct, zipfile, re, copy
from pathlib import Path
import numpy as np
from build123d import (import_step, Pos, Cylinder, Box, Align, Location, Plane, Rot,
                       Compound, Solid, Cone)
from tools.core import validity, common_volume, compare_step, write_step, write_stl
from tools.measure import (envelope, feature_census, bore_census, locate_bore, clearance,
                           min_wall, min_wall_wide, overhang_census, flat_ceiling_spans,
                           radial_extent, mesh_census, mesh_deviation)
from tools.drawing import write_sections, nothing_clipped
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame"); WK = W/"reviews/RV02_work"
OUTNAME="r12b_slow.json"
M = WK/"mutants"; M.mkdir(exist_ok=True)
part = import_step(str(W/"02_STEP_STL/od_c01_frame_C1_v03.step"))
asm  = import_step(str(W/"02_STEP_STL/od_c01_assembly_C1_v03.step"))
P = {c.label: c for c in asm.children}
out = {}
def note(fam, mutant, got, required, fails):
    out.setdefault(fam, []).append(dict(mutant=mutant, got=got, required=required,
                                        result="FAIL" if fails else "PASS (control did NOT fail)"))
    print(f"[{fam}] {mutant}: {got}  (need {required}) -> {'FAIL' if fails else 'NO-FAIL'}")

Y = (0,1,0)
def plug(sh,x,z,d=4.0):   # fill a hole with an oversize slug so no face is coincident
    return (sh + Pos(x,-3,z)*Cylinder(d/2+0.5, 6.0)).clean()
def drill(sh,x,z,d=4.0):
    return (sh - Pos(x,-3,z)*Cylinder(d/2, 6.2)).clean()

# --- M1 resize: front edge pushed +0.5 in z  (envelope family)
m1 = part + Pos(0,-3,100.25)*Box(200,6,0.5)
e = envelope(m1); note("envelope / U-02, D-02", "M1 resize: front edge +0.5 in z",
     f"size_z {e['size_z'].measured:.3f}", "405.0 +-0.1", abs(e['size_z'].measured-405.0)>0.1+0.005)

# --- M2 relocate: REQ-13 hole (104.5, -15) moved 0.5 mm in x (locate_bore family)
m2 = drill(plug(part,104.5,-15), 105.0, -15)
r = locate_bore(bore_census(m2), (104.5,0,-15), Y)
note("bore_census + locate_bore / U-05, REQ-01..14", "M2 relocate: hole (104.5,-15) moved +0.5 mm in x",
     f"offset {r['offset'].measured:.4f} mm", "<= 0.10", r['offset'].measured > 0.10+0.005)

# --- M3 remove: REQ-11 hole (88,-78) filled in  (feature_census / compare_step family)
m3 = plug(part,88,-78)
fc = feature_census(m3); bcm = bore_census(m3)
note("feature_census / bore_census / U-05", "M3 remove: insert hole (88,-78) filled",
     f"{bcm.measured} bores, {fc['cylinder_faces'].measured} cylindrical faces",
     "44 bores, 48 cylindrical faces", bcm.measured!=44 or fc['cylinder_faces'].measured!=48)
write_step(m3, M/"m3_hole_removed.step", timestamp="2026-10-05T00:00:00")
c = compare_step(part, M/"m3_hole_removed.step")
note("compare_step / U-04", "M3 remove: delivered solid vs hole-removed STEP",
     f"faces_delta {c['faces_delta'].measured}, volume_delta {c['volume_delta'].measured:.3f} mm3",
     "faces_delta 0, volume_delta <= 0 (band 0.001)",
     c['faces_delta'].measured!=0 or c['volume_delta'].measured>0.001)
# relabelled body
m3b = Solid(part.wrapped); m3b.label = "not_od_c01_frame"
write_step(m3b, M/"m3b_relabelled.step", timestamp="2026-10-05T00:00:00")
c2 = compare_step(part, M/"m3b_relabelled.step")
note("compare_step / U-04", "M3b relabelled body `not_od_c01_frame`",
     f"labels {c2['labels'].measured}", "labels == 1", c2['labels'].measured!=1)

# --- M4 degrade: OD-C07 hole (-113,-42) moved out to x -117.5 (min_wall / radial_extent)
m4 = drill(plug(part,-113,-42), -117.5, -42)
write_step(m4, M/"m4_thin_web.step", timestamp="2026-10-05T00:00:00")
mw = min_wall(m4, spacing=0.7); mww = min_wall_wide(m4, spacing=0.7)
note("min_wall / D-01a, D-01b, D-06a, J-05", "M4 degrade: hole moved to x -117.5 (2.5 web)",
     f"min_wall {mw.measured:.4f} mm at {mw.at}", ">= 2.0 (D-01b)", mw.measured < 2.0-0.005)
note("min_wall_wide / U-06", "M4 degrade: hole moved to x -117.5",
     f"{mww.measured:.4f} mm", ">= 2.0", mww.measured < 2.0-0.005)
least=None
for a in range(0,360,5):
    rr = radial_extent(m4, (-117.5,-6.0,-42.0), Y, (1,0,0), float(a), 5.5, side="outer")
    if str(rr.status)=="MEASURED" and (least is None or rr.measured<least): least=rr.measured
note("radial_extent / D-05a, J-05 ring", "M4 degrade: hole moved to x -117.5",
     f"{2*least:.4f} mm across (ring {least-2:.4f})", ">= 8.0 across; ring >= 3.0", 2*least < 8.0-0.005)

# --- M5 overhang: 90-deg countersink cut up from the bottom face of a drain hole
m5 = part - Pos(-80,-6,-120)*Cone(6.0, 2.0, 4.0, align=(Align.CENTER,Align.MIN,Align.CENTER))
oh = overhang_census(m5, build_dir=Y, spacing=0.7)
note("overhang_census / D-03a", "M5 degrade: countersink cut up from the bed face at the drain (-80,-120)",
     f"least {oh.measured:.3f} deg at {oh.at} ({oh.status})", ">= 45 deg",
     str(oh.status)!="MEASURED" or oh.measured < 45.0-0.001)

# --- M6 bridge: 10 mm wide pocket in the bottom face -> 10 mm flat ceiling off the bed
m6 = part - Pos(0,-6,-160)*Box(10,2,60, align=(Align.CENTER,Align.MIN,Align.CENTER))
fs = flat_ceiling_spans(m6, build_dir=Y, max_span=5.0, spacing=0.7)
note("flat_ceiling_spans / D-03b", "M6 degrade: 10 x 2 mm pocket in the bed face at z -160",
     f"span {fs.measured:.3f} mm at {fs.at} ({fs.status})", "<= 5 mm",
     str(fs.status)!="MEASURED" or fs.measured > 5.0+0.005)


json.dump(out, open(WK/OUTNAME,"w"), indent=1, default=str)
print("\n--- summary ---")
for fam, rows in out.items():
    print(fam, "->", ", ".join(r["result"] for r in rows))
