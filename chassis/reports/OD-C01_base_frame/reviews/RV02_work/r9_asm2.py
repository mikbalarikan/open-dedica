import json, math
from pathlib import Path
import numpy as np
from build123d import import_step, Plane, Location, Pos
from tools.core import validity, common_volume, compare_step
from tools.measure import clearance, envelope, bore_census, locate_bore
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
part = import_step(str(W/"02_STEP_STL/od_c01_frame_C1_v03.step"))
asm = import_step(str(W/"02_STEP_STL/od_c01_assembly_C1_v03.step"))
P = {c.label: c for c in asm.children}
out={}
# ---- REQ-07 top face
tops=[]
for f in part.faces():
    try: nrm = f.normal_at(None)
    except Exception: nrm = f.normal_at()
    if abs(nrm.Y-1)<1e-9 and f.geom_type.name.lower().startswith("plane"):
        bb=f.bounding_box(); tops.append(dict(area=f.area, min_y=bb.min.Y, max_y=bb.max.Y))
out["REQ07_plusY_planar_faces"]=tops
out["REQ07_count"]=len(tops)
out["envelope_part"]={k:v.measured for k,v in envelope(part).items()}
# ---- U-03 coaxiality: plate Ø4.0 bores vs each placed part's plate-facing Ø3.4 bores
pbc = bore_census(P["od_c01_frame"])
EXP = {
 "od_c03_cradle":[(-4,-239),(-4,-171),(37,-239),(37,-171)],
 "od_c04_mount":[(-40,-148),(40,-148),(-40,-114),(40,-114)],
 "od_c07_valve_mount":[(-113,-42),(-71,-42),(-113,-148.5),(-71,-148.5)],
 "od_c08_tray":[(88,-222),(106,-222),(88,-78),(106,-78)],
 "od_c11_back_panel":[(-81,-282),(81,-282),(-95,-282),(95,-282)],
 "od_c09_front_panel":[(-85,77),(85,77),(-95,77),(95,77)],
 "od_c16_r_z-262_bracket":[(104.5,-262)], "od_c16_l_z-262_bracket":[(-104.5,-262)],
 "od_c16_r_z-15_bracket":[(104.5,-15)],   "od_c16_l_z-15_bracket":[(-104.5,-15)],
 "od_c16_r_z62_bracket":[(104.5,62)],     "od_c16_l_z62_bracket":[(-104.5,62)],
}
coax={}
for name, pts in EXP.items():
    bc = bore_census(P[name])
    b34=[b for b in bc.detail["bores"] if abs(b["diameter"]-3.4)<1e-6
         and abs(abs(b["axis_dir"][1])-1)<1e-9]
    rows=[]
    for (x,z) in pts:
        own=min(b34, key=lambda b:(b["start"][0]-x)**2+(b["start"][2]-z)**2) if b34 else None
        pl = locate_bore(pbc,(x,0.0,z),(0,1,0))
        if own is None:
            rows.append(dict(at=[x,z], err="no Dia3.4 Y-axis bore in part")); continue
        ax=[own["start"][0], own["start"][2]]
        rows.append(dict(at=[x,z], part_axis=[round(ax[0],6),round(ax[1],6)],
            part_dia=round(own["diameter"],6), part_len=round(own["length"],6),
            plate_dia=round(pl["diameter"].measured,6),
            plate_off_from_nom=round(pl["offset"].measured,9),
            coax_offset=round(math.hypot(ax[0]-x, ax[1]-z),9)))
    coax[name]=dict(n_dia34_Y=len(b34), rows=rows,
                    worst_coax=max((r.get("coax_offset",9e9) for r in rows)))
out["coaxiality"]=coax
out["worst_coax_all"]=max(v["worst_coax"] for v in coax.values())
# ---- U-03 assembly path: lower each seated part along -Y from a lift
SEATED=list(EXP)+["od_c05_foot_reference_A01"]
path={}
plate=P["od_c01_frame"]
for name in SEATED:
    r={}
    for lift in (10.0,1.0,0.1,0.0):
        moved = Pos(0,lift,0)*P[name]
        c = clearance(plate, moved)
        cv = common_volume(plate, moved)
        r[str(lift)]=dict(clr=round(c.measured,9), clr_st=str(c.status),
                          common=cv.measured, common_st=str(cv.status))
    path[name]=r
out["assembly_path"]=path
out["path_worst_dev"]=max(abs(v[str(l)]["clr"]-l) for v in path.values() for l in (10.0,1.0,0.1,0.0))
out["path_max_common"]=max(v[str(l)]["common"] for v in path.values() for l in (10.0,1.0,0.1,0.0) if isinstance(v[str(l)]["common"],(int,float)))
# ---- OD-H11 and OD-H01 envelopes
for n in ("od_h11_thermoblock","od_h01_pump","od_g01_housing","od_c07_valve_mount",
          "od_c08_tray","od_c09_front_panel","od_c11_back_panel"):
    out.setdefault("envelopes",{})[n]={k:round(v.measured,6) for k,v in envelope(P[n]).items()}
# ---- U-04 assembly per part
out["compare_asm"]={}
cmp_ = compare_step(asm, W/"02_STEP_STL/od_c01_assembly_C1_v03.step")
out["compare_asm"]={k:dict(m=getattr(v,"measured",None),st=str(getattr(v,"status",None)),
                           why=getattr(v,"reason",None)) for k,v in cmp_.items()}
json.dump(out, open(W/"reviews/RV02_work/r9_asm2.json","w"), indent=1, default=str)
print("REQ-07 +Y planar faces:", out["REQ07_count"], tops)
print("worst coax offset over all 1.3 + mount parts:", out["worst_coax_all"])
print("path worst |clearance - lift|:", out["path_worst_dev"], " max common:", out["path_max_common"])
print("compare_asm:", {k:(v['m'],v['st']) for k,v in out["compare_asm"].items()})
print("OD-H11 env:", out["envelopes"]["od_h11_thermoblock"])
