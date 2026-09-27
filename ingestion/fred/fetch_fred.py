from __future__ import annotations

import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FRED_API_KEY")
if not API_KEY:
    raise RuntimeError("Missing FRED_API_KEY in .env")

OUT_DIR = Path("data/raw/fred")
OUT_DIR.mkdir(parents=True, exist_ok=True)

SERIES = {
    "CPIAUCSL": "cpi_all_urban_consumers",
    "UNRATE": "unemployment_rate",
    "RSAFS": "retail_and_food_services_sales",
    "UMCSENT": "consumer_sentiment",
}

URL = "https://api.stlouisfed.org/fred/series/observations"

for series_id, name in SERIES.items():
    params = {
        "series_id": series_id,
        "api_key": API_KEY,
        "file_type": "json",
        "observation_start": "2011-01-01",
        "observation_end": "2016-06-30",
    }
    r = requests.get(URL, params=params, timeout=30)
    r.raise_for_status()
    payload = r.json()

    out = OUT_DIR / f"{series_id}_{name}.json"
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"saved {series_id} -> {out}")
