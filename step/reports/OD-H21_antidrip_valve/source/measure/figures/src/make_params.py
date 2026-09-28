"""make_params.py - build measure/params.json from measure/figures/fits.json (OD-H21).
Every value is scan authority (scan-only job). Rule 'keep-measured' = value is the fitted estimate
(rounded to 4 decimals, far inside the 0.0347 mm noise floor, so measured == value exactly).
Derived profile vertices (e.g. where two fitted surfaces intersect) are computed here from fitted
params and recorded with the derivation in 'estimator'."""
from __future__ import annotations
import datetime, hashlib, json
from pathlib import Path
import numpy as np
RUN = Path(__file__).resolve().parents[3]
F = json.loads((RUN / 'measure/figures/fits.json').read_text())
AL = json.loads((RUN / 'intake/alignment.json').read_text())
NOISE = AL['scan_noise_mm']['value']
FJ = 'measure/figures/fits.json'
R4 = lambda x: [round(float(v), 4) for v in x] if isinstance(x, (list, tuple, np.ndarray)) else round(float(x), 4)
P: dict = {}

def km(name, val, unit, est, ev, unc=None, crit=False, trig=None, note=None, frame=None):
    v = R4(val)
    row = dict(value=v, unit=unit, measured=v, rule='keep-measured', source='scan', estimator=est,
               uncertainty_mm=round(float(unc if unc is not None else NOISE), 4), evidence=ev, critical=crit)
    if trig: row['rerun_trigger'] = trig
    if note: row['note'] = note
    if frame: row['frame'] = frame
    P[name] = row

def assumed(name, val, unit, est, note, crit=False):
    P[name] = dict(value=val, unit=unit, measured=None, rule='assumed', source='assumed', estimator=est,
                   uncertainty_mm=None, evidence='build/MODELING_PLAN.md §6', critical=crit, note=note)

S = F['segments']; L = F['levels']; RD = F['rounds']; O = F['outlet']; B = F['barb']
TRIG = 'one caliper reading of this feature -> re-run measure (scan-only value, CHK-SCALE FLAG)'
FR = 'datum frame; theta CCW about +Z from +X (+X = outlet collar normal)'
# ---- poses (datum frame)
n = S['nozzle']
km('noz_axis_c', [n['cx'], n['cy']], 'mm', f"tilted-cylinder fit (soft-l1) of nozzle OD faces z -22.3..-14.7, r 5.3..6.3; centre at z0={n['z0']}; rms {n['rms']:.4f}", FJ + '#segments.nozzle', n['rms'],
   note='nozzle axis point at z = -18.5 (datum). Nozzle is its own sub-part (as-scanned assembly)')
km('noz_axis_tilt', [n['tx_deg'], n['ty_deg']], 'deg', 'same fit: axis direction = (tan tx, tan ty, 1) normalised', FJ + '#segments.nozzle', n['rms'], frame=FR,
   note=f"total tilt {n['tilt_deg']:.3f} deg vs band-face normal (CHK-TILT finding, alignment.json)")
for k, nm in [('nut', 'nut'), ('band_lo', 'bandlo'), ('band_up', 'bandup'), ('body', 'body')]:
    s = S[k]
    km(f'{nm}_axis_c', [s['cx'], s['cy']], 'mm', f"centre of the {k} surface fit (tilt fixed 0: tilt-free fit gives {S.get(k+'_tiltfree', {}).get('tilt_deg', 'n/a')} deg); rms {s['rms']:.4f}",
       FJ + f'#segments.{k}', s['rms'], note='axis parallel to datum Z; centre offset kept as scanned (assembly misalignment beyond noise, intent-rules §5)')
c = S['cap_part']
km('cap_axis_c', [c['cx'], c['cy']], 'mm', f"joint ring+cap tilted-cylinder fit, centre at z0=17.0; ring rms {c['ring']['rms']:.4f}, cap rms {c['cap']['rms']:.4f}", FJ + '#segments.cap_part', c['cap']['rms'])
km('cap_axis_tilt', [c['tx_deg'], c['ty_deg']], 'deg', 'same joint fit: axis = (tan tx, tan ty, 1)', FJ + '#segments.cap_part', c['cap']['rms'], frame=FR,
   note=f"cap part tilted {c['tilt_deg']:.3f} deg towards {c['tilt_dir_deg']:.1f} deg: as-scanned assembly state, kept (a square cap would leave ~0.7 mm at r 12)")
