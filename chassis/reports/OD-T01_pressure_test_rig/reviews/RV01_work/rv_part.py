"""RV01 reviewer: part rows on the delivered STEP (independent)."""
import json, sys, time
from pathlib import Path
from tools.core import read_step, validity, compare_step, step_roundtrip, mesh_sagitta, solids
from tools.core.step import labels, read_schema
from tools.measure import (envelope, feature_census, bore_census, locate_bore, min_wall,
                           min_wall_wide, overhang_census, flat_ceiling_spans, mesh_census,
                           mass_properties)
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SHELL, TopAbs_SOLID, TopAbs_FACE
from tools.core.shapes import occ

J = Path("/root/oguz-jobs/20261002-od-t01-pressure-test-rig")
W = J / "reviews/RV01_work"
step = Path(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1] else J / "02_STEP_STL/od_t01_rig_C1_v01.step"
tag = sys.argv[2] if len(sys.argv) > 2 else "nominal"
which = sys.argv[3].split(",") if len(sys.argv) > 3 else ["all"]
out = {}
def R(r): return r.to_dict()
t0 = time.time()
rig = read_step(step)
out["labels"] = labels(rig)
out["schema"] = read_schema(step)
v = validity(rig); out["validity"] = {k: R(x) for k, x in v.items()}
env = envelope(rig); out["envelope"] = {k: R(x) for k, x in env.items()}
# stray shells: shells not inside a solid
s = occ(rig); nsh = 0; e = TopExp_Explorer(s, TopAbs_SHELL, TopAbs_SOLID)
while e.More(): nsh += 1; e.Next()
nf = 0; e = TopExp_Explorer(s, TopAbs_FACE, TopAbs_SHELL)
while e.More(): nf += 1; e.Next()
out["stray_shells"] = nsh; out["stray_faces"] = nf
def want(k): return "all" in which or k in which
if want("census"):
    fc = feature_census(rig); out["feature_census"] = {k: {kk: vv for kk, vv in R(x).items() if kk != "detail"} for k, x in fc.items()}
    bc = bore_census(rig); out["bore_census"] = R(bc)
    loc = {}
    for nm, pt in [*[(f"screw_{sx}{sz}", (sx*44.0, 136.5, sz*44.0)) for sx in (1,-1) for sz in (1,-1)],
                   *[(f"cbore_{sx}{sz}", (sx*44.0, 144.0, sz*44.0)) for sx in (1,-1) for sz in (1,-1)],
                   ("window", (0.0, 142.5, 0.0)),
                   *[(f"bench_{sx}{sz}", (sx*105.0, 5.0, sz*40.0)) for sx in (1,-1) for sz in (1,-1)]]:
        loc[nm] = {k: R(x) for k, x in locate_bore(bc, pt, (0, 1, 0)).items()}
    out["locate"] = loc
    out["mass"] = {k: R(x) for k, x in mass_properties(rig, 1240).items()}
if want("wall"):
    out["min_wall"] = R(min_wall(rig)); out["min_wall_wide"] = R(min_wall_wide(rig))
if want("overhang"):
    out["overhang_raw"] = R(overhang_census(rig, build_dir=(0, 0, 1), min_deg=45))
if want("bridge"):
    out["flat_ceiling"] = R(flat_ceiling_spans(rig, build_dir=(0, 0, 1), max_span=5.0))
if want("rt"):
    out["compare_delivered"] = {k: R(x) for k, x in compare_step(rig, step).items()}
    out["roundtrip"] = {k: R(x) for k, x in step_roundtrip(rig, W / f"rt_{tag}.step", timestamp="2026-10-03T00:00:00").items()}
out["seconds"] = time.time() - t0
(W / f"part_{tag}_{'_'.join(which)}.json").write_text(json.dumps(out, indent=1, default=str))
print(json.dumps({k: out[k] for k in out if k not in ("bore_census",)}, default=str)[:6000])
