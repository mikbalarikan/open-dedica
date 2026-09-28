#!/usr/bin/env python3
"""QA comparison: it1 vs it2 gated statistics and zones side by side, read from the two gate.json /
deviation.json files (same protocol, CHK-LIKE4LIKE). Writes qa/it1_vs_it2_gated.json."""
import json, sys
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import header, write_json
g1 = json.load(open("_it1_SUPERSEDED/qa/gate.json")); g2 = json.load(open("qa/gate.json"))
d1 = json.load(open("_it1_SUPERSEDED/qa/deviation.json")); d2 = json.load(open("qa/deviation.json"))
K = ("n", "rms", "p50", "p95", "p99", "max")
f = lambda s: {k: s[k] for k in K}
out = {"gated": {x["item"]: {"it1": f(x["stats"]), "it2": f(y["stats"]), "it1_pass": x["result"]["pass"], "it2_pass": y["result"]["pass"]}
                 for x, y in zip(g1["gated_results"], g2["gated_results"])},
       "whole_part": {k: {"it1": f(d1[k]), "it2": f(d2[k])} for k in ("scan_to_cad", "cad_to_scan", "cad_to_scan_masked", "cad_to_scan_observable")},
       "unobservable_fraction": {"it1": d1["unobservable_fraction"], "it2": d2["unobservable_fraction"]},
       "over_band_scan_to_cad_points": {"it1": d1["over_band_clusters"]["scan_to_cad"]["n_over"], "it2": d2["over_band_clusters"]["scan_to_cad"]["n_over"]},
       "over_band_cad_to_scan_points": {"it1": d1["over_band_clusters"]["cad_to_scan"]["n_over"], "it2": d2["over_band_clusters"]["cad_to_scan"]["n_over"]},
       "registration": {t: {k: g["registration"][k] for k in ("iterations", "max_iterations", "converged", "delta_deg", "delta_mm")} for t, g in (("it1", g1), ("it2", g2))},
       "datum_audit": {t: {k: g["datum_audit"][k] for k in ("angle_deg", "origin_offset_mm", "point_disagreement_p95_mm")} for t, g in (("it1", g1), ("it2", g2))},
       "zones_masked_p95_max": {z: {dn: {"it1": [d1["zones"][z][dn]["masked"]["p95"], d1["zones"][z][dn]["masked"]["max"]],
                                         "it2": [d2["zones"][z][dn]["masked"]["p95"], d2["zones"][z][dn]["masked"]["max"]]}
                                    for dn in ("scan_to_cad", "cad_to_scan")} for z in d2["zones"]}}
write_json("qa/it1_vs_it2_gated.json", {**header("it1_vs_it2_gated", "qa/scripts/it_compare_gated.py",
           ["_it1_SUPERSEDED/qa/gate.json", "_it1_SUPERSEDED/qa/deviation.json", "qa/deviation.json"], None), **out})
for k, v in out["gated"].items():
    print(k, "it1 p95 %.3f max %.3f" % (v["it1"]["p95"], v["it1"]["max"]), "| it2 p95 %.3f max %.3f" % (v["it2"]["p95"], v["it2"]["max"]))
print(out["over_band_scan_to_cad_points"], out["over_band_cad_to_scan_points"])
