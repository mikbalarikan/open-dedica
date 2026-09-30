import zipfile, re, numpy as np, struct
import xml.etree.ElementTree as ET
def read_3mf(path):
    z = zipfile.ZipFile(path)
    names = z.namelist()
    model = [n for n in names if n.lower().endswith(".model")][0]
    root = ET.fromstring(z.read(model))
    unit = root.attrib.get("unit")
    ns = {"m": root.tag.split("}")[0].strip("{")}
    objs = root.findall(".//m:object", ns)
    tris_all = []
    for o in objs:
        V = np.array([[float(v.attrib[k]) for k in "xyz"] for v in o.findall(".//m:vertex", ns)])
        T = np.array([[int(t.attrib[k]) for k in ("v1","v2","v3")] for t in o.findall(".//m:triangle", ns)])
        if len(T): tris_all.append(V[T])
    items = root.findall(".//m:build/m:item", ns)
    return {"names": names, "unit": unit, "objects": len(objs), "items": [i.attrib for i in items], "tris": np.concatenate(tris_all)}
def read_stl(path):
    b = open(path, "rb").read()
    n = struct.unpack("<I", b[80:84])[0]
    a = np.frombuffer(b[84:84+50*n], dtype=np.dtype([("n","<f4",3),("v","<f4",(3,3)),("a","<u2")]))
    return a["v"].astype(float)
def tri_key_set(tris, dec=4):
    out = set()
    for t in np.round(tris, dec):
        rows = [tuple(r) for r in t]
        i = rows.index(min(rows)); rows = rows[i:] + rows[:i]   # rotate, keep winding
        out.add(tuple(rows))
    return out
def signed_volume(tris):
    return float(np.sum(np.einsum("ij,ij->i", tris[:,0], np.cross(tris[:,1], tris[:,2]))) / 6.0)
