"""make_params_it2.py - it2 (REVISE, route geometry, gate dd052135f7c2): overlay the re-measured latch windows,
ring windows and skirt slits (measure/figures/fits_it2.json) onto measure/params.json. Every other row is
left untouched. The it1 rows stay in _it1_SUPERSEDED/measure/params.json; each changed row carries an
'it1 -> it2' note."""
from __future__ import annotations
import datetime, hashlib, json
from pathlib import Path
RUN = Path(__file__).resolve().parents[3]
PJ = RUN / 'measure/params.json'
doc = json.loads(PJ.read_text()); P = doc['params']
OLD = json.loads((RUN / '_it1_SUPERSEDED/measure/params.json').read_text())['params']
F2 = json.loads((RUN / 'measure/figures/fits_it2.json').read_text())
FJ = 'measure/figures/fits_it2.json'
R4 = lambda x: [round(float(v), 4) for v in x] if isinstance(x, (list, tuple)) else round(float(x), 4)
TAG = 'it2 REVISE (gate dd052135f7c2, finding {n})'

def km(name, val, unit, est, ev, unc, n, frame=None, note=''):
    v = R4(val); old = OLD.get(name, {}).get('value')
    row = dict(value=v, unit=unit, measured=v, rule='keep-measured', source='scan', estimator=est, uncertainty_mm=unc,
               evidence=ev, critical=False, note=(f"{TAG.format(n=n)}: it1 {old!r} -> it2 {v!r}. " if old is not None else f"{TAG.format(n=n)}: new param. ") + note)
    if frame: row['frame'] = frame
    P[name] = row

removed = []
def drop(name):
    if name in P:
        P.pop(name); removed.append(name)

# 1. latch windows (nozzle local frame; side order [phi+90, phi-90])
L = F2['latch_windows']; FRN = 'nozzle local frame; x\' along the lug b-side normal (phi+90 / phi-90), y\' CCW'
km('latch_cut_d', [x['cut_plane_d'] for x in L], 'mm', L[0]['method'], FJ + '#latch_windows', 0.1, 1, FRN,
   'the lug cut-back floor is a plane parallel to the b-side flat (it1 modelled a cylindrical floor at the nozzle radius, which cut 0.84 too deep near the phi-90 corners)')
km('latch_cut_y0', [x['cut_half_width'][0] for x in L], 'mm', "lateral extent y' = d tan(first cut bin edge)", FJ + '#latch_windows', 0.2, 1, FRN)
km('latch_cut_y1', [x['cut_half_width'][1] for x in L], 'mm', "lateral extent y' = d tan(last cut bin edge)", FJ + '#latch_windows', 0.2, 1, FRN)
T = L[0]
km('latch_through_theta', T['through_theta'], 'deg', T['through_method'], FJ + '#latch_windows', 1.0, 1, 'nozzle local frame, CCW about the nozzle axis',
   f"through-window into the bore on the phi+90 side (scanned bridge p10/p50 r {T['bridge_rho_p10_p50'][0]:.2f}/{T['bridge_rho_p10_p50'][1]:.2f}); it1 cut only to r 4.79 over 90..114")
for n_ in ('latch_theta0_deg', 'latch_theta1_deg', 'latch_floor_rho', 'latch_deep_theta', 'latch_deep_floor_rho'):
    drop(n_)
