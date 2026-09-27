# Initial Data Dictionary

## Target canonical sales grain
`date x store_id x item_id`

## Canonical fields
| Field | Type | Description |
|---|---|---|
| date | date | Business date |
| store_id | string | Retail store identifier |
| state_id | string | U.S. state identifier |
| item_id | string | Product/SKU identifier |
| category_id | string | Product category |
| department_id | string | Product department |
| units_sold | numeric | Daily unit demand |
| sell_price | numeric | Selling price |
| event_name | string | Calendar/holiday event |
| event_type | string | Event class |
| cpi | numeric | CPI macro indicator |
| unemployment_rate | numeric | U.S. unemployment rate |
| retail_market_sales | numeric | U.S. retail market benchmark |
| consumer_sentiment | numeric | Consumer sentiment indicator |
| temp_avg | numeric | Daily average temperature |
| precipitation | numeric | Daily precipitation |
| snowfall | numeric | Daily snowfall |
| news_volume | integer | Number of relevant news records |
| news_tone | numeric | Aggregated daily GDELT tone/sentiment proxy |
