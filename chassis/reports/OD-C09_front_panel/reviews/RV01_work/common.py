"""RV01 reviewer helpers: load the exported part and place every reference solid by spec 1.1 section 2."""
import math, sys, json
from pathlib import Path
sys.path.insert(0, "/home/claude/oguz-atolye")
from OCP.gp import gp_Trsf, gp_Ax3, gp_Pnt, gp_Dir, gp_Vec, gp_Ax1
from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
from build123d import Solid, Compound, Box, Cylinder, Pos, Location, Plane, Vector
from tools.core import read_step, solids
from tools.core.shapes import occ, volume_mm3

JOB = Path("/root/oguz-jobs/20261002-od-c09-front-panel")
INP = JOB / "00_Spec/inputs"
WORK = JOB / "reviews/RV01_work"
PART_STEP = JOB / "02_STEP_STL/od_c09_front_C1_v01.step"
PART_STL = JOB / "02_STEP_STL/od_c09_front_C1_v01.stl"

def wrap(o):
    return Solid(o) if o.ShapeType().name.endswith("SOLID") else Compound(o)

def mapping(xmap, ymap, zmap, origin):
    """gp_Trsf sending local axes x,y,z to the given machine directions, local origin to origin."""
    t = gp_Trsf()
    # build matrix columns
    xm, ym, zm = xmap, ymap, zmap
    t.SetValues(xm[0], ym[0], zm[0], origin[0],
                xm[1], ym[1], zm[1], origin[1],
                xm[2], ym[2], zm[2], origin[2])
    return t

HOUSING = mapping((1, 0, 0), (0, 0, 1), (0, -1, 0), (0.0, 180.06, 32.0))
BOARD = mapping((0, -1, 0), (-1, 0, 0), (0, 0, -1), (-99.0, 140.0, 69.35))

def apply(shape, trsf):
    o = occ(shape)
    return wrap(BRepBuilderAPI_Transform(o, trsf, True).Shape())

def rot_about_axis(shape, phi_deg):
    """Rotate about the line x 0, z 32 along +Y; phi > 0 turns +Z toward +X (right hand about +Y)."""
    t = gp_Trsf()
    t.SetRotation(gp_Ax1(gp_Pnt(0, 0, 32.0), gp_Dir(0, 1, 0)), math.radians(phi_deg))
    return apply(shape, t)

def translate(shape, v):
    t = gp_Trsf(); t.SetTranslation(gp_Vec(*v)); return apply(shape, t)

def part():
    s = read_step(PART_STEP)
    ss = solids(s)
    return s, ss

def refs():
    out = {}
    c01 = read_step(INP / "OD-C01_base_frame.step"); out["C01"] = Solid(solids(c01)[0]) if len(solids(c01)) == 1 else c01
    c10 = read_step(INP / "OD-C10_top_panel.step"); out["C10"] = Solid(solids(c10)[0]) if len(solids(c10)) == 1 else c10
    c05 = read_step(INP / "OD-C05_group_head_carrier.step")
    out["C05"] = apply(Solid(solids(c05)[0]) if len(solids(c05)) == 1 else c05, HOUSING)
    g = read_step(INP / "od_g01_assembly_C1_v03.step")
    gs = [Solid(x) for x in solids(g)]
    h = read_step(INP / "od_g01_housing_C1_v03.step")
    hv = volume_mm3(h)
    placed = [apply(x, HOUSING) for x in gs]
    vols = [volume_mm3(x) for x in gs]
    ih = min(range(len(gs)), key=lambda i: abs(vols[i] - hv))
    rest = [i for i in range(len(gs)) if i != ih]
    ig10 = max(rest, key=lambda i: placed[i].bounding_box().max.Z)
    ig04 = [i for i in rest if i != ig10][0]
    out["HOUS"], out["G10"], out["G04"] = placed[ih], placed[ig10], placed[ig04]
    out["_ident"] = {"housing_vol": vols[ih], "housing_alone_vol": hv, "g10_vol": vols[ig10], "g04_vol": vols[ig04],
                     "g10_maxz": placed[ig10].bounding_box().max.Z, "n": len(gs)}
    e02 = read_step(INP / "OD-E02_control_board.step")
    es = solids(e02)
    out["E02"] = apply(Solid(es[0]) if len(es) == 1 else e02, BOARD)
    out["_ident"]["e02_solids"] = len(es)
    return out

def box(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)

def cyl_y(x, z, r, y0, y1):
    return Pos(x, (y0 + y1) / 2, z) * (Plane.XZ.location * Cylinder(r, y1 - y0))

def cyl_z(x, y, r, z0, z1):
    return Pos(x, y, (z0 + z1) / 2) * Cylinder(r, z1 - z0)

def R(r):
    if isinstance(r, dict):
        return {k: R(v) for k, v in r.items()}
    d = r.to_dict(); d.pop("params", None)
    return d

def dump(name, obj):
    (WORK / name).write_text(json.dumps(obj, indent=1, default=str))
