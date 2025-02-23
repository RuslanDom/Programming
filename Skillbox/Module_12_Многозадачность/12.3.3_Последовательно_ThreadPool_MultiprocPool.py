import multiprocessing
from multiprocessing import cpu_count
import logging
import time
import requests
from multiprocessing.pool import ThreadPool


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


"""
inputs для теста производительности
"""
INPUT_VALUE = [5000000] * 10
# INPUT_VALUE = [
#     'https://www.rambler.ru',
#     'https://en.wikipedia.org/wiki/Main_Page',
# ] * 20


"""
Задачи для теста CPU и GET-запрос
"""
def task_cpu(number: int):
    """
    CPU bound - задача
    """
    return sum(i * i for i in range(number))

def task_get_response(url):
    """
    GET request задача
    """
    resp = requests.get(url, timeout=(5, 5))
    if resp.status_code == 200:
        return len(resp.content)


"""
ФУНКЦИИ
"""
def sequential_task():
    """
    Последовательное (sequential) выполнение задач
    """
    start = time.time()
    logger.info("Запуск sequential")
    for num in INPUT_VALUE:             # [5000000, 5000000, 5000000 ...]
        task_cpu(num)                   # task_cpu(5000000)
        # task_get_response(val)
    end = time.time()
    logger.info(f"Время затраченное на выполнение последовательно: {end - start}")


def solve_with_threadpool():
    """
    Выполнение с использованием многопоточности
    """
    pool = ThreadPool(processes=cpu_count())
    logger.info("Запуск threading pool")
    start = time.time()
    result = pool.map(task_cpu, INPUT_VALUE)
    # result = pool.map(task_get_response, INPUT_VALUE)
    pool.close()
    pool.join()
    end = time.time()
    logger.info(f"Время затраченное на выполнение в многопоточности: {end - start}")


def solve_with_multiprocessing_pool():
    """
    Выполнение с использованием многопроцессности
    """
    pool = multiprocessing.Pool(processes=cpu_count())
    logger.info("Запуск multiprocessing pool")
    start = time.time()
    result = pool.map(task_cpu, INPUT_VALUE)  # добавляет в pool: task_cpu(5000000), task_cpu(5000000), task_cpu(5000000) ...
    # result = pool.map(task_get_response, INPUT_VALUE)
    pool.close()
    pool.join()
    end = time.time()
    logger.info(f"Время затраченное на выполнение в многопроцессности: {end - start}")


if __name__ == '__main__':
    sequential_task()  # Последовательно
    solve_with_threadpool()  # Многопоточность
    solve_with_multiprocessing_pool()  # Многопроцессность