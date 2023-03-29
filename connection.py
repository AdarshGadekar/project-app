
import streamlit as s

from database import Database
mysql_db = Database("MySQL")
postgres_db = Database("PostgreSQL")
oracle_db = Database("Oracle")
mongo_db = Database("MongoDB")

def connect_mysql():
        with s.form(key="MySQL database", clear_on_submit=True):
            s.write("MySQL database")
            mysql_host = s.text_input("Host")
            mysql_user = s.text_input("User")
            mysql_password = s.text_input("Password", type="password")
            button = s.form_submit_button("Connect")
            if button:
                try:
                    mysql_db.connect_mysql(mysql_host, mysql_user, mysql_password)
                    s.success("Connected successfully!")
    
                except Exception as e:
                    s.write("Could not connect:", e)
                    return None

def connect_postgres():
    with s.form(key="Postgres database", clear_on_submit=True):
        s.write("PostgresSQL database")
        postgres_host = s.text_input("Host")
        postgres_user = s.text_input("User")
        postgres_password = s.text_input("Password", type="password")
        button = s.form_submit_button("Connect")
        if button:
            try:
                postgres_db.connect_postgres(postgres_host, postgres_user, postgres_password)
                s.success("Connected successfully!")
            except Exception as e:
                s.write("Could not connect:", e)
                return None


# Function to connect to Oracle database
def connect_oracle():
    with s.form(key="Oracle database", clear_on_submit=True):
        s.write("Oracle database")
        oracle_host = s.text_input("Host")
        oracle_user = s.text_input("Username")
        oracle_password = s.text_input("Password", type="password",)
        button = s.form_submit_button("Connect")
        if button :
            try:
                oracle_db.connect_oracle(oracle_host, oracle_user, oracle_password)
                s.success("Connected successfully!")
            
            except Exception as e:
                s.write("Could not connect:", e)
                return None

def connect_mongo():
    with s.form(key="Mongo database", clear_on_submit=True):
        s.write("MongoDB")
        mongo_user = s.text_input("User")
        mongo_password = s.text_input("Enter Password", type="password")
        mongo_host = s.text_input("Host ", value="localhost")
        mongo_port = s.number_input("Port", value=27017)
        mongo_database = s.text_input("Database Name")
        button = s.form_submit_button("Connect")
        if button:
            try:
                mongo_db.connect_mongo(mongo_user, mongo_password, mongo_host, mongo_port, mongo_database)
                s.success("Connected successfully!")
            
            except Exception as e:
                s.write("Could not connect:", e)
                return None           
           