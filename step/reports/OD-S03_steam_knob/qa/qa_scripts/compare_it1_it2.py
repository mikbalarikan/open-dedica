"""QA-own CHK-LIKE4LIKE table: it1 (_it1_SUPERSEDED/qa) vs it2 (qa), same regime/masks/zones/ICP/sampling."""
import json, hashlib
def L(p): return json.load(open(p))
def h(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
A, B = '_it1_SUPERSEDED/qa/', 'qa/'
same = {f: h(A + f) == h(B + f) for f in ['regime.json', 'masks.json', 'zones.json', 'icp_scan_masks.json', 'datum_spec.json']}
da, db = L(A + 'deviation.json'), L(B + 'deviation.json')
ra, rb = L(A + 'registration.json'), L(B + 'registration.json')
pa = {k: v for k, v in da['observability']['params'].items() if k != 'helper_switched_for_n_points'}
pb = {k: v for k, v in db['observability']['params'].items() if k != 'helper_switched_for_n_points'}
proto = {'inputs_identical': same, 'sampling_identical': da['sampling'] == db['sampling'],
         'icp_params_identical': ra['params'] == rb['params'], 'observability_params_identical': pa == pb,
         'label': [da['label'], db['label']]}
def s(x): return {k: round(x[k], 4) for k in ('n', 'rms', 'p50', 'p95', 'p99', 'max')}
rows = {}
for k in ['scan_to_cad', 'cad_to_scan', 'cad_to_scan_masked', 'cad_to_scan_observable']:
    rows[k] = {'it1': s(da[k]), 'it2': s(db[k])}
for z in db['zones']:
    for d in ('scan_to_cad', 'cad_to_scan'):
        za = da['zones'][z][d]['masked'] if isinstance(da['zones'][z][d], dict) and 'masked' in da['zones'][z][d] else None
        zb = db['zones'][z][d]['masked'] if isinstance(db['zones'][z][d], dict) and 'masked' in db['zones'][z][d] else None
        if za and zb: rows[f'zone {z} {d} (masked)'] = {'it1': s(za), 'it2': s(zb)}
reg = {'it1': {k: ra[k] for k in ('iterations', 'converged', 'delta_deg', 'delta_mm', 'final_kept_fraction')},
       'it2': {k: rb[k] for k in ('iterations', 'converged', 'delta_deg', 'delta_mm', 'final_kept_fraction')}}
dda, ddb = L(A + 'datum_audit.json'), L(B + 'datum_audit.json')
aud = {i: {k: d[k] for k in ('angle_deg', 'axis_angle_deg', 'origin_offset_mm', 'point_disagreement_p95_mm')} for i, d in (('it1', dda), ('it2', ddb))}
sca, scb = L(A + 'step_check.json'), L(B + 'step_check.json')
val = {i: {f.split('/')[-1]: {'faces': v['validity']['counts']['face'], 'volume_mm3': round(v['validity']['volume_mm3'], 3),
                               'brepcheck_valid': v['validity']['brepcheck_valid'], 'tess_watertight_0.005_0.05': v['tessellation']['watertight']}
           for f, v in d['steps'].items()} for i, d in (('it1', sca), ('it2', scb))}
tp = L(B + 'tess_probe.json')
tess = [{k: r[k] for k in ('iteration', 'step', 'tolerance_mm', 'angular_rad', 'watertight', 'open_edges', 'nonmanifold_edges')} for r in tp['results']]
clus = {i: [{k: c[k] for k in ('n', 'r_range', 'theta_deg_range', 'd_max')} for c in d['over_band_clusters']['scan_to_cad']['clusters']] for i, d in (('it1', da), ('it2', db))}
out = {'schema': 'stl-re/it_compare@1', 'tool': 'qa_scripts/compare_it1_it2.py (QA-own)', 'seed': None,
       'inputs': {p: h(p) for p in [A + 'deviation.json', B + 'deviation.json', A + 'registration.json', B + 'registration.json', B + 'tess_probe.json']},
       'protocol': proto, 'registration': reg, 'datum_audit': aud, 'validity': val, 'tessellation_probe': tess,
       'deviation': rows, 'scan_to_cad_clusters': clus,
       'mask_dependent_passes': {'it1': da['mask_dependent_passes'], 'it2': db['mask_dependent_passes']},
       'unobservable_fraction': {'it1': da['unobservable_fraction'], 'it2': db['unobservable_fraction']}}
json.dump(out, open('qa/it1_vs_it2.json', 'w'), indent=1)
print(json.dumps(proto)); print(json.dumps(reg)); print(json.dumps(val))
for k, v in rows.items(): print(f"{k:60s} it1 p95 {v['it1']['p95']:.3f} max {v['it1']['max']:.3f} | it2 p95 {v['it2']['p95']:.3f} max {v['it2']['max']:.3f}")
