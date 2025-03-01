import queue
from datetime import datetime
import threading
import time
import requests
from multiprocessing.pool import ThreadPool
from typing import List


def write_log(name: str) -> List[str]:
    res = []
    for _ in range(20):
        time.sleep(1)
        now = int(datetime.now().timestamp())
        url = "http://127.0.0.1:8080/timestamp/{}".format(now)
        resp = requests.get(url).text
        res.append(f"Поток {name} | {now} | {resp}\n")
    return res


def write_log_2(name: str) -> None:
    for _ in range(20):
        time.sleep(1)
        now = int(datetime.now().timestamp())
        url = "http://127.0.0.1:8080/timestamp/{}".format(now)
        resp = requests.get(url).text
        with open('timestamp.log', 'a') as f:
            f.write(f"{name} | {now} | {resp}\n")



def main():
    q = queue.Queue()  # Создание очереди FIFO(first in first out)

    l = [str(i)for i in range(1, 11)]
    with ThreadPool(11) as pool:
        t = pool.map(write_log, l)
        q.put(t)
    while not q.empty():
        with open('timestamp.log', 'a') as f:
            for line in q.get():
                f.write("".join(line))

    # Способ №2
    # q = queue.Queue()  # Создание очереди FIFO(first in first out)
    # for i in range(1, 11):
    #     time.sleep(1)  # Задержка 1 сек при создании потоков
    #     t = threading.Thread(target=write_log_2, args=(i,))  # Создание потока
    #     t.start()  # Старт потока
    #     q.put(t)  # Помещение запущенного потока в очередь
    # while not q.empty():  # Выполнение цикла, до тех пор пока очередь полностью не освободится
    #     q.get()  # Получение объектов (потоков) очереди

if __name__ == '__main__':
    main()
