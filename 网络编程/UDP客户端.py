# LangYA.wang
# @Time : 2026/1/18 10:36
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject

import socket

# 创建客户端socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    # 给服务端发送数据
    send_str = input('给服务端发送>>>')
    client_socket.sendto(send_str.encode('utf-8'),('10.64.7.32',6001))

    # 接受服务端的数据
    msg_data, source_addr = client_socket.recvfrom(10*1024)

    print(f"接收到了一个IP是: {source_addr[0]},端口是{source_addr[1]}的数据包")
    print(f"接收到的数据包为: {msg_data.decode('utf-8')}")

# 关闭
client_socket.close()