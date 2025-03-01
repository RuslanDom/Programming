"""
Перепишите пример с очередью так, чтобы инициализация объектов происходила внутри отдельных процессов,
а вызов метода do_something — внутри основного.
"""


import os
import logging
import multiprocessing
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MySuperClass(object):

    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        proc_id = os.getpid()
        logger.info(f"Doing something for {proc_name} with pid {proc_id} for {self.name}")


def worker(_queue: multiprocessing.Queue):

    while not _queue.empty():
        obj = MySuperClass(_queue.get())  # MySuperClass(1), MySuperClass(2), ...
        obj.do_something()  # Нужно вынести вызов метода do_something — внутри основного
        time.sleep(0.1)



if __name__ == '__main__':
    # 1. Инициализация очереди
    queue = multiprocessing.Queue()  # Инициализация объекта (Queue)очереди

    # 2. Наполнение очереди объектами(задачами)
    """
        Наполнение очереди с помощью put()
    """
    for i in range(1, 20):
        queue.put(i)  # i = 1, 2, 3, ...

    # 3. Добавление в пул процессов задач на выполнение
    pool: multiprocessing.Pool = multiprocessing.Pool(
        processes=multiprocessing.cpu_count(),
        initializer=worker,  # Функция из initializer будет вызвана в каждом процессе
        initargs=(queue,)  # input для функции в initializer
    )
    print(type(pool))




    queue.close()
    queue.join_thread()

    pool.close()
    pool.join()

