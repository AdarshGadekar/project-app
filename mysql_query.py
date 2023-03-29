import streamlit as s
import pandas as pd
from connection import mysql_db

def mysql_query():
    try :
        query = s.text_input("Enter SQL Query")

        if query:
            with mysql_db.conn.cursor() as cursor: 
                cursor.execute(query)
                columns = [i[0] for i in cursor.description]
                result = cursor.fetchall()
                df = pd.DataFrame(result, columns=columns)
                s.dataframe(df)
                cursor.close()
    except Exception as e:
        s.error("Unable to load! Connect to database.")