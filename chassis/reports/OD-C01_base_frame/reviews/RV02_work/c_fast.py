import json, math, struct, zipfile, re
from pathlib import Path
import numpy as np
from build123d import import_step, Pos, Rot, Cylinder, Box, Align, Cone, Compound, Solid
from tools.core import validity, common_volume, compare_step, write_step, write_stl
from tools.measure import (envelope, feature_census, bore_census, locate_bore, clearance,
                           mesh_census, mesh_deviation)
from tools.drawing import write_sections
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame"); WK = W/"reviews/RV02_work"
M = WK/"mutants"; M.mkdir(exist_ok=True)
part = Solid(import_step(str(W/"02_STEP_STL/od_c01_frame_C1_v03.step")).wrapped)
part.label = "od_c01_frame"
asm  = import_step(str(W/"02_STEP_STL/od_c01_assembly_C1_v03.step"))
P = {c.label: c for c in asm.children}
out={}
def note(fam, mutant, got, required, fails):
    out.setdefault(fam, []).append(dict(mutant=mutant, got=got, required=required,
                                        got_word="FAIL" if fails else "PASS"))
    print(f"[{fam}] {mutant}\n    got {got} | need {required} -> {'FAIL' if fails else 'NO-FAIL'}", flush=True)
Y=(0,1,0)
def drill(sh,x,z,d=4.0): return sh - Pos(x,-3,z)*Rot(90,0,0)*Cylinder(d/2, 6.4)

# 1 RESIZE -> envelope
m = part + Pos(0,-3,100.25)*Box(200,6,0.5)
e = envelope(m)
note("envelope (U-02, D-02, REQ-07, REQ-08)", "resize: a 0.5 mm strip added on the front edge",
     f"size_z {e['size_z'].measured:.3f} mm", "405.0 +-0.1 mm", abs(e['size_z'].measured-405.0)>0.105)

# 2 RELOCATE -> locate_bore offset
m = Pos(0.5,0,0)*part
r = locate_bore(bore_census(m), (104.5,0.0,-15.0), Y)
note("locate_bore offset (REQ-01..06, REQ-10..14, U-03, U-05)",
     "relocate: the whole plate moved +0.5 mm in x, so every hole sits 0.5 mm off its spec position",
     f"offset {r['offset'].measured:.4f} mm at the REQ-13 hole (104.5, -15)", "<= 0.10 mm",
     r['offset'].measured > 0.105)

# 3 REMOVE/ADD -> bore + feature census, and locate_bore diameter
m = drill(part, 88, -78, 6.0)          # the REQ-11 hole at (88,-78) opened out to Dia 6.0
bc = bore_census(m); fc = feature_census(m)
rb = locate_bore(bc,(88,0.0,-78),Y)
note("bore_census / feature_census (U-05)", "degrade: the REQ-11 hole (88,-78) opened out to Dia 6.0",
     f"{bc.measured} bores, {fc['cylinder_faces'].measured} cylindrical faces, that bore Dia {rb['diameter'].measured:.3f}",
     "44 bores, 48 cylindrical faces, Dia 4.0 +- 0.05",
     bc.measured!=44 or fc['cylinder_faces'].measured!=48 or abs(rb['diameter'].measured-4.0)>0.055)
note("locate_bore diameter / depth (D-04a, D-05b)", "degrade: the REQ-11 hole (88,-78) opened out to Dia 6.0",
     f"Dia {rb['diameter'].measured:.3f} mm", "4.0 +- 0.05 mm", abs(rb['diameter'].measured-4.0)>0.055)
write_step(m, M/"c3_hole_opened.step", timestamp="2026-10-05T00:00:00")
c = compare_step(part, M/"c3_hole_opened.step")
note("compare_step (U-04)", "remove: the delivered solid read back against the opened-hole STEP",
     f"faces_delta {c['faces_delta'].measured}, volume_delta {c['volume_delta'].measured:.3f} mm3",
     "faces_delta 0, volume_delta <= 0 (band 0.001 mm3)",
     c['faces_delta'].measured!=0 or c['volume_delta'].measured>0.001)
m2 = Solid(part.wrapped); m2.label = "not_od_c01_frame"
write_step(m2, M/"c3b_relabelled.step", timestamp="2026-10-05T00:00:00")
c2 = compare_step(part, M/"c3b_relabelled.step")
note("compare_step labels (U-04)", "remove: the body relabelled `not_od_c01_frame`",
     f"labels {c2['labels'].measured}", "labels == 1 (kept)", c2['labels'].measured!=1)

# 4 ADD a second solid -> validity
m = Compound(children=[Solid(part.wrapped), Pos(0,50,0)*Box(10,10,10)])
v = validity(m)
note("validity (U-01)", "add: a detached 10 mm cube 50 mm above the plate",
     f"solid_count {v['solid_count'].measured}, brep_valid {v['brep_valid'].measured}, naked_edges {v['naked_edges'].measured}",
     "1 / 1 / 0", v['solid_count'].measured!=1)

