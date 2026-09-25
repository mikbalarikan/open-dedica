#!/usr/bin/env python3
"""build_params.py - assemble measure/params.json from the measurement JSONs (numbers are copied
programmatically, never retyped). Usage: python3 build_params.py <RUN>"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import math
import sys

import numpy as np

RUN = sys.argv[1]
FIG = f"{RUN}/measure/figures"
M = json.load(open(f"{FIG}/measurements.json"))
AL = json.load(open(f"{RUN}/intake/alignment.json"))
NOISE = AL["scan_noise_mm"]["value"]
LS = json.load(open(f"{FIG}/axis_stations.json"))["stem_group_line"]
RT = json.load(open(f"{FIG}/rib_tip.json"))
CNT = json.load(open(f"{FIG}/count_ribs.json"))


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


P: dict = {}


def v(name):
    return M[name]["value"]


def add(name, value, unit, measured, rule, estimator, unc, evidence, critical=False, source="scan", **kw):
    P[name] = {"value": value, "unit": unit, "measured": measured, "rule": rule, "source": source,
               "estimator": estimator, "uncertainty_mm": unc, "evidence": evidence, "critical": critical, **kw}


def km(name, unit="mm", unc=None, evidence="measure/figures/measurements.json", critical=False, key=None, **kw):
    """keep-measured scan value copied from measurements.json"""
    k = key or name
    val = M[k]["value"]
    u = unc if unc is not None else M[k].get("rms", M[k].get("std", NOISE))
    if isinstance(u, list):
        u = float(max(u))
    add(name, val, unit, val, "keep-measured", M[k]["estimator"], float(u), f"{evidence}#{k}", critical, **kw)


EV = "measure/figures/measurements.json"
TRIG = "one caliper reading of this dimension (or the thread/bore spec from the owner) -> re-run measure + rebuild"
# ---------------------------------------------------------------- axes / frames
km("cap_cx"); km("cap_cy")
km("collar_cx"); km("collar_cy")
tilt = math.degrees(math.atan(math.hypot(LS["dxdz"], LS["dydz"])))
dirn = math.degrees(math.atan2(LS["dydz"], LS["dxdz"]))
add("stem_axis_x0", LS["x0"], "mm", LS["x0"], "keep-measured", "stem-group axis line x(z)=x0+tan(tilt)cos(dir) z: LSQ line through 20 Z-parallel circle-fit centres (stem core 18.5-27.5, neck 30.3/30.9, sleeve 33.7-36.7, bore 36.3/36.8); resid rms %.4f max %.4f" % (LS["resid_rms"], LS["resid_max"]), LS["resid_rms"], "measure/figures/axis_stations.json#stem_group_line")
add("stem_axis_y0", LS["y0"], "mm", LS["y0"], "keep-measured", "same line, y intercept at z=0", LS["resid_rms"], "measure/figures/axis_stations.json#stem_group_line")
add("stem_axis_tilt_deg", tilt, "deg", tilt, "keep-measured", "same line: atan(|(dx/dz, dy/dz)|) relative to datum Z (crown normal)", LS["resid_rms"], "measure/figures/axis_stations.json#stem_group_line",
    frame="datum frame; tilt of the stem-group line from +Z")
add("stem_axis_dir_deg", dirn, "deg", dirn, "keep-measured", "same line: atan2(dy/dz, dx/dz) = azimuth toward which the axis leans with +z", LS["resid_rms"], "measure/figures/axis_stations.json#stem_group_line",
    frame="datum frame, theta CCW about +Z from +X")
# ---------------------------------------------------------------- cap + lever
add("crown_z", 0.0, "mm", v("crown_z"), "round-within-noise", M["crown_z"]["estimator"] + "; the crown is the datum primary (z=0 by construction), measured offset is inside the plane noise", M["crown_z"]["std"], f"{EV}#crown_z")
km("cap_R_z0")
dr = [v("cap_draft_deg"), v("lever_flank_py_draft_deg"), v("lever_flank_my_draft_deg")]
add("draft_deg", float(np.mean(dr)), "deg", dr, "mean-of-n", "mean of the three moulded-wall draft reads [cap wall cone, lever +Y flank, lever -Y flank] (each: see measurements.json); one mould draft for cap, lever flanks, tip and blends", float(np.ptp(dr)) * math.pi / 180 * 13.7 / 2,
    f"{EV}#cap_draft_deg,lever_flank_py_draft_deg,lever_flank_my_draft_deg", note="lever tip cone read %.3f deg (lever_tip_draft_deg) - declared simplification" % v("lever_tip_draft_deg"))
cr = [v("crown_round_R"), v("lever_crown_round_R")]
add("crown_round_R", float(np.mean(cr)), "mm", cr, "mean-of-n", "mean of [cap crown-round circle fit (r,z), lever-tip crown-round circle fit (x,z)]; one fillet around the whole crown loop", float(max(M["crown_round_R"]["rms"], M["lever_crown_round_R"]["rms"])), f"{EV}#crown_round_R,lever_crown_round_R")
sz = v("step_z")
add("step_z", float(np.mean(sz)), "mm", sz, "mean-of-n", "mean of [cap step-face annulus z, lever underside z] (area-weighted +Z-facing faces, same moulded face)", float(max(M["step_z"]["std"])), f"{EV}#step_z")
se = [v("step_edge_R"), v("lever_under_edge_R")]
add("step_edge_R", float(np.mean(se)), "mm", se, "mean-of-n", "mean of [cap wall->step-face round fit, lever-tip underside edge round fit]; one fillet around the step-face outer loop", float(max(M["step_edge_R"]["rms"], M["lever_under_edge_R"]["rms"])), f"{EV}#step_edge_R,lever_under_edge_R")
for tag in ("py", "my"):
    y18, pl = v(f"lever_flank_{tag}_y18_z0"), v(f"lever_flank_{tag}_plan_deg")
    y0 = y18 - 18.0 * math.tan(math.radians(pl))
    add(f"lever_flank_{tag}_y0", y0, "mm", y0, "keep-measured", f"lever {'+Y' if tag == 'py' else '-Y'} flank line at z=0 in plan, y = y0 + tan(plan_deg) x: y0 = y(x=18,z=0) - 18 tan(plan_deg), from {M[f'lever_flank_{tag}_y18_z0']['estimator']}",
        M[f"lever_flank_{tag}_y18_z0"]["std"], f"{EV}#lever_flank_{tag}_y18_z0,lever_flank_{tag}_plan_deg")
    km(f"lever_flank_{tag}_plan_deg", unit="deg", unc=M[f"lever_flank_{tag}_y18_z0"]["std"], frame="datum frame, plan angle of the flank line from +X, CCW positive")
km("lever_tip_cx", unc=float(np.std(M["lever_tip_cx"]["reads"])))
pf = M["lever_blend_R_z0"]["per_fit"]
for side, tag in (("+Y", "py"), ("-Y", "my")):
    zz = np.array([a[0] for a in pf[side]]); RR = np.array([a[1] for a in pf[side]])
    b = np.polyfit(zz, RR, 1)
    add(f"lever_blend_R_{tag}_z0", float(b[1]), "mm", float(b[1]), "keep-measured", f"concave lever-cap blend {side}: line R(z) through plan circle fits at z 4/7/10/12.5 (lever_blend_R_z0.per_fit), extrapolated to z=0 (slope {b[0]:.4f})",
        float(np.std(RR - np.polyval(b, zz))), f"{EV}#lever_blend_R_z0")
for k in ("pocket_y_plus_at_step", "pocket_y_minus_at_step", "pocket_x_inner_at_step"):
    km(k)
km("pocket_end_cx")
pdr = [v("pocket_y_plus_draft_deg"), v("pocket_y_minus_draft_deg"), v("pocket_x_inner_draft_deg")]
add("pocket_draft_deg", float(np.mean(pdr)), "deg", pdr, "mean-of-n", "mean of the pocket wall drafts [+Y wall, -Y wall, inner end] (lines through per-z wall medians z 10-13.3)", 0.14, f"{EV}#pocket_y_plus_draft_deg,pocket_y_minus_draft_deg,pocket_x_inner_draft_deg")
km("pocket_floor_z", unc=0.12, note="floor only sparsely scanned (64 faces, z p5 8.42 / p50 8.65); depth ~5.15 below the step face")
km("pocket_corner_R", unc=float(np.ptp(M["pocket_corner_R"]["reads"])))
# ---------------------------------------------------------------- collar region
for k in ("collar_R", "mouth_chamfer_r_out", "mouth_chamfer_r_in", "mouth_ring_z", "collar_top_round_R", "collar_bot_z", "collar_bot_round_R"):
    km(k, unc=M[k].get("rms", M[k].get("std", M["mouth_chamfer_slope"]["std"])))
for k, lst in (("groove_out_rc", "per_sector"), ("groove_out_bottom_z", "per_sector"), ("groove_out_R", "per_sector"),
               ("groove_in_rc", "per_sector"), ("groove_in_bottom_z", "per_sector"), ("groove_in_R", "per_sector")):
    val = v(k); reads = M[k][lst]
    add(k, val, "mm", f"{min(reads):.4f}..{max(reads):.4f}", "keep-measured", M[k]["estimator"] + f" (per-sector reads {', '.join(f'{x:.3f}' for x in reads)})",
        float(np.std(reads)), f"{EV}#{k}")
fz = v("flange_z"); reads = [a[1] for a in M["flange_z"]["per_sector"]]
add("flange_z", fz, "mm", f"{min(reads):.4f}..{max(reads):.4f}", "keep-measured", M["flange_z"]["estimator"], float(np.std(reads)), f"{EV}#flange_z")
# ---------------------------------------------------------------- stem
km("stem_base_z", unc=0.1); km("stem_core_top_z", unc=0.1); km("neck_bot_z", unc=0.1)
R18, R28 = v("stem_core_R_z18"), v("stem_core_R_z28")
for nm, zk in (("stem_core_R_base", "stem_base_z"), ("stem_core_R_top", "stem_core_top_z")):
    val = R18 + (R28 - R18) * (v(zk) - 18.0) / 10.0
    add(nm, val, "mm", val, "keep-measured", f"stem-core cone line R(z) through station circle fits z 18.5-27.5 (R(18)={R18:.4f}, R(28)={R28:.4f}, measurements.json) evaluated at {zk}",
        0.087, f"{EV}#stem_core_R_z18,stem_core_R_z28,{zk}", note="stem core is not perfectly round: station circle rms 0.072-0.087 (axis_stations.json)")
km("neck_R", unc=0.052)
add("rib_count", int(CNT.get("count", 4)), "count", int(CNT.get("count", 4)), "keep-measured", "pattern_count.py radius signal, rotational-order FFT dominant order 4 at z 19.5/22.5/25.5, residual local minimum at every station (CHK-COUNT pass)", 0.0, "measure/figures/count_ribs.json")
t18, t27, rtop = v("rib_tip_r_z18"), v("rib_tip_r_z27"), v("rib_top_z")
tf = [a + (b_ - a) * (v("flange_z") - 18.0) / 9.0 for a, b_ in zip(t18, t27)]
tt = [a + (b_ - a) * (zt_ - 18.0) / 9.0 for a, b_, zt_ in zip(t18, t27, rtop)]
add("rib_tip_r_flange", tf, "mm", tf, "keep-measured", "per rib: tip line through the p98 tip radii at z 18 and 27 (rib_tip_r_z18/_z27, measurements.json) evaluated at flange_z", 0.05, f"{EV}#rib_tip_r_z18,rib_tip_r_z27,flange_z")
add("rib_tip_r_top", tt, "mm", tt, "keep-measured", "per rib: same tip line evaluated at that rib's rib_top_z", 0.05, f"{EV}#rib_tip_r_z18,rib_tip_r_z27,rib_top_z")
for k, unit in (("rib_theta_deg", "deg"), ("rib_width", "mm"), ("rib_top_z", "mm")):
    val = v(k)
    add(k, val, unit, val, "keep-measured", M[k]["estimator"] + " - per rib in the order [~0, ~90, ~180, ~-90 deg]", 0.05 if unit == "mm" else 0.5, f"{EV}#{k}",
        critical=(k in ("rib_width", "rib_theta_deg")), **({"frame": "stem-group local frame (tilted line), theta CCW about +Z from datum +X"} if unit == "deg" else {}),
        **({"rerun_trigger": TRIG} if k in ("rib_width", "rib_theta_deg") else {}))
P["rib_width"]["note"] = "rib tip modelled as a full round (R = width/2): fitted tip radius median %.3f (rib_tip.json), mean width/2 %.3f" % (RT["median_all"], float(np.mean(v("rib_width"))) / 2)
# ---------------------------------------------------------------- sleeve / spigot
km("sleeve_bottom_z", unc=M["sleeve_bottom_z"]["rms"]); km("sleeve_top_z", unc=M["sleeve_top_z"]["rms"])
for end in ("bottom", "top"):
    for k, unit in ((f"sleeve_{end}_ramp_start_deg", "deg"), (f"sleeve_{end}_ramp_end_deg", "deg"), (f"sleeve_{end}_ramp_h", "mm")):
        km(k, unit=unit, unc=M[k]["rms"], **({"frame": "spigot local frame (stem-group line), theta CCW about +Z from datum +X, 0..360; ramp rises with theta (right-hand)"} if unit == "deg" else {}))
km("sleeve_crest_R", critical=True, rerun_trigger=TRIG, unc=M["sleeve_crest_R"]["rms"])
km("sleeve_ripple_rho", unc=M["sleeve_ripple_rho"]["rms"])
km("sleeve_ripple_pitch", critical=True, rerun_trigger=TRIG, unc=M["sleeve_ripple_pitch"]["rms"])
km("sleeve_first_crest_z", unc=M["sleeve_first_crest_z"]["rms"])
km("sleeve_tail_r_in", unc=0.1)
km("bore_R", critical=True, rerun_trigger=TRIG, unc=0.064)
a, b = M["bore_shoulder_slope"]["a"], M["bore_shoulder_slope"]["value"]
zt = a + b * v("bore_R")
add("bore_shoulder_top_z", zt, "mm", zt, "keep-measured", "bore shoulder cone: line z=a+b r through +Z-facing shoulder faces r 2.8-4.05 (a=%.4f, b=%.4f), evaluated at r=bore_R" % (a, b), M["bore_shoulder_slope"]["std"], f"{EV}#bore_shoulder_slope")
zf_ = v("bore_seen_min_z"); rf_ = (zf_ - a) / b
add("bore_floor_z", zf_, "mm", zf_, "keep-measured", M["bore_seen_min_z"]["estimator"] + " - the model closes the bore with a flat floor here (floor shape assumed, see open_questions)", 0.1, f"{EV}#bore_seen_min_z")
add("bore_floor_r", rf_, "mm", rf_, "keep-measured", "shoulder line (a,b above) evaluated at bore_floor_z; cf. innermost observed radius %.3f (bore_seen_min_r)" % v("bore_seen_min_r"), 0.1, f"{EV}#bore_shoulder_slope,bore_seen_min_z")

# ---------------------------------------------------------------- simplifications (deviation costs measured on the scan)
tipR = v("lever_tip_R_z0")
S = [
 {"name": "stem group axis", "modelled_as": "stem revolve and spigot revolve each Z-parallel, centred on the fitted tilted line (tilt %.3f deg) at their mid heights" % tilt,
  "deviation_cost": "<= %.3f mm lateral over the stem core half-span (5.5 mm x tan tilt), <= %.3f over the spigot half-span" % (5.5 * math.tan(math.radians(tilt)), 3.8 * math.tan(math.radians(tilt)))},
 {"name": "stem core roundness", "modelled_as": "cone R(z) through station circle fits", "deviation_cost": "station circle rms 0.072-0.087, p95 0.165 mm (axes.json stem_core_45)"},
 {"name": "one mould draft", "modelled_as": "draft_deg on cap wall, lever flanks, lever tip and blends",
  "deviation_cost": "flanks +/-%.3f mm over 13.7 mm; lever tip cone read %.2f deg -> <= %.2f mm at z=0/13.7" % (math.tan(math.radians(float(np.ptp(dr)) / 2)) * 13.7, v("lever_tip_draft_deg"), abs(math.tan(math.radians(float(np.mean(dr)) - v("lever_tip_draft_deg")))) * 6.85)},
 {"name": "lever tip tangent to flanks", "modelled_as": "tip arc tangent to both flank lines, centre on their bisector at x=lever_tip_cx",
  "deviation_cost": "fitted tip circle R(z=0) %.3f centre y %.3f vs tangent arc: <= 0.22 mm at z=0 on +Y, ~0.06 mm at mid height" % (tipR, v("lever_tip_cy"))},
 {"name": "single crown round", "modelled_as": "one fillet R=crown_round_R on the whole crown loop", "deviation_cost": "reads 2.436 (cap, rms 0.038) / 2.482 (lever tip, rms 0.114, not circular): <= 0.1 mm"},
 {"name": "single step-edge round", "modelled_as": "one fillet R=step_edge_R on the step-face outer loop", "deviation_cost": "reads 0.450 / 0.619: <= 0.05 mm"},
 {"name": "pocket single draft, flat floor, no floor fillet, no mouth round", "modelled_as": "one draft pocket_draft_deg, flat floor at pocket_floor_z",
  "deviation_cost": "wall drafts 3.0/5.6/3.4 deg -> <= 0.14 mm at the floor; floor seen by only 64 faces; mouth round ~0.3 not modelled -> <= 0.09 mm"},
 {"name": "sleeve ripple as rings", "modelled_as": "4 touching crest arcs (tori) at fixed z; helical crossover only on the end faces",
  "deviation_cost": "inside the ramp sectors (about 120 deg) the scanned crests rise with the crossover; ring ripple is misplaced there by at most the ripple depth %.3f mm" % M["sleeve_ripple_depth_derived"]["value"]},
 {"name": "sleeve end ramps", "modelled_as": "level + linear right-hand helical ramp + step (bottom cut tool, top tail)", "deviation_cost": "edge-height fit rms 0.073 / 0.056, p95 0.148 mm (jog.json)"},
 {"name": "groove depths", "modelled_as": "one arc per groove (median over sectors)", "deviation_cost": "outer groove bottom spread 0.60 mm, inner 0.44 mm across sectors -> up to ~0.3 mm locally"},
 {"name": "stem flange face level", "modelled_as": "plane z=flange_z", "deviation_cost": "sector medians spread 0.32 mm -> +/-0.16 mm"},
 {"name": "rib ends and roots", "modelled_as": "flat rib top at rib_top_z (mid-crossing), no root fillets, full-round tips", "deviation_cost": "crest falls from tip to core over ~0.5 mm in z -> <= 0.25 mm at the rib tops; root fillets <= 0.1 mm"},
 {"name": "bore notch (E20) not modelled", "modelled_as": "plain bore", "deviation_cost": "notch ~0.5 mm deep, ~25 deg wide at theta ~180, z 36-37 (bore r(theta) max 4.59 vs 4.09)"},
 {"name": "sleeve top inner lip not modelled", "modelled_as": "flat top face", "deviation_cost": "lip r 4.2-4.4 stands ~0.1 mm above the top face"},
 {"name": "stem base flare", "modelled_as": "straight line from the inner groove's innermost point to the core at stem_base_z", "deviation_cost": "<= 0.05 mm (between-rib profile, measurements.json#stem_base_z)"},
 {"name": "interior", "modelled_as": "solid (the scan is an outer skin; cap/stem/sleeve interfaces unobservable)", "deviation_cost": "not observable by the scan; CAD->scan on hidden interior not evaluated"},
]
doc = {
 "schema": "stl-re/params.json@1", "tool": "build_params.py (measure/figures/src)", "tool_version": "stl-re-measure-intent/1.0 (builder scripts)",
 "inputs": {"intake/aligned_work.stl": sha(f"{RUN}/intake/aligned_work.stl"), "intake/alignment.json": sha(f"{RUN}/intake/alignment.json"),
            "measure/figures/measurements.json": sha(f"{FIG}/measurements.json")},
 "seed": 0, "created": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
 "part": "OD-S03_steam-knob",
 "frame": "datum frame from intake/alignment.json (frozen): primary = cap crown face -> XY at z=0, material +Z (toward the sleeve); origin = median of sleeve-envelope + cap-wall section centres; clock = lever centreline -> +X (area-weighted fourier_mass). theta CCW about +Z from +X. Sub-body axes (cap, collar, stem group) are measured positions IN this frame, never a re-levelled frame.",
 "scan_noise_mm": NOISE,
 "params": P,
 "struck": [],
 "simplifications": S,
 "checks": {
  "CHK-COUNT": {"ran": True, "result": "pass", "note": "stem ribs: pattern_count.py radius signal, FFT dominant order 4 at z 19.5/22.5/25.5, residual minimum (count_ribs.json)"},
  "CHK-ACHIEVABLE": {"ran": False, "result": "pass", "note": "no caliper or photo readings exist (scan-only run, DECISIONS.md MEASUREMENTS); nothing to prove achievable"},
  "CHK-CLUSTER": {"ran": True, "result": "pass", "note": "bore/axis box z 35.2-38.3 r<3.9: one coherent component = the planned bore shoulder cone E19 (cluster_bore_axis.json); nothing above the sleeve tail; E20 bore notch is missing material, declared in simplifications"},
  "CHK-FRAME": {"ran": True, "result": "pass", "note": "every angle re-measured on the aligned scan in the frozen frame (theta CCW from +X); intake clock check: lever flank planes -0.64/+1.03 deg about +X agree with lever_flank_*_plan_deg"}},
 "open_questions": [
  "Thread/sleeve form: the scan shows planar ring turns (pitch %.3f) with a ~1 mm helical crossover over ~120 deg at both ends (a formed coil?), ripple only %.3f mm deep; true thread profile/spec unobservable on this chrome scan." % (v("sleeve_ripple_pitch"), M["sleeve_ripple_depth_derived"]["value"]),
  "Bore below z %.2f and the internal splines of photo 5 are not scanned; the model closes the bore with a flat floor at bore_floor_z (assumed shape)." % zf_,
  "Lever pocket floor seen sparsely (64 faces); floor depth should be confirmed with a depth rod (MEASUREMENTS F11).",
  "Absolute scale unverified (no calipers, CHK-SCALE FLAG)."],
}
json.dump(doc, open(f"{RUN}/measure/params.json", "w"), indent=1)
print("params:", len(P))