km('outlet_axis_p', O['axis_p'], 'mm', 'outlet tube tilted-cylinder fit u 11..19.2 (3 refinements), point where the axis crosses the plane through Z normal to its horizontal projection', FJ + '#outlet', O['tube']['rms'])
km('outlet_axis_d', O['axis_d'], 'mm', f"same fit; unit direction (az {O['az_deg']:.3f} deg, elev {O['elev_deg']:.3f} deg)", FJ + '#outlet', O['tube']['rms'], note='unit vector (unit field mm = dimensionless direction cosines)')
km('barb_axis_p', B['axis_p'], 'mm', 'barb tube tilted-cylinder fit u 13.5..22.5, re-anchored at the Z axis', FJ + '#barb', B['tube']['rms'])
km('barb_axis_d', B['axis_d'], 'mm', f"same fit; unit direction (az {B['az_deg']:.3f} deg, elev {B['elev_deg']:.3f} deg)", FJ + '#barb', B['tube']['rms'], note='unit vector')
# ---- nozzle sub-part (u along the nozzle axis, u = datum z at the axis point)
km('noz_R', n['R'], 'mm', 'radius of the nozzle tilted-cylinder fit', FJ + '#segments.nozzle', n['rms'], crit=True, trig=TRIG)
km('noz_tip_u', L['nozzle_tip']['u_median'], 'mm', 'median axial coordinate of tip-face faces (n.axis < -0.97, r 4.2..5.4)', FJ + '#levels.nozzle_tip', L['nozzle_tip']['scatter'])
km('noz_tip_round_R', RD['nozzle_tip_outer']['a'], 'mm', '(u,rho) circle fit to the tip outer edge vertices u -27.3..-26.8', FJ + '#rounds.nozzle_tip_outer', RD['nozzle_tip_outer']['rms'])
km('noz_root_R', RD['shoulder_root']['a'], 'mm', '(u,rho) circle fit to the nozzle/shoulder root fillet vertices', FJ + '#rounds.shoulder_root', RD['shoulder_root']['rms'])
nb = F['nozzle_bore']
km('noz_bore_R', nb['r'], 'mm', 'IRLS circle on bore-wall vertices u -26.9..-25.0 (nozzle frame)', FJ + '#nozzle_bore', nb['rms'], crit=True, trig=TRIG)
BF = F['bore_floors']
km('noz_bore_floor_u', 0.5 * (BF['nozzle']['u_p10'] + BF['nozzle']['u_p90']), 'mm', BF['nozzle']['method'] + ': minimax level = mid of p10..p90' + f" (p10 {BF['nozzle']['u_p10']:.3f}, p90 {BF['nozzle']['u_p90']:.3f}); bore wall observed up to u -23.8 (p95 of wall vertices)",
   FJ + '#bore_floors.nozzle; intake/coverage.json loop 1', 0.3, note='blind recess to the observed (bridged) floor only; the real flow bore continues (unscanned), not invented')
lg = F['lip']
km('lug_c', [lg['cx'], lg['cy']], 'mm', 'rounded-rectangle SDF fit (soft-l1) to the outer envelope u -24.8..-23.6 (points outside the nozzle cylinder; latch-window side excluded)', FJ + '#lip', lg['rms'])
km('lug_half_a', lg['half_a'], 'mm', 'same fit: half-width along phi (this side lies inside the nozzle cylinder, set by the corners)', FJ + '#lip', lg['rms'],
   note=f"band-to-band spread {min(b['half_a'] for b in lg['bands'].values()):.3f}..{max(b['half_a'] for b in lg['bands'].values()):.3f} (hidden side, corners only)")
