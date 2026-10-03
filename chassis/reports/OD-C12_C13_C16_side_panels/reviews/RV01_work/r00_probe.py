import sys; sys.path.insert(0, "/root/oguz-jobs/20261002-od-c12-c13-c16-side-panels/reviews/RV01_work")
from common import *
from tools.core.step import labels
from tools.measure import envelope
for n in ("od_c13_right_C1_v01.step", "od_c12_left_C1_v01.step", "od_c16_bracket_C1_v01.step"):
    s = load(n); print(n, type(s).__name__, labels(s), len(solids(s)))
refs = references()
for k, v in refs.items():
    e = envelope(v); print(k, [round(e[f"{w}_{a}"].measured, 3) for w in ("min", "max") for a in "xyz"])
