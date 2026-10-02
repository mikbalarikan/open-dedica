"""Spec section 2 poses, shared by the D1 plan measurements (no geometry is built here)."""
from pathlib import Path
from OCP.gp import gp_Trsf, gp_Ax3, gp_Pnt, gp_Dir
from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
from build123d import Shape, Solid, Compound
from tools.core import read_step, solids

WS = Path(__file__).resolve().parents[2]
INP = WS / "00_Spec" / "inputs"


def trsf(origin, x_to, z_to):
    """Map a source frame onto the machine frame: source +x goes to x_to, +z to z_to."""
    t = gp_Trsf()
    t.SetTransformation(gp_Ax3(gp_Pnt(*origin), gp_Dir(*z_to), gp_Dir(*x_to)), gp_Ax3())
    return t


# housing frame: x -> X, y -> +Z, z -> -Y, origin (0, 180.06, 32.0)
HOUSING = trsf((0.0, 180.06, 32.0), (1, 0, 0), (0, -1, 0))
# OD-E02 board frame: x -> -Y, y -> -X, z -> -Z, origin (-99.0, 140.0, 69.35)
BOARD = trsf((-99.0, 140.0, 69.35), (0, -1, 0), (0, 0, -1))


def place(shape, t):
    w = shape.wrapped if hasattr(shape, "wrapped") else shape
    return BRepBuilderAPI_Transform(w, t, True).Shape()


def load(name, t=None):
    s = read_step(INP / name)
    return s if t is None else place(s, t)