km('lug_half_b', lg['half_b'], 'mm', 'same fit: half-width along phi+90 (the latch-window sides)', FJ + '#lip', lg['rms'], crit=True, trig=TRIG)
km('lug_corner_R', lg['corner_r'], 'mm', 'same fit: corner radius', FJ + '#lip', lg['rms'])
km('lug_phi_deg', lg['phi_deg'], 'deg', 'same fit: direction of the a-side normal in the nozzle local frame (e1 = datum X projected)', FJ + '#lip', lg['rms'], frame='nozzle local frame, theta CCW about the nozzle axis from projected datum +X')
cz = np.array(lg['corner_z_p1_p99'])
km('lug_u_lo', float(np.median(cz[:, 0])), 'mm', 'median over 4 corners of the p1 axial coordinate of corner vertices (rho > 7.2)', FJ + '#lip.corner_z_p1_p99', float(np.std(cz[:, 0])))
km('lug_u_hi', float(np.median(cz[:, 1])), 'mm', 'median over 4 corners of the p99 axial coordinate of corner vertices', FJ + '#lip.corner_z_p1_p99', float(np.std(cz[:, 1])))
LW = F['latch_windows']
km('latch_theta0_deg', [x['recess_theta'][0] for x in LW], 'deg', 'per lug b-side (phi+90, phi-90): first/last 4-deg bin where the scan envelope (u -25.2..-24.65) lies > 0.25 mm inside the fitted lug outline', FJ + '#latch_windows', 2.0, frame='nozzle local frame')
km('latch_theta1_deg', [x['recess_theta'][1] for x in LW], 'deg', 'same: upper angular edge', FJ + '#latch_windows', 2.0, frame='nozzle local frame')
km('latch_u_lo', [x['u_p3_p97'][0] for x in LW], 'mm', 'p3 axial coordinate of wall vertices inside noz_R - 0.12 within the window span', FJ + '#latch_windows', 0.1)
km('latch_u_hi', [x['u_p3_p97'][1] for x in LW], 'mm', 'same: p97 axial coordinate', FJ + '#latch_windows', 0.1)
km('latch_floor_rho', [x['recess_floor_rho'] for x in LW], 'mm', 'median envelope radius over the central bins (bins deeper than 5.3 excluded): the lugs are cut back to about the nozzle cylinder between the corners', FJ + '#latch_windows', 0.1)
dw = [x for x in LW if 'deep_theta' in x][0]
km('latch_deep_theta', dw['deep_theta'], 'deg', 'contiguous 4-deg bins with envelope < 5.3 (through-window into the bore, partly bridged) on the phi+90 side', FJ + '#latch_windows', 2.0, frame='nozzle local frame')
km('latch_deep_floor_rho', dw['deep_floor_rho'], 'mm', 'median envelope radius of those bins (observed bridged floor; the bore wall shows at 3.9 in places)', FJ + '#latch_windows', 0.4,
   note='cut to the observed (bridged) floor, not through to the bore')
# ---- nut
s = S['nut']
km('nut_shoulder_u', L['shoulder']['u_median'], 'mm', 'median axial coordinate of shoulder faces (normal < -0.97 along the nut axis, r 7..10)', FJ + '#levels.shoulder', L['shoulder']['scatter'])
km('nut_R0', s['R'], 'mm', 'drafted-cone fit of the nut base between ribs (ribs +-11 deg excluded), radius at z0=-10', FJ + '#segments.nut', s['rms'])
km('nut_k', s['k'], 'mm', f"same fit: d rho / d u (draft {s['draft_deg']:.3f} deg, wider towards +Z)", FJ + '#segments.nut', s['rms'], note='unit mm/mm')
ch = F['nut_chamfer']
u_x = (s['R'] + s['k'] * (0 + 10.0) - ch['rho_at_m6p7'] - ch['slope_drho_du'] * 6.7) / (ch['slope_drho_du'] - s['k'])
km('nut_chamfer_u0', u_x, 'mm', 'derived: intersection of the nut cone with the line fit through the nut->band transition (u -6.7..-6.15, ribs excluded)', FJ + '#nut_chamfer', ch['rms'])
km('nut_top_u', -6.15, 'mm', 'upper end of the straight chamfer fit window (the transition curves on into the band above it)', FJ + '#nut_chamfer; #tables body_frame', ch['rms'])
km('nut_top_rho', ch['rho_at_m6p15'], 'mm', 'chamfer line evaluated at nut_top_u', FJ + '#nut_chamfer', ch['rms'])
rb = F['ribs']
km('rib_theta_deg', [r['theta_deg'] for r in rb], 'deg', 'per rib: IRLS circle (scale 0.1) on rib faces r > base+0.2, z -13.2..-7.3, angle of the rod centre about the nut axis', FJ + '#ribs', 0.3, frame=FR,
   note='pitch 44.9..45.4 deg, phase 23.75 +- 0.25: equal pitch within the measured scatter, kept as measured per instance')
