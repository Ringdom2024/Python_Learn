# LangYA.wang
# @Time : 2026/1/18 10:11
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject

import socket

# 创建服务器socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 绑定ip,和端口
server_socket.bind(('192.168.2.103',6001))

while True:
    # 接受客户端的数据
    # 返回一个元组,一个是数据包,另一个是源地址
    msg_data, source_addr = server_socket.recvfrom(10*1024)

    print(f"接收到了一个IP是: {source_addr[0]},端口是{source_addr[1]}的数据包")
    print(f"接收到的数据包为: {msg_data.decode('utf-8')}")

    # 给客户端发送数据
    send_str = input('给客户端发送>>>')
    server_socket.sendto(send_str.encode('utf-8'),source_addr)


# 关闭
server_socket.close()