#!/usr/bin/env python3
"""
Create a Directed Acyclic Graph (DAG) in Airflow.
"""
from datetime import timedelta
from airflow import DAG, utils
from airflow.operators.python import PythonOperator
from scraper import scrape
from word_cloud import make

default_args = {
    'owner': 'jla524',
    'depends_on_past': False,
    'start_date': utils.dates.days_ago(1),
    'email': ['jla524@sfu.ca'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'reddit_dag',
    default_args=default_args,
    schedule_interval='@daily'
) as dag:
    scrape_posts = PythonOperator(
        task_id='scrape_posts',
        python_callable=scrape,
        dag=dag
    )

    make_cloud = PythonOperator(
        task_id='make_cloud',
        python_callable=make,
        dag=dag
    )

    scrape_posts.set_downstream(make_cloud)
