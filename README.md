# Data Engineering Project 2: ETL Pipeline with Airflow

## Overview

This project demonstrates a simple **ETL pipeline** (Extract, Transform, Load) implemented using **Apache Airflow**. The pipeline extracts data from a public API, transforms it, and loads it into a **PostgreSQL** database. The setup includes Docker containers for a fully isolated and reproducible environment.

---

## Features

- **ETL Pipeline**: Automates the data pipeline with Airflow.
- **Modular Setup**: Organized into well-defined directories for clarity and maintainability.
- **Custom Plugin**: Includes a custom Airflow operator to demonstrate plugin usage.
- **Containerized Environment**: Uses Docker Compose for easy deployment.
- **Scalable**: Supports adding more DAGs and tasks with minimal effort.

---

## Project Structure

Data Engineering Project 2/ ├── dags/ │ ├── etl_example_dag.py # Main ETL DAG │ └── custom_operator_dag.py # DAG using the custom operator ├── plugins/ │ └── plugin.py # Custom Airflow plugin ├── logs/ # Airflow logs (auto-generated) ├── Dockerfile # Docker configuration for custom Airflow image ├── requirements.txt # Python dependencies for Airflow ├── docker-compose.yml # Docker Compose configuration └── README.md # Project documentation
