import gc
import os
import json
import csv
import time
import math
import logging
import requests
import numpy as np
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from configparser import ConfigParser



def _get_repo_path():
    dir_path = Path(__file__).resolve()
    repo_dir = dir_path.parents[2]
    return repo_dir

# utility functions:
def _get_creds(name):

    REPO_DIR = _get_repo_path()
    credentials_env = f"{REPO_DIR}/src/.env"
    # env
    load_dotenv(dotenv_path=credentials_env)
    creds = os.getenv(f"{name}")

    return creds


def _get_sql_query(file_name):

    REPO_DIR = _get_repo_path()
    with open(f'{REPO_DIR}/dags/sql/{file_name}.sql') as f:
        query_template = f.read()

    return query_template

def _get_sql_2_df(file_name):
    
    sql_query = _get_sql_query(file_name)
    conn= _get_db_connection()
    df = pd.read_sql(sql_query, conn)
    return df