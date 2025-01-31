from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
        dag_id="test_dag",
        schedule_interval=None,
        start_date=datetime(2025, 1, 1),
        catchup=False
) as dag:
    t0 = PythonOperator(
        python_callable=lambda : print("hello world")
    )