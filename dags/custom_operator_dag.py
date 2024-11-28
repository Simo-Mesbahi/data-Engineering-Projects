from airflow import DAG
from plugins.plugin import CustomOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='custom_operator_dag',
    default_args=default_args,
    description='A DAG with a custom operator',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    custom_task = CustomOperator(
        task_id='custom_task',
        custom_message="Hello from Custom Operator!"
    )
