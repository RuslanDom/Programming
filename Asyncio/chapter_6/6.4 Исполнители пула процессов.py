import asyncio
import functools
import time
from asyncio import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from typing import List


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f'Закончен подсчёт до {count_to} за время: {end - start}')
    return counter

# Последовательное выполнение

def without_async():
    print("Последовательное выполнение")
    with ProcessPoolExecutor() as process_pool:
        numbers = [1000, 3, 5, 22, 100000000]
        for result in process_pool.map(count, numbers):
            print(result)



# Асинхронное выполнение

async def main():
    print("Конкурентное выполнение")
    with ProcessPoolExecutor() as process_pool:
        loop: AbstractEventLoop = asyncio.get_running_loop()
        numbers = [1000, 3, 5, 22, 100000000]
        # partial - частичное применение функции
        # Пример: count(77) можно определить как count_77 = functools.partial(count, 77),
        # затем просто вызвать count_77()

        calls: List[functools.partial[int]] = [functools.partial(count, num) for num in numbers]
        calls_list = []

        for call in calls:
            # в run_in_executor помещается исполнитель пула процессов и исполняемый объект
            # process_pool - это исполнитель пула процессов
            # call - здесь является исполняемым объектом
            calls_list.append(loop.run_in_executor(executor=process_pool, func=call))

        # Через as_completed() результаты будут выводиться по мере вычисления
        for res in asyncio.as_completed(calls_list, timeout=10):
            print(await res)

        # Через gather() результаты будут выведены по окончанию всех вычислений
        # results = await asyncio.gather(*calls_list)
        # for result in results:
        #     print(result)

if __name__ == "__main__":
    without_async()
    print('---------*******---------' * 5)
    asyncio.run(main())