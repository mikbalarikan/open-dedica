"""Re-export the finished STEPs as FLAT single-product AP214 files (no assembly wrapper).

build123d's export_step writes the solid as a sub-product under an assembly node
(NEXT_ASSEMBLY_USAGE_OCCURRENCE). NX then files the body into a separate SOLID.prt
component and the opened part shows no solid body. This writer uses the plain
STEPControl_Writer, so the ADVANCED_BREP_SHAPE_REPRESENTATION belongs to the one
product and NX / SolidWorks / FreeCAD open it as a single part with one solid body.

IN : argv[1] dir with OD-H24_flowmeter_scanframe.step and OD-H24_flowmeter.step (build123d export)
OUT: the same file names overwritten in place (flat) + flat_check.json
"""

import json
import sys
from pathlib import Path

from OCP.BRepCheck import BRepCheck_Analyzer
from OCP.IFSelect import IFSelect_RetDone
from OCP.Interface import Interface_Static
from OCP.ShapeFix import ShapeFix_Shape
from OCP.STEPControl import STEPControl_AsIs, STEPControl_Reader, STEPControl_Writer
from OCP.TopAbs import TopAbs_FACE, TopAbs_SOLID
from OCP.TopExp import TopExp_Explorer


def read(path):
    r = STEPControl_Reader()
    if r.ReadFile(str(path)) != IFSelect_RetDone:
        raise SystemExit(f"cannot read {path}")
    r.TransferRoots()
    return r.OneShape()


def count(shape, kind):
    e = TopExp_Explorer(shape, kind)
    n = 0
    while e.More():
        n += 1
        e.Next()
    return n


def first_solid(shape):
    e = TopExp_Explorer(shape, TopAbs_SOLID)
    if not e.More():
        raise SystemExit("no solid in shape")
    s = e.Current()
    e.Next()
    if e.More():
        raise SystemExit("more than one solid")
    return s


def write_flat(solid, path, name):
    Interface_Static.SetCVal_s("write.step.schema", "AP214IS")
    Interface_Static.SetCVal_s("write.step.unit", "MM")
    Interface_Static.SetCVal_s("write.step.product.name", name)
    w = STEPControl_Writer()
    if w.Transfer(solid, STEPControl_AsIs) != IFSelect_RetDone or w.Write(str(path)) != IFSelect_RetDone:
        raise SystemExit(f"write failed {path}")


def main():
    d = Path(sys.argv[1])
    rep = {}
    for fn in ("OD-H24_flowmeter_scanframe.step", "OD-H24_flowmeter.step"):
        p = d / fn
        solid = first_solid(read(p))
        fix = ShapeFix_Shape(solid)
        fix.Perform()
        solid = first_solid(fix.Shape())
        write_flat(solid, p, "OD-H24 Flowmeter")
        back = read(p)
        txt = p.read_text(errors="ignore")
        rep[fn] = dict(
            solids=count(back, TopAbs_SOLID), faces=count(back, TopAbs_FACE),
            valid=bool(BRepCheck_Analyzer(back).IsValid()),
            PRODUCT=txt.count("PRODUCT("), NEXT_ASSEMBLY_USAGE_OCCURRENCE=txt.count("NEXT_ASSEMBLY_USAGE_OCCURRENCE"),
            MANIFOLD_SOLID_BREP=txt.count("MANIFOLD_SOLID_BREP("), CLOSED_SHELL=txt.count("CLOSED_SHELL("),
            BREP_WITH_VOIDS=txt.count("BREP_WITH_VOIDS"), size_MB=round(p.stat().st_size / 1e6, 2))
        print(fn, rep[fn])
    json.dump(rep, open(d / "flat_check.json", "w"), indent=2)


if __name__ == "__main__":
    main()
