# LangYA.wang
# @Time : 2026/1/17 10:44
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject
import random
import time
import os
import multiprocessing

def func1(qu):
    while True:
        num = random.randint(1,50)
        qu.put(num)
        print(f"进程{os.getpid}向队列放入了{num}")
        time.sleep(1)

def func2(qu):
    while True:
        num = qu.get()
        print(f"进程{os.getpid}从队列取出了{num}")
        time.sleep(1)

if __name__ == '__main__':
    # qu = multiprocessing.Queue()
    # p1 = multiprocessing.Process(target=func1, args=(qu,))
    # p2 = multiprocessing.Process(target=func2, args=(qu,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    qu = multiprocessing.Manager().Queue()
    pool = multiprocessing.Pool(2)
    pool.apply_async(func1, args=(qu,))
    pool.apply_async(func2, args=(qu,))
    pool.close()
    pool.join()