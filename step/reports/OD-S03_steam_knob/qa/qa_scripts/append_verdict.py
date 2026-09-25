"""QA-own: append verdict reason, owner options and the it1-vs-it2 table to VERDICT.md (verdict.py does not
carry the reason, known defect). Numbers are read from qa/gate.json, qa/review.json and qa/it1_vs_it2.json."""
import json, hashlib
g = json.load(open('qa/gate.json')); rv = json.load(open('qa/review.json')); c = json.load(open('qa/it1_vs_it2.json'))
sha = hashlib.sha256(open('qa/gate.json', 'rb').read()).hexdigest()
L = ['', '## Verdict reason', '', rv['verdict_reason'], '',
     f"Gate identity for an ACCEPT-BAND entry: `qa/gate.json` sha256 `{sha[:12]}`, created `{g['created']}`. band_fails names: "
     + ', '.join(f"`{b.split(':')[0] if not b.startswith('zone:') else ':'.join(b.split(':')[:3])}`" for b in g['band_fails']) + '.', '',
     '## Options for the owner (BAND_NOT_MET)', '',
     '1. **Accept the band miss** and record it: a `DECISIONS.md` `ACCEPT-BAND` line whose evidence file lives outside the pipeline folders (e.g. `decisions/accept_band.md`), cites this gate (sha256 prefix or `created` above) and names the missed band(s) (`scan_to_cad`, `cad_to_scan_observable`, `zone`). Then `deliver/` may proceed with the limitations below.',
     '2. **Rescan** the chrome cap with matting spray (removes the hole-B flap, closes chrome holes) and re-run verify unchanged; expected to clear scan->CAD max / Z4 if the CAD is right, as the photos indicate.',
     '3. **Supply depth readings** (lever-pocket floor depth, bore depth; any caliper reading also clears L1/L2), rebuild those closures and re-verify.',
     '4. **Geometry loop 3 of 3** only for the crevice cluster (local groove deepening at theta ~300): removes cluster 1 but cannot clear the band (cluster 0 remains); not recommended alone.',
     '5. **HALT** if none of the above is wanted.', '',
     '## it1 vs it2 (CHK-LIKE4LIKE, same protocol; source qa/it1_vs_it2.json)', '',
     'Protocol: ' + json.dumps(c['protocol']), '',
     '| Item | it1 | it2 |', '|---|---|---|']
for i in ('it1', 'it2'): pass
v1, v2 = c['validity']['it1'], c['validity']['it2']
for f in v1:
    L.append(f"| {f} faces / volume / 0.005-0.05 watertight | {v1[f]['faces']} / {v1[f]['volume_mm3']} / {v1[f]['tess_watertight_0.005_0.05']} | {v2[f]['faces']} / {v2[f]['volume_mm3']} / {v2[f]['tess_watertight_0.005_0.05']} |")
r1, r2 = c['registration']['it1'], c['registration']['it2']
L.append(f"| ICP its / delta | {r1['iterations']} / {r1['delta_deg']:.3f} deg {r1['delta_mm']:.3f} mm | {r2['iterations']} / {r2['delta_deg']:.3f} deg {r2['delta_mm']:.3f} mm |")
a1, a2 = c['datum_audit']['it1'], c['datum_audit']['it2']
L.append(f"| datum audit angle / origin / pts p95 | {a1['angle_deg']:.3f} / {a1['origin_offset_mm']:.3f} / {a1['point_disagreement_p95_mm']:.3f} | {a2['angle_deg']:.3f} / {a2['origin_offset_mm']:.3f} / {a2['point_disagreement_p95_mm']:.3f} |")
for k, v in c['deviation'].items():
    L.append(f"| {k} p95 / max | {v['it1']['p95']:.3f} / {v['it1']['max']:.3f} | {v['it2']['p95']:.3f} / {v['it2']['max']:.3f} |")
L.append(f"| unobservable fraction | {c['unobservable_fraction']['it1']:.4f} | {c['unobservable_fraction']['it2']:.4f} |")
L.append(f"| mask-dependent passes | {'; '.join(c['mask_dependent_passes']['it1'])} | {'; '.join(c['mask_dependent_passes']['it2'])} |")
L += ['', 'Band fails it1 (from _it1_SUPERSEDED/qa/gate.json) vs it2: zone Z1 CAD->scan (max 0.893) no longer fails; the it1 VALIDITY geometry fail is cleared; the other three misses are unchanged (scan artefact / unobserved floors, not geometry).', '',
      '## Tessellation / watertightness probe (qa/tess_probe.json, both iterations, both frames)', '',
      '| iter | STEP | tol mm | ang rad | watertight | open | non-manifold |', '|---|---|---|---|---|---|---|']
for t in c['tessellation_probe']:
    L.append(f"| {t['iteration']} | {t['step'].split('/')[-1]} | {t['tolerance_mm']} | {t['angular_rad']} | {t['watertight']} | {t['open_edges']} | {t['nonmanifold_edges']} |")
L += ['', 'it1 defects located (datum frame): rib foot z 15.99 r 6.42 theta 175-182 at every setting; sleeve bottom z 32.31 r 5.36 theta 192.2 only at 0.1 rad (missed by the it1 single-setting probe). it2: none at any setting. B-rep: rib-foot curve-on-surface flag gone; 6 analyzer flags on ramps/shoulder present in both iterations, measured deviation <= 2.8e-6 mm (qa/brep_selfcheck.json, qa/cos_dev.json), report-only.', '']
open('qa/VERDICT.md', 'a').write('\n'.join(L))
