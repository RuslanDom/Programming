import asyncio, signal
from asyncio import AbstractEventLoop
from typing import Set


async def delay(delay_seconds:int):
    print(f"Засыпаю на {delay_seconds} с")
    await asyncio.sleep(delay_seconds)
    print(f"Сон в течении {delay_seconds} с")
    return delay_seconds


def cancel_tasks():
    print("Получен сигнал SIGNIT")
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    print(f"Снимается {len(tasks)} задач")
    [task.cancel() for task in tasks]

async def main():
    loop: AbstractEventLoop = asyncio.get_running_loop()
    loop.add_signal_handler(sig=signal.SIGINT, callback=cancel_tasks)
    await delay(10)


if __name__ == "__main__":
    asyncio.run(main())

""" Запускать с терминала   python 3.9\ Добавление\ обработчика\ сигнала\ снимающего\ все\ задачи.py """

# Ожидание завершения начатых задач

async def await_all_tasks():
    [await task for task in asyncio.all_tasks()]

async def main_2():
    loop: AbstractEventLoop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, lambda: asyncio.create_task(await_all_tasks()))

