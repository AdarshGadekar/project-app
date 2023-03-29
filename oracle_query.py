import streamlit as s
import cx_Oracle
import pandas as pd
from connection import oracle_db

def oracle_query():
    try :
                
        query = s.text_input("Enter Query")
        if query:
            with oracle_db.conn.cursor() as cursor:
                cursor.execute(query)
                columns = [desc[0] for desc in cursor.description]
                result = cursor.fetchall()
                df = pd.DataFrame(result, columns=columns)
                s.dataframe(df)
    except Exception as e:
        s.error(e)
