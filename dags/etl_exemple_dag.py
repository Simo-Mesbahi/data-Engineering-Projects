from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta
import requests
import psycopg2

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_data(**kwargs):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def transform_data(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='extract_data')
    return [{'id': item['id'], 'title': item['title']} for item in data]

def load_data_to_postgres(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='transform_data')
    conn = psycopg2.connect(
        host="postgres",
        database="airflow_db",
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS posts (id INT PRIMARY KEY, title TEXT);")
    for row in data:
        cur.execute("INSERT INTO posts (id, title) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING;", (row['id'], row['title']))
    conn.commit()
    cur.close()
    conn.close()

with DAG(
    dag_id='etl_example_dag',
    default_args=default_args,
    description='A simple ETL DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    load = PythonOperator(
        task_id='load_data_to_postgres',
        python_callable=load_data_to_postgres,
    )

    extract >> transform >> load
