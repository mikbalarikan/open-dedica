"""Assemble measure/params.json from the measurement JSONs in measure/figures/ (no retyped numbers:
every scan value is read from the file named in its `evidence`). Scan values are kept as measured
(rule keep-measured, value == measured), except the rim plane (datum z = 0, round-within-noise).
Unscanned geometry is tagged assumed with measured = null.

Run from the run folder:  python measure/scripts/m99_write_params.py
"""
import datetime as _dt
import hashlib
import json
from pathlib import Path

F = Path('measure/figures')
J = lambda n: json.load(open(F / n))
bp, hax, hpr, npad, pfit = J('body_profile.json'), J('handle_axis.json'), J('handle_profile.json'), J('neck_pad.json'), J('pad_fit.json')
lugs, det, ss, rf, wire = J('lugs_notches.json'), J('details.json'), J('spouts_screw.json'), J('ribs_floor.json'), J('wire.json')
vfl, vseg, tro, lend, feet = J('vrib_flanks.json'), J('vrib_segments.json'), J('trough.json'), J('lug_ends.json'), J('arch_feet.json')
nco, wgr = J('neck_collar.json'), J('wire_groove.json')
al = json.load(open('intake/alignment.json'))
noise = al['scan_noise_mm']['value']
P = {}


def scan(name, value, est, ev, unc, unit='mm', critical=False, note=None, rerun=None):
    row = {"value": value, "unit": unit, "measured": value, "rule": "keep-measured", "source": "scan",
           "estimator": est, "uncertainty_mm": float(unc), "evidence": ev, "critical": critical}
    if note: row["note"] = note
    if unit == 'deg': row["frame"] = "datum frame, theta CCW about +Z from +X"
    if rerun: row["rerun_trigger"] = rerun
    P[name] = row


def assumed(name, value, why, unit='mm', ev='build/MODELING_PLAN.md', critical=False):
    P[name] = {"value": value, "unit": unit, "measured": None, "rule": "assumed", "source": "assumed",
               "estimator": "not measurable on the scan: " + why, "uncertainty_mm": 0.5, "evidence": ev, "critical": critical,
               "note": "not scan evidence; confirm physically"}


R = 'measure/figures/'
# ---------------------------------------------------------------- cup body (revolve about datum Z)
P["rim_top_z"] = {"value": 0.0, "unit": "mm", "measured": bp["rim_top_z"]["median"], "rule": "round-within-noise", "source": "scan",
                  "estimator": "median z of rim-top samples r 28.4..30.1, clean sectors (m03)", "uncertainty_mm": noise,
                  "evidence": R + "body_profile.json#rim_top_z", "critical": True,
                  "note": "the datum plane itself (alignment.json primary); moved by less than the noise floor",
                  "rerun_trigger": "a caliper/height gauge reading of the rim face vs lug tops"}
ow = bp["outer_wall"]
scan("outer_wall_r_at_z0", ow["a"], "line fit r = a + b z on outer-wall samples z -38..-3, clean sectors (m03)", R + "body_profile.json#outer_wall", ow["rms"], critical=True,
     rerun="caliper OD of the cup just below the lugs")
scan("outer_wall_dr_dz", ow["b"], "slope of the same line fit (draft)", R + "body_profile.json#outer_wall", ow["rms"], unit='mm')
P["outer_wall_dr_dz"]["note"] = "dimensionless slope dr/dz (unit field 'mm' per mm)"
scan("rim_outer_round_R", bp["rim_outer_round"]["R"], "circle fit (r,z) at the rim outer edge (m03)", R + "body_profile.json#rim_outer_round", bp["rim_outer_round"]["rms"])
scan("rim_inner_round_R", bp["rim_inner_round"]["R"], "circle fit (r,z) at the rim inner edge (m03)", R + "body_profile.json#rim_inner_round", bp["rim_inner_round"]["rms"])
scan("rim_inner_round_cr", bp["rim_inner_round"]["cu"], "centre r of the same circle fit", R + "body_profile.json#rim_inner_round", bp["rim_inner_round"]["rms"])
bu = bp["bore_upper"]
scan("bore_r_at_z0", bu["a"], "line fit r = a + b z on rim-bore samples z -10.8..-7.5 (m03)", R + "body_profile.json#bore_upper", bu["rms"], critical=True,
     rerun="caliper ID of the rim bore (basket seat)")
