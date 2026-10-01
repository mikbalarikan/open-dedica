import json, re, sys
S = json.load(open("/home/claude/oguz-atolye/atolye/schemas/verdict.schema.json"))
D = json.load(open("/home/claude/oguz-jobs/20260930-od-c02-bulkhead/reviews/RV01_od_c02_bulkhead_v02.json"))
err = []
T = {"string": str, "boolean": bool, "array": list, "object": dict, "null": type(None)}
def check(s, v, p):
    if "anyOf" in s:
        if not any(ok(x, v) for x in s["anyOf"]): err.append(f"{p}: anyOf")
        return
    t = s.get("type")
    if t == "number":
        if not (isinstance(v, (int, float)) and not isinstance(v, bool)): err.append(f"{p}: number"); return
    elif t and not isinstance(v, T[t]): err.append(f"{p}: {t}"); return
    if t == "boolean" and not isinstance(v, bool): err.append(f"{p}: bool")
    if "enum" in s and v not in s["enum"]: err.append(f"{p}: enum {v}")
    if "pattern" in s and not re.search(s["pattern"], v): err.append(f"{p}: pattern {v}")
    if t == "object":
        for r in s.get("required", []):
            if r not in v: err.append(f"{p}: missing {r}")
        if s.get("additionalProperties") is False:
            for k in v:
                if k not in s["properties"]: err.append(f"{p}: extra {k}")
        for k, sub in s.get("properties", {}).items():
            if k in v: check(sub, v[k], f"{p}.{k}")
    if t == "array":
        for i, x in enumerate(v): check(s["items"], x, f"{p}[{i}]")
def ok(s, v):
    n = len(err); check(s, v, "?"); good = len(err) == n; del err[n:]; return good
check(S, D, "$")
# consistency rules
for g in D["gates"]:
    if g["status"] == "PASS_ASSUMED" and not g["assumes"]: err.append(f"{g['gate']}: PASS_ASSUMED without assumes")
    if g["measured"] is None and g["status"] not in ("INCONCLUSIVE", "NOT_APPLICABLE"): err.append(f"{g['gate']}: null measured")
for f in D["findings"]:
    if f["blocks"] != (f["kind"] not in ("SOFT_GATE_MISS", "OBSERVATION")): err.append(f"{f['id']}: blocks")
print("errors:", err or "none", len(D["gates"]))
