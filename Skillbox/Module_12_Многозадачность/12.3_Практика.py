"""Найдите сумму всех факториалов до числа 100 000 включительно.
Определите, при каком количестве процессов (или потоков) это можно выполнить быстрее всего.
Чтобы найти факториал числа, можете воспользоваться функцией factorial модуля math."""
import multiprocessing
import threading
from multiprocessing.pool import ThreadPool
import time
import logging
from typing import List
from math import factorial

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

N = 100


def factorial_sum(n):
    return sum(map(lambda e: factorial(e), [i for i in range(1, N)]))





def solve_thread():
    start = time.time()
    # threads: List[threading.Thread] = []
    # for _ in range(1):
    #     thread = threading.Thread(target=factorial_sum, args=(N, ))
    #     thread.start()
    #     threads.append(thread)
    #
    # for t in threads:
    #     t.join()

    with ThreadPool(processes=5) as pool:
        thread = pool.apply_async(factorial_sum, args=(N, ))
        # Число 1000000 можно записать в экспоненциальной форме как 1 x 10 ^ 6 или 1e+6. 9.4279e+155
        # Число 0, 000001 можно записать в экспоненциальной форме 1 x 10 ^ -6 или 1e-6.
        print("{:.1e}".format(thread.get()))  # 2e = 9.43e+155, 4e = 9.4279e+155
    end = time.time()
    logger.info("Время выполнения в потоковой обработке: {}".format(end - start))


def solve_process():
    start = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.apply_async(factorial_sum, args=(N, ))
    end = time.time()
    logger.info("Время выполнения в многопроцессной обработке: {}".format(end - start))


if __name__ == "__main__":
    solve_thread()
    solve_process()

