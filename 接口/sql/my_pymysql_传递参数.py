

import pymysql

# 1、建立连接
from pymysql.cursors import DictCursor

conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='',
                       charset='utf8', database='test',
                       cursorclass=DictCursor)
print(conn)
# 2、建立游标
cursor = conn.cursor()

# 3、执行sql语句
mobile = '13812340000'
# 传递参数的第一种方式：format，不要用这种方式，sql注入
# 传递参数的第二种方式：args, %s 是一个占位符，所得的值都放到后面的args里，注意args里类型是，元组、列表、字典
# cursor.execute('select * from member where mobile_phone={}'.format(mobile))
cursor.execute('select * from member where mobile_phone=%s and id=%s', args=[mobile])

# 4、获取结果
# all_data = cursor.fetchall()
# print(all_data)
one_data = cursor.fetchone()
print(one_data)

# 5、使用完后，要把游标和 连接都要关闭掉
cursor.close()
conn.close()



