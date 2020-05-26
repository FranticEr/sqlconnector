import sqlite3
import pandas
import PyQt5
import manager
from sqlalchemy import create_engine

#链接sql
#提交sqlquery
#现实查询结果
class connecter:
    input_string :str
    def __init__(self):
        print("im connecter")
    def connect_to_sqlite(self):
        print("connect to sqlite successfully")
    def submit_sql_query(self,sql_query):
        print('the sql query is "%s"'%sql_query)
    def set_sql_query(self,input_string):
        self.input_string=input_string
        print ('the input string is "%s"'%self.input_string)
    def connect(self):
        db=sqlite3.connect(manager.manager.db_address)
        cur=db.cursor()
        cur.execute("select * from job")
        print(cur.fetchall())
    def connect_2(self):
        #engine=create_engine("mssql://%s:%s@%s/%s"%(manager.manager.db_username,manager.manager.db_password,manager.manager.db_address,manager.manager.db_dbname))
        #engine=create_engine("mssql+pyodbc://newone:newone@locallhost/DESKTOP-D5ANO0I", echo=True)
        engine=create_engine("mssql+pyodbc://newone:newone@localhost/DESKTOP-D5ANO0I?driver=SQL+Server+Native+Client+10.0", echo=True)
if __name__ == "__main__":
    conn=connecter()
    conn.connect_2()
    pass