from __future__ import annotations

import json
from pathlib import Path

import requests

# GDELT DOC 2.0 API is convenient for current/recent news testing.
# Historical 2015-2016 research data should later be sourced from GDELT bulk/BigQuery archives.
url = "https://api.gdeltproject.org/api/v2/doc/doc"
params = {
    "query": '(walmart OR retail OR "consumer spending")',
    "mode": "artlist",
    "maxrecords": 50,
    "format": "json",
}

r = requests.get(url, params=params, timeout=60)
r.raise_for_status()
payload = r.json()

out_dir = Path("data/raw/gdelt")
out_dir.mkdir(parents=True, exist_ok=True)
out = out_dir / "gdelt_recent_test.json"
out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
print(f"GDELT public API works. Saved -> {out}")
