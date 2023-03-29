import streamlit as s
import pandas as pd
from connection import mongo_db

def monogdb_query():
    try:
        collection_names = mongo_db.conn.list_collection_names()
        collection_name = s.selectbox("Select a collection", collection_names)
        if collection_name:
            query = s.text_input("Enter Query")
            if query:
                # Execute the query and get the results
                result = list(mongo_db.conn['mydatabase'][collection_name].find(eval(query)))

                # Convert the results to a pandas dataframe and display it
                df = pd.DataFrame(result)
                s.dataframe(df)

    except Exception as e:
        s.error("Unable to load! Connect to database.")

