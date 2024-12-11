import asyncio
import time


# Сопрограмма
async def coroutine_func():
    f1 = time.ctime()
    await asyncio.sleep(1)
    return f'Корутина. Время запуска {f1}'

def start_func():
    f1 = time.ctime()
    return f'Функция которая запустилась после корутины. Время запуска {f1}'

async def main():
    message = await coroutine_func()
    print(start_func())
    print(message)

asyncio.run(main())





