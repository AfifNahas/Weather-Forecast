from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from weather import run_weather_api

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

# Create the DAG instance
dag = DAG(
    'weather_etl_project',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  # Set the schedule interval
)


run_etl = PythonOperator(
    task_id='extract_api',
    python_callable=run_weather_api,
    dag=dag,
)

run_etl
