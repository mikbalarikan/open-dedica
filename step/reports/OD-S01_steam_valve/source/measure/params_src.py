#!/usr/bin/env python3
"""Source of measure/params.json for OD-S01 (builder-side measurement record).
Every value below was read on intake/aligned_work.stl (datum frame, alignment.json) with the
scripts in measure/ (mlib.py plane_pos / cyl_fit, rprofile.py, loop_simplify.py, spline_pitch.py)
or the stl-re-measure-intent scripts; the estimator and evidence columns say which.
Run: python3 measure/params_src.py  -> writes measure/params.json (then param_table.py renders the table)."""
import json, hashlib, datetime, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
NOISE = json.loads((R/'intake/alignment.json').read_text())['scan_noise_mm']['value']
P = {}
def p(name, value, measured, rule, estimator, evidence, unc=None, source='scan', unit='mm', critical=False, **kw):
    if unc is None: unc = round(NOISE, 3)
    P[name] = dict(value=value, unit=unit, measured=measured, rule=rule, source=source, estimator=estimator,
                   uncertainty_mm=unc, evidence=evidence, critical=critical, **kw)
PL = 'measure/mlib.py plane_pos (p50 of faces with normal within 18 deg of the axis, in a box)'
CY = 'measure/mlib.py cyl_fit (IRLS Cauchy 0.3 circle on wall faces projected along the axis)'
RP = 'measure/rprofile.py (percentile of radial-facing face radii per z bin)'
LS = 'measure/loop_simplify.py (section loop, Douglas-Peucker 0.2) - vertex read'
# ---------------- spindle (F01)
p('spindle_r', 3.70, '3.68..3.75', 'keep-measured', 'median outer radius over theta 45..315 (clear of flat and key), 6 z stations; spline teeth not resolved', 'measure/figures/spline_pitch.json', unc=0.12, critical=True,
  rerun_trigger='a caliper reading of the spindle OD or a tooth count from the mating knob', note='the fine spline (CHK-COUNT finding: order 23..25 not resolved) is modelled as its median cylinder')
