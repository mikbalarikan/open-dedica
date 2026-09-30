"""D7 sweep of od_c07_mount (REPORT v02, spec 1.2): rebuild at the low and high end of every
fit-critical parameter (DESIGN_PLAN §4 "Fit" rows) into 01_CAD/sweep_<TAG>/<run>/ and run the same
check script on each. Nominal is the delivered STEP (01_CAD/check_out_v02/check_v02.json).
Spec 1.2 makes ring_ri, pin1_d, pin2_d, slot_w and slit_x_top one-sided (+0.1/-0): their low end is
the nominal value, so the low run is None (the nominal check stands for it) and only the high end is built.
The v01 sweep (two-sided bands, spec 1.1) stays on disk in 01_CAD/sweep_v01/."""
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
REPO = Path("/home/claude/oguz-atolye")
TAG = "v02"
RUNS = {
    "foot_hole_d": (["foot_hole_d=3.3"], ["foot_hole_d=3.5"]),
    "ped_top_z": (["ped_top_z=9.9"], ["ped_top_z=10.1"]),
    "ring_ri": (None, ["ring_ri=16.40"]),                    # REQ-01 [16.30, 16.40], spec 1.2
    "pin1_d": (None, ["pin1_d=4.9"]),                        # REQ-02 Ø4.8 +0.1/-0, spec 1.2
    "pin2_d": (None, ["pin2_d=3.9"]),                        # REQ-02 Ø3.8 +0.1/-0, spec 1.2
    "hook_ri": (["hook_ri=20.77", "catch_reach=1.9"], ["hook_ri=20.97", "catch_reach=2.1"]),   # catch R held at 18.87
    "hook_t": (["hook_t=1.9"], ["hook_t=2.1"]),
    "catch_under_z": (["catch_under_z=29.8"], ["catch_under_z=30.0"]),
    "catch_ri": (["catch_reach=1.9"], ["catch_reach=2.1"]),                                     # catch R 18.97 / 18.77
    "leg_gap_half": (["leg_gap_half=21.9"], ["leg_gap_half=22.1"]),
    "deck_top_z": (["deck_top_z=47.9"], ["deck_top_z=48.1"]),
    "deck_t": (["deck_t=7.6"], ["deck_t=7.8"]),
    "slot_w": (None, ["slot_w=14.2"]),                       # REQ-04 14.1 +0.1/-0, spec 1.2
    "slit_w": (["slit_w=2.3"], ["slit_w=2.5"]),
    "slit_x_top": (None, ["slit_x_top=11.95"]),              # REQ-04 11.85 +0.1/-0, spec 1.2
    "screw_dx": (["screw_dx=15.347,-15.438"], ["screw_dx=15.547,-15.238"]),                    # both holes shifted -0.1 / +0.1 in x
    "screw_clear_d": (["screw_clear_d=3.3"], ["screw_clear_d=3.5"]),
    "insert_d": (["insert_d=3.95"], ["insert_d=4.05"]),
    "recess_r": (["recess_r=14.0"], ["recess_r=14.2"]),
    "recess_depth": (["recess_depth=0.55"], ["recess_depth=0.65"]),
}


def one(job):
    name, sets = job
    d = f"01_CAD/sweep_{TAG}/{name}"
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
    jobs = [(f"{k}_low", v[0]) for k, v in RUNS.items() if v[0]] + [(f"{k}_high", v[1]) for k, v in RUNS.items() if v[1]]
    only = sys.argv[1:]
    if only:
        jobs = [j for j in jobs if j[0] in only]
    with ThreadPoolExecutor(max_workers=4) as ex:
        for name, status in ex.map(one, jobs):
            print(name, status, flush=True)
