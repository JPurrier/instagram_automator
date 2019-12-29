import sqlite3
from sqlite3 import Error

class DatabaseInteractions(object):
    def create_connection(self,db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            #print(sqlite3.version_info)
        except Error as e:
            print(e)
        return conn
