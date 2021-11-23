#!/usr/bin/env python3
"""
Create a Directed Acyclic Graph (DAG) in Airflow.
"""
from datetime import timedelta
from airflow import DAG, utils

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

dag = DAG('reddit_dag', default_args=default_args, schedule_interval='@daily')

# TODO: Use PythonOperator to define tasks