km('rib_rho_c', [r['rho_c'] for r in rb], 'mm', 'same fits: rod-centre radius about the nut axis', FJ + '#ribs', 0.1)
km('rib_rod_R', [r['rod_r'] for r in rb], 'mm', 'same fits: rod radius (rib crest modelled as a vertical cylinder)', FJ + '#ribs', 0.1)
P['rib_count'] = dict(value=8, unit='count', measured=8, rule='keep-measured', source='scan',
    estimator='pattern_count.py radius signal, 3 stations z -12.5/-10/-7.8, FFT-dominant rotational order 8 at every station, residual local minimum (CHK-COUNT pass)',
    uncertainty_mm=0.0, evidence='measure/figures/count_nut_ribs.json', critical=False)
# ---- band / body
s = S['band_lo']
km('bandlo_R0', s['R'], 'mm', 'drafted-cone fit of the lower band ring u -5.8..-2.9 (outlet sector excluded), radius at z0=-4.35', FJ + '#segments.band_lo', s['rms'])
km('bandlo_k', s['k'], 'mm', f"same fit: d rho/d u (draft {s['draft_deg']:.2f} deg)", FJ + '#segments.band_lo', s['rms'], note='unit mm/mm')
km('bandlo_base_u', -5.6, 'mm', 'profile table (band frame): first station where rho p50 reaches the cone within noise (12.12 vs 12.14); the nut->band transition ends here', FJ + '#tables_cols; measure/figures/fits.json tables body_frame', 0.1)
km('band_step_u', L['band_step']['u_median'], 'mm', 'median axial coordinate of the up-facing step faces (normal > 0.9) at r 12.0..12.3', FJ + '#levels.band_step', L['band_step']['scatter'])
s = S['band_up']
km('bandup_R', s['R'], 'mm', 'cylinder fit of the upper band ring u -2.3..-0.75', FJ + '#segments.band_up', s['rms'])
km('bandup_top_round_R', RD['band_up_top']['a'], 'mm', '(u,rho) circle fit to the band top outer edge', FJ + '#rounds.band_up_top', RD['band_up_top']['rms'])
km('primary_u', L['primary']['u_median'], 'mm', 'median axial coordinate of the band top face (= the datum primary, z=0 by construction)', FJ + '#levels.primary', L['primary']['scatter'])
s = S['body']
km('body_R', s['R'], 'mm', 'cylinder fit of the body u 0.5..8.4 (outlet sector +-35 deg excluded)', FJ + '#segments.body', s['rms'])
# ---- cap part (u along the cap axis)
km('ring_R', c['R_ring'], 'mm', 'joint cap-part fit: ring skirt radius (windows excluded)', FJ + '#segments.cap_part', c['ring']['rms'])
km('cap_R', c['R_cap'], 'mm', 'joint cap-part fit: cap radius (barb sector excluded)', FJ + '#segments.cap_part', c['cap']['rms'])
km('ring_bottom_u', L['ring_bottom']['u_median'], 'mm', 'median axial coordinate of down-facing faces along the cap axis, r 10.3..12.6', FJ + '#levels.ring_bottom', L['ring_bottom']['scatter'])
km('ring_bottom_round_R', RD['ring_bottom_outer']['a'], 'mm', '(u,rho) circle fit to the ring bottom outer edge', FJ + '#rounds.ring_bottom_outer', RD['ring_bottom_outer']['rms'])
km('ring_top_u', L['ring_top']['u_median'], 'mm', 'median axial coordinate of up-facing faces r 12.3..12.9 (ring top step)', FJ + '#levels.ring_top', L['ring_top']['scatter'])
km('ring_top_round_R', RD['ring_top_outer']['a'], 'mm', '(u,rho) circle fit to the ring top outer edge', FJ + '#rounds.ring_top_outer', RD['ring_top_outer']['rms'])
km('cap_root_R', RD['cap_root']['a'], 'mm', '(u,rho) circle fit to the concave cap root fillet', FJ + '#rounds.cap_root', RD['cap_root']['rms'])
km('cap_top_u', L['cap_top']['u_median'], 'mm', 'median axial coordinate of up-facing faces r 3.5..11.5 along the cap axis', FJ + '#levels.cap_top', L['cap_top']['scatter'])
km('cap_top_round_R', RD['cap_top_edge']['a'], 'mm', '(u,rho) circle fit to the cap top edge', FJ + '#rounds.cap_top_edge', RD['cap_top_edge']['rms'])
W = F['ring_windows']
km('win_theta_deg', [x['theta_c'] for x in W], 'deg', 'centre of each envelope gap (rho < 13.0 at u 13.0..13.8, 0.5 deg bins, gaps <= 1 deg merged) in the cap local frame', FJ + '#ring_windows', 0.5, frame='cap local frame (e1 = datum X projected), CCW')
km('win_width_deg', [x['width_deg'] for x in W], 'deg', 'angular width of each gap', FJ + '#ring_windows', 0.5)
km('win_u_lo', [x['u_lo'] for x in W], 'mm', 'p1 axial coordinate of the window-interior vertices', FJ + '#ring_windows', 0.1)
km('win_u_hi', [x['u_hi'] for x in W], 'mm', 'p99 axial coordinate of the window-interior vertices', FJ + '#ring_windows', 0.1)
km('win_floor_rho', [x['floor_rho_deep_median'] for x in W], 'mm', 'median radius of window-interior vertices deeper than 0.7 mm below the ring surface, central half of the window (the latch hooks seen through the windows)', FJ + '#ring_windows', 0.3,
   note='pockets cut to the observed floor, per window; interiors beyond are unscanned')
SL = F['skirt_slits']
km('slit_theta0_deg', [x['theta_p2_p98'][0] for x in SL], 'deg', 'slits under the ring skirt (open loops L5, L7): p2 angular edge of scan vertices with rho 10.15..12.5, u 9.7..12.5 in the cap frame', FJ + '#skirt_slits', 1.0, frame='cap local frame')
km('slit_theta1_deg', [x['theta_p2_p98'][1] for x in SL], 'deg', 'same: p98 angular edge', FJ + '#skirt_slits', 1.0, frame='cap local frame')
km('slit_u_top', [x['u_p98'] for x in SL], 'mm', 'same: p98 axial coordinate (top of the visible slit)', FJ + '#skirt_slits', 0.1)
km('slit_rho_in', [x['rho_p2_p98'][0] for x in SL], 'mm', 'same: p2 radius', FJ + '#skirt_slits', 0.1)
km('slit_rho_out', [x['rho_p2_p98'][1] for x in SL], 'mm', 'same: p98 radius', FJ + '#skirt_slits', 0.1,
   note='assembly gap between the cap-part skirt and the body, visible at two places only; interior beyond is unscanned')
WB = F['outlet_ring_web']
km('web_hw_at_10p5', WB['hw_at_10p5'], 'mm', f"linear fit of the web half-width vs x over {WB['n_sections']} two-sided section crossings at z 8.3/8.4/8.5 (between the outlet tube top and the ring bottom), value at x 10.5", FJ + '#outlet_ring_web', WB['fit']['rms'])
km('web_hw_slope', WB['hw_slope'], 'mm', 'same fit: d(half-width)/dx', FJ + '#outlet_ring_web', WB['fit']['rms'], note='unit mm/mm')
km('web_y_centre', WB['y_centre'], 'mm', 'median centre y of the same crossings (datum frame)', FJ + '#outlet_ring_web', WB['fit']['rms'])
# ---- outlet (u along the outlet axis from outlet_axis_p)
T = O['tube']
km('out_tube_R', T['R'], 'mm', 'outlet tube cylinder fit u 11..19.2', FJ + '#outlet.tube', T['rms'])
km('out_root_R', O['root_round']['a'], 'mm', '(u,rho) circle fit to the tube/collar concave fillet', FJ + '#outlet.root_round', O['root_round']['rms'])
km('out_collar_in_u', O['collar_inner_face']['u'], 'mm', 'median u of collar inner-face faces (normal < -0.95)', FJ + '#outlet.collar_inner_face', O['collar_inner_face']['scatter'])
km('out_collar_R', O['collar_R'], 'mm', 'median rho of collar OD faces u 20.9..22.3', FJ + '#outlet', O['collar_R_stats']['rms'], crit=True, trig=TRIG)
km('out_collar_round_R', O['collar_round']['a'], 'mm', '(u,rho) circle fit to the collar inner outer edge', FJ + '#outlet.collar_round', O['collar_round']['rms'])
km('out_collar_out_u', O['collar_outer_face']['u'], 'mm', 'median u of collar outer-face faces (normal > 0.95; the clock plane)', FJ + '#outlet.collar_outer_face', O['collar_outer_face']['scatter'])
og = O['oring']
km('oring_u', og['u_c'], 'mm', '(u,rho) circle fit to the O-ring section vertices u 22.85..24.35, rho 4.9..5.7', FJ + '#outlet.oring', og['rms'], crit=True, trig=TRIG)
km('oring_rho', og['rho_c'], 'mm', 'same fit: section centre radius (torus major radius)', FJ + '#outlet.oring', og['rms'], crit=True, trig=TRIG)
km('oring_a', og['a'], 'mm', 'same fit: section radius (torus minor radius)', FJ + '#outlet.oring', og['rms'], crit=True, trig=TRIG)
th_ = O['thread_rho']
km('out_thread_R', th_['mean'], 'mm', f"mean rho of thread-zone vertices u 25..29 (p1 {th_['p1']:.3f}, p99 {th_['p99']:.3f}); plain cylinder in place of the helix", FJ + '#outlet.thread_rho', (th_['p99'] - th_['p1']) / 2,
   crit=True, trig='thread gauge / caliper on the crests -> re-run; a helical thread would need the scan to resolve the profile')
