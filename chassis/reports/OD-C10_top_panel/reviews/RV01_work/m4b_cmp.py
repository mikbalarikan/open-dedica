import numpy as np, trimesh, sys
a = trimesh.load(sys.argv[1], process=False); b = trimesh.load(sys.argv[2], process=False)
def key(m): return sorted(tuple(sorted(map(tuple, np.round(t, 5)))) for t in m.vertices[m.faces])
ka, kb = key(a), key(b)
print(len(ka), len(kb), ka == kb, float(np.abs(np.array(ka) - np.array(kb)).max()) if len(ka) == len(kb) else None)
print(open(sys.argv[1], 'rb').read(80)); print(open(sys.argv[2], 'rb').read(80))
