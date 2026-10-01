import json, re, sys
S = json.load(open("/home/claude/oguz-atolye/atolye/schemas/verdict.schema.json"))
D = json.load(open(sys.argv[1]))
errs = []
T = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}
def chk(s, v, p):
    if "anyOf" in s:
        if not any(not _try(x, v) for x in s["anyOf"]): errs.append(f"{p}: anyOf")
        return
    t = s.get("type")
    if t == "number":
        if isinstance(v, bool) or not isinstance(v, (int, float)): errs.append(f"{p}: not number")
    elif t and not isinstance(v, T[t]) or (t in ("number",) and isinstance(v, bool)): errs.append(f"{p}: not {t}"); return
    if "enum" in s and v not in s["enum"]: errs.append(f"{p}: {v!r} not in enum")
    if "pattern" in s and not re.search(s["pattern"], v): errs.append(f"{p}: pattern")
    if t == "object":
        for k in s.get("required", []):
            if k not in v: errs.append(f"{p}.{k}: missing")
        for k in v:
            if k not in s["properties"]: errs.append(f"{p}.{k}: extra")
            else: chk(s["properties"][k], v[k], f"{p}.{k}")
    if t == "array":
        for i, x in enumerate(v): chk(s["items"], x, f"{p}[{i}]")
def _try(s, v):
    n = len(errs); chk(s, v, "?"); bad = len(errs) > n; del errs[n:]; return bad
chk(S, D, "$")
print("errors:", errs or "none")
