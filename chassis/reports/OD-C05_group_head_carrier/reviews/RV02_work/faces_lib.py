"""Reviewer's own analytic downward-face listing and flat-ceiling (bridge) finder."""
import math, numpy as np
from tools.core.shapes import faces, edges, vertices, solids
from tools.measure.sampling import kind, outward_normal, Inside
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.BRep import BRep_Tool
from OCP.BRepTools import BRepTools
from OCP.GeomAbs import GeomAbs_Plane, GeomAbs_Cylinder
from OCP.TopAbs import TopAbs_REVERSED
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
from OCP.TopExp import TopExp
from OCP.TopTools import TopTools_IndexedDataMapOfShapeListOfShape
from OCP.TopAbs import TopAbs_EDGE, TopAbs_FACE
from OCP.BRepAdaptor import BRepAdaptor_Curve

B = np.array([0.0, 0.0, 1.0])

def vz(face):
    zs = [BRep_Tool.Pnt_s(v).Z() for v in vertices(face)]
    xs = [(BRep_Tool.Pnt_s(v).X(), BRep_Tool.Pnt_s(v).Y(), BRep_Tool.Pnt_s(v).Z()) for v in vertices(face)]
    return xs

def props(face):
    g = GProp_GProps(); BRepGProp.SurfaceProperties_s(face, g)
    c = g.CentreOfMass()
    return g.Mass(), (c.X(), c.Y(), c.Z())

def listing(shape, bed_z=None):
    """Per face: kind, least angle from horizontal of its downward normals (analytic)."""
    out = []
    for i, f in enumerate(faces(shape)):
        s = BRepAdaptor_Surface(f)
        area, c = props(f)
        u0, u1, v0, v1 = BRepTools.UVBounds_s(f)
        rec = {"i": i, "kind": kind(f), "area": area, "centre": c}
        if s.GetType() == GeomAbs_Plane:
            n = outward_normal(f, (u0+u1)/2, (v0+v1)/2)
            rec["normal"] = [float(x) for x in n]
            down = -float(n @ B)
            rec["down"] = down > 1e-9
            rec["angle"] = math.degrees(math.acos(min(1.0, down))) if down > 1e-9 else None
        elif s.GetType() == GeomAbs_Cylinder:
            ax = s.Cylinder().Axis().Direction()
            a = np.array([ax.X(), ax.Y(), ax.Z()])
            rec["axis"] = [float(x) for x in a]
            rec["radius"] = s.Cylinder().Radius()
            # normals of a cylinder are perpendicular to its axis: along Z axis -> horizontal
            if abs(abs(a @ B) - 1) < 1e-12:
                rec["down"] = False; rec["angle"] = None
            else:
                # sample u range densely incl. bounds
                best = None
                for u in np.linspace(u0, u1, 721):
                    n = outward_normal(f, u, (v0+v1)/2)
                    d = -float(n @ B)
                    if d > 1e-9:
                        ang = math.degrees(math.acos(min(1.0, d)))
                        best = ang if best is None else min(best, ang)
                rec["down"] = best is not None; rec["angle"] = best
        else:
            rec["down"] = None; rec["angle"] = None
        pts = vz(f)
        rec["zmin"] = min(p[2] for p in pts) if pts else None
        rec["zmax"] = max(p[2] for p in pts) if pts else None
        out.append(rec)
    return out

def flat_ceilings(shape, tol_deg=1.0):
    """Downward faces within tol_deg of horizontal (ceilings), with their extent."""
    L = listing(shape)
    return [r for r in L if r.get("down") and r.get("angle") is not None and r["angle"] < tol_deg]

def shared_edges(shape, fa, fb):
    m = TopTools_IndexedDataMapOfShapeListOfShape()
    TopExp.MapShapesAndAncestors_s(fa, TopAbs_EDGE, TopAbs_FACE, m)
    out = []
    for e in edges(fb):
        for e2 in edges(fa):
            if e.IsSame(e2):
                c = BRepAdaptor_Curve(e)
                p0 = c.Value(c.FirstParameter()); p1 = c.Value(c.LastParameter())
                out.append(((p0.X(), p0.Y(), p0.Z()), (p1.X(), p1.Y(), p1.Z())))
    return out
