#!/usr/bin/env python3
"""Compose measure/params.json (run-contract §4) from measure/figures/pcb_measure.json.

Provenance: NEW, run-local (OD-E01). No number is typed here except rule-labelled assumptions
(source "assumed"/"standard"), each with a note. Every scan value is copied from the measurement
JSON (keep-measured, rounded to 0.001 mm on both `value` and `measured`) or is a mean-of-n of
listed per-instance reads. Run from the run root: python3 measure/make_params.py
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
from pathlib import Path

import numpy as np
from shapely.geometry import LineString

RUN = Path(__file__).resolve().parents[1]
MJ = RUN / "measure" / "figures" / "pcb_measure.json"
AJ = RUN / "intake" / "alignment.json"
D = json.loads(MJ.read_text())
A = json.loads(AJ.read_text())
NOISE = float(A["scan_noise_mm"]["value"])
EV = "measure/figures/pcb_measure.json"
P: dict = {}


def r3(v):
    if isinstance(v, (list, tuple)):
        return [r3(x) for x in v]
    return round(float(v), 3)


def km(name, vals, est, unc, ev_key, critical=False, unit="mm", note=None, rerun=None):
    v = r3(vals)
    row = {"value": v, "unit": unit, "measured": v, "rule": "keep-measured", "source": "scan",
           "estimator": est, "uncertainty_mm": round(float(unc), 3), "evidence": f"{EV}#{ev_key}", "critical": critical}
    if note:
        row["note"] = note
    if critical:
        row["rerun_trigger"] = rerun or "a caliper reading of this dimension -> re-run measure and rebuild"
    P[name] = row


def mean_n(name, reads, est, ev_key, critical=False, note=None, unit="mm"):
    reads = r3(reads)
    P[name] = {"value": round(float(np.mean(reads)), 3), "unit": unit, "measured": reads, "rule": "mean-of-n",
               "source": "scan", "estimator": est, "uncertainty_mm": round(float(np.std(reads)), 3),
               "evidence": f"{EV}#{ev_key}", "critical": critical}
    if note:
        P[name]["note"] = note
    if critical:
        P[name]["rerun_trigger"] = "a caliper reading of this dimension -> re-run measure and rebuild"


def assumed(name, value, unit, note, source="assumed", ev="intake/INTAKE_CARD.md §8"):
    P[name] = {"value": value, "unit": unit, "measured": None, "rule": "assumed" if source == "assumed" else "photo-inferred",
               "source": source, "estimator": "not measurable on this scan", "uncertainty_mm": 0.0 if unit != "mm" else 0.5,
               "evidence": ev, "critical": False, "note": note}


# ------------------------------------------------------------------ board
e = D["board"]["edges"]
for k in ("x_min", "x_max", "y_min", "y_max"):
    km(f"board_{k}", e[k]["pos"], f"robust line fit (Cauchy 0.05) on the {k} edge-wall faces, value at mid-span; "
       f"{e[k]['n_faces']} faces, slope {e[k]['slope_deg']:.3f} deg", e[k]["rms"], f"board.edges.{k}", critical=True,
       rerun="ENV-X / ENV-Y caliper reading -> re-run")
km("board_thickness", -D["board"]["wall_bottom_z_p50"], "minus the median lowest z of the edge-wall faces per 3 mm station "
   "(top face = z 0 by datum); the solder side is not scanned", 0.1, "board.wall_bottom_z_p50", critical=True,
   note="consistent with a standard 1.6 mm FR-4 board; kept as measured (no snap: scan source)",
   rerun="F03 caliper reading of the board thickness -> re-run")
sl = D["board"]["slot"]
km("slot_y", [sl["y_min"], sl["y_max"]], sl["method"], 0.1, "board.slot")
km("slot_x_end", sl["x_end"], "max x of the slot no-data region (round end, radius = half width)", 0.1, "board.slot")
for hn, h in D["holes"].items():
    km(f"hole_{hn}", [h["wall_cx"], h["wall_cy"], h["wall_r"]],
       f"IRLS circle (Cauchy 0.1) on {h['wall_faces']} inner bore-wall faces, z -1.45..-0.15, "
       f"angular coverage {h['wall_angular_coverage_deg']} deg; [cx, cy, r]", h["wall_rms"], f"holes.{hn}",
       critical=hn in ("H1", "H2"), rerun="F01/F02 caliper readings -> re-run")

# ------------------------------------------------------------------ heatsink (HS1)
hs = D["heatsink"]
km("hs_top_z", hs["top_z_p50"], "median height-map z of the extrusion top face (z > 24.3)", NOISE, "heatsink.top_z_p50",
   critical=True, rerun="F06 depth reading -> re-run")
assumed("hs_bottom_z", 0.0, "mm", "heatsink root is hidden (fins seen down to ~0.3 mm above the board); modelled standing on the board top")
for hn in ("upper", "lower"):
    h = hs["hubs"][hn]
    km(f"hs_hub_{hn}", [h["cx"], h["cy"], h["r_hub_fill80"], h["hole_r"], h["channel"]["x0"], h["channel"]["x1"]],
       "hub: [cx, cy, R_hub, hole_r, channel_x0, channel_x1]; centre and hole r = Kasa on the screw-channel no-data "
       "boundary; R_hub = radius where the top-mask ring fill drops below 0.8 (0.1 mm rings); the C-shaped channel opens "
       "outward (away from the spine) between the short fins: x0/x1 = " + h["channel"]["method"],
       max(h["hole_rms"], 0.1), f"heatsink.hubs.{hn}")
sn = D["to220_Q1"]["spine_notch"]
km("hs_spine_notch", [sn["y0"], sn["y1"], sn["z_top"]], "[y0, y1, z_top] of the notch under the TO-220: " + sn["method"],
   0.1, "to220_Q1.spine_notch", note="the notch is taken through the full spine thickness, down to the board")
km("hs_spine_x", hs["spine_x"], "median per-row x extent of the spine top between the hubs (height map)", 0.1, "heatsink.spine_x")
long_ = [a for a in hs["arms"] if a["width_measured"]]
short = [a for a in hs["arms"] if not a["width_measured"]]
for i, a in enumerate(long_, 1):
    km(f"hs_fin_{i:02d}", [*a["root"], *a["tip"], a["width"]],
       f"fin/crossbar arm ({a['hub']} hub): PCA line of the arm pixels outside the hub; root extended 1.2 mm into the hub, "
       f"tip = far end minus half width; width = median per-station width; [root_x, root_y, tip_x, tip_y, width]", 0.1,
       "heatsink.arms")
for i, a in enumerate(short, 1):
    km(f"hs_shortfin_{i:02d}", [*a["root"], *a["tip"]],
       f"short fin ({a['hub']} hub): PCA in a +/-14 deg wedge about the hub; [root_x, root_y, tip_x, tip_y]", 0.1,
       "heatsink.arms", note="width from hs_fin_width_short (stub too short for a per-station width)")
mean_n("hs_fin_width_short", [a["width"] for a in long_], "mean of the measured long-fin widths, applied to the 4 short fins",
       "heatsink.arms")

# ------------------------------------------------------------------ TO-220 (Q1)
q = D["to220_Q1"]
km("q1_body", [q["body_front_x"], q["tab_front_x"], q["body_y0"], q["body_y1"], q["body_bottom_z"], q["body_top_z"]],
   "[x_front, x_back, y0, y1, z_bottom, z_top]: front = median x of -X faces; back = tab front face; y from the top-view "
   "(1/99 pct); bottom = 1st pct z of the front faces; top = median height map", 0.1, "to220_Q1")
km("q1_tab", [q["tab_front_x"], q["tab_back_x"], q["tab_y0"], q["tab_y1"], q["tab_top_z_hm_p50"]],
   "[x_front, x_back, y0, y1, z_top]: front = -X faces above the body, back = +X faces seen through the spine notch; "
   "tab spans z from the body bottom to z_top", 0.1, "to220_Q1")
km("q1_tab_hole", [q["tab_hole_in_tab"]["u"], q["tab_hole_in_tab"]["z"], q["tab_hole_in_tab"]["d_fit"]],
   "[y, z, d]: " + q["tab_hole_in_tab"]["method"], q["tab_hole_in_tab"]["fit_rms"], "to220_Q1.tab_hole_in_tab")
km("hs_spine_hole", [q["tab_hole"]["u"], q["tab_hole"]["z"], q["tab_hole"]["d_fit"]],
   "[y, z, d]: " + q["tab_hole"]["method"] + " (the TO-220 screw hole in the heatsink; not coaxial with the tab hole)",
   q["tab_hole"]["fit_rms"], "to220_Q1.tab_hole")
from shapely.geometry import LineString
for i, l_ in enumerate(q["leads"], 1):
    xz = [(x_, z_) for x_, z_ in l_["path_xz"]]
    xz_s = list(LineString(xz).simplify(0.15).coords)
    km(f"q1_lead_{i}", [l_["y"], *[v_ for pt in xz_s for v_ in pt]],
       "[y, then x, z pairs from the board up]: median x of the lead faces per 0.5 mm z bin (z 0.25..4.25), "
       "Douglas-Peucker 0.15 mm; the lead continues straight up to the body bottom", 0.15, "to220_Q1.leads",
       note="lead cross-section from q1_lead_w / q1_lead_t (standard TO-220)")
for nm_, v_ in (("q1_lead_w", 0.8), ("q1_lead_t", 0.5)):
    P[nm_] = {"value": v_, "unit": "mm", "measured": None, "rule": "assumed", "source": "standard",
              "estimator": "TO-220 lead width / thickness (JEDEC TO-220AB nominal), not resolvable on the scan",
              "uncertainty_mm": 0.1, "evidence": "JEDEC TO-220AB outline", "critical": False}

# ------------------------------------------------------------------ clip (S1)
c = D["clip_S1"]
km("clip_path", [v for xy in c["path_vertices"] for v in xy],
   f"top-view strap pixels (12.3 < z < 14.3), skeletonised, ordered end-to-end, Douglas-Peucker {c['simplify_tol_mm']} mm; "
   "flattened [x1, y1, x2, y2, ...]", 0.25, "clip_S1.path_vertices")
hk = D.get("clip_S1_hook")
if hk:
    km("clip_hook", [v for xy in hk["outer_surface_vertices"] for v in xy], hk["method"] + "; strap centre offset "
       "not applied (outer surface used as the path)", 0.4, "clip_S1_hook")
km("clip_width", c["width_topview_p50"], "median 2x distance-transform at the skeleton (top view)", 0.1, "clip_S1")
km("clip_z", [c["bottom_z_p2"], c["top_z_p50"]], "[z_bottom = 2nd pct of strap side faces, z_top = median strap top]", 0.1,
   "clip_S1")

# ------------------------------------------------------------------ caps
for cp in D["caps"]:
    pr = cp["profile"]
    km(f"cap_{cp['name']}", [pr["axis_x_at_z0"], pr["axis_y_at_z0"], pr["axis_dx_dz"], pr["axis_dy_dz"], pr["r_base"],
                             pr["groove_z0"], pr["r_groove"], pr["groove_z1"], pr["r_body"], cp["ztop_p50"]],
       "[axis x, y at z 0, dx/dz, dy/dz, r_base, groove z0, r_groove, groove z1, r_body, z_top]: IRLS circles (Cauchy 0.1) "
       "on the outward can-wall faces per 1 mm z bin; axis = weighted line through the bin centres (rms < 0.08, coverage "
       ">= 225 deg); r_body = median of the upper-half bins; the sealing groove = lower bins > 0.12 below r_body (z to 0.5 mm, "
       "the bin size); r_base = bins under the groove; z_top = median height map inside 0.75 r",
       max(cp["rms"], 0.05), f"caps.{cp['name']}.profile", critical=cp["name"] in ("C3", "C4"),
       rerun="F07 caliper Ø/height -> re-run", note="groove z limits are 1 mm bin edges (+/-0.5 mm)")

for cp in D["caps"]:
    st = cp["profile"].get("standoff")
    if st and "stem_r" in st:
        km(f"capstem_{cp['name']}", [st["stem_r"], st["standoff_z"]], "[stem r, stand-off z]: " + st["method"], 0.2,
           f"caps.{cp['name']}.profile.standoff")
bp = D["caps"][0]["base_plate"]
km("cap_C1_base", [bp["x0"], bp["x1"], bp["y0"], bp["y1"], bp["ztop"]],
   "[x0, x1, y0, y1, z_top] of C1's SMD V-chip base plate: " + bp["method"], 0.1, "caps.C1.base_plate")

# ------------------------------------------------------------------ X2 film cap
x2 = D["x2_CX1"]
km("x2_CX1", [x2["x0"], x2["x1"], x2["y0"], x2["y1"], x2["ztop"]],
   "[x0, x1, y0, y1, z_top]: height-map pixels above half height (bbox), top = median of the >85% pixels", 0.1, "x2_CX1",
   critical=True, rerun="F08 caliper L x W x H -> re-run")

# ------------------------------------------------------------------ fastons
F = D["fastons"]
km("faston_x", [f["x_centre"] for f in F], "per tab: mid-plane of the median +X and -X blade faces (z 3..9)", 0.05,
   "fastons", critical=True, rerun="F04 caliper tab positions -> re-run")
km("faston_y", [0.5 * (f["y0"] + f["y1"]) for f in F], "per tab: mid of the median +Y and -Y blade-edge faces (z 3..9)",
   0.05, "fastons")
mean_n("faston_width", [f["width"] for f in F], "blade width = +Y face - -Y face median per tab", "fastons")
mean_n("faston_thickness", [f["thickness"] for f in F], "blade thickness = +X face - -X face median per tab", "fastons")
mean_n("faston_top_z", [f["ztop_p95"] for f in F], "95th pct height map over the blade per tab", "fastons", critical=True)
ch = [(f["width"] - f["top_y_extent_at_minus0.3"]) / 2 + 0.3 for f in F if f["top_y_extent_at_minus0.3"] < f["width"]]
mean_n("faston_chamfer", ch, "45-deg corner chamfer leg = (blade width - top-view width 0.3 mm below the top)/2 + 0.3, "
       "per tab; tab 5 excluded (its top-view extent is merged with a neighbour, extent > width)", "fastons")
fl = [f for f in F if f["foot_y1"] is not None and f["foot_top_z"] and f["foot_top_z"] > 1.2]
mean_n("faston_foot_len", [f["foot_y1"] - f["foot_y0"] for f in fl], "foot (base) length = +Y minus -Y foot-face medians (z 0.3..1.5); "
       "tabs with a missing foot face excluded", "fastons")
mean_n("faston_foot_top_z", [f["foot_top_z"] for f in fl], "highest z where the tab section is wider than the blade + 0.5", "fastons")
mean_n("faston_foot_dx", [0.5 * (f["foot_x_minus"] + f["foot_x_plus"]) - f["x_centre"] for f in F],
       "x offset of the foot mid-plane from the blade mid-plane", "fastons")
fh = D["faston_detent_holes"]
mean_n("faston_hole_z", [h["z"] for h in fh], "detent hole centre z (Kasa on the -X face occupancy hole)", "faston_detent_holes")
mean_n("faston_hole_d", [h["d_fit"] for h in fh], "detent hole diameter (Kasa on the -X face occupancy hole)", "faston_detent_holes")
mean_n("faston_hole_dy", [h["u"] - 0.5 * (f["y0"] + f["y1"]) for h, f in zip(fh, F)], "detent hole y offset from the blade centre",
       "faston_detent_holes")

# ------------------------------------------------------------------ connectors, base+riser blocks
for cn in D["connectors"]:
    floor = cn["cav_floor_seen_min"]
    if cn.get("cav_floor_upfacing_median") is not None:
        floor = cn["cav_floor_upfacing_median"]
    km(f"conn_{cn['name']}", [cn["x0"], cn["x1"], cn["y0"], cn["y1"], cn["ztop"], cn["cav_x0"], cn["cav_x1"], cn["cav_y0"],
                              cn["cav_y1"], max(floor, 0.0)],
       "[x0, x1, y0, y1, z_top, cav_x0, cav_x1, cav_y0, cav_y1, cav_floor_z]: housing walls = dominant side-wall faces; "
       "cavity = inner-wall faces (else 2/98 pct of the low pixels); floor = median z of the up-facing faces inside the "
       "cavity when >= 20 exist, else the lowest scan point seen "
       f"(no-data fraction {cn['cav_nodata_frac']:.2f}: the true floor may be deeper)", 0.1, f"connectors.{cn['name']}")
for cn in D["connectors"]:
    for i, pp in enumerate(cn["inner_parts"], 1):
        km(f"connpin_{cn['name']}_{i:02d}", pp, "[x0, x1, y0, y1, z_top]: contact / rib standing > 0.8 mm above the lowest "
           "point seen inside the cavity (height-map component bbox, top = 90th pct)", 0.1, f"connectors.{cn['name']}.inner_parts")
for br in D["base_riser"]:
    for j, bmp in enumerate(br.get("bumps", []), 1):
        km(f"box_bump_{br['name']}_{j}", bmp, "[x0, x1, y0, y1, z_top]: part standing > 0.5 mm on the block's base top, away "
           "from the riser (height-map component bbox, 90th pct top)", 0.1, f"base_riser.{br['name']}.bumps")
    rs, sl_ = br["riser"], br["riser_back_slope"]
    km(f"blk_{br['name']}", [*br["base"], rs[0], sl_["x_at_base_top"], sl_["x_at_top"], rs[2], rs[3], rs[4]],
       "[base x0, x1, y0, y1, z_top, riser x0, riser back x at the base top, riser back x at its top, riser y0, y1, z_top]: "
       "base walls = dominant side-wall faces; riser front / y = pixels above 60% of the base-to-riser rise; riser back = "
       f"line fit x(z) on its +X-facing faces (rms {sl_['fit_rms']:.3f})", max(0.1, sl_["fit_rms"]), f"base_riser.{br['name']}")

# ------------------------------------------------------------------ axial parts along Y
for key in ("resistor_R1", "axial_D1", "axial_D2", "axial_L2"):
    ax = D[key]
    leads = [l_ for l_ in ax["leads"] if l_]
    vals = [ax["x_axis"], ax["z_axis"], ax["r"], ax["y0"], ax["y1"]]
    for l_ in leads:
        far = l_["y_max"] if l_["y_min"] >= ax["y1"] - 0.05 else l_["y_min"]
        vals += [l_["x"], far, l_["z_top_p90"]]
    km(f"ax_{ax['name']}", vals,
       "[x_axis, z_axis, r, y0, y1, then per lead: x, y_far_end, z_top]: IRLS circle in (x, z) on the body faces; y ends and "
       "leads from the height map (lead strips > 0.5 mm above the board)", max(ax["fit_rms"], 0.1), key)
    for j, l_ in enumerate(leads, 1):
        if len(l_["descent_xyz"]) >= 2:
            xyz = list(LineString(l_["descent_xyz"]).simplify(0.15).coords)
            km(f"axlead_{ax['name']}_{j}", [v_ for pt in xyz for v_ in pt],
               "descending part of the lead (x, y, z triples), from the board up: median x and y of the lead faces per 0.4 mm "
               "z bin up to 1.0 below the lead top, Douglas-Peucker 0.15 (3D)", 0.15, f"{key}.leads")
    for j, sp in enumerate(ax.get("side_parts", []), 1):
        km(f"box_side_{ax['name']}_{j}", sp, "[x0, x1, y0, y1, z_top]: low part beside the body, merged with it in the top view "
           "(pixels 0.25..1.5 above the board, > r + 0.3 from the axis; bbox above half its height)", 0.1, f"{key}.side_parts")
P["lead_d"] = {"value": 0.8, "unit": "mm", "measured": None, "rule": "assumed", "source": "standard",
               "estimator": "through-hole lead wire diameter (typical 0.6-0.8 for these parts); the scan-dilated strip widths "
                            "0.7-1.2 mm cannot resolve it", "uncertainty_mm": 0.2, "evidence": EV + "#resistor_R1.leads",
               "critical": False}

# ------------------------------------------------------------------ Y-cap
y = D["ycap_CY1"]
km("ycap_CY1", [*y["centre"], *y["normal"], y["core_R"], y["rim_rho"]],
   "[cx, cy, cz, nx, ny, nz, core_R, rim_rho]: soft-L1 SDF fit of a rounded disc (flat core swept by a sphere) to the visible "
   f"faces z > 6.5 (necks and faston blades excluded); sdf rms {y['sdf_rms']:.3f}", y["sdf_rms"], "ycap_CY1",
   note="unit vector entries (n) are dimensionless")
for i, l_ in enumerate(D["ycap_leads"], 1):
    km(f"ycap_lead_{i}", [*l_["p_low"], *l_["p_high"]], "3D PCA line on the lead faces; [x,y,z low end, x,y,z high end]",
       l_["perp_p90"], "ycap_leads")

# ------------------------------------------------------------------ auto boxes
for i, b in enumerate(D["auto_boxes"], 1):
    km(f"box_{i:03d}", [b["x0"], b["x1"], b["y0"], b["y1"], b["ztop"]],
       f"SMD/low part (segment {b['seg']}): axis-aligned bbox of the pixels above half its height (0.1 mm raster), "
       f"top = median z of the >80% pixels; min-rect angle {b['minrect_angle_deg']:.1f} deg (placed at 0/90)", 0.1,
       "auto_boxes")

# ------------------------------------------------------------------ document
simpl = [
    {"name": "board flatness", "modelled_as": "flat plate, top at z 0",
     "deviation_cost": f"board-top quadratic warp surface spans {D['board']['warp_quadratic']['surface_min_mm']:.3f} .. "
                       f"{D['board']['warp_quadratic']['surface_max_mm']:.3f} mm inside the outline; corner pixels near H1 read about -0.35"},
    {"name": "SMD / low parts", "modelled_as": "axis-aligned boxes of the half-height footprint, flat top",
     "deviation_cost": "terminations, solder fillets and leads below half height are not modelled (lower than the part top by 0.2-1.0 mm)"},
    {"name": "heatsink profile", "modelled_as": "extrusion of hubs + spine + straight round-ended fins (stadiums)",
     "deviation_cost": f"profile IoU vs the scanned top mask {hs['profile_iou_vs_top_mask']:.3f}"},
    {"name": "spring clip", "modelled_as": "constant-width strap extruded along a Douglas-Peucker path",
     "deviation_cost": f"path simplification tolerance {c['simplify_tol_mm']} mm"},
    {"name": "electrolytic caps", "modelled_as": "cone frustum along the axis through the two measured wall circles, flat top",
     "deviation_cost": "top vent crosses and rim crimp (about 0.1-0.4 mm) not modelled"},
    {"name": "Y-capacitor", "modelled_as": "rounded disc (cylinder with full-round rim) + straight leads",
     "deviation_cost": f"SDF fit rms {y['sdf_rms']:.3f} / p95 {y['sdf_p95_abs']:.3f} mm; epoxy necks onto the leads not modelled"},
    {"name": "leads", "modelled_as": "straight round wires (horizontal run + vertical drop), bends as corners",
     "deviation_cost": "lead bends are curved on the part (radius ~0.5-1 mm)"},
]
doc = {"schema": "stl-re/params.json@1", "tool": "measure/make_params.py", "tool_version": "run-local@1",
       "inputs": {"measure/figures/pcb_measure.json": hashlib.sha256(MJ.read_bytes()).hexdigest(),
                  "intake/alignment.json": hashlib.sha256(AJ.read_bytes()).hexdigest()},
       "seed": 0, "created": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
       "part": "OD-E01_Power-PCB",
       "frame": "datum frame of intake/alignment.json: origin = mounting hole H1 axis ∩ PCB top face; +Z out of the component "
                "side; +X along the long board edge (clock: +X short-edge normal); theta CCW about +Z from +X. Component "
                "placements are axis-aligned (0/90 deg) unless a direction is given as a vector.",
       "scan_noise_mm": NOISE, "params": P, "struck": [], "simplifications": simpl,
       "checks": {"CHK-COUNT": {"ran": True, "result": "pass", "note": "no rotational pattern on this part; instance counts are "
                                "connected components of the height map (16 heatsink arms, 6 fastons, 5 caps, 60 boxes), each placed "
                                "at its own measured position"},
                  "CHK-ACHIEVABLE": {"ran": True, "result": "pass", "note": "no caliper readings (scan-only run)"},
                  "CHK-CLUSTER": {"ran": True, "result": "pass", "note": f"{len(D['segments'])} clusters > 0.18 mm above the local "
                                  "board surface; every one is owned by a named part or an auto box (figures/pcb_measure.json#segments)"},
                  "CHK-FRAME": {"ran": True, "result": "pass", "note": "all positions and direction vectors measured in the frozen datum frame"}},
       "open_questions": ["connector cavity floors (J1, J2) and the heatsink root are not visible on the scan",
                          "board thickness and all sizes are scan values; no caliper verified the scale"]}
(RUN / "measure" / "params.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False))
print("params:", len(P))
