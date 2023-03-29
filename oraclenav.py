import streamlit as s
import pandas as pd
import cx_Oracle as oracle
from connection import oracle_db
def database_navigator():
    try:

        with oracle_db.conn.cursor() as cursor: 

            # list tables
            cursor.execute("SELECT table_name FROM user_tables")
            tables = [i[0] for i in cursor.fetchall()]

            s.title('Database Navigator')
            selected_table = s.selectbox('Select a table', tables)

            #data 
            cursor.execute(f"SELECT * FROM {selected_table}")
            data = cursor.fetchall()

            if len(data) > 0:
                s.write(f'Data in table {selected_table}:')
                df = pd.DataFrame(data, columns=[j[0] for j in cursor.description])
                s.write(df)
            else:
                s.write(f'No data found in table {selected_table}')

    except Exception as e:
        s.info("Unable to load! Connect to database🚨")
