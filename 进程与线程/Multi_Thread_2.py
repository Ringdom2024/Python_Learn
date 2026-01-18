# LangYA.wang
# @Time : 2026/1/17 11:29
# @Author : 王一凡
# @Version : 
# @IDE : PyCharm
# @Project : PythonProject
import time
import threading

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        flag = 0
        while True:
            print(f"{self.name}:{str(flag)*5}", end="\n")
            flag = flag ^ 1  # 替换0和1
            time.sleep(0.2)

if __name__ == "__main__":
    t1 = Worker("线程1")
    t2 = Worker("线程2")
    t1.start()
    t2.start()
