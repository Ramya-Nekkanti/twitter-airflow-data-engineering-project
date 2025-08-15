from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from twitter_etl import run_twitter_etl

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Define the DAG
dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='My first ETL DAG for Twitter',
    schedule=timedelta(days=1),  # run daily
    start_date=datetime(2025, 8, 14),
    catchup=False
)

# Define the PythonOperator
run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag
)

run_etl