km('out_thread_pitch', O['thread_pitch']['pitch'], 'mm', 'helical phase coherence of (rho - mean) over (u, theta), pitch scan 0.80..1.10 step 0.002, both hands', FJ + '#outlet.thread_pitch', 0.01,
   note='0.908 = 28 TPI (BSP/G 1/8) within 0.001: recorded for identification only, not modelled (plain cylinder)')
ec = O['end_chamfer']
km('out_chamfer_slope', ec['slope'], 'mm', 'line fit of rho(u) over u 29.3..29.85 (end chamfer)', FJ + '#outlet.end_chamfer', 0.05, note='unit mm/mm')
km('out_chamfer_rho0', ec['rho_at_29p3'], 'mm', 'same line at u 29.3', FJ + '#outlet.end_chamfer', 0.05)
km('out_end_u', O['end_face']['u'], 'mm', 'median u of end-face faces', FJ + '#outlet.end_face', O['end_face']['scatter'])
km('out_bore_R', O['end_bore']['r'], 'mm', 'IRLS circle on end-bore vertices u 28.4..29.8', FJ + '#outlet.end_bore', O['end_bore']['rms'])
km('out_bore_floor_u', 0.5 * (BF['outlet']['u_p10'] + BF['outlet']['u_p90']), 'mm', BF['outlet']['method'] + ': minimax level = mid of p10..p90' + f" (p10 {BF['outlet']['u_p10']:.3f}, p90 {BF['outlet']['u_p90']:.3f})", FJ + '#bore_floors.outlet', 0.6,
   note='blind recess to the observed floor; the flow bore beyond is unscanned')
km('out_tube_u0', 5.0, 'mm', 'tube start inside the body cylinder (body_R 10.02 > tube reach): any value between the axis and the body wall gives the same solid', FJ + '#outlet', 0.0,
   note='construction value inside material; not a visible dimension')
