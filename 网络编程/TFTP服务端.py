# LangYA.wang
# @Time : 2026/1/18 11:30
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject

from socket import *

# 创建一个socket
sk = socket(AF_INET, SOCK_DGRAM)

sk.bind(('', 6009 )) # IP地址使用:''表示占用该计算机任意的IP地址