p('spindle_tip_z', -14.76, -14.756, 'round-within-noise', PL+' z- faces |x|,|y|<3', 'measure/figures/sec_spindle.png')
p('spindle_flat_x', 2.43, '2.40..2.47', 'keep-measured', PL+' x+ faces on both sides of the key', 'measure/figures/sec_spindle.png', critical=True, rerun_trigger='caliper reading flat-to-opposite-crest')
p('spindle_key_x', 3.82, 3.82, 'keep-measured', PL+' x+ faces |y|<0.5', 'measure/figures/sec_spindle.png', critical=True, rerun_trigger='caliper key height')
p('spindle_key_y', [-0.74, 0.76], [-0.74, 0.759], 'keep-measured', PL+' y- / y+ faces of the key', 'measure/figures/sec_spindle.png', critical=True, rerun_trigger='caliper key width')
p('spindle_tip_chamfer', 0.7, '0.6..0.8', 'keep-measured', RP+' r(z) at theta 180: 3.1 at z -14.8 vs 3.70 body', 'measure/figures/rz_a.png', unc=0.1)
# ---------------- cap disc, skirt, column, neck (F02 revolve)
p('cap_r', 14.36, 14.364, 'keep-measured', CY+' z 0.3..1.9', 'measure/figures/sec_zlow.png', critical=True, rerun_trigger='caliper cap OD')
p('cap_top_z', 2.13, 2.131, 'round-within-noise', PL+' z+ faces z 1.5..3', 'measure/figures/rz_a.png')
p('column_r', 8.60, 8.603, 'keep-measured', CY+' z 16..26', 'measure/figures/rz_a.png', critical=True, rerun_trigger='caliper column OD')
p('column_top_z', 27.67, 27.67, 'round-within-noise', PL+' z+ faces r<8.6, z 26.5..28.5', 'measure/figures/rz_a.png')
p('neck_lo_r', 5.35, 5.346, 'round-within-noise', CY+' z 28..33', 'measure/figures/rz_a.png')
p('neck_up_r', 5.38, 5.382, 'round-within-noise', CY+' z 36.3..42.8', 'measure/figures/rz_a.png', critical=True, rerun_trigger='caliper neck OD')
# ---------------- top clip port (F03)
p('top_blk_x', [-6.36, 6.33], [-6.356, 6.326], 'keep-measured', PL+' x-/x+ faces z 43.5..47', 'measure/figures/sec_ztop.png', critical=True, rerun_trigger='caliper across flats')
p('top_blk_y', [-6.26, 6.16], [-6.263, 6.162], 'keep-measured', PL+' y-/y+ faces z 43.5..47', 'measure/figures/sec_ztop.png', critical=True, rerun_trigger='caliper across flats')
p('top_blk_bot_z', 43.36, 43.358, 'round-within-noise', PL+' z- faces z 41.5..44', 'measure/figures/sec_ztop.png')
p('top_blk_top_z', 47.4, '47.2..47.6', 'keep-measured', 'section sequence z 46.8 (square) / 48.0 (round)', 'measure/figures/sec_ztop.png', unc=0.2)
p('top_round_r', 6.61, 6.613, 'round-within-noise', CY+' z 47.6..48.4', 'measure/figures/sec_ztop.png')
p('top_z', 48.57, 48.573, 'round-within-noise', PL+' z+ faces z 47..49.5', 'measure/figures/sec_ztop.png', critical=True, rerun_trigger='caliper overall height')
p('top_bore_r', 4.97, 4.974, 'keep-measured', CY+' inner wall z 44..48', 'measure/figures/sec_ztop.png', unc=0.125, critical=True, rerun_trigger='pin gauge on the port bore')
p('top_bore_bot_z', 43.9, '43.8..44.0', 'keep-measured', 'section z 43.8 shows the bore wall, z 42.8 does not', 'measure/figures/sec_ztop.png', unc=0.3)
# ---------------- side ports (F04, F05) along -X
p('pu_axis_yz', [12.92, 30.06], '[12.914..12.994, 30.035..30.094]', 'keep-measured', CY+' 4 x-stations', 'measure/figures/sec_xport_up.png', critical=True, rerun_trigger='caliper port centre height')
p('pl_axis_yz', [-14.05, 18.17], '[-14.058..-14.023, 18.148..18.192]', 'keep-measured', CY+' 4 x-stations', 'measure/figures/sec_xport_lo.png', critical=True, rerun_trigger='caliper port centre height')
p('port_r_end', 5.47, '5.461..5.478', 'keep-measured', CY+' x -20.3..-17 (both ports)', 'measure/figures/sec_xport_up.png', critical=True, rerun_trigger='caliper port OD')
p('port_r_root', 5.58, '5.568..5.586', 'keep-measured', CY+' x -11..-8 (both ports): drafted OD', 'measure/figures/sec_xport_up.png')
p('port_bore_r', 4.00, '3.932..4.048', 'keep-measured', CY+' inner wall, 8 stations', 'measure/figures/sec_xport_up.png', critical=True, rerun_trigger='pin gauge on the port bore')
p('port_end_x', -20.44, '-20.47..-20.41', 'keep-measured', PL+' x- end faces of both ports', 'measure/figures/sec_xport_up.png', critical=True, rerun_trigger='caliper overall X')
p('pu_plate_faces', [[6.5, 36.316, 12.5, 35.632, 0.868], [6.5, 24.05, 12.5, 24.487, 0.928]], '[[y 6.5..12.5: 36.316..35.632, under 35.448@6.5], [24.05..24.487, over 24.978@6.5]]', 'keep-measured', 'median z of z-facing faces per 1 mm y-strip, x -19.5..-12 (outer face line (y,z)x2 + thickness to the inner face)', 'measure/figures/sec_xport_up.png', unc=0.08,
  note='plates are drafted (outer faces slope 0.07..0.11 mm/mm); [top plate, bottom plate]')