# ---- barb (u along the barb axis from barb_axis_p)
tt = B['tube_taper']
km('barb_R0', tt['R'], 'mm', 'drafted-cone fit of the barb tube u 12.6..22.5 (beyond the cap rim), radius at u 17.5', FJ + '#barb.tube_taper', tt['rms'], crit=True, trig=TRIG)
km('barb_k', tt['k'], 'mm', 'same fit: d rho/d u (tube narrows outward)', FJ + '#barb.tube_taper', tt['rms'], note='unit mm/mm')
km('barb_rear_u', B['rear_face']['u'], 'mm', 'median u of the rear end face faces (normal < -0.9)', FJ + '#barb.rear_face', B['rear_face']['scatter'])
km('barb_rear_round_R', B['rear_round']['a'], 'mm', '(u,rho) circle fit to the rear end edge', FJ + '#barb.rear_round', B['rear_round']['rms'])
fl = B['flare']
km('barb_flare_slope', fl['slope'], 'mm', 'line fit rho(u) over u 23.6..24.7 (flare)', FJ + '#barb.flare', fl['rms'], note='unit mm/mm')
km('barb_flare_rho0', fl['rho_at_23p6'], 'mm', 'same line at u 23.6', FJ + '#barb.flare', fl['rms'])
bo = B['bulb_cone_offset']
km('bulb_offset', [bo['cx'], bo['cy']], 'mm', 'drafted-cone fit of the bulb u 25.1..27.9 with free centre (tilt fixed to the tube axis): centre offset in the barb local frame (e1 ~ datum up)', FJ + '#barb.bulb_cone_offset', bo['rms'])
km('bulb_R0', bo['R'], 'mm', 'same fit: radius at u 26.5', FJ + '#barb.bulb_cone_offset', bo['rms'], crit=True, trig=TRIG)
km('bulb_k', bo['k'], 'mm', f"same fit: d rho/d u (half-angle {-bo['draft_deg']:.2f} deg)", FJ + '#barb.bulb_cone_offset', bo['rms'], note='unit mm/mm')
km('barb_end_u', B['end_face']['u'], 'mm', 'median u of end-face faces', FJ + '#barb.end_face', B['end_face']['scatter'])
km('barb_bore_R', B['end_bore']['r'], 'mm', 'IRLS circle on end-bore vertices u 26.9..28.2', FJ + '#barb.end_bore', B['end_bore']['rms'])
km('barb_bore_floor_u', 0.5 * (BF['barb']['u_p10'] + BF['barb']['u_p90']), 'mm', BF['barb']['method'] + ': minimax level = mid of p10..p90' + f" (p10 {BF['barb']['u_p10']:.3f}, p90 {BF['barb']['u_p90']:.3f})", FJ + '#bore_floors.barb', 0.4,
   note='blind recess to the observed floor')
for nm_, k_ in (('noz_bore_floor_u', 'nozzle'), ('out_bore_floor_u', 'outlet'), ('barb_bore_floor_u', 'barb')):
    P[nm_]['measured'] = f"{BF[k_]['u_p10']:.4f}..{BF[k_]['u_p90']:.4f}"   # the measured spread of the bridge; value = its mid
