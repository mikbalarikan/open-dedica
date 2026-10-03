import json, sys
d = json.load(open(sys.argv[1]))
def walk(o, p=""):
    if isinstance(o, dict) and "measured" in o and "status" in o:
        extra = ""
        det = o.get("detail") or {}
        for k in ("start","end","span_deg","open_ends","wide","inside","on_b","per_kind_least_deg","below_min_deg","sampling_bound_deg","gated_mm","ceilings","found","built_mm3","reimported_mm3","built","reimported"):
            if k in det: extra += f" {k}={det[k]}"
        print(f"{p}: {o['measured']} {o['unit']} at={o.get('at')} {o['status']} {o.get('reason','')[:150]}{extra}"[:600])
    elif isinstance(o, dict):
        for k, v in o.items(): walk(v, f"{p}.{k}" if p else k)
    else:
        print(f"{p}: {str(o)[:300]}")
walk({k: v for k, v in d.items() if k != "bore_census"})
if "bore_census" in d:
    for b in d["bore_census"]["detail"]["bores"]:
        print("bore", round(b["diameter"],4), [round(x,3) for x in b["start"]], [round(x,3) for x in b["end"]], round(b["span_deg"],1), b["through"], b["open_ends"])