p('pl_plate_faces', [[-6.5, 24.221, -13.5, 23.689, 0.929], [-5.5, 15.717, -8.5, 15.598, 0.896]], '[[y -6.5..-13.5: 24.221..23.689, under 23.292@-6.5], [15.717..15.598, over 16.613@-5.5]]', 'keep-measured', 'median z of z-facing faces per 1 mm y-strip, x -19.5..-12', 'measure/figures/sec_xport_lo.png', unc=0.08)
p('pu_plate_edge', [[-19.38, 6.25], [-9.74, 2.96]], '[[-19.38,6.25],[-9.74,2.96]] z 24.65; [[-19.45,6.29],[-8.77,2.59]] z 35.7', 'keep-measured', LS+' inner plate edge (two plates share the line)', 'measure/figures/sec_zplates.png', unc=0.2)
p('pl_plate_edge', [[-20.10, -7.25], [-8.61, -2.72]], '[[-20.10,-7.25],[-8.61,-2.72]] z 23.6; [[-15.25,-5.05],[-8.92,-2.81]] z 16.1', 'keep-measured', LS+' inner plate edge', 'measure/figures/sec_zplates.png', unc=0.3)
# ---------------- barb nipple (F06) along -Y
p('barb_axis_xz', [-0.09, 30.76], [-0.086, 30.762], 'keep-measured', CY+' shaft y -19..-10', 'measure/figures/sec_ybarb.png', critical=True, rerun_trigger='caliper')
p('barb_shaft_r', 2.70, 2.695, 'round-within-noise', CY+' shaft y -19..-10', 'measure/figures/sec_ybarb.png', critical=True, rerun_trigger='caliper hose-barb OD')
p('barb_bore_r', 1.42, 1.42, 'keep-measured', CY+' inner wall y -21.5..-15', 'measure/figures/sec_ybarb.png', unc=0.1)
p('barb_crest', [-19.25, 3.45], [-19.25, 3.450], 'keep-measured', 'r p95 per 0.25 mm y-slice (max at y -19.25)', 'measure/figures/sec_ybarb.png', critical=True, rerun_trigger='caliper barb OD')
p('barb_tip', [-21.92, 1.95], [-21.917, '1.87..2.13'], 'keep-measured', PL+' y- tip face; r p95 at y -22..-21.75', 'measure/figures/sec_ybarb.png')
p('barb_back_y', -18.45, '-18.5..-18.4', 'keep-measured', 'r p95 per y-slice falls to the shaft by y -18.5', 'measure/figures/sec_ybarb.png', unc=0.1)
p('barb_collar', [-8.67, -7.30, 4.88], [-8.667, -7.298, 4.88], 'keep-measured', PL+' y faces; '+CY+' y -8.5..-7.5', 'measure/figures/sec_ybarb.png')
# ---------------- microswitch (F07) and bracket (F08)
p('sw_x', [9.73, 15.65], [9.732, 15.652], 'keep-measured', PL+' x faces', 'measure/figures/sec_x_sw.png')
p('sw_y', [-9.66, 10.02], [-9.660, 10.023], 'keep-measured', PL+' y faces', 'measure/figures/sec_x_sw.png')
p('sw_z', [15.74, 25.11], [15.739, 25.112], 'keep-measured', PL+' z faces', 'measure/figures/sec_x_sw.png')
p('sw_blade_y', [[-0.76, -0.26], [7.94, 8.46]], [[-0.758, -0.264], [7.941, 8.459]], 'keep-measured', PL+' blade faces', 'measure/figures/sec_x_sw.png')
p('sw_blade_x', [10.51, 14.09], [10.514, 14.085], 'keep-measured', PL+' blade x faces', 'measure/figures/sec_x_sw.png')
p('sw_blade_top_z', 33.30, 33.295, 'round-within-noise', PL+' blade tops', 'measure/figures/sec_x_sw.png')
p('sw_tab', [8.6, 18.00, 10.0, 11.51, 18.02, 21.11], ['bracket face', 17.997, '9.07..10.02', 11.514, 18.02, 21.108], 'keep-measured', PL+' tab faces (x start at the bracket, x end, y-, y+, z-, z+); sections y 10.5/11.2 show it running from the bracket', 'measure/figures/sec_y_pos.png')
p('brk_box', [-0.29, 8.37, 8.3, 13.35, 15.75, 23.31], [-0.291, 8.368, '8.2..8.4', 13.348, 15.754, 23.313], 'keep-measured', PL+' bracket plate faces (x-, x+ step, y- read from the z 19 section line, y+, z-, z+)', 'measure/figures/sec_y_pos.png', unc=0.2)

# ---------------- lower cam ring (F09): 3-fold posts + trapezoid teeth + pocket floors
UW = 'measure/unwrap.py r_max(theta,z) map (1 deg x 0.2 mm), measure/figures/unwrap_low.png/.npy'
p('cam_floor', [[10.58, 6.0], [9.50, 8.2]], '[[10.38..10.89, 6.0], [9.30..9.92, ~8.2]]', 'keep-measured', UW+' pocket-centre medians z 2.5..5.8 and 6.2..8.1; step z from the map', 'measure/figures/unwrap_low.png', unc=0.2,
  note='pocket floor radius, lower then upper level (r, z_top)')