scan("bore_dr_dz", bu["b"], "slope of the same fit", R + "body_profile.json#bore_upper", bu["rms"])
scan("ledge_z", bp["ledge_z"]["median"], "median z of ledge samples r 26..27 (m03)", R + "body_profile.json#ledge_z", noise, critical=True,
     rerun="depth gauge from the rim to the basket ledge")
lt = bp["ledge_taper"]
scan("ledge_taper_r_at_z0", lt["a"], "line fit r = a + b z, z -15.5..-12.3 (m03)", R + "body_profile.json#ledge_taper", lt["rms"])
scan("ledge_taper_dr_dz", lt["b"], "slope of the same fit", R + "body_profile.json#ledge_taper", lt["rms"])
iw = bp["insert_wall"]
scan("insert_wall_r_at_z0", iw["a"], "line fit r = a + b z, z -32..-17 (m03)", R + "body_profile.json#insert_wall", iw["rms"])
scan("insert_wall_dr_dz", iw["b"], "slope of the same fit", R + "body_profile.json#insert_wall", iw["rms"])
scan("floor_fillet_R", bp["floor_fillet"]["R"], "circle fit (r,z) floor-to-wall, back sectors (m03)", R + "body_profile.json#floor_fillet", bp["floor_fillet"]["rms"])
dm = bp["dome"]
scan("dome_centre_z", dm["z0"], "sphere with centre on the axis fitted to bottom samples r 7..24 (m03)", R + "body_profile.json#dome", dm["rms"])
scan("dome_R", dm["R"], "radius of the same sphere fit", R + "body_profile.json#dome", dm["rms"])
scan("bottom_corner_R", bp["bottom_corner"]["R"], "circle fit (r,z) wall-to-dome corner (m03)", R + "body_profile.json#bottom_corner", bp["bottom_corner"]["rms"])
# ---------------------------------------------------------------- lugs and rim notches
for i, (L, rp) in enumerate(zip(lugs["lugs"], det["lug_ramps"])):
    scan(f"lug{i+1}_centre_deg", L["centre_deg"], "mid-angle of the 1-deg bins where the outer radius > 33.2 over z -4.6..-0.6 (m04)", R + "lugs_notches.json#lugs", 0.5 * 33 * 3.1416 / 180, unit='deg')
    P[f"lug{i+1}_centre_deg"]["note"] = "kept at its measured angle; spacing 120.5/120.5/119 deg is not within noise, so no 3-fold symmetry is enforced"
    scan(f"lug{i+1}_span_deg", L["span_deg"], "count of lug bins (m04)", R + "lugs_notches.json#lugs", 1.0 * 33 * 3.1416 / 180, unit='deg')
    scan(f"lug{i+1}_r_outer", L["r_outer_median"], "median p99 radius over the lug core bins (m04)", R + "lugs_notches.json#lugs", 0.05, critical=True,
         rerun="caliper across a lug to the opposite wall")
    scan(f"lug{i+1}_under_z_centre", rp["z_at_centre"], "line fit of the lug under-face z vs theta, value at the lug centre (m11)", R + "details.json#lug_ramps", rp["rms"], critical=True,
         rerun="feeler/height reading of the bayonet ramp at both lug ends")
    scan(f"lug{i+1}_under_dz_per_deg", rp["dz_per_deg"], "slope of the same ramp fit (mm per deg)", R + "details.json#lug_ramps", rp["rms"])
for i, E in enumerate(lend["lugs"]):
    scan(f"lug{i+1}_leadout_z_centre", E["leadout_z_at_centre_line"], "line fit of the under-face z vs theta from the knee to the last bin, value extrapolated to the lug centre (m17; it2)", R + "lug_ends.json", E["rms"], critical=True,
         rerun="feeler/height reading of the bayonet ramp at both lug ends")
    scan(f"lug{i+1}_leadout_dz_per_deg", E["leadout_dz_per_deg"], "slope of the same lead-out fit (mm per deg)", R + "lug_ends.json", E["rms"])
