# Retail Sales Lakehouse - Data Sources

## Data backbone

The project uses the U.S. retail market because public retail, macroeconomic, weather, and news data are abundant and well documented.

### DS01 - Walmart M5
- Role: Core retail transaction/demand source
- Type: Structured CSV
- Grain: Date x Store x Item
- Main files: `sales_train_evaluation.csv`, `sell_prices.csv`, `calendar.csv`
- Core period: approximately 2011-01-29 to 2016-06-19
- Use: Sales analytics, pricing, event analysis, demand forecasting
- Authentication: Kaggle account/API credentials and acceptance of competition rules may be required

### DS02 - FRED
- Role: Macroeconomic context
- Type: REST/JSON
- Grain: Monthly or weekly series
- Core series:
  - `CPIAUCSL`: Consumer Price Index
  - `UNRATE`: Unemployment Rate
  - `RSAFS`: Retail and Food Services Sales
  - `UMCSENT`: Consumer Sentiment
- Authentication: FRED API key required

### DS03 - U.S. Census Monthly Retail Trade
- Role: Retail market benchmark
- Type: REST/JSON
- Grain: Monthly
- Use: Benchmark project sales movement against the U.S. retail market
- Authentication: Basic public API requests can be made without a key; a Census key can be added later if needed

### DS04 - NOAA Climate Data Online
- Role: Historical weather
- Type: REST/JSON
- Grain: Daily x location/station
- Coverage needed: California, Texas, Wisconsin
- Use: Temperature, precipitation, snow and extreme-weather features
- Authentication: NOAA CDO token required

### DS05 - GDELT
- Role: News and market-intelligence data
- Type: Semi-structured JSON / bulk data
- Grain: Article/event timestamp
- Useful overlap with M5: 2015-02 to 2016-06
- Use: News volume, topic counts, tone/sentiment proxies
- Authentication: No API key required for public access

### DS06 - X API (optional)
- Role: Social sentiment
- Type: REST/JSON
- Grain: Post
- Use: Current social-sentiment extension, not a core historical source
- Reason optional: Full-archive access can require paid/restricted access; it is not necessary for the MVP

## Recommended implementation order
1. M5
2. FRED
3. Census
4. NOAA
5. GDELT
6. X only if access is available

## Keys to obtain now
- `FRED_API_KEY`
- `NOAA_TOKEN`
- Kaggle API credentials (`KAGGLE_USERNAME`, `KAGGLE_KEY`) if downloading by script

GDELT does not require a key. X is optional and should not block the project.
