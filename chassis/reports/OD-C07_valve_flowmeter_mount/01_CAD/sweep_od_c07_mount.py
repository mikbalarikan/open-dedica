"""D7 sweep of od_c07_mount v01: rebuild at the low and high end of every fit-critical parameter
(DESIGN_PLAN §4 "Fit" rows) into 01_CAD/sweep_v01/<run>/ and run the same check script on each.
Nominal is the delivered v01 (01_CAD/check_out_v01/check_v01.json)."""
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
REPO = Path("/home/claude/oguz-atolye")
RUNS = {
    "foot_hole_d": (["foot_hole_d=3.3"], ["foot_hole_d=3.5"]),
    "ped_top_z": (["ped_top_z=9.9"], ["ped_top_z=10.1"]),
    "ring_ri": (["ring_ri=16.25"], ["ring_ri=16.35"]),
    "pin1_d": (["pin1_d=4.7"], ["pin1_d=4.9"]),
    "pin2_d": (["pin2_d=3.7"], ["pin2_d=3.9"]),
    "hook_ri": (["hook_ri=20.77", "catch_reach=1.9"], ["hook_ri=20.97", "catch_reach=2.1"]),   # catch R held at 18.87
    "hook_t": (["hook_t=1.9"], ["hook_t=2.1"]),
    "catch_under_z": (["catch_under_z=29.8"], ["catch_under_z=30.0"]),
    "catch_ri": (["catch_reach=1.9"], ["catch_reach=2.1"]),                                     # catch R 18.97 / 18.77
    "leg_gap_half": (["leg_gap_half=21.9"], ["leg_gap_half=22.1"]),
    "deck_top_z": (["deck_top_z=47.9"], ["deck_top_z=48.1"]),
    "deck_t": (["deck_t=7.6"], ["deck_t=7.8"]),
    "slot_w": (["slot_w=14.0"], ["slot_w=14.2"]),
    "slit_w": (["slit_w=2.3"], ["slit_w=2.5"]),
    "slit_x_top": (["slit_x_top=11.75"], ["slit_x_top=11.95"]),
    "screw_dx": (["screw_dx=15.347,-15.438"], ["screw_dx=15.547,-15.238"]),                    # both holes shifted -0.1 / +0.1 in x
    "screw_clear_d": (["screw_clear_d=3.3"], ["screw_clear_d=3.5"]),
    "insert_d": (["insert_d=3.95"], ["insert_d=4.05"]),
    "recess_r": (["recess_r=14.0"], ["recess_r=14.2"]),
    "recess_depth": (["recess_depth=0.55"], ["recess_depth=0.65"]),
}


def one(job):
    name, sets = job
    d = f"01_CAD/sweep_v01/{name}"
    args = sum((["--set", s] for s in sets), [])
    env = dict(os.environ)
    log = WS / d / "run.log"
    (WS / d).mkdir(parents=True, exist_ok=True)
    with open(log, "w") as fh:
        b = subprocess.run(["uv", "run", "tools/run.py", "python", str(HERE / "build_od_c07_mount.py"), "--outdir", d,
                            "--no-assembly", *args], cwd=REPO, env=env, stdout=fh, stderr=subprocess.STDOUT)
        if b.returncode != 0:
            return name, "BUILD FAILED"
        c = subprocess.run(["uv", "run", "tools/run.py", "python", str(HERE / "check_od_c07_mount.py"),
                            "--step", f"{d}/od_c07_mount_C1_v01.step", "--stl", f"{d}/od_c07_mount_C1_v01.stl",
                            "--out", f"{d}/check.json", *args], cwd=REPO, env=env, stdout=fh, stderr=subprocess.STDOUT)
    return name, "ok" if c.returncode == 0 else "CHECK FAILED"


if __name__ == "__main__":
    jobs = [(f"{k}_low", v[0]) for k, v in RUNS.items()] + [(f"{k}_high", v[1]) for k, v in RUNS.items()]
    only = sys.argv[1:]
    if only:
        jobs = [j for j in jobs if j[0] in only]
    with ThreadPoolExecutor(max_workers=4) as ex:
        for name, status in ex.map(one, jobs):
            print(name, status, flush=True)
