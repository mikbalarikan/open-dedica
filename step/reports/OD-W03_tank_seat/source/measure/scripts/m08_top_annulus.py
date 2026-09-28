"""m08_top_annulus.py - slope of the cup top annulus z(r) (binned medians, r 8.4..10.1) and of the boss top
(r 2.6..5.2). Added after the builder self-check showed a systematic ring on the flat cup top (it1 attempt 2).
Writes measure/figures/m08_top_annulus.json."""
import json, math, numpy as np
out = {"tool": "measure/scripts/m08_top_annulus.py"}
for nm, rr, zr in (('cupA', (8.4, 10.1), (11.8, 12.7)), ('cupB', (8.4, 10.1), (11.8, 12.7)), ('boss', (2.6, 5.2), (11.8, 12.9))):
    d = np.load(f'measure/figures/m02_profile_{nm}.npz'); r, z = d['r'], d['z']
    k = (r > rr[0]) & (r < rr[1]) & (z > zr[0]) & (z < zr[1])
    rb, zb = [], []
    for b in np.arange(rr[0], rr[1], 0.2):
        kk = k & (r >= b) & (r < b + 0.2)
        if kk.sum() > 20: rb.append(b + 0.1); zb.append(float(np.median(z[kk])))
    rb, zb = np.array(rb), np.array(zb)
    A = np.c_[np.ones(len(rb)), rb]; c, *_ = np.linalg.lstsq(A, zb, rcond=None)
    out[nm] = {"z0": float(c[0]), "dz_dr": float(c[1]), "slope_deg": float(math.degrees(math.atan(-c[1]))),
               "bins": len(rb), "rms_of_medians": float(np.sqrt(((zb - A @ c) ** 2).mean())),
               "z_at_r_lo": float(c[0] + c[1] * rr[0]), "z_at_r_hi": float(c[0] + c[1] * rr[1])}
json.dump(out, open('measure/figures/m08_top_annulus.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
