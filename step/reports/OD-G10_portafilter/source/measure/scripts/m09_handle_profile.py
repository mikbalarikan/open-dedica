"""Handle meridian details about the fitted handle axis (handle_axis.json): outer envelope r(t)
(p99 of radial distance per 0.1 mm t-bin, upper half only so the open channel does not bias it),
then line fits on the collar flanks, the end chamfer and the end face position."""
import json, numpy as np, trimesh
A = json.load(open('measure/figures/handle_axis.json')); p0 = np.array(A['axis_point_x0']); d = np.array(A['axis_dir'])
m = trimesh.load('intake/aligned_work.stl'); P, _ = trimesh.sample.sample_surface(m, 3000000, seed=0)
q = P - p0; t = q @ d; perp = q - np.outer(t, d); rad = np.linalg.norm(perp, axis=1)
upper = perp[:, 2] > 0
def env(lo, hi, step=0.1):
    e = []
    for a in np.arange(lo, hi, step):
        s = upper & (t >= a) & (t < a + step) & (rad < 17)
        if s.sum() > 15: e.append([float(a + step / 2), float(np.percentile(rad[s], 99))])
    return np.array(e)
E1 = env(41.0, 51.0); E2 = env(150.0, 167.0)
def lfit(E, lo, hi):
    s = (E[:, 0] >= lo) & (E[:, 0] <= hi); b, a = np.polyfit(E[s, 0], E[s, 1], 1); res = E[s, 1] - (a + b * E[s, 0])
    return {"t_range": [lo, hi], "r = a + b t": [float(a), float(b)], "rms": float(np.sqrt((res**2).mean()))}
out = {"envelope_collar": E1.tolist(), "envelope_end": E2.tolist()}
out["neck_cone"] = lfit(E1, 41.2, 44.2)
out["collar_front_flank"] = lfit(E1, 45.0, 47.4)
out["collar_peak_r"] = float(E1[(E1[:, 0] > 47) & (E1[:, 0] < 49), 1].max())
out["collar_peak_t"] = float(E1[(E1[:, 0] > 47) & (E1[:, 0] < 49)][np.argmax(E1[(E1[:, 0] > 47) & (E1[:, 0] < 49), 1]), 0])
back = E1[(E1[:, 0] > out["collar_peak_t"]) & (E1[:, 1] < 13.6)]
out["collar_back_t"] = float(back[0, 0]) if len(back) else None
out["collar_step_t"] = float(E1[(E1[:, 0] > 44) & (E1[:, 0] < 45.5)][np.argmax(np.diff(E1[(E1[:, 0] > 44) & (E1[:, 0] < 45.5), 1])), 0])
out["end_chamfer"] = lfit(E2, 160.2, 164.3)
s = (np.abs(perp[:, 2]) < 8) & (t > 164) & (rad < 10); out["end_face_t"] = float(np.median(t[s & (t > np.percentile(t[s], 50))]))
out["cap_joint_groove_t"] = float(E2[(E2[:, 0] > 156) & (E2[:, 0] < 160)][np.argmin(E2[(E2[:, 0] > 156) & (E2[:, 0] < 160), 1]), 0])
out["chamfer_start_t"] = float(E2[(E2[:, 0] > 158) & (E2[:, 0] < 161)][np.argmax(E2[(E2[:, 0] > 158) & (E2[:, 0] < 161), 1]), 0])
json.dump(out, open('measure/figures/handle_profile.json', 'w'), indent=1)
print(json.dumps({k: v for k, v in out.items() if not k.startswith('envelope')}, indent=1))
for row in E1[::5]: print('collar', np.round(row, 3))
for row in E2[60::6]: print('end', np.round(row, 3))
