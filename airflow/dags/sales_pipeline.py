from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def process_sales():
    print("Processing sales data...")

    with open("/opt/airflow/data/sales.csv", "r") as file:
        data = file.read()

    print(data)


with DAG(
    dag_id="sales_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    process_task = PythonOperator(
        task_id="process_sales",
        python_callable=process_sales,
    )