p('cam_top_z', 8.2, '8.16..8.3', 'keep-measured', PL+' skirt top; map edge', 'measure/figures/unwrap_low.png', unc=0.1)
p('cam_phase', 1.0, [1.0, 121.3, 240.0], 'symmetry', 'post centres from flank-line fits (unwrapped map, r=11.6 crossings); pattern period 120', 'measure/figures/unwrap_low.png', unit='deg', unc=0.2,
  scatter_mm=0.3, scatter_note='3-fold intent (posts at 1/121.3/240.0, teeth at 61.8/181.7/300.35); spread 0.6 deg = 0.13 mm at r 12.6')
p('cam_post_half', 32.1, [32.2, 32.5, 31.2], 'symmetry', 'post half-widths at z 2.5 (flank-line fits)', 'measure/figures/unwrap_low.png', unit='deg', unc=0.3,
  scatter_mm=0.28, scatter_note='3-fold intent; 1.3 deg spread = 0.28 mm at r 12.6')
p('cam_post_r', 12.65, '12.63..12.78', 'keep-measured', UW+' post outer radius z 3..8', 'measure/figures/unwrap_low.png', unc=0.1)
p('cam_tooth_r', 12.49, '12.34..12.59', 'keep-measured', UW+' tooth outer radius z 3..8', 'measure/figures/unwrap_low.png', unc=0.12)
p('cam_flank_z', [2.5, 8.0], [2.5, 8.0], 'keep-measured', 'z stations at which the tooth half-widths were read off the flank-line fits', 'measure/figures/unwrap_low.png', unc=0.1)
p('cam_tooth_half_bot', 22.6, [22.6, 22.6, 22.55], 'symmetry', 'tooth half-width at z 2.5 (flank-line fits, 3 teeth)', 'measure/figures/unwrap_low.png', unit='deg', unc=0.3,
  scatter_mm=0.01, scatter_note='3-fold intent; 0.05 deg spread')
p('cam_tooth_half_top', 13.3, [13.4, 13.5, 12.9], 'symmetry', 'tooth half-width at z 8.0 (flank-line fits, 3 teeth)', 'measure/figures/unwrap_low.png', unit='deg', unc=0.3,
  scatter_mm=0.13, scatter_note='3-fold intent; 0.6 deg spread = 0.13 mm at r 12.5')
p('blk240', [212.0, 269.0, 12.6, 12.3], '[211..214, 266..269, 12.50..12.66, 12.3]', 'keep-measured', UW+' r>12 extent per z', 'measure/figures/unwrap_low.png', unc=0.2)
p('col_windows', [[160.0, 205.0], [340.0, 385.0]], 'theta 155..205 and 335..25 at z 10..15', 'keep-measured', UW+' r<7.5 regions', 'measure/figures/unwrap_low.png', unit='deg', unc=2.0)
p('col_window_cone', [[8.75, 10.2], [6.15, 14.4], [6.15, 15.4]], '(r,z): 10.2 8.71..8.86, 14.4 6.18..6.25, 15.2 6.08..6.24; column resumes by z 16', 'keep-measured', 'fine r(z) of outward faces inside the two window sectors (theta 165..195, 350..8)', 'measure/figures/profiles.json#window_180', unc=0.12)

p('port_web_x0', -15.5, [-15.5, -15.5], 'mean-of-n', 'x of the -X-facing web face (both ports): area histogram, 0.25 mm bins', 'measure/figures/sec_xport_up.png', unc=0.15)
p('port_web_x1', -13.625, [-13.5, -13.75], 'mean-of-n', 'area histogram (0.25 mm bins) of x-facing faces inside the bore r<3.9, both ports', 'measure/figures/sec_xport_up.png', unc=0.15)
p('port_orifice_r', 2.0, '1.94..2.09', 'keep-measured', 'p5 radius of x-facing web faces (both ports)', 'measure/figures/sec_xport_up.png', unc=0.1)
p('fin', [12.79, -4.76, -3.52, 8.52], [12.794, -4.758, -3.523, 8.518], 'keep-measured', PL+' fin faces (x end, y-, y+, z bottom); top meets the switch bottom', 'measure/figures/sec_zlow.png', unc=0.1)

