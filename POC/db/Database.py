from sqlalchemy import create_engine
import pymysql
import pandas as pd

class DB():

    DB_NAME = "besant"
    TB_NAME = "emp"
    def __init__(self, uname, pwd):

        self.__uname = uname
        self.__pwd = pwd

    def get_connection(self):

        connection = "mysql+pymysql://{}:{}@localhost:3306".format(self.__uname, self.__pwd)
        sqlEngine       = create_engine(connection  , pool_recycle=3600)
        dbConnection    = sqlEngine.connect()

        return connection

    def get_data(self, connection):

        df  = pd.read_sql(f"select * from {self.DB_NAME}.{self.TB_NAME}", connection)

        return df

