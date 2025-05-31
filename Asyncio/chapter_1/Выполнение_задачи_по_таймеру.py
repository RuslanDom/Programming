import asyncio
from asyncio import CancelledError
from random import randint



# Вариант №1
async def print_num():
    """
    Основная задача
    :return: Просто печатает случайные цифры
    """
    try:
        while True:
            print(randint(0, 9), end='')
            await asyncio.sleep(0.000000001)
    except CancelledError:
        raise

async def countdown(second):
    """
    Функция таймер после выполнения которой будет завершена основная задача
    :param second: секунды
    :return: None
    """
    await asyncio.sleep(second)


async def main():
    """
    Функция для запуска задач
    """
    # Запуск функции задачи
    task_1 = asyncio.create_task(print_num())
    # Запуск таймера
    await countdown(10)
    # Завершение выполнение задачи
    task_1.cancel()
    try:
        # Ожидание завершения задачи(обработка отмены)
        await task_1
    except CancelledError:
        pass # Игнорирование ошибки

# Вариант №2 через wat_for
async def main2():
    task = asyncio.create_task(print_num())
    try:
        await asyncio.wait_for(task, timeout=10)
    except asyncio.TimeoutError:
        pass


if __name__ == '__main__':
    # Запуска асинхронного цикла
    # asyncio.run(main())
    asyncio.run(main2())

