import asyncio
from Asyncio.chapter_1.util import async_timer

"""ПРИМЕР НЕПРАВИЛЬНОЙ РАБОТЫ КОДА"""

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

    await task_1
    await task_2


if __name__ == "__main__":
    asyncio.run(main())

# Конкурентно не работает, а синхронно(последовательно)

# Выполняется функция <function main at 0x7592c1066700> с аргументами: () {}
# Выполняется функция <function cpu_bound_work at 0x7592c1a86c00> с аргументами: () {}
# Время работы кода: 0.34179234504699707
# Выполняется функция <function cpu_bound_work at 0x7592c1a86c00> с аргументами: () {}
# Время работы кода: 0.3503403663635254
# Время работы кода: 0.6922731399536133