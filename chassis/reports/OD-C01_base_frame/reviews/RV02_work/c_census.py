import json
from pathlib import Path
from build123d import import_step, Solid, Pos, Rot, Cylinder
from tools.measure import bore_census, feature_census
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
part = Solid(import_step(str(W/"02_STEP_STL/od_c01_frame_C1_v03.step")).wrapped)
m = part - Pos(92,-3,77)*Rot(90,0,0)*Cylinder(2.0, 6.4)
bc=bore_census(m); fc=feature_census(m)
r=dict(bores=bc.measured, cylinder_faces=fc["cylinder_faces"].measured,
       concave=fc["concave_cylinders"].measured, planar=fc["plane_faces"].measured)
print(r)
json.dump(r, open(W/"reviews/RV02_work/c_census.json","w"), indent=1)
