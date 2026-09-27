# Retail Sales Data Lakehouse

Starter repository for a U.S. retail sales Lakehouse project combining retail demand, macroeconomic, market, weather and news data.

## 1. Local setup

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
cp .env.example .env
```

Fill `.env` with your API credentials. Never commit `.env` or `kaggle.json`.

## 2. Keys needed for the MVP

- FRED API key -> `FRED_API_KEY`
- NOAA Climate Data Online token -> `NOAA_TOKEN`
- Kaggle username/key only if downloading M5 programmatically

GDELT does not require an API key. X is optional.

## 3. First run

```bash
python ingestion/fred/fetch_fred.py
python ingestion/noaa/test_noaa.py
python ingestion/gdelt/test_gdelt.py
```

Then download M5:

```bash
python ingestion/m5/download_m5.py
```

If Kaggle requires competition-rule acceptance, open the M5 competition page once in the browser, accept the rules, then rerun the script.

## 4. Current repo scope

This starter pack only sets up raw-data acquisition and documentation. Spark/Delta/MinIO should be added after the data sources and join windows are validated.