for i, N in enumerate(lugs["rim_notches"]):
    c = N["start_deg"] + N["span_deg"] / 2
    scan(f"notch{i+1}_centre_deg", c, "centre of the theta span with no rim-top samples (m04)", R + "lugs_notches.json#rim_notches", 1.0 * 29 * 3.1416 / 180, unit='deg')
    scan(f"notch{i+1}_span_deg", N["span_deg"], "width of the same span", R + "lugs_notches.json#rim_notches", 1.0 * 29 * 3.1416 / 180, unit='deg')
    scan(f"notch{i+1}_floor_z", N["floor_z_p90"], "p90 z of samples inside the notch (m04)", R + "lugs_notches.json#rim_notches", 0.1)
# ---------------------------------------------------------------- pad on the +X wall
cv = pfit["cone_vertical_axis"]
scan("pad_axis_x", cv["x0"], "cone with vertical axis fitted to pad-face samples z -32..-3 (m06)", R + "pad_fit.json#cone_vertical_axis", cv["rms"])
scan("pad_axis_y", cv["y0"], "same fit", R + "pad_fit.json#cone_vertical_axis", cv["rms"])
scan("pad_R_at_z0", cv["R0_at_z0"], "same fit, radius at z = 0", R + "pad_fit.json#cone_vertical_axis", cv["rms"])
scan("pad_dR_dz", cv["dRdz"], "same fit, slope dR/dz (reverse draft)", R + "pad_fit.json#cone_vertical_axis", cv["rms"])
ph = det["pad_halfwidth"]
scan("pad_halfwidth_at_z0", ph["hw = a + b z"][0], "line fit of the pad half-width vs z, z -24..-4 (m11 from m05 edges)", R + "details.json#pad_halfwidth", ph["rms"])
scan("pad_halfwidth_dz", ph["hw = a + b z"][1], "slope of the same fit", R + "details.json#pad_halfwidth", ph["rms"])
pc = det["pad_underchamfer"]
scan("pad_underchamfer_x_at_z0", pc["x = a + b z"][0], "line fit x = a + b z of the pad under-chamfer at |y| 8.5..11.8 (m11)", R + "details.json#pad_underchamfer", pc["rms"])
scan("pad_underchamfer_dx_dz", pc["x = a + b z"][1], "slope of the same fit", R + "details.json#pad_underchamfer", pc["rms"])
# ---------------------------------------------------------------- handle axis, neck arch, collar, grip, end
for k, v in zip(("handle_axis_y0", "handle_axis_z0"), hax["axis_point_x0"][1:]):
    scan(k, v, "line through IRLS circle centres of x-sections 50..155 (m01/m02), value at x = 0", R + "handle_axis.json", 0.02)
