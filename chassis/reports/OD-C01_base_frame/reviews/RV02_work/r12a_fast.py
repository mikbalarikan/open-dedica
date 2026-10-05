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
OUTNAME="r12a_fast.json"
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

# --- M7 validity: a second, detached solid
m7 = Compound(children=[part.copy(), Pos(0,50,0)*Box(10,10,10)])
v = validity(m7)
note("validity / U-01", "M7: a second detached 10 mm cube added",
     f"solid_count {v['solid_count'].measured}, brep_valid {v['brep_valid'].measured}, naked {v['naked_edges'].measured}",
     "1 / 1 / 0", v['solid_count'].measured!=1)

# --- M8 clearance & interference: OD-C04 sunk 1 mm into the plate; and lifted 1 mm
sunk = Pos(0,-1,0)*P["od_c04_mount"]; lift = Pos(0,1,0)*P["od_c04_mount"]
cs = clearance(P["od_c01_frame"], sunk); iv = common_volume(P["od_c01_frame"], sunk)
note("interference (common_volume) / U-03", "M8a relocate: OD-C04 sunk 1 mm into the plate",
     f"{iv.measured:.3f} mm3 ({iv.status})", "<= 0 mm3",
     str(iv.status)=="MEASURED" and iv.measured > 0.001)
cl = clearance(P["od_c01_frame"], lift)
note("clearance / U-03, REQ-08", "M8b relocate: OD-C04 lifted 1 mm off the plate",
     f"contact clearance {cl.measured:.4f} mm", "= 0 (designed contact)", abs(cl.measured) > 0.005)
# coaxiality control: OD-C08 shifted 0.5 mm in x
sh8 = Pos(0.5,0,0)*P["od_c08_tray"]
b8=[b for b in bore_census(sh8).detail["bores"] if abs(b["diameter"]-3.4)<1e-6 and abs(abs(b["axis_dir"][1])-1)<1e-9]
own=min(b8,key=lambda b:(b["start"][0]-88)**2+(b["start"][2]+222)**2)
off=math.hypot(own["start"][0]-88, own["start"][2]+222)
note("coaxiality (locate_bore on both solids) / U-03", "M8c relocate: OD-C08 shifted 0.5 mm in x",
     f"coaxial offset {off:.4f} mm", "<= 0.20", off > 0.20+0.005)

# --- M9 mesh: coarse STL at tolerance 0.05
w = write_stl(part, str(M/"m9_coarse.stl"), tolerance=0.05, angular_tolerance=0.5)
sag = w.checks["max_sagitta"]
note("write_stl / mesh_sagitta / U-07", "M9 degrade: STL remeshed at tolerance 0.05",
     f"sagitta {sag.measured:.6f} mm", "<= 0.01", sag.measured > 0.01+0.005)
dev = mesh_deviation(str(M/"m9_coarse.stl"), part)
note("mesh_deviation / U-07", "M9 degrade: coarse STL vs B-rep",
     f"{dev.measured:.6f} mm", "<= 0.01", dev.measured > 0.01+0.005)
# mesh_census on an open mesh: drop 20 triangles
raw=(W/"02_STEP_STL/od_c01_frame_C1_v03.stl").read_bytes()
n=struct.unpack("<I",raw[80:84])[0]
(M/"m9b_open.stl").write_bytes(raw[:80]+struct.pack("<I",n-20)+raw[84:84+50*(n-20)])
mc=mesh_census(str(M/"m9b_open.stl"))
note("mesh_census / U-07 (V-05)", "M9b remove: 20 triangles dropped from the delivered STL",
     f"bodies {mc['bodies'].measured}, naked_edges {mc['naked_edges'].measured}",
     "1 body, 0 naked edges", mc['naked_edges'].measured!=0)
# 3MF-vs-STL comparison control: compare the 3MF with the coarse mesh instead
cr=(M/"m9_coarse.stl").read_bytes(); cn=struct.unpack("<I",cr[80:84])[0]
with zipfile.ZipFile(W/"02_STEP_STL/od_c01_frame_C1_v03.3mf") as z:
    xml=z.read([x for x in z.namelist() if x.endswith(".model")][0]).decode()
mt=len(re.findall(r'<triangle ',xml))
note("3MF parse vs STL / U-07", "M9c: 3MF compared with the coarse (tol 0.05) mesh",
     f"3MF {mt} triangles vs mesh {cn}", "equal triangle sets", mt!=cn)

# --- M13 nothing_clipped control: section drawn with no margin
ws = write_sections(part, str(M), part="m13_clipped", version=3, views=("front",),
                    through=(0,-3,0), margin_mm=-6.0)
nc = ws[0].checks["nothing_clipped"]
note("nothing_clipped / D6 sections", "M13: plan section redrawn with a negative margin",
     f"{nc.measured} px ({nc.status})", "== 0 px", str(nc.status)!="MEASURED" or nc.measured!=0)

# --- M12 hole spacing control: REQ-14 hole (95,77) moved to (88,77) -> c2c 3.0
m12 = drill(plug(part,95,77), 88, 77)
ax=[(b["start"][0],b["start"][2]) for b in bore_census(m12).detail["bores"]]
own=min(ax,key=lambda a:(a[0]-88)**2+(a[1]-77)**2)
d=min(math.hypot(a[0]-own[0],a[1]-own[1]) for a in ax if a is not own)
note("hole spacing (bore axes) / REQ-11..14", "M12 relocate: hole (95,77) moved to (88,77)",
     f"nearest centre to centre {d:.4f} mm", ">= 6.0", d < 6.0-0.005)


json.dump(out, open(WK/OUTNAME,"w"), indent=1, default=str)
print("\n--- summary ---")
for fam, rows in out.items():
    print(fam, "->", ", ".join(r["result"] for r in rows))
