import sys, json
sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c03-pump-cradle/reviews/RV01_work")
from checks import load
from build123d import Pos
from tools.measure import clearance
from tools.core import common_volume
part, pump, sleeve = load()
rows=[]
for dy in (-60,-40,-30,-20,-10,-5,-3,-2,-1,-0.5,-0.1,0.0):
    pm = Pos(0,dy,0)*pump; sl = Pos(0,dy,0)*sleeve
    c = clearance(part, pm); s = clearance(part, sl)
    rows.append((dy, round(c.measured,4), c.at, round(s.measured,4)))
    print(rows[-1], flush=True)
json.dump(rows, open("path.json","w"))
