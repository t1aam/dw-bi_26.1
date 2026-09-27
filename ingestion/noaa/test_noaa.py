from __future__ import annotations

import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("NOAA_TOKEN")
if not TOKEN:
    raise RuntimeError("Missing NOAA_TOKEN in .env")

url = "https://www.ncei.noaa.gov/cdo-web/api/v2/datasets"
headers = {"token": TOKEN}
params = {"limit": 10}

r = requests.get(url, headers=headers, params=params, timeout=30)
r.raise_for_status()
payload = r.json()

out_dir = Path("data/raw/noaa")
out_dir.mkdir(parents=True, exist_ok=True)
out = out_dir / "datasets_test.json"
out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
print(f"NOAA token works. Saved test response -> {out}")
