# LangYA.wang
# @Time : 2026/1/24 13:32
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='db_24')

cursor = conn.cursor()
sql = "insert into student(name,age,sex) values(%s,%s,%s)"
try:
    cursor.executemany(sql,[('王宝钏',18,'女'),('李四',21,'女'),('王五',34,'男')])
except Exception as e:
    print(e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
