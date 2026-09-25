"""QA-own: quantify the curve-on-surface deviation of every edge/face pair (ShapeAnalysis_Edge.CheckSameParameter)
vs the edge tolerance, it1 and it2 datum STEPs. Reports pairs whose deviation exceeds the edge tolerance."""
import json
from build123d import import_step
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_FACE, TopAbs_EDGE
from OCP.TopoDS import TopoDS
from OCP.ShapeAnalysis import ShapeAnalysis_Edge
from OCP.BRep import BRep_Tool
from OCP.BRepAdaptor import BRepAdaptor_Curve
out = {}
for f in ['_it1_SUPERSEDED/build/OD-S03_steam-knob_datum.step', 'build/OD-S03_steam-knob_datum.step']:
    s = import_step(f).wrapped; sae = ShapeAnalysis_Edge(); rows = []; worst = 0.0
    fe = TopExp_Explorer(s, TopAbs_FACE)
    while fe.More():
        face = TopoDS.Face(fe.Current()); ee = TopExp_Explorer(face, TopAbs_EDGE)
        while ee.More():
            e = TopoDS.Edge(ee.Current()); dev = [0.0]
            from OCP.BRepLib import BRepLib_ValidateEdge
            from OCP.BRepAdaptor import BRepAdaptor_Curve2d, BRepAdaptor_Surface
            from OCP.Adaptor3d import Adaptor3d_CurveOnSurface
            from OCP.Geom2dAdaptor import Geom2dAdaptor_Curve
            c3 = BRepAdaptor_Curve(e)
            c2 = BRepAdaptor_Curve2d(e, face); su = BRepAdaptor_Surface(face)
            cos = Adaptor3d_CurveOnSurface(c2, su)
            v = BRepLib_ValidateEdge(c3, cos, True); v.SetExitIfToleranceExceeded(1e9) if hasattr(v,'SetExitIfToleranceExceeded') else None
            v.Process(); d = v.GetMaxDistance() if v.IsDone() else float('nan')
            tol = BRep_Tool.Tolerance_s(e); worst = max(worst, d)
            if d > tol:
                p = c3.Value(0.5*(c3.FirstParameter()+c3.LastParameter()))
                rows.append({'dev_mm': round(d, 6), 'edge_tol_mm': tol, 'mid_xyz': [round(p.X(),3), round(p.Y(),3), round(p.Z(),3)]})
            ee.Next()
        fe.Next()
    out[f] = {'pairs_over_tol': rows, 'max_dev_mm': worst}
    print(f, 'max', worst, 'over-tol pairs', len(rows)); [print('  ', r) for r in rows]
json.dump(out, open('qa/cos_dev.json', 'w'), indent=1)
