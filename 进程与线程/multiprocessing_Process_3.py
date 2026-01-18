import os
import multiprocessing
import time

def  func():
    for i in range(10):
        print(os.getpid(),i)
        time.sleep(2.0)

if __name__ == '__main__':
    process_num = 3
    pool = multiprocessing.Pool(process_num)
    for p in range(process_num):
        pool.apply_async(func)
    pool.close()
    pool.join()
    print(f'当前进程名称:{multiprocessing.current_process().name}:end')