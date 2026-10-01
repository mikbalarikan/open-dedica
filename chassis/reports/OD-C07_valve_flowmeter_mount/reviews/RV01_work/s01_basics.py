import sys; sys.path.insert(0, "/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount/reviews/RV01_work")
from common import *
from tools.core import validity, compare_step, read_step, step_roundtrip
from tools.core.step import labels, node_labels, read_schema, read_length_unit
from tools.measure import envelope, feature_census, bore_census, mass_properties
raw = read_step(MOUNT)
print("solids in file", len(solids(raw)), "labels", labels(raw), node_labels(raw)[:5])
print("schema", read_schema(MOUNT), read_length_unit(MOUNT))
m = load_mount()
out = {}
v = validity(raw); print({k: (r.measured, r.status, r.reason) for k, r in v.items()})
e = envelope(m); print({k: round(r.measured, 6) for k, r in e.items()})
rt = step_roundtrip(raw, W / "roundtrip_mount.step", timestamp="2026-09-30T00:00:00")
print("roundtrip", {k: (r.measured, r.status) for k, r in rt.items()})
cs = compare_step(raw, MOUNT); print("compare to file", {k: (r.measured, r.status) for k, r in cs.items()})
fc = feature_census(m); print({k: r.measured for k, r in fc.items()})
bc = bore_census(m)
for b in bc.detail["bores"]:
    print(" bore d=%.4f axis=%s start=%s end=%s L=%.4f through=%s span=%s" % (b["diameter"], b["axis_dir"], b["start"], b["end"], b["length"], b.get("through"), b["span_deg"]))
print("concave arcs", bc.detail["concave_arcs"])
mp = mass_properties(m, 1270); print({k: round(r.measured, 4) for k, r in mp.items()})
dump("s01.json", {"validity": v, "envelope": e, "roundtrip": rt, "compare_file": cs, "census": fc, "bores": bc, "mass": mp})
# assembly
a = read_step(ASM)
print("assembly solids", len(solids(a)), "labels", node_labels(a))
for s in solids(a):
    S = Solid(s); bb = S.bounding_box(); print("  vol %.3f bb %s %s" % (S.volume, tuple(round(x,3) for x in bb.min), tuple(round(x,3) for x in bb.max)))
h22, h24, h22p, h24p = load_oem()
for nm, L in (("H22", h22p), ("H24", h24p)):
    for S in L:
        bb = S.bounding_box(); print(" mine", nm, "vol %.3f bb %s %s" % (S.volume, tuple(round(x,3) for x in bb.min), tuple(round(x,3) for x in bb.max)))
