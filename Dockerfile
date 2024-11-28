FROM apache/airflow:2.5.0

USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev && \
    apt-get clean

USER airflow
RUN pip install --no-cache-dir \
    requests \
    psycopg2-binary \
    pandas==1.3.5

COPY ./dags /opt/airflow/dags
COPY ./plugins /opt/airflow/plugins
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
