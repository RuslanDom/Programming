import asyncio
from ..util import delay

# Здесь код выполняется НЕ АСИНХРОННО, а последовательно потому что не созданы задачи
async def add_one(number: int):
    return number + 1


async def hello_world():
    await delay(1)
    return "Hello world"


async def main():
    message = await hello_world()
    one_plus = await add_one(1)
    print(one_plus)
    print(message)

asyncio.run(main())
print('---***---' * 5)

async def _main():
    sleep_for_three = asyncio.create_task(delay(3))
    print("Этот код выполнился раньше")
    result = await sleep_for_three
    print(result)

asyncio.run(_main())

