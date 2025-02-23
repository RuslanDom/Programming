import logging
import multiprocessing
import time
from typing import List
from multiprocessing import Pool, cpu_count

# Pool - высокоуровневый API который позволяет нагружать созданные процессы

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def task_cpu(number):
    return sum(i ** i for i in range(number))


def app_async():
    pool: multiprocessing.Pool = Pool(processes=2)  # Определяем для работы 2 процесса
    start = time.time()
    input_value: int = 1000
    # Метод для запуска функции apply бывает блокирующий и неблокирующий apply_async
    result_1 = pool.apply_async(task_cpu, args=(input_value, ))
    result_2 = pool.apply_async(task_cpu, args=(input_value, ))
    pool.close()
    pool.join()

    logger.info(result_1)
    logger.info(result_2.get(timeout=1))  # timeout нужен чтобы, если с функцией что-то случится не оказаться в заблокированном состоянии

    end = time.time()
    logger.info(f"Time taken in sec (Время затрачено в сек): {end - start}")


def map_async():
    pool: multiprocessing.Pool = Pool(processes=2)
    start = time.time()
    input_value: List[int] = [1000, 1000]
    # Метод для запуска функции map бывает блокирующий и неблокирующий map_async
    result_1 = pool.map_async(task_cpu, input_value)
    result_2 = pool.map_async(task_cpu, input_value)
    pool.close()
    pool.join()

    logger.info(result_1)
    logger.info(result_2.get(timeout=1))

    end = time.time()
    logger.info(f"Time taken in sec (Время затрачено в сек): {end - start}")

"""
Загрузка всех процессоров с использованием контекст-менеджера
"""
def high_load_map():
    start = time.time()
    # input_value = [i * 1000 for i in range(1, 12)]
    input_value = [i for i in range(1, 1000, 100)]

    with Pool(processes=cpu_count()) as pool:
        result = pool.map(task_cpu, input_value)

    end = time.time()
    logger.info(f"Time taken in sec (Время затрачено в сек): {end - start}")
    logger.info(len(result))  # Сколько раз запускались процессы в пуле


if __name__ == '__main__':
    app_async()
    # map_async()
    # high_load_map()