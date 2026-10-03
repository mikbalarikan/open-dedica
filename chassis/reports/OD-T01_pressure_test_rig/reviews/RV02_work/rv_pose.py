"""RV02 pose helper: the housing set placed by spec 2 from od_g01_assembly_C1_v03.step,
solids identified by measurement (reviewer's own code)."""
from pathlib import Path
import numpy as np
from build123d import Solid, Location, Pos, Rot, Box, Cylinder
from tools.core import step as st
from tools.measure import envelope, bore_census
W = Path("/root/oguz-jobs/20261002-od-t01-pressure-test-rig")
RIG = W / "02_STEP_STL/od_t01_rig_C1_v02.step"
ASM = W / "00_Spec/inputs/od_g01_assembly_C1_v03.step"

def load_rig():
    return Solid(st.read_step(RIG).solids()[0].wrapped)

def identify():
    a = st.read_step(ASM)
    sols = [Solid(s.wrapped) for s in a.solids()]
    info = []
    for i, s in enumerate(sols):
        e = {k: v.measured for k, v in envelope(s).items()}
        info.append((i, e, s.volume))
    housing = g10 = g04 = None
    for i, e, v in info:
        big = max(e["size_x"], e["size_y"], e["size_z"])
        if big > 120:
            g10 = i
        elif abs(e["size_x"] - 100) < 0.01 and abs(e["size_y"] - 100) < 0.01:
            bc = bore_census(sols[i])
            four = [b for b in bc.detail["bores"] if abs(b["diameter"] - 4.0) < 0.01
                    and abs(abs(b["start"][0]) - 44) < 0.01 and abs(abs(b["start"][1]) - 44) < 0.01]
            if len(four) == 4:
                housing = i
    g04 = [i for i, _, _ in info if i not in (housing, g10)]
    assert housing is not None and g10 is not None and len(g04) == 1, info
    return sols[housing], sols[g04[0]], sols[g10], info, (housing, g04[0], g10)

# spec 2: housing x -> X, y -> +Z, z -> -Y, origin (0, 110.06, 0): +90 deg about X
POSE = Location((0, 110.06, 0)) * Location((0, 0, 0), (1, 0, 0), 90)

def check_pose_axes():
    m = np.array(POSE.wrapped.Transformation().VectorialPart().Row(1).Coord())  # unused
    t = POSE.wrapped.Transformation()
    out = {}
    for name, v in (("x", (1, 0, 0)), ("y", (0, 1, 0)), ("z", (0, 0, 1))):
        from OCP.gp import gp_Dir
        d = gp_Dir(*v).Transformed(t)
        out[name] = (round(d.X(), 9), round(d.Y(), 9), round(d.Z(), 9))
    return out

def place(shape, phi=0.0, dy=0.0, dz=0.0, dx=0.0):
    """posed in the rig frame, then rotated by phi about rig +Y through x 0, z 0, then moved."""
    return Location((dx, dy, dz)) * Location((0, 0, 0), (0, 1, 0), phi) * POSE * shape
