import json, math
from pathlib import Path
from tools.core.step import read_step
from tools.core.shapes import faces
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall, min_wall_wide,
                           overhang_census, mass_properties, radial_profile, radial_extent)
W = Path("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle")
OUT = W/"reviews/RV02_work/m1_part.json"
part = read_step(W/"02_STEP_STL/od_c03_cradle_C1_v02.step")
out = {}
d = lambda r: r.to_dict()
out["envelope"] = {k: d(v) for k, v in envelope(part).items()}
out["feature_census"] = {k: d(v) for k, v in feature_census(part).items()}
bc = bore_census(part); out["bore_census"] = d(bc)
out["locate"] = {}
for x in (-34.0, 34.0):
    for z in (-4.0, 37.0):
        out["locate"][f"{x},{z}"] = {k: d(v) for k, v in locate_bore(bc, (x, 38.5, z), (0, 1, 0)).items()}
mw = min_wall(part); out["min_wall"] = d(mw)
out["min_wall_wide"] = d(min_wall_wide(part))
out["overhang"] = d(overhang_census(part, build_dir=(0, -1, 0), min_deg=45))
out["mass"] = {k: d(v) for k, v in mass_properties(part, 1270).items()}
A = ((0, 0, 0), (0, 0, 1), (1, 0, 0))
angles = list(range(50, 131, 5))
out["req01"] = {}
for band in ((-2.5, 2.5), (25.5, 30.5)):
    rp = radial_profile(part, *A, angles, band, margin=0, z_step=0.1, side="inner")
    out["req01"][str(band)] = {k: {kk: vv for kk, vv in d(v).items() if kk != "detail"} | {"unread": d(v)["detail"].get("unread"), "on_face": d(v)["detail"].get("on_face")} for k, v in rp.items()}
out["req02"] = {}
for z in (0.0, 28.0):
    for a in (50, 130):
        out["req02"][f"inner {a} z{z}"] = d(radial_extent(part, *A, a, z, side="inner"))
    for a in (40, 140):
        out["req02"][f"win {a} z{z}"] = d(radial_extent(part, *A, a, z, side="inner", r_min=0, r_max=32.0))
        out["req02"][f"ray {a} z{z}"] = d(radial_extent(part, *A, a, z, side="inner"))
    # also just inside the sector edges and at other angles near the edges
    for a in (44, 45.5, 134.5, 136):
        out["req02"][f"win {a} z{z}"] = d(radial_extent(part, *A, a, z, side="inner", r_min=0, r_max=32.0))
# planar faces list
fl = []
for f in part.faces():
    bb = f.bounding_box()
    try:
        n = f.normal_at(); n = (round(n.X, 6), round(n.Y, 6), round(n.Z, 6))
    except Exception:
        n = None
    fl.append({"type": f.geom_type.name if hasattr(f.geom_type, "name") else str(f.geom_type), "normal": n,
               "min": (round(bb.min.X, 6), round(bb.min.Y, 6), round(bb.min.Z, 6)),
               "max": (round(bb.max.X, 6), round(bb.max.Y, 6), round(bb.max.Z, 6)), "area": round(f.area, 6)})
out["faces"] = fl
OUT.write_text(json.dumps(out, indent=1, default=str))
print("done")