p('port_window', [-8.0, 4.0], '[-8 (U end at x -12), 4.0]', 'keep-measured', 'side renders: U-window from x -0.3 to -12 (semicircle end), height 8 = bore diameter; centre x of the end arc and radius', 'measure/figures/zoom_up_py.png', unc=0.5,
  note='window opens the bore on the +Y side of the upper port and the -Y side of the lower port')
p('port_trim', [-5.0, 13.52, -13.30], [None, 13.515, -13.3], 'keep-measured', PL+' flats beside the windows (x -6..-1.5): x start, upper +Y flat, lower -Y flat', 'measure/figures/sec_xport_up.png', unc=0.2)

p('top_slot', [0.85, 4.45, 44.63, 45.87], [0.84, 4.57, 44.61, 45.9], 'symmetry', 'x=+-6.0 section loops of the two clip slots per side (1st/99th percentiles), 4 instances', 'measure/figures/sec_x_top.png', unc=0.1,
  scatter_mm=0.14, scatter_note='mirror intent about y=0 and x=0; 0.14 spread over 4 instances')
p('top_blk_edge_r', 1.7, '1.5..1.9', 'keep-measured', 'x=+-6 section: corner arcs of the lug outline (edges parallel to X at y=+-6.2, z 43.4/47.4)', 'measure/figures/sec_x_top.png', unc=0.2)
p('collar_z', 10.2, '10.0..10.4', 'keep-measured', UW+' collar level ends between z 10.0 and 10.4', 'measure/figures/unwrap_low.png', unc=0.2)
p('collar_sectors', [[328.0, 388.0, 9.45], [152.0, 210.0, 9.85], [270.0, 288.0, 9.55], [72.0, 99.0, 9.42]], 'z 9.0 row: 328..28 9.38-9.6, 152..209 9.85, 270..287 9.58, 72..96 9.41', 'keep-measured', UW+' 1-deg runs at z 9.0 (theta0, theta1, r)', 'measure/figures/unwrap_low.png', unc=0.2)
p('rib_sectors', [[17.0, 28.0, 9.36], [72.0, 99.0, 9.42], [151.0, 160.0, 9.56], [201.0, 210.0, 9.90], [270.0, 287.0, 9.55]], 'runs at z 10.4..12.8 with r 9.36..9.92', 'keep-measured', UW+' 1-deg runs at z 10.4/11.0/11.6/12.2 (theta0, theta1, r)', 'measure/figures/unwrap_low.png', unc=0.2)
p('rib_top_z', 13.0, '12.8..13.4', 'keep-measured', UW+' ribs present at z 12.8, gone by z 14 (r 8.5..8.6 there)', 'measure/figures/unwrap_low.png', unc=0.3)
p('cap_slot_3', [-10.87, 0.13, 88.3, 2.0, 0.8], [-10.87, 0.13, 88.3, 2.0, 0.8], 'keep-measured', 'centre and axis from the partial wall loop (1.31 x 0.58 visible); size 2.0 x 0.8 from the -Z render (it1 used 4.0 x 1.0, flagged by QA c2s cluster 6)', 'intake/figures/view_mz.png', unc=0.5)
p('cap_slot_1', [3.16, 8.69, 131.7, 5.0, 2.1], [3.04, 8.83, 131.5, 4.6, 2.22], 'symmetry', 'slot wall faces z 0.15..2 (centre, long-axis angle, length, width from SVD extents); slot 3 barely scanned, size from the -Z render', 'measure/figures/sec_z_cap.png', unc=0.3,
  scatter_mm=0.6, scatter_note='slots 1 and 2 mirror about the X axis (the scan shows them as mirror images); size averaged, spread 0.6 mm')
p('cap_slot_2', [3.16, -8.69, 48.3, 5.0, 2.1], [3.28, -8.55, 48.1, 5.77, 2.58], 'symmetry', 'slot wall faces z 0.15..2 (centre, long-axis angle, length, width from SVD extents)', 'measure/figures/sec_z_cap.png', unc=0.3,
  scatter_mm=0.6, scatter_note='mirror of slot 1 about the X axis; size averaged, spread 0.6 mm')

