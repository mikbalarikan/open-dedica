import json, re, sys
S = json.load(open("/home/claude/oguz-atolye/atolye/schemas/verdict.schema.json"))
D = json.load(open(sys.argv[1]))
T = {"string": str, "boolean": bool, "array": list, "object": dict, "null": type(None)}
errs = []
def v(sch, x, path):
    if "anyOf" in sch:
        if not any(ok(s, x) for s in sch["anyOf"]): errs.append(f"{path}: anyOf")
        return
    t = sch.get("type")
    if t == "number":
        if isinstance(x, bool) or not isinstance(x, (int, float)): errs.append(f"{path}: not number"); return
    elif t and not isinstance(x, T[t]) or (t in ("string",) and isinstance(x, bool)): errs.append(f"{path}: not {t}"); return
    if "enum" in sch and x not in sch["enum"]: errs.append(f"{path}: {x!r} not in enum")
    if "pattern" in sch and not re.search(sch["pattern"], x): errs.append(f"{path}: pattern")
    if t == "object":
        for k in sch.get("required", []):
            if k not in x: errs.append(f"{path}: missing {k}")
        if sch.get("additionalProperties") is False:
            for k in x:
                if k not in sch["properties"]: errs.append(f"{path}: extra {k}")
        for k, s in sch.get("properties", {}).items():
            if k in x: v(s, x[k], f"{path}.{k}")
    if t == "array":
        for i, it in enumerate(x): v(sch["items"], it, f"{path}[{i}]")
def ok(s, x):
    n = len(errs); v(s, x, ""); good = len(errs) == n; del errs[n:]; return good
v(S, D, "$"); print("errors:", errs if errs else "none")
