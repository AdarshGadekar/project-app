import streamlit as s
import pandas as pd
from connection import mongo_db

def database_navigator():
    selected_col_index = None
    try :
        col_names = mongo_db.conn.list_collection_names()
        selected_col = s.selectbox('Select a database', col_names)
        selected_col_index = col_names.index(selected_col)
        col = mongo_db.conn[col_names[selected_col_index]]
        
        data = list(col.find())
        if len(data) > 0:
            s.write(f'Data in collection {selected_col}:')
            df = pd.DataFrame(data)
            s.dataframe(df)
        else:
         s.write('No data found in collection')

    except Exception as e:
        s.info("Unable to load! Connect to database🚨")





