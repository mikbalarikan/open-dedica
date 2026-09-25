import json, numpy as np, trimesh
a=json.load(open('run/intake/alignment.json'))
m=trimesh.load_mesh('run/input/scan.stl'); m.apply_transform(np.array(a['matrix_4x4'])); m.export('full_aligned.stl')
