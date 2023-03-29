import mysql.connector
import psycopg2
import cx_Oracle
import pymongo

class Database:
    def __init__(self, db_type):
        self.name = db_type
        self.conn = None


    def mysql_con(self, host, user, password):
        #print(type(user))
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        return conn
    #postgre connection
    def postgre_con(self, host, user, password):
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password
        )
        return conn
    
    #oracle connection
    def oracle_con(self, host, user, password):
        conn = cx_Oracle.connect(user=user, password=password, dsn=host)
        return conn

    #mongodb connection
    def mongo_con(self, username, password, host, port, database):
        conn = f"mongodb://{username}:{password}@{host}:{port}/{database}"
        client = pymongo.MongoClient(conn)
        db = client[database]
        return db

    def connect_mysql(self, host, user, password):
        self.conn = self.mysql_con(host, user, password)
        if self.conn.is_connected():
            print(f"{self.name} - MySQL connection successful")
        else:
            print(f"{self.name} - MySQL connection failed")


    #connecting to postgre database
    def connect_postgres(self, host, user, password):
        self.conn = self.postgre_con(host, user, password)
        if self.conn.status == psycopg2.extensions.STATUS_READY:
            print(f"{self.name} - PostgreSQL connection successful")
        else:
            print(f"{self.name} - PostgreSQL connection failed")
    
    #connecting to oracle database
    def connect_oracle(self, host, user, password):
        self.conn = self.oracle_con(host, user, password)
        if self.conn.version:
            print(f"{self.name} - Oracle connection successful")
        else:
            print(f"{self.name} - Oracle connection failed")
            
    #connecting to mongo database
    def connect_mongo(self, username, password, host, port, database):
        self.conn = self.mongo_con(username, password, host, port, database)
        if self.conn is not None:
            print(f"{self.name} - MongoDB connection successful")

        else:
            print(f"{self.name} - MongoDB connection failed")
