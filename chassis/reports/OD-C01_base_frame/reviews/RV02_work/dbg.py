from pathlib import Path
from build123d import import_step, Pos, Cylinder, Solid
from tools.measure import bore_census
W = Path("/home/claude/oguz-jobs/20260930-od-c01-base-frame")
p0 = import_step(str(W/"02_STEP_STL/od_c01_frame_C1_v03.step"))
print("location", p0.location, "parent", p0.parent is not None)
part = Solid(p0.wrapped)
m = part - Pos(92,-3,77)*Cylinder(2.0, 6.4)
bc = bore_census(m)
print("bores", bc.measured)
near=[(round(b["start"][0],4), round(b["start"][2],4), round(b["diameter"],4), round(b["span_deg"],2), round(b["length"],3))
      for b in bc.detail["bores"] if abs(b["start"][0]-93)<8 and abs(b["start"][2]-77)<8]
print("near (92..95,77):", near)
mc = part.cut(Pos(92,-3,77)*Cylinder(2.0,6.4)).clean()
bc2 = bore_census(mc); print("cut+clean bores", bc2.measured)
print([ (round(b["start"][0],4), round(b["start"][2],4), round(b["diameter"],4), round(b["span_deg"],2))
      for b in bc2.detail["bores"] if abs(b["start"][0]-93)<8 and abs(b["start"][2]-77)<8])