p('holder_y0', -4.97, -4.974, 'keep-measured', PL+' -y face of the switch holder between the column and the switch (x 7.3..9.6)', 'measure/figures/sec_z_brk.png', unc=0.2)
p('col_top_fillet', 1.5, '1.4..1.6', 'keep-measured', 'fine r(z) profile (theta windows clear of attachments): r 8.57 at z 25.9 -> 7.4 at 27.5, top at 27.67', 'measure/figures/profiles.json#column_top', unc=0.15)
p('groove_profile', [[5.35, 32.9], [4.85, 34.0], [4.02, 34.75], [4.02, 35.35], [4.63, 36.0], [5.21, 36.8], [5.38, 37.3]], '(r,z) p50 per 0.2 mm: 33.0 5.31, 34.0 4.85, 34.8 4.00, 35.2 3.99, 36.0 4.63, 36.8 5.21, 37.2 5.33', 'keep-measured', 'fine r(z) profile, theta windows 300..60 and 165..250 (clear of attachments)', 'measure/figures/profiles.json#neck_groove', unc=0.08)
p('top_cbore', [5.45, 46.8], '[5.1..5.68 (ribbed), 46.6..47.0]', 'keep-measured', 'fine r(z) inner radii z 46.6..48.6 (p10..p50; internal ribs averaged)', 'measure/figures/sec_ztop.png', unc=0.25)

p('finger_slot', [10.5, 6.5], '[10.23..11.15, visible from z 6.5]', 'keep-measured', 'inward-facing faces at r 9.8..12.4 in the tooth sectors (only seen z 6.5..8)', 'measure/figures/unwrap_low.png', unc=0.3,
  note='slot behind the top of each trapezoid tooth (snap finger); its bottom is not visible below z 6.5 (occluded), so 6.5 is the visibility limit, not a measured floor')

# ---- iteration 2 additions (QA it1 findings, _it1_SUPERSEDED/qa/VERDICT.md)
p('port_col_x', -0.12, [-0.129, -0.117], 'mean-of-n', PL+' +X-facing end walls of both port blocks beside the neck (it1 CAD stopped at x -1: QA clusters 0, 2)', 'measure/figures/sec_xport_up.png', unc=0.05)
p('port_junction_x0', -4.0, -4.0, 'keep-measured', 'x sections -4..0: the port blocks are solid from the neck to the U-window between the plates (sec_xport_up/lo x -4, -2, -1, -0.5)', 'measure/figures/sec_xport_up.png', unc=0.5)
p('pu_lip', [-1.34, 9.4, 22.60], [-1.337, 9.4, 22.595], 'keep-measured', PL+' -X face x, y start (QA cluster 10), bottom z of the lip under the upper port block', 'measure/figures/sec_xport_up.png', unc=0.1)
p('sw_bump', [10.7, 13.9, 1.79, 3.84, 14.39], [10.7, 13.895, 1.794, 3.837, 14.387], 'keep-measured', PL+' bump faces under the switch (x-, x+, y-, y+, bottom); x- from the z 14.6 loop (QA cluster 4)', 'measure/figures/sec_z_brk.png', unc=0.1)
p('bar330', [12.3, -6.74, -5.6, 10.85, 12.22], [12.3, -6.737, -5.6, 10.846, 12.222], 'keep-measured', PL+' bar faces (x end and y+ from the QA cluster-5 extents, y-, bottom, top)', 'measure/figures/rz_b.png', unc=0.1)
p('lug320', [312.1, 328.5, 10.41, 22.26, 23.16], [312.1, 328.5, 10.41, 22.26, 23.163], 'keep-measured', 'theta 2/98 pct, r p95, bottom/top faces of the column lug (QA cluster 8)', 'measure/figures/rz_b.png', unc=0.1)
p('barb_rib', [-0.32, 0.23, -8.67, 36.85, -4.5, 37.53], [-0.317, 0.231, -8.67, 36.85, -4.5, 37.527], 'keep-measured', PL+' rib side faces; top z at the collar (section y -8.0) and near the neck (z+ faces p50)', 'measure/figures/sec_ybarb.png', unc=0.15)
p('top_bore2', [3.61, 43.0], [3.61, 43.007], 'keep-measured', 'lower bore wall r p50 z 42.2..43.8 and floor z+ faces p50 (QA cluster 9: floor ~1 mm lower than it1)', 'measure/figures/sec_ztop.png', unc=0.15)
p('blk120_lo', [100.0, 150.0, 14.0, 12.4], [100.0, 150.0, 14.0, 12.39], 'keep-measured', UW+' r>13.3 extent below z 12 (theta0, theta1, r, top z at theta 145)', 'measure/figures/rz_b.png', unc=0.2)
p('blk120_up', [104.0, 142.0, 10.05, 14.0, 15.05], [104.0, 142.0, 10.05, 14.0, 15.048], 'keep-measured', 'upper shell: theta edges (unwrap), inner wall r median theta 115..140, outer r, flat top z p50 theta 125..140', 'measure/figures/rz_b.png', unc=0.2)
p('blk120_slope', [104.0, 12.0, 125.0, 15.05], [104.0, 12.0, 125.0, 15.048], 'keep-measured', UW+' left edge of the r>13.3 region: theta 104 at z 12.0 rising to theta 125 at the flat top (QA cluster 1: it1 used 2 flat steps)', 'measure/figures/unwrap_low.png', unc=0.5)
p('holder_edge', [3.86, 7.0, 6.6, 4.9], [3.86, 7.0, 6.6, 4.9], 'keep-measured', 'x 2/98 pct of the holder top/bottom faces per 1 mm y-strip (y 5: x>=6.44..6.67, y 6: 5.54..5.67, y 7: 3.83..3.86, y 8..9: 2.07..2.28): inner diagonal edge from (3.86, 7.0) to (6.6, 4.9); for x < 3.86 the scanned -y face at y 8.2..8.6 is the bracket underside; the region inside it (toward the column) is open (QA c2s cluster 4)', 'measure/figures/sec_z_brk.png', unc=0.3)


