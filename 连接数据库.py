# LangYA.wang
# @Time : 2026/1/24 13:18
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='db_24')
cursor = conn.cursor()
sql = """
create table teacher(
    name varchar(20),
    age int,
    sex enum('男','女')
)
"""
cursor.execute(sql)

conn.commit()

cursor.close()
conn.close()