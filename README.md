
# Azure Data Engineering Portfolio Project

## Project Overview
This project demonstrates an end-to-end Azure-based data engineering pipeline.
The goal is to ingest public data, store it in a data lake, transform it into
analytics-ready tables, and orchestrate the workflow using industry-standard tools.

The project is designed to reflect real-world data engineering practices used
in production environments.

---

## Architecture
Public APIs  
→ Python ingestion  
→ Azure Data Lake Gen2 (raw zone)  
→ Cloud Data Warehouse (to be decided)  
→ dbt transformations (staging & marts)  
→ Analytics-ready tables  

Orchestration will be handled using Apache Airflow.

---

## Tech Stack
- Cloud: Azure
- Storage: Azure Data Lake Gen2
- Ingestion: Python
- Data Warehouse: TBD (Azure Synapse or Snowflake)
- Transformations: dbt
- Orchestration: Apache Airflow
- Version Control: GitHub

---

## Data Sources
- OpenWeather API (weather data)
- Public mobility dataset (to be added)

---

## Key Features (Planned)
- Incremental data ingestion
- Dimensional data modeling
- Data quality checks using dbt tests
- Automated pipeline orchestration
- Production-oriented folder structure and documentation

---

## Project Status

## Ingestion Script
The Python script ingests weather data from OpenWeather API and uploads raw JSON files
to Azure Data Lake Gen2 (`raw/` container).  
See `ingestion/weather_api_ingest.py`.

