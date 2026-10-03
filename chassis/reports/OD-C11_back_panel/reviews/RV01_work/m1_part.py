"""RV01 part measurements: validity, envelope, census, bores, located holes."""
import json, sys
from tools.core import read_step, validity, solid_count
from tools.measure import envelope, feature_census, bore_census, locate_bore, mass_properties
from tools.result import gate
J = "/root/oguz-jobs/20261001-od-c11-back-panel"
STEP = sys.argv[1] if len(sys.argv) > 1 else f"{J}/02_STEP_STL/od_c11_back_C1_v03.step"
p = read_step(STEP)
out = {}
def d(r): return r.to_dict()
out["validity"] = {k: d(v) for k, v in validity(p).items()}
out["envelope"] = {k: d(v) for k, v in envelope(p).items()}
out["census"] = {k: d(v) for k, v in feature_census(p).items()}
bc = bore_census(p)
out["bores"] = bc.detail["bores"]
out["bore_count"] = bc.measured
out["concave_arcs"] = bc.detail.get("concave_arcs")
loc = {}
for (x, z) in [(81, -282), (95, -282), (-81, -282), (-95, -282)]:
    loc[f"flange_{x}"] = {k: d(v) for k, v in locate_bore(bc, (x, 2.0, z), (0, 1, 0)).items()}
for x in (90, -90):
    loc[f"insert_{x}"] = {k: d(v) for k, v in locate_bore(bc, (x, 212.0, -293), (0, 1, 0)).items()}
for (x, y) in [(95, 30), (-100, 30), (-84, 30)]:
    loc[f"pass_{x}"] = {k: d(v) for k, v in locate_bore(bc, (x, y, -300.5), (0, 0, 1)).items()}
out["located"] = loc
out["mass"] = {k: d(v) for k, v in mass_properties(p, 1270).items()} if isinstance(mass_properties(p,1270), dict) else d(mass_properties(p,1270))
json.dump(out, open(sys.argv[2] if len(sys.argv) > 2 else f"{J}/reviews/RV01_work/m1_part.json", "w"), indent=1, default=str)
print(json.dumps({k: (v["measured"], v["status"]) for k, v in out["validity"].items()}))
print(json.dumps({k: v["measured"] for k, v in out["envelope"].items()}))
print(json.dumps({k: v["measured"] for k, v in out["census"].items()}))
print("bores", out["bore_count"], "arcs", out["concave_arcs"])
for b in out["bores"]:
    print(round(b["diameter"],4), b["axis_dir"], [round(c,3) for c in b["start"]], [round(c,3) for c in b["end"]], round(b["length"],4), b.get("through"), b["span_deg"])
for k, v in loc.items():
    print(k, {kk: (round(vv["measured"],4) if vv["measured"] is not None else None, vv["status"]) for kk, vv in v.items()})
print(out["mass"])
