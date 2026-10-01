import json
from pathlib import Path
from tools.core.step import read_step
from tools.drawing.write import write_sections
J = Path("/home/claude/oguz-jobs/20260930-od-c02-bulkhead"); W = J/"reviews/RV01_work/sections"
s = read_step(J/"02_STEP_STL/od_c02_bulkhead_C1_v02.step")
cuts = [("top", (65, 100, -100), "z-100_profile"), ("top", (65, 100, -200), "z-200_w1"), ("top", (65, 100, -60), "z-60_w3_topbore"),
        ("top", (65, 100, -45), "z-45_basebore"), ("top", (65, 100, -44), "z-44_w4_gable"), ("top", (65, 100, -210), "z-210_topbore"),
        ("front", (65, 212, -100), "y212_topbores"), ("front", (65, 3, -100), "y3_basebores"), ("front", (65, 150, -100), "y150_windows"),
        ("front", (65, 60, -100), "y60_w4"), ("front", (65, 100, -100), "y100_wall"), ("front", (65, 200, -100), "y200_wall"), ("front", (65, 208, -100), "y208_flange"),
        ("left", (65, 100, -100), "x65_wall"), ("left", (61, 100, -100), "x61_wetflange"), ("left", (69, 100, -100), "x69_elecflange")]
log = {}
for view, thr, tag in cuts:
    sub = W / tag
    for w in write_sections(s, sub, part="rv01_od_c02", version=2, views=(view,), through=thr):
        log[tag] = {"png": str(w.path), "sha256": w.sha256, **{k: v for k, v in w.detail.items()}, "clipped": w.checks["nothing_clipped"].measured}
(J/"reviews/RV01_work/m6_sections.json").write_text(json.dumps(log, indent=1, default=str))
for k, v in log.items(): print(k, v["plane"], v["cut_faces"], round(v["cut_area_mm2"], 3), v["clipped"])
