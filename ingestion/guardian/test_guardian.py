import os
import json
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GUARDIAN_API_KEY")

if not API_KEY:
    raise ValueError("GUARDIAN_API_KEY is missing from .env")

URL = "https://content.guardianapis.com/search"

params = {
    "api-key": API_KEY,
    "q": '"retail sales"',
    "section": "business",

    "from-date": "2015-01-01",
    "to-date": "2015-01-31",

    "page-size": 20,
    "order-by": "oldest",

    "show-fields": "headline,trailText,wordcount"
}

response = requests.get(
    URL,
    params=params,
    timeout=30
)

print("Status code:", response.status_code)

response.raise_for_status()

data = response.json()

results = data["response"]["results"]

print("Total matching articles:", data["response"]["total"])
print("Articles returned:", len(results))

for article in results[:5]:
    print("-" * 80)
    print("Date:", article.get("webPublicationDate"))
    print("Section:", article.get("sectionName"))
    print("Title:", article.get("webTitle"))
    print("URL:", article.get("webUrl"))


# Lưu nguyên response để làm RAW data
output_dir = Path("data/raw/guardian")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "guardian_test_2015_01_01.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nSaved raw response to:", output_file)