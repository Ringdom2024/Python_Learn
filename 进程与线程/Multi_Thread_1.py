# LangYA.wang
# @Time : 2026/1/17 11:12
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject
import threading
import time


def func():
    flag = 0
    while True:
        print(threading.current_thread().name,f'{flag}'*5)
        flag ^= 1
        time.sleep(0.5)

if __name__ == '__main__':
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func)
    # t3 = threading.Thread(target=func)
    t1.start()
    t2.start()
    # t3.start()