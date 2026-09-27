# Initial Architecture

Data Sources -> Batch/API Ingestion -> Raw Landing -> Bronze -> Silver -> Gold -> BI / ML

## MVP
- M5 CSV
- FRED API
- Census API
- NOAA API
- GDELT

## Later
- MinIO object storage
- Apache Spark + Delta Lake
- Streaming simulation with Redpanda/Kafka
- Streamlit dashboard
