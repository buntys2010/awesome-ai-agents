#!/usr/bin/env python3
"""
Generate a consolidated catalog.json from CSV sources to power the interactive comparison UI.
- Reads data/frameworks.csv and data/computer_use.csv
- Applies maturity_overrides.json if present
- Outputs compare/catalog.json
"""
import csv, json, os

DATA_DIR = "data"
OUT_DIR = "compare"
FRAMEWORKS = os.path.join(DATA_DIR, "frameworks.csv")
COMPUTER_USE = os.path.join(DATA_DIR, "computer_use.csv")
OVERRIDES = os.path.join(DATA_DIR, "maturity_overrides.json")
CATALOG_OUT = os.path.join(OUT_DIR, "catalog.json")

os.makedirs(OUT_DIR, exist_ok=True)

def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def load_overrides():
    if not os.path.exists(OVERRIDES):
        return {}
    with open(OVERRIDES, encoding="utf-8") as f:
        data = json.load(f)
    # Map by name for quick lookup
    return {item["name"].strip(): item for item in data.get("overrides", [])}

def apply_overrides(items, overrides):
    for it in items:
        name = it.get("name", "").strip()
        if name in overrides:
            ov = overrides[name]
            if ov.get("maturity"):
                it["maturity"] = ov["maturity"]
            if ov.get("notes"):
                it["notes"] = (it.get("notes", "") + " | " + ov["notes"]).strip(" |")
    return items

def coerce_int(val):
    try:
        return int(str(val).replace(",", "").strip())
    except:
        return None

frameworks = read_csv(FRAMEWORKS)
computer_use = read_csv(COMPUTER_USE)

# Normalize keys
for row in frameworks:
    if "Stars" in row:
        row["stars"] = row.get("stars") or row["Stars"]
    if "last_commit" not in row:
        row["last_commit"] = row.get("last_update", "")
    row["stars_int"] = coerce_int(row.get("stars", "")) or 0

for row in computer_use:
    row["stars_int"] = coerce_int(row.get("stars", "")) or 0

# Apply maturity overrides
overrides = load_overrides()
frameworks = apply_overrides(frameworks, overrides)

catalog = {
    "generated_at": __import__("datetime").datetime.utcnow().isoformat() + "Z",
    "frameworks": frameworks,
    "computer_use": computer_use,
    "stats": {
        "framework_count": len(frameworks),
        "computer_use_count": len(computer_use),
        "total_stars": sum(x.get("stars_int", 0) for x in frameworks)
    }
}

with open(CATALOG_OUT, "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=2)

print(f"Wrote {CATALOG_OUT} with {len(frameworks)} frameworks and {len(computer_use)} computer-use entries")
