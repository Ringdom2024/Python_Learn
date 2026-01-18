# LangYA.wang
# @Time : 2026/1/15 10:46
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject
"""
    该案例演示了使用multiprocessing的子类创建进程对象
"""
import os
import multiprocessing

class Worker(multiprocessing.Process):
    def run(self):
        print(f'当前进程名:{self.name},进程id:{os.getpid()},父进程id:{os.getppid()},name:{__name__}')

if __name__ == '__main__':
    #创建进程对象
    for i in range(3):
        Worker().start()
