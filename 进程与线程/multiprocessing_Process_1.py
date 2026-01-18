# LangYA.wang
# @Time : 2026/1/15 10:05
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject

"""
    该案例演示了使用multiprocessing.Process创建进程
    需求:同时对文件进行读写操作
"""
import multiprocessing
import time



def write_file():
    with open("test.txt","a") as f:
        while True:
            f.write('Hello World\n')
            # 手动刷新缓冲区
            f.flush()
            time.sleep(0.5)

def read_file():
    with open("test.txt","r") as f:
        while True:
            time.sleep(0.5)
            print(f.readline())


# 用前面掌握的知识,无法让这两个函数同时执行
# 需要创建两个进程,分别用来读写文件
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=write_file)
    p2 = multiprocessing.Process(target=read_file)

    p1.start()
    p2.start()