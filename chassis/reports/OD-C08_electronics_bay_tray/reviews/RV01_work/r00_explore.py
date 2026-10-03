import json, sys
from tools.core import read_step, validity, solids
from tools.core.step import labels, node_labels
from tools.measure import envelope, feature_census, bore_census
from build123d import *
J="/root/oguz-jobs/20261001-od-c08-electronics-bay-tray/"
t=read_step(J+"02_STEP_STL/od_c08_tray_C1_v01.step")
print(type(t), node_labels(t), labels(t))
print({k:(v.measured,v.status) for k,v in validity(t).items()})
print({k:v.measured for k,v in envelope(t).items()})
fc=feature_census(t); print({k:v.measured for k,v in fc.items()})
bc=bore_census(t); print(bc.measured, bc.status); print(json.dumps(bc.detail, default=str)[:3000])
a=read_step(J+"02_STEP_STL/od_c08_assembly_C1_v01.step")
print(node_labels(a)); 
for c in a.children: print(c.label, type(c), len(solids(c)), c.location, c.bounding_box())
