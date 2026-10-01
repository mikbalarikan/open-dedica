import json, re
S = json.load(open("/home/claude/oguz-atolye/atolye/schemas/verdict.schema.json"))
D = json.load(open("/home/claude/oguz-jobs/20260930-od-c05-group-head-carrier/reviews/RV02_od_c05_carrier_v04.json"))
errs = []
def check(node, sch, path):
    if "anyOf" in sch:
        if not any(ok(node, s) for s in sch["anyOf"]): errs.append(f"{path}: anyOf")
        return
    t = sch.get("type")
    tm = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}
    if t == "number":
        if not (isinstance(node, (int, float)) and not isinstance(node, bool)): errs.append(f"{path}: not number"); return
    elif t and not isinstance(node, tm[t]): errs.append(f"{path}: not {t}"); return
    if "enum" in sch and node not in sch["enum"]: errs.append(f"{path}: {node!r} not in enum")
    if "pattern" in sch and not re.search(sch["pattern"], node): errs.append(f"{path}: pattern {node!r}")
    if t == "object":
        for r in sch.get("required", []):
            if r not in node: errs.append(f"{path}: missing {r}")
        if sch.get("additionalProperties") is False:
            for k in node:
                if k not in sch["properties"]: errs.append(f"{path}: extra {k}")
        for k, v in node.items():
            if k in sch.get("properties", {}): check(v, sch["properties"][k], f"{path}.{k}")
    if t == "array":
        for i, v in enumerate(node): check(v, sch["items"], f"{path}[{i}]")
def ok(node, sch):
    global errs
    saved = errs; errs = []
    check(node, sch, "")
    good = not errs; errs = saved; return good
check(D, S, "$")
print("errors:", errs if errs else "none")
