# LangYA.wang
# @Time : 2026/1/18 11:40
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject

from socket import *
sk = socket(AF_INET, SOCK_DGRAM)

# 定义了一个元组,指定了TFTP服务的地址和端口
sk.bind(('127.0.0.1', 6009))

'''
组装一个客户端请求的数据包，包含5个部分的数据
第一部分：操作码(int)
第二部分：文件名(str)
第三部分：分隔符
第四部分：模式（字节数据的存储和解析）octet
第五部分：分隔符
一个数据包,本质是字节数值,是由不同的Python类型生产的, 
'''