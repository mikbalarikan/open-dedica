"""QA-own B-rep probe: BOPAlgo_ArgumentAnalyzer self-interference / small-edge / continuity checks and
BRepCheck on it1 and it2 datum/scan STEPs (a tessellation-independent view of the contact defect)."""
import json
from build123d import import_step
from OCP.BOPAlgo import BOPAlgo_ArgumentAnalyzer
from OCP.BRepCheck import BRepCheck_Analyzer
out = {}
for f in ['_it1_SUPERSEDED/build/OD-S03_steam-knob_datum.step', '_it1_SUPERSEDED/build/OD-S03_steam-knob.step',
          'build/OD-S03_steam-knob_datum.step', 'build/OD-S03_steam-knob.step']:
    s = import_step(f).wrapped
    a = BOPAlgo_ArgumentAnalyzer(); a.SetShape1(s)
    for mname in ("ArgumentTypeMode","SelfInterMode","SmallEdgeMode","RebuildFaceMode","TangentMode","MergeVertexMode","MergeEdgeMode","ContinuityMode","CurveOnSurfaceMode"):
        setattr(a, mname, True)
    a.Perform()
    res = []
    from OCP.BRepGProp import BRepGProp
    from OCP.GProp import GProp_GProps
    from OCP.Bnd import Bnd_Box
    from OCP.BRepBndLib import BRepBndLib
    for cr in a.GetCheckResult():
        st = str(cr.GetCheckStatus()).split('.')[-1]
        locs = []
        for sh in cr.GetFaultyShapes1():
            b = Bnd_Box(); BRepBndLib.Add_s(sh, b); p0, p1 = b.CornerMin(), b.CornerMax(); x0,y0,z0,x1,y1,z1 = p0.X(),p0.Y(),p0.Z(),p1.X(),p1.Y(),p1.Z()
            locs.append({'type': str(sh.ShapeType()).split('.')[-1], 'bbox': [round(v,3) for v in (x0,y0,z0,x1,y1,z1)]})
        res.append({'status': st, 'shapes': locs, 'max_dist': cr.GetMaxDistance1()})
    out[f] = {'faulty': res, 'brepcheck_valid': bool(BRepCheck_Analyzer(s).IsValid()), 'argument_analyzer_has_faulty': bool(a.HasFaulty()),
              'n_faulty': int(a.GetCheckResult().Size())}
    print(f, out[f], flush=True)
json.dump(out, open('qa/brep_selfcheck.json', 'w'), indent=1)
