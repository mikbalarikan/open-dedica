"""Reviewer RV01 common loaders (own code; no designer script read)."""
import json, math, sys
from pathlib import Path
import numpy as np
from build123d import Location, Solid, Compound, Box, Cylinder, Pos, Rot
from tools.core import read_step
from tools.core.shapes import solids, faces, occ, volume_mm3

JOB = Path("/root/oguz-jobs/20260930-od-c07-valve-flowmeter-mount")
W = JOB / "reviews/RV01_work"
MOUNT = JOB / "02_STEP_STL/od_c07_mount_C1_v01.step"
ASM = JOB / "02_STEP_STL/od_c07_assembly_C1_v01.step"
STL = JOB / "02_STEP_STL/od_c07_mount_C1_v01.stl"
H22 = JOB / "00_Spec/inputs/OD-H22_3way_valve.step"
H24 = JOB / "00_Spec/inputs/OD-H24_flowmeter.step"
BAND_MM, BAND_DEG, BAND_MM3 = 0.005, 0.001, 0.001

def one_solid(shape):
    s = solids(shape)
    assert len(s) == 1, len(s)
    return Solid(s[0])

def load_mount():
    return one_solid(read_step(MOUNT))

def load_oem():
    """OEM solids placed by the spec §2 joints (pure translations)."""
    h22 = [Solid(s) for s in solids(read_step(H22))]
    h24 = [Solid(s) for s in solids(read_step(H24))]
    h22p = [s.moved(Location((62.0, 0, 48.0))) for s in h22]
    h24p = [s.moved(Location((0, 0, 10.0))) for s in h24]
    return h22, h24, h22p, h24p

def comp(lst):
    return Compound(children=list(lst)) if len(lst) > 1 else lst[0]

def dump(name, obj):
    (W / name).write_text(json.dumps(obj, indent=1, default=lambda o: o.to_dict() if hasattr(o, "to_dict") else str(o)))
