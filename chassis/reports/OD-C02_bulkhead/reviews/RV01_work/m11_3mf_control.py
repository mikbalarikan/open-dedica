import zipfile, re, struct, json
import numpy as np
J = '/home/claude/oguz-jobs/20260930-od-c02-bulkhead/'
txt = zipfile.ZipFile(J+'02_STEP_STL/od_c02_bulkhead_C1_v02.3mf').read('3D/3dmodel.model').decode()
V = np.array(re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', txt), float)
T = np.array(re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', txt), int)
b = open(J+'02_STEP_STL/od_c02_bulkhead_C1_v02.stl', 'rb').read(); n = struct.unpack('<I', b[80:84])[0]
S = np.frombuffer(b[84:], dtype=np.dtype([('n', '<3f4'), ('v', '<9f4'), ('a', '<u2')]), count=n)['v'].astype(float).reshape(n, 3, 3)
def key(tris): return set(tuple(sorted(map(tuple, np.round(t, 3)))) for t in tris)
ks = key(S); k3 = key(V[T])
V2 = V.copy(); V2[0] += 0.05; k32 = key(V2[T])
out = {"stl_tris": len(ks), "3mf_tris": len(k3), "common": len(ks & k3), "mutant_common": len(ks & k32), "mutant": "3MF vertex 0 moved 0.05 mm", "got": "FAIL" if len(ks & k32) < len(ks) else "PASS"}
open(J+'reviews/RV01_work/m11_3mf_control.json', 'w').write(json.dumps(out)); print(out)
