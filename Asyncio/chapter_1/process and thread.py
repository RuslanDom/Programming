from multiprocessing import Process
from threading import Thread
import time


def task_1(num: int):
    res = 0
    for i in range(1000000):
        res += i ** num
    # print(f'Задача выполнена: {res}')

def proc(i):
    p1 = Process(target=task_1, args=(i,))
    p2 = Process(target=task_1, args=(i,))
    p3 = Process(target=task_1, args=(i,))
    start_time = time.time()
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    res_time = time.time() - start_time
    print(f"Время затраченное с использованием процессов: {res_time}")

def thread(i):
    t1 = Thread(target=task_1, args=(i,))
    t2 = Thread(target=task_1, args=(i,))
    t3 = Thread(target=task_1, args=(i,))
    start_time = time.time()
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    res_time = time.time() - start_time
    print(f"Время затраченное с использованием потоков: {res_time}")

if __name__ == "__main__":
    proc(5)
    thread(5)






