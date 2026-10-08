# AWS S3 Sales Processing Project

A small learning project using AWS S3, Python, Boto3, AWS CLI, Docker, and Apache Airflow.

## What I learned

* AWS Cloud basics
* AWS S3
* AWS CLI
* Python CSV processing
* Boto3
* Reading a CSV file from S3
* Calculating total sales
* Git and GitHub
* Docker basics
* Docker Compose
* Apache Airflow basics
* Creating an Airflow DAG
* Running and triggering a pipeline with Airflow

## Project Workflow

```text
CSV file
   ↓
AWS S3
   ↓
Python + Boto3
   ↓
Process sales data
   ↓
Docker
   ↓
Apache Airflow
   ↓
Run and manage the pipeline
```

## Airflow

The Airflow part of the project contains a DAG called `sales_pipeline`.

The DAG is used to run the sales processing task and can be triggered manually through Airflow.

## Project Structure

```text
building-things/
├── process_sales.py
├── read_s3.py
├── sales.csv
├── sales_summary.csv
├── .gitignore
│
└── airflow/
    ├── docker-compose.yml
    └── dags/
        └── sales_pipeline.py
```

## Tools Used

* Python
* Boto3
* AWS CLI
* Amazon S3
* Docker
* Docker Compose
* Apache Airflow
* Git
* GitHub
