import streamlit as s
# for mysql connection
from connection import connect_mysql as connection_mysql
from connection import connect_postgres as connection_postgre
from connection import connect_oracle as connection_oracle
from connection import connect_mongo as connection_mongodb

#for query
from mysql_query import mysql_query as mysql_q
from postgre_query import postgres_query as postgre_q
from oracle_query import oracle_query as oracle_q
from mongodb_query import monogdb_query as mongodb_q
#for databse navigator
from mysqlnav import database_navigator as mysql_dbnav
from postgrenav import database_navigator as postgres_dbnav
from oraclenav import database_navigator as oracle_dbnav
from mongonav import database_navigator as mongo_dbnav

database_type = s.selectbox("Select database type", ["MySQL", "PostgreSQL", "Oracle", "MongoDB"])
if database_type == "MySQL":
    connection_mysql()
    with s.expander("Mysql Accordiant"):

        tab1, tab2 = s.tabs(["Database Navigator", "Query Page"])

        with tab1:
                
            s.header("Mysql")
            mysql_dbnav()

        with tab2:

            s.header("Type In Query Here")
            mysql_q()
elif database_type == "PostgreSQL":
    connection_postgre()
    with s.expander("Postgre Accordiant"):

        tab1, tab2 = s.tabs(["Database Navigator", "Query Page"])

        with tab1:
            s.header("PostgreSQL")
            postgres_dbnav()

        with tab2:
            s.header("Type In Query Here")
            postgre_q()

elif database_type == "Oracle":
    connection_oracle()
    with s.expander("Oracle Accordiant"):

        tab1, tab2 = s.tabs(["Database Navigator", "Query Page"])

        with tab1:
            s.header("Oracle")
            oracle_dbnav()

        with tab2:
            s.header("Type In Query Here")
            oracle_q()
elif database_type == "MongoDB":
    connection_mongodb()
    with s.expander("Mongodb Accordiant"):

        tab1, tab2 = s.tabs(["Database Navigator", "Query Page"])

        with tab1:
            s.header("Mongodb")
            mongo_dbnav()

        with tab2:
            s.header("Type In Query Here")
            mongodb_q()    
#     mongo_dbnav()
    
# querypage.mysql_query()

# login.homepage()
