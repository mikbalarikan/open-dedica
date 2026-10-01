import sys; sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_work")
from common import *
from mesh_lib import *
import numpy as np
from scipy.spatial import cKDTree
def match(A, B):
    # canonical rotation: start at lexicographically smallest vertex (rounded 3 dp for ordering)
    def canon(T):
        out = []
        for t in T:
            keys = [tuple(np.round(v, 3)) for v in t]
            i = keys.index(min(keys)); out.append(np.roll(t, -i, axis=0).reshape(-1))
        return np.array(out)
    a, b = canon(A), canon(B)
    tree = cKDTree(b)
    d, idx = tree.query(a)
    return float(d.max()), len(set(idx.tolist())), len(a)
st = read_stl(STL); m = read_3mf(MF3)["tris"]
print("stl->3mf maxdist, unique matched, n", match(st, m))
print("3mf->stl", match(m, st))