# 5 RELOCATE a mate -> clearance and interference
sunk = Pos(0,-1,0)*P["od_c04_mount"]; lift = Pos(0,1,0)*P["od_c04_mount"]
iv = common_volume(P["od_c01_frame"], sunk)
note("interference / common_volume (U-03)", "relocate: OD-C04 sunk 1 mm into the plate",
     f"{iv.measured:.1f} mm3 ({iv.status})", "<= 0 mm3",
     str(iv.status)=="MEASURED" and iv.measured>0.001)
cl = clearance(P["od_c01_frame"], lift)
note("clearance (U-03, REQ-08)", "relocate: OD-C04 lifted 1 mm off the plate",
     f"contact clearance {cl.measured:.4f} mm", "= 0 (designed contact)", abs(cl.measured)>0.005)
sh8 = Pos(0.5,0,0)*P["od_c08_tray"]
b8=[b for b in bore_census(sh8).detail["bores"] if abs(b["diameter"]-3.4)<1e-6 and abs(abs(b["axis_dir"][1])-1)<1e-9]
own=min(b8,key=lambda b:(b["start"][0]-88)**2+(b["start"][2]+222)**2)
off=math.hypot(own["start"][0]-88, own["start"][2]+222)
note("coaxiality: bore_census + locate_bore on both solids (U-03)",
     "relocate: OD-C08 shifted 0.5 mm in x over its plate holes",
     f"coaxial offset {off:.4f} mm", "<= 0.20 mm", off>0.205)

# 6 DEGRADE the mesh -> write_stl / sagitta / deviation / census / 3MF
w = write_stl(part, str(M/"c6_coarse.stl"), tolerance=0.05, angular_tolerance=0.5)
sag = w.checks["max_sagitta"]
note("write_stl / mesh sagitta (U-07)", "degrade: the part remeshed at tolerance 0.05 mm",
     f"sagitta {sag.measured:.6f} mm", "<= 0.01 mm", sag.measured>0.015)
dev = mesh_deviation(str(M/"c6_coarse.stl"), part)
note("mesh_deviation (U-07, V-05)", "degrade: the coarse STL against the B-rep",
     f"{dev.measured:.6f} mm", "<= 0.01 mm", dev.measured>0.015)
raw=(W/"02_STEP_STL/od_c01_frame_C1_v03.stl").read_bytes(); n=struct.unpack("<I",raw[80:84])[0]
(M/"c6b_open.stl").write_bytes(raw[:80]+struct.pack("<I",n-20)+raw[84:84+50*(n-20)])
mc=mesh_census(str(M/"c6b_open.stl"))
note("mesh_census (U-07, V-05)", "remove: 20 triangles dropped from the delivered STL",
     f"bodies {mc['bodies'].measured}, naked_edges {mc['naked_edges'].measured}, winding {mc['winding'].measured}",
     "1 body, 0 naked edges, winding 1", mc['naked_edges'].measured!=0)
cr=(M/"c6_coarse.stl").read_bytes(); cn=struct.unpack("<I",cr[80:84])[0]
with zipfile.ZipFile(W/"02_STEP_STL/od_c01_frame_C1_v03.3mf") as z:
    xml=z.read([x for x in z.namelist() if x.endswith(".model")][0]).decode()
mt=len(re.findall(r'<triangle ',xml))
note("3MF parse against the STL (U-07)", "degrade: the 3MF compared with the coarse (tol 0.05) mesh",
     f"3MF {mt} triangles vs mesh {cn}", "the same triangle set", mt!=cn)

# 7 RELOCATE -> hole spacing (REQ-11..14)
m = drill(part, 92.0, 77.0)
ax=[(b["start"][0],b["start"][2]) for b in bore_census(m).detail["bores"]]
own=min(ax,key=lambda a:(a[0]-95)**2+(a[1]-77)**2)
d=min(math.hypot(a[0]-own[0],a[1]-own[1]) for a in ax if a is not own)
note("hole spacing from bore axes (REQ-11..14)",
     "add: an extra Dia 4.0 hole at (92, 77), 3.0 mm from the REQ-14 hole at (95, 77)",
     f"nearest centre to centre {d:.4f} mm", ">= 6.0 mm", d<5.995)

# 8 nothing_clipped
ws = write_sections(part, str(M), part="c8_clipped", version=3, views=("front",),
                    through=(0,-3,0), margin_mm=-8.0)
nc = ws[0].checks["nothing_clipped"]
note("nothing_clipped (D6 sections)", "degrade: the plan section redrawn with a negative margin",
     f"{nc.measured} px ({nc.status})", "== 0 px", str(nc.status)!="MEASURED" or nc.measured!=0)

json.dump(out, open(WK/"c_fast.json","w"), indent=1, default=str)
print("\n--- summary ---")
for fam, rows in out.items(): print(fam, "->", ", ".join(r["got_word"] for r in rows))