def _isnum(v): return isinstance(v, (int, float)) and not isinstance(v, bool)
def _flat_ok(v): return isinstance(v, list) and v and all(_isnum(x) for x in v)
FLAT = {}
for k, q in list(P.items()):
    v, m_ = q['value'], q['measured']
    if isinstance(v, list) and v and all(isinstance(x, list) for x in v):
        del P[k]
        for i, vi in enumerate(v, 1):
            qi = dict(q, value=vi)
            if isinstance(m_, list) and len(m_) == len(v) and _flat_ok(m_[i - 1]) and len(m_[i - 1]) == len(vi):
                qi['measured'] = m_[i - 1]
            else:
                qi['measured'] = list(vi); qi['note'] = (q.get('note', '') + ' measured: ' + str(m_)).strip()
            if qi['rule'] == 'keep-measured' and qi['measured'] != vi:
                qi['rule'] = 'round-within-noise' if all(abs(a - b) <= NOISE for a, b in zip(vi, qi['measured'])) else qi['rule']
            FLAT[f'{k}_{i}'] = qi
        continue
    if isinstance(v, list):
        if not _flat_ok(m_) or len(m_) != len(v):
            q['note'] = (q.get('note', '') + ' measured: ' + str(m_)).strip(); q['measured'] = list(v)
        elif q['rule'] == 'keep-measured' and any(abs(a - b) > 1e-9 for a, b in zip(v, m_)):
            if all(abs(a - b) <= NOISE for a, b in zip(v, m_)): q['rule'] = 'round-within-noise'
            else: q['value'] = list(m_)
    elif _isnum(v) and _isnum(m_) and q['rule'] == 'keep-measured' and abs(v - m_) > 1e-9:
        q['rule'] = 'round-within-noise' if abs(v - m_) <= NOISE else q['rule']
P.update(FLAT)

meta = dict(schema='stl-re/params.json@1', tool='measure/params_src.py', tool_version='OD-S01 builder',
            inputs={p_: hashlib.sha256((R/p_).read_bytes()).hexdigest() for p_ in ['intake/aligned_work.stl', 'intake/alignment.json']},
            seed=0, created=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
            part='OD-S01_steam-valve',
            frame='datum frame of intake/alignment.json: primary = cap disc outer face (z=0, +Z into the body), axis = upper valve column, clock = microswitch outer face normal -> +X; theta CCW about +Z from +X',
            scan_noise_mm=NOISE)
out = dict(meta, params=P, struck=[], simplifications=[], checks={}, open_questions=[])
extra = R/'measure/params_extra.json'
if extra.exists(): out.update({k: v for k, v in json.loads(extra.read_text()).items()})
(R/'measure/params.json').write_text(json.dumps(out, indent=1))
print(len(P), 'params written')