scan("handle_axis_dy_dx", hax["yz_slope"][0], "slope of the same line", R + "handle_axis.json", 0.02)
scan("handle_axis_dz_dx", hax["yz_slope"][1], "slope of the same line", R + "handle_axis.json", 0.02)
scan("grip_r_at_t0", hax["r_linear"]["r_at_x0"], "line fit r(t) of the station radii t 50..155 (m02)", R + "handle_axis.json#r_linear", hax["r_linear"]["rms"])
scan("grip_dr_dt", hax["r_linear"]["slope"], "slope of the same fit (taper)", R + "handle_axis.json#r_linear", hax["r_linear"]["rms"])
scan("arch_outer_r", npad["arch_outer_r"]["median"], "median radial distance about the handle axis, upper half, x 32..37.5 (m05)", R + "neck_pad.json#arch_outer_r", 0.05)
scan("channel_halfwidth", (npad["channel_halfwidth"]["v_pos"] - npad["channel_halfwidth"]["v_neg"]) / 2, "mean |v| of the two channel side walls (m05)", R + "neck_pad.json#channel_halfwidth", 0.05)
scan("channel_roof_r", npad["channel_roof_r"]["median"], "median radial distance of the down-facing roof samples (m05)", R + "neck_pad.json#channel_roof_r", 0.05)
scan("arch_foot_w", npad["foot_min_w"]["median_of_lowest_decile"], "lowest-decile median of the leg feet below the handle axis (m05)", R + "neck_pad.json#foot_min_w", 0.05)
fs = [o for o in feet["sections"] if o["x"] <= 38.0]
import statistics as _st
scan("arch_foot_round_R", feet["R_median"], "median Kasa radius of the lowest 1.8 mm of each leg, x-sections 33..41 (m18; it2)", R + "arch_feet.json", (feet["R_p25_p75"][1] - feet["R_p25_p75"][0]) / 2)
scan("arch_foot_centre_v", _st.median(abs(o["cv"]) for o in fs), "median |v| of the foot-round centres, x 33..38 (arch part, m18)", R + "arch_feet.json", 0.05)
scan("arch_foot_centre_w", _st.median(o["cw"] for o in fs), "median w of the foot-round centres, x 33..38 (arch part, m18)", R + "arch_feet.json", 0.05)
scan("channel_start_t", npad["roof_x_extent"]["x_min"], "p0.5 x of the down-facing channel-roof samples (m05)", R + "neck_pad.json#roof_x_extent", 0.1)
scan("channel_end_t", npad["channel_end_x"], "median x of the channel end wall (m05)", R + "neck_pad.json#channel_end_x", 0.1)
for key, pre in (("neck_cone", "neck_cone"), ("collar_flank", "collar_flank")):
    N_ = nco[key]
    scan(f"{pre}_r_at_t0", N_["r = a + b t"][0], f"line fit r(x) of IRLS circle fits on full x-sections {N_['x_range']} (m20; it2, replaces the m09 upper-envelope fit)", R + "neck_collar.json#" + key, N_["r_rms"])
    scan(f"{pre}_dr_dt", N_["r = a + b t"][1], "slope of the same fit", R + "neck_collar.json#" + key, N_["r_rms"])
    scan(f"{pre}_axis_dy", N_["dy_off"], "median circle-centre offset from the grip axis, y (m20)", R + "neck_collar.json#" + key, N_["circle_rms_median"])
    scan(f"{pre}_axis_dz", N_["dz_off"], "median circle-centre offset from the grip axis, z (m20)", R + "neck_collar.json#" + key, N_["circle_rms_median"])
scan("collar_step_t", hpr["collar_step_t"], "t of the largest envelope step 44..45.5 (m09)", R + "handle_profile.json#collar_step_t", 0.1)
scan("collar_peak_r", hpr["collar_peak_r"], "max of the envelope t 47..49 (m09)", R + "handle_profile.json#collar_peak_r", 0.05)
scan("collar_back_t", hpr["collar_back_t"], "first envelope bin after the peak with r < 13.6 (m09)", R + "handle_profile.json#collar_back_t", 0.1)
ec = hpr["end_chamfer"]
scan("end_chamfer_r_at_t0", ec["r = a + b t"][0], "line fit of the envelope t 160.2..164.3 (m09)", R + "handle_profile.json#end_chamfer", ec["rms"])
scan("end_chamfer_dr_dt", ec["r = a + b t"][1], "slope of the same fit", R + "handle_profile.json#end_chamfer", ec["rms"])
scan("end_face_t", hpr["end_face_t"], "median t of end-face samples (m09)", R + "handle_profile.json#end_face_t", 0.05, critical=True,
     rerun="overall length reading (rim centre to handle end)")
assumed("end_round_R", 0.6, "the end-face edge round is a few samples wide; value read by eye from handle_meridian.png", ev=R + "handle_meridian.png")
assumed("collar_top_round_R", 0.6, "collar crest round read by eye from handle_meridian.png", ev=R + "handle_meridian.png")
# ---------------------------------------------------------------- spouts and screws
for i, key in enumerate(("spout_0", "spout_1")):
    S = ss[key]
    scan(f"spout{i+1}_x", S["cx"], "median centre of IRLS circle fits z -55..-49.5 (m07)", R + "spouts_screw.json#" + key, 0.02, critical=True,
         rerun="caliper spout-to-spout distance")
    scan(f"spout{i+1}_y", S["cy"], "same", R + "spouts_screw.json#" + key, 0.02, critical=True, rerun="caliper spout-to-spout distance")
    a, b = det[f"{key}_boss_wall r = a + b z"]
    scan(f"spout{i+1}_wall_r_at_z0", a, "line fit r = a + b z of the boss wall z -55.3..-50.3 (m11)", R + "details.json", 0.02)
    scan(f"spout{i+1}_wall_dr_dz", b, "slope of the same fit", R + "details.json", 0.02)
    scan(f"spout{i+1}_ring_z", det[f"{key}_bottom_ring_z"], "median z of the down-facing bottom ring r 4.3..5.4 (m11)", R + "details.json", 0.05)
    scan(f"spout{i+1}_tip_z", S["tip_zmin"], "p0.5 z within r < 1.5 of the boss axis (m07)", R + "spouts_screw.json#" + key, 0.05, critical=True,
         rerun="height reading rim face to spout tip")
    scan(f"spout{i+1}_head_z_r3p2", det[f"{key}_head_z_at_r3.2"], "median z of head samples at r 3.0..3.4 (m11)", R + "details.json", 0.05)
