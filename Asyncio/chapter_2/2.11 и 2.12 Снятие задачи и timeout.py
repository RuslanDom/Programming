import asyncio
from asyncio import CancelledError
from Asyncio.util import delay

# 2.11

async def main():
    long_task = asyncio.create_task(delay(5))
    second_elapsed = 0
    while not long_task.done():
        print('Задача не закончилась, проверка через секунду')
        await asyncio.sleep(1)
        second_elapsed += 1
        if second_elapsed == 3:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print("Задача была снята!")


# 2.12 Задание таймаута с помощью wait for

async def main_2():
    delay_task = asyncio.create_task(delay(3))
    try:
        result = await asyncio.wait_for(delay_task, timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("Таймаут")
        print(f"Задача была снята: {delay_task.cancelled()}")



if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(main_2())