#coding=utf-8
import pymysql
from src.config import readConfig

class MysqlHelper(object):
    # def __init__(self,host='120.78.147.9',port=3306,db='test1',user='root',passwd='123456',charset='utf8'):
    #     self.conn=pymysql.connect(host=host,port=port,db=db,user=user,passwd=passwd,charset=charset)

    def __init__(self):
        self.conn=pymysql.connect(host=readConfig.host,
                                  port=int(readConfig.port),
                                  db=readConfig.db_name,
                                  user=readConfig.user,
                                  passwd=readConfig.password,
                                  charset='utf8')

    def insert(self,sql,params):
        return self.__cud(sql,params)

    def update(self,sql,params):
        return self.__cud(sql,params)

    def delete(self,sql,params):
        return self.__cud(sql,params)

    def __cud(self,sql,params=[]):
        try:
            cs1 = self.conn.cursor()
            rows=cs1.execute(sql, params)
            self.conn.commit()
            cs1.close()
            self.conn.close()
            return rows
        except Exception as e:
            print(e)
            self.conn.rollback()

    def fetchone(self,sql,params=[]):
        try:
            cs1=self.conn.cursor()
            cs1.execute(sql,params)
            row=cs1.fetchone()
            cs1.close()
            self.conn.close()
            return row
        except Exception as e:
            print(e)

    def fetchall(self,sql,params):
        try:
            cs1=self.conn.cursor()
            cs1.execute(sql,params)
            rows=cs1.fetchall()
            cs1.close()
            self.conn.close()

            return rows
        except Exception as e:
            print(e)


# con = MysqlHelper()
# print(con)