from __future__ import annotations

import json
from pathlib import Path

import requests

# Metadata endpoint for Monthly Retail Trade Survey (MRTS).
# We use this as a zero-key connectivity/schema check before selecting exact variables.
url = "https://api.census.gov/data/timeseries/eits/mrts/variables.json"

r = requests.get(url, timeout=30)
r.raise_for_status()
payload = r.json()

out_dir = Path("data/raw/census")
out_dir.mkdir(parents=True, exist_ok=True)
out = out_dir / "mrts_variables.json"
out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
print(f"Census MRTS metadata downloaded -> {out}")
