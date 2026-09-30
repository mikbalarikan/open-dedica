"""Reviewer helpers for RV01: analytic downward angle per face, plane sections, and
section edge reading. Written by the reviewer; reads only the exported B-rep."""
import math
import numpy as np
from OCP.BRepAdaptor import BRepAdaptor_Surface, BRepAdaptor_Curve
from OCP.BRepTools import BRepTools
from OCP.GeomAbs import GeomAbs_Plane, GeomAbs_Cylinder, GeomAbs_Line, GeomAbs_Circle
from OCP.TopAbs import TopAbs_REVERSED
from OCP.BRepAlgoAPI import BRepAlgoAPI_Section, BRepAlgoAPI_Common
from OCP.gp import gp_Pln, gp_Pnt, gp_Dir
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeFace
from OCP.BRepGProp import BRepGProp
from OCP.GProp import GProp_GProps
from tools.core.shapes import faces, edges, occ

UP = np.array([0.0, 1.0, 0.0])

def v(p): return np.array([p.X(), p.Y(), p.Z()], float)

def face_normal_at(face, u, w):
    s = BRepAdaptor_Surface(face)
    p = s.Value(u, w)
    from OCP.gp import gp_Vec, gp_Pnt as P
    d1u, d1v = gp_Vec(), gp_Vec(); pp = P()
    s.D1(u, w, pp, d1u, d1v)
    n = np.cross(v(d1u), v(d1v)); n /= np.linalg.norm(n)
    if face.Orientation() == TopAbs_REVERSED: n = -n
    return v(p), n

def angle_from_horizontal(n, b=UP):
    """acos(-n.b) in degrees: 0 for a ceiling, 90 for a vertical wall (the tool's definition)."""
    c = float(np.clip(-np.dot(n, b), -1, 1))
    return math.degrees(math.acos(c))

def downward_faces(shape, b=UP, down_eps=1e-9):
    """Every face with a downward-facing point, and its exact least angle from horizontal:
    planes read their one normal; cylinders read the analytic extremum of -n.b over the
    face's u interval (endpoints plus the interior critical point where n is most downward)."""
    rows = []
    for i, f in enumerate(faces(shape)):
        s = BRepAdaptor_Surface(f)
        u0, u1, w0, w1 = BRepTools.UVBounds_s(f)
        t = s.GetType()
        if t == GeomAbs_Plane:
            p, n = face_normal_at(f, (u0 + u1) / 2, (w0 + w1) / 2)
            if -np.dot(n, b) > down_eps:
                rows.append(dict(face=i, kind="plane", least_deg=angle_from_horizontal(n, b), at=p.tolist(),
                                 normal=n.tolist()))
        elif t == GeomAbs_Cylinder:
            cyl = s.Cylinder(); ax = v(cyl.Axis().Direction()); loc = v(cyl.Axis().Location()); r = cyl.Radius()
            wm = (w0 + w1) / 2
            us = list(np.linspace(u0, u1, 721))
            # interior critical point: the u where n is most downward, found by golden refinement
            vals = [(-np.dot(face_normal_at(f, u, wm)[1], b), u) for u in us]
            best = max(vals)
            if best[0] <= down_eps:
                continue
            k = us.index(best[1]); lo = us[max(k - 1, 0)]; hi = us[min(k + 1, len(us) - 1)]
            g = (math.sqrt(5) - 1) / 2
            for _ in range(200):
                a = hi - g * (hi - lo); c = lo + g * (hi - lo)
                if -np.dot(face_normal_at(f, a, wm)[1], b) > -np.dot(face_normal_at(f, c, wm)[1], b): hi = c
                else: lo = a
            um = (lo + hi) / 2
            cands = [(u0, "u_min edge"), (u1, "u_max edge"), (um, "interior")]
            worst = None
            for u, where in cands:
                p, n = face_normal_at(f, u, wm)
                a = angle_from_horizontal(n, b)
                if worst is None or a < worst[0]: worst = (a, p, where)
            rows.append(dict(face=i, kind="cylinder", radius=r, axis_dir=ax.tolist(),
                             axis_loc=loc.tolist(), u_range=[u0, u1], least_deg=worst[0],
                             at=worst[1].tolist(), where=worst[2],
                             axis_perp_build_deg=math.degrees(math.acos(abs(float(np.dot(ax, b)))))))
        else:
            rows.append(dict(face=i, kind=f"other {t}", least_deg=None))
    return rows

def section_edges(shape, origin, normal):
    sec = BRepAlgoAPI_Section(occ(shape), gp_Pln(gp_Pnt(*origin), gp_Dir(*normal)))
    sec.Build()
    out = []
    for e in edges(sec.Shape()):
        c = BRepAdaptor_Curve(e)
        a, b_ = c.FirstParameter(), c.LastParameter()
        p0, p1 = v(c.Value(a)), v(c.Value(b_))
        t = c.GetType()
        row = dict(p0=p0.tolist(), p1=p1.tolist())
        if t == GeomAbs_Line:
            d = p1 - p0; row.update(kind="line", length=float(np.linalg.norm(d)))
        elif t == GeomAbs_Circle:
            ci = c.Circle(); row.update(kind="circle", radius=ci.Radius(), centre=v(ci.Location()).tolist(),
                                        first=a, last=b_)
            from OCP.gp import gp_Vec, gp_Pnt as P
            for key, par in (("t0", a), ("t1", b_)):
                pp, dv = P(), gp_Vec(); c.D1(par, pp, dv); row[key] = (v(dv) / dv.Magnitude()).tolist()
        else:
            row.update(kind=str(t))
        out.append(row)
    return out

def section_area(shape, origin, normal, size=1000.0):
    """Area of the solid's cut by the plane (common of the solid with a big planar face)."""
    face = BRepBuilderAPI_MakeFace(gp_Pln(gp_Pnt(*origin), gp_Dir(*normal)), -size, size, -size, size).Face()
    com = BRepAlgoAPI_Common(occ(shape), face); com.Build()
    g = GProp_GProps(); BRepGProp.SurfaceProperties_s(com.Shape(), g)
    return float(g.Mass()), com.Shape()