doc = {"schema": "stl-re/params.json@1", "tool": "make_params.py (run-local, builder)", "tool_version": "stl-re-measure-intent/1.0",
       "inputs": {"measure/figures/fits.json": hashlib.sha256((RUN / FJ).read_bytes()).hexdigest(),
                  "intake/alignment.json": hashlib.sha256((RUN / 'intake/alignment.json').read_bytes()).hexdigest(),
                  "intake/aligned_work.stl": F['inputs']['intake/aligned_work.stl'],
                  "input/photos/photo_1.png": hashlib.sha256((RUN / 'input/photos/photo_1.png').read_bytes()).hexdigest(),
                  "input/photos/photo_2.png": hashlib.sha256((RUN / 'input/photos/photo_2.png').read_bytes()).hexdigest()},
       "seed": 0, "created": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
       "part": "OD-H21_antidrip-valve",
       "frame": "datum frame of intake/alignment.json: primary = band top face (z=0, +Z to the cap), origin = nozzle OD axis ∩ band top face, "
                "+X = side-outlet collar face normal; theta CCW about +Z from +X. Sub-part axes (nozzle, nut, bands, body, cap part, outlet, barb) "
                "are params in this frame; local angles say which local frame they use (e1 = datum X projected on the local plane, CCW about the local axis).",
       "scan_noise_mm": NOISE,
       "authority": "scan-only job (DECISIONS.md MEASUREMENTS): every dimension is scan authority; no caliper, no photo dimension",
       "params": P, "struck": [],
       "simplifications": [
          {"name": "outlet thread (pitch 0.908, E14)", "modelled_as": "plain cylinder at the mean thread radius out_thread_R",
           "deviation_cost": f"<= {(th_['p99'] - th_['mean']):.3f} / {(th_['mean'] - th_['p1']):.3f} mm (scan p99/p1 about the mean); scanner-smoothed profile only 0.37 mm peak-to-peak"},
          {"name": "O-ring (E13)", "modelled_as": "torus fused to the outlet (single-solid deliverable; invented connection of two real parts)",
           "deviation_cost": f"section fit rms {og['rms']:.3f}, max {og['max']:.3f} mm"},
          {"name": "nut->band transition", "modelled_as": "one straight chamfer (nut) + one straight segment (band) instead of the scanned curve",
           "deviation_cost": f"chamfer line rms {ch['rms']:.3f}, max {ch['max']:.3f} mm"},
          {"name": "nut ribs", "modelled_as": "8 vertical cylinders (rods) from the shoulder to nut_top_u, no draft",
           "deviation_cost": f"rod fit rms {min(r['rms'] for r in rb):.3f}..{max(r['rms'] for r in rb):.3f} mm"},
          {"name": "body cylinder out-of-round", "modelled_as": "circular cylinder body_R", "deviation_cost": f"rms {S['body']['rms']:.3f}, max {S['body']['max']:.3f} mm"},
          {"name": "barb flare", "modelled_as": "straight cone between the tube and the bulb cone", "deviation_cost": f"line rms {fl['rms']:.3f}, max {fl['max']:.3f} mm"},
          {"name": "ring-top speckle (E22)", "modelled_as": "not modelled", "deviation_cost": "< 0.3 mm"},
          {"name": "outlet-to-ring web (E25)", "modelled_as": "vertical-walled pentagon prism (half-width linear in x) from the tube to inside the ring; concave blends into tube and ring not modelled", "deviation_cost": f"half-width fit rms {WB['fit']['rms']:.3f}, max {WB['fit']['max']:.3f} mm"},
          {"name": "gap between ring skirt and body (E21)", "modelled_as": "closed ring bottom except the two scanned slits (sector pockets)", "deviation_cost": "scan dips 0.2..0.5 mm into the gap at the ring-bottom/body corner elsewhere"},
          {"name": "small edge rounds not listed (collar outer edge, end-face edges, body root at z=0)", "modelled_as": "sharp edges", "deviation_cost": "<= 0.15 mm (edge rounds <= ~0.3 mm radius read from the profile tables)"},
          {"name": "ring windows", "modelled_as": "rectangular radial pockets to the per-window observed floor", "deviation_cost": "window interior is unscanned beyond the floor; floor scatter p10..p50 up to 0.85 mm (window 112)"},
          {"name": "unscanned interior (E24) and bore depths (E02, E15, E20)", "modelled_as": "outer envelope + blind bores to the observed floor; no flow passages or valve internals",
           "deviation_cost": "none against the scan (not scanned); CAD is not a functional flow part"}],
       "checks": {
          "CHK-COUNT": {"ran": True, "result": "pass", "note": "nut ribs: FFT order 8 at 3 stations, residual local minimum (count_nut_ribs.json). Ring windows (4) are an irregular set (theta -66.75, -0.25, 112.0, 180.0): enumerated from envelope gaps, placed per instance, no rotational order claimed."},
          "CHK-ACHIEVABLE": {"ran": False, "result": "pass", "note": "no caliper or photo readings exist (scan-only); nothing to test"},
          "CHK-CLUSTER": {"ran": True, "result": "finding", "note": "on-axis material above the cap top (r<3, z 23.4..27.1) = barb tube crossing the axis (E19). Three coherent clusters were first found as builder self-check residuals (not by the intake enumeration) and are now measured and modelled: (1) the web joining the outlet tube top to the ring bottom (E25, z 8.0..9.0, x 10..13), (2) two slits under the ring skirt (E21, open loops L5/L7), (3) the lug cut-back on BOTH latch sides (E23 was declared a 0.25 mm recess; it is the bridged twin of the phi+90 latch window). CHK-ENUM addendum in intake/INTAKE_CARD.md."},
          "CHK-FRAME": {"ran": True, "result": "pass", "note": "all angles re-measured in the frozen datum frame or in named local frames; no intake angle copied (the intake clock 13.878 deg is the frame definition itself)"}},
       "open_questions": ["Is the 3.36 deg cap tilt and the 1.36 deg nozzle tilt a real assembly state (snap fit / insert play) or specimen damage? A nominal coaxial model is a different deliverable.",
                          "Owner to confirm scan_resolution=full and units mm (no calipers)."]}
(RUN / 'measure/params.json').write_text(json.dumps(doc, indent=1, ensure_ascii=False))
print(len(P), 'params')
