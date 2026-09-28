#!/usr/bin/env python3
"""QA comparison: for every it1 over-band cluster (bbox from _it1_SUPERSEDED/qa/deviation.json, grown 0.5 mm),
count it1 and it2 points over the 0.8 mm band inside that same box and their max distance, both directions.
Same protocol both runs (same scan, regime, masks, zones, ICP params, sampling seeds). Writes qa/it1_vs_it2_clusters.json."""
import json, sys
import numpy as np
sys.path.insert(0, "/home/user/agentic_STL-to-CAD/skills/stl-re-verify/scripts")
from _common import header, write_json
a = np.load("_it1_SUPERSEDED/qa/dev_arrays.npz"); b = np.load("qa/dev_arrays.npz")
d1 = json.load(open("_it1_SUPERSEDED/qa/deviation.json")); d2 = json.load(open("qa/deviation.json"))
out = {}
for dn, pk, dk in (("scan_to_cad", "s2c_pts", "s2c_d"), ("cad_to_scan", "c2s_pts", "c2s_d")):
    rows = []
    for src, dev in (("it1", d1), ("it2", d2)):
        for i, c in enumerate(dev["over_band_clusters"][dn]["clusters"]):
            lo, hi = np.array(c["bbox_min"]) - 0.5, np.array(c["bbox_max"]) + 0.5
            row = {"from": f"{src} cluster {i}", "n_listed": c["n"], "centroid": c["centroid"],
                   "theta": c["theta_deg_range"], "r": c["r_range"]}
            for tag, A in (("it1", a), ("it2", b)):
                P, d = A[pk], A[dk]
                m = np.all((P >= lo) & (P <= hi), axis=1)
                row[tag] = {"n_in_box": int(m.sum()), "n_over": int((d[m] > 0.8).sum()),
                            "max": round(float(d[m].max()), 3) if m.any() else None,
                            "p95": round(float(np.percentile(d[m], 95)), 3) if m.any() else None}
            rows.append(row)
    out[dn] = rows
write_json("qa/it1_vs_it2_clusters.json", {**header("it1_vs_it2_clusters", "qa/scripts/it_compare.py",
           ["_it1_SUPERSEDED/qa/dev_arrays.npz", "qa/dev_arrays.npz", "_it1_SUPERSEDED/qa/deviation.json", "qa/deviation.json"], None),
           "note": "bbox of each listed cluster grown 0.5 mm; n_over = points > 0.8 mm inside the box", **out})
for dn, rows in out.items():
    print("==", dn)
    for r in rows:
        print(f"{r['from']:15s} th {r['theta']} r {r['r']} | it1 over {r['it1']['n_over']:5d} max {r['it1']['max']} p95 {r['it1']['p95']} | it2 over {r['it2']['n_over']:5d} max {r['it2']['max']} p95 {r['it2']['p95']}")
