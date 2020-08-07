from airflow import DAG
from airflow.operators import (DataQAOperator, DataPullOperator, FactTableLoadOperator, DimTableLoadOperator, StageOperator)
from datetime import datetime, timedelta

run_date = datetime.today() - timedelta(days - 1)

default_args = {
	'owner': 'demeritiusg',
	'start_date': run_date,
	'depends_on_past': False,
	'email_on_retry': False,
	'retries': 3,
	'retry_delay':timedelta(minutes=5)
}

dag = DAG('redshift_etl_pipeline'.
	default_args=default_args,
	description='Load and transform in Redshift using Airflow',
	schedule_interval='0 * * * *',
	catchup=False
	)

# grab data from data source
T1 = DataPullOperator()

# clean data
T2 = DataQAOperator()

# create fact table
T3 = FactTableLoadOperator()

# create dim table
T4 = DimTableLoadOperator()

# load staging table
T5 = StageOperator()
