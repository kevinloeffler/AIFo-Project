# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 17:01:27 2021

@author: Benjamin Plattner
"""

from google.cloud.sql.connector import connector
import os


def query_sql_imdb(sql_query):

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
        cursor.execute(sql_query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print(e, '\n\nInvalid query, try again')
    finally:
        cursor.close()
        conn.close()