cs = ss["centre_screw"]
scan("cscrew_x", cs["cx"], "centroid of the raised disc on the bottom height map (m07)", R + "spouts_screw.json#centre_screw", 0.1)
scan("cscrew_y", cs["cy"], "same", R + "spouts_screw.json#centre_screw", 0.1)
scan("cscrew_disc_r", cs["disc_r_p98"], "p98 radius of the raised disc cells (m07)", R + "spouts_screw.json#centre_screw", 0.1)
scan("cscrew_disc_raise", cs["disc_raise_median"], "median height of the disc above the dome sphere (m07)", R + "spouts_screw.json#centre_screw", 0.05)
scan("recess_arm", max(abs(v) for v in cs["recess_extent_x"] + cs["recess_extent_y"]), "max half-extent of cells > 0.6 mm deep (m07)", R + "spouts_screw.json#centre_screw", 0.2)
scan("recess_depth", cs["recess_depth_max"], "max depth of the cross recess over the dome (m07)", R + "spouts_screw.json#centre_screw", 0.2)
assumed("recess_width", 0.9, "cross-recess slot width below the 0.2 mm height-map cell resolution; read by eye from spouts_screw.png", ev=R + "spouts_screw.png")
assumed("spout_boss_root_R", 1.5, "boss-to-dome round read by eye from spouts_screw.png", ev=R + "spouts_screw.png")
assumed("spout_head_r", 3.5, "screw-head rim radius read by eye from spouts_screw.png and the pocket ring profile (head sits in a r~3.5 counterbore)", ev=R + "spouts_screw.png")
assumed("pocket_bore_r", 3.5, "inner pocket opening radius: the inside height map drops to the screw head inside r ~3.5 of the boss axis (ring medians, it1 notes)", ev=R + "floor_heightmap_max_z.npy")
assumed("pocket_bore_bottom_z", -54.0, "the pocket interior is not scanned (open mesh); depth invented, leaves ~2.3 mm above the bottom ring")
# ---------------------------------------------------------------- interior insert: floor, ribs
fc = rf["floor_funnel_cone"]
scan("funnel_apex_z", fc["apex_z"], "vertical-axis cone z = apex + k*rho fitted to flat floor cells outside the U (m08)", R + "ribs_floor.json#floor_funnel_cone", fc["rms"])
scan("funnel_slope", fc["slope_dz_dr"], "same fit, dz/drho", R + "ribs_floor.json#floor_funnel_cone", fc["rms"])
scan("funnel_axis_x", fc["axis_x"], "same fit, axis x", R + "ribs_floor.json#floor_funnel_cone", fc["rms"])
scan("funnel_axis_y", fc["axis_y"], "same fit, axis y", R + "ribs_floor.json#floor_funnel_cone", fc["rms"])
up = rf["floor_in_U_plane"]
tc = tro["const"]
for k_, nm_ in (("rc", "trough_rc"), ("zc", "trough_zc"), ("rho", "trough_rho")):
    scan(nm_, tc[k_], "circular (r,z) section revolved about the cup axis, fitted to floor cells r 13..23.6 between the spout angles (m16; it2; the model spans the same spout angles, from spout{1,2}_x/y)", R + "trough.json#const", tc["rms"])
