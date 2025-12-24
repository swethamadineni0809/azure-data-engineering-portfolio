
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

## Environment Configuration

This project uses environment variables for configuration.

Create a `.env` file in the project root using the template below:

```bash
cp .env.example .env


---

## Project Status

## Project Status

🚧 **In Progress – Core Data Ingestion Completed**

### ✅ Completed
- Azure project and resource setup
- Secure configuration using environment variables (`.env`, `.env.example`)
- Python-based ingestion from OpenWeather API
- Support for ingesting data for multiple cities
- Valid JSON files written to Azure Data Lake Gen2 (raw zone)
- Partitioned raw data storage using date-based folders
- No hardcoded values (fully configuration-driven ingestion)

### 🔄 In Progress
- Raw data querying and exploration layer
- SQL-based schema-on-read access to raw data
- Data modeling and transformations using dbt

### ⏭️ Planned
- dbt staging models to clean and standardize raw data
- Analytics-ready fact and dimension tables
- Incremental transformations
- Data quality tests using dbt
- Workflow orchestration using Apache Airflow
- Documentation of production considerations and improvements

This project is being developed incrementally to reflect real-world
data engineering practices, with a focus on clean architecture,
configurability, and production readiness.


