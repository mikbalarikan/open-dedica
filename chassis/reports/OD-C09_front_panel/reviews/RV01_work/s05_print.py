"""D-01a/b, D-06a, U-06 (min_wall), D-03a, D-03b, D-05a, J-05, D-02."""
from common import *
from tools.measure import min_wall, min_wall_wide, overhang_census, flat_ceiling_spans, radial_extent, radial_profile, envelope
out = {}
s, ss = part(); P = Solid(ss[0])
def res(x):
    return {"measured": x.measured, "status": x.status, "reason": x.reason, "at": x.at,
            "detail": {k: v for k, v in x.detail.items() if k in ("wide", "gated_mm", "largest_step_mm", "sampling_bound_deg", "below_min_deg", "per_kind_least_deg", "bed_samples", "ceilings")}}
# overhang on the part, then with the four flange holes plugged (named exception)
oc = overhang_census(P, build_dir=(0, 0, -1)); out["overhang_raw"] = res(oc); print("oh raw", out["overhang_raw"], flush=True)
plug = P
for (x, z) in [(-95, 77), (-85, 77), (85, 77), (95, 77)]:
    plug = plug + cyl_y(x, z, 1.7, 0, 4)
plug = plug.solids()[0] if len(plug.solids()) == 1 else plug
out["plugged_solids"] = len(plug.solids())
oc2 = overhang_census(plug, build_dir=(0, 0, -1)); out["overhang_plugged"] = res(oc2); print("oh plug", out["overhang_plugged"], flush=True)
fc = flat_ceiling_spans(plug, build_dir=(0, 0, -1), max_span=5.0); out["bridge_plugged"] = res(fc); print("bridge plug", out["bridge_plugged"], flush=True)
fc0 = flat_ceiling_spans(P, build_dir=(0, 0, -1), max_span=5.0); out["bridge_raw"] = res(fc0); print("bridge raw", out["bridge_raw"], flush=True)
# radial: D-05a and J-05
bores = {"L": (-91.0555, 153.2349), "R": (-90.9987, 127.2515)}
for k, (x, y) in bores.items():
    prof = radial_profile(P, (x, y, 85.485), (0, 0, 1), (1, 0, 0), [2.0 * i for i in range(180)], (0.0, 6.0), margin=(0.0, 0.0), z_step=0.25, side="outer", r_min=2.0, r_max=7.0)
    mn = prof["min"]
    out["prof_" + k] = {"min": mn.measured, "at": mn.at, "status": mn.status, "reason": mn.reason, "detail_min": {kk: vv for kk, vv in mn.detail.items() if kk != "points"}}
    pts = mn.detail.get("points") or prof["max"].detail.get("points")
    out["prof_" + k]["n_points"] = len(pts) if pts else None
    # across: r(theta) + r(theta + 180) for each level
    across = None
    if pts:
        table = {}
        for p in pts:
            table[(round(p["angle_deg"], 3), round(p["z"], 4))] = p["low"]
        for (ang, z), rr in table.items():
            if ang < 180:
                o = table.get((round(ang + 180, 3), z))
                if o is not None and rr is not None:
                    v = rr + o
                    if across is None or v < across[0]:
                        across = (v, ang, z)
    out["across_" + k] = across
    print(k, out["prof_" + k], across, flush=True)
dump("s05_print.json", out)
mw = min_wall(P, spacing=0.45); out["min_wall"] = res(mw); print("mw", out["min_wall"], flush=True)
mww = min_wall_wide(P, spacing=0.45); out["min_wall_wide"] = res(mww); print("mww", out["min_wall_wide"], flush=True)
dump("s05_print.json", out)
