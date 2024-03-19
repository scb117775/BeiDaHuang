# -*- codeing = utf-8 -*-
# @Project :prodect
# @File    :拷机.py
# @IDE     :PyCharm
# @Author  :孙崇博
# @Date    :2024/2/21 14:19

import multiprocessing
import math
import time


def cpu_intensive_task():
    while True:
        # 执行一些计算密集型任务
        x = 4
        for _ in range(1000000):
            x += math.sqrt(x)
            print(x)



if __name__ == "__main__":
    # 获取CPU核心数
    num_cores = multiprocessing.cpu_count()
    print(f"Detected {num_cores} CPU cores.")

    # 创建与CPU核心数相等的进程数
    processes = []
    for _ in range(num_cores):
        process = multiprocessing.Process(target=cpu_intensive_task)
        process.start()
        processes.append(process)

        # 等待所有进程完成
    for process in processes:
        process.join()

    print("All processes finished.")