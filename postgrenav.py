import streamlit as s
import pandas as pd
from connection import postgres_db

def database_navigator():
        try:
            with postgres_db.conn.cursor() as cursor:
                # Show available schemas in the database
                cursor.execute("SELECT schema_name FROM information_schema.schemata")
                schemas = [schema[0] for schema in cursor.fetchall()]
                
                s.title('Database Navigator')
                selected_schema = s.selectbox('Select a schema', schemas)
                s.write(selected_schema)
                
                if selected_schema:
                    # List tables
                    try:
                        cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{selected_schema}'")
                        tables = [i[0] for i in cursor.fetchall()]
                    
                        s.write(f'Tables in schema {selected_schema}:')
                        selected_table = s.selectbox('Select a table', tables)
                        
                        # Get data from the selected table
                        cursor.execute(f"SELECT * FROM {selected_table};")
                        data = cursor.fetchall()
                        
                        if len(data) > 0:
                            s.write(f'Data in table {selected_table}:')
                            df = pd.DataFrame(data, columns=[j[0] for j in cursor.description])
                            s.write(df)

                    except Exception as e:
                        s.write('No data found in table')  
        
        except Exception as e:
            s.info("Unable to load! Connect to database🚨")