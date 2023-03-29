import pandas as pd

class DatabaseQueries:
    def __init__(self, conn):
        self.conn = conn
    
    def run_mysql_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        columns = [i[0] for i in cursor.description]
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=columns)
        cursor.close()
        return df

                