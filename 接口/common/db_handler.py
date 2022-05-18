import pymysql
from pymysql.cursors import DictCursor


class DBhandler():

    def __init__(self, host='127.0.0.1', port='3306',
                            database='test', user='root',
                            password='', charset='utf8', cursorclass=DictCursor, **kwargs):
        self.conn = pymysql.connect(host=host, port=port,
                                    database=database, user=user,
                                    password=password, charset=charset,
                                    cursorclass=cursorclass)
        self.cursor = self.conn.cursor()

    def query(self, sql, args, one=True):
        self.cursor.execute(sql, args)
        # 提交事务
        self.conn.commit()
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def close(self):
        self.conn.close()
        self.cursor.close()
