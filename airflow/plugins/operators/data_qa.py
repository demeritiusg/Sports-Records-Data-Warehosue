import logging
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator

class DataQAOperator(BaseOperator):
