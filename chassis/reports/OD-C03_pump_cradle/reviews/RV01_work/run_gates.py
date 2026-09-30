import json, sys
sys.path.insert(0, "/home/claude/oguz-jobs/20260930-od-c03-pump-cradle/reviews/RV01_work")
from checks import load, run, W
part, pump, sleeve = load()
G = run(part, pump, sleeve)
rows = {k: g.row() | {"reason": g.reason} for k, g in G.items()}
json.dump(rows, open(W/"reviews/RV01_work/gates_delivered.json", "w"), indent=1, default=str)
for k, r in rows.items(): print(f"{k:28s} {r['status']:13s} {r['measured']} {r['unit']} margin {r['margin']} at {r['at']} {r['reason']}")
