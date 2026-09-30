import sys
sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c03-pump-cradle/reviews/RV01_work")
exec(open("/home/claude/oguz-jobs/20260930-od-c03-pump-cradle/reviews/RV01_work/controls.py").read().split("res = {}")[0])
from tools.core.shapes import solids, volume_mm3
from tools.measure import bore_census, clearance, envelope
m = M(part)["M02 foot grown to z 42.5"]
print(type(m), [volume_mm3(s) for s in solids(m)], {k:v.measured for k,v in envelope(m).items()})
b = bore_census(m); print([(x["diameter"], x["start"], x["end"]) for x in b.detail["bores"]])
print(clearance(m, pump).to_dict())
