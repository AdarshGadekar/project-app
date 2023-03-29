import streamlit as s
import pandas as pd
from connection import postgres_db

def postgres_query():
    try :

        query = s.text_input("Enter Query")
        if query:
            with postgres_db.conn.cursor() as cursor :
                cursor.execute(query)
                columns = [desc[0] for desc in cursor.description]
                result = cursor.fetchall()
                df = pd.DataFrame(result, columns=columns)
                s.dataframe(df)

    except Exception as e:
        s.error("Unable to load! Connect to database.")

    