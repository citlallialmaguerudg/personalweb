#!/usr/bin/env python3
"""Verifica que todos los campos {es, en} de data.js esten traducidos.
Reporta: (1) campos EN faltantes/vacios, (2) campos EN identicos al ES
(posible traduccion pendiente). Uso: python3 check_translations.py [ruta_data.js]
"""
import re, json, sys

path = sys.argv[1] if len(sys.argv) > 1 else "data.js"
txt = open(path, "r", encoding="utf-8").read()
start = txt.index("window.DATA")
brace = txt.index("{", start)
end = txt.rindex("}")
data = json.loads(txt[brace:end + 1])

missing, equal = [], []

def walk(node, p):
    if isinstance(node, dict):
        if "es" in node and "en" in node and isinstance(node["es"], (str, list)):
            es, en = node["es"], node["en"]
            if en is None or (isinstance(en, str) and not en.strip()):
                missing.append((p, es))
            elif es == en and isinstance(es, str) and es.strip():
                equal.append((p, es))
        for k, v in node.items():
            walk(v, f"{p}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, f"{p}[{i}]")

walk(data, "DATA")
print(f"FALTANTES/VACIOS en EN: {len(missing)}")
for p, es in missing:
    s = es if isinstance(es, str) else " | ".join(es)
    print("  -", p, "=>", s[:80])
print(f"\nEN IDENTICO A ES (revisar): {len(equal)}")
for p, es in equal:
    print("  -", p, "=>", es[:90])
sys.exit(1 if missing else 0)
