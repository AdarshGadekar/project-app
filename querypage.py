import streamlit as s 
from connection import connect_mysql
from querries import DatabaseQueries
import database 

def mysql_query():

    if s.button('Go to QueryPage') :
        db_queries = DatabaseQueries(database.conn)#conn conection object from connection mod
        s.text_input("Enter Query")
        query = s.text_input("Enter Query")
        if s.button("Execute Query"):
            result = db_queries.run_mysql_query(query)
            s.write(result)
        else :
            s.write('some error')