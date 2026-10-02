"""D1: measure the reference solids in the housing frame (diagnostic, not a gate check)."""
from pathlib import Path
import sys
from tools.core import read_step, validity
from tools.measure import envelope, bore_census
from build123d import Compound, Solid

WS = Path(__file__).resolve().parent.parent
INP = WS / "00_Spec" / "inputs"

def env(s):
    r = envelope(s)
    return {k: round(v.measured, 3) if hasattr(v, "measured") and v.measured is not None else v for k, v in r.items()} if isinstance(r, dict) else r

def solids(shape):
    return list(shape.solids())

h = read_step(INP / "od_g01_housing_C1_v03.step")
print("housing solids", len(solids(h)))
print("housing envelope", env(h))
v = validity(h)
print("housing validity", {k: (x.measured, x.status) for k, x in v.items()} if isinstance(v, dict) else v)
bc = bore_census(h)
print("housing bores:")
try:
    for b in bc.detail["bores"]:
        print("  ", b)
except Exception as e:
    print("bore census raw", bc, e)

a = read_step(INP / "od_g01_assembly_C1_v03.step")
for i, s in enumerate(solids(a)):
    print("asm solid", i, "vol", round(s.volume, 1), "valid", s.is_valid, env(s))
