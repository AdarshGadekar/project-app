import streamlit as s
import pandas as pd
from connection import mysql_db

def database_navigator():
        try :
            with mysql_db.conn.cursor() as cursor:  
                cursor.execute("SHOW DATABASES")
                schemas = [schema[0] for schema in cursor.fetchall()]
                s.title('Database Navigator')
                selected_schema = s.selectbox('Select a schema', schemas)
                # s.write(selected_schema)
                if selected_schema:
                    #for table
                    cursor.execute(f"USE {selected_schema}")
                    cursor.execute("SHOW TABLES")
                    tables = [table[0] for table in cursor.fetchall()]

                    # list of tables
                    try:
                        s.write(f'Tables in schema {selected_schema}:')
                        selected_table = s.selectbox('Select a table', tables)
                        cursor.execute(f"SELECT * FROM {selected_table};")
                        data = cursor.fetchall()
                        if len(data) > 0:
                            s.write(f'Data in table {selected_table}:')
                            df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                            s.write(df)
                    except Exception as e:
                        s.write('No data found in table')
        except Exception as e:
             s.info("Unable to load! Connect to database🚨")
