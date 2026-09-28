"""Bayonet lugs and rim notches (datum frame). Per 1-degree theta bin over z in [-4.6,-0.6]:
outer radius (p99 of r), and lug under-face z (p50 of z for points r in [31.8,35.0], z<-3.8).
Lug edges = where the outer radius crosses the midpoint between body (~30.6) and lug (~35.8).
Rim notches: theta span where no rim-top points (z>-0.4, r 28.4..30.2) exist; notch floor z."""
import json, numpy as np, trimesh
m = trimesh.load('intake/aligned_work.stl'); P, _ = trimesh.sample.sample_surface(m, 3000000, seed=0)
r = np.hypot(P[:, 0], P[:, 1]); z = P[:, 2]; th = np.degrees(np.arctan2(P[:, 1], P[:, 0])) % 360
out = {"bins": []}
for a in range(360):
    s = (th >= a) & (th < a + 1)
    sb = s & (z > -4.6) & (z < -0.6)
    ro = float(np.percentile(r[sb], 99)) if sb.sum() > 20 else None
    su = s & (r > 31.8) & (r < 35.0) & (z < -3.8) & (z > -6.5)
    zu = float(np.median(z[su])) if su.sum() > 20 else None
    st = s & (z > -0.4) & (r > 28.4) & (r < 30.2)
    out["bins"].append({"th": a + 0.5, "r_out": ro, "lug_under_z": zu, "rim_top_n": int(st.sum())})
b = out["bins"]; ro = np.array([x["r_out"] or 0 for x in b])
lug = ro > 33.2
# group contiguous (circular)
edges = []
for i in range(360):
    if lug[i] and not lug[i - 1]: edges.append(("start", b[i]["th"] - 0.5))
    if not lug[i] and lug[i - 1]: edges.append(("end", b[i]["th"] - 0.5))
starts = [e[1] for e in edges if e[0] == "start"]; ends = [e[1] for e in edges if e[0] == "end"]
lugs = []
for s0 in starts:
    e0 = min(ends, key=lambda e: (e - s0) % 360)
    span = (e0 - s0) % 360; idx = [int((s0 + k) % 360) for k in range(int(span))]
    core = idx[2:-2]
    lugs.append({"start_deg": s0, "end_deg": e0, "span_deg": span, "centre_deg": (s0 + span / 2) % 360,
                 "r_outer_median": float(np.median([b[i]["r_out"] for i in core])),
                 "under_z_by_deg": [[b[i]["th"], b[i]["lug_under_z"]] for i in core],
                 "under_z_median": float(np.median([b[i]["lug_under_z"] for i in core if b[i]["lug_under_z"] is not None]))})
out["lugs"] = lugs
nt = np.array([x["rim_top_n"] for x in b]); gap = nt < 5
ng = []
for i in range(360):
    if gap[i] and not gap[i - 1]:
        j = i
        while gap[j % 360]: j += 1
        ng.append({"start_deg": float(i), "end_deg": float(j % 360), "span_deg": float(j - i)})
out["rim_notches"] = ng
for n in ng:
    c = (n["start_deg"] + n["span_deg"] / 2); s = (np.abs(((th - c + 180) % 360) - 180) < n["span_deg"] / 2 - 1.5) & (r > 28.4) & (r < 30.2) & (z > -3)
    n["floor_z_p90"] = float(np.percentile(z[s], 90)) if s.sum() else None
json.dump(out, open('measure/figures/lugs_notches.json', 'w'), indent=1)
for L in lugs: print({k: (round(v, 2) if isinstance(v, float) else v) for k, v in L.items() if k != "under_z_by_deg"}, [ (round(t),round(zz,2)) for t, zz in L["under_z_by_deg"][::4] if zz])
print(ng)