# 2. ring windows (cap local frame)
W = F2['ring_windows']; FRC = 'cap local frame (e1 = datum X projected), CCW'
km('win_theta0_deg', [w['theta0'] for w in W], 'deg', W[0]['method'], FJ + '#ring_windows', 1.0, 2, FRC)
km('win_theta1_deg', [w['theta1'] for w in W], 'deg', 'same map: last open column + 1 deg', FJ + '#ring_windows', 1.0, 2, FRC)
km('win_u_lo', [w['u_lo'] for w in W], 'mm', 'same map: first row open in >= 50 % of the window columns', FJ + '#ring_windows', 0.2, 2)
km('win_u_hi', [w['u_hi'] for w in W], 'mm', 'same map: last open row + 0.2', FJ + '#ring_windows', 0.2, 2)
km('win_floor_rho', [w['floor_rho'] for w in W], 'mm', W[0]['floor_rule'], FJ + '#ring_windows', 0.4, 2)
D = [w for w in W if 'deep_theta' in w]
assert len(D) == 1, 'expected one window opening into the skirt/body gap'
km('win_deep_theta', D[0]['deep_theta'], 'deg', 'bounding box of window cells whose minimum radius is < 11.0 (opening into the skirt/body gap)', FJ + '#ring_windows', 1.0, 2, FRC,
   f"window centred near {0.5 * (D[0]['deep_theta'][0] + D[0]['deep_theta'][1]):.0f} deg only")
km('win_deep_u', D[0]['deep_u'], 'mm', 'same cells: axial extent', FJ + '#ring_windows', 0.2, 2)
km('win_deep_floor_rho', D[0]['deep_floor_rho'], 'mm', 'same cells: p10 of the minimum radius (the scanned membrane in the gap)', FJ + '#ring_windows', 0.3, 2)
drop('win_theta_deg'); drop('win_width_deg')
# 3. skirt slits (cap local frame), from the open-boundary loops
S = F2['skirt_slits']
km('slit_theta0_deg', [s['ceiling_theta0'] for s in S], 'deg', S[0]['ceiling_method'] + ': first bin', FJ + '#skirt_slits', 1.0, 3, FRC,
   'the open loops L5/L7 (theta ' + ', '.join(f"{s['theta0']:.1f}..{s['theta1']:.1f}" for s in S) + ') mark only the hole in the scanned slit surface; the scanned slit ceiling spans the value given')
km('slit_theta1_deg', [s['ceiling_theta1'] for s in S], 'deg', 'same bins: last bin + 1 deg', FJ + '#skirt_slits', 1.0, 3, FRC)
km('slit_u_top', [s['ceiling_u'] for s in S], 'mm', 'same bins: median of the per-bin highest vertex (slit ceiling)', FJ + '#skirt_slits', 0.1, 3)
km('slit_rho_in', [s['ceiling_rho_p2_p95'][0] for s in S], 'mm', 'p2 radius of the vertices above ring_bottom_u + 0.9 in the slit span', FJ + '#skirt_slits', 0.1, 3)
km('slit_rho_out', [s['ceiling_rho_p2_p95'][1] for s in S], 'mm', 'p95 radius of the same vertices', FJ + '#skirt_slits', 0.1, 3)

doc['inputs']['measure/figures/fits_it2.json'] = hashlib.sha256((RUN / FJ).read_bytes()).hexdigest()
doc['created'] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
doc['tool'] = 'make_params.py (it1) + make_params_it2.py (it2 overlay, run-local, builder)'
doc['revisions'] = [r_ for r_ in doc.get('revisions', []) if r_.get('iteration') != 2] + [dict({"iteration": 2, "route": "geometry", "gate": "dd052135f7c2",
    "changed": sorted(k for k in P if 'it2 REVISE' in P[k].get('note', '')), "removed": sorted(set(OLD) - set(P)),
    "why": "verifier findings: latch window under-cut (+ phi-90 cut-back too deep), ring windows over-cut / wrong depth, skirt slits over-cut"})]
for s_ in doc['simplifications']:
    if s_['name'] == 'ring windows':
        s_['modelled_as'] = 'annular-sector pockets (radial walls) over the measured open theta/u span to the median shallow floor; the window near 110 deg also gets a deeper sector to the membrane seen in the skirt/body gap'
        s_['deviation_cost'] = 'window floors are sloped (latch-hook ramps): per-cell minimum radius spreads about 11..12.9 around the median floor; window corners are rounded, not rectangular'
PJ.write_text(json.dumps(doc, indent=1, ensure_ascii=False))
print('changed', doc['revisions'][-1]['changed']); print('removed', removed)
