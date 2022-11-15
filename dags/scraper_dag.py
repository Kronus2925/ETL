
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from hurtownia import main

default_args = {
    'owner': 'Jakub Kolsut',
    'depends_on_past': False,
    'start_date': datetime(2022, 11, 12),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'scraper_dag',
    default_args=default_args,
    description='Automate python script',
    schedule_interval=timedelta(days=1),
)


run_etl = PythonOperator(
    task_id='hurtownia',
    python_callable=main,
    dag=dag,
)

run_etl 