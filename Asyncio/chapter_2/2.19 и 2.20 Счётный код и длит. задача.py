import asyncio
from Asyncio.util import async_timer, delay
import requests

"""ПРИМЕР НЕПРАВАЛЬНОЙ РАБОТЫ КОДА"""

@async_timer()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(10000000):
        counter += 1
    return counter


@async_timer()
async def main():
    task_1 = asyncio.create_task(cpu_bound_work())
    task_2 = asyncio.create_task(cpu_bound_work())
    task_3 = asyncio.create_task(delay(3))

    await task_1
    await task_2
    await task_3



# Из-за счётных задач помещённых в цикл событий заблокировано выполнение в фоне длительной задачи

# Выполняется функция <function main at 0x7addab2667a0> с аргументами: () {}
# Выполняется функция <function cpu_bound_work at 0x7addabc86ca0> с аргументами: () {}
# Время работы кода: 0.31119561195373535
# Выполняется функция <function cpu_bound_work at 0x7addabc86ca0> с аргументами: () {}
# Время работы кода: 0.3093395233154297
# Засыпаю на 3 с
# Сон в течении 3 с
# Время работы кода: 3.6230545043945312

"""Неправильное использование блокирующего API как сопрограммы"""

@async_timer()
async def get_request():
    return requests.get('http://www.example.com').status_code

@async_timer()
async def main_2():
    task_1 = asyncio.create_task(get_request())
    task_2 = asyncio.create_task(get_request())
    task_3 = asyncio.create_task(get_request())

    await task_1
    await task_2
    await task_3

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(main_2())








