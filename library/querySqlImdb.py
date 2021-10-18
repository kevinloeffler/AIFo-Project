# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 17:01:27 2021

@author: Benjamin Plattner
"""

import os
import library.debug as DEBUG
from google.cloud.sql.connector import connector

def query_sql_imdb(query):

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'imdb-db_key.json'

    conn = connector.connect(
        "glass-arcana-329015:us-central1:imdb-db",
        "pg8000",
        user="postgres",
        password="imdb-project",
        db="imdb",
        enable_iam_auth=True,
    )
    conn.autocommit = True
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        if len(results) == 0:
            return 0
        else:
            return results
    except Exception as e:
        DEBUG.log(f'DB Query Error: {e}')
        return -1
    finally:
        cursor.close()
        conn.close()