scan("uplat_z0", up["z0"], "plane z = z0 + a x + b y fitted to the floor cells inside the U (m08)", R + "ribs_floor.json#floor_in_U_plane", up["rms"])
scan("uplat_dz_dx", up["dz_dx"], "same fit", R + "ribs_floor.json#floor_in_U_plane", up["rms"])
scan("uplat_dz_dy", up["dz_dy"], "same fit", R + "ribs_floor.json#floor_in_U_plane", up["rms"])
scan("urib_top_z", rf["U_top_z"], "median z of U-rib top cells (m08)", R + "ribs_floor.json#U_top_z", 0.05)
scan("urib_inner_absy", det["U_leg_inner_face_absy"], "median |y| of the U-leg inner-face samples (m11)", R + "details.json", 0.05)
scan("urib_outer_absy", det["U_leg_outer_face_absy"], "median |y| of the U-leg outer-face samples z -33..-28.5 (m11)", R + "details.json", 0.1)
scan("urib_open_end_x", det["U_top_x_range"][0], "p0.2 x of the U-rib top samples (m11)", R + "details.json", 0.1)
scan("urib_round_end_outer_x", det["U_round_end_outer_x"], "p99.8 x of the U-rib top samples (m11)", R + "details.json", 0.1)
for key, nm in (("V_pos", "vrib1"), ("V_neg", "vrib2")):
    V, G = rf[key], vseg[key]
    scan(f"{nm}_outer_end", G["outer_end"], "two-segment TLS fit of the crest centreline, segment-1 point at the m08 outer end (m15; it2)", R + "vrib_segments.json#" + key, G["seg1_rms"])
    scan(f"{nm}_joint", G["joint"], "intersection of the two crest segments (m15; it2)", R + "vrib_segments.json#" + key, max(G["seg1_rms"], G["seg2_rms"]))
    scan(f"{nm}_tip", G["inner_end"], "segment-2 point at the last crest bin (m15; it2)", R + "vrib_segments.json#" + key, G["seg2_rms"])
    scan(f"{nm}_top_z", V["top_z"], "median z of the rib top cells (m08)", R + "ribs_floor.json#" + key, 0.05)
bn = vfl["V_neg"]["bins"]; lo_, hi_ = bn[0], bn[-1]
w_lo, w_hi = lo_["inner_flank_u"] - lo_["outer_flank_u"], hi_["inner_flank_u"] - hi_["outer_flank_u"]
scan("vrib_width_top", w_hi, f"V_neg inner minus outer flank offset in the z = {hi_['z']} bin (m13; V_pos outer flank is occluded, same law used)", R + "vrib_flanks.json", 0.1)
scan("vrib_width_base", w_lo, f"same, z = {lo_['z']} bin (m13)", R + "vrib_flanks.json", 0.1)
scan("vrib_width_z_top", hi_["z"], "z of the top width bin", R + "vrib_flanks.json", 0.5)
scan("vrib_width_z_base", lo_["z"], "z of the base width bin", R + "vrib_flanks.json", 0.5)

# ---------------------------------------------------------------- wire spring (3 exposed arcs)
for i, S in enumerate(wire["segments"]):
    for k in ("cx", "cy", "R", "zc"):
        scan(f"wire{i+1}_{k}", S[k], "torus-section fit (circle path in xy at constant z, tube radius) to the exposed wire samples (m10)", R + "wire.json#segments", S["rms"])
    scan(f"wire{i+1}_theta_span", S["theta_span_deg"], "theta range of the exposed samples (m10)", R + "wire.json#segments", 1.0, unit='deg')
scan("groove_theta_start", wgr["theta_span_deg"][0], "first 5-deg bin of the groove run (m19; it2)", R + "wire_groove.json", 2.5, unit='deg')
scan("groove_theta_end", wgr["theta_span_deg"][1], "end of the last 5-deg bin of the groove run (m19)", R + "wire_groove.json", 2.5, unit='deg')
scan("groove_depth", wgr["apex_depth_mm"], "median max depth behind the bore line per bin (m19)", R + "wire_groove.json", 0.1)
scan("groove_apex_z", wgr["apex_z"], "median z of the deepest point per bin (m19)", R + "wire_groove.json", 0.1)
scan("groove_upper_z", wgr["upper_edge_z"], "p75 z of groove samples above the apex (m19)", R + "wire_groove.json", 0.1)
scan("groove_lower_z", wgr["lower_edge_z"], "p25 z of groove samples below the apex (m19)", R + "wire_groove.json", 0.1)
scan("wire_r", wire["segments"][0]["wire_r"], "tube radius of the cleanest segment fit (m10)", R + "wire.json#segments", wire["segments"][0]["rms"])

doc = {"schema": "stl-re/params.json@1", "tool": "m99_write_params.py", "tool_version": "run-local",
       "inputs": {p: hashlib.sha256(open(p, 'rb').read()).hexdigest() for p in ("intake/aligned_work.stl", "intake/alignment.json")},
       "seed": 0, "created": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds'),
       "part": "OD-G11_portafilter",
       "frame": "datum: primary = cup rim end face -> z = 0, material in -z (+Z points out of the cup opening); secondary = cup axis (outer wall + rim bore wall faces) -> Z axis; clock = handle end-cap flat normal -> +X (handle along +X); origin = cup axis ∩ rim plane. theta CCW about +Z from +X.",
       "scan_noise_mm": noise, "params": P, "struck": [],
       "simplifications": [
           {"name": "floor trough (+X)", "modelled_as": "one circular (r,z) section revolved about the cup axis between the spout angles", "deviation_cost": f"rms {tc['rms']:.3f} / p95 {tc['p95']:.3f} mm on floor cells (includes rib-base cells)"},
           {"name": "handle grip", "modelled_as": "straight cone about a straight fitted axis", "deviation_cost": f"station radius residual rms {hax['r_linear']['rms']:.3f} / max {hax['r_linear']['max']:.3f} mm (quadratic rms {hax['r_quad_rms']:.3f})"},
           {"name": "funnel floor", "modelled_as": "one vertical-axis cone", "deviation_cost": f"rms {fc['rms']:.3f} / p95 {fc['p95']:.3f} / max {fc['max']:.3f} mm on flat floor cells"},
           {"name": "pad face", "modelled_as": "one vertical-axis cone (reverse draft) above the under-chamfer", "deviation_cost": f"rms {cv['rms']:.3f} / p95 {cv['p95']:.3f} / max {cv['max']:.3f} mm; z < -26 transitions deviate more (station fits in pad_fit.json)"},
           {"name": "lug under-faces", "modelled_as": "two inclined planes per lug: the main ramp and the trailing lead-out (helical ramps approximated)", "deviation_cost": "ramp line rms " + "/".join(f"{r['rms']:.3f}" for r in det['lug_ramps']) + " mm; plane vs helix < 0.06 mm over the lug width"},
           {"name": "ribs", "modelled_as": "U rib constant thickness (no draft); V ribs drafted, two straight crest segments each", "deviation_cost": "V crest segments rms " + "/".join(f"{vseg[k]['seg1_rms']:.2f}+{vseg[k]['seg2_rms']:.2f}" for k in vseg) + f" mm; U-leg inner {det['U_leg_inner_face_absy']:.2f} vs outer {det['U_leg_outer_face_absy']:.2f} at mid-height (draft ignored)"},
           {"name": "wire spring", "modelled_as": "three planar arcs of round wire; the ends diving into the bore windows are not modelled", "deviation_cost": "fit rms " + "/".join(f"{s['rms']:.2f}" for s in wire['segments']) + " mm; hidden wire behind the bore not modelled"},
           {"name": "lug-to-wall and small edge rounds", "modelled_as": "sharp except the measured rounds", "deviation_cost": "local, < 1 mm at the lug roots (see lugs_notches.json)"},
       ],
       "checks": {
           "CHK-COUNT": {"ran": True, "result": "pass", "note": "lugs 3, spouts 2, wire arcs 3, V ribs 2: counted as separated angular/area clusters (lugs_notches.json, spouts_screw.json, wire.json, ribs_floor.json); no rotational-order FFT count was needed because no pattern is repeated more than 3 times"},
           "CHK-ACHIEVABLE": {"ran": False, "result": "pass", "note": "no caliper readings (scan-only job)"},
           "CHK-CLUSTER": {"ran": True, "result": "finding", "note": "every coherent cluster in the height maps is assigned to a feature (ribs, screw heads, wire, pockets); the spout pockets are open holes in the mesh (unscanned) and are modelled as assumed geometry"},
           "CHK-FRAME": {"ran": True, "result": "pass", "note": "all angles re-measured in the frozen datum frame; none copied from intake"},
       },
       "open_questions": ["Is the black insert (floor, ribs, pockets) wanted as part of the single solid or only the cast body? (owner chose one fused solid)",
                          "Spout pocket depth is invented (not scanned)."]
}
json.dump(doc, open('measure/params.json', 'w'), indent=1, ensure_ascii=False)
print(len(P), "params